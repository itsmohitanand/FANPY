from fanpy import prep_climate_cflux
import matplotlib.pylab as plt

home_dir = '/p/project/hai_hhhack/anand1/'

project_data_path = home_dir + 'Project_Data/forest-carbon-flux/'

plot_path = project_data_path+f'graphics/gpp_hist.png'

col = 1 # 5
row = 1 # 4

fig, axes = plt.subplots(col,row, figsize = (20,16))

for i in range(col):
    for j in range(row):
        k = 4*i+j
        climate_file = project_data_path+f'climate_data/weather_sim_10000_{k}.txt'
        cflux_file = project_data_path + f'formind_sim/results_{k}/beech_general.cflux'
        cflux_data, data_climate, time = prep_climate_cflux(cflux_file, climate_file, 1)
        gpp = cflux_data[1]
        if row == 1 and col ==1:
            axes.hist(gpp[1000:]*100, bins = 200)
            axes.set_xlabel(f'GPP [g/m2/yr] | Year {k}')
            axes.set_xlim(left = 300, right = 1600)            
        else:
            axes[i][j].hist(gpp[1000:]*100, bins = 200)
            axes[i][j].set_xlabel(f'GPP [g/m2/yr] | Year {k}')
            axes[i][j].set_xlim(left = 300, right = 1600)

plt.savefig(plot_path)