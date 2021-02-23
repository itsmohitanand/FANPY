from forpy import download_era5_met

var_met = ['rainfall_flux',  
            'near_surface_air_temperature', 
            'near_surface_wind_speed', 
            'surface_air_pressure', 
            'surface_downwelling_shortwave_radiation']


var_pressure = 'relative_humidity'
download_dir = '/data/compoundx/era5_met/'


for year in range(1979,2019):
    for var in var_met:
        download_era5_met(var, year, download_dir)


#download_era5_pressure(var_pressure, year)