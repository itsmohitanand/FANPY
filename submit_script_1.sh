#!/usr/bin/env bash

#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --time=20:00:00
#SBATCH --gres=gpu
#SBATCH --job-name=FORMIND
#SBATCH -A hai_deep_c
#SBATCH -o for_sim_1.out
#SBATCH -e for_sim_1.err
#SBATCH --mail-user=itsmohitanand@gmail.com

module load Stages/2022  GCCcore/.11.2.0 SciPy-bundle/2021.10 
module load GCC/11.2.0  OpenMPI/4.1.1 h5py/3.5.0
module load matplotlib/3.4.3

source venv/bin/activate

# Run script

python script_1_beech.py