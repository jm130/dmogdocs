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

.. list-table:: 
   :widths: 10 15 10 10 10 10 10 25
   :header-rows: 1

   * - JOBID
     - PARTITION
     - NAME
     - USER
     - ST
     - TIME
     - NODES
     - NODELIST(REASON)
   * - JOBID
     -
     - Row 1, column 3
     - pp
     - 00
     - jlkj
     - jhkh
     - hjhkj
 
Where

.. list-table:: 
   :widths: 25 75

   * - JOBID
     - Job or step ID. For array jobs, the job ID format will be of the form <job_id>_<index>
   * - PARTITION
     - Partition of the job/step
   * - NAME
     - Name of the job/step
   * - USER
     - Owner of the job/step
   * - ST
     - State of the job/step. See below for a description of the most common states
   * - TIME
     - Time used by the job/step. Format is days-hours:minutes:seconds (days,hours only printed as needed)
   * - NODES
     - Number of nodes allocated to the job or the minimum number of nodes required by a pending job
   * - NODELIST(REASON)
     - For pending jobs: Reason why pending.
       For failed jobs: Reason why failed.
       For all other job states: List of allocated nodes. See below for a list of the most common reason codes.
       
During its lifetime, a job passes through several states. The most common states are PENDING, RUNNING, 
SUSPENDED, COMPLETING, and COMPLETED. Some other states are shown in the table below:   

.. list-table:: 
   :widths: 15 85

   * - PD
     - Pending. Job is waiting for resource allocation
   * - R
     - Running. Job has an allocation and is running
   * - S
     - Suspended. Execution has been suspended and resources have been released for other jobs
   * - CA
     - Cancelled. Job was explicitly cancelled by the user or the system administrator
   * - CG
     - Completing. Job is in the process of completing. Some processes on some nodes may still be active
   * - CD
     - Completed. Job has terminated all processes on all nodes with an exit code of zero
   * - F
     - Failed. Job has terminated with non-zero exit code or other failure condition
     
If the job has failed or it is pending, a reason for its current state is given in the last 
column of the ``squeue`` output. Some of the most common reasons are:


.. list-table:: 
   :widths: 20 80

   * - (Resources)
     - The job is waiting for resources to become available so that the jobs resource request can be fulfilled
   * - (Priority)
     - The job is not allowed to run because at least one higher prioritized job is waiting for resources
   * - (Dependency)
     - The job is waiting for another job to finish first (–dependency=… option)
   * - (TimeLimit)
     - The job exhausted its time limit.
   * - (ReqNodeNotAvail)
     - Some node required by the job is currently not available. The node may currently be in use, reserved for another job, in an advanced reservation, DOWN, DRAINED, or not responding
   * - JobLaunchFailure
     - The job could not be launched. This may be due to a file system problem, invalid program name, etc.
  
For a complete list of job states codes and reasons, see `Job State Codes <https://slurm.schedmd.com/squeue.html#lbAG>`_ and `Job Reasons <https://slurm.schedmd.com/squeue.html#lbAF>`_    
