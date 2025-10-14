import fsspec
import pyproj
import tempfile
import rasterio
import pandas as pd
import xarray as xr
from datetime import datetime
from pyproj import Transformer
from shapely.geometry import box
from pystac_client import Client
from shapely.ops import transform

from fhws.fhws_collection_get_list import collection_get_list
from fhws.fhws_core import name_band

fs = fsspec.filesystem('https')

def data_cube(stac_url, collection, start_date, end_date, tile=None, bbox=None, freq=None, bands=None):
    
    stac = Client.open(stac_url)

    collection=dict(
        collection=collection, 
        start_date=start_date,
        end_date=end_date,    
        bbox=bbox,
        bands=bands
    )
    
    if collection['collection'] not in ['landsat-2', 'LANDSAT-16D-1', 'S2-16D-2', 'S2_L2A-1', 'samet_daily-1', 'prec_merge_daily-1']:
        return print(f"{collection['collection']} collection not yet supported.")
    
    bands_dict = collection_get_list(stac, collection)
                
    bbox = tuple(map(float, collection['bbox'].split(',')))
    
    sample_image_path = bands_dict[bands[0]][0]
    
    if (collection['collection'] == "samet_daily-1" or collection['collection'] == "prec_merge_daily-1"):
        data_proj = pyproj.CRS.from_epsg(4326)
    else:
        with rasterio.open(sample_image_path) as src:
            data_proj = src.crs
        
    proj_converter = Transformer.from_crs(pyproj.CRS.from_epsg(4326), data_proj, always_xy=True).transform

    bbox_polygon = box(*bbox)
    reproj_bbox = transform(proj_converter, bbox_polygon)
    
    list_da = []

    if (collection['collection'] == "prec_merge_daily-1"): 
        data_cube = xr.Dataset()
        for i in range(len(bands)):
            for image in bands_dict[bands[i]]:
                try:
                    with tempfile.NamedTemporaryFile() as tmp:
                        fs.get(image, tmp.name)
                        ds = xr.open_dataset(tmp.name, engine='cfgrib')
                        ds_dropped = ds.drop_vars("prmsl")
                        del ds_dropped.attrs['GRIB_edition']
                        del ds_dropped.attrs['GRIB_centre']
                        del ds_dropped.attrs['GRIB_centreDescription']
                        del ds_dropped.attrs['GRIB_subCentre']
                        del ds_dropped.attrs['Conventions']
                        del ds_dropped.attrs['institution']
                        del ds_dropped.attrs['history']
                        ds_dropped = ds_dropped.drop_vars(['valid_time'])
                        ds_dropped = ds_dropped.drop_vars(['surface'])
                        ds_dropped = ds_dropped.drop_vars(['time'])
                        ds_dropped = ds_dropped.drop_vars(['step'])
                        time = image.split("/")[-1].split('.')[0].split("_")[2]
                        dt = datetime.strptime(time, '%Y%m%d') 
                        dt = pd.to_datetime(dt)
                        da = ds_dropped.assign_coords(time = dt)
                        da = da.expand_dims(dim="time")
                        list_da.append(da)
                except:
                    pass
            data_cube = xr.combine_by_coords(list_da)

    elif (collection['collection'] == "samet_daily-1"): 
        data_cube = xr.Dataset()
        for i in range(len(bands)):
            for image in bands_dict[bands[i]]:
                f = fs.open(image)
                ds = xr.open_dataset(f)
                
                min_lon, min_lat, max_lon, max_lat = map(float, collection['bbox'].split(','))
                bbox = {
                    'min_lon': min_lon,
                    'max_lon': max_lon,
                    'min_lat': min_lat,
                    'max_lat': max_lat
                }

                clipped_ds = ds.sel(
                    lon=slice(bbox['min_lon'], bbox['max_lon']),
                    lat=slice(bbox['min_lat'], bbox['max_lat'])
                )

                ds_dropped = clipped_ds.drop_vars("nobs")
                data_cube = xr.merge([data_cube, ds_dropped])
    
    else:
        for i in range(len(bands)):
            for image in bands_dict[bands[i]]:
                da = xr.open_dataarray(image, engine='rasterio')
                da = da.astype('int16')
                try:
                    da = da.rio.clip_box(*reproj_bbox.bounds)  
                    image = image.split('/')[-1]
                    if (collection['collection'] == "AMZ1-WFI-L4-SR-1" or "S2-16D-2" or "LANDSAT-16D-1" or "landsat-2"):
                        time = image.split("_")[3]
                        dt = datetime.strptime(time, '%Y%m%d') 
                    if (collection['collection'] == "S2_L2A-1"):
                        time = image.split("_")[2].split('T')[0]
                        dt = datetime.strptime(time, '%Y%m%d')
                    else:
                        time = image.split("_")[-2]
                        dt = datetime.strptime(time, '%Y%m%d') 
                    dt = pd.to_datetime(dt)
                    da = da.assign_coords(time = dt)
                    da = da.expand_dims(dim="time")
                    list_da.append(da)
                except:
                    pass
            if (i==0):
                data_cube = xr.combine_by_coords(list_da)
                data_cube = data_cube.rename({'band_data': name_band(collection['collection'], bands[i])})
            else:
                band_data_array = xr.combine_by_coords(list_da)
                band_data_array = band_data_array.rename({'band_data': name_band(collection['collection'], bands[i])})
                data_cube = xr.merge([data_cube, band_data_array])

    return data_cube
