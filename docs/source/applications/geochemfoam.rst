GeoChemFoam
===========

GeoChemFoam can be enabled for use within your submission script (or interactively) with the following commands:

.. code-block:: bash
    
    flight env activate gridware
    module load apps/openfoamplus
    module load apps/anaconda3
    conda activate gcfoam
    source /opt/gridware/depots/761a7df9/el9/share/openfoamplus/22.06/applications/utilities/GeoChemFoam-5.1/etc/bashrc

The above assumes you have created a GeoChemFoam conda environment as outlined in the GeoChemFoam Github repo `HERE <https://github.com/GeoChemFoam/GeoChemFoam/wiki/GeoChemFoam-Native-version:-Install-GeoChemFoam-from-source-code#python-for-tutorial-scripts>`_
