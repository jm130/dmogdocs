Python
======

In shared facilities, ``Python`` is commonly managed using tools like ``Conda`` and ``Anaconda`` to ensure efficient and reliable environment management. 
On DMOG, the flight environment ``Conda`` and the ``Anaconda`` modules, offer a comprehensive solution for creating isolated and reproducible 
``Python`` environments. These environments allow multiple users to work on the same system without conflicts, as each user can have their own 
customized ``Python`` environment with specific package versions and dependencies. 

This approach ensures that Python-based projects on DMOG can be executed reliably and with minimal compatibility issues, enabling collaborative research 
and streamlined workflows.

Conda
-----

``Conda`` is an open-source package management system and environment management system. It allows you to create and manage isolated environments for 
different projects, ensuring that each project has its own set of dependencies and packages. ``Conda`` simplifies package installation, 
updating, and removal, making it easier to maintain a consistent and reproducible development environment.

To use conda you need to activate the relevant flight environment:

.. code-block:: bash
   
   flight env activate conda@<name>
   
The above command will fail if you haven't created ``Conda`` environment yet. To do so, just use the 
``flight env create`` command as follows:

.. code-block:: bash

   flight env create conda[@name]

``Conda`` itself supports multiple user environments. The default environment is called ``base``. 
You can use it to build your own custom workspace. The ``conda`` command enables you to list the
currently installed packages, and also search and install new ones.

.. code-block:: bash

   conda list
   conda search <packagename>
   conda install <packagename>

Alternatively, you can create new environment to suit your needs. For example to create a  
new environment called "myenv" with a specific version of ``Python``:

.. code-block:: bash

   conda create --name myenv python=3.9
   
To navigate across the different ``Conda`` environment you can use:

.. code-block:: bash

   conda info --env
   conda activate <name>
   conda deactivate
   
If you prefer to search and install packages using ``pip``, you can also use

.. code-block:: bash

   pip list
   pip search <packagename>
   pip install <packagename>

Anaconda
---------

``Anaconda`` is a widely-used distribution of ``Python`` that comes bundled with a comprehensive collection of
packages and tools for scientific computing and data analysis. On DMOG, ``Anaconda`` is available through 
the ``flight env gridware modules``, which offer two separate modules—one for ``Python 2`` and the other for
``Python 3``. These modules provide users with a convenient way to access and utilize ``Anaconda`` for their
research and data analysis tasks. 

To use anaconda:

.. code-block:: bash
   
   flight env activate gridware
   module load app/<anaconda/anaconda3>
   
Once the module is loaded, the same commands as for ``Conda`` apply to ``Anaconda``. 
See :ref:`the Conda section<Conda>` for further details.
