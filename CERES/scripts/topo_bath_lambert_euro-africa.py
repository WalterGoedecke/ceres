from mpl_toolkits.basemap import Basemap, shiftgrid, cm
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset

# read in etopo5 topography/bathymetry.
url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'
etopodata = Dataset(url)

topoin = etopodata.variables['ROSE'][:]
lons = etopodata.variables['ETOPO05_X'][:]
lats = etopodata.variables['ETOPO05_Y'][:]
# shift data so lons go from -180 to 180 instead of 20 to 380.
topoin,lons = shiftgrid(180.,topoin,lons,start=False)

# plot topography/bathymetry as an image.

# create the figure and axes instances.
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# setup of basemap ('lcc' = lambert conformal conic).
# use major and minor sphere radii from WGS84 ellipsoid.
m = Basemap(llcrnrlon=0.0,llcrnrlat=20.,urcrnrlon=120.0,urcrnrlat=46.352,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',area_thresh=1000.,projection='lcc',\
            lat_1=50.,lon_0=70.,ax=ax)

# transform to nx x ny regularly spaced 5km native projection grid
nx = int((m.xmax-m.xmin)/5000.)+1; ny = int((m.ymax-m.ymin)/5000.)+1
topodat = m.transform_scalar(topoin,lons,lats,nx,ny)
# plot image over map with imshow.
im = m.imshow(topodat,cm.GMT_haxby)

#######################
# Read & plot netcdf data file. 
# # # # # # # # # # # #
#root_grp = Dataset('datasets/example_wind_fields.nc')
root_grp = Dataset('datasets/WMI_Lear.nc')

#lats = root_grp.variables['latitude'][0:179]
#lons = root_grp.variables['longitude'][0:179]
lats = root_grp.variables['latitude'][:]
lons = root_grp.variables['longitude'][:]

#latlen = len(lats)
#lonlen = len(lons)
#print('Lat: %i\tLon: %i\n' % (latlen, lonlen))

# Plot datapoints.
x, y = m(lons, lats)
#m.plot(x, y, 'k', markersize = 1)
#m.plot(x, y, 'b.', markersize = 1)
m.plot(x, y, 'b', linewidth = 1.5)
#######################

#######################
# Read & plot netcdf data file. 
# # # # # # # # # # # #
root_grp = Dataset('datasets/tos_O1_2001-2002.nc')

lats = root_grp.variables['lat'][:]
lons = root_grp.variables['lon'][:]

latlen = len(lats)
lonlen = len(lons)
print('Lat: %i\tLon: %i\n' % (latlen, lonlen))

# Plot datapoints.
#for lon in lons:
for index, lon in enumerate(lons):
    if index == 39:
        for index, lat in enumerate(lats):
            if index == 39:
                x, y = m(lon, lat)
                m.plot(x, y, 'co', markersize = 2)

#######################

# draw coastlines and political boundaries.
m.drawcoastlines()
m.drawcountries()
m.drawstates()

# draw parallels and meridians.
# label on left and bottom of map.
parallels = np.arange(0.,80,20.)
m.drawparallels(parallels,labels=[1,0,0,1])
meridians = np.arange(0., 360., 15.)
m.drawmeridians(meridians,labels=[1,0,0,1])
# add colorbar
cb = m.colorbar(im,"right", size="5%", pad='2%')
ax.set_title('ETOPO5 Topography - Lambert Conformal Conic')
plt.show()

# Save figure. 
fig.savefig("topo_bath_lambert_euro-africa.png")
