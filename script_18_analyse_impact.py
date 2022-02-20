from fanpy import Formind
import numpy as np
import os
import time
import pandas as pd
import matplotlib.pylab as plt

initial_time = time.time()

home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'

compound_1 = np.array([0,0,0,0,0,0,0])
c_1 = np.sum(compound_1)
compound_string_1 = ''.join(map(str, compound_1))
intervention_path_1 = home_dir + f'formind_sim/compound_{c_1}/{compound_string_1}/sim_100ha_spin_base/'

compound_2 = np.array([1,1,1,1,1,1,1])
c_2 = np.sum(compound_2)
compound_string_2 = ''.join(map(str, compound_2))
intervention_path_2 = home_dir + f'formind_sim/compound_{c_2}/{compound_string_2}/sim_100ha_spin_base/'


gpp_val = np.zeros((10,2))
for i in range(10):
    path_1 = intervention_path_1 + f'/results/beech_c{c_1}_{i}_00.cflux'
    data_1 = pd.read_csv(path_1, skiprows=2, delimiter= '\t')
    gpp_1 = data_1['GPP'][4] 
    
    path_2 = intervention_path_2 + f'/results/beech_c{c_2}_{i}_00.cflux'
    data_2 = pd.read_csv(path_2, skiprows=2, delimiter= '\t')
    gpp_2 = data_2['GPP'][4] 
    

    gpp_val[i, 0] = gpp_1*100
    gpp_val[i, 1] = gpp_2*100


fig, ax = plt.subplots(1,1)

x_1 = np.zeros(10)+1
x_2 = np.zeros(10)+2

ax.scatter(x_1, gpp_val[:,0], color = 'b')
ax.scatter(x_2, gpp_val[:,1], color = 'g')
plt.savefig('scratch.png')