Hardware
========

The DMOG HPC cluster consists of 25 compute nodes connected by a high-speed Ethernet network. 
Of these, 10 nodes are equipped with GPU cards, while the remaining nodes are CPU-only. 
A Lustre parallel filesystem serves shared scratch space across the cluster, maximizing 
the performance of the underlying hardware. 
Home directories are shared via NFS.

CPU compute nodes
-----------------
There are two types of standard compute nodes available on the DMOG HPC cluster:

Large Memory Nodes
~~~~~~~~~~~~~~~~~~

There are ten large memory nodes.
Each large memory node contains two 2.6 GHz, 32-core AMD EPYC 7513 processors and 
512GB of RAM. Hyperthreading is disabled by default, but the processors support it 
if needed. A local SSD disk of 1TB is available on the nodes. There are a total of 
ten compute nodes of this type.
These nodes are well-suited for memory-intensive workloads.

Medium Core Count Nodes
~~~~~~~~~~~~~~~~~~~~~~

There are five medium core count nodes. 
Each node is equipped with two 2.3GHz, 48-core AMD EPYC 7643 processors and 256GB of RAM. 
Hyperthreading is disabled on these nodes. A local SSD disk is available for high throughput. 
These nodes are well-suited for CPU-intensive workloads.

High Core Count Nodes
~~~~~~~~~~~~~~~~~~~~~~

There are six high core count nodes available. 
Each node is equipped with two 2.45GHz, 64-core AMD EPYC 7763 processors and 1024GB of RAM. 
Hyperthreading is disabled on these nodes. A local SSD disk is available for high throughput. 
These nodes are well-suited for highly parellelised, CPU-intensive workloads.

GPU compute nodes
-----------------

The DMOG HPC cluster includes 22 compute nodes equipped with GPU cards. 
Each node is equipped with 2 Nvidia A40 (48GB) cards, 2 32-core AMD EPYC 7543 32-Core Processor, 
and 256GB of RAM. These nodes are well-suited for workloads that require significant GPU 
computing resources, such as deep learning, or artificial intelligence.

Storage
-------

The DMOG HPC cluster provides a Lustre parallel file system that serves 
the shared scratch directory. This file system has a total capacity of 93TB 
and is the primary storage location for processing data. In addition to the 
Lustre file system, there are also several other volumes available on the 
cluster that are presented as NFS exports. These volumes are intended for 
specific use cases, such as software installations or backups, and are not part 
of the Lustre file system:

* ``/mnt/data/``: 30TB
* ``/users/``: 12TB of shared space for home directories
* ``/mnt/scratch/``: 93TB of high read/write bandwidth for parallel calculations
* ``/tmp/``: 1TB SSD locally attached to the node

Networking
----------

The nodes on the cluster are connected through high-speed Ethernet switches, 
enabling fast and efficient communication between nodes.
