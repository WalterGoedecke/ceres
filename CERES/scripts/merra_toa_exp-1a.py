# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:51:48 2015

@author: walter
"""
from netCDF4 import Dataset #, date2index
import numpy as np
from pylab import *
# Add directory to path. 
import sys
sys.path.insert(0, "../modules")
import MeteoPlot

# Calculate monthly averages. 
def process_dataset(dataset):
    # find size. 
    # Set variables.
    #times = toa_data.variables['time'][:]
    lats = toa_data.variables['latitude'][:]
    lons = toa_data.variables['longitude'][:]
    
    # Incoming top of atmosphere radiation. 
    solar_down = toa_data.variables['swtdn'][:, :, :]
    # Long wave top of atmosphere all sky outgoing radiation. 
    lw_up = toa_data.variables['lwtup'][:, :, :]
    # Net long & short wave top of atmosphere all sky incoming radiation. 
    net_sw_down = toa_data.variables['swtnt'][:, :, :]
    
    #timesSize = times.size
    latsSize = lats.size
    lonsSize = lons.size
    
#    print ('times: %i\t lats: %i\t lons: %i\t solar: %i' % \
#        (timesSize, latsSize, lonsSize, solar_down.size))
        
    # Calculate the data for the month.
    # Set time = 0 for all datasets. 
    time = 0
    solar_down_avg_lats_month = [average([solar_down[time, i, j] for j in range(0, lonsSize)]) \
        for i in range(0, latsSize)]
    lw_up_avg_lats_month = [average([lw_up[time, i, j] for j in range(0, lonsSize)]) \
        for i in range(0, latsSize)]
    net_sw_down_avg_lats_month = [average([net_sw_down[time, i, j] for j in range(0, lonsSize)]) \
        for i in range(0, latsSize)]

    return ( [solar_down_avg_lats_month, lw_up_avg_lats_month, net_sw_down_avg_lats_month] )
    
#def main(): 
if __name__ == "__main__":    

    ######################
    # Calculate monthly flux averages. 
    # # # # # # # # # # #

    # # # # # # # # # # #
    # January.
    # Import netcdf dataset.
    toa_data = Dataset('../datasets/MERRA301.prod.assim.tavg1_2d_rad_Nx.20010101.SUB.nc')
    lats = toa_data.variables['latitude'][:]
    lons = toa_data.variables['longitude'][:]
    latsSize = lats.size
    lonsSize = lons.size
    print ('lats: %i\t lons: %i\n' % (latsSize, lonsSize))

    solar_down_avg_lats_all = np.zeros(shape=(12, latsSize))
    lw_up_avg_lats_all = np.zeros(shape=(12, latsSize))
    net_sw_down_avg_lats_all = np.zeros(shape=(12, latsSize))

    # Use subroutine to generate monthy average fluxes. 
    return_dataset = process_dataset(toa_data)

    solar_down_avg_lats_jan = return_dataset[0] 
    lw_up_avg_lats_jan = return_dataset[1]
    net_sw_down_avg_lats_jan = return_dataset[2]

    solar_down_avg_lats_all[0, :] = return_dataset[0] 
    lw_up_avg_lats_all[0, :] = return_dataset[1]
    net_sw_down_avg_lats_all[0, :] = return_dataset[2]
    
    ######################
   
    ######################
   # Calculate monthly group flux averages. 

    # # # # # # # # # # #
    # Calculate the January, February, & December average data.
    solar_down_avg_lats_jan_feb_dec = [ average(  [solar_down_avg_lats_all[time, i] \
        for time in [0, 1, 11]] ) for i in range(0, latsSize) ] 
    lw_up_avg_lats_jan_feb_dec = [ average(  [lw_up_avg_lats_all[time, i] \
        for time in [0, 1, 11]] ) for i in range(0, latsSize) ] 
    net_sw_down_avg_lats_jan_feb_dec = [ average( [net_sw_down_avg_lats_all[time, i] \
        for time in [0, 1, 11]] ) for i in range(0, latsSize) ] 
    # # # # # # # # # # # #
    
    # # # # # # # # # # # #
    # Calculate the June, July, & August average data.
    solar_down_avg_lats_jun_jul_aug = [ average( [solar_down_avg_lats_all[time, i] \
        for time in [5, 6, 7]] ) for i in range(0, latsSize) ] 
    lw_up_avg_lats_jun_jul_aug = [ average( [lw_up_avg_lats_all[time, i] \
        for time in [5, 6, 7]] ) for i in range(0, latsSize) ] 
    net_sw_down_avg_lats_jun_jul_aug = [ average( [net_sw_down_avg_lats_all[time, i] \
        for time in [5, 6, 7]] ) for i in range(0, latsSize) ] 
    # # # # # # # # # # # #
    
    # Calculate all the months' data.
    # Average for all the months in a year. 
    solar_down_avg_lats = [ average( [solar_down_avg_lats_all[time, i] \
        for time in range(0, 11)] ) for i in range(0, latsSize) ]
    lw_up_avg_lats = [ average( [lw_up_avg_lats_all[time, i] \
        for time in range(0, 11)] ) for i in range(0, latsSize) ]
    net_sw_down_avg_lats = [ average( [net_sw_down_avg_lats_all[time, i] \
        for time in range(0, 11)] ) for i in range(0, latsSize) ] 
    # # # # # # # # # # # #
    
    #######################
    # Create plot of incoming short-wave radiation: January, July, & all months.
    plot(lats, solar_down_avg_lats_jan, '-b', label='January')
    plot(lats, solar_down_avg_lats_jul, '-g', label='July')
    plot(lats, solar_down_avg_lats, '-r', label='All Months')
    
    legend(loc='lower center')
    
    axis([-90, 90, -2, 1.2*amax(solar_down_avg_lats_jan) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA Solar Incoming Short Wave Flux\nJanuary, July, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_solar_incoming_avg_lats-jan_jul_2014.png")
    show()
    
    # # # # # # # # # # # #
    # Create plot of incoming short-wave radiation: winter, summer, & all months.
    plot(lats, solar_down_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
    plot(lats, solar_down_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
    plot(lats, solar_down_avg_lats, '-r', label='All Months')
    
    legend(loc='lower center')
    
    axis([-90, 90, -2, 1.2*amax(solar_down_avg_lats_jan_feb_dec) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA Solar Incoming Short Wave Flux\nWinter, Summer, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_solar_incoming_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
    show()
    
    #######################
    # Create plot of toa outgoing lw radiation: January, July, & all months.
    plot(lats, lw_up_avg_lats_jan, '-b', label='January')
    plot(lats, lw_up_avg_lats_jul, '-g', label='July')
    plot(lats, lw_up_avg_lats, '-r', label='All Months')
    
    legend(loc='lower right')
    
    axis([-90, 90, -2, 1.2*amax(lw_up_avg_lats_jan) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Long Wave Outgoing Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_lw_up_avg_lats-jan_jul_2014.png")
    show()
    
    # # # # # # # # # # # #
    # Create plot of toa outgoing lw radiation: winter, summer, & all months.
    plot(lats, lw_up_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
    plot(lats, lw_up_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
    plot(lats, lw_up_avg_lats, '-r', label='All Months')
    
    legend(loc='lower right')
    
    axis([-90, 90, -2, 1.2*amax(lw_up_avg_lats_jan_feb_dec) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Long Wave Outgoing Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_lw_up_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
    show()
    
    #######################
    # Create plot of toa net incoming sw radiation: January, July, & all months.
    plot(lats, net_sw_down_avg_lats_jan, '-b', label='January')
    plot(lats, net_sw_down_avg_lats_jul, '-g', label='July')
    plot(lats, net_sw_down_avg_lats, '-r', label='All Months')
    
    legend(loc='lower center')
    
    axis([-90, 90, -2, 1.2*amax(net_sw_down_avg_lats_jan) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Solar Short Wave Net Incoming Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_net_sw_down_avg_lats-jan_jul_2014.png")
    show()
    
    # # # # # # # # # # # #
    # Create plot of toa net incoming sw radiation: winter, summer, & all months.
    plot(lats, net_sw_down_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
    plot(lats, net_sw_down_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
    plot(lats, net_sw_down_avg_lats, '-r', label='All Months')
    
    legend(loc='lower center')

    axis([-90, 90, -2, 1.2*amax(net_sw_down_avg_lats_jan_feb_dec) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Short Wave Net Incoming Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_net_sw_down_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
    show()

    #######################
    # Calculate the outgoing sw flux: the difference between the incoming and net incoming sw radiation. 
    sw_up_avg_lats_jan = [y-x for x, y in zip(net_sw_down_avg_lats_jan, solar_down_avg_lats_jan)]
    sw_up_avg_lats_jul = [y-x for x, y in zip(net_sw_down_avg_lats_jul, solar_down_avg_lats_jul)]
    sw_up_avg_lats = [y-x for x, y in zip(net_sw_down_avg_lats, solar_down_avg_lats)]
    # # # # # # # # # # # #
    
    # Create plot of outgoing sw flux.
    plot(lats, sw_up_avg_lats_jan, '-b', label='January')
    plot(lats, sw_up_avg_lats_jul, '-g', label='July')
    plot(lats, sw_up_avg_lats, '-r', label='All Months')
    
    legend(loc='upper right')
    
    axis([-90, 90, -2, 1.2*amax(sw_up_avg_lats_jan) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Outgoing Short Wave Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_sw_up_avg_lats-jan_jul_2014.png")
    show()
    
    # # # # # # # # # # # #
    # Calculate the outgoing sw flux: the difference between the incoming and outgoing sw radiation. 
    sw_up_avg_lats_jan_feb_dec = [y-x for x, y in zip(net_sw_down_avg_lats_jan_feb_dec, solar_down_avg_lats_jan_feb_dec)]
    sw_up_avg_lats_jun_jul_aug = [y-x for x, y in zip(net_sw_down_avg_lats_jul, solar_down_avg_lats_jun_jul_aug)]
    sw_up_avg_lats = [y-x for x, y in zip(net_sw_down_avg_lats, solar_down_avg_lats)]
    # # # # # # # # # # # #
    
    # Create plot of outgoing sw flux.
    plot(lats, sw_up_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
    plot(lats, sw_up_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
    plot(lats, sw_up_avg_lats, '-r', label='All Months')
    
    legend(loc='upper right')
    
    axis([-90, 90, -2, 1.2*amax(sw_up_avg_lats_jan_feb_dec) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Outgoing Short Wave Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_sw_up_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
    show()

    #######################
    # Calculate the albedo: the ratio of the outgoing to incoming sw radiation. 
    
    # Check if the solar incoming flux is null; if so, set value to "None," 
    albedo_avg_lats_jan = [None if y == 0 else x/y for x, y in zip(sw_up_avg_lats_jan, solar_down_avg_lats_jan)]
    # Ignore opposite hemisphere albedo above 60 deg. latitude. 
    for i, x in enumerate(lats):
        if x > 60:
            albedo_avg_lats_jan[i] = None
    
    albedo_avg_lats_jul = [None if y == 0 else x/y for x, y in zip(sw_up_avg_lats_jul, solar_down_avg_lats_jul)]
    for i, x in enumerate(lats):
        if x < -60:
            albedo_avg_lats_jul[i] = None
    
    albedo_avg_lats = [None if y == 0 else x/y for x, y in zip(sw_up_avg_lats, solar_down_avg_lats)]
    
    # Create plot of albedo. 
    plot(lats, albedo_avg_lats_jan, '-b', label='January')
    plot(lats, albedo_avg_lats_jul, '-g', label='July')
    plot(lats, albedo_avg_lats, '-r', label='All Months')
    
    legend(loc='upper right')
    
    axis([-90, 90, 0, 1])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Albedo')
    title('MERRA Top of Atmosphere Albedo\n January, July, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_albedo_avg_lats-jan_jul_2014.png")
    show()
    
    # # # # # # # # # # # #
    # Check if the solar incoming flux is null; if so, set value to "None," 
    albedo_avg_lats_jan_feb_dec = [None if y == 0 else x/y for x, y in zip(sw_up_avg_lats_jan_feb_dec, solar_down_avg_lats_jan_feb_dec)]
    # Ignore opposite hemisphere albedo above 60 deg. latitude. 
    for i, x in enumerate(lats):
        if x > 60:
            albedo_avg_lats_jan_feb_dec[i] = None
    
    albedo_avg_lats_jun_jul_aug = [None if y == 0 else x/y for x, y in zip(sw_up_avg_lats_jun_jul_aug, solar_down_avg_lats_jun_jul_aug)]
    for i, x in enumerate(lats):
        if x < -60:
            albedo_avg_lats_jun_jul_aug[i] = None
    
    albedo_avg_lats = [None if y == 0 else x/y for x, y in zip(sw_up_avg_lats, solar_down_avg_lats)]
    
    # Create plot of albedo. 
    plot(lats, albedo_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
    plot(lats, albedo_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
    plot(lats, albedo_avg_lats, '-r', label='All Months')
    
    legend(loc='upper right')
    
    axis([-90, 90, 0, 1])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Albedo')
    title('MERRA Top of Atmosphere Albedo\n Winter, Summer, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_albedo_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
    show()
    
    #######################
    # Calculate the net incoming sw & lw flux: the difference between the net incoming 
    #  sw flux to the outgoing lw flux. 
    net_all_down_avg_lats_jan = [x-y for x, y in zip(net_sw_down_avg_lats_jan, lw_up_avg_lats_jan)]
    net_all_down_avg_lats_jul = [x-y for x, y in zip(net_sw_down_avg_lats_jul, lw_up_avg_lats_jul)]
    net_all_down_avg_lats = [x-y for x, y in zip(net_sw_down_avg_lats, lw_up_avg_lats)]
    # # # # # # # # # # # #
    
    # Create plot of toa net incoming sw & lw radiation: January, July, & all months.
    plot(lats, net_all_down_avg_lats_jan, '-b', label='January')
    plot(lats, net_all_down_avg_lats_jul, '-g', label='July')
    plot(lats, net_all_down_avg_lats, '-r', label='All Months')
    
    legend(loc='lower center')
    
    axis([-90, 90, 1.2*amin(net_all_down_avg_lats_jan), 1.2*amax(net_all_down_avg_lats_jan) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Net Incoming Short & Long Wave Flux, All Sky\n January, July, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_incoming_net_all_avg_lats-jan_jul_2014.png")
    show()
    
    # # # # # # # # # # # #
    net_all_down_avg_lats_jan_feb_dec = [x-y for x, y in zip(net_sw_down_avg_lats_jan_feb_dec, lw_up_avg_lats_jan_feb_dec)]
    net_all_down_avg_lats_jun_jul_aug = [x-y for x, y in zip(net_sw_down_avg_lats_jun_jul_aug, lw_up_avg_lats_jun_jul_aug)]
    net_all_down_avg_lats = [x-y for x, y in zip(net_sw_down_avg_lats, lw_up_avg_lats)]
    # # # # # # # # # # # #
    # Create plot of toa net incoming sw & lw radiation: winter, summer, & all months.
    plot(lats, net_all_down_avg_lats_jan_feb_dec, '-b', label='Jan-Feb-Dec')
    plot(lats, net_all_down_avg_lats_jun_jul_aug, '-g', label='Jun-Jul-Aug')
    plot(lats, net_all_down_avg_lats, '-r', label='All Months')
    
    legend(loc='lower center')

    axis([-90, 90, 1.2*amin(net_all_down_avg_lats_jan_feb_dec), 1.2*amax(net_all_down_avg_lats_jan_feb_dec) ])
    plt.xticks(range(-90, 91, 30))
    xlabel('Latitude')
    ylabel('Radiative Flux $(W/m^2)$')
    title('MERRA TOA Net Incoming Short & Long Wave Flux, All Sky\n Winter, Summer, and all Months in 2014', fontsize=18)
    grid(True)
    savefig("../images/MERRA_TOA_incoming_net_all_avg_lats-jan-feb-dec_jun-jul-aug_2014.png")
    show()
    #######################
    

#main() 
