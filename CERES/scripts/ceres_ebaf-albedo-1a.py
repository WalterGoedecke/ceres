# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:08:51 2015

@author: walter
"""
from netCDF4 import Dataset #, date2index
#import numpy as np
#from numpy import * 
#import matplotlib
#import matplotlib.pyplot as plt
from pylab import *
# Add directory to path. 
import sys
sys.path.insert(0, "../modules")

import MeteoPlot

#######################
# # Import netcdf dataset.
# # # # # # # # # # # #
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-sw-22oct15.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
sw_all = toa_data.variables['toa_sw_all_mon'][:, :, :]
solar = toa_data.variables['solar_mon'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t sw_all: %i\t solar: %i\n' % \
    (timesSize, latsSize, lonsSize, sw_all.size, solar.size))

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to January. 
time = 0

sw_all_avg_lats_jan = [average([sw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
solar_avg_lats_jan = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
    
# Check if the solar incoming data so that the values are null. If so, 
#  set value to unity, and set corresponding reflected albedo value to null, 
#  so that the ratio is not unstable, but null. 
for i, x in enumerate(solar_avg_lats_jan):
    if x == 0:
        sw_all_avg_lats_jan[i] = 0
        solar_avg_lats_jan[i] = 1
    
albedo_avg_lats_jan = [x/y for x, y in zip(sw_all_avg_lats_jan, solar_avg_lats_jan)]

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to July. 
time = 6

sw_all_avg_lats_jul = [average([sw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
solar_avg_lats_jul = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
    
# Check if the solar incoming data so that the values are null. If so, 
#  set value to unity, and set corresponding reflected albedo value to null, 
#  so that the ratio is not unstable, but null. 
for i, x in enumerate(solar_avg_lats_jul):
    if x == 0:
        sw_all_avg_lats_jul[i] = 0
        solar_avg_lats_jul[i] = 1
    
albedo_avg_lats_jul = [x/y for x, y in zip(sw_all_avg_lats_jul, solar_avg_lats_jul)]

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Average for all the months in a year. 
sw_all_avg_lats = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
solar_avg_lats = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]

# Check if the solar incoming data so that the values are null. If so, 
#  set value to unity, and set corresponding reflected albedo value to null, 
#  so that the ratio is not unstable, but null. 
for i, x in enumerate(solar_avg_lats):
    if x == 0:
        sw_all_avg_lats[i] = 0
        solar_avg_lats[i] = 1
    
albedo_avg_lats = [x/y for x, y in zip(sw_all_avg_lats, solar_avg_lats)]

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# All plots. 
plot(lats, albedo_avg_lats_jan, '-b', label='January')

plot(lats, albedo_avg_lats_jul, '-g', label='July')

plot(lats, albedo_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 0, 1.2])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Ratio Flux')
title('CERES Top of Atmosphere Albedo\n January, July, and all Months in 2014', fontsize=16)
grid(True)
savefig("../images/CERES_TOF_albedo_avg_lats-jan_jul_2014.png")
show()

#######################
