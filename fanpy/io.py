import numpy as np
import pandas as pd
# from netCDF4 import Dataset

def write_climate_file(file_name: str, path: str, **kwargs) -> None:
    
    """The function writes the climate file for formind climate data

    Args:
        file_name (str): The name of the file
        path (str): path of the file
        **nparray (np.ndarray) : numpy array of rain, temp, irradiance, day_length, PET
        **pddf (pd.DataFrame) : PD.DataFrame of rain, temp, irradiance, day_length and PET, with header
    Returns:
        None: The function just writes the file and returns None
    """

    for key,val in kwargs.items():
        if key=="nparray":
            nparray = val
            df = pd.DataFrame(nparray, columns=[
                      "rain[mm]", "temperature[�C]", "irradiance[m�mol/s/m2]", "day_length[h]",	"PET[mm]", "co2[ppm]"])
            df.to_csv(path+file_name, index=False, sep= "\t")

        elif key == "pddf":
            df = val
            df.round(7).to_csv(path+file_name, index=False, sep= "\t")
        else:
            print("provide nparray or pddf as an input")
    

    return

def read_climate_file(file_name: str, path: str) :
    
    """[summary]

    Args:
        file_name (str): The name of the file
        path (str): The path to the file

    Returns:
        pd.DataFrame: The pandas dataframe for the climate file
    """    
                
    df = pd.read_csv(path+file_name, delimiter="\t")
    return df

# def read_single_level(year:int, var:str = 'total_cloud_cover'):

#     data_path = '/data/compoundx/era_5_single/'+var+'/'+var+'_'+str(year)+'.nc'
#     data = Dataset(data_path)['tcc'][:, 0, 0]

#     return data
