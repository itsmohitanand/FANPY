from fanpy import Formind

home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'

model_path = home_dir	
par_file_name='beech'
project_path= home_dir + 'formind_sim/compound_7/1111111/sim_100ha_spin_base/'

num_sim = 1
print(model_path)
print(project_path)
print(par_file_name)
model = Formind(model_path, project_path, par_file_name)
sim_id = 'c7_9'
model.run(sim_id=sim_id, num_sim=num_sim)