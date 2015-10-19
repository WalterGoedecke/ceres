# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:07:57 2015

@author: walter
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset #, date2index
import numpy as np
from numpy import * 
import matplotlib.pyplot as plt
#from datetime import datetime
#date = datetime(2007,12,15,0) # date to plot.

#######################
# Read netcdf data file. 
# # # # # # # # # # # #
# Import dataset. 
winds = Dataset('datasets/example_wind_fields.nc')

# Set variables.
levels = winds.variables['ilev'][:]
# Set level to choice. 
level = 0
lats = winds.variables['lat'][:]
lons = winds.variables['lon'][:]
omegas = winds.variables['OMEGA'][0, 0, :]
us = winds.variables['U'][0, level, :]
vs = winds.variables['V'][0, level, :]

print('levels: %i\tlats: %i\tlons: %i\tomegas: %i\tus: %i\tvs: %i\n' % \
    (levels.size, lats.size, lons.size, omegas.size, us.size, vs.size))

# Set up complex array of wind velocity components to compute magnitude. 
cmplx = us + 1j*vs
mags = abs(cmplx)
#phis = rad2deg(angle(cmplx))

#######################

#######################
# Create figure, axes instancesm and colored magnitude component. 
# # # # # # # # # # # #
fig = plt.figure()
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
m = Basemap(projection='kav7', lon_0=0, resolution='c')

# Mesh grid.
grdlons, grdlats = np.meshgrid(lons,lats)
# plot values with pcolor
ims = m.pcolormesh(grdlons, grdlats, mags, shading='flat', \
    cmap=plt.cm.jet, latlon=True)

# add colorbar
cb = m.colorbar(ims,"bottom", size="5%", pad="2%", label='(m/s)')

#######################

#######################
# Create unit vector arrows to show wind direction.
# # # # # # # # # # # #
# Set sparseness faxctor. 
sf = 5

# Create sparser lat, lon, us, & vs arrays to prevent 
#  over densifying the direction arrow plot. 
sprs_lats = [x for x in lats[::sf]]
sprs_lons = [x for x in lons[::sf]]
# Example array sampler:
#n = [x for x in p[::2]]

# Create wind velocity unit vectors. 
us_unit = us/mags
vs_unit = vs/mags

# Create sparser U and V unit wind velocity components. 
sprs_us_u = [[us_unit[i, j] for j in range(0, 192, sf)] for i in range(0, 94, sf)]
sprs_vs_u = [[vs_unit[i, j] for j in range(0, 192, sf)] for i in range(0, 94, sf)]

# Plot datapoints.
#lons, lats = np.meshgrid(lons,lats)
#newlons, newlats = np.meshgrid(dirlons, dirlats)
grdlons, grdlats = np.meshgrid(sprs_lons, sprs_lats)

# compute native x,y coordinates of grid.
#x, y = m(lons, lats)
#x, y = m(dirlons, dirlats)
x, y = m(grdlons, grdlats)

# Plot vectors.
#arrowScale = 700
#arrowScale = 2000
#arrowScale = 70
arrowScale = 40
Q = m.quiver(x, y, sprs_us_u, sprs_vs_u, scale = arrowScale)

# make quiver key.
#qk = plt.quiverkey(Q, 0.1, 0.1, 20, '20 m/s', labelpos='W')

#######################

#######################
# Draw remaining map attributes and save.
# # # # # # # # # # # #
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up as this color.
#m.drawmapboundary(fill_color='0.3') # Dark grey.
#m.drawmapboundary(fill_color='0.95') # Light grey.
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90., 99., 30.))
m.drawmeridians(np.arange(-180., 180., 60.))

# add a title.
ax.set_title('Wind Fields - Level ' + str(level) \
    + ' - Magnitude & Direction')
plt.show()

# Create figure file name. 
figname = 'images/wind_fields_colors-level_' + str(level) + '.png'

# Save figure. 
#fig.savefig("images/wind_fields_vectors-kav7_proj-arrows.png")
fig.savefig(figname)
#######################


#######################
# Create figure, axes instances.
#  Arrows represent both magnitude and phase. 
# # # # # # # # # # # #
fig = plt.figure()
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])

# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
#m = Basemap(projection='kav7', lon_0=0, resolution=None)
m = Basemap(projection='kav7', lon_0=0, resolution='c')

# Set sparseness faxctor. 
sf = 5
#sf = 10

# Create sparser lat, lon, us, & vs arrays to prevent 
#  over densifying the direction arrow plot. 
sprs_lats = [x for x in lats[::sf]]
sprs_lons = [x for x in lons[::sf]]

# Create sparser U and V wind velocity components. 
sprs_us = [[us[i, j] for j in range(0, 192, sf)] for i in range(0, 94, sf)]
sprs_vs = [[vs[i, j] for j in range(0, 192, sf)] for i in range(0, 94, sf)]

# Plot datapoints.
#lons, lats = np.meshgrid(lons,lats)
#newlons, newlats = np.meshgrid(dirlons, dirlats)
grdlons, grdlats = np.meshgrid(sprs_lons, sprs_lats)

# compute native x,y coordinates of grid.
#x, y = m(lons, lats)
#x, y = m(dirlons, dirlats)
x, y = m(grdlons, grdlats)

# Plot vectors.
#arrowScale = 700
#arrowScale = 2000
#arrowScale = 70
arrowScale = 1200
Q = m.quiver(x, y, sprs_us, sprs_vs, scale = arrowScale)

# make quiver key.
qk = plt.quiverkey(Q, 0.1, 0.1, 20, '20 m/s', labelpos='W')

#######################

#######################
# Draw remaining map attributes and save.
# # # # # # # # # # # #
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
#m.drawmapboundary(fill_color='0.3') # Dark grey.
#m.drawmapboundary(fill_color='0.95') # Light grey.
m.drawcountries()

# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90., 99., 30.))
m.drawmeridians(np.arange(-180., 180., 60.))

# add a title.
ax.set_title('Wind Fields - Level ' + str(level) \
    + '\n(Arrows show magnitude and direction)')
plt.show()

# Create figure file name. 
figname = 'images/wind_fields_arrows-level_' + str(level) + '.png'

# Save figure. 
#fig.savefig("images/wind_fields_vectors-kav7_proj-arrows.png")
fig.savefig(figname)
#######################
