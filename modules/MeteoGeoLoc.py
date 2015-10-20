"""
module: MeteoGeoLoc
"""

import os
import geocoder

def addressToLocation(address):

    gLatLon = geocoder.location(address)
    gEl = geocoder.elevation(address)
    return gLatLon.lng, gLatLon.lat, gEl.elevation

def strAbsLonLat(lon, lat):

    if (lon >= 0.0):
        strLon = "%5.2f E" % lon
    else:
        strLon = "%5.2f W" % abs(lon)

    if (lat >= 0.0):
        strLat = "%4.2f N" % lat
    else:
        strLat = "%4.2f S" % abs(lat)

    return strLon, strLat

if __name__ == "__main__":

    broomfield = addressToLocation("Broomfield, CO")
    print(broomfield)

