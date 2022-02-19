from fanpy import prep_climate_cflux, plot_climate_cflux

home_dir = '/p/project/hai_deep_c/'

project_data_path = home_dir + 'project_data/forest-carbon-flux/'


climate_file = project_data_path+f'formind_sim/sim_100ha_19/formind_parameters/Climate/weather_sim_10000_19.txt'
cflux_file = project_data_path +f'formind_sim/sim_100ha_19/results/beech_spinoff.cflux'

plot_path = project_data_path+f'graphics/sim_100ha_spinoff.png'

cflux_data, data_climate, time = prep_climate_cflux(cflux_file, climate_file, 1)

plot_climate_cflux(cflux_data, data_climate, time, plot_path)