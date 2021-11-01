from fanpy import read_climate
import matplotlib.pylab as plt
import numpy as np

home_dir = '/p/project/hai_hhhack/anand1/'

project_data_path = home_dir + 'Project_Data/forest-carbon-flux/'

plot_path = project_data_path+f'graphics/precip_perc.png'

fig, axes = plt.subplots(5,4, figsize = (20,16))

for i in range(5):
    for j in range(4):
        k = 4*i+j
        climate_file = project_data_path+f'climate_data/weather_sim_10000_{k}.txt'
        climate_data = read_climate(climate_file)

        var = climate_data.values[365*1000:365*10000, 0]
        var = var.reshape((9000,365)).T
        
        for perc in range(1,10):
            var_per =np.percentile(var, perc*10, axis = 1) 

       
            axes[i][j].plot(var_per)
        axes[i][j].set_xlabel(f'precip_percentile  | Year {k}')
            #axes[i][j].set_xlim(left = 300, right = 1600)

plt.savefig(plot_path)