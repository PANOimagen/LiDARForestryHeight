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
import os

def get_version_from_metadata():
    """ This function reads the plugin metadata file in txt format and returns
        the version number
    """
    try:
        path = os.path.split(os.path.abspath(__file__))[0]
        metadata_file = open(os.path.join(path, 'metadata.txt'), 'rt')
        contents = metadata_file.readlines()
        metadata_file.close()
        
        for line in contents:
            if 'version=' in line:
                lin = line.replace('version=', '')
                version = lin.replace('\n', '')
        
        return version
    
    except FileNotFoundError:
        return 'n.a.'