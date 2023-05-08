R
==

R is a programming language and software environment used for statistical 
computing and graphics. It provides a wide variety of statistical and graphical 
techniques, and is highly extensible. R is popular among researchers and data 
analysts in many fields, and is widely used in the academic and business communities.

Running R jobs
--------------

To run R on the HPC cluster, you need to load the appropriate software module:

.. code-block:: bash

   flight env activate gridware
   module load apps/R/4.2.3

To run R on the CPU queue, you need to create a job script that specifies the resources 
required for your job. Here is an example job script:

.. code-block:: bash
   
   #!/bin/bash
   #SBATCH --job-name=my_R_job
   #SBATCH --output=output.log
   #SBATCH --error=error.log
   #SBATCH --partition=nodes
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=8
   #SBATCH --time=01:00:00
   
   # Load the R module
   flight env activate gridware
   module load R/4.2.3
   
   # Run the R script
   Rscript my_R_script.R
   
In this example, the job is submitted to the nodes partition, which is the default 
partition for CPU jobs. The job requests one node with 8 CPU cores 
(``--nodes=1`` and ``--cpus-per-task=8``). The job also requests a runtime 
of 1 hour (``--time=01:00:00``). The ``my_R_script.R`` file is the R script that you want to run.

To run R on the GPU queue, you need to use a different partition and request the appropriate resources.

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=my_R_job
   #SBATCH --output=output.log
   #SBATCH --error=error.log
   #SBATCH --partition=gpu
   #SBATCH --gres=gpu:1
   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=4
   #SBATCH --time=01:00:00
   
   # Load the R module
   flight env activate gridware
   module load R/4.2.3
   
   # Run the R script
   Rscript my_R_script.R
   
In this example, the job is submitted to the gpu partition, which is the partition 
for GPU jobs. The job requests one node with 1 GPU (``--gres=gpu:1``), 
4 CPU cores (``--cpus-per-task=4``), and a runtime of 1 hour (``--time=01:00:00``). 
The ``my_R_script.R`` file is the R script that you want to run.

Here are a couple of simple R scripts that you can use to test your setup:

**Example 1: Hello World**

.. code-block:: bash

   # Print "Hello, world!" to the console
   cat("Hello, world!\n")

**Example 2: Basic Data Analysis**

.. code-block:: bash

   # Load the built-in iris dataset
   data(iris)
   
   # Print the dimensions of the dataset
   cat("Number of rows: ", nrow(iris), "\n")
   cat("Number of columns: ", ncol(iris), "\n")
   
   # Compute the mean of the Sepal.Length variable
   mean_sepal_length <- mean(iris$Sepal.Length)
   cat("Mean Sepal.Length: ", mean_sepal_length, "\n
