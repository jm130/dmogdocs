ORCA
====

ORCA is a general-purpose quantum chemistry program package that features virtually all modern electronic 
structure methods (density functional theory, many-body perturbation and coupled cluster theories, and multireference 
and semiempirical methods). It is designed with the aim of generality, extendibility, efficiency, and user friendliness. 
Its main field of application is larger molecules, transition metal complexes, and their spectroscopic properties

Please note that ORCA does not currently support GPU acceleration. Therefore, when utilizing ORCA on our HPC cluster, 
it is essential to optimize job scripts and resource allocation for CPU-based calculations to achieve optimal performance.

Running ORCA jobs
-----------------

To run ORCA on the HPC cluster, you need to load the appropriate software module:

.. code-block:: bash

   flight env activate gridware
   module load apps/ORCA/5.0.4
   module load mpi/openmpi/4.0.7
   
Below is an example of a job script and input file for running a basic ORCA calculation:

.. code-block:: bash

   !/bin/bash
   
   #SBATCH --job-name=orca-test
   #SBATCH --nodes=1
   #SBATCH --tasks-per-node=4
   #SBATCH --time=1:00:00
   #SBATCH --partition=nodes
   
   export UCS_LOG_LEVEL=error
   
   flight env activate gridware
   module load apps/orca
   module load mpi/openmpi
   
   input=input.inp
   
   $ORCADIR/orca ${input} > ${input}.out 2>&1

In the example, the job is submitted to the CPU queue (``--partition=nodes``). It reserves 4 cores for 1 hour.

The input file (``input.inp``):

.. code-block:: bash

   ! DLPNO-CCSD(T) cc-pVTZ cc-pVTZ/C cc-pVTZ/jk rijk verytightscf TightPNO LED
   # Specify number of processors
   %pal
   nprocs 4
   end
   # Specify memory
   %maxcore 12000
   %mdci
   printlevel 3
   end
   * xyz 0 1
   O 1.327706 0.106852 0.000000 
   H 1.612645 -0.413154 0.767232
   H 1.612645 -0.413154 -0.767232
   O -1.550676 -0.120030 -0.000000
   H -0.587091 0.053367 -0.000000
   H -1.954502 0.759303 -0.000000
   *
   %geom
   Fragments
   2 {3:5} end
   end
   end

