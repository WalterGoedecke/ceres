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

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

#######################
# # Import netcdf dataset and extract variables.
# # # # # # # # # # # #
#toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412_solar-sw-lw-net.nc')
#toa_data = Dataset('../datasets/MERRA301.prod.assim.tavg1_2d_rad_Nx.20010101.SUB.nc')
toa_data = Dataset('http://goldsmr2.sci.gsfc.nasa.gov/cgi-bin/dpool/HTTP_DpFileDownloadMERRA.pl?DATASET=MERRA_DP&FCP_DIR=/ftp/private/tmp/&APPLICATION=SUBSET_LATS4D&FILTER=SUBSET_LATS4D&SUB_LONMIN=-180&SUB_LONMAX=180&SUB_LATMAX=90&SUB_LATMIN=-90&OUTPUT_FORMAT=NetCDF&LOOKUPID_List=MAT1NXRAD&STARTYR=2001&STARTMON=01&STARTDAY=01&ENDYR=2001&ENDMON=01&ENDDAY=02&variable=lwtup&variable=swtdn&variable=swtnt&&meanValue=1/MERRA301.prod.assim.tavg1_2d_rad_Nx.20010101.SUB.nc')

# Set variables.
times = toa_data.variables['time'][:]
lats = toa_data.variables['latitude'][:]
lons = toa_data.variables['longitude'][:]

# Short-wave incoming top of atmosphere radiation. 
sw_down = toa_data.variables['swtdn'][:, :, :]
# Long wave outgoing top of atmosphere radiation. 
lw_up = toa_data.variables['lwtup'][:, :, :]
# Short-wave net outgoing top of atmosphere all sky incoming radiation. 
sw_net = toa_data.variables['swtnt'][:, :, :]

timesSize = times.size
latsSize = lats.size
lonsSize = lons.size

print('times: %i\t lats: %i\t lons: %i\t sw_all: %i\t solar: %i\n' % \
    (timesSize, latsSize, lonsSize, sw_all.size, solar.size))

#######################
# Calculate the short and long wave input and outputs.
#  Average for year.  
# # # # # # # # # # # #
#sw_in = [ [average([sw_in[time, i, j] for time in range(0, timesSize)]) \
#    for j in range(0, lonsSize)] for i in range(0, latsSize) ]
#sw_out = [ [average([sw_all[time, i, j] for time in range(0, timesSize)]) \
#    for j in range(0, lonsSize)] for i in range(0, latsSize) ]
#lw_out = [ [average([lw_all[time, i, j] for time in range(0, timesSize)]) \
#    for j in range(0, lonsSize)] for i in range(0, latsSize) ]
#net_in = [ [average([net_all[time, i, j] for time in range(0, timesSize)]) \
#    for j in range(0, lonsSize)] for i in range(0, latsSize) ]
#print('sw_in array size: %i\n' % len(sw_in))
#print('sw_in array size: %i\n' % len(sw_in[0]))

#######################

#######################
# Calculate and plot the albedo: the ratio of the outgoing to incoming sw radiation. 
# # # # # # # # # # # #
#l_variable = [[[2]*3]*4]*5
albedo = [[0]*lonsSize]*latsSize

# Check array sizes. 
#print('albedo array size: %i\n' % len(albedo))
#print('albedo array size: %i\n' % len(albedo[0]))
#
#print('sw_in array size: %i\n' % len(sw_in))
#print('sw_in array size: %i\n' % len(sw_in[0]))
#
#print('sw_out array size: %i\n' % len(sw_out))
#print('sw_out array size: %i\n' % len(sw_out[0]))

# i = lat, j = lon
for i in range(0, latsSize):
    #albedo[i] = [None if y == 0 else x/y for x, y in zip(sw_out[i], sw_in[i])]
    #albedo[i] = [x-y for x, y in zip(sw_down[i], sw_net[i])]
    albedo[i] = sw_down[0, i] - sw_net[0, i]
        
