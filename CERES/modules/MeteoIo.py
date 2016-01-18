"""
module: MeteoIo
"""

import collections
import os
import numpy
from scipy.io import netcdf

def ncOpen(nameFile):
    idFile = netcdf.netcdf_file(nameFile, "r", mmap = False)
    print("MeteoIo.ncOpen:opening:", nameFile)
    return idFile

def ncRead(idFile, nameVar):
    data = idFile.variables[nameVar][:]
    print("MeteoIo.ncRead:reading:", nameVar)
    return data

def ncCreate(nameFile):
    idFile = netcdf.netcdf_file(nameFile, "w", version=2)
    print("MeteoIo.ncCreate:creating:", nameFile)
    return idFile

def ncWriteTimeSeries(idFile, time, dictVars, dictUnits):
    idFile.createDimension("time", len(time))
    for nameVar in dictVars:
        print("MeteoIo.ncWriteTimeSeries:creating:", nameVar)
        idVar = idFile.createVariable(nameVar, "float64", ["time"])
        idVar[:] = dictVars[nameVar]
        idVar.units = dictUnits[nameVar]

def strPairToTuple(strPair):
    # "(a, b)" to (a, b), a and b real
    strLocal = strPair.replace("(","").replace(")", "")
    strLocal = strLocal.replace("\n", "").split(",")
    return (float(strLocal[0]), float(strLocal[1]))

def readSites(nameFile):
    dictCoords = collections.OrderedDict()
    dictTags = collections.OrderedDict()
    for line in open(nameFile):
        name, coords, tag = line.split(";")
        dictCoords[name.strip()] \
            = strPairToTuple(coords)
        dictTags[name.strip()] = tag
    return dictCoords, dictTags

def readRegions(nameFile):
    dictRegions = collections.OrderedDict()
    for line in open(nameFile):
        name, coordsBottomLeft, coordsUpperRight \
            = line.split(";")
        dictRegions[name.strip()] = \
            (strPairToTuple(coordsBottomLeft),
             strPairToTuple(coordsUpperRight))
    return dictRegions

if __name__ == "__main__":

    pass

