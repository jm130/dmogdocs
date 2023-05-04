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

Here are some examples of job submission scripts:

 Serial job
 ~~~~~~~~~~

.. code-block:: bash

   #!/bin/bash -l

   ################# Part-1 Slurm directives ####################
   ## Working dir
   #SBATCH -D /users/username
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
   #SBATCH -D /users/username
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
   #SBATCH -D /users/username
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


