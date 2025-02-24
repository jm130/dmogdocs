hwEfficiency
============

hwEfficiency allows you to check the CPU and memory efficiency of your successfully completed jobs. It will also provide information about number of successful jobs, waittime, runtime, and power usage.

It is intended to assist you with ensuring you are only requesting the resources you require, as requesting too much memory, for example, may cause your job(s) to wait in the queue for much longer than needed.

The tool will ask you which username you'd like to check the jobs for (defaulting to your own), and how many days back you'd like to check for jobs.

An example output:

.. code-block:: bash

    [gp27@login1 [dmog] scripts]$ hwEfficiency
    Enter username to check [gp27]: 
    Enter duration to check in days [30]: 
 
    Total number of valid jobs: 2
    Average CPU efficiency: 1.05%
    Average maximum memory efficiency: 2.67%
    Average waittime: 00:00:00
    Average runtime: 00:16:15
    Average power usage: .1571kWh
    Total power usage: .3142kWh

To assist with testing resource requests for jobs, it is also possible to check the efficiency of a single job by providing a job ID when you run the command, like so:

.. code-block:: bash

    [gp27@login1 [dmog] scripts]$ hwEfficiency 189624
 
    Total number of valid jobs: 1
    Average CPU efficiency: 94.86%
    Average maximum memory efficiency: 8.85%
    Average waittime: 00:00:02
    Average runtime: 21:41:07
    Average power usage: 13.6070kWh
    Total power usage: 13.6070kWh
