Julia
======

``Julia`` is a high-level, high-performance programming language designed for numerical and scientific computing. 
It combines the ease of use and expressive power of high-level languages like Python with the performance of 
low-level languages like C.

To utilize Julia on the DMOG HPC cluster, follow the instructions below:

.. code-block:: bash

   flight env activate gridware
   module load apps/julia
   
Note that ``Julia`` runs alongside Python. Therefore, any additional dependencies required 
for your ``Julia`` programs need to be installed in your user workspace using ``Conda`` or ``Anaconda``
(see :ref:`Python <apps-python>` for further details). Make sure you have 
the necessary packages installed to fulfill your requirements.

By default, ``Julia`` packages are stored in the .julia directory located within your home directory. 
If you want to use a different path to store local packages, you can modify the ``JULIA_DEPOT_PATH`` environment variable:

.. code-block:: bash

   export JULIA_DEPOT_PATH=/path/to/myjulia
   
This would only work in the current active session. To make it permanent, add that line in your ``.bashrc`` file.
