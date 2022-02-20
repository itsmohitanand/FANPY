from fanpy import Formind
import numpy as np
import os
import time

initial_time = time.time()

home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'

par_file_name='beech'

compound = np.array([0,0,0,0,0,0,0])

c = np.sum(compound)

compound_string = ''.join(map(str, compound))


## Delete any files in the folder 
cmd = 'rm -r ' + home_dir + f'formind_sim/compound_{c}/{compound_string}/*'
os.system(cmd)

## Add base spinoff
cmd = 'cp -r ' + home_dir + 'formind_sim/sim_100ha_spin_base/ ' + home_dir + f'formind_sim/compound_{c}/{compound_string}/ '
os.system(cmd)

intervention_path = home_dir + f'formind_sim/compound_{c}/{compound_string}/sim_100ha_spin_base/'
model_path = intervention_path
project_path = intervention_path

# add climate file

from_folder = home_dir+f'formind_sim/weather_file/compound_{c}/{compound_string}/* '
to_folder = home_dir + f'formind_sim/compound_{c}/{compound_string}/sim_100ha_spin_base/formind_parameters/Climate/'
cmd = 'cp -r ' + from_folder + to_folder 
os.system(cmd)



for i in range(10):
    initial_sim_time = time.time()

    par_file = open(intervention_path + 'formind_parameters/beech.par', 'r')
    list_lines = par_file.readlines()
    list_lines[695] = f'    weather_intervention_c{c}_comb_{compound_string}_{i}.txt \n'
    par_file.close()

    par_file = open(intervention_path + 'formind_parameters/beech.par', 'w')
    par_file.writelines(list_lines)
    par_file.close()

    # print(model_path)
    # print(project_path)
    # print(par_file_name)
    model = Formind(model_path, project_path, par_file_name)
    sim_id = f'c{c}_{i}'
    model.run(sim_id=sim_id, num_sim=1)

    print(f'Time taken for simulation {i} is {time.time()-initial_sim_time} seconds')

## Delete .res file for size 

cmd =  'rm '+intervention_path + 'results/*.res'
os.system(cmd)

print(f'Total time taken is {time.time()-initial_time} seconds')