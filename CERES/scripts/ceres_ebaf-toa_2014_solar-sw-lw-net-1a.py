# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:11:48 2015

@author: walter
"""
from netCDF4 import Dataset #, date2index
from pylab import *
# Add directory to path. 
import sys
sys.path.insert(0, "../modules")
import MeteoPlot

#######################
# # Import netcdf dataset.
# # # # # # # # # # # #
#toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412-sw-22oct15.nc')
toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412_solar-sw-lw-net.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['lat'][:]
lons = toa_data.variables['lon'][:]

# Incoming top of atmosphere radiation. 
solar = toa_data.variables['solar_mon'][:, :, :]
# Short wave top of atmosphere all sky outgoing radiation. 
sw_all = toa_data.variables['toa_sw_all_mon'][:, :, :]
# Long wave top of atmosphere all sky outgoing radiation. 
lw_all = toa_data.variables['toa_lw_all_mon'][:, :, :]
# Net long & short wave top of atmosphere all sky incoming radiation. 
net_all = toa_data.variables['toa_net_all_mon'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t sw_all: %i\t solar: %i\n' % \
    (timesSize, latsSize, lonsSize, sw_all.size, solar.size))

# # # # # # # # # # # #
# Calculate the January data.
# Set time to January. 
time = 0
solar_avg_lats_jan = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
sw_all_avg_lats_jan = [average([sw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
lw_all_avg_lats_jan = [average([lw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
net_all_avg_lats_jan = [average([net_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
# # # # # # # # # # # #

# Calculate the January, February, & December average data.
solar_avg_lats_jan_feb_dec = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in [0, 1, 11]]) for i in range(0, latsSize) ]
sw_all_avg_lats_jan_feb_dec = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in [0, 1, 11]]) for i in range(0, latsSize) ]
lw_all_avg_lats_jan_feb_dec = [ average([[lw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in [0, 1, 11]]) for i in range(0, latsSize) ]
net_all_avg_lats_jan_feb_dec = [ average([[net_all[time, i, j] for j in range(0, lonsSize)] \
    for time in [0, 1, 11]]) for i in range(0, latsSize) ]
# # # # # # # # # # # #

# Calculate the July data.
# Set time to July. 
time = 6
solar_avg_lats_jul = [average([solar[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
sw_all_avg_lats_jul = [average([sw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
lw_all_avg_lats_jul = [average([lw_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
net_all_avg_lats_jul = [average([net_all[time, i, j] for j in range(0, lonsSize)]) \
    for i in range(0, latsSize)]
# # # # # # # # # # # #
    
# Calculate the June, July, & August average data.
solar_avg_lats_jun_jul_aug = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in range(5, 8)]) for i in range(0, latsSize) ]
sw_all_avg_lats_jun_jul_aug = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(5, 8)]) for i in range(0, latsSize) ]
lw_all_avg_lats_jun_jul_aug = [ average([[lw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(5, 8)]) for i in range(0, latsSize) ]
net_all_avg_lats_jun_jul_aug = [ average([[net_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(5, 8)]) for i in range(0, latsSize) ]
# # # # # # # # # # # #

# Calculate all the months' data.
# Average for all the months in a year. 
solar_avg_lats = [ average([[solar[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
sw_all_avg_lats = [ average([[sw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
lw_all_avg_lats = [ average([[lw_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
net_all_avg_lats = [ average([[net_all[time, i, j] for j in range(0, lonsSize)] \
    for time in range(0, timesSize)]) for i in range(0, latsSize) ]
# # # # # # # # # # # #

#######################
# Create plot of incoming short-wave radiation: January, July, & all months.
plot(lats, solar_avg_lats_jan, '-b', label='January')
plot(lats, solar_avg_lats_jul, '-g', label='July')
plot(lats, solar_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, -2, 1.2*amax(solar_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('Solar Incoming Short Wave Flux\nJanuary, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_solar_incoming_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #
# Create plot of incoming short-wave radiation: winter, summer, & all months.
plot(lats, solar_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
plot(lats, solar_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, solar_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, -2, 1.2*amax(solar_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('Solar Incoming Short Wave Flux\nWinter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_solar_incoming_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()

#######################

# Create plot of toa outgoing sw radiation: January, July, & all months.
plot(lats, sw_all_avg_lats_jan, '-b', label='January')
plot(lats, sw_all_avg_lats_jul, '-g', label='July')
plot(lats, sw_all_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 1.2*amin(sw_all_avg_lats_jul), 1.2*amax(sw_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('TOA Solar Short Wave Outgoing Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_outgoing_sw_all_avg_lats-jan_jul_2014.png")
#savefig("../images/CERES_TOA_solar_net_all_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #
# Create plot of toa outgoing sw radiation: winter, summer, & all months.
plot(lats, sw_all_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
plot(lats, sw_all_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, sw_all_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 1.2*amin(sw_all_avg_lats_jun_jul_aug), 1.2*amax(sw_all_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
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
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
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
plot(lats, absorbed_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
plot(lats, absorbed_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, absorbed_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, -2, 1.2*amax(absorbed_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('CERES TOA Absorbed Short Wave Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_absorbed_sw_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()
#######################

# Calculate the albedo: the ratio of the outgoing to incoming sw radiation. 

# Check if the solar incoming flux is null; if so, set value to "None," 
albedo_avg_lats_jan = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats_jan, solar_avg_lats_jan)]
# Ignore opposite hemisphere albedo above 60 deg. latitude. 
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
xlabel('Latitude')
ylabel('Albedo')
title('CERES Top of Atmosphere Albedo\n January, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_albedo_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #

# Check if the solar incoming flux is null; if so, set value to "None," 
albedo_avg_lats_jan_feb_dec = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats_jan_feb_dec, solar_avg_lats_jan_feb_dec)]
# Ignore opposite hemisphere albedo above 60 deg. latitude. 
for i, x in enumerate(lats):
    if x > 60:
        albedo_avg_lats_jan_feb_dec[i] = None

albedo_avg_lats_jun_jul_aug = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats_jun_jul_aug, solar_avg_lats_jun_jul_aug)]
for i, x in enumerate(lats):
    if x < -60:
        albedo_avg_lats_jun_jul_aug[i] = None

albedo_avg_lats = [None if y == 0 else x/y for x, y in zip(sw_all_avg_lats, solar_avg_lats)]

# Create plot of albedo. 
plot(lats, albedo_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
plot(lats, albedo_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, albedo_avg_lats, '-r', label='All Months')

legend(loc='upper right')

axis([-90, 90, 0, 1])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Albedo')
title('CERES Top of Atmosphere Albedo\n Winter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_albedo_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()

#######################

# Create plot of toa outgoing lw radiation: January, July, & all months.
plot(lats, lw_all_avg_lats_jan, '-b', label='January')
plot(lats, lw_all_avg_lats_jul, '-g', label='July')
plot(lats, lw_all_avg_lats, '-r', label='All Months')

legend(loc='lower right')

axis([-90, 90, -2, 1.2*amax(lw_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('TOA Solar Long Wave Outgoing Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_outgoing_lw_all_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #
# Create plot of toa outgoing lw radiation: winter, summer, & all months.
plot(lats, lw_all_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
plot(lats, lw_all_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, lw_all_avg_lats, '-r', label='All Months')

legend(loc='lower right')

axis([-90, 90, -2, 1.2*amax(lw_all_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('TOA Solar Long Wave Outgoing Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_outgoing_lw_all_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()

#######################

# Create plot of toa net incoming sw & lw radiation: January, July, & all months.
plot(lats, net_all_avg_lats_jan, '-b', label='January')
plot(lats, net_all_avg_lats_jul, '-g', label='July')
plot(lats, net_all_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, 1.2*amin(net_all_avg_lats_jan), 1.2*amax(net_all_avg_lats_jan) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('CERES TOA Net Incoming Short & Long Wave Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_incoming_net_all_avg_lats-jan_jul_2014.png")
show()

# # # # # # # # # # # #
# Create plot of toa net incoming sw & lw radiation: winter, summer, & all months.
plot(lats, net_all_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
plot(lats, net_all_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
plot(lats, net_all_avg_lats, '-r', label='All Months')

legend(loc='lower center')

axis([-90, 90, 1.2*amin(net_all_avg_lats_jan_feb_dec), 1.2*amax(net_all_avg_lats_jan_feb_dec) ])
plt.xticks(range(-90, 91, 30))
xlabel('Latitude')
ylabel('Radiative Flux $(W/m^2)$')
title('CERES TOA Net Incoming Short & Long Wave Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
grid(True)
savefig("../images/CERES_TOA_incoming_net_all_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
show()
#######################

