hwQuota
=======

The hwQuota utility will display your current storage space utilization across a number of directories.

An example output would be:

.. code-block:: bash

    /export/users/gp27 | 38.91GiB | 25.94% of your quota
    /mnt/scratch/gp27 | 0GiB | 0.00% of used space
    /mnt/data/shared/gp27 | 7.93GiB | 0.03% of used space

The top line will show you how much space the files in your home directory (exluding the other folders shown), and the percentage of your quota you have used.

The next lines will show you how much space the files in the listed directories take up. Because there is no quota for these folders, it shows you a percantage of all used space in that location you are using (your share of the space used).
