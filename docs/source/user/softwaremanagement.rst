Software Management
===================

System software
---------------

HPC clusters typically have many users with varying software requirements and installing software for each
user can be time-consuming and may lead to conflicts between different versions of the same software.

``Modules`` provide a way to manage software installations and make different versions of the same 
software available to users on demand. With modules, users can load and unload different versions of 
software into their environment without interfering with other users or the system's default settings. 
This makes it easy for users to work with different versions of the same software or to use different 
software packages for different projects or workflows.

.. note::

   Please note that the easiest way to use modules is by activating the gridware user HPC 
   environment (``flight env activate gridware``).
   
   Some of the most useful commands for interacting with modules include:
   
* ``module avail``: This command lists all the available modules on the system, showing the name, version, and any dependencies.
* ``module load``: This command loads a specific module into the user's environment, making its executable and library files available for use.
* ``module unload``: This command unloads a previously loaded module, removing its executable and library files from the user's environment.
* ``module list``: This command lists all the currently loaded modules, showing their name and version.
* ``module show``: This command displays detailed information about a specific module, including its version, dependencies, and any available module options.

Installing new software
-----------------------

In general, installing software on DMOG may require root access, as it often involves making changes to the 
system's configuration and installing packages in system directories that are only accessible to the root user.

However, there are alternative ways to install and manage software that do not require root access. 
For example, users may be able to install software in their home directories or in a designated software 
directory that's writable by users. 

If you're not sure whether you need root access to install software on your cluster, it's a good idea 
to contact the cluster's system administrators for guidance.

Requesting new software
-----------------------

If you require software that is not currently available on the cluster and could benefit the broader user 
community, please contact the cluster support team at ISHelp@hw.ac.uk. They can assist you in installing the 
software or evaluating its suitability for the cluster. This will also help other users who may require the 
same software. Please note that the support team will evaluate the software for security and compatibility 
issues before installing it on the cluster.
