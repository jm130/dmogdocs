.. _vsCodeSlurm:

hwVSCode
========

This tool is used to create a job in the system which you can connect to via VS Code for development or testing purposes.

There is also a version if a GPU is required: hwVSCodeGPU

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

   Submitting VSCode CPU job...done.
   VSCode job started.
   JobID: 195659
   Port used: 2222
   End time: Wed  5 Mar 18:02:59 GMT 2025

   To cancel job early: scancel 195659

Once you have run the tool, you can connect to DMOG using VS Code by clicking Remote Explorer on the left, then clicking the arrow next to hpc-job on the list of remotes.

Please note that depending on how busy the cluster is, your job may not start immediately and be put in the queue. Should this happen you'll see an output like this:

.. code-block:: bash
   
   [gp27@login1 [dmog] scripts]$ ./hwVSCode 

   Submitting VSCode CPU job...done.
   VSCode job queued.
   Job ID: 195655
   Port Used: 2361

   Job waiting to start. Please monitor job using 'squeue -j 195655' to see when it starts.
