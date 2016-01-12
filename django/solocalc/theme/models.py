
from django.db import models
from django.template import RequestContext, Template, TemplateSyntaxError
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import Orderable, SiteRelated
from mezzanine.core.request import current_request
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

from django.contrib import admin
###############################
# New imports for SolarFS form. 
# # # # # # # # # # # # # # # # 

#Python imports
from django.template.defaultfilters import slugify
import datetime 

# Import python settings, and defintion from app.
from solocalc.settings import MEDIA_ROOT
from theme import SfsLight

# Geocoders
import pygeocoder, geocoder
# Pandas et al.
import pandas, pvlib
from pvlib.location import Location 
# Matplotlib routinesl.
import matplotlib
matplotlib.use('Agg') # Must have here - not after from matplotlib.~ commands. 
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib import pyplot

###############################

DEFAULT_COPYRIGHT = '&copy {% now "Y" %} {{ settings.SITE_TITLE }}'

class SiteConfiguration(SiteRelated):
    '''
    A model to edit sitewide content
    '''
    col1_heading = models.CharField(max_length=200, default="Contact us")
    col1_content = RichTextField()
    col2_heading = models.CharField(max_length=200, default="Go social")
    col2_content = RichTextField(blank=True, 
                                 help_text="If present will override the "
                                           "social network icons.")
    col3_heading = models.CharField(max_length=200, default="Subscribe")
    col3_content = RichTextField()
    twitter_link = models.CharField(max_length=2000, blank=True)
    facebook_link = models.CharField(max_length=2000, blank=True)
    pinterest_link = models.CharField(max_length=2000, blank=True)
    youtube_link = models.CharField(max_length=2000, blank=True)
    github_link = models.CharField(max_length=2000, blank=True)
    linkedin_link = models.CharField(max_length=2000, blank=True)
    vk_link = models.CharField(max_length=2000, blank=True)
    gplus_link = models.CharField(max_length=2000, blank=True)
    has_social_network_links = models.BooleanField(default=False, blank=True)
    copyright = models.TextField(default=DEFAULT_COPYRIGHT)

    class Meta:
        verbose_name = _('Site Configuration')
        verbose_name_plural = _('Site Configuration')

    def save(self, *args, **kwargs):
        '''
        Set has_social_network_links
        '''
        if (self.twitter_link or self.facebook_link or self.pinterest_link or
            self.youtube_link or self.github_link or self.linkedin_link or
            self.vk_link or self.gplus_link):
            self.has_social_network_links = True
        else:
            self.has_social_network_links = False
        super(SiteConfiguration, self).save(*args, **kwargs)

    
    def render_copyright(self):
        '''
        Render the footer
        '''
        c = RequestContext(current_request())
        try:
            t = Template(self.copyright)
        except TemplateSyntaxError:
            return ''
        return t.render(c)


class HomePage(Page):
    '''
    A home page page type
    '''
    heading = models.CharField(max_length=100)
    slide_in_one_icon = models.CharField(max_length=50, blank=True)
    slide_in_one = models.CharField(max_length=200, blank=True)
    slide_in_two_icon = models.CharField(max_length=50, blank=True)
    slide_in_two = models.CharField(max_length=200, blank=True)
    slide_in_three_icon = models.CharField(max_length=50, blank=True)
    slide_in_three = models.CharField(max_length=200, blank=True)
    header_background = FileField(verbose_name=_("Header Background"),
        upload_to=upload_to("theme.HomePage.header_background", "homepage"),
        format="Image", max_length=255, blank=True)
    header_image = FileField(verbose_name=_("Header Image (optional)"),
        upload_to=upload_to("theme.HomePage.header_image", "homepage"),
        format="Image", max_length=255, blank=True, null=True)
    welcome_heading = models.CharField(max_length=100, default="Welcome")
    content = RichTextField()
    recent_blog_heading = models.CharField(max_length=100,
        default="Latest blog posts")
    number_recent_posts = models.PositiveIntegerField(default=3,
        help_text="Number of recent blog posts to show")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class IconBox(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="boxes")
    icon = models.CharField(max_length=50,
        help_text="Enter the name of a font awesome icon, i.e. "
                  "fa-eye. A list is available here "
                  "http://fontawesome.io/")
    title = models.CharField(max_length=200)
    link_text = models.CharField(max_length=100)
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the box will go here.")

###############################
# New models for SolarFS form. 
# # # # # # # # # # # # # # # # 
class Calculation(models.Model):
    # Geocode variables. 
    address = models.TextField(max_length=120, blank=True, null=True, verbose_name='Address')
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
    # Solar panel specs.  
    panel_azimuth = models.FloatField(max_length=20, default=180, blank=True, null=True, verbose_name='Panel azimuth (degrees from north)')
    panel_tilt = models.FloatField(max_length=20, default=30, blank=True, null=True, verbose_name='Panel tilt (degrees from vertical)')
    doc =  models.CharField(max_length=80, blank=True, null=True)
    pix1 =  models.CharField(max_length=80, blank=True, null=True)
    pix2 =  models.CharField(max_length=80, blank=True, null=True)

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