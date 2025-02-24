hwInteractive
================

There are currently 2 hwInteractive tools available, hwCPUInteractive, and hwGPUInteractive.

These tools allows you to create an interactive job to connect to one of the compute nodes, CPU or GPU node respectively. Useful for testing things out as running code on the login node, or on a compute node outside of a job is not allowed and the processes will be terminated.

An example output:

.. code-block:: bash

    [gp27@login1 [dmog] scripts]$ hwCPUInteractive 
    flight start: Flight Direct environment is already active.
    [gp27@node06 [dmog] scripts]$

The resouces requested using these tools are quite limited, but if you'd like to adjust this you can just make a copy of the tool in your home directory and edit the values. The current tools look like this:

.. code-block:: bash

    hwCPUInteractive:
    srun --job-name "interactiveCPU" --cpus-per-task 16 --mem-per-cpu 1000 --time 00:30:00 --pty /usr/bin/bash

    hwGPUInteractive:
    srun --job-name "interactiveGPU" --cpus-per-task 8 --mem-per-cpu 1024 --partition=gpu --gres=gpu:1 --time 00:30:00 --pty /usr/bin/bash

