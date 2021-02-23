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
from tqdm import trange
from forpy.io import read_climate_file, write_climate_file



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
		for i in trange(num_sim):
			par_file_path_new = par_file_without_ext+'_'+sim_id+'_'+str(i).zfill(2)+par_file_ext
			copyfile(par_file_path_ori, par_file_path_new)
			run_command = self.model_path+'formind '+par_file_path_new
			output_command = '1>'+ouput_path+'stout_'+str(i).zfill(2)+'.txt'
			error_command = '2>'+ouput_path+'sterr_'+str(i).zfill(2)+'.txt'
			command = run_command+' '+output_command+' '+error_command
			os.system(command)
			os.remove(par_file_path_new)
			
		print(f'Simulation completed for {sim_id} scenario')

	def generate_scenario_climate(self, climate_file:str, scenario:str, **kwargs):
		self.scenario = scenario
		if scenario=="percentage-change":
			perc = kwargs['perc']
			scenario_dict = {
				'I':1+perc/100, # Increase
				'U': 1,	# Usual
				'D':1-perc/100, # Decrease
			}
		else:
			pass
		
		climate_file_path = self.project_path+'formind_parameters/Climate/'
		
		val_list = []
		key_list = []
		for key, val in scenario_dict.items():
			key1 = key
			val1 = val
			for key, val in scenario_dict.items():
				key2 = key
				val2 = val
				for key,val in scenario_dict.items():
					key3 = key
					val3 = val
					val_list.append([val1,val2, val3])
					key_list.append([key1,key2,key3])

		for i in range(len(key_list)):
			data = read_climate_file(climate_file, climate_file_path).values
			val_arr = np.array(val_list[i])
			key = key_list[i]
			data[100000:105001,0:3] = val_arr* data[100000:105001,0:3]

			write_file_name = scenario+'_'+''.join(key)+'_perc_'+str(perc)+'_climate_400y.txt'

			write_climate_file(write_file_name, climate_file_path, nparray = data)

	def change_par_climate(self, cfile_name:str):
		
		par_file_name = self.project_path+'formind_parameters/'+self.par_file_name+".par"
		print(par_file_name)	
		with open(par_file_name, 'r+') as f:
			list_lines = f.readlines()
			f.truncate(0)
			line_num = 636
			initial_line = list_lines[636]
			new_line = '	'+cfile_name+'\n'
			list_lines[636] = new_line
			f.writelines(list_lines)

		
	# def run_scenario(self, scenario, num_sim_per_scenario = 10):
	# 	self.scenario = scenario

	# 	climate_dir = self.project_path+'formind_parameters/Climate/'

	# 	list_all_files = os.listdir(climate_dir)
	# 	for each in list_all_files:
	# 		if each.split('_')[0]== scenario:
	# 			sim_id = '_'.join(each.split('_')[:4])
	# 			print(sim_id)
	# 			# self.change_par_climate(each)
	# 			# self.run(sim_id=sim_id, num_sim=num_sim_per_scenario)