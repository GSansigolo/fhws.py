# Create environment with Python 3.11
conda create -n fweather python=3.11 -y
conda activate fweather

# Install the packages
conda install -c conda-forge numpy -y
conda install -c conda-forge gdal -y
conda install -c conda-forge tqdm=4.66.4 -y
conda install -c conda-forge pyproj -y
conda install -c conda-forge shapely -y
conda install -c conda-forge requests=2.32.3 -y
conda install -c conda-forge rasterio=1.3.11 -y
conda install -c conda-forge xarray=2024.3.0 -y
conda install -c conda-forge urllib3=2.2.2 -y
conda install -c conda-forge pandas=2.2.2 -y
conda install -c conda-forge scipy=1.13.1 -y
conda install -c conda-forge python-dateutil -y 
conda install -c conda-forge rioxarray -y
conda install -c conda-forge fsspec=2025.9.0 -y
conda install -c conda-forge aiohttp=3.12.15 -y
conda install -c conda-forge h5netcdf=1.6.4 -y
conda install -c conda-forge cfgrib=0.9.15.0 -y
conda install -c conda-forge pystac-client -y
conda install -c conda-forge build -y
conda install -c conda-forge matplotlib -y