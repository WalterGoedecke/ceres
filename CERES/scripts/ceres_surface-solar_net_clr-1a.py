# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:57:42 2015

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
toa_data = Dataset('../datasets/CERES_EBAF-Surface_Ed2.8_Subset_201401-201412.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
sw_clr = toa_data.variables['sfc_net_sw_clr_mon'][:, :, :]
#sw_all = toa_data.variables['sfc_net_sw_all_mon'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t lw: %i\n' % \
    (timesSize, latsSize, lonsSize, sw_clr.size))

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to January. 
time = 0

sw_clr_avg_lats_jan = [average([sw_clr[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, sw_clr_avg_lats_jan)
axis([-90, 90, -2, 1.1*amax(sw_clr_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Surface Solar Net Flux for January, 2014')
grid(True)
savefig("../images/CERES_sfc_solar_net_clr_avg_lats-jan14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Set time to July. 
time = 6

sw_clr_avg_lats_jul = [average([sw_clr[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

plot(lats, sw_clr_avg_lats_jul)
axis([-90, 90, -2, 1.1*amax(sw_clr_avg_lats_jul) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Surface Solar Net Flux for July, 2014\n Clear Sky')
grid(True)
savefig("../images/CERES_sfc_solar_net_clr_avg_lats-jul14.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# Average for all the months in a year. 
sw_clr_avg_lats = [ average([[sw_clr[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]

plot(lats, sw_clr_avg_lats)
axis([-90, 90, -2, 1.1*amax(sw_clr_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Surface Solar Net Flux for all months in 2014\n Clear Sky')
grid(True)
savefig("../images/CERES_sfc_solar_net_clr_avg_lats-2014.png")
show()

#######################

#######################
# Create profile & plot.
# # # # # # # # # # # #
# All plots. 
plot(lats, sw_clr_avg_lats_jan, '-b', label='January')

plot(lats, sw_clr_avg_lats_jul, '-g', label='July')

plot(lats, sw_clr_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, -2, 1.2*amax(sw_clr_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Surface Solar Net Flux for Jnauary, July, and all Months in 2014\n Clear Sky', fontsize=16)
grid(True)
savefig("../images/CERES_sfc_solar_net_clr_avg_lats-jan_jul_2014.png")
show()

#######################
