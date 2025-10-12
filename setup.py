import os
from setuptools import find_packages, setup

DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(DIR, "VERSION"), "r") as file:
    VERSION = file.read()

with open(os.path.join(DIR, "README.rst"), "r") as file:
    LONG_DESCRIPTION = file.read()

long_description = LONG_DESCRIPTION,

setup(
    name='fhws',
    packages=find_packages(),
    include_package_data=True,
    version = VERSION,
    description='Python Client API for Forecast and Historical Weather Service ',
    author='Gabriel Sansigolo',
    author_email = "gabrielsansigolo@gmail.com",
    url = "https://github.com/GSansigolo/fhws",
    install_requires= [
        "xarray==2024.3.0",
        "tqdm==4.66.4",
        "numpy==1.26",
        "urllib3==2.2.2",
        "requests==2.32.3",
        "pandas==2.2.2",
        "scipy==1.13.1",
        "datetime==5.5",
        "rasterio==1.3.11",
        "rioxarray==0.17.0",
        "fsspec==2025.9.0",
        "aiohttp==3.12.15",
        "h5netcdf==1.6.4",
        "cfgrib==0.9.15.0"
    ],
    long_description = LONG_DESCRIPTION,
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
