# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:17:24 2015

@author: walter
"""

import numpy as np
from netCDF4 import Dataset
# Mapping
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# 3D plot imports
from mpl_toolkits.mplot3d import axes3d
# Graph size. 
import plotly.plotly as py
import plotly.graph_objs as go

# create new figure, axes instances.
fig=plt.figure()
# Figure size. 
#ax=fig.add_axes([0.1,0.1,0.8,0.8])
#ax=fig.add_axes([0.15, 0.15, 1.2, 1.2])

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.

#m = Basemap(projection='cyl', resolution='l', urcrnrlat=37.0, urcrnrlon=-116.0, \
#    llcrnrlon=-118.5, llcrnrlat=35.0, area_thresh=1000.)
m = Basemap(projection='cyl', resolution='l', urcrnrlat=53.0, urcrnrlon=-70.0, \
    llcrnrlon=-120.0, llcrnrlat=25.0, area_thresh=1000.)

#######################
# Draw state lines, rivers, global lines. 
# # # # # # # # # # # #
m.drawcoastlines()
m.drawcountries()
m.drawstates(color="red")
m.drawrivers(color="blue")
m.fillcontinents(color='coral', lake_color='aqua')

# draw parallels and meridians.
parallels = np.arange(30., 60, 5.)
m.drawparallels(parallels, labels=[1, 0, 0, 1])
meridians = np.arange(-120., -60., 10.)
m.drawmeridians(meridians, labels=[1, 0, 0, 1])

m.drawmapboundary(fill_color='aqua')

#######################

#######################
# Read netcdf data file. 
# # # # # # # # # # # #
satdata = Dataset('../datasets/CERES_SSF_XTRK-MODIS_Edition3A_Subset_2014010100-2014010223.nc')

#start = 0
#stop = 100000
# Middle USA swath. 
start = 825000
stop = 835000
size = stop - start

times = satdata.variables['time'][start:stop]
lats = satdata.variables['lat'][start:stop]
lons = satdata.variables['lon'][start:stop]

toss = satdata.variables['CERES_SW_TOA_flux___upwards'][start:stop]

print('time: %i\tlat: %i\tlon: %i\ttos: %i\n' % \
    (times.size, lats.size, lons.size, toss.size))
#print('start time: %f\t stop time: %f\n' % \
#    (satdata.variables['time'][start], satdata.variables['time'][stop]))
begin = times[0]
end = times[times.size-1]
print('start time: %f\t stop time: %f\n' % (begin, end))

# # # # # # # # # # # #
# Plot datapoints.
x, y = m(lons, lats)
#Boulder
x1, y1 = m(-105, 40)
#L-20
#x2, y2 = m(-117.63, 35.7)

#m.plot(lons, lats, 'b*', markersize=8)
m.plot(x, y, 'g', linewidth=0.6)
m.plot(x1, y1, 'b.', markersize=8)

#plt.title("CERES Satelite Swath\nEquidistant Cylindrical Projection")
plt.title("CERES Satelite Swathover North America\n(North to South)")
plt.show()

# Save figure. 
fig.savefig("../images/Mid_Amer_cyl_proj.png")

#######################
# 3-D plot.
# # # # # # # # # # # #
            
index1 = 0
index2 = int(size/3)
index3 = 2*int(size/3)
index4 = size

# solar_avg_lats = [ [solar[time, i, j] for j in range(0, lonsSize)] for i in range(0, latsSize) ]
x1 = [ x[i] for i in range(index1, index2) ]
x2 = [ x[i] for i in range(index2, index3) ]
x3 = [ x[i] for i in range(index3, index4) ]
y1 = [ y[i] for i in range(index1, index2) ]
y2 = [ y[i] for i in range(index2, index3) ]
y3 = [ y[i] for i in range(index3, index4) ]

#X, Y, Z = [t, s1, 0]
fig = plt.figure()
#newax = fig.add_subplot(111, projection='3d')
newax = fig.gca(projection='3d')

# Create mesh at z-levels. 
x_pnts = np.arange(-120, -70, 1)
y_pnts = np.arange(25, 53, 1)
z_levels = np.arange(0, 3.1, 1)
#X, Y = np.meshgrid(X, Y)
X, Y = np.meshgrid(x_pnts, y_pnts)
#for z in z_levels:
#    newax.plot_wireframe(X, Y, z, rstride=10, cstride=10, color='red',
#        linewidth=.01, antialiased=False)
newax.plot_wireframe(X, Y, 0, rstride=10, cstride=10, color='magenta',
    linewidth=.01, antialiased=False)
newax.plot_wireframe(X, Y, 1, rstride=10, cstride=10, color='red',
    linewidth=.01, antialiased=False)
newax.plot_wireframe(X, Y, 2, rstride=10, cstride=10, color='green',
    linewidth=.01, antialiased=False)
newax.plot_wireframe(X, Y, 3, rstride=10, cstride=10, color='blue',
    linewidth=.01, antialiased=False)
                       
# Plot data.
newax.plot_wireframe(x, y, 0, rstride=10, cstride=10, color='magenta', \
        linewidth=.2)
newax.plot_wireframe(x1, y1, 1.0, rstride=10, cstride=10, \
    color='red', linewidth=0.2)
newax.plot_wireframe(x2, y2, 2.0, rstride=10, cstride=10, \
    color='green', linewidth=0.2)
newax.plot_wireframe(x3, y3, 3.0, rstride=10, cstride=10, \
    color='blue', linewidth=0.2)

newax.grid(True)

newax.set_zticks(np.arange(min(z_levels), max(z_levels) + 1, 1.0))

#layout = go.Layout(
#    autosize=False,
#    width=500,
#    height=500,
#    margin=Margin(
#        l=50,
#        r=50,
#        b=100,
#        t=100,
#        pad=4
#    ),
#    paper_bgcolor='#7f7f7f',
#    plot_bgcolor='#c7c7c7'
#)
# Plot size (doesn't work).
layout = go.Layout(
    autosize=False,
    #width=2000,
    height=2000,
)
# Set axes labels.
newax.set_xlabel('Longitude')
newax.set_ylabel('Latitude')
newax.set_zlabel('Time Slice')

newax.set_title('Satellite Swath Time Slices\n(Entire Swath on Level 0)')

# Save figure. 
fig.savefig("../images/Mid_Amer_cyl_proj-3D.png")

#######################


