ABAQUS
======

To use Abaqus on DMOG, first you need to create an input file from the model you are looking to submit. You can do this in Abaqus CAE on your PC by right-clicking on the job you want to run on DMOG and select Write Input. This will create a file with the same name as the job's name.

Next, connect to DMOG and run the following commands:

.. code-block:: bash
  
  flight env activate gridware
  module load apps/abaqus/2024

This will activate Abaqus and ensure it is ready to use for your jobs.

You should see something similar to this:  


.. code-block:: bash
  
  [gp27@login1 [dmog] ~]$ flight env activate gridware
  <gridware{+}> [gp27@login1 [dmog] ~]$ module load apps/abaqus/2024
  apps/abaqus/2024
   |
   OK
  <gridware{+}> [gp27@login1 [dmog] ~]$




Next, copy your input file from earlier to DMOG. Then, to submit a job to DMOG create a script (.sh) file similar to this (replacing the info in the [ ] ):



.. code-block:: slurm

  #!/bin/bash
  #SBATCH --job-name=TestCPUs
  #SBATCH --ntasks-per-node=16
  #SBATCH --mem-per-cpu=1024
  #SBATCH --time=05:00:00
  abaqus job=[nameForYourJob] input=[yourInputFile].inp cpus=16 interactive


The values next to --cpus-per-task, --mem-per-cpu, and --time can be adjusted as needed to suit your job. Please note that higher values next to --cpus-per-task and --mem may mean that your job has to wait for a while before these resources are available.

More info on the SBATCH values can be found here: `Job Submission <https://dmogdocs.readthedocs.io/en/latest/user/jobsubmission.html>`_

Once you have created the script file you can submit the job by running this command:

``sbatch yourscript.sh``

Note that this will need to be run from within the folder where the .inp file is, or specify the full path to it in your script.

Once your job is submitted, you can monitor it either via the sacct command, or by using:

``tail -f [yourJobName].sta``

or

``tail -f [yourJobName].msg``
