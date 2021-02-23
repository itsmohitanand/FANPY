# ##########################################################
# Created on Thu Dec 10 2020
# 
# __author__ = Mohit Anand
# __copyright__ = Copyright (c) 2020, Author's Project
# __credits__ = [Mohit Anand,]
# __license__ = GPL
# __version__ = 0.0.0
# __maintainer__ = Mohit Anand
# __email__ = itsmohitanand@gmail.com
# __status__ = Development
# ##########################################################


from zipfile import ZipFile
import netCDF4 as nc
import numpy as np

def read_era5_met(var:str, year:int):
    """The function reads the variables from era5 meterological data

    Args:
        var (str): The variable to be read
        year (int): The year of the data
    """

    # Its a zip file so we first need to Unzip it

    file_name = 'data/'+var+'/'+var+'_'+str(year)+'.zip'
    
    with ZipFile(file_name, 'r') as f_zip:
        f_zip.extractall('data/'+var+'/'+var+'_'+str(year))

    f_name = 'data/rainfall_flux/rainfall_flux_1979/Rainf_WFDE5_CRU_197901_v1.0.nc'
    
    ds = nc.Dataset(f_name)
    print(ds.variables)
    print(ds['lat'][:])
    print(ds['lon'][:])

def extract_data_for_location(lat:float, lon:float)<-np.array:



# var = 'rainfall_flux'
# read_era5_met(var,1979)