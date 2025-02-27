hwVSCode
========

This tool is used to create a job in the system which you can connect to via VS Code for development or testing purposes.

There is also a version if a GPU is required: hwVSCodeGPU

.. _vsCodeSlurm:

To use this tool, please first modify/create your SSH config file (Windows: C:\\users\\[username]\\.ssh\\config Mac/Linux: ~/.ssh/config) to include the following:

.. note::
   You may need to create the '.ssh' folder and the 'config' config file if they are not already there.

.. code-block:: bash
  
  Host dmog
    User [YOUR USERNAME]
    IdentityFile [PATH TO YOUR DMOG SSH PRIV KEY]
    ControlMaster auto
    HostName dmog.hw.ac.uk

  Host hpc-job
    User [YOUR USERNAME]
    IdentityFile [PATH TO YOUR DMOG SSH PRIV KEY]
    ProxyCommand ssh dmog 'nc $(squeue --me --name=vsCode --states=R -h -O NodeList) $(< ~/hwTunnelPort)'
    StrictHostKeyChecking no

.. note::
   If your computer is using Windows 10 you will need to use double quotes (" "), instead of the single quotes (' ') as shown above.

When hwVSCode is run, it creates a small file in your home directory called hwTunnelPort. This file contains the port number used by the job, which your SSH config above tells VS Code to use to connect to the compute node.

An example output:

.. code-block:: bash

    [gp27@login1 [dmog] ~]$ hwVSCode

    Starting VSCode CPU job...
    VSCode job started.
    JobID: 190340
    Port used: 2313
    End time: Tue 25 Feb 09:52:10 GMT 2025

    To cancel job early: scancel 190340

Once you have run the tool, you can connect to DMOG using VS Code as normal.
