from fanpy import Formind

home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'

model_path = home_dir	
par_file_name='beech'
project_path= home_dir + 'formind_sim/sim_100ha_19/'

num_sim = 1
print(model_path)
print(project_path)
print(par_file_name)
model = Formind(model_path, project_path, par_file_name)
sim_id = 'spinoff'
model.run(sim_id=sim_id, num_sim=num_sim)