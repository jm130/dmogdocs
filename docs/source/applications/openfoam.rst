OpenFoam
========

OpenFOAM is a popular open-source computational fluid dynamics (CFD) software 
package used for simulating complex fluid flow problems. It provides a 
comprehensive range of tools for solving problems involving flow of fluids, 
including heat and mass transfer.

Running OpenFoam jobs
---------------------

To run OpenFOAM on the cluster, you first need to load the appropriate module. 
On the DMOG cluster, the OpenFOAM module can be loaded using the following commands:

.. code-block:: bash

   flight env activate gridware
   module load apps/openfoamplus

.. note::
   The default version of OpenFOAM is 22.06, but we also have 24.12 available. This can be loaded with:

   .. code-block:: bash
      module load apps/openfoamplus/24.12
   
Once you have loaded the module, you can run OpenFOAM applications using the 
standard OpenFOAM command line interface. Here are a couple of example 
jobscripts to get you started:

**Example 1: Running an OpenFOAM job on the "nodes" queue**

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=myOpenFOAMJob
   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=16
   #SBATCH --time=1:00:00
   #SBATCH --partition=nodes
   
   flight env activate gridware
   module load apps/openfoamplus
   
   mpirun -np $SLURM_NTASKS --hostfile $SLURM_JOB_NODELIST interFoam -parallel

**Example 2: Running an OpenFOAM job on the "gpu" queue (using GPUs)**

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=myOpenFOAMJob
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=8
   #SBATCH --gres=gpu:1
   #SBATCH --time=1:00:00
   #SBATCH --partition=gpu
   
   flight env activate gridware
   module load apps/openfoamplus
   
   mpirun -np $SLURM_NTASKS --hostfile $SLURM_JOB_NODELIST interFoam -parallel

In the above examples, we use the mpirun command to run the OpenFOAM application in 
parallel. The ``-np`` option specifies the number of processes to be run, and ``--hostfile`` 
specifies the file that contains the list of hosts to be used for the job.
