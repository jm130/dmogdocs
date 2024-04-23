VSCode via Slurm
================

To create a job on DMOG and have VSCode connect to the job to debug code etc:

You will need to have an SSH keypair set up for connecting to DMOG.

Open VSCode, install the 'Remote - SSH' extension.

Modify/create your SSH config file (Windows: C:\\users\\[username]\\.ssh\\config Mac: ~/.ssh/config) to include the following:

Note that you may need to create the '.ssh' folder and the 'config' config file if they are not already there.

.. code-block:: bash
  
  Host dmog
    User [YOUR USERNAME]
    IdentityFile [PATH TO YOUR DMOG SSH PRIV KEY]
    ControlMaster auto
    HostName dmog.hw.ac.uk

  Host hpc-job
    User [YOUR USERNAME]
    IdentityFile [PATH TO YOUR DMOG SSH PRIV KEY]
    ProxyCommand ssh dmog "nc $(squeue --me --name=tunnel --states=R -h -O NodeList) 2222"
    StrictHostKeyChecking no


SSH in to DMOG via command line (or other SSH client you normally use)

Create a file called ``interact.sh``, Set its contents to:

.. code-block:: bash

  srun --job-name "vsCode" --cpus-per-task 2 --mem-per-cpu 500 --time 1:00:00 sshd -D -p 2222 -f /dev/null -h ~/.ssh/id_alcescluster


Allow it to be executed:
    
``chmod +x interact.sh``

Run the [interact.sh](<http://interact.sh>) script. Then go to VS Code and connect to the hpc-job host under remote connections on the left.



