from fanpy import prep_climate_cflux, plot_climate_cflux

home_dir = '/p/project/hai_deep_c/'

project_data_path = home_dir + 'project_data/forest-carbon-flux/'

for i in range(2,20):

    climate_file = project_data_path+f'formind_sim/sim_100ha_42_{i}/formind_parameters/Climate/weather_sim_10000_{i}.txt'
    cflux_file = project_data_path +f'formind_sim/sim_100ha_42_{i}/results/beech_100ha.cflux'

    plot_path = project_data_path+f'graphics/sim_100ha_{i}_100ha.png'

    cflux_data, data_climate, time = prep_climate_cflux(cflux_file, climate_file, 1)

    plot_climate_cflux(cflux_data, data_climate, time, plot_path)