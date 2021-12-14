from fanpy import prep_climate_cflux, plot_climate_cflux

home_dir = '/p/project/hai_hhhack/anand1/'

i = 0

project_data_path = home_dir + 'Project_Data/forest-carbon-flux/'

climate_file = home_dir+f'Projects/FANPY/Projects/Project_Beech/formind_parameters/Climate/weather_sim_10000_{i}.txt'
cflux_file = home_dir + f'Projects/FANPY/Projects/Project_Beech/results_16ha_{i}/beech_16ha.cflux'

plot_path = project_data_path+f'graphics/sim_10000_{i}_16ha.png'

cflux_data, data_climate, time = prep_climate_cflux(cflux_file, climate_file, 1)

plot_climate_cflux(cflux_data, data_climate, time, plot_path)