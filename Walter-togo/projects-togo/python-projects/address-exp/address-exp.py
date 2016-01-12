# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:18:03 2015

@author: walter
"""
# Prototype to many things.  

import datetime #Python imports
# Geocoders
import pygeocoder, geocoder
from geopy import geocoders

import numpy, pandas, matplotlib #Anaconda imports
#import pvlib, seaborn #Misc. imports
#from pvlib.location import Location 
#from matplotlib import pyplot

# Gets latitude & longitude from address. 
def address2llh(address):
    geoBoulder = pygeocoder.Geocoder.geocode(address)
    #print(geoBoulder.coordinates)
    # Use geocoder to get elevation in meters AMSL. 
    #g = geocoder.elevation(address)
    #print(g.location) # Returns lat, long
    #elevation = g.elevation
    
#    return Location(*geoBoulder.coordinates, 
#                    altitude = elevation, name = address)
    #return *geoBoulder.coordinates, altitude = elevation, name = address
    return (geoBoulder.formatted_address, geoBoulder.coordinates)
    
# Gets elevation from address. 
def address2elev(address):
    # geocoder
    g = geocoder.elevation(address)
    #print(g.location) # Returns lat, long
    elevation = g.elevation
    
    return elevation
    
if __name__ == "__main__":
    #pass
    # Get latitude & longitude from address. 
    #address = "boulder, colorado"
    #address = "3210 Dartmouth Avenue, boulder, colorado"
    #address = "12th and North Avenue, Grand Junction, CO"
    #address = "salt lake city, ut"
    address = "colfax, ca"
    #address = "tucson, arizona"
    
    
    [location, coordinates] = address2llh(address)
    #print(location)
    print('\nLocation:\n%s' % location)
    print('\nCoordinates:')
    print(coordinates)
    print()
    [lat, lng] = coordinates
    
    g = geocoders.GoogleV3()
    timezone = g.timezone((lat, lng))    
    #timezone = g.timezone(coordinates)    
    print('\nTimezone:\n%s' % timezone)
    
    print('\nTimezone:')
    timezone
    print(timezone._tzname)
    print()
    
    #elevation = address2elev(address)
    #print('Elevation: %s meters\n' % elevation)
    
    timeSequence = pandas.date_range(
#        start=datetime.datetime(2015,7,30,15), 
#        end=datetime.datetime(2015,7,30,16), freq='3Min')
    start=datetime.datetime(2015,7,1, 11), 
    end=datetime.datetime(2015,7,1, 12), freq='3Min')
    print('Time sequence:\n', timeSequence)
    

    


