# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:07:57 2015

@author: walter
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset #, date2index
from numpy import * 
import numpy as np
import matplotlib.pyplot as plt
#from datetime import datetime
#date = datetime(2007,12,15,0) # date to plot.

#######################
# Read & plot netcdf data file. 
# # # # # # # # # # # #
winds = Dataset('datasets/example_wind_fields.nc')

levels = winds.variables['ilev'][:]
lats = winds.variables['lat'][:]
lons = winds.variables['lon'][:]
omegas = winds.variables['OMEGA'][0, 0, :]
us = winds.variables['U'][0, 0, :]
vs = winds.variables['V'][0, 0, :]

print('levels: %i\tlats: %i\tlons: %i\tomegas: %i\tus: %i\tvs: %i\n' % \
    (levels.size, lats.size, lons.size, omegas.size, us.size, vs.size))

# Plot datapoints.
lons, lats = np.meshgrid(lons,lats)
#ims = m.pcolormesh(lons, lats, omegas, shading='flat', cmap=plt.cm.jet, \
#    latlon=True)
#######################

#######################
# Create figure, axes instances.
#  U component. 
# # # # # # # # # # # #
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
m = Basemap(projection='kav7', lon_0=0, resolution='c')

# plot values with pcolor
ims = m.pcolormesh(lons, lats, us, shading='flat', cmap=plt.cm.jet, \
    latlon=True)

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# add colorbar
cb = m.colorbar(ims,"bottom", size="5%", pad="2%")

# add a title.
ax.set_title('Wind Fields - U component')
plt.show()

# Save figure. 
fig.savefig("wind_fields-kav7_proj-U.png")
#######################

#######################
# Create figure, axes instances.
#  V component. 
# # # # # # # # # # # #
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
m = Basemap(projection='kav7', lon_0=0, resolution='c')

# plot values with pcolor
ims = m.pcolormesh(lons, lats, vs, shading='flat', cmap=plt.cm.jet, \
    latlon=True)

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# add colorbar
cb = m.colorbar(ims,"bottom", size="5%", pad="2%")

# add a title.
ax.set_title('Wind Fields - V component')
plt.show()

# Save figure. 
fig.savefig("wind_fields-kav7_proj-V.png")
#######################

#######################
# Create figure, axes instances.
#  Magnitude component. 
# # # # # # # # # # # #
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
m = Basemap(projection='kav7', lon_0=0, resolution='c')

#cmplx = complex(us[0, :], vs[0, :])
cmplx = us + 1j*vs
mags = abs(cmplx)
phis = rad2deg(angle(cmplx))

#for w in range(0, 10): 
    #print('%f\t%f\t%f\n' % (us[0, w], vs[0, w], mags[0, w]))
    #print('%f\t %f\t %f\t %f\n' % (us[0, w], vs[0, w], mags[0, w], phis[0, w]))

# plot values with pcolor
ims = m.pcolormesh(lons, lats, mags, shading='flat', cmap=plt.cm.jet, \
    latlon=True)

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# add colorbar
cb = m.colorbar(ims,"bottom", size="5%", pad="2%")

# add a title.
ax.set_title('Wind Fields - Magnitude')
plt.show()

# Save figure. 
fig.savefig("wind_fields-kav7_proj-mag.png")
#######################

#######################
# Create figure, axes instances.
#  Magnitude component. 
# # # # # # # # # # # #
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
m = Basemap(projection='kav7', lon_0=0, resolution='c')

# plot values with pcolor
ims = m.pcolormesh(lons, lats, phis, shading='flat', cmap=plt.cm.jet, \
    latlon=True)

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# add colorbar
cb = m.colorbar(ims,"bottom", size="5%", pad="2%")

# add a title.
ax.set_title('Wind Fields - Direction')
plt.show()

# Save figure. 
fig.savefig("wind_fields-kav7_proj-angles.png")
#######################


