#!/bin/bash
 
#SBATCH --job-name=run_sim
#SBATCH --time=0-01:30:00
#SBATCH --mem-per-cpu=16G
#SBATCH --mail-type=ALL
 
#SBATCH --mail-user=itsmohitanand@gmail.com
 
# output files
#SBATCH -o run_sim.out
#SBATCH -e run_sim.err

# Load Environment
module purge
module load Anaconda3
source ~/.bashrc
conda activate FANPY38

# Run script

python script_1_beech.py