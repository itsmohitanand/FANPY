from fanpy import prep_climate_cflux
import matplotlib.pylab as plt

home_dir = '/p/project/hai_hhhack/anand1/'

project_data_path = home_dir + 'Project_Data/forest-carbon-flux/'

plot_path = project_data_path+f'graphics/gpp_hist.png'


fig, axes = plt.subplots(5,4, figsize = (20,16))

for i in range(5):
    for j in range(4):
        k = 4*i+j
        climate_file = project_data_path+f'climate_data/weather_sim_10000_{k}.txt'
        cflux_file = project_data_path + f'formind_sim/results_{k}/beech_general.cflux'
        cflux_data, data_climate, time = prep_climate_cflux(cflux_file, climate_file, 1)
        gpp = cflux_data[1]

        axes[i][j].hist(gpp[1000:]*100, bins = 200)
        axes[i][j].set_xlabel(f'GPP [g/m2/yr] | Year {k}')
        axes[i][j].set_xlim(left = 300, right = 1600)

plt.savefig(plot_path)