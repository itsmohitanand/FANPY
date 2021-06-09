import pandas as pd
import matplotlib.pylab as plt
import numpy as np

clim_dir = 'Projects/Project_Beech/formind_parameters/Climate/'

clim_fname = 'weatherGermany_100_ori.txt'

clim_fpath = clim_dir+clim_fname

data = pd.read_csv(clim_fpath, delimiter=' ')

strt = 901
num_year = 10000
index = [i for i in range(num_year*365)]

X = pd.DataFrame(index = index, columns=data.columns)

def create_clim_data(index, data, X, strt):    

    # Read the data
    sim_dir = '/data/compoundx/WG_sim/'
    fname = 'clim_dly_'+str(index)+'.csv'
    sim_fpath = sim_dir+fname

    sim = pd.read_csv(sim_fpath, header=None)
    sim_col = ['day', 'precip', 'press', 'temp', 'wind', 'swr', 'cc', 'rh']

    # For personal reference name the coloumns
    sim.columns = sim_col

    # Remove leap year 
    sim = sim[sim.day!=366]



    # Convert precip to mm/day
    sim.precip = sim.precip*24
    sim['irr'] = sim.swr*5.0

    # prep data
    num_year = 100

    dl = np.tile(data.iloc[:365, 3], num_year)

    strt_index =  (index-strt)*365*num_year 
    end_index = (index-strt+1)*365*num_year

    X.iloc[strt_index:end_index, 0] = sim.precip
    X.iloc[strt_index:end_index, 1] = sim.temp
    X.iloc[strt_index:end_index, 2] = sim.irr
    X.iloc[strt_index:end_index, 3] = dl
    X.iloc[strt_index:end_index, 4] = 12
    X.iloc[strt_index:end_index, 5] = 400

    return X

for i in range(strt, strt + int(num_year/100)):
    X = create_clim_data(i, data, X, strt)
    if i%10 == 0:
        print(f'Percentange complete {(i-strt+1)*10000/num_year} %')
        print(f'{i}th Climate file read')


X.to_csv(f'/data/compoundx/FORMIND/Project_Beech/formind_parameters/Climate/weather_sim_10000_{strt//100}.txt', sep = ' ', index= False, float_format='%.3f')