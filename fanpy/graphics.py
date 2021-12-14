#
# Created on Mon Nov 23 2020
#
# Copyright (c) 2020 Mohit Anand
#
# For any details contact itsmohitanand@gmail.com 
#


## The goal of this script is to create plots from the output of forest model with mininum dependencies. 


import pandas as pd
import matplotlib.pylab as plt
import numpy as np


from typing import Tuple

def plot_climate_cflux(cflux_data: Tuple, climate_data: np.array, time: np.array, plot_path:str=".")-> None:
    """The function plots the carbon flux with climatological data
    Args:
    	cflux_path (str): The path to cflux ouput file.
		climate_path (str): The path to climate data input file.
        plot_path (str): The path to the ouput graph.
		
	Returns:
		None: And plots in the specified folder
	"""

    av_rain = climate_data[0,:]
    av_temp = climate_data[1,:]
    av_irradiance = climate_data[2,:]
    #fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5,1, figsize=(12,8))
    
    nee_arr, gpp_arr, biomass_arr, deadwood_arr = cflux_data
  

    strt = 0
    end  = climate_data.shape[1]
    end = 1500

    av_rain = climate_data[0,strt:end]
    av_temp = climate_data[1,strt:end]
    av_irradiance = climate_data[2,strt:end]
    time = time[strt:end]
    # Multiplying by 100 for unit conversion 
    nee_arr = nee_arr[strt:end]*100
    gpp_arr = gpp_arr[strt:end]*100
    biomass_arr = biomass_arr[strt:end]*100
    deadwood_arr = deadwood_arr[strt:end]*100
    if strt>0 or end<climate_data.shape[1]:
        plot_path = plot_path.split('.')[0]+'_short.'+plot_path.split('.')[1]

    fig, (ax1, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(7,1, figsize=(16,14))

    ax1.plot(time, av_irradiance, color = "darkorange")
    ax1.set_xlim(left = time[0], right = time[-1])
    ax1.set_ylabel("Solar Irradiance [$micro mol$ $s^{-1}$ $m^{-2}$]")
    
    # ax2.plot(time, av_pet)
    ax3.plot(time, av_temp, color = "indianred")
    ax3.set_xlim(left = time[0], right = time[-1])
    ax3.set_ylabel(u'Temperature $[\u00B0C]$')
    

    ax4.bar(time, av_rain, color = "mediumblue")
    ax4.set_xlim(left = time[0], right = time[-1])
    ax4.set_ylabel("Precipitation [$mm$ $d^{-1}$]")

    # Cflux plots

    ax5.plot(time, nee_arr, color = "lightblue")
    ax5.plot(time, np.mean(nee_arr, axis =1), color = "k")

    
    #nee_positive = np.where(nee_extend<0, 0, nee_extend)
    #nee_negative = np.where(nee_extend>0, 0, nee_extend)
    # ax5.fill_between(time, nee_positive, color = "slateblue")
    # ax5.fill_between(time, nee_negative, color = "lightcoral")
    ax5.axhline(color = "k", linestyle = "--")
    # ax5.set_ylabel("NEE [$t_C$ $ha^{-1}$ $a^{-1}$]")
    ax5.set_ylabel("NEE [$g_C$ $m^{-2}$ $a^{-1}$]")

    ax5.set_xlabel("Time [Years]")
    ax5.set_xlim(left = time[0], right = time[-1])
    
    # We are doing a custom hline here
    
    y = np.mean(np.mean(gpp_arr, axis=1))
    ax6.plot(time, gpp_arr, color = "lightblue")
    ax6.plot(time, np.mean(gpp_arr, axis =1), color = "k")
    ax6.axhline(y=y,color = "k", linestyle = "--")
    # ax6.set_ylabel("GPP [$t_C$ $ha^{-1}$ $a^{-1}$]")
    ax6.set_ylabel("GPP [$g_C$ $m^{-2}$ $a^{-1}$]")

    ax6.set_xlabel("Time [Years]")
    ax6.set_xlim(left = time[0], right = time[-1])
    
    y = np.mean(np.mean(biomass_arr, axis=1))
    ax7.plot(time, biomass_arr, color = "lightblue")
    ax7.plot(time, np.mean(biomass_arr, axis =1), color = "k")
    ax7.axhline(y=y,color = "k", linestyle = "--")
    # ax7.set_ylabel("Cpool_Biomass [$t_C$ $ha^{-1}$]")
    ax7.set_ylabel("Cpool_Biomass [$g_C$ $m^{-2}$]")
    
    ax7.set_xlabel("Time [Years]")
    ax7.set_xlim(left = time[0], right = time[-1])
    
    y = np.mean(np.mean(deadwood_arr, axis=1))
    ax8.plot(time, deadwood_arr, color = "lightblue")
    ax8.plot(time, np.mean(deadwood_arr, axis =1), color = "k")
    ax8.axhline(y=y,color = "k", linestyle = "--")
    # ax8.set_ylabel("Cpool_Deadwood [$t_C$ $ha^{-1}$]")
    ax8.set_ylabel("Cpool_Deadwood [$g_C$ $m^{-2}$]")
    ax8.set_xlabel("Time [Years]")
    ax8.set_xlim(left = time[0], right = time[-1])

    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    
    ### Another figure
    # fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8,8))

    # av_gpp = np.mean(gpp_arr, axis =1)
    
    # ax1.scatter(av_gpp, av_temp, color = "rebeccapurple")
    # ax1.set_ylabel("av_temp [..]")
    # ax1.set_xlabel("gpp [..]")

    # ax2.scatter(av_gpp, av_rain, color = "rebeccapurple")
    # ax2.set_ylabel("av_rainp [..]")
    # ax2.set_xlabel("gpp [..]")
    
    # plt.savefig('plots/scatter.png')

    return 


def prep_climate_cflux(cflux_path: str, climate_path: str, num_sim:int = 10) -> Tuple :
    """  The function prepares climate and cflux data for plotting
    Args:
    	cflux_path (str): The path to cflux ouput file.
		climate_path (str): The path to climate data input file.
    	num_sim (int): Number of cflux simulatiions
        
	Returns:
		Tuple: Tuple of np.array containing climate and cflux data
	"""

    ## We need to fix this line
    cflux_file = cflux_path.split('.')[0]+'_'+"00"+"."+cflux_path.split(".")[1]
    
    cflux = pd.read_csv(cflux_file, delimiter="\t", skiprows=2)    
    time = cflux["Time"].values
    nee = cflux["NEE"].values
    gpp = cflux["GPP"].values
    cpool_biomass =  cflux['CPool_Biomass'].values
    cpool_deadwood = cflux['CPool_DeadWood'].values

    nee_arr = np.zeros((num_sim,nee.shape[0]))
    gpp_arr = np.zeros((num_sim,gpp.shape[0]))
    biomass_arr = np.zeros((num_sim,cpool_biomass.shape[0]))
    deadwood_arr = np.zeros((num_sim,cpool_deadwood.shape[0]))


    nee_arr[0,:] = nee
    gpp_arr[0,:] = gpp
    biomass_arr[0,:] = cpool_biomass
    deadwood_arr[0,:] = cpool_deadwood


    for i in range(1,num_sim):
        cflux_file = cflux_path.split('.')[0]+'_'+str(i).zfill(2)+"."+cflux_path.split(".")[1]
        cflux = pd.read_csv(cflux_file, delimiter="\t", skiprows=2)    
        nee_arr[i,:] = cflux["NEE"].values    
        gpp_arr[i,:] = cflux["GPP"].values
        biomass_arr[i,:] =  cflux['CPool_Biomass'].values
        deadwood_arr[i,:] = cflux['CPool_DeadWood'].values
    
        
    # Read the climate file

    time_climate = np.arange(-1,time.shape[0])
    nee_extend = np.zeros((nee_arr.shape[0], time_climate.shape[0]))
    gpp_extend = np.zeros((gpp_arr.shape[0], time_climate.shape[0]))
    biomass_extend = np.zeros((biomass_arr.shape[0], time_climate.shape[0]))
    deadwood_extend = np.zeros((deadwood_arr.shape[0], time_climate.shape[0]))
    
    nee_extend[:,1:] = nee_arr
    gpp_extend[:,1:] = gpp_arr
    biomass_extend[:,1:] = biomass_arr
    deadwood_extend[:,1:] = deadwood_arr


    data_climate = read_av_climate(climate_path)
    
    cflux_data = (nee_extend.T, gpp_extend.T, biomass_extend.T, deadwood_extend.T)
    return  cflux_data, data_climate[:,:time_climate.shape[0]], time_climate

def read_climate(climate_path: str)->pd.DataFrame:
    """  The climate data is read from the txt file
	Args:
		climate_path (str): The path to the climate text file.

	Returns:
		pd.DataFrame: pandas dataframe of climate data

	""" 

    climate = pd.read_csv(climate_path, delimiter=" ", skiprows=1, header=None)
    climate.columns = ["rain[mm]","temperature[C]","irradiance[mumol/s/m2]","day_length[h]","PET[mm]", "CO2[ppm]"]    
    
    return climate

def read_av_climate(climate_path: str) -> np.array:
    """  The function averages the climatological variables from daily to yearly values.
	
    Args:
		climate_path (str): The path to the climate text file

	Returns:
		np.array: Containing av_rain, av_temp, av_irradiance, av_day_length,   and av_PET 
	Raises:
		AttributeError: The ``Raises`` section is a list of all exceptions
			that are relevant to the interface.
	ValueError: If `param2` is equal to `param1`.
	""" 

    climate = read_climate(climate_path)
    
    rain = climate["rain[mm]"].values
    temp = climate["temperature[C]"].values
    irradiance = climate["irradiance[mumol/s/m2]"].values
    daylength = climate["day_length[h]"].values
    pet = climate["PET[mm]"].values

    av_rain = _average_annualy(rain)
    av_temp = _average_annualy(temp)
    av_irradiance = _average_annualy(irradiance)
    av_daylength = _average_annualy(daylength)
    av_pet = _average_annualy(pet)

    return np.array([av_rain, av_temp, av_irradiance, av_daylength, av_pet])
    
def _average_annualy(data:np.array)->np.array:
    
    """ Annual average values is calculated from daily values.
        The year is of 365 days
	Args:
		data (np.array): 1-d np.array of values
	Returns:
		np.array: The annual average of the daily data

	""" 
    num_years = data.shape[0]//365
    data_avg = np.zeros((num_years))
    for i in range(num_years):
        data_avg[i] = np.mean(data[365*i:365*(i+1)]) 

    return data_avg

