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
