#!/usr/bin/env bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --time=12:40:00
#SBATCH --gres=gpu
#SBATCH --job-name=INV0
#SBATCH -A hai_deep_c
#SBATCH -o inv_0.out
#SBATCH -e inv_.err
#SBATCH --mail-user=itsmohitanand@gmail.com

module load Stages/2022  GCCcore/.11.2.0 SciPy-bundle/2021.10 
module load GCC/11.2.0  OpenMPI/4.1.1 h5py/3.5.0
module load matplotlib/3.4.3
module load Seaborn/0.11.2

source venv/bin/activate

# Run script

python script_19_generate_climate_comb.py 