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
•	``flight env info``: This command will display detailed information about the currently active flight environment, including the environment's name, description, and location on the cluster.
•	``flight env deactivate``: This command is used to deactivate the currently active flight environment. Once deactivated, any commands you run will be executed outside of the selected environment.

Remote desktop (flight desktop)
-------------------------------

When working on interactive applications on an HPC cluster, it can often be difficult to test and fine-tune 
your workflows, especially when you're working remotely. That's where Flight desktop comes in. By providing a 
desktop environment that you can access remotely, Flight desktop gives you the flexibility to work on your applications 
from your desktop or laptop computer as if they were running locally.

Now, let's look at the pre-requisites for Windows, Mac, and Linux:

