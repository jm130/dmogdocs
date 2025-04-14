Ansys
=======

Ansys can be enabled for use within your submission script (or interactively) with the following commands:

.. code-block:: bash
    
    flight env activate gridware
    module load apps/ansys

Here is an example of a full submission script for Ansys Fluent (provided by Assistant Professor Fabio Malizia):

.. code-block:: bash
    
    #!/bin/bash -l
    ################# Part-1 Slurm directives ####################
    # Working dir
    ##SBATCH -D /users/USERNAME/SimFolder ## Deactivated because the batch file is in the same folder 
    ## Job name
    #SBATCH -J JobName
    ## Environment variables
    #SBATCH --export=ALL
    ## Output and Error Files
    #SBATCH -o job-%j.output
    #SBATCH -e job-%j.error
    ## Run time: "hours:minutes:seconds", "days-hours"
    #SBATCH --time=144:05:00
    ## Memory limit (in megabytes). Total --mem or amount per cpu --mem-per-cpu
    ##SBATCH --mem-per-cpu=1024
    #SBATCH --mem=464000
    ## Processing slots
    #SBATCH --nodes=1
    #SBATCH --ntasks=64
    ## Specify partition
    #SBATCH -p nodes

    ################# Part-2 Shell script ####################
    #===============================
    #  Activate Flight Environment for Ansys Fluent
    #-------------------------------
    source "${flight_ROOT:-/opt/flight}"/etc/setup.sh
    # Load modules
    flight env activate gridware
    module load apps/ansys


    #===========================
    #  Create results directory
    #---------------------------
    #RESULTS_DIR="$(pwd)/${SLURM_JOB_NAME}-outputs/${SLURM_JOB_ID}"
    RESULTS_DIR="$(pwd)/${SLURM_JOB_ID}"
    echo "Your results will be stored in: $RESULTS_DIR"
    mkdir -p "$RESULTS_DIR"

    #===============================
    #  Application launch commands
    #-------------------------------
    # Customize this section to suit your needs.

    echo "Executing job commands, current working directory is $(pwd)"

    # Command time used to measure the time of the following command
    # Add -meshing after 3ddp if you want to start fluent in meshing mode
    time fluent 3ddp -t$SLURM_NPROCS -ssh -gu -driver null -i journalFile.jou > $RESULTS_DIR/outputFile.out 2> $RESULTS_DIR/errorFile.err

    date  ## echo the date at the end
    echo end of job
