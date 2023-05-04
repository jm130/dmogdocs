Job Management
==============

DMOG uses the ``Slurm`` job scheduler to manage resources and ensure fair access for all users. 
To submit jobs to the scheduler, users write a submission script specifying the required resources 
(such as the number of CPUs, amount of memory, etc.) and input/output files. 
After submitting a job, ``Slurm`` will try to allocate the requested resources and start the job. 
If the requested resources are not immediately available, the job will be queued until enough resources become available.

In addition to batch mode jobs, ``Slurm`` also supports interactive jobs which can be useful for testing code or 
troubleshooting problems. To start an interactive session, users can request an allocation of resources and 
then start a shell session on a compute node.

``Slurm`` is not only used to submit and monitor jobs, but also to describe 
the resources required for the jobs. To ensure that your job runs efficiently, 
it is important to specify the correct resources in your submission script. 


Basic Slurm commands
--------------------

*	``sinfo``: This command is used to display information about the nodes available on the cluster, such as their state (idle, down, etc.), partition, number of CPUs, and amount of available memory. It can help users choose appropriate resources for their jobs.
*	``squeue``: This command is used to display the current queue of jobs on the cluster, including their status, user, and estimated start time. It can help users track the progress of their jobs and estimate when they will start running.
*	``sbatch``: This command is used to submit a batch job to the Slurm scheduler. Users specify the required resources and the commands to run in a script, and then submit the script using the sbatch command. The job is then scheduled by the Slurm scheduler and run on the requested resources.
*	``scancel``: This command is used to cancel a running or pending job on the cluster. Users can specify the job ID or job name to be cancelled.
*	``scontrol``: This command is used to view and modify Slurm configuration and status information. It can be used to monitor the status of Slurm components.
*	``squeue``: use this command to get a high-level overview of all active (running and pending) jobs in the cluster. 

Further information about these commands is available in the online manual: ``man <command>``

Job queue states and reasons
----------------------------

The ``squeue`` command allows users to view information about the state of a job. The default output format of the command is as follows:

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     


