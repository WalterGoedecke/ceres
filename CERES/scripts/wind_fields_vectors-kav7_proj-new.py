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

cmplx = us + 1j*vs
mags = abs(cmplx)
phis = rad2deg(angle(cmplx))

#for w in range(0, 10): 
    #print('%f\t%f\t%f\n' % (us[0, w], vs[0, w], mags[0, w]))
    #print('%f\t %f\t %f\t %f\n' % (us[0, w], vs[0, w], mags[0, w], phis[0, w]))

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
#fig = plt.figure()
#ax = fig.add_axes([0.05,0.05,0.9,0.9])
#
## create Basemap instance.
## coastlines not used, so resolution set to None to skip
## continent processing (this speeds things up a bit)
##m = Basemap(projection='kav7', lon_0=0, resolution=None)
#m = Basemap(projection='kav7', lon_0=0, resolution='c')
#
## plot values with pcolor
#ims = m.pcolormesh(lons, lats, us, shading='flat', cmap=plt.cm.jet, \
#    latlon=True)
#
## draw line around map projection limb.
## color background of map projection region.
## missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3')
#m.drawcountries()
#
## draw parallels and meridians, but don't bother labelling them.
#m.drawparallels(np.arange(-90.,99.,30.))
#m.drawmeridians(np.arange(-180.,180.,60.))
#
## add colorbar
#cb = m.colorbar(ims,"bottom", size="5%", pad="2%")
#
## add a title.
#ax.set_title('Wind Fields - U component')
#plt.show()
#
## Save figure. 
#fig.savefig("images/wind_fields_vectors-kav7_proj-U.png")
#######################

#######################
# Create figure, axes instances.
#  V component. 
# # # # # # # # # # # #
#fig = plt.figure()
#ax = fig.add_axes([0.05,0.05,0.9,0.9])
#
## create Basemap instance.
## coastlines not used, so resolution set to None to skip
## continent processing (this speeds things up a bit)
##m = Basemap(projection='kav7', lon_0=0, resolution=None)
#m = Basemap(projection='kav7', lon_0=0, resolution='c')
#
## plot values with pcolor
#ims = m.pcolormesh(lons, lats, vs, shading='flat', cmap=plt.cm.jet, \
#    latlon=True)
#
## draw line around map projection limb.
## color background of map projection region.
## missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3')
#m.drawcountries()
#
## draw parallels and meridians, but don't bother labelling them.
#m.drawparallels(np.arange(-90.,99.,30.))
#m.drawmeridians(np.arange(-180.,180.,60.))
#
## add colorbar
#cb = m.colorbar(ims,"bottom", size="5%", pad="2%")
#
## add a title.
#ax.set_title('Wind Fields - V component')
#plt.show()
#
## Save figure. 
#fig.savefig("images/wind_fields_vectors-kav7_proj-V.png")
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
ims = m.pcolormesh(lons, lats, mags, shading='flat', cmap=plt.cm.jet, \
    latlon=True)

# compute native x,y coordinates of grid.
x, y = m(lons, lats)

# Plot vectors.
#Q = m.quiver(xx, yy, uproj, vproj, scale=700)
#Q = m.quiver(x, y, us, vs, scale=7000)

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
fig.savefig("images/wind_fields_vectors-kav7_proj-mag.png")
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
ims = m.pcolormesh(lons, lats, mags, shading='flat', cmap=plt.cm.jet, \
    latlon=True)

# compute native x,y coordinates of grid.
x, y = m(lons, lats)

# Plot vectors.
#Q = m.quiver(xx, yy, uproj, vproj, scale=700)
#Q = m.quiver(x, y, us, vs, scale=7000)

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
#ax.set_title('Wind Fields - Magnitude & Direction')
#plt.show()

# Save figure. 
#fig.savefig("images/wind_fields_vectors-kav7_proj-cmplx.png")
#######################

#######################
# Create figure, axes instances.
#  Phase component. 
# # # # # # # # # # # #
#fig = plt.figure()
#ax = fig.add_axes([0.05,0.05,0.9,0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
#m = Basemap(projection='kav7', lon_0=0, resolution='c')

# Create sparser lat, lon, us, & vs arrays to prevent 
#  over densifying the direction arrow plot. 
#lats = winds.variables['lat'][:]
#lons = winds.variables['lon'][:]
#us = winds.variables['U'][0, 0, :]
#vs = winds.variables['V'][0, 0, :]
dirlats = winds.variables['lat'][:]
dirlons = winds.variables['lon'][:]

sublats = [x for x in dirlats[::5]]
sublons = [x for x in dirlons[::5]]

dirus = winds.variables['U'][0, 0, :, :]
dirvs = winds.variables['V'][0, 0, :, :]

dircmplx = dirus + 1j*dirvs
dirmags = abs(dircmplx)

dirus = dirus/dirmags
dirvs = dirvs/dirmags

