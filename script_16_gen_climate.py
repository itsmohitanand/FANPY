from statistics import mode
from typing import Dict
import h5py 
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm
import copy
import pandas as pd
import os

from fanpy.process import Intervention

PROJECT_PATH = "/p/project/hai_deep_c/project_data/forest-carbon-flux/"

DATA_PATH = PROJECT_PATH + "ml_data/"

GRAPHICS_SAVE_FOLDER = DATA_PATH + "graphics/"

MODEL_SAVE_FOLDER = DATA_PATH + "models/"

intervention_f = DATA_PATH + "intervention_dict.npy"

clim_data_f = DATA_PATH + 'av_gpp_clim.npy'

clim_data = np.load(clim_data_f)

intervention = np.load(intervention_f, allow_pickle = True)


           


like_df = pd.read_csv(PROJECT_PATH + '/formind_sim/sim_100ha_spin/formind_parameters/Climate/weather_sim_1000.txt', delimiter=' ')

intervention_object = Intervention(climate_data=clim_data, intervention_dict=intervention.item())

clim_intervention = intervention_object.intervene(combination = [1,1,1,1,1,1,1])

intervention_object.write_climate(like_df=like_df, write_folder=PROJECT_PATH+'formind_sim/weather_file/')


# print(intervention.item()['event_1'])

# def apply_intervention(clim_data, intervention):
    
#     print(intervention)
#     changed_clim = copy.deepcopy(clim_data)
#     if intervention[0] == 'rad':
#         index = 0 
#     elif intervention[0] == 'precip':
#         index = 1
#     elif intervention[0] == 'temp':
#         index =2

#     print(np.mean(changed_clim, axis =0))
#     changed_clim[intervention[1]:intervention[2], index] = changed_clim[intervention[1]:intervention[2], index] + intervention[3]
#     print(np.mean(changed_clim, axis =0))

#     return changed_clim


clim_1 = clim_data[0,:,:]
# clim_2 = clim_data[1,:,:]

intervention_clim_1 = clim_intervention[0,:,:]

fig , (ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (20, 10))

ax1.plot(clim_1[:,0], color = 'b')
ax1.plot(intervention_clim_1[:,0], color = 'r')
#ax1.plot(clim_2[:,0], color = 'b', alpha = 0.6, linestyle = '--')

ax2.plot(clim_1[:,1], color = 'b')
ax2.plot(intervention_clim_1[:,1], color = 'r')
#ax2.plot(clim_2[:,1], color = 'b', alpha = 0.2, linestyle = '--')


ax3.plot(clim_1[:,2], color = 'b')
ax3.plot(intervention_clim_1[:,2], color = 'r')
#ax3.plot(clim_2[:,2], color = 'b', alpha = 0.6, linestyle = '--')


plt.savefig(GRAPHICS_SAVE_FOLDER + 'intervention_example.png')

