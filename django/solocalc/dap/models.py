# Matplotlib routines.
# Must be at top of models; otherwise, tcl error!
import matplotlib
matplotlib.use('Agg') # Must have here - not after from matplotlib.~ commands. 

from django.db import models
from django.contrib import admin
###############################
# New imports for SolarFS form. 
# # # # # # # # # # # # # # # # 
#Python imports
from django.template.defaultfilters import slugify
import datetime 

# Import python settings, and defintion from app.
from solocalc.settings import MEDIA_ROOT
from dap import SfsLight, PlotPrefs

# Geocoders
import pygeocoder, geocoder
# Pandas et al.
import pandas, pvlib
from pvlib.location import Location 

#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib import pyplot
import numpy as np

# Import mapping functions. 
from mpl_toolkits.basemap import Basemap

# OPeNDAP netCDF4.
import netCDF4 
from netCDF4 import Dataset 

###############################

# Create your models here.
###############################
# New models for SolarFS form. 
# # # # # # # # # # # # # # # # 
class Calculation(models.Model):
    # Geocode variables.
    address = models.TextField(max_length=120, blank=True, null=True, verbose_name='Address', default='3210 Dartmouth Ave, Boulder, CO')
    address_slug = models.SlugField(max_length=120, blank=True, null=True)
    formatted_address = models.TextField(max_length=120, null=True, blank=True)
    coordinates = models.CharField(max_length=80, blank=True, null=True, verbose_name='latitude, longitude')
    #elevation = models.CharField(max_length=60, blank=True, null=True, verbose_name='Elevation (AMSL)', default="None'")
    elevation = models.FloatField(default=0.0, blank=True, null=True)
    # Panda variables. 
    #begin = models.CharField(max_length=30, default='2015, 7, 1, 11', blank=True, null=True)
    begin = models.CharField(max_length=30, blank=True, null=True)
    begin_slug = models.SlugField(max_length=120, blank=True, null=True)
    #end = models.CharField(max_length=30, default='2015, 7, 1, 12', blank=True, null=True)
    end = models.CharField(max_length=30, blank=True, null=True)
    frequency = models.CharField(max_length=20, default='10 min', blank=True, null=True)
    time_sequence = models.TextField(max_length=600, null=True, blank=True)
    # pvlib variables. 
    ephem_sequence = models.TextField(max_length=6000, null=True, blank=True)
    statistics = models.TextField(max_length=300, null=True, blank=True)
    irradiance_sequence = models.TextField(max_length=6000, null=True, blank=True)
    # dap_process variable. 
    #dap_process_temp = models.TextField(max_length=60, null=True, blank=True)
    # Solar panel specs.  
    panel_azimuth = models.FloatField(max_length=20, default=180, blank=True, null=True, verbose_name='Panel azimuth (degrees from north)')
    panel_tilt = models.FloatField(max_length=20, default=30, blank=True, null=True, verbose_name='Panel tilt (degrees from vertical)')
    doc =  models.CharField(max_length=80, blank=True, null=True)
    pix1 =  models.CharField(max_length=80, blank=True, null=True)
    pix2 =  models.CharField(max_length=80, blank=True, null=True)
    pix3 =  models.CharField(max_length=80, blank=True, null=True)

    # Creates a slug name. 
    prepopulated_fields = {
                           "address_slug": ("address",),
    }
    
    def __str__(self):
        return self.address
        #return '%s %s' % (self.question, self.answer)

    # Gets latitude & longitude from address. 
    def address2llh(self, address):
        geoAddress = pygeocoder.Geocoder.geocode(self.address)
        self.formatted_address = geoAddress.formatted_address
        self.coordinates = geoAddress.coordinates

        # Use geocoder to get elevation in meters AMSL. 
        elevation = self.address2elev(self.address)
        self.elevation = elevation
        # pyemphem requires a numeric elevation value. 
        return Location(*geoAddress.coordinates, altitude = elevation, name = self.address)
        
    # geocoder gets elevation from address. (g.location) returns lat, long 
    def address2elev(self, address):
        g = geocoder.elevation(address)
        elevation = g.elevation
        if elevation is None:    
            elevation = 0    
        return elevation
    
    def ephemeris(self, begin, end, frequency):
        location = self.address2llh(self.address)

        # Invoke panda routine.
        strBegin = begin.split(',')
        intBegin = [int(x) for x in strBegin]
        strEnd = end.split(',')
        intEnd = [int(x) for x in strEnd]

        # Avoids the "..." ellipsis that appear in data. 
        pandas.set_option('display.max_rows', 1000000)
    
        timeSequence = pandas.date_range(
            start=datetime.datetime(intBegin[0], intBegin[1], intBegin[2], intBegin[3]), 
            end=datetime.datetime(intEnd[0], intEnd[1], intEnd[2], intEnd[3]), freq = frequency)
        #self.time_sequence = timeSequence

        ##################
        # Solar ephemeris.
        # # # # # # # # # # # # # 
        ephemSequence = pvlib.solarposition.pyephem(
            timeSequence, location).drop(
                ['apparent_elevation', 'apparent_azimuth', 
                'apparent_zenith', 'elevation'], axis=1)
        self.ephem_sequence = ephemSequence
        # Create plot figure file. 
        ephemSequence.plot()
        pix1_name = 'ephem_' + self.address_slug + '_' + self.begin_slug + '.png' 
        self.pix1 = pix1_name
        plot_path = MEDIA_ROOT + 'plots/' + pix1_name
        pyplot.savefig(plot_path)
        ##################

        # Solar ephemeris. 
        eph_seq = str(ephemSequence)
        eph_seq_lines = eph_seq.split('\n')
        self.time_sequence = eph_seq_lines

        # Compute statistics. 
        self.statistics  = ephemSequence.describe()

        ##################
        # Solar specifications.
        # # # # # # # # # # # # # 
        location = self.address2llh(self.address)
        solarZenith = ephemSequence['zenith']
        solarAzi = ephemSequence['azimuth']
        irradianceSequence = pvlib.clearsky.ineichen(timeSequence, location)
        
        DNI = irradianceSequence['dni']
        DB = SfsLight.directBeam(self.panel_tilt, solarZenith, self.panel_azimuth-solarAzi, DNI)  

        irradianceSequence['DB'] = DB
        self.irradiance_sequence = irradianceSequence

        irradianceSequence.plot()
        pix2_name = 'irrad_' + self.address_slug + '_' + self.begin_slug + '.png' 
        self.pix2 = pix2_name
        plot_path = MEDIA_ROOT + 'plots/' + pix2_name
        pyplot.savefig(plot_path)
        ##################

        # Create plot figure file. 
        '''ephemSequence.plot()
        plot_path = MEDIA_ROOT + 'plots/ephemSequence.png'
        pyplot.savefig(plot_path)'''

        return

    # This routine creates plots from the OPeNDAP server data. 
    def DapProcess(self, begin):
        # # # # # # # # # # # # # 
        # Construct URL to opendap server.
        # # # # # # # # # # # # # 
        # Extract year and month from 'begin' variable.
        year = begin.split(',')[0].strip()
        month = begin.split(',')[1].strip()
        year_month = year + month
        
        # Create file name. 
        site_name = 'http://goldsmr4.sci.gsfc.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNXRAD.5.12.4/'
       
        file_prefix = '/MERRA2_300.tavgM_2d_rad_Nx.'
        file_suffix = '.nc4'
        #file_name = 'MERRA2_300.tavgM_2d_rad_Nx.200101.nc4'
        file_name = file_prefix + year_month + file_suffix
        
        path_name = site_name + year + file_name
        # # # # # # # # # # # #

        # # # # # # # # # # # #
        # Create data objects.
        #toa_data = Dataset('../datasets/CERES_EBAF-TOA_Ed2.8_Subset_201401-201412_solar-sw-lw-net.nc')
        #toa_data = Dataset('../datasets/MERRA301.prod.assim.tavg1_2d_rad_Nx.20010101.SUB.nc')
        #toa_data = Dataset('http://goldsmr4.sci.gsfc.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNXRAD.5.12.4/2001/MERRA2_300.tavgM_2d_rad_Nx.200101.nc4')
        toa_data = Dataset(path_name)
        
        # Set variables.
        times = toa_data.variables['time'][:]
        lats = toa_data.variables['lat'][:]
        lons = toa_data.variables['lon'][:]
        
        # Short-wave incoming top of atmosphere radiation. 
        sw_down = toa_data.variables['SWTDN'][:, :, :]
        # Long wave outgoing top of atmosphere radiation. 
        lw_up = toa_data.variables['LWTUP'][:, :, :]
        # Short-wave net outgoing top of atmosphere all sky incoming radiation. 
        sw_net = toa_data.variables['SWTNT'][:, :, :]

        # Create shortwave outgoing radiation. 
        sw_up = sw_down - sw_net

        timesSize = times.size
        latsSize = lats.size
        lonsSize = lons.size

        # # # # # # # # # # # #
        # Calculate and plot the albedo: the ratio of the outgoing to incoming sw radiation. 
        #3d array example (3x4x5 with values set at 2): l_variable = [[[2]*3]*4]*5
        # 2d mxn array example: a = [[init_value]*n for x in xrange(m)]
        albedo = [[0]*lonsSize]*latsSize # 2d array, lonsSize x latsSize
        #albedo = sw_up
        
        #i = lat, j = lon
        #for i in range(0, latsSize):
            #albedo[0, i] = [None if y == 0 else x/y for x, y in zip(sw_up[0, i], sw_down[0, i])]
            #albedo[:, i] = [None if y == 0 else x/y for x, y in zip(sw_up[0, :, i], sw_down[0, :, i])]
            #albedo[i] = [None if y == 0 else x/y for x, y in zip(sw_up[0, :, i], sw_down[0, :, i])]
            #albedo[0, i] = [x-y for x, y in zip(sw_down[0, i], sw_net[0, i])] # Works.
            #albedo[0, i] = sw_down[0, i] - sw_net[0, i] # Works.
            #albedo[i] = sw_down[i] - sw_net[i] # Works.

        sw_in = [[0]*lonsSize]*latsSize
        sw_out = [[0]*lonsSize]*latsSize
        for i in range(0, latsSize):
            sw_in[i] = sw_down[0, i]
            sw_out[i] = sw_up[0, i]
            #albedo[i] = [None if y == 0 else x/y for x, y in zip(sw_out[i], sw_in[i])]
            #albedo[i] = [x-y for x, y in zip(sw_down[i], sw_net[i])]

