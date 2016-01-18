# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:49:04 2015

@author: walter
"""
from netCDF4 import Dataset #, date2index
import numpy as np
from numpy import * 
import matplotlib
#import matplotlib.pyplot as plt
from pylab import *
import sys
sys.path.insert(0, "../modules")

import MeteoPlot

#######################
# Plot 1
#######################
# # Import netcdf dataset.
# # # # # # # # # # # #
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412.nc')

# Set variables.
times = toa_data.variables['time'][:]
# Set time to choice. 
time = 0
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
lw_all = toa_data.variables['toa_lw_all_mon'][time, :, :]
lw_clr = toa_data.variables['toa_lw_clr_mon'][time, :, :]
sw_all = toa_data.variables['toa_sw_all_mon'][time, :, :]
sw_clr = toa_data.variables['toa_sw_clr_mon'][time, :, :]

latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t lw_all: %i\n' % \
    (times.size, latsSize, lonsSize, lw_all.size))

#######################
# Create latitude profile array for a particular longitude.
#  All the latitudes are averaged for the particular longitude. 
# # # # # # # # # # # #
# Examples: 
#n = [x for x in p[::2]]
#new_array = [[array[i, j] for j in range(0, n, 10)] for i in range(0, m, 10)]

# Create profile. 
lw_all_avg_lats = [average([lw_all[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
lw_clr_avg_lats = [average([lw_clr[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
sw_all_avg_lats = [average([sw_all[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
sw_clr_avg_lats = [average([sw_clr[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

#######################
# Plot. 
# # # # # # # # # # # #
# Simple plot:
#t = arange(0.0, 2.0, 0.01)
#s = sin(2*pi*t)
#plot(t, s)
#
#xlabel('time (s)')
#ylabel('voltage (mV)')
#title('About as simple as it gets, folks')
#grid(True)
#savefig("images/test.png")
#show()

plot(lats, lw_all_avg_lats)
xlabel('latitude (deg)')
ylabel('flux (W/m^2)')
title('Top of Atmosphere Long Wave. All Sky Flux')
grid(True)
savefig("../images/CERES_EBAF_lw_all_avg_lats.png")
show()

plot(lats, lw_clr_avg_lats)
xlabel('latitude (deg)')
ylabel('flux (W/m^2)')
title('Top of Atmosphere Long Wave, Clear Sky Flux')
grid(True)
savefig("../images/CERES_EBAF_lw_clr_avg_lats.png")
show()

plot(lats, sw_all_avg_lats)
xlabel('latitude (deg)')
ylabel('flux (W/m^2)')
title('Top of Atmosphere Short Wave. All Sky Flux')
grid(True)
savefig("../images/CERES_EBAF_lw_all_avg_lats.png")
show()

plot(lats, sw_all_avg_lats)
xlabel('latitude (deg)')
ylabel('flux (W/m^2)')
title('Top of Atmosphere Short Wave. Clear Sky Flux')
grid(True)
savefig("../images/CERES_EBAF_lw_clr_avg_lats.png")
show()

#######################

