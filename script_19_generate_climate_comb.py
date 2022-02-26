from fanpy.process import get_combination, Intervention
import pandas as pd
import numpy as np
from fanpy.run_formind import run_formind_intervention
import os

PROJECT_PATH = "/p/project/hai_deep_c/project_data/forest-carbon-flux/"

DATA_PATH = PROJECT_PATH + "ml_data/"

GRAPHICS_SAVE_FOLDER = DATA_PATH + "graphics/"

MODEL_SAVE_FOLDER = DATA_PATH + "models/"

intervention_f = DATA_PATH + "intervention_dict.npy"

clim_data_f = DATA_PATH + 'av_gpp_clim.npy'

clim_data = np.load(clim_data_f)

intervention = np.load(intervention_f, allow_pickle = True)
           
like_df = pd.read_csv(PROJECT_PATH + '/formind_sim/sim_100ha_spin/formind_parameters/Climate/weather_sim_1000.txt', delimiter=' ')


c = 0
list_compound = get_combination(c=c)

for compound in list_compound:
    ## Delete any files in the folder 
    compound_string = ''.join(map(str, compound))

    folder_path =  PROJECT_PATH + f'formind_sim/compound_{c}/{compound_string}/'
    isExist = os.path.exists(folder_path)
	
    if not isExist:
        os.makedirs(folder_path)
        print(f"The new directory is created at {folder_path}")
    
    # Delete anything inside the folder
    cmd = 'rm -r ' + folder_path+'*'
    os.system(cmd)

    ## Add base spinoff
    cmd = 'cp -r ' + PROJECT_PATH + 'formind_sim/sim_100ha_spin_base/* ' + PROJECT_PATH + f'formind_sim/compound_{c}/{compound_string} '
    os.system(cmd)


    intervention_object = Intervention(climate_data=clim_data, intervention_dict=intervention.item())

    clim_intervention = intervention_object.intervene(combination = compound)
    
    #add_climate
    intervention_object.write_climate(like_df=like_df, write_folder=PROJECT_PATH+'formind_sim/')

    run_formind_intervention(compound)
