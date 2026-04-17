# Slurm Workload Manager

Slurm is an open-source workload manager designed for Linux clusters of all sizes. It provides three key functions. First it allocates exclusive and/or non-exclusive access to resources (computer nodes) to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (typically a parallel job) on a set of allocated nodes. Finally, it arbitrates contention for resources by managing a queue of pending work.

Slurm\'s design is very modular with dozens of optional plugins. In its simplest configuration, it can be installed and configured in a couple of minutes (see http://www.linux-mag.com/id/7239/1/ by Jeffrey B. Layton). More complex configurations can satisfy the job scheduling needs of world-class computer centers and rely upon a http://www.mysql.com/ database for archiving [accounting](accounting.md) records, managing [resource limits](resource_limits.md) by user or account, or supporting sophisticated [job prioritization](priority_multifactor.md) algorithms.

While other workload managers do exist, Slurm is unique in several respects:

- **Scalability**: It is designed to operate in a heterogeneous cluster with up to tens of millions of processors.
- **Performance**: It can accept 1,000 job submissions per second and fully execute 500 simple jobs per second (depending upon hardware and system configuration).
- **Free and Open Source**: Its source code is freely available under the http://www.gnu.org/licenses/gpl.html.
- **Portability**: Written in C with a GNU autoconf configuration engine. While initially written for Linux, Slurm has been ported to a diverse assortment of systems.
- **Power Management**: Job can specify their desired CPU frequency and power use by job is recorded. Idle resources can be powered down until needed.
- **Fault Tolerant**: It is highly tolerant of system failures, including failure of the node executing its control functions.
- **Flexibility**: A plugin mechanism exists to support various interconnects, authentication mechanisms, schedulers, etc. These plugins are documented and simple enough for the motivated end user to understand the source and add functionality.
- **Resizable Jobs**: Jobs can grow and shrink on demand. Job submissions can specify size and time limit ranges.
- **Status Jobs**: Status running jobs at the level of individual tasks to help identify load imbalances and other anomalies.

Slurm provides workload management on many of the most powerful computers in the world. On the November 2013 http://www.top500.org/ list, five of the ten top systems use Slurm including the number one system. These five systems alone contain over 5.7 million cores. A few of the systems using Slurm are listed below:

- http://www.top500.org/blog/lists/2013/06/press-release/ designed by http://english.nudt.edu.cn/ in China has 16,000 nodes, each with two Intel Xeon IvyBridge processors and three Xeon Phi processors for a total of 3.1 million cores and a peak performance of 33.86 Petaflops.
- https://asc.llnl.gov/computing_resources/sequoia/, an http://www.ibm.com/ BlueGene/Q system at https://www.llnl.gov/ with 1.6 petabytes of memory, 96 racks, 98,304 compute nodes, and 1.6 million cores, with a peak performance of over 17.17 Petaflops.
- http://www.cscs.ch/computers/piz_daint/index.html a http://www.cray.com/ XC30 system at the http://www.cscs.ch/ with 28 racks and 5,272 hybrid compute nodes each with an http://www.intel.com/ Xeon E5-2670 CPUs plus an http://www.nvidia.com/ Tesla K20X GPUs for a total of 115,984 compute cores and a peak performance of 6.27 Petaflops.
- http://www.tacc.utexas.edu/stampede at the http://www.tacc.utexas.edu/ is a http://www.dell.com/ with over 80,000 http://www.intel.com/ Xeon cores, Intel Phi co-processors, plus 128 http://www.nvidia.com/ GPUs delivering 5.17 Petaflops.
- http://www-hpc.cea.fr/en/complexe/tgcc-curie.htm, owned by http://www.genci.fr/ and operated in the TGCC by http://www.cea.fr/, Curie is offering 3 different fractions of x86-64 computing resources for addressing a wide range of scientific challenges and offering an aggregate peak performance of 2 PetaFlops.
- http://www.wcm.bull.com/internet/pr/rend.jsp?DocId=567851&lang=en at http://www.cea.fr/ with 140,000 Intel Xeon 7500 processing cores, 300TB of central memory and a theoretical computing power of 1.25 Petaflops.
- http://hpc.msu.ru/?q=node/59, a http://www.t-platforms.com/ system at http://hpc.msu.ru/ with 52,168 Intel Xeon processing cores and 8,840 NVIDIA GPUs.
- http://compeng.uni-frankfurt.de/index.php?id=86, a combined CPU-GPU Linux cluster at http://csc.uni-frankfurt.de/ of the Goethe University Frankfurt, Germany, with 20,928 AMD Magny-Cours CPU cores (176 Teraflops peak performance) plus 778 ATI Radeon 5870 GPUs (2.1 Petaflops peak performance single precision and 599 Teraflops double precision) and QDR Infiniband interconnect.
