MATLAB
======

MATLAB is a high-level programming language and interactive environment widely 
used for numerical computation, visualization, and programming. It provides an extensive 
collection of mathematical functions, algorithms, and toolboxes for various areas of 
engineering, science, and finance. MATLAB is designed to make numerical analysis and data 
processing easier, faster, and more accurate. It is widely used in academia, research, and 
industry for a range of applications, from data analysis and visualization to control 
systems design and image processing.

MATLAB is available for use under the university's licenses for teaching and academic 
research purposes. If you need to use MATLAB for other purposes, please contact 
ISHelp@hw.ac.uk for further guidance.

Running MATLAB jobs
===================

To use MATLAB on the cluster, you need to load the MATLAB module first. 
You can do this by running the following commands in your terminal:

.. code-block:: bash

   flight env activate gridware
   module load apps/matlab/r2022b
   
To run MATLAB jobs on the cluster, you need to create a job script that contains the 
MATLAB commands that you want to run. Here is an example job script (``my_matlab_job.sh``):
   
.. code-block:: bash
   
   #!/bin/bash
   #SBATCH --job-name=my-matlab-job
   #SBATCH --output=my-matlab-job.out
   #SBATCH --error=my-matlab-job.err
   #SBATCH --nodes=1
   #SBATCH --cpus-per-task=4
   #SBATCH --time=00:30:00
   
   flight env activate gridware
   module load apps/matlab/r2022b
   
   matlab -nodesktop -nosplash -r "my_matlab_script"

This job script requests one node with four CPUs and a maximum run time of 30 minutes. 
It loads the MATLAB module and runs a MATLAB script called ``my_matlab_script``. The output 
and error messages are written to ``my-matlab-job.out`` and ``my-matlab-job.err`` respectively.

Here is an example MATLAB script that calculates the sum of two numbers (``my_matlab_script.m``):

.. code-block:: bash

   a = 5;
   b = 10;
   c = a + b;
   disp(['The sum of a and b is ', num2str(c)]);

Save this script as ``my_matlab_script.m`` and put it in the same directory as your job script.
To submit the job script to the cluster, run the following command in the terminal:

.. code-block:: bash

   sbatch my_matlab_job.sh

This will submit the job script to the cluster, and you can monitor the job status using the ``squeue`` command.

Here is an example job script that requests a GPU node and uses the "gpu" queue (``my_matlab_gpu_job.sh``):

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=my-matlab-gpu-job
   #SBATCH --output=my-matlab-gpu-job.out
   #SBATCH --error=my-matlab-gpu-job.err
   #SBATCH --nodes=1
   #SBATCH --cpus-per-task=4
   #SBATCH --gres=1
   #SBATCH --partition=gpu
   #SBATCH --time=00:30:00
   
   flight env activate gridware
   module load apps/matlab/r2022b
   module load apps/nvidia-cuda/11.2.2
   
   matlab -nodesktop -nosplash -r "my_matlab_gpu_script"

This job script is like the previous one, but it requests a GPU node with one GPU and uses 
the "gpu" queue. It also loads the CUDA toolkit module to enable GPU acceleration in MATLAB.

Here is an example MATLAB script that uses the GPU to perform matrix multiplication (``my_matlab_gpu_script.m``):

.. code-block:: bash

   a = gpuArray.rand(1000);
   b = gpuArray.rand(1000);
   c = a * b;
   d = gather(c);
   disp(d);

Save this script as ``my_matlab_gpu_script.m`` and put it in the same directory as your job script.

To submit the job script to the cluster, run the following command in the terminal:

.. code-block:: bash

   sbatch my_matlab_gpu_job.sh

This will submit the job script to the "gpu" queue, and the cluster will allocate a GPU node for your job to run.
