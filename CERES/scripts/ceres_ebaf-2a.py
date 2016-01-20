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
#from pylab import *
# Add directory to path. 
import sys
sys.path.insert(0, "../modules")

import MeteoPlot

#######################
# Plot 1
#######################
# # Import netcdf dataset.
# # # # # # # # # # # #
#toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-cre.nc')
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-total.nc')

# Set variables.
times = toa_data.variables['time'][:]
# Set time to choice. 
time = 6
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
solar = toa_data.variables['solar_mon'][time, :, :]
lw = toa_data.variables['toa_cre_lw_mon'][time, :, :]
sw = toa_data.variables['toa_cre_sw_mon'][time, :, :]
net = toa_data.variables['toa_cre_net_mon'][time, :, :]

latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t lw: %i\n' % \
    (times.size, latsSize, lonsSize, lw.size))

#######################
# Create latitude profile array for a particular longitude.
#  All the latitudes are averaged for the particular longitude. 
# # # # # # # # # # # #
# Examples: 
#n = [x for x in p[::2]]
#new_array = [[array[i, j] for j in range(0, n, 10)] for i in range(0, m, 10)]

# Create profile. 
solar_avg_lats = [average([solar[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
lw_avg_lats = [average([lw[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
sw_avg_lats = [average([sw[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
net_avg_lats = [average([net[i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]

#######################
# Plot. 
# # # # # # # # # # # #
plot(lats, solar_avg_lats)
axis([-90, 90, -2, 1.1*amax(solar_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar Flux')
grid(True)
savefig("../images/CERES_EBAF_solar_avg_lats.png")
show()

plot(lats, lw_avg_lats)
axis([-90, 90, -1, 1.1*amax(lw_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Top of Atmosphere Cloud Radiative Effects Long Wave Flux')
grid(True)
savefig("../images/CERES_EBAF_lw_cre_avg_lats.png")
show()

plot(lats, sw_avg_lats)
axis([-90, 90, -2 + amin(sw_avg_lats), 1.1*amax(sw_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Top of Atmosphere Cloud Radiative Effects Short Wave Flux')
grid(True)
savefig("../images/CERES_EBAF_sw_cre_avg_lats.png")
show()

plot(lats, net_avg_lats)
axis([-90, 90, -2 + amin(net_avg_lats), 1.1*amax(net_avg_lats) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Top of Atmosphere Cloud Radiative Effects Net Flux')
grid(True)
savefig("../images/CERES_EBAF_net_cre_avg_lats.png")
show()

#######################
