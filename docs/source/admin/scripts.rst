Info Scripts
============

We have created a number of infromational scripts to allow users to see more information about their jobs, as well as the cluster itself.

These scripts are located in /opt/site/hwscripts/

hwNodes: This script will show you information on each node in the cluster, how many CPU cores, GPUs, and how much memory they have. It also displays the current usage information, how many CPU cores, GPUs, or memory are currently in use on each node.

hwStatus: This small script shows a very high level overview of the cluster, how many CPU cores and GPUs are in use in total, how many active jobs there are, and how many are waiting in the queue.

hwEfficiency: This script will show you various information about a given users jobs that have run over a given timeframe. Total Number of jobs, average CPU efficiency of those jobs, average memory efficiency, average wait time (time in the queue before starting), and average runtime.

  This script is intended to help users efficiently request resources. Requesting more resources (CPU cores, memory, GPUs) than needed can cause a job to wait longer in the queue than needed while waiting for those resources to be freed up, and also prevents other users' jobs from running as there are fewer resouces left available while said job is running.
  A low average CPU efficiency metric shows that too many CPU cores are being requested on average. For example, if you always request 32 CPU cores for your jobs, and your CPU efficiency is <50% you should be able to request only 16 CPU cores for your jobs with no impact on performance, while helping keeping the queue clear. The same applies to the average memory efficiency metric.
