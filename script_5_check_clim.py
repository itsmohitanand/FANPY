import pandas as pd
import matplotlib.pylab as plt


fname_1 = 'Projects/Project_Beech/formind_parameters/Climate/weatherGermany_100_ori.txt'
fname_2 = 'Projects/Project_Beech/formind_parameters/Climate/weatherGermany_era5_adjusted.txt'

data_1 = pd.read_csv(fname_1, delimiter=' ')
data_2 = pd.read_csv(fname_1, delimiter=' ')

print(data_1.describe())
print(data_2.describe())


fig, ax  = plt.subplots(1,1 ,figsize = (10,4))

y_1 = data_1.iloc[14000:15000,1].values 
y_2 = data_1.iloc[14000:15000,1].values 

plt.plot(y_1)
plt.plot(y_2)

plt.savefig('check.png')
