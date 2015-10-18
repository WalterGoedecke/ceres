# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:07:57 2015

@author: walter
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt

#from datetime import datetime
#date = datetime(2007,12,15,0) # date to plot.
#
## open dataset.
#dataset = \
#Dataset('http://www.ncdc.noaa.gov/thredds/dodsC/OISST-V2-AVHRR_agg')
#timevar = dataset.variables['time']
#timeindex = date2index(date,timevar) # find time index for desired date.
## read sst.  Will automatically create a masked array using
## missing_value variable attribute. 'squeeze out' singleton dimensions.
#sst = dataset.variables['sst'][timeindex,:].squeeze()
## read ice.
#ice = dataset.variables['ice'][timeindex,:].squeeze()
## read lats and lons (representing centers of grid boxes).
#lats = dataset.variables['lat'][:]
#lons = dataset.variables['lon'][:]
#lons, lats = np.meshgrid(lons,lats)

#######################
# Read & plot netcdf data file. 
# # # # # # # # # # # #
tosses = Dataset('datasets/tos_O1_2001-2002.nc')

times = tosses.variables['time'][:]
lats = tosses.variables['lat'][:]
lons = tosses.variables['lon'][:]
#toss = tosses.variables['tos'][12,:]
toss = tosses.variables['tos'][12,:].squeeze()

print('time: %i\tlat: %i\tlon: %i\ttos: %i\n' % \
    (times.size, lats.size, lons.size, toss.size))

# Plot datapoints.
lons, lats = np.meshgrid(lons,lats)

#######################

# create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
m = Basemap(projection='kav7',lon_0=0,resolution=None)
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')
# plot sst, then ice with pcolor
#im1 = m.pcolormesh(lons,lats,sst,shading='flat',cmap=plt.cm.jet,latlon=True)
#im2 = m.pcolormesh(lons,lats,ice,shading='flat',cmap=plt.cm.gist_gray,latlon=True)
tossed = m.pcolormesh(lons, lats, toss, shading='flat', cmap=plt.cm.jet, \
    latlon=True)

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))
# add colorbar
#cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
# add a title.

# add colorbar
cb = m.colorbar(tossed,"bottom", size="5%", pad="2%")

#ax.set_title('SST and ICE analysis for %s'%date)
ax.set_title('Sea Surface Temperature')
plt.show()

# Save figure. 
fig.savefig("sea_surface_temp_kav7_proj.png")

