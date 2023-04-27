AMBER
=====

AMBER (Assisted Model Building with Energy Refinement) is a widely used 
software package for molecular dynamics simulations of biomolecules. It 
allows users to simulate the motion and behaviour of molecules in a variety 
of conditions, such as in different solvents or under different temperatures.

On DMOG, users can access AMBER by activating the gridware flight 
environment using the command `flight env activate gridware`. Once activated, the 
AMBER package module can be loaded using the command `module load apps/amber/22/gcc-12.2.0`. 
This will make the AMBER tools and executables available for use on the cluster. 

AMBER includes several executables that are commonly used for molecular dynamics 
simulations. Some of the most frequently used executables include:
* `sander`: The main molecular dynamics engine used in AMBER, which can perform energy minimization, equilibrium simulations, and production runs.
* `pmemd`: An optimized version of sander that can run on GPUs, which can significantly accelerate molecular dynamics simulations.
* `cpptraj`: A utility that can perform a variety of tasks related to analyzing and processing the output from AMBER simulations, such as calculating RMSDs, extracting specific frames from a trajectory, and generating input files for other programs.

Running AMBER jobs
------------------
An example job script for AMBER would be:

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=amber
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=32
   #SBATCH --cpus-per-task=1
   #SBATCH --time=1:00:00
   #SBATCH --mem=128G
   #SBATCH --partition=nodes
   
   # Load required modules
   flight env activate gridware
   module load apps/amber/22/gcc-12.2.0
   
   # Change to the directory where input files are located
   cd /path/to/input/files
   
   # Run the Amber simulation
   srun --mpi=pmi2 $AMBERHOME/bin/pmemd.MPI -O -i input.in -o output.out -p prmtop -c inpcrd -r output.rst
   
In this script, the job is named "amber" and will run on a single node with 32 tasks (processes) 
per node, using 1 CPU per task. The requested memory is 128GB and the job has a maximum runtime of 1 hour. 
The "nodes" partition is specified.

The required modules for Amber and Gridware are loaded, and the script changes to the directory where 
the input files for the simulation are located. Finally, the Amber simulation is run using the `srun` 
command with the appropriate arguments. 


