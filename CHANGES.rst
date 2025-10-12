..
    This file is part of Python Client Library for FHWS.
    Copyright (C) 2025 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.


Changes
=======


0.1.0 (2025-10-15)
------------------

* **NetCDF Support**: The ``data_cube`` function can now create data cubes directly from NetCDF files.
* **GRIB2 Support**: The ``data_cube`` function can now create data cubes directly from GRIB2 files.
* **SAMeT Daily**: Added full support for SAMeT Daily data. 🛰️
* **Function Update**: Updated the ``get_timeseries_data_cube`` function to align with new NetCDF and remote file capabilities.
* **MERGE Daily**: Added full support for MERGE Daily Precipitation data. 🛰️
* **New Notebooks**: Added several example notebooks:
    * ``fhws_samet.ipynb``: An example for creating an SAMeT Daily data cube.
    * ``fhws_merge.ipynb``: An example for creating a prec Merge daily data cube.
* **COG Support**: Added support for reading Cloud Optimized GeoTIFFs (COGs) with RasterIO, allowing data cube creation without downloading the images. 🛰️
* **Initial Release**: First implementation of ``data_cube`` function.