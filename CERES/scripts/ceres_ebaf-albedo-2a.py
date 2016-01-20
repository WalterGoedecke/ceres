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

#import MeteoPlot

#######################
# # Import netcdf dataset.
# # # # # # # # # # # #
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-sw-22oct15.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]
# Short wave top of atmosphere all sky outgoing radiation. 
sw_all = toa_data.variables['toa_sw_all_mon'][:, :, :]
# Incoming top of atmosphere radiation. 
solar = toa_data.variables['solar_mon'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t sw_all: %i\t solar: %i\n' % \
    (timesSize, latsSize, lonsSize, sw_all.size, solar.size))

# # # # # # # # # # # #
# Calculate the January data.
# Set time to January. 
time = 0
sw_all_avg_lats_jan = [average([sw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
solar_avg_lats_jan = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
# # # # # # # # # # # #

# Calculate the January, February, & December average data.
sw_all_avg_lats_jan_feb_dec = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in [0, 1, 11]]) for i in range(0, latsSize) ]
solar_avg_lats_jan_feb_dec = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in [0, 1, 11]]) for i in range(0, latsSize) ]
# # # # # # # # # # # #

# Calculate the July data.
# Set time to July. 
time = 6
sw_all_avg_lats_jul = [average([sw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
solar_avg_lats_jul = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
# # # # # # # # # # # #
    
# Calculate the June, July, & August average data.
sw_all_avg_lats_jun_jul_aug = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(5, 8)]) for i in range(0, latsSize) ]
solar_avg_lats_jun_jul_aug = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in range(5, 8)]) for i in range(0, latsSize) ]
# # # # # # # # # # # #

# Calculate all the months' data.
# Average for all the months in a year. 
sw_all_avg_lats = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
solar_avg_lats = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
# # # # # # # # # # # #

#######################
# Create plot of incoming short-wave radiation.
plot(lats, solar_avg_lats_jan, '-b', label='January')
plot(lats, solar_avg_lats_jul, '-g', label='July')
plot(lats, solar_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, -2, 1.2*amax(solar_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar Incoming Short Wave Flux\nJanuary, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_solar_incoming_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #
# Create plot of incoming short-wave radiation.
plot(lats, solar_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
plot(lats, solar_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, solar_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, -2, 1.2*amax(solar_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('Solar Incoming Short Wave Flux\nWinter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_solar_incoming_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()
#######################

# Create plot of toa outgoing sw radiation.
plot(lats, sw_all_avg_lats_jan, '-b', label='January')
plot(lats, sw_all_avg_lats_jul, '-g', label='July')
plot(lats, sw_all_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 1.2*amin(sw_all_avg_lats_jul), 1.2*amax(sw_all_avg_lats_jan) ])
#axis([-90, 90, 1.2*amin(net_all_avg_lats_jul), 1.2*amax(net_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Solar Short Wave Outgoing Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
#title('TOA Solar Net Short Wave Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_outgoing_sw_all_avg_lats-jan_jul_2014.png")
#savefig("../images/CERES_TOA_solar_net_all_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #
# Create plot of toa outgoing sw radiation.
plot(lats, sw_all_avg_lats_jan_feb_mar, '-b', label='Jan-Feb-Dec')
plot(lats, sw_all_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, sw_all_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 1.2*amin(sw_all_avg_lats_jun_jul_aug), 1.2*amax(sw_all_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('TOA Solar Short Wave Outgoing Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_outgoing_sw_all_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()
#######################

# Calculate the absorption: the difference between the incoming and outgoing sw radiation. 
absorbed_avg_lats_jan = [y-x for x, y in zip(sw_all_avg_lats_jan, solar_avg_lats_jan)]
absorbed_avg_lats_jul = [y-x for x, y in zip(sw_all_avg_lats_jul, solar_avg_lats_jul)]
absorbed_avg_lats = [y-x for x, y in zip(sw_all_avg_lats, solar_avg_lats)]
# # # # # # # # # # # #

# Create plot of absorption.
plot(lats, absorbed_avg_lats_jan, '-b', label='January')
plot(lats, absorbed_avg_lats_jul, '-g', label='July')
plot(lats, absorbed_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, -2, 1.2*amax(absorbed_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('CERES TOA Absorbed Short Wave Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_absorbed_sw_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #

# Calculate the absorption: the difference between the incoming and outgoing sw radiation. 
absorbed_avg_lats_jan_feb_dec = [y-x for x, y in zip(sw_all_avg_lats_jan_feb_dec, solar_avg_lats_jan_feb_dec)]
absorbed_avg_lats_jun_jul_aug = [y-x for x, y in zip(sw_all_avg_lats_jul, solar_avg_lats_jun_jul_aug)]
absorbed_avg_lats = [y-x for x, y in zip(sw_all_avg_lats, solar_avg_lats)]
# # # # # # # # # # # #

# Create plot of absorption.
plot(lats, absorbed_avg_lats_jan_feb_mar, '-b', label='Jan-Feb-Dec')
plot(lats, absorbed_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, absorbed_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, -2, 1.2*amax(absorbed_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Radiative flux $(W/m^2)$')
title('CERES TOA Absorbed Short Wave Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_absorbed_sw_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()
#######################

# Calculate the albedo: the ratio of the outgoing to incoming sw radiation. 
#  Check if the solar incoming flux is null; if so, set value to "None," 
#  Also, ignore opposite hemisphere albedo above 60 deg. latitude. 

albedo_avg_lats_jan = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats_jan, solar_avg_lats_jan)]
for i, x in enumerate(lats):
    if x > 60:
        albedo_avg_lats_jan[i] = None

albedo_avg_lats_jul = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats_jul, solar_avg_lats_jul)]
for i, x in enumerate(lats):
    if x < -60:
        albedo_avg_lats_jul[i] = None

albedo_avg_lats = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats, solar_avg_lats)]

# Create plot of albedo. 
plot(lats, albedo_avg_lats_jan, '-b', label='January')
plot(lats, albedo_avg_lats_jul, '-g', label='July')
plot(lats, albedo_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 0, 1])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Ratio Flux')
title('CERES Top of Atmosphere Albedo\n January, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_albedo_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #

albedo_avg_lats_jan_feb_dec = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats_jan_feb_dec, solar_avg_lats_jan_feb_dec)]
for i, x in enumerate(lats):
    if x > 60:
        albedo_avg_lats_jan_feb_mar[i] = None

albedo_avg_lats_jun_jul_aug = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats_jun_jul_aug, solar_avg_lats_jun_jul_aug)]
for i, x in enumerate(lats):
    if x < -60:
        albedo_avg_lats_jun_jul_aug[i] = None

albedo_avg_lats = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats, solar_avg_lats)]

# Create plot of albedo. 
plot(lats, albedo_avg_lats_jan_feb_mar, '-b', label='Jan-Feb-Dec')
plot(lats, albedo_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, albedo_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 0, 1])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude (deg)')
ylabel('Ratio Flux')
title('CERES Top of Atmosphere Albedo\n Winter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_albedo_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()

#######################

