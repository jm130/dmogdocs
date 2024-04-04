OpenMolcas
===========

OpenMolcas is a state-of-the-art quantum chemistry software package developed by scientists for scientists. It offers a comprehensive suite of programs for applying various electronic structure methods to chemical systems. One of its standout features is the multiconfigurational approach, incorporating advanced methods like CASSCF (Complete Active Space Self-Consistent Field) and CASPT2 (Complete Active Space Perturbation Theory). Unlike being a fork or reimplementation, OpenMolcas is a substantial part of the Molcas codebase released as free and open-source software (FOSS) under the Lesser General Public License (LGPL). However, some portions of Molcas remain under a different license due to the decisions of their original authors or accessibility issues.

We have installed two versions of OpenMolcas on our HPC cluster: version 23.10 and version 24.02. Users can access these versions by enabling the gridware flight environment and loading the respective modules. Each version of OpenMolcas includes both serial and parallel executable files, facilitating efficient calculations on both single-core and multi-core processor systems.

For further reading and to understand the capabilities and advancements of OpenMolcas, we recommend the following references:

* "OpenMolcas: From Source Code to Insight." J. Chem. Theory Comput. 15 (2019) 5925-5964. doi:10.1021/acs.jctc.9b00532
* "Modern quantum chemistry with [Open]Molcas." J. Chem. Phys. 152 (2020) 214117. doi:10.1063/5.0004835
* "The OpenMolcas Web: A Community-Driven Approach to Advancing Computational Chemistry." J. Chem. Theory Comput. 19 (2023) 6933-6991. doi:10.1021/acs.jctc.3c00182

.. note::

   We are aware of an issue with the parallel build of OpenMolcas version 23.10, whereby some jobs may hang. If you encounter this issue, we recommend using OpenMolcas version 24.02 as an alternative.


Running OpenMolcas jobs
-----------------------

An example job script for OpenMolcas would be:

.. code-block:: bash

   #!/bin/bash

   #SBATCH --job-name=molcas-test
   #SBATCH --nodes=1
   #SBATCH --tasks-per-node=4
   #SBATCH --time=100:00:00
   #SBATCH --partition=nodes
   #SBATCH --mem=50000MB
   #SBATCH --output=molcas.%j.o
   #SBATCH --error=molcas.%j.e

   flight env activate gridware
   module load apps/openmolcas_mpi/24.02
   export MOLCAS_NPROCS=$SLURM_TASKS_PER_NODE

   pymolcas -np  molcas.input > MOLCAS.out

Where ``molcas.input`` is:

.. code-block:: bash

   &GATEWAY
   COORD 
   5

   N        0.000000000     15.566997820      0.000000000
   O        0.000000000     14.503597820      0.000000000
   C        0.000000000      0.000000000      0.000000000
   O        0.000000000     -1.160000000      0.000000000
   O        0.000000000      1.160000000      0.000000000
   GROUP = nosym
   TITLE = Molcas-Test
   BASIS = STO-3G
   
   &SEWARD
   
   &RASSCF
   SPIN= 2
   RAS2= 10
   NACTEL = 13
   INACTIVE  = 12
   CIROOT = 20 20 1

To submit a job using the provided Slurm script, you can use the following command:

.. code-block:: bash

   sbatch submit_molcas.sh





