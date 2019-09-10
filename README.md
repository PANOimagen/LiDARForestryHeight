# LiDAR Forestry Height

QGIS minimum version = 3.0

Author = **PANOimagen S.L.**

e-mail = *info@panoimagen.com*

Plugin to generates a Digital Elevation Model (DEM) with the forest height, calculated from a classified LiDAR point cloud. This plugin uses the LasPy Library to process the point cloud (las format) and LasZip if the cloud is compressed (laz format)

Combines the ground returns and the first returns of the cloud of LiDAR classified data (ASPRS classification / *.laz, *.las formats). The result is a raster file (GeoTif).

The following image shows the heigths results of a forest area in grey scale.
![image](https://github.com/PANOimagen/LiDARForestryHeight/blob/master/icons/captura_alturas_raw.PNG?raw=true)

You can classify with a color gradient by heigths, as follow.
![image](https://github.com/PANOimagen/LiDARForestryHeight/blob/master/icons/captura_alturas.PNG?raw=true)

To use this plugin you need LasPy:

  To install LasPy Library, you must launch the following lines at OSGEO Shell (OSGeo4W.bat at QGIS installation folder):
  > By default OSGeo console runs with Python 2, you need to configure  the console to run with Python 3, so launch, from QGIS installation folder (Windows):

  >>> bin/py3_env.bat
  
  >>> bin/qt5_env.bat
  
  >>> python -m pip install laspy
    
  LasPy documentation is avaible at: *https://github.com/laspy/laspy*
  
  If the process option with the LasPy library is not activated once it has been installed, you must restart QGIS.

  If you need to process compressed LiDAR data (*.laz format), the plugin uncompress automatically the point cloud with LasZip Library:

  LasZip is LGPL License and you can found it at: *https://laszip.org/*

KeyWords = Forest, Forestry, Digital Terrain Model, DTM, Digital Elevation Model, DEM, Digital Surface Model, DSM, LiDAR, Heights, Raster, GeoTif, Python3, QGIS3

LiDAR Forestry Heights license:

    Copyright (C) 2019  by PANOimagen S.L.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

![image](https://github.com/PANOimagen/LiDARForestryHeight/blob/master/icons/PANOiFullHD.png?raw=true)
