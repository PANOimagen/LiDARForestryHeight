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
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LiDARForestryHeight class from file LiDARForestryHeight.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LiDARForestryHeight import LiDARForestryHeight
    return LiDARForestryHeight(iface)
