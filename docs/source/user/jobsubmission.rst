Job Submission
==============

Batch Jobs
----------

To submit a batch job to the cluster, you need a submission script that contains two parts. 
The first part, located at the top of the script, describes the resources that the job requires 
using ``#SBATCH`` directives. These directives are treated as ``Slurm`` options and specify the necessary resources 
for the job. The second part of the submission script contains the job-specific shell commands.

``Slurm`` options can also be added to the sbatch command directly as command line arguments, 
which will override the ones embedded in the job script.

Batch jobs are submitted to the cluster via ``sbatch``. 

For example: ``sbatch ./myJob.sh``

Here are some examples of job submission scripts:

Serial job
~~~~~~~~~~

.. code-block:: bash

   #!/bin/bash -l

   ################# Part-1 Slurm directives ####################
   ## Working dir
   ## Environment variables
   #SBATCH --export=ALL
   ## Output and Error Files
   #SBATCH -o job-%j.output
   #SBATCH -e job-%j.error
   ## Job name
   #SBATCH -J serial-test
   ## Run time: "hours:minutes:seconds", "days-hours"
   #SBATCH --time=00:05:00
   ## Memory limit (in megabytes)
   #SBATCH --mem=1024
   ## Specify partition
   #SBATCH -p nodes

   ################# Part-2 Shell script ####################
   #===============================
   #  Activate Flight Environment
   #-------------------------------
   source "${flight_ROOT:-/opt/flight}"/etc/setup.sh

   #===========================
   #  Create results directory
   #---------------------------
   RESULTS_DIR="$(pwd)/${SLURM_JOB_NAME}-outputs/${SLURM_JOB_ID}"
   echo "Your results will be stored in: $RESULTS_DIR"
   mkdir -p "$RESULTS_DIR"
   
   #===============================
   #  Application launch commands
   #-------------------------------
   # Customize this section to suit your needs.
   
   echo "Executing job commands, current working directory is $(pwd)"
   
   # REPLACE THE FOLLOWING WITH YOUR APPLICATION COMMANDS

   echo "Hello, dmog" > $RESULTS_DIR/test.output
   echo "This is an example job. It ran on `hostname -s` (as `whoami`)." >> $RESULTS_DIR/test.output
   echo "Output file has been generated, please check $RESULTS_DIR/test.output"

Shared memory job
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   #!/bin/bash -l
   
   ################# Part-1 Slurm directives ####################
   ## Working dir
   ## Environment variables
   #SBATCH --export=ALL
   ## Output and Error Files
   #SBATCH -o job-%j.output
   #SBATCH -e job-%j.error
   ## Job name
   #SBATCH -J shared-mem-test
   ## Run time: "hours:minutes:seconds", "days-hours"
   #SBATCH --time=00:05:00
   ## Memory limit (in megabytes). Total --mem or amount per cpu --mem-per-cpu
   #SBATCH --mem-per-cpu=1024
   ## Processing slots
   #SBATCH --nodes=1
   #SBATCH --ntasks=32
   ## Specify partition
   #SBATCH -p nodes
   
   ################# Part-2 Shell script ####################
   #===============================
   #  Activate Flight Environment
   #-------------------------------
   source "${flight_ROOT:-/opt/flight}"/etc/setup.sh
   
   #===========================
   #  Create results directory
   #---------------------------
   RESULTS_DIR="$(pwd)/${SLURM_JOB_NAME}-outputs/${SLURM_JOB_ID}"
   echo "Your results will be stored in: $RESULTS_DIR"
   mkdir -p "$RESULTS_DIR"
   
   #===============================
   #  Application launch commands
   #-------------------------------
   # Customize this section to suit your needs.
   
   echo "Executing job commands, current working directory is $(pwd)"
   
   # REPLACE THE FOLLOWING WITH YOUR APPLICATION COMMANDS
   
   echo "Hello, dmog" > $RESULTS_DIR/test.output
   echo "This is an example job. It ran on `hostname -s` (as `whoami`)." >> $RESULTS_DIR/test.output
   echo "Output file has been generated, please check $RESULTS_DIR/test.output"

Parallel (mpi) job
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   #!/bin/bash -l
   
   ################# Part-1 Slurm directives ####################
   ## Working dir
   ## Environment variables
   #SBATCH --export=ALL
   ## Output and Error Files
   #SBATCH -o job-%j.output
   #SBATCH -e job-%j.error
   ## Job name
   #SBATCH -J parallel-mpi-test
   ## Run time: "hours:minutes:seconds", "days-hours"
   #SBATCH --time=00:05:00
   ## Memory limit (in megabytes). Total --mem or amount per cpu --mem-per-cpu
   #SBATCH --mem-per-cpu=1024
   ## Processing slots
   #SBATCH --nodes=2
   #SBATCH --ntasks=32
   ## Specify partition
   #SBATCH -p nodes
   
   ################# Part-2 Shell script ####################
   #===============================
   #  Activate Flight Environment
   #-------------------------------
   source "${flight_ROOT:-/opt/flight}"/etc/setup.sh
   
   #==============================
   #  Activate Package Ecosystem
   #------------------------------
   # e.g.:
   # Load the OpenMPI module for access to `mpirun` command
   flight env activate gridware
   module load mpi/openmpi
   
   if ! command -v mpirun &>/dev/null; then
       echo "No mpirun command found, ensure that a version of MPI is installed and available in PATH" >&2
       exit 1  
   fi
   
   #===========================
   #  Create results directory
   #---------------------------
   RESULTS_DIR="$(pwd)/${SLURM_JOB_NAME}-outputs/${SLURM_JOB_ID}"
   echo "Your results will be stored in: $RESULTS_DIR"
   mkdir -p "$RESULTS_DIR"
   
   #===============================
   #  Application launch commands
   #-------------------------------
   # Customize this section to suit your needs.
   
   echo "Executing job commands, current working directory is $(pwd)"
   
   # REPLACE THE FOLLOWING WITH YOUR APPLICATION COMMANDS

   echo "Hello, dmog" > $RESULTS_DIR/test.output
   echo "This is an example job. It was allocated $SLURM_NTASKS slot(s) across $SLURM_JOB_NUM_NODES node(s). The master process ran on `hostname -s` (as `whoami`)." >>    $RESULTS_DIR/test.output
   mpirun -np $SLURM_NTASKS \
       /bin/bash -c \
       'echo "This process was executed on `hostname -s` with rank $OMPI_COMM_WORLD_RANK."' \
       >> $RESULTS_DIR/test.output
   
   echo "Output file has been generated, please check $RESULTS_DIR/test.output"

