import xarray as xr

def load_xarray(filename, decode_times=False):
    ds = xr.open_dataset(filename, decode_times=decode_times)
    if '_xarray_type' in ds.attrs and ds.attrs['_xarray_type'] == 'DataArray':
        da = ds['dataarray']
        da.attrs = {k: v for k, v in ds.attrs.items() if k != '_xarray_type'}
        ds.close()
        return da
    else:
        return ds
    