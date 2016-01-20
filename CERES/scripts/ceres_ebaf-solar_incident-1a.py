# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:44:55 2015

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
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-solar_incident.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
solar = toa_data.variables['solar_mon'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t lw: %i\n' % \
    (timesSize, latsSize, lonsSize, solar.size))

#######################
# Create latitude profile array for a particular longitude.
#  All the latitudes are averaged for the particular longitude. 
# # # # # # # # # # # #
# Examples: 
#n = [x for x in p[::2]]
#new_array = [[array[i, j] for j in range(0, n, 10)] for i in range(0, m, 10)]

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to January. 
time = 0

solar_avg_lats_jan = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, solar_avg_lats_jan)
axis([-90, 90, -2, 1.1*amax(solar_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar Flux for January, 2014')
grid(True)
savefig("../images/CERES_TOF_solar_avg_lats-jan14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to July. 
time = 6

solar_avg_lats_jul = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, solar_avg_lats_jul)
axis([-90, 90, -2, 1.1*amax(solar_avg_lats_jul) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar Flux for July, 2014')
grid(True)
savefig("../images/CERES_TOF_solar_avg_lats-jul14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Average for all the months in a year. 
solar_avg_lats = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]

plot(lats, solar_avg_lats)
axis([-90, 90, -2, 1.1*amax(solar_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar Flux for all months in 2014')
grid(True)
savefig("../images/CERES_TOF_solar_avg_lats-2014.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# All plots. 
plot(lats, solar_avg_lats_jan, '-b', label='January')

plot(lats, solar_avg_lats_jul, '-g', label='July')

plot(lats, solar_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, -2, 1.2*amax(solar_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar Flux for Jnauary, July, and all Months in 2014', fontsize=16)
grid(True)
savefig("../images/CERES_TOF_solar_avg_lats-jan_jul_2014.png")
show()

#######################
