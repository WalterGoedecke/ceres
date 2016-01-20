# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:44:39 2015

@author: walter
"""
from netCDF4 import Dataset #, date2index
import numpy as np
from numpy import * 
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
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
#solar = toa_data.variables['solar_mon'][:, :, :]
lw_all = toa_data.variables['toa_lw_all_mon'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t lw: %i\n' % \
    (timesSize, latsSize, lonsSize, lw_all.size))

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to January. 
time = 0

lw_all_avg_lats_jan = [average([lw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, lw_all_avg_lats_jan)
axis([-90, 90, -2, 1.1*amax(lw_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Long Wave Flux for January, 2014\nAll Sky')
grid(True)
savefig("../images/CERES_TOF_lw_all_avg_lats-jan14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to July. 
time = 6

lw_all_avg_lats_jul = [average([lw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, lw_all_avg_lats_jul)
axis([-90, 90, -2, 1.1*amax(lw_all_avg_lats_jul) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Long Wave Flux for July, 2014\nAll Sky')
grid(True)
savefig("../images/CERES_TOF_lw_all_avg_lats-jul14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Average for all the months in a year. 
lw_all_avg_lats = [ average([[lw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]

plot(lats, lw_all_avg_lats)
axis([-90, 90, -2, 1.1*amax(lw_all_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Long Wave Flux for all months in 2014\nAll Sky')
grid(True)
savefig("../images/CERES_TOF_lw_all_avg_lats-2014.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# All plots. 
plot(lats, lw_all_avg_lats_jan, '-b', label='January')

plot(lats, lw_all_avg_lats_jul, '-g', label='July')

plot(lats, lw_all_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, -2, 1.2*amax(lw_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Long Wave Flux for January, July, and all Months in 2014\nAll Sky', fontsize=16)
grid(True)
savefig("../images/CERES_TOF_lw_all_avg_lats-jan_jul_2014.png")
show()

#######################
