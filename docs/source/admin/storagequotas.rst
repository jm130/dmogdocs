Storage Quotas
==============

There are two separate quotas relating to data storage on DMOG:

#. A quota of 150GB of data capacity
#. A quota of 250k total files

If you exceed either of these quotas you will no longer be able to create new files on DMOG until you remove files and no longer exceed either quota.

You can check your current quota usage with the following command:

``quota -s``

This will display an output similar to the following:

.. code-block:: bash

  [gp27@login1 [dmog] ~]$ quota -s
  Disk quotas for user gp27 (uid 433400227):
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
  storage:/export/users
                 22111M    150G    200G           10299    250k    300k


Should you exceed either of these quotas an asterisk (*) will apear next to the value in the Files column.

Conda
-----

Using Conda frequently causes the total number of files quota to be exceeded.

Our recommended workaround for this is to move your .local folder (where Conda stores your enviroments) to the archive folder and create a symbolic link to the new location.

You can do this by using the following commands:

``mv $HOME/.local $HOME/archive/``

``ln -s $HOME/archive/.local $HOME/.local``

You can confirm that this has worked by using the ``ls -la`` command. You should see an output similar to ths:

.. code-block:: bash

  [gp27@login1 [dmog] ~]$ ls -la
  total 212
  drwx------  32 gp27 clusterusers  4096 May  1 08:46 .
  drwxr-xr-x 214 root root          4096 Apr 30 12:54 ..
  drwx------   2 gp27 clusterusers  4096 Feb 13 12:25 .apptainer
  lrwxrwxrwx   1 gp27 clusterusers    22 Dec  5 09:59 archive -> /mnt/data/shared/gp27/
  -rw-------   1 gp27 clusterusers 22927 May  1 08:52 .bash_history
  -rw-------   1 gp27 clusterusers    18 Dec  5 09:59 .bash_logout
  -rw-------   1 gp27 clusterusers   193 Dec  5 09:59 .bash_profile
  -rw-------   1 gp27 clusterusers   231 Dec  5 09:59 .bashrc
  drwxr-xr-x  16 gp27 clusterusers  4096 Apr 25 10:21 .cache
  drwxr-xr-x   2 gp27 clusterusers  4096 Apr  3 08:48 .conda
  drwxr-xr-x  11 gp27 clusterusers  4096 Mar  7 16:17 .config
  drwx------   3 gp27 clusterusers  4096 Jan  9 13:18 .dbus
  drwxr-xr-x   2 gp27 clusterusers  4096 Jan  9 13:19 Desktop
  drwxr-xr-x   3 gp27 clusterusers  4096 Feb  9 10:42 Documents
  drwxr-xr-x   2 gp27 clusterusers  4096 Jan  9 13:19 Downloads
  -rw-------   1 gp27 clusterusers   334 Dec  5 09:59 .emacs
  lrwxrwxrwx   1 gp27 clusterusers    15 Apr 16 15:23 .local -> archive/.local/
  ...

This line ``lrwxrwxrwx   1 gp27 clusterusers    15 Apr 16 15:23 .local -> archive/.local/`` shows that my .local folder is actually located in archive/.local