#         for i in range(0, latsSize):
#             #sw_in[i] = sw_down[0, i]
#             #sw_out[i] = sw_up[0, i]
#             albedo[i] = [None if y == 0 else x/y for x, y in zip(sw_out[i], sw_in[i])]
#             #albedo[i] = [x-y for x, y in zip(sw_down[i], sw_net[i])]
#             if sw_in[i] == 0:
#                 albedo[i] = 0
#             else:
#                 albedo[i] = sw_out[i]/sw_in[i]
                
        # # # # # # # # # # # #
        # create figure, axes instances.
        #fig = plt.figure()
        fig = pyplot.figure()
        ax = fig.add_axes([0.05,0.05,0.9,0.9])

        # Create Basemap instance.
        m = Basemap(projection='kav7', lon_0=0, resolution='c')
        #m = Basemap(projection='kav7', lon_0=0, resolution='l')

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

        #solars = m.pcolormesh(meshlons, meshlats, albedo, shading='flat', cmap=pyplot.cm.jet, \
        #    latlon=True)
        solars = m.pcolormesh(meshlons, meshlats, sw_out, shading='flat', cmap=pyplot.cm.jet, \
            latlon=True)
            
        # add colorbar
        cb = m.colorbar(solars, "bottom", size="5%", pad="2%")
        #cb.set_label('Albedo (0 - 1.0)')
        cb.set_label('Radiative Flux $(W/m^2)$')
        
        title = 'World Albedo Average for ' + month + '/' + year
        ax.set_title(title)
        #pyplot.show()
        
        # Save figure. 
        fig.savefig("/home/dv8000/virtualenv/temp/MERRA-world_albedo-kav7_proj.png")
        
        # # # # # # # # # # # #
        # Create plot figure file. 
        #ephemSequence.plot()
        pix1_name = 'MERRA-world_albedo-kav7_proj_' + year_month + '.png' 
        self.pix1 = pix1_name
        plot_path = MEDIA_ROOT + 'plots/' + pix1_name
        pyplot.savefig(plot_path)
        ##################

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
        fig = pyplot.figure()
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
        
        lw_out_plot = m.pcolormesh(meshlons, meshlats, lw_out, shading='flat', cmap=pyplot.cm.jet, \
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
                
        title = 'World Long Wave Emittivity, Average for ' + month + '/' + year
        ax.set_title(title)
        #plt.show()
        
        # Create plot figure file. 
        # Save figure. 
        #fig.savefig("../images/MERRA-world-lw_out_-kav7_proj.png")
        pix2_name = 'MERRA-world-lw_out_-kav7_proj_' + year_month + '.png' 
        self.pix2 = pix2_name
        plot_path = MEDIA_ROOT + 'plots/' + pix2_name
        pyplot.savefig(plot_path)
        
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
        fig = pyplot.figure()
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
        
        net_in_plot = m.pcolormesh(meshlons, meshlats, net_in, shading='flat', cmap=pyplot.cm.jet, \
            latlon=True)
            
        # add colorbar
        cb = m.colorbar(net_in_plot, "bottom", size="5%", pad="2%")
        cb.set_label('Radiative Flux $(W/m^2)$')
        
        title = 'Net Incomming Short Wave Solar Flux\n Average for ' + month + '/' + year
        ax.set_title(title)
        #plt.show()
        
        # Save figure. 
        #fig.savefig("../images/MERRA-world-net_in-kav7_proj.png")
        #fig.savefig("../images/MERRA-world-lw_out_-kav7_proj.png")
        pix3_name = 'MERRA-world-net_in-kav7_proj_' + year_month + '.png' 
        self.pix3 = pix3_name
        plot_path = MEDIA_ROOT + 'plots/' + pix3_name
        pyplot.savefig(plot_path)
        
        #######################

        return (year, month, path_name, timesSize)

    # Write data to file, that can be downloaded. 
    def write_data(self):
        doc_name = 'SolarFS_' + self.address_slug + '_' + self.begin_slug + '.dat' 
        self.doc = doc_name

        data_path = MEDIA_ROOT + 'docs/' + doc_name
        f = open(data_path,"w")
        f.write('Formatted address: %s\n' % self.formatted_address)
        f.write('Coordinates (latitude, longitude): %s\n' % str(self.coordinates))
        f.write('Elevation: (meters AMSL) %s\t(feet): %f\n\n' % ( str(self.elevation), self.elevation/0.3048 ))
        #### Pandas time sequence ####
        f.write('Time sequence:\n')
        f.write('Start: %s\n' % self.begin)
        f.write('Stop: %s\n' % self.end)
        f.write('Frequency: %s\n\n' % self.frequency)
        #### #### ####
        f.write('Ephemeris:\n %s\n\n' % self.ephem_sequence)
        f.write('Statistics:\n %s\n\n' % self.statistics)
        f.write('Irradiance:\n %s\n\n' % self.irradiance_sequence)
        #### #### ####
        #f.write('Dap Process:\n %s\n\n' % self.dap_process_temp)
        #### #### ####
        f.close()
        return
    
    def save(self, *args, **kwargs):
        # Create slug of address. 
        self.address_slug = slugify(self.address)
        # Create slug of beginning time. 
        self.begin_slug = slugify(self.begin)
        # Invoke 'address2llh' function. . 
        self.formatted_address = self.address2llh(self.address)
        # Solar calculations.
        self.ephemeris(self.begin, self.end, self.frequency)
        # Solar calculations.
        self.DapProcess(self.begin)
        # Write data to file. 
        self.write_data()
        # Save all. 
        super(Calculation, self).save()

class CalculationAdmin(admin.ModelAdmin):
    search_fields = ["address"]
    display_fields = ["address"]
    # Creates a slug name within ~/admin/. 
    prepopulated_fields = {
                           "address_slug": ("address",), 
                           "begin_slug": ("begin",), 
}

###############################