from statistics import mode
from typing import Dict
import h5py 
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm


DATA_PATH = "/p/project/hai_deep_c/project_data/forest-carbon-flux/ml_data/"

GRAPHICS_SAVE_FOLDER = DATA_PATH + "graphics/"

MODEL_SAVE_FOLDER = DATA_PATH + "models/"

data_stats_f = MODEL_SAVE_FOLDER + 'final_model/model_stats.h5'

clim_data_f = DATA_PATH + 'av_gpp_clim.h5'

with h5py.File(data_stats_f) as f:
    clim_diff = f['concept_1_clim_diff_17'][:,:]
    concept_0 = f['concept_0_counter_17'][()]
    concept_1 = f['concept_1_counter_17'][()]

# Detail analysis Radiation 
month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n_year = 4
x_ticks = [0]
for _ in range(n_year):
    for i in range(1,13):
        x_ticks.append(x_ticks[-1]+month_day[i])

x_ticklabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']*n_year
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w
    
w = 14

x = np.arange(n_year*365)

rad = clim_diff[:, 0]
precip = clim_diff[:, 1]
temp = clim_diff[:, 2]

mov_av_rad = moving_average(rad, w)
mov_av_precip = moving_average(precip, w)
mov_av_temp = moving_average(temp, w)


x_mov = x[w//2:-w//2+1]
## Manually taking 2 months threshold with average_diff greater than 5

# for i, rad_i in zip(x_mov, mov_av_rad):
#     if abs(rad_i) > 10:
#         print(i)


rad_1_strt = 841
rad_1_end = 935
x_rad_1 = np.linspace(rad_1_strt, rad_1_end, rad_1_end-rad_1_strt+1)
av_rad_1 = np.repeat(np.mean(rad[rad_1_strt:rad_1_end]), rad_1_end - rad_1_strt + 1)

rad_2_strt = 1192
rad_2_end = 1342
x_rad_2 = np.linspace(rad_2_strt, rad_2_end, rad_2_end-rad_2_strt+1)
av_rad_2 = np.repeat(np.mean(rad[rad_2_strt:rad_2_end]), rad_2_end - rad_2_strt + 1)

# for i, rad_i in zip(x_mov, mov_av_precip):
#     if abs(rad_i) > 0.25:
#         print(i)

precip_3_strt = 839
precip_3_end = 951
x_precip_3 = np.linspace(precip_3_strt, precip_3_end, precip_3_end-precip_3_strt+1)
av_precip_3 = np.repeat(np.mean(precip[precip_3_strt:precip_3_end]), precip_3_end - precip_3_strt + 1)

precip_4_strt = 971
precip_4_end = 1126
x_precip_4 = np.linspace(precip_4_strt, precip_4_end, precip_4_end-precip_4_strt+1)
av_precip_4 = np.repeat(np.mean(precip[precip_4_strt:precip_4_end]), precip_4_end - precip_4_strt + 1)


precip_5_strt = 1220
precip_5_end = 1300

x_precip_5 = np.linspace(precip_5_strt, precip_5_end, precip_5_end-precip_5_strt+1)
av_precip_5 = np.repeat(np.mean(precip[precip_5_strt:precip_5_end]), precip_5_end - precip_5_strt + 1)

# for i, rad_i in zip(x_mov, mov_av_temp):
#     if abs(rad_i) > 0.5:
#         print(i)

temp_6_strt = 1098
temp_6_end = 1220
x_temp_6 = np.linspace(temp_6_strt, temp_6_end, temp_6_end-temp_6_strt+1)
av_temp_6 = np.repeat(np.mean(temp[temp_6_strt:temp_6_end]), temp_6_end - temp_6_strt + 1)

temp_7_strt = 1361
temp_7_end = 1386

x_temp_7 = np.linspace(temp_7_strt, temp_7_end, temp_7_end-temp_7_strt+1)
av_temp_7 = np.repeat(np.mean(temp[temp_7_strt:temp_7_end]), temp_7_end - temp_7_strt + 1)

fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(16,8))

ax1.plot(x,rad, alpha = 0.2)
ax1.plot(x_mov, mov_av_rad, color = 'b', alpha = 0.5)

ax1.plot(x_rad_1, av_rad_1, linestyle='--', color = 'r')
ax1.axvline(rad_1_strt, linestyle='--', color = 'r', alpha = 0.5)
ax1.axvline(rad_1_end, linestyle='--', color = 'r', alpha = 0.5)

ax1.plot(x_rad_2, av_rad_2, linestyle='--', color = 'r')
ax1.axvline(rad_2_strt, linestyle='--', color = 'r', alpha = 0.5)
ax1.axvline(rad_2_end, linestyle='--', color = 'r', alpha = 0.5)

ax1.axhline(color = 'k', linestyle = '--')

ax2.plot(x,precip, alpha = 0.2)
ax2.plot(x_mov, mov_av_precip, color = 'b', alpha = 0.5)

ax2.plot(x_precip_3, av_precip_3, linestyle='--', color = 'r')
ax2.axvline(precip_3_strt, linestyle='--', color = 'r', alpha = 0.5)
ax2.axvline(precip_3_end, linestyle='--', color = 'r', alpha = 0.5)

ax2.plot(x_precip_4, av_precip_4, linestyle='--', color = 'r')
ax2.axvline(precip_4_strt, linestyle='--', color = 'r', alpha = 0.5)
ax2.axvline(precip_4_end, linestyle='--', color = 'r', alpha = 0.5)

ax2.plot(x_precip_5, av_precip_5, linestyle='--', color = 'r')
ax2.axvline(precip_5_strt, linestyle='--', color = 'r', alpha = 0.5)
ax2.axvline(precip_5_end, linestyle='--', color = 'r', alpha = 0.5)

ax2.axhline(color = 'k', linestyle = '--')

ax3.plot(x,temp, alpha = 0.2)
ax3.plot(x_mov, mov_av_temp, color = 'b', alpha = 0.5)

ax3.plot(x_temp_6, av_temp_6, linestyle='--', color = 'r')
ax3.axvline(temp_6_strt, linestyle='--', color = 'r', alpha = 0.5)
ax3.axvline(temp_6_end, linestyle='--', color = 'r', alpha = 0.5)

ax3.plot(x_temp_7, av_temp_7, linestyle='--', color = 'r')
ax3.axvline(temp_7_strt, linestyle='--', color = 'r', alpha = 0.5)
ax3.axvline(temp_7_end, linestyle='--', color = 'r', alpha = 0.5)


ax3.axhline(color = 'k', linestyle = '--')

plt.savefig(GRAPHICS_SAVE_FOLDER+'intervention/example.png')

intervention_dict = dict()

intervention_dict['event_1'] = ('rad', rad_1_strt, rad_1_end, av_rad_1[0])
intervention_dict['event_2'] = ('rad', rad_2_strt, rad_2_end, av_rad_2[0])
intervention_dict['event_3'] = ('precip', precip_3_strt, precip_3_end, av_precip_3[0])
intervention_dict['event_4'] = ('precip', precip_4_strt, precip_4_end, av_precip_4[0])
intervention_dict['event_5'] = ('precip', precip_5_strt, precip_5_end, av_precip_5[0])
intervention_dict['event_6'] = ('temp', temp_6_strt, temp_6_end, av_temp_6[0])
intervention_dict['event_7'] = ('temp', temp_7_strt, temp_7_end, av_temp_7[0])
intervention_dict['concept'] = (concept_0, concept_1)


print(intervention_dict)

np.save(DATA_PATH+'intervention_dict.npy', intervention_dict)