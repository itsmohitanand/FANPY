#!/bin/bash
 
#SBATCH --job-name=download_cloud
#SBATCH --time=30:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --mail-type=ALL
 
#SBATCH --mail-user=itsmohitanand@gmail.com
 
# output files
#SBATCH -o download_cloud.out
#SBATCH -e download_cloud.err

# Load Environment
module purge
module load Anaconda3
source ~/.bashrc
conda activate FANPY38

# Run script

python script_3_download.py