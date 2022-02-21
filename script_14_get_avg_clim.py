from statistics import mode
import h5py 
import numpy as np
import matplotlib.pylab as plt

DATA_PATH = "/p/project/hai_deep_c/project_data/forest-carbon-flux/ml_data/"

GRAPHICS_SAVE_FOLDER = DATA_PATH + "graphics/"

MODEL_SAVE_FOLDER = DATA_PATH + "models/"

data_stats_f = MODEL_SAVE_FOLDER + 'final_model/model_stats.h5'


gpp_arr = np.zeros(9000*20)

for i in range(20):

    clim_data_f = DATA_PATH + f'data_100ha_{i}.h5'

    with h5py.File(clim_data_f, 'r') as f:
        # X = f['X']
        # irr = X['irradiance'][:, :]
        # rain = X['rain'][:, :]
        # temp = X['temperature'][:, :]
        Y = f['Y']
        gpp_arr[i*9000:(i+1)*9000] = Y['GPP'][:]

sorted_index = np.argsort(gpp_arr)

fig, ax = plt.subplots()
mean_gpp = np.mean(gpp_arr)
print(mean_gpp)
diff = np.abs((gpp_arr - mean_gpp))
ind_mean = np.argsort(diff)


clim_sim = np.zeros((100, 4*365, 3))

gpp_av = np.zeros(100)

counter = 0
for ind in ind_mean[:100]:
    i = ind//9000
    index = ind%9000

    clim_data_f = DATA_PATH + f'data_100ha_{i}.h5'

    with h5py.File(clim_data_f, 'r') as f:
        X = f['X']
        irr = X['irradiance'][index-3:index+1, :]
        rain = X['rain'][index-3:index+1, :]
        temp = X['temperature'][index-3:index+1, :]
        Y = f['Y']
        gpp = Y['GPP'][index]

    clim_sim[counter, :, 0] = irr.reshape(-1)
    clim_sim[counter, :, 1] = rain.reshape(-1)
    clim_sim[counter, :, 2] = temp.reshape(-1)

    gpp_av[counter] = gpp 

    counter+=1

# print(irr.shape)
# print(rain.shape)
# print(temp.shape)
# print(gpp.shape)

# counter = 0

# gppm = np.average(gpp)

# print(gppm-0.005,gppm+0.005 )

# index_list = []
# for i in range(2004, 9000):
#     gpp_i = gpp[i]
#     if gppm - 0.005 < gpp_i < gppm + 0.005:
#         print(i, counter, gpp_i)
#         counter+=1
#         index_list.append(i)
#     if counter > 19:
#         break

# clim_sim = np.zeros((20, 4*365, 3))

# gpp_av = np.zeros(20)

# for i, index_val in enumerate(index_list):
#     clim_sim[i, :, 0] = irr[index_val-3:index_val+1].reshape(-1)
#     clim_sim[i, :, 1] = rain[index_val-3:index_val+1].reshape(-1)
#     clim_sim[i, :, 2] = temp[index_val-3:index_val+1].reshape(-1)

#     gpp_av[i] = gpp[index_val] 

print(np.mean(gpp_av))
np.save(DATA_PATH+'av_gpp_clim.npy', clim_sim)
np.save(DATA_PATH+'av_gpp.npy', gpp_av)
