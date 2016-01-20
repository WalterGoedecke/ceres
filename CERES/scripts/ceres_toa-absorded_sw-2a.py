# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:17:40 2015

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

toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-solar_incident.nc')

# Set variables.
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412.nc')

# Set variables.
sw_all = toa_data.variables['toa_sw_all_mon'][:, :, :]

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
    
absorbed_avg_lats_jan = [y-x for x, y in zip(sw_all_avg_lats_jan, solar_avg_lats_jan)]

plot(lats, absorbed_avg_lats_jan)
axis([-90, 90, -.2, 1.1*amax(absorbed_avg_lats_jan) ])

plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar TOA Absorbed SW Flux for January, 2014\n All Sky')
grid(True)
savefig("../images/CERES_TOF_absorbed_avg_lats-jan14.png")
show()

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
    
absorbed_avg_lats_jul = [y-x for x, y in zip(sw_all_avg_lats_jul, solar_avg_lats_jul)]

plot(lats, absorbed_avg_lats_jul)
axis([-90, 90, -.2, 1.1*amax(absorbed_avg_lats_jul) ])

plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar TOA Absorbed SW Flux for July, 2014\n All Sky')
grid(True)
savefig("../images/CERES_TOF_absorbed_avg_lats-jul14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Average for all the months in a year. 
sw_all_avg_lats = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
solar_avg_lats = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]

absorbed_avg_lats = [y-x for x, y in zip(sw_all_avg_lats, solar_avg_lats)]

plot(lats, absorbed_avg_lats)
axis([-90, 90, 0, 1.1*amax(absorbed_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar TOA Absorbed SW Flux for all months in 2014\n All Sky')
grid(True)
savefig("../images/CERES_TOF_absorbed_avg_lats-2014.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# All plots. 
plot(lats, absorbed_avg_lats_jan, '-b', label='January')

plot(lats, absorbed_avg_lats_jul, '-g', label='July')

plot(lats, absorbed_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, -2, 1.2*amax(absorbed_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('CERES TOA Absorbed Flux, All Sky\n January, July, and all Months in 2014', fontsize=16)
grid(True)
savefig("../images/CERES_TOF_absorbed_avg_lats-jan_jul_2014.png")
show()

#######################
