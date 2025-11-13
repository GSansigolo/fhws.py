import xarray as xr

def save_xarray(ds, filename):
    if isinstance(ds, xr.DataArray):
        ds = ds.to_dataset(name='dataarray')
        ds.attrs['_xarray_type'] = 'DataArray'
    ds.to_netcdf(filename)
    print(f"xarray object saved to {filename}")