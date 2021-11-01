from fanpy import Formind

home_dir = '/p/project/hai_hhhack/anand1/'

model_path = home_dir+'linux_models/'	
par_file_name='beech'
project_path= home_dir + 'Projects/FANPY/Projects/Project_Beech/'

num_sim = 1
model = Formind(model_path, project_path, par_file_name)
sim_id = 'general'
model.run(sim_id=sim_id, num_sim=num_sim)