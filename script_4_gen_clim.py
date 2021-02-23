import pandas as pd
import numpy as np
import matplotlib.pylab as plt

clim_data = pd.read_csv('daily_clim_data.csv')
formind_file = pd.read_csv('Projects/Project_Beech/formind_parameters/Climate/weatherGermany_100_ori.txt', delimiter=' ')

num_days = clim_data.shape[0]
new_formind_arr = np.zeros((num_days, 6))

new_formind_arr[:, 0] = clim_data.Rainf.values*3600*24 
new_formind_arr[:, 1] = clim_data.Tair.values - 273.15
new_formind_arr[:, 2] = clim_data.SWdown.values*4.91
new_formind_arr[:, 3] = formind_file.iloc[:num_days, 3]
new_formind_arr[:, 4] = formind_file.iloc[:num_days, 4]
new_formind_arr[:, 5] = formind_file.iloc[:num_days, 5]

new_fa = np.tile(new_formind_arr, (30,1))

formind_df = pd.DataFrame(new_fa)

formind_df.columns = formind_file.columns

formind_df.to_csv('Projects/Project_Beech/formind_parameters/Climate/weatherGermany_100.txt', sep = ' ', index= False)