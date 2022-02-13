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

module load GCCcore/.10.3.0 SciPy-Stack/2021-Python-3.8.5

module load h5py/3.1.0-serial-Python-3.8.5

source venv/bin/activate

# Run script

python script_1_beech.py