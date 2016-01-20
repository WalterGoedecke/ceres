# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:43:05 2015

@author: walter
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:07:57 2015

@author: walter
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
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
#tosses = Dataset('../datasets/tos_O1_2001-2002.nc')
tosses = Dataset('../datasets/CERES_SSF_XTRK-MODIS_Edition3A_Subset_2014010100-2014010223.nc')

#start = 0
#stop = 100000
# Middle USA swath. 
start = 825000
stop = 835000

times = tosses.variables['time'][start:stop]
lats = tosses.variables['lat'][start:stop]
lons = tosses.variables['lon'][start:stop]

#toss = tosses.variables['tos'][12,:]
#sw_all = toa_data.variables['toa_sw_all_mon'][:, :, :]
#sw_up = tosses.variables['CERES_SW_TOA_flux___upwards'][:, :, :]

toss = tosses.variables['CERES_SW_TOA_flux___upwards'][start:stop]

print('time: %i\tlat: %i\tlon: %i\ttos: %i\n' % \
    (times.size, lats.size, lons.size, toss.size))

# Plot datapoints.
#lons, lats = np.meshgrid(lons, lats)
print('Regridded lat & lon: %i\t %i\n' % \
    (lats.size, lons.size))

#######################
# create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
m = Basemap(projection='kav7',lon_0=0,resolution='c')
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
x, y = m(lons, lats)
#Boulder
x1, y1 = m(-105, 40)
#L-20
x2, y2 = m(-117.63, 35.7)

#m.plot(lons, lats, 'b*', markersize=8)
m.plot(x, y, 'r', markersize=0)
m.plot(x1, y1, 'b.', markersize=8)
m.plot(x2, y2, 'c.', markersize=8)
        
# add colorbar
#cb = m.colorbar(tossed,"bottom", size="5%", pad="2%")

#ax.set_title('SST and ICE analysis for %s'%date)
ax.set_title('Satelite View Surface')
plt.show()

# Save figure. 
fig.savefig("../images/CERES_sat_footprint_kav7_proj.png")