subus = [[dirus[i, j] for j in range(0, 192, 5)] for i in range(0, 94, 5)]
subvs = [[dirvs[i, j] for j in range(0, 192, 5)] for i in range(0, 94, 5)]

# Example array sampler:
#n = [x for x in p[::2]]

#for w in range(0, 10): 
    #print('%f\t%f\t%f\n' % (us[0, w], vs[0, w], mags[0, w]))
    #print('%f\t %f\t %f\t %f\n' % (us[0, w], vs[0, w], mags[0, w], phis[0, w]))

# Plot datapoints.
#lons, lats = np.meshgrid(lons,lats)
#newlons, newlats = np.meshgrid(dirlons, dirlats)
newlons, newlats = np.meshgrid(sublons, sublats)

# plot values with pcolor
#ims = m.pcolormesh(lons, lats, mags, shading='flat', cmap=plt.cm.jet, \
#    latlon=True)

# compute native x,y coordinates of grid.
#x, y = m(lons, lats)
#x, y = m(dirlons, dirlats)
x, y = m(newlons, newlats)

# Plot vectors.
#Q = m.quiver(xx, yy, uproj, vproj, scale=700)
#Q = m.quiver(x, y, dirus, dirvs, scale=2000)
#Q = m.quiver(x, y, dirus, dirvs, scale=70)
Q = m.quiver(x, y, subus, subvs, scale=40, cmap=plt.cm.jet)

# make quiver key.
#qk = plt.quiverkey(Q, 0.1, 0.1, 20, '20 m/s', labelpos='W')

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3') # Dark grey.
#m.drawmapboundary(fill_color='0.95') # Light grey.
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# add colorbar
#cb = m.colorbar(ims,"bottom", size="5%", pad="2%")

# add a title.
ax.set_title('Wind Fields - Magnitude & Direction')
plt.show()

# Save figure. 
fig.savefig("images/wind_fields_vectors-kav7_proj-cmplx.png")

#######################

#######################
# Create figure, axes instances.
#  Phase component. 
# # # # # # # # # # # #
#fig = plt.figure()
#ax = fig.add_axes([0.05,0.05,0.9,0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
#m = Basemap(projection='kav7', lon_0=0, resolution='c')

# Create sparser lat, lon, us, & vs arrays to prevent 
#  over densifying the direction arrow plot. 
#lats = winds.variables['lat'][:]
#lons = winds.variables['lon'][:]
#us = winds.variables['U'][0, 0, :]
#vs = winds.variables['V'][0, 0, :]
dirlats = winds.variables['lat'][:]
dirlons = winds.variables['lon'][:]

sublats = [x for x in dirlats[::5]]
sublons = [x for x in dirlons[::5]]

dirus = winds.variables['U'][0, 0, :, :]
dirvs = winds.variables['V'][0, 0, :, :]

dircmplx = dirus + 1j*dirvs
dirmags = abs(dircmplx)

dirus = dirus/dirmags
dirvs = dirvs/dirmags

subus = [[dirus[i, j] for j in range(0, 192, 5)] for i in range(0, 94, 5)]
subvs = [[dirvs[i, j] for j in range(0, 192, 5)] for i in range(0, 94, 5)]

# Example array sampler:
#n = [x for x in p[::2]]

#for w in range(0, 10): 
    #print('%f\t%f\t%f\n' % (us[0, w], vs[0, w], mags[0, w]))
    #print('%f\t %f\t %f\t %f\n' % (us[0, w], vs[0, w], mags[0, w], phis[0, w]))

# Plot datapoints.
#lons, lats = np.meshgrid(lons,lats)
#newlons, newlats = np.meshgrid(dirlons, dirlats)
newlons, newlats = np.meshgrid(sublons, sublats)

# plot values with pcolor
#ims = m.pcolormesh(lons, lats, mags, shading='flat', cmap=plt.cm.jet, \
#    latlon=True)

# compute native x,y coordinates of grid.
#x, y = m(lons, lats)
#x, y = m(dirlons, dirlats)
x, y = m(newlons, newlats)

# Plot vectors.
#Q = m.quiver(xx, yy, uproj, vproj, scale=700)
#Q = m.quiver(x, y, dirus, dirvs, scale=2000)
#Q = m.quiver(x, y, dirus, dirvs, scale=70)
Q = m.quiver(x, y, subus, subvs, scale=40)

# make quiver key.
qk = plt.quiverkey(Q, 0.1, 0.1, 20, '20 m/s', labelpos='W')

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3') # Dark grey.
#m.drawmapboundary(fill_color='0.95') # Light grey.
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# add colorbar
#cb = m.colorbar(ims,"bottom", size="5%", pad="2%")

# add a title.
ax.set_title('Wind Fields - Magnitude & Direction')
plt.show()

# Save figure. 
fig.savefig("images/wind_fields_vectors-kav7_proj-arrows.png")

#######################

#######################
# Create figure, axes instances.
#  Phase component. 
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
fig.savefig("images/wind_fields_vectors-kav7_proj-angles.png")
#######################


