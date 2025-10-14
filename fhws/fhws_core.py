import pyproj
import warnings
from shapely.geometry import box

warnings.filterwarnings("ignore", 
                       message="invalid value encountered in cast",
                       category=RuntimeWarning,
                       module="xarray.core.duck_array_ops")

warnings.filterwarnings('ignore', category=RuntimeWarning)

warnings.filterwarnings("ignore", message="Unable to import Axes3D")

cloud_dict = {
    'S2-16D-2':{
        'cloud_band': 'SCL',
        'non_cloud_values': [4,5,6],
        'cloud_values': [0,1,2,3,7,8,9,10,11]
    },
    'S2_L2A-1':{
        'cloud_band': 'SCL',
        'non_cloud_values': [4,5,6],
        'cloud_values': [0,1,2,3,7,8,9,10,11]
    },
    'LANDSAT-16D-1':{
        'cloud_band': 'qa_pixel',
        'non_cloud_values': [6,7],
        'cloud_values': [0,1,2,3,4,5]
    },
    'landsat-2':{
        'cloud_band': 'qa_pixel',
        'non_cloud_values': [6,7],
        'cloud_values': [0,1,2,3,4,5]
    },
    'AMZ1-WFI-L4-SR-1':{
        'cloud_band': 'CMASK',
        'non_cloud_values': [127],
        'cloud_values': [255, 0],
        'no_data_value': 0
    }
}

bands_dict_names = {
  "S2": {
    "B01": { "name": "coastal" },
    "B02": { "name": "blue" },
    "B03": { "name": "green" },
    "B04": { "name": "red" },
    "B05": { "name": "red-edge-1" },
    "B06": { "name": "red-edge-2" },
    "B07": { "name": "red-edge-3" },
    "B08": { "name": "nir" },
    "B8A": { "name": "narrow-nir" },
    "B09": { "name": "water-vapour" },
    "B10": { "name": "swir-cirrus" },
    "B11": { "name": "swir-1" },
    "B12": { "name": "swir-2" },
    "NDVI": { "name": "ndvi" },
    "EVI": { "name": "evi" },
    "NBR": { "name": "nbr" },
    "SCL": { "name": "scl" },
  },
 "SAMET":{
     "tmax": { "name": "tmax" },
     "tmin": { "name": "tmin" },
     "tmean": { "name": "tmean" },
     "thumbnail": { "name": "thumbnail" }
 }
}

coverage_proj = pyproj.CRS.from_wkt('''
    PROJCS["unknown",
        GEOGCS["unknown",
            DATUM["Unknown based on GRS80 ellipsoid",
                SPHEROID["GRS 1980",6378137,298.257222101,
                    AUTHORITY["EPSG","7019"]]],
            PRIMEM["Greenwich",0,
                AUTHORITY["EPSG","8901"]],
            UNIT["degree",0.0174532925199433,
                AUTHORITY["EPSG","9122"]]],
        PROJECTION["Albers_Conic_Equal_Area"],
        PARAMETER["latitude_of_center",-12],
        PARAMETER["longitude_of_center",-54],
        PARAMETER["standard_parallel_1",-2],
        PARAMETER["standard_parallel_2",-22],
        PARAMETER["false_easting",5000000],
        PARAMETER["false_northing",10000000],
        UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
        AXIS["Easting",EAST],
        AXIS["Northing",NORTH]]''')

def get_timeseries_data_cube(datacube, geom, band):
    
    if "latitude" in datacube.coords:
        band_ts = datacube.sel(latitude=geom[0]['coordinates'][0], longitude=geom[0]['coordinates'][1], method='nearest')[band].values
    elif "lat" in datacube.coords:
        band_ts = datacube.sel(lat=geom[0]['coordinates'][0], lon=geom[0]['coordinates'][1], method='nearest')[band].values
    else:
        band_ts = datacube.sel(x=geom[0]['coordinates'][0], y=geom[0]['coordinates'][1], method='nearest')[band].values
    timeline = datacube.coords['time'].values
    ts = []
    for value in band_ts:
        ts.append(value)
    return dict(values=ts, timeline=timeline)


def geometry_collides_with_bbox(geometry,input_bbox):
    """
    Check if a Shapely geometry collides with a bounding box.
    
    Args:
        geometry: A Shapely geometry object (Polygon, LineString, Point, etc.)
        bbox: A tuple in (minx, miny, maxx, maxy) format
        
    Returns:
        bool: True if the geometry intersects with the bbox, False otherwise
    """
    # Create a Polygon from the bbox
    bbox_polygon = box(*input_bbox)
    
    # Check for intersection
    return geometry.intersects(bbox_polygon)


def name_band(collection, band_id):
    standardized_name = collection.lower().replace('_', '-')
    code = standardized_name.upper().split('-')[0]
    return bands_dict_names[code][band_id]['name']