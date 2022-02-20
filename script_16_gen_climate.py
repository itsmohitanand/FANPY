from statistics import mode
from typing import Dict
import h5py 
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm
import copy
import pandas as pd
import os

PROJECT_PATH = "/p/project/hai_deep_c/project_data/forest-carbon-flux/"

DATA_PATH = PROJECT_PATH + "ml_data/"

GRAPHICS_SAVE_FOLDER = DATA_PATH + "graphics/"

MODEL_SAVE_FOLDER = DATA_PATH + "models/"

intervention_f = DATA_PATH + "intervention_dict.npy"

clim_data_f = DATA_PATH + 'av_gpp_clim.npy'

clim_data = np.load(clim_data_f)

intervention = np.load(intervention_f, allow_pickle = True)


class Intervention(object):
    def __init__(self, climate_data, intervention_dict) -> None:
        super().__init__()

        self.climate_data = copy.deepcopy(climate_data)
        self.intervention_dict  = intervention_dict
        self.intervention_apllied = False

    def _precip_intervention(self, precip_intervention_tuple):
        tot_precip = np.mean(self.climate_data[:,precip_intervention_tuple[1]:precip_intervention_tuple[2], 1])
        diff_precip = precip_intervention_tuple[3]
        factor = (tot_precip + diff_precip)/tot_precip

        self.climate_data[:,precip_intervention_tuple[1]:precip_intervention_tuple[2], 1] = factor*self.climate_data[:,precip_intervention_tuple[1]:precip_intervention_tuple[2], 1]

    def _bias_intervention(self, intervention_tuple, index):
        
        self.climate_data[:,intervention_tuple[1]:intervention_tuple[2],index] = self.climate_data[:,intervention_tuple[1]:intervention_tuple[2], index] + intervention_tuple[3]
        
    def _intervene(self, intervention_tuple):
        if intervention_tuple[0] == 'rad':
            index = 0
            self._bias_intervention(intervention_tuple, index)
        elif intervention_tuple[0] == 'temp':
            index = 2
            self._bias_intervention(intervention_tuple, index)
        elif intervention_tuple[0] == 'precip':
            self._precip_intervention(intervention_tuple)

    def intervene(self, combination = [1, 1, 1, 1, 1, 1, 1] ):
        self.combination = np.array(combination)
        index_list = np.where(self.combination==1)[0]
        if len(index_list)>0:
            index_list+=1 # For event_index

            for each in index_list:
                intervention_tuple = self.intervention_dict[f'event_{each}']
                self._intervene(intervention_tuple)

        self.intervention_apllied = True
        print(f'Intervention applied {self.combination}')
        return self.climate_data

    def write_climate(self, like_df, write_folder):

        assert self.intervention_apllied == True,  f'No intervention applied'

        like_df.drop(like_df.index[365*4:], inplace=True)

        for i in range(self.climate_data.shape[0]):
            like_df.iloc[:,0] = self.climate_data[i, :, 1]
            like_df.iloc[:,1] = self.climate_data[i, :, 2]            
            like_df.iloc[:,2] = self.climate_data[i, :, 0]

            c = np.sum(self.combination)
            comb_str = "".join(map(str, self.combination))

            folder_path = write_folder + f'/compound_{c}/{comb_str}/'
            isExist = os.path.exists(folder_path)

            if not isExist:
                os.makedirs(folder_path)
                print(f"The new directory is created at {folder_path}")

            like_df.to_csv(folder_path + f'weather_intervention_c{c}_comb_{comb_str}_{i}.txt', sep = ' ', index= False, float_format='%.3f')            


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

