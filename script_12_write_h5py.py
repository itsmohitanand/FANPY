import h5py
from fanpy.io import read_climate, read_cflux_file

index = 4
area = '16ha'
strt_year = 1000

clim_path = 'Projects/Project_Beech/formind_parameters/Climate/'
clim_name = f'weather_sim_10000_{index}.txt'
clim_data = read_climate(climate_path=clim_path+clim_name)

rain = clim_data.values[365*1000:365*10000, 0].reshape(9000,365)
temperature = clim_data.values[365*1000:365*10000, 1].reshape(9000,365)
irradiance = clim_data.values[365*1000:365*10000, 2].reshape(9000,365)

cflux_path = f'Projects/Project_Beech/results_{area}_{index}/beech_{area}.cflux'

cflux_data = read_cflux_file(cflux_path)

gpp = cflux_data['GPP'].values[strt_year+1:].reshape(-1)
nee = cflux_data['NEE'].values[strt_year+1:].reshape(-1)


data_path = '/p/project/hai_deep_c/project_data/forest-carbon-flux/ml_data/'

with h5py.File(data_path+f'data_{area}_{index}.h5', 'w') as f:
    X = f.create_group('X')
    X['irradiance'] = irradiance
    X['temperature'] = temperature
    X['rain'] = rain 


    Y = f.create_group('Y')
    Y['GPP'] = gpp
    Y['NEE'] = nee