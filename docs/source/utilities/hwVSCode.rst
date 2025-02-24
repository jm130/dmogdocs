hwVSCode
========

This tool is used to create a job in the system which you can connect to via VS Code for development or testing purposes.

There is also a version if a GPU is required: hwVSCodeGPU

To use this tool, please first follow the steps for getting setup to connect to DMOG via VS Code shown :ref:`HERE <user-connecting>`

Please note, however, that you will need to modify part of the config file:

In your SSH config file, under hpc-job, rather than "ProxyCommand ssh dmog 'nc $(squeue --me --name=vsCode --states=R -h -O NodeList) 2222'"

Please use "ProxyCommand ssh dmog 'nc \$(squeue --me --name=vsCode --states=R -h -O NodeList) $(< ~/hwTunnelPort)'"

An example output:

.. code-block:: bash

    [gp27@login1 [dmog] scripts]$ hwVSCode
    Starting VSCode CPU job...
    VSCode job started.
    JobID: 190028
    End time: Mon 24 Feb 10:21:36 GMT 2025

    To cancel job early: scancel 190028

Once you have run the tool, you can connect to DMOG using vsCode as normal.
