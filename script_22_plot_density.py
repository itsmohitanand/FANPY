from fanpy.process import get_combination
import numpy as np
import os
import pandas as pd
import matplotlib.pylab as plt
import h5py
import seaborn as sns


DATA_PATH = "/p/project/hai_deep_c/project_data/forest-carbon-flux/ml_data/"

home_dir = '/p/project/hai_deep_c/project_data/forest-carbon-flux/'


intervention_list = get_combination(c=0)
#intervention_list.extend(get_combination(c=1))
# intervention_list.extend(get_combination(c=2))
# intervention_list.extend(get_combination(c=3))
# intervention_list.extend(get_combination(c=4))
# intervention_list.extend(get_combination(c=5))
# intervention_list.extend(get_combination(c=6))
intervention_list.extend(get_combination(c=7))

num_sim = 100

base_gpp = np.zeros(num_sim)

num = len(intervention_list)
print(num)
intervention_gpp = np.zeros((num_sim, num-1))

xticklabels = []
for i in range(num_sim):
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

print(base_gpp.shape)
print(intervention_gpp.shape)


print(num)



gpp_arr = np.zeros(9000*20)

for i in range(20):

    clim_data_f = DATA_PATH + f'data_100ha_{i}.h5'

    with h5py.File(clim_data_f, 'r') as f:

        Y = f['Y']
        gpp_arr[i*9000:(i+1)*9000] = Y['GPP'][:]

print(gpp_arr.shape)

fig , (ax1, ax2) = plt.subplots(1,2)
ax1.hist(gpp_arr*100, density = True, alpha =0.4, bins = 100)
ax1.hist(base_gpp*100, density = True, alpha =0.4, bins = 20)
ax1.hist(intervention_gpp*100, density = True, alpha =0.4, bins = 20)

ax2.hist((base_gpp-intervention_gpp[:,0])*100, density = True, bins = 30)
plt.savefig('scratch_2.png')
plt.close()


sns.distplot(gpp_arr*100)
sns.distplot(base_gpp*100, bins = 20)
sns.distplot(intervention_gpp*100, bins = 20)
plt.savefig('scratch_3.png')

# fig, ax = plt.subplots(1,1, figsize = (8,6))

# ax.hist(gpp_arr*100, alpha = 0.1, bins = 20, density = True)
# ax.hist(base_gpp*100, alpha = 0.5, bins = 20, density = True)

# for r in range(num-1):

#     ax.hist(intervention_gpp[:,r]*100, alpha = 0.5, bins = 20, density = True)


#     # mean_gpp[r] = np.mean(base_gpp - intervention_gpp[:,r])*100

# # ax.set_xticks(np.arange(num-1))
# # ax.set_xticklabels(xticklabels)
# # ax.tick_params(axis='x', labelrotation = 90)
# # ax.axhline(mean_gpp[0], color = 'r', label = 'compound')
# #ax.axhline(np.sum(mean_gpp[1:]), color = 'b', label = 'sum_each')

# plt.legend()
# fig.tight_layout()