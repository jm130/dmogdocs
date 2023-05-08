Data Management
===============

There are several data storage types available to users. Each of which has 
different characteristics and policies, and it is suitable for different types of use. 
Please note that the cluster is intended to store data for as long as it is being 
processed and so none of the storage options are backed up.

The following table shows the different storage options that are currently available to users:

.. list-table:: 
   :widths: 15 15 20 20 30
   :header-rows: 1

   * - Storage
     - Use
     - Exported to nodes
     - Total Capacity
     - Notes
   * - ``/users/``
     - Home dir
     - Yes
     - 12TB 
     - Quota: 150GB, No backup
   * - ``/mnt/data/``
     - Local data
     - Yes
     - 30TB
     - No backup
   * - ``/mnt/scratch/``
     - Compute
     - Yes
     - 93TB
     - No backup 
   * - ``/tmp/users/``
     - Compute
     - No
     - up to 1TB
     - No backup

File Transfer
=============
 
The easiest way to transfer data from/to the cluster is to use one of the standard 
programs based on the SSH protocol such us ``scp`` or ``rsync``.

The scp command
----------------

The ``scp`` command creates a copy of a file, or a directory (if the -r flag is called) on a remote machine.

To copy data to the cluster:

.. code-block:: bash

   scp [options] /source/path/to/object <user>@domg.hw.ac.uk:/path/to/destination

To copy data from the cluster:

.. code-block:: bash

   scp [options] <user>@domg.hw.ac.uk:/source/path/to/object /path/to/destination
   
For a complete list of options available: ``man scp``

The rsync command
-----------------

``rsync`` uses the same underlying protocol as ``scp``, but it employs a special 
delta transfer algorithm. It compares if there is any differences in the files 
and only transfer those differences. Also, while copying if the connection drops, 
it can pick up the transfer where it was left off.

The syntax to copy files to/from the cluster:

.. code-block:: 

   rsync [options] /source/path/to/object <user>@domg.hw.ac.uk:/path/to/destination
   rsync [options] <user>@domg.hw.ac.uk: /source/path/to/object /path/to/destination

For a list of options: ``man rsync``


   
