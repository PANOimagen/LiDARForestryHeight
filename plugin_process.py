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

from . import files_paths_funs as dir_fns
from . import laspy_funs as laspy_fns
from . import raster_funs as raster_fns
from . import height_calculator
from . import run_LASzip

class Process(object):
    
    def __init__(self, 
                 full_filename,
                 out_path, 
                 pixel_size,
                 inter_method,                 
                 partials_create_load):
        
        if not os.path.exists(full_filename):
            raise OSError(u"LiDAR Forestry Height can't open the file.\n" + 
                          u"Please try again or with other LiDAR file")
        # Check input file extension:
        _, filename = os.path.split(full_filename)
        _, ext = os.path.splitext(filename)
        if ext == '.LAZ' or ext == '.laz':
            ret, las_path = run_LASzip.run_LASzip(full_filename)
            self.laz = True
            if ret:
                self.full_filename = las_path
            else:
                return
        else:
            self.full_filename = full_filename
            self.laz = False
            
        self.out_path = out_path

        self.dirs = dir_fns.DirAndPaths(filename, out_path)
        
        # Crear directorio de salida:
        self.dirs.create_dir(self.dirs.out_dirs['height'])
        
        self.pixel_size = pixel_size
        self.inter_method = inter_method
        self.partials_create_load = partials_create_load
        
        self.laspy()
        
        self.rasterize = raster_fns.RasterizeLiDAR(self.las_file_extent, 
            self.pixel_size)
        
        self.interpolated_surface_grid = self.rasterize.interpolate_grid(
            self.surfaces_array_list)

        try:
            self.interpolated_terrain_grid = self.rasterize.interpolate_grid(
                  self.terrain_array_list)
        except ValueError:
            raise ValueError(u"Error: An error has occurred. The selected" +
                                  u" file is not valid for the process, it is" +
                                  u" possibly not classified.\nPlease, solve" +
                                  u" it and restart the process!")
            return
        
            
        self.heights()
        
        if self.partials_create_load:            
            self.dirs.create_dir(self.dirs.out_dirs['dem'])
            
            terrain__full_path = self.rasterize.array_2_raster(
                self.interpolated_terrain_grid,
                self.dirs.out_paths['dtm'])
            surface_full_path = self.rasterize.array_2_raster(
                self.interpolated_surface_grid,
                self.dirs.out_paths['dsm'])
        
    def laspy(self):
        
        lidar = laspy_fns.LiDAR(self.full_filename, 
                                     self.out_path, 
                                     self.partials_create_load)
        
        lidar_list = lidar.lidar_results
        
        self.terrain_array_list = lidar_list[0]
        self.surfaces_array_list = lidar_list[1]
        self.las_file_extent = lidar_list[-1]
        
        if self.laz:
            self.dirs.remove_temp_file(self.full_filename)
            
    def heights(self):
        
        heights_array = height_calculator.height_calc(
                self.interpolated_surface_grid,
                self.interpolated_terrain_grid)
        
        self.heights_full_path = self.rasterize.array_2_raster(
            heights_array, self.dirs.out_paths['height'])