# # # # # # # # # # # #
# create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
m = Basemap(projection='kav7', lon_0=0, resolution='c')
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3')
m.drawmapboundary()
m.drawcoastlines()
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# Plot datapoints.
#x, y = m(lons, lats)
# Plot meshgrid.
meshlons, meshlats = np.meshgrid(lons, lats)

solars = m.pcolormesh(meshlons, meshlats, albedo, shading='flat', cmap=plt.cm.jet, \
    latlon=True)
    
# add colorbar
cb = m.colorbar(solars, "bottom", size="5%", pad="2%")
cb.set_label('Albedo (0 - 1.0)')

# # # # # # # # # # # #
# Plot some points. 
#Boulder
#x1, y1 = m(-105, 40)
#L-20
#x2, y2 = m(-117.63, 35.7)
#m.plot(x1, y1, 'b.', markersize=8)
#m.plot(x2, y2, 'c.', markersize=8)
        
ax.set_title('World Albedo Average for 1/1/2001')
plt.show()

# Save figure. 
fig.savefig("../images/MERRA-world_albedo-kav7_proj.png")

#######################

#######################
# Calculate the long-wave upward radiation.
# # # # # # # # # # # #
lw_out = [[0]*lonsSize]*latsSize
for i in range(0, latsSize):
    #albedo[i] = [None if y == 0 else x/y for x, y in zip(sw_out[i], sw_in[i])]
    #albedo[i] = [x-y for x, y in zip(sw_down[i], sw_net[i])]
    lw_out[i] = lw_up[0, i]
       
# # # # # # # # # # # #

# Plot the emitted lw radiation averaged for the year. 
# # # # # # # # # # # #
# create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
m = Basemap(projection='kav7', lon_0=0, resolution='c')
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3')
m.drawmapboundary()
m.drawcoastlines()
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

lw_out_plot = m.pcolormesh(meshlons, meshlats, lw_out, shading='flat', cmap=plt.cm.jet, \
    latlon=True)
    
# add colorbar
cb = m.colorbar(lw_out_plot, "bottom", size="5%", pad="2%")
cb.set_label('Radiative Flux $(W/m^2)$')

# # # # # # # # # # # #
# Plot some points. 
#Boulder
#x1, y1 = m(-105, 40)
#L-20
#x2, y2 = m(-117.63, 35.7)
#m.plot(x1, y1, 'b.', markersize=8)
#m.plot(x2, y2, 'c.', markersize=8)
        
ax.set_title('World Long Wave Emittivity, Average for 1/1/2001')
plt.show()

# Save figure. 
fig.savefig("../images/MERRA-world-lw_out_-kav7_proj.png")

#######################

#######################
# Calculate the net short-wave inward radiation.
# # # # # # # # # # # #
net_in = [[0]*lonsSize]*latsSize
for i in range(0, latsSize):
    #albedo[i] = [None if y == 0 else x/y for x, y in zip(sw_out[i], sw_in[i])]
    #albedo[i] = [x-y for x, y in zip(sw_down[i], sw_net[i])]
    net_in[i] = sw_net[0, i]
       
# # # # # # # # # # # #

# Plot the net absorbed sw & lw radiation averaged for the year. 
# # # # # # # # # # # #
# create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
m = Basemap(projection='kav7', lon_0=0, resolution='c')
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3')
m.drawmapboundary()
m.drawcoastlines()
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

net_in_plot = m.pcolormesh(meshlons, meshlats, net_in, shading='flat', cmap=plt.cm.jet, \
    latlon=True)
    
# add colorbar
cb = m.colorbar(net_in_plot, "bottom", size="5%", pad="2%")
cb.set_label('Radiative Flux $(W/m^2)$')

ax.set_title('Net Incomming Short Wave Solar Flux\n Average for 1/1/2001')
plt.show()

# Save figure. 
fig.savefig("../images/MERRA-world-net_in-kav7_proj.png")

#######################
