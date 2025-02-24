hwPending
=========

hwPending will display all of your currently pending jobs, including the reason for the job being in the pending state.

An example output:

.. code-block:: bash

    [gp27@login1 [dmog] scripts]$ hwPending
    JOBID   USER    PARTITSUBMIT_TIME         START_TIME          REASON                   SCHEDNODESQOS         TRES_ALLOC                                   PRIORITYTIME_LIMIT          
    189262  gp27    gpu   2025-02-20T17:38:04 N/A                 Dependency               (null)    highlimits  cpu=2,mem=450G,node=1,billing=2,gres/gpu=1   1071    6-00:00:00          
    189260  gp27    gpu   2025-02-20T17:38:04 N/A                 Dependency               (null)    highlimits  cpu=2,mem=450G,node=1,billing=2,gres/gpu=1   1071    6-00:00:00          
    189258  gp27    gpu   2025-02-20T17:38:04 N/A                 Dependency               (null)    highlimits  cpu=2,mem=450G,node=1,billing=2,gres/gpu=1   1071    6-00:00:00          
    189256  gp27    gpu   2025-02-20T17:38:04 N/A                 Dependency               (null)    highlimits  cpu=2,mem=450G,node=1,billing=2,gres/gpu=1   1071    6-00:00:00          
    189254  gp27    gpu   2025-02-20T17:38:04 N/A                 Dependency               (null)    highlimits  cpu=2,mem=450G,node=1,billing=2,gres/gpu=1   1071    6-00:00:00           


For collaborative purposes, it's possible to check the pending state of another user's jobs by entering their username when running the command:

.. code-block:: bash

    [gp27@login1 [dmog] scripts]$ hwPending jm130
    JOBID   USER     PARTITSUBMIT_TIME         START_TIME          REASON                   SCHEDNODESQOS         TRES_ALLOC                                   PRIORITYTIME_LIMIT
    181992  jm130    nodes 2025-02-06T11:57:44 N/A                 QOSMaxCpuPerUserLimit    (null)    userlimits  cpu=48,mem=16G,node=1,billing=48             2030    3-00:00:00          
    181991  jm130    nodes 2025-02-06T11:57:03 N/A                 QOSMaxCpuPerUserLimit    (null)    userlimits  cpu=48,mem=16G,node=1,billing=48             2030    3-00:00:00          
    181990  jm130    nodes 2025-02-06T11:56:32 N/A                 QOSMaxCpuPerUserLimit    (null)    userlimits  cpu=48,mem=16G,node=1,billing=48             2030    3-00:00:00          
    181989  jm130    nodes 2025-02-06T11:55:49 N/A                 QOSMaxCpuPerUserLimit    (null)    userlimits  cpu=48,mem=16G,node=1,billing=48             2030    3-00:00:00          
    181988  jm130    nodes 2025-02-06T11:55:16 N/A                 QOSMaxCpuPerUserLimit    (null)    userlimits  cpu=48,mem=16G,node=1,billing=48             2030    3-00:00:00          