GPU job
~~~~~~~

.. code-block:: bash

   #!/bin/bash -l

   ################# Part-1 Slurm directives ####################
   ## Working dir
   ## Environment variables
   #SBATCH --export=ALL
   ## Output and Error Files
   #SBATCH -o job-%j.output
   #SBATCH -e job-%j.error
   ## Job name
   #SBATCH -J gpu-test
   ## Run time: "hours:minutes:seconds", "days-hours"
   #SBATCH --time=00:05:00
   ## Memory limit (in megabytes). Total --mem or amount per cpu --mem-per-cpu
   #SBATCH --mem-per-cpu=1024
   ## GPU requirements
   #SBATCH --gres gpu:1
   ## Specify partition
   #SBATCH -p gpu
   
   ################# Part-2 Shell script ####################
   #===============================
   #  Activate Flight Environment
   #-------------------------------
   source "${flight_ROOT:-/opt/flight}"/etc/setup.sh
   
   #==============================
   #  Activate Package Ecosystem
   #------------------------------
   # e.g.:
   # Load the OpenMPI module for access to `mpirun` command
   flight env activate gridware
   module load mpi/openmpi
   
   if ! command -v mpirun &>/dev/null; then
       echo "No mpirun command found, ensure that a version of MPI is installed and available in PATH" >&2
       exit 1
   fi
      
   #===========================
   #  Create results directory
   #---------------------------
   RESULTS_DIR="$(pwd)/${SLURM_JOB_NAME}-outputs/${SLURM_JOB_ID}"
   echo "Your results will be stored in: $RESULTS_DIR"
   mkdir -p "$RESULTS_DIR"
   
   #===============================
   #  Application launch commands
   #-------------------------------
   # Customize this section to suit your needs.
   
   echo "Executing job commands, current working directory is $(pwd)"
   
   # REPLACE THE FOLLOWING WITH YOUR APPLICATION COMMANDS
   
   echo "Hello, dmog" > $RESULTS_DIR/test.output
   echo "This is an example job. It ran on `hostname -s` (as `whoami`)." >> $RESULTS_DIR/test.output
   echo "I was allocated the following GPU devices: $CUDA_VISIBLE_DEVICES" >> $RESULTS_DIR/test.output
   echo "Output file has been generated, please check $RESULTS_DIR/test.output"
   
Interactive Jobs
================

When debugging or developing code, interactive testing is often necessary. However, running interactive jobs 
directly on the login node can cause overloading. It is recommended to run interactive jobs on the compute nodes 
instead. This allows you to debug your code in the same environment that it will run in. 

Resource allocation for interactive jobs is done through the command line.

To start an interactive session on CPU node:

.. code-block:: bash
 
   srun --nodes=1 --ntasks-per-node=32 --mem=1024 --time=00:05:00 --partition=nodes --pty /usr/bin/bash 
   
On a GPU enabled node, the command is very similar:

.. code-block:: bash

   srun --nodes=1 --ntasks-per-node=32 --mem=1024 --time=00:05:00 --partition=gpu --gres=gpu:1 --pty /usr/bin/bash 

Making dynamic jobs scripts
===========================

``Slurm`` provides several environment variables at runtime that can be used to create more dynamic submission scripts. 
These variables can be used to specify the job name, set the number of nodes or tasks, and much more. 
Here are some of the main environment variables that Slurm creates at runtime:

* ``SLURM_JOB_NAME``: The name of the job
* ``SLURM_JOB_ID``: The job ID number
* ``SLURM_JOB_CPUS_PER_NODE``: The number of CPUs per node
* ``SLURM_JOB_NODELIST``: The list of nodes allocated to the job
* ``SLURM_ARRAY_TASK_ID``: The index of the job within an array job

In addition, ``Slurm`` also supports using format characters in submission scripts to define directives. 
These format characters can be used to dynamically specify options such as the output file name or the number 
of nodes to use. Here are some of the most common format characters:

*	``%j``: Job ID
*	``%N``: Node name
*	``%u``: User name
*	``%a``: Array job ID
*	``%A``: Array job ID range

By using these environment variables and format characters, you can create more dynamic and flexible submission scripts 
that can adapt to different job requirements. For example, you can use the ``%j`` format character to dynamically specify
the output file name based on the job ID, or use the ``SLURM_JOB_CPUS_PER_NODE`` variable to dynamically set the number of CPUs to use.


