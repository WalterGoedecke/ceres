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
#m = Basemap(llcrnrlon=-145.5,llcrnrlat=1.,urcrnrlon=-2.566,urcrnrlat=46.352,\
#            rsphere=(6378137.00,6356752.3142),\
#            resolution='l',area_thresh=1000.,projection='lcc',\
#            lat_1=50.,lon_0=-107.,ax=ax)
m = Basemap(llcrnrlon=-118.5,llcrnrlat=35.0,urcrnrlon=-116.0,urcrnrlat=37.0,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',area_thresh=1000.,projection='lcc',\
            lat_1=35.,lon_0=-116.,ax=ax)
            
# transform to nx x ny regularly spaced 5km native projection grid
nx = int((m.xmax-m.xmin)/5000.)+1; ny = int((m.ymax-m.ymin)/5000.)+1
topodat = m.transform_scalar(topoin,lons,lats,nx,ny)
# plot image over map with imshow.
im = m.imshow(topodat,cm.GMT_haxby)

#######################
# Plot chalk sites. 
# # # # # # # # # # # #
# L-20. 
L20lat = 35.699390
L20lon = -117.626023
x, y = m(L20lon, L20lat)
#m.plot(x, y, 'ko', markersize=3)
m.plot(x, y, 'k^', markersize=3)
#plt.text(x, y, 'L', fontsize=14, fontweight='bold', ha='center', va='center', color='b')
label = 'L-20'
#z = zip(labels, x, y)
#plt.text(x+10000, y+5000, label, fontsize=5)
plt.text(x+.02, y+.02, label, fontsize=5)
# # # # # # # # # # # #
# Rotr1. 
R1lat = 35.76873778
R1lon = -117.7756747
x, y = m(R1lon, R1lat)
m.plot(x, y, 'bo', markersize=2)
label = 'ROTR 1'
plt.text(x+.02, y+.02, label, fontsize=5)
# # # # # # # # # # # #
# Rotr2. 
R2lat = 35.85866406
R2lon = -117.5768854
x, y = m(R2lon, R2lat)
m.plot(x, y, 'ro', markersize=2)
label = 'ROTR 2'
plt.text(x+.02, y+.02, label, fontsize=5)
# # # # # # # # # # # #
# Rotr3. 
R3lat = 35.77147283
R3lon = -117.7761122
x, y = m(R3lon, R3lat)
m.plot(x, y, 'go', markersize=2)
label = 'ROTR 3'
plt.text(x+.02, y-.04, label, fontsize=5)
# # # # # # # # # # # #
# Rotr4. 
R4lat = 35.89375766
R4lon = -117.6123566
x, y = m(R4lon, R4lat)
m.plot(x, y, 'yo', markersize=2)
label = 'ROTR 4'
plt.text(x+.02, y+.02, label, fontsize=5)
# # # # # # # # # # # #
# B-mtn. 
lat = 35.666088
lon = -117.598263
x, y = m(lon, lat)
m.plot(x, y, 'y+', markersize=2)
label = 'B-Mtn'
plt.text(x+.02, y-.05, label, fontsize=5)
# # # # # # # # # # # #
# Telescope Pk. 
lat = 36.169827
lon = -117.089208
x, y = m(lon, lat)
m.plot(x, y, 'b+', markersize=2)
label = 'Telescope Pk'
plt.text(x+.02, y+.02, label, fontsize=5)
#######################

#######################
# Read & plot data file. 
# # # # # # # # # # # #
data_file = open('datasets/rtr4-dec.lle')

lats, lons = [], []
for index, line in enumerate(data_file.readlines()):
    lats.append(float(line.split()[1]))
    lons.append(float(line.split()[2]))
    
    #lat = float(line.split()[1])
    #lon = float(line.split()[2])
    #print('%i\t %f\t %f\n' % (index, lat, lon))
    
# Plot datapoints.
x, y = m(lons, lats)
m.plot(x, y, 'r.', markersize = 1)

#######################

# draw coastlines and political boundaries.
m.drawcoastlines()
m.drawcountries()
m.drawstates()
# draw parallels and meridians.
# label on left and bottom of map.
parallels = np.arange(0.,80,20.)
m.drawparallels(parallels,labels=[1,0,0,1])
meridians = np.arange(10.,360.,30.)
m.drawmeridians(meridians,labels=[1,0,0,1])
# add colorbar
cb = m.colorbar(im,"right", size="5%", pad='2%')
ax.set_title('IWV - ETOPO5 Topography - Lambert Conformal Conic')
plt.show()

# Save figure. 
fig.savefig("IWV_topo_bath_lambert.png")
