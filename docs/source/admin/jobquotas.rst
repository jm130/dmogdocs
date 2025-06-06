Job Quotas
==========

To ensure fair share of resources among the HPC user community, we have implemented 
job quotas. These quotas are subject to review and may be adjusted as required. 
The current job quotas for standard users are as follows:

#. maximum of 10 jobs running per user 
#. maximum of 60 jobs submitted per user (allowing up to 50 jobs to be held in a queued/pending state)
#. Maximum of 128 CPU cores 
#. Maximum of 1006G RAM 
#. Maximum of 2 GPUs per user (minimum of 1 GPU per job)
#. Maximum runtime 7 days

These quotas are designed to ensure that all users have a fair opportunity to access 
the cluster resources. Users who require additional resources are encouraged to contact 
the HPC team to discuss their requirements.

There are also groups which have different quotas. Membership of these groups is based on various factors, including early testers, financial contribution to DMOG, etc.

Currently there are no differences in job priority between groups.

Details of these groups are:

.. list-table::
   :widths: 25 25 25 25 25 25
   :header-rows: 1

   * - Group Name
     - CPUs
     - GPUs
     - Mem
     - Active Jobs
     - Total Jobs
   * - COMSEL
     - 768*
     - 20*
     - 2.51TB*
     - 20
     - 65
   * - highlimits
     - 384 
     - 6
     - 3TB
     - 15
     - 65
   * - prilimits
     - 256
     - 4
     - 2TB
     - 15
     - 65

(*): resource is shared between members of the group
