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
from fanpy.io import read_climate_file

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
