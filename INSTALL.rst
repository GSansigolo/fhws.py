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


Installation
============

``fhws.py`` depends essentially on `Requests <https://requests.readthedocs.io/en/master/>`_. Please, read the instructions below in order to install ``fhws``.


Development Installation
------------------------

Clone the Software Repository::

    git clone git@github.com:GSansigolo/fhws.git


Go to the source code folder::

    cd fhws


Install in development mode::

    pip3 install -e .[all]


.. note::

    If you want to create a new *Python Virtual Environment*, please, follow this instruction:

    *1.* Create a new virtual environment linked to Python 3.11::

        python3.11 -m venv venv


    **2.** Activate the new environment::

        source venv/bin/activate


    **3.** Update pip and setuptools::

        pip3 install --upgrade pip

        pip3 install --upgrade setuptools

Run the Tests
+++++++++++++

WIP

Build the Documentation
+++++++++++++++++++++++

WIP