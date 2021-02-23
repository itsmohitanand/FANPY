from fanpy import Formind

model_path = '/home/anand/github/FORMIND-addon/'	
par_file_name='beech-forest-monoculture'
project_path='/home/anand/github/FORMIND-addon/Projects/Project_Beech/'


num_sim = 1
model = Formind(model_path, project_path, par_file_name)
sim_id = 'general'
model.run(sim_id=sim_id, num_sim=num_sim)