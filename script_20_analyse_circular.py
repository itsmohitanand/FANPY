from fanpy.process import get_combination
import numpy as np
import os
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'


intervention_list = get_combination(c=0)
#intervention_list.extend(get_combination(c=1))
# intervention_list.extend(get_combination(c=2))
# intervention_list.extend(get_combination(c=3))
# intervention_list.extend(get_combination(c=4))
# intervention_list.extend(get_combination(c=5))
# intervention_list.extend(get_combination(c=6))
intervention_list.extend(get_combination(c=7))


base_gpp = np.zeros(100)

num = len(intervention_list)
print(num)
intervention_gpp = np.zeros((10, num-1))

xticklabels = []
for i in range(100):
    for j, intervention in enumerate(intervention_list[:num]):
        compound = np.array(intervention)
        
        c = np.sum(compound)
        c_string = ''.join(map(str, compound))
        intervention_path = home_dir + f'formind_sim/compound_{c}/{c_string}/'
        path = intervention_path + f'/results/beech_c{c}_{i}_00.cflux'

        data = pd.read_csv(path, skiprows=2, delimiter= '\t')
        gpp = data['GPP'][4]

        if c==0:
            base_gpp[i]=gpp
        else:
            intervention_gpp[i, j-1] = gpp
            if i==0:
                xticklabels.append(c_string)



theta = 2*np.pi

# mean_gpp = np.zeros(8)

print(base_gpp)
print(intervention_gpp[:,0])
print(base_gpp - intervention_gpp[:,0])
fig, ax = plt.subplots(1,1, figsize = (8,6))

for r in range(num-1):

    ax.scatter([r]*100, (base_gpp - intervention_gpp[:,r])*100)
    # mean_gpp[r] = np.mean(base_gpp - intervention_gpp[:,r])*100

ax.set_xticks(np.arange(num-1))
ax.set_xticklabels(xticklabels)
ax.tick_params(axis='x', labelrotation = 90)
# ax.axhline(mean_gpp[0], color = 'r', label = 'compound')
#ax.axhline(np.sum(mean_gpp[1:]), color = 'b', label = 'sum_each')

plt.legend()
fig.tight_layout()
plt.savefig('scratch_2.png')