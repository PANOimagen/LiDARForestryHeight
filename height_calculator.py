# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LiDARForestryHeight
                                 A QGIS plugin. LiDAR Forestry Height 
                                 generates a DEM with the forest height, 
                                 calculated from a classified LiDAR point
                                 cloud using LasPy Library
                                 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-09-24
        copyright            : (C) 2019 by PANOimagen S.L.
        email                : info@panoimagen.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import numpy as np

def height_calc(surfaces_array, terrain_array):
    """ This function calculates the difference between two raster arrays
    """
    
    difference = surfaces_array - terrain_array
    
    return difference.astype(terrain_array.dtype)
