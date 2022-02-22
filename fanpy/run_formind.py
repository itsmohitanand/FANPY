#
# Created on Tue Nov 24 2020
#
# Copyright (c) 2020 Mohit Anand
#
# For any details contact itsmohitanand@gmail.com 
######################

# This script is used to run multiple simulations for FORMIND model with different seeds and output names.

import os
from shutil import copyfile
import numpy as np
from fanpy.io import read_climate_file
import time

class Formind(object):
	def __init__(self,model_path: str, project_path: str, par_file_name:str) -> None:
		self.model_path = model_path
		self.project_path = project_path
		self.par_file_name = par_file_name

	def run(self, sim_id, num_sim):
		par_file_ext = '.par'
		par_file_without_ext = self.project_path+'formind_parameters/'+self.par_file_name
		par_file_path_ori = par_file_without_ext+par_file_ext
	
		ouput_path = self.project_path+'results/'
		for i in range(num_sim):
			par_file_path_new = par_file_without_ext+'_'+sim_id+'_'+str(i).zfill(2)+par_file_ext
			copyfile(par_file_path_ori, par_file_path_new)
			run_command = self.model_path+'formind '+par_file_path_new
			output_command = '1>'+ouput_path+'stout_'+str(i).zfill(2)+'.txt'
			error_command = '2>'+ouput_path+'sterr_'+str(i).zfill(2)+'.txt'
			command = run_command+' '+output_command+' '+error_command
			os.system(command)
			os.remove(par_file_path_new)
			
		print(f'Simulation completed for {sim_id} scenario')

def run_formind_intervention(compound):
	initial_time = time.time()

	home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'

	par_file_name='beech'

	c = np.sum(compound)

	compound_string = ''.join(map(str, compound))


	intervention_path = home_dir + f'formind_sim/compound_{c}/{compound_string}/'
	model_path = intervention_path
	project_path = intervention_path


	for i in range(100):
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

