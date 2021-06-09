from fanpy import prep_climate_cflux, plot_climate_cflux

i = 9

project_path='/data/compoundx/FORMIND/Project_Beech/'

climate_file = f'weather_sim_10000_{i}.txt'

cflux_file = 'beech_general.cflux'
cflux_path = project_path+f'results_{i}/'+cflux_file

climate_path = project_path+'formind_parameters/Climate/'+climate_file

plot_path = project_path+f'graphics/sim_10000_{i}.png'

cflux_data, data_climate, time = prep_climate_cflux(cflux_path, climate_path, 1)

plot_climate_cflux(cflux_data, data_climate, time, plot_path)