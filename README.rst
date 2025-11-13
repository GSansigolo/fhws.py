..
    This file is part of Python Client Library for FWeather.
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

.. image:: https://raw.githubusercontent.com/GSansigolo/fweather/main/docs/img/fweather.png
   :width: 300
   :align: center
   :alt: FWeather logo

=================================================================
Python Client Library for Forecast and Weather Service 
=================================================================


.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
        :target: https://github.com/GSansigolo/fweather/blob/master/LICENSE
        :alt: Software License


.. image:: https://readthedocs.org/projects/fweather/badge/?version=latest
        :target: https://fweather.readthedocs.io/en/latest/
        :alt: Documentation Status


.. image:: https://img.shields.io/badge/lifecycle-stable-green.svg
        :target: https://www.tidyverse.org/lifecycle/#stable
        :alt: Software Life Cycle


.. image:: https://img.shields.io/github/tag/GSansigolo/fweather.svg
        :target: https://github.com/GSansigolo/fweather/releases
        :alt: Release


.. image:: https://img.shields.io/pypi/v/fweather
        :target: https://pypi.org/project/fweather/
        :alt: Python Package Index


.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord


About
=====

Forecast and historical weather data comprehend a group of data, such as Land Surface Temperature (LST), meteorological data and historical Enhanced Transparency Framework (ETF) data. These data are composed of satellite thermal bands (MODIS, AVHRR, GOES), weather models/reanalysis (ERA5, GFS) and climatology (10-20 years of previous data).

Called Forecast and Weather Service the software extracts climate data from big EO data collections. It can be (i) cumulative precipitation, (ii) precipitation - daily, (iii) temperature - daily and (iv) climate change projections, all of those as time series. The FWeather library also allow the creation of labelled multi-dimensional arrays from climate data based on INPE's data.

We created the FWeather library from scratch to facilitate climate data analysis operations. This library was developed to be interoperable with other Python libraries, thus enabling users to integrate established libraries into their own workflows for pre- or post-processing and analysis. The FWeather library has a group of functions, the main ones are:

- ``data_cube``: create multi-dimensional arrays from forecast and historical weather data as xarray.

- ``get_timeseries_data_cube``: returns in list format the climate data time series from FWeather's ``data_cube``.


Installation
============

See `INSTALL.rst <https://github.com/GSansigolo/fweather/blob/master/INSTALL.rst>`_.


Documentation
=============

See https://fweather.readthedocs.io/en/latest.


References
==========


WIP


License
=======


.. admonition::
    Copyright (C) 2025 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
