import h5py
import numpy as np
import pandas as pd 
import matplotlib.pylab as plt

home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'
model_path = home_dir	
par_file_name='beech'

ml_data_path = home_dir + 'ml_data/'

met = np.zeros((365, 20, 3))
gpp = np.zeros(20)

for i in range(20):
    path = ml_data_path + f'data_100ha_{i}.h5'
    with h5py.File(path, 'r') as f:
        print(f['X']['irradiance'].shape)
        met[:, i, 0] =  np.mean(f['X']['irradiance'], axis = 0)
        met[:, i, 1] = np.mean(f['X']['rain'], axis = 0)
        met[:, i, 2] = np.mean(f['X']['temperature'], axis = 0)
        
        gpp[i] = np.mean(f['Y']['GPP'])


met = np.mean(met, axis=1)
print(met)
print(np.mean(gpp))

# plt.plot(met[:,1:])
# plt.savefig('scratch.png')


clim_data = pd.read_csv(home_dir+'formind_sim/sim_100ha_mean/formind_parameters/Climate/weather_sim_1000.txt', delimiter=' ')

year_data = clim_data.iloc[:365, : ]

year_data.iloc[:, 0] = met[:, 1]
year_data.iloc[:, 1] = met[:, 2]
year_data.iloc[:, 2] = met[:, 0]

print(year_data)

mean_data = pd.concat([year_data]*2000)

mean_data.to_csv(home_dir+'formind_sim/sim_100ha_mean/formind_parameters/Climate/weather_sim_2000_mean.txt', sep = ' ', index= False, float_format='%.3f')

# formind_file = pd.read_csv('Projects/Project_Beech/formind_parameters/Climate/weatherGermany_100_ori.txt', delimiter=' ')

# num_days = 39*365
# new_formind_arr = np.zeros((num_days, 6))

# new_formind_arr[:, 0] = clim_data.Rainf.values[:num_days]*3600*24 
# new_formind_arr[:, 1] = clim_data.Tair.values[:num_days] - 273.15 
# new_formind_arr[:, 2] = clim_data.SWdown.values[:num_days]*4.91

# new_formind_arr[:, 3] = formind_file.iloc[:num_days, 3]
# new_formind_arr[:, 4] = formind_file.iloc[:num_days, 4]
# new_formind_arr[:, 5] = formind_file.iloc[:num_days, 5]

# new_fa = np.tile(new_formind_arr, (30,1))

# formind_df = pd.DataFrame(new_fa)

# formind_df.columns = formind_file.columns


# print(formind_file.describe())
# print(formind_df.describe())
# formind_df.to_csv('Projects/Project_Beech/formind_parameters/Climate/weatherGermany_era5_adjusted.txt', sep = ' ', index= False, float_format='%.3f')