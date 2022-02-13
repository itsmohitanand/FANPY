This is the code that needs to be added around line ~100


```
int   myResultFileSwitch.restart   1
int   myResultFileSwitch.restartplot   1

comment  ==============================
comment  --- Switches:TreeLists -------
comment  ==============================

float  N_Par.TreeListOutputStart  9
  \u years
  \d Time for first generation of tree list output (res-file containing each tree with position and cohort-file containing each cohort)
  \r 1.0:10000.0
  \i 1 General

float  N_Par.TreeListOutputStep  1
  \u years
  \d Time interval between generation of tree list outputs (res-file containing each tree with position and cohort-file containing each cohort)
  \r 1.0:10000.0
  \i 1 General

int  N_Par.TreeListInput  0
  \d Switch to specify if tree list should be read in to initialize simulation. 
  \d There needs to be an *.inv file in the formind_parameters directory. 
  \d Either copy the *.restart file from previous simulation run and change file extension to *.inv or prepare field inventory data to match the format of a *.restart file
  \r 0:1
  \i 0 General
  
int  N_Par.InitPools    0
  \d Switch to specify if carbon and seed pools per plot should be read in to initialize simulation.
  \d There needs to be an *.initpools file in the formind_parameters directory.
  \d Either copy the *.restartplot file from previous simulation run and change file extension to *.initpools or prepare field measurement data to match the format of a *.restartplot file
  \r 0:1
  \i 0 General
```


1. add the lines from the contineu.txt into your parfile after the List of outputfile (~ line 100 in your par file). With these new lines you create a .restart (containing the information of all trees) and .restartplot (containing the info of carbonpools and seeds) files

2. copy the restart and restartplot into your formind_parameter-folder.

3. rename XX.restart into XX.inv and XX.restartplot into XX.iniplot

4. add the following lines within the section "general" in your par file
string    N_Par.InvFileName    experiment.inv
    \d Name of initialization file for tree list input (from restart or inventory)
    \i 1 General
    
string    N_Par.InitPoolsFileName    experiment.initpools
    \d Name of initialization file for carbon and seed pool input (from restartplot or measurements)
    \i 1 General

5. rename experiment.inv and experiment.initpools into your names of the file...