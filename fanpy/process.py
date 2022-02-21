import itertools
import copy
import numpy as np
import os

def get_combination(c=0, tot_compound = 7):
    results = []
    for events_ind in itertools.combinations(range(tot_compound), c):
        base = [0]*tot_compound
        for i in events_ind:
            base[i] =  1
        
        results.append(base)

    return results

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

            folder_path = write_folder + f'compound_{c}/{comb_str}/formind_parameters/Climate/'
            # isExist = os.path.exists(folder_path)
            # print(folder_path)
            # if not isExist:
            #     os.makedirs(folder_path)
            #     print(f"The new directory is created at {folder_path}")
            path =  folder_path + f'weather_intervention_c{c}_comb_{comb_str}_{i}.txt'
            like_df.to_csv(path, sep = ' ', index= False, float_format='%.3f')
            print(f'folder_written_to \n {path}')     