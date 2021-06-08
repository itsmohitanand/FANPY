# ##########################################################
# Created on Wed Dec 09 2020
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

import cdsapi
import os

def download_era5_land(var:str, year:int)->None:
    """The function downloads one year of howrly era5 data

    Args:
        var (str): The variable to be downloaded.
            The available options are: 
                'total_precipitation'
                '2m_temperature'
                '10m_u_component_of_wind'
                '10m_v_component_of_wind'
                'surface_solar_radiation_downwards'
                'surface_pressure'
        year (int): The year for which data needs to be downloaded
    """

    _create_var_folder(download_dir+var)

    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-land',
        {
            'format': 'netcdf',
            'year': str(year),
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
            'area': [
                -17.58, 49.22, -17.59,
                49.23,
            ],
            'variable': var,
        },
        download_dir+var+'/'+var+'_'+str(year)+'.nc')

def download_era5_met(var:str, year:int, download_dir:str)-> None:
    """[summary]

    Args:
        var (str): The variable to be downloaded and can be one of :
            'rainfall_flux'
            'near_surface_air_temperature', 
            'near_surface_wind_speed', 
            'rainfall_flux',
            'surface_air_pressure', 
            'surface_downwelling_shortwave_radiation',
        year (int): The year for which the data needs to be downloaded and can range
            from 1979-2018
    """
    _create_var_folder(download_dir+var)

    c = cdsapi.Client()

    c.retrieve(
        'derived-near-surface-meteorological-variables',
        {
            'variable': var,
            'reference_dataset': 'cru',
            'year': str(year),
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'format': 'zip',
        },
        download_dir+var+'/'+var+'_'+str(year)+'.zip')

def download_era5_pressure(var:str, year:int, download_dir:str)-> None:
    """[summary]

    Args:
        var (str): Can be multiple variables from ERA5 pressure level data :
            'relative_humidity'
        year (int): The year for which the data needs to be downloaded,
            can range from 1979-present
    """
    _create_var_folder(download_dir+var)

    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': var,
            'pressure_level': '1000',
            'year': str(year),
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
            'area': [
                -17.58, 49.22, -17.59,
                49.23,
            ],
        },
        download_dir+var+'/'+var+'_'+str(year)+'.nc')

def download_era5_single(var:str, year:int, download_dir: str) -> None:
    """The function downloads era5 single level dataset

    Args:
        var (str): The variable for which data needs to be downloaded like
            'total_cloud_cover'
        year (int): The year for which data needs to be downloaded and 
            can range from 1979-present
    """

    c = cdsapi.Client()

    c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': var,
        'year': str(year),
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            51.10, 10.40, 51.11,
            10.41,
        ],
    },
    download_dir+var+'/'+var+'_'+str(year)+'.nc')

def _create_var_folder(directory:str):
    """The function creates a folder wth var name in data folder

    Args:
        var (str): The name of the folder
    """
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        pass

