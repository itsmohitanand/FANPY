from fanpy import prep_climate_cflux, plot_climate_cflux

project_path='/home/anand/Projects/FANPY/Projects/Project_Beech/'

climate_file = 'weatherGermany_era5.txt'

cflux_file = 'beech_general.cflux'
cflux_path = project_path+'results/'+cflux_file

climate_path = project_path+'formind_parameters/Climate/'+climate_file

plot_path = project_path+'graphics/sim_1_ha_1_beech_era5.png'

cflux_data, data_climate, time = prep_climate_cflux(cflux_path, climate_path, 1)

plot_climate_cflux(cflux_data, data_climate, time, plot_path)