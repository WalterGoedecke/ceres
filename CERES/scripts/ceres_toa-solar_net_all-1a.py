# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:09:51 2015

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
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-net.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
net_all = toa_data.variables['toa_net_all_mon'][:, :, :]
#sw_all = toa_data.variables['sfc_net_sw_all_mon'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t lw: %i\n' % \
    (timesSize, latsSize, lonsSize, net_all.size))

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to January. 
time = 0

net_all_avg_lats_jan = [average([net_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, net_all_avg_lats_jan)
axis([-90, 90, 1.2*amin(net_all_avg_lats_jan), 1.2*amax(net_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Solar Net Flux for January, 2014')
grid(True)
savefig("../images/CERES_toa_solar_net_all_avg_lats-jan14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to July. 
time = 6

net_all_avg_lats_jul = [average([net_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, net_all_avg_lats_jul)
axis([-90, 90, 1.2*amin(net_all_avg_lats_jul), 1.2*amax(net_all_avg_lats_jul) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Solar Net Flux for July, 2014\n All Sky')
grid(True)
savefig("../images/CERES_toa_solar_net_all_avg_lats-jul14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Average for all the months in a year. 
net_all_avg_lats = [ average([[net_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]

plot(lats, net_all_avg_lats)
axis([-90, 90, 1.2*amin(net_all_avg_lats), 1.2*amax(net_all_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Solar Net Flux for all months in 2014\n All Sky')
grid(True)
savefig("../images/CERES_toa_solar_net_all_avg_lats-2014.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# All plots. 
plot(lats, net_all_avg_lats_jan, '-b', label='January')

plot(lats, net_all_avg_lats_jul, '-g', label='July')

plot(lats, net_all_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 1.2*amin(net_all_avg_lats_jul), 1.2*amax(net_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Solar Net Flux for January, July, and all Months in 2014\n All Sky', fontsize=16)
grid(True)
savefig("../images/CERES_toa_solar_net_all_avg_lats-jan_jul_2014.png")
show()

#######################
