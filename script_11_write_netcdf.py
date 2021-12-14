import h5py
import pandas as pd
from fanpy.io import read_climate_file

index = 0

DATA_PATH = '/p/project/hai_hhhack/anand1/Project_Data/forest-carbon-flux/'

cflux_csv = DATA_PATH + f'formind_sim/results_{index}_16ha/beech_general_00.cflux'

df_cflux = pd.read_csv(cflux_csv, '\t', skiprows=[0,1])

print(df_cflux)

fpath = DATA_PATH + f"forest_data_16_ha_{index}" + ".hdf5"

# with h5py.File(fpath, 'w') as f:
#     X = f.create_group("X")
#     X = f.create_group("Y")
    
#     X.create_dataset('rain', data = )
#     X.create_dataset('temp', data = )
#     X.create_dataset('irradiance', data = )
    
#     Y.create_dataset('GPP', data = )
   
# raw_X = (irradiance, rain, temp)

# raw_Y = gpp

# print(
#     Fore.CYAN
#     + f"raw_X-(irradiance, rainfall, temperature) | raw_Y-gpp for index {index}"
# )
# print(Style.RESET_ALL)

# return raw_X, raw_Y