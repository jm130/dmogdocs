A word on OpenFlightHPC 
=======================

We have installed ``OpenFlightHPC`` on our cluster to provide a robust and scalable HPC management solution 
for our users. With ``OpenFlightHPC``, users have access to a suite of tools that can help them manage 
their jobs and resources more effectively, improving the overall efficiency and productivity of the 
cluster. Additionally, the modular nature of ``OpenFlightHPC`` allows us to easily add new functionality 
and adapt the system to meet evolving needs.

HPC User environments (flight env)
----------------------------------

User environments (i.e flight environments) are software environments that have been pre-configured 
to support specific applications or workflows on an HPC cluster. They typically include a specific 
combination of software libraries, compilers, and tools that are required to run the application or 
workflow effectively.

On DMOG, there are several flight environments available to users, including ``Gridware``, ``Conda``, and ``Singularity``. 
``Gridware`` is a package manager that provides access to a range of pre-built software packages that have 
been compiled for use on the cluster, including the ``Modules`` package that allows you to load and manage 
software modules on the cluster. ``Conda`` is an open-source package management system and environment management 
system that makes it easy to install and manage multiple software packages on the cluster. ``Singularity`` is 
a containerization tool that allows you to create and run containers that encapsulate specific software environments and dependencies.

By providing these flight environments on the cluster, we aim to make it easier for users to access the 
software and tools they need to complete their work. Each flight environment has its own unique features 
and benefits. You can easily explore and manage the flight environments available on the 
cluster by using these commands: 

* ``flight env avail``: This command will display a list of all the available flight environments on the cluster. It will show you the name of each environment, as well as a brief description of its purpose and contents.
* ``flight env activate <env_name>``: This command is used to activate a specific flight environment on the cluster. Replace <env_name> with the name of the environment you want to activate. Once activated, any commands you run will be executed within the selected environment.
*	``flight env info``: This command will display detailed information about the currently active flight environment, including the environment's name, description, and location on the cluster.
*	``flight env deactivate``: This command is used to deactivate the currently active flight environment. Once deactivated, any commands you run will be executed outside of the selected environment.

Remote desktop (flight desktop)
--------------------------------

When working on interactive applications on an HPC cluster, it can often be difficult to test and fine-tune 
your workflows, especially when you're working remotely. That's where Flight desktop comes in. By providing a 
desktop environment that you can access remotely, Flight desktop gives you the flexibility to work on your applications 
from your desktop or laptop computer as if they were running locally.

Now, let's look at the pre-requisites for Windows, Mac, and Linux:

*	Windows:
   * VNC viewer: You will need to install a VNC viewer, such as TightVNC or RealVNC, to connect to your Flight Desktop session.
   * SSH client: You will need to install an SSH client, such as PuTTY, to connect to your HPC cluster account and launch Flight Desktop.
* Mac:
   * VNC viewer: You can use the built-in Screen Sharing app on Mac to connect to your Flight Desktop session, or you can install a third-party VNC viewer such as RealVNC.
   * SSH client: The built-in Terminal app on Mac can be used as an SSH client to connect to your HPC cluster account and launch Flight Desktop.
* Linux:
   * VNC viewer: You can install a VNC viewer, such as Remmina or TigerVNC, to connect to your Flight Desktop session.
   * SSH client: Most Linux distributions come with an SSH client pre-installed, so you should be able to use your system's built-in SSH client to connect to your HPC cluster account and launch Flight Desktop.

To launch a flight desktop environment, follow these steps:

#.	Log in to your HPC cluster account.
#.	Open a terminal window and type ``flight desktop start <desktop-name>`` to launch ``Flight Desktop``. If you're unsure what name to use, you can find the list of available desktop sessions by typing ``flight desktop avail``.
#.	Wait for the desktop environment to start up. Be patient, this may take a few minutes.
#.	Once the desktop environment has started, you can connect to it using a ``VNC viewer``. The specific details for connecting to Flight Desktop will be shown on the screen once the desktop session is created and can be retrieved by using this command: ``flight desktop show <sessionid>``, where sessionid is the ID for the specific session.
#.	Note that the desktop sessions are created on the login node, and they must be terminated manually by the user when they are no longer needed. To do so, you can use the ``flight desktop kill <sessionid>`` command. 

For further information on using Flight Desktop, you can consult the online manual available through ``flight help desktop``.

Disabling OpenFlightHPC
-----------------------

``OpenFlightHPC`` is a powerful tool for HPC users, but there may be situations where users want to disable it. 
Some reasons for disabling ``OpenFlightHPC`` could include avoiding potential conflicts with other software installed 
on the cluster, or simply not needing any of the features provided by ``OpenFlightHPC``.

To disable ``OpenFlightHPC``, users can issue the ``flight stop`` command, which will stop any currently running 
Flight services. Additionally, users can use the ``flight set always off`` command to disable Flight services 
from starting up automatically in the future. It's important to note that these commands only affect 
the user who issues them and not the entire cluster.
