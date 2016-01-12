from django.db import models
from django.contrib import admin

#Python imports
from django.template.defaultfilters import slugify
import datetime 

# Import python settings, and defintion from app.
from memorial.settings import MEDIA_ROOT
#from classic import SfsLight

# Geocoders
#import pygeocoder, geocoder
# Pandas et al.
#import pandas, pvlib
#from pvlib.location import Location 
# Matplotlib routinesl.
#import matplotlib
#matplotlib.use('Agg') # Must have here - not after from matplotlib.~ commands. 
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.backends.backend_agg import FigureCanvasAgg
#from matplotlib.figure import Figure
#from matplotlib import pyplot

# Create your models here.

class MyProfile(models.Model):
    user = models.OneToOneField("auth.User")
    #date_of_birth = models.DateField()
    bio = models.TextField()

class Calculation(models.Model):
    # Geocode variables. 
    address = models.TextField(max_length=120, blank=True, null=True, verbose_name='Address')
    address_slug = models.SlugField(max_length=120, blank=True, null=True)
    formatted_address = models.TextField(max_length=120, null=True, blank=True)
    coordinates = models.CharField(max_length=80, blank=True, null=True, verbose_name='latitude, longitude')
    #elevation = models.CharField(max_length=60, blank=True, null=True, verbose_name='Elevation (AMSL)', default="None'")
    elevation = models.FloatField(default=0.0, blank=True, null=True)
    # Panda variables. 
    begin = models.CharField(max_length=30, default='2015, 7, 1, 11', blank=True, null=True)
    end = models.CharField(max_length=30, default='2015, 7, 1, 12', blank=True, null=True)
    frequency = models.CharField(max_length=20, default='3Min', blank=True, null=True)
    time_sequence = models.TextField(max_length=600, null=True, blank=True)
    # pvlib variables. 
    ephem_sequence = models.TextField(max_length=600, null=True, blank=True)
    statistics = models.TextField(max_length=300, null=True, blank=True)
    irradiance_sequence = models.TextField(max_length=600, null=True, blank=True)
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

    def save(self, *args, **kwargs):
        super(Calculation, self).save()

class CalculationAdmin(admin.ModelAdmin):
    search_fields = ["address"]
    display_fields = ["address"]
    # Creates a slug name within ~/admin/. 
    prepopulated_fields = {
                           "address_slug": ("address",), 
}


