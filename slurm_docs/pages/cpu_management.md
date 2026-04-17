# CPU Management User and Administrator Guide

## Overview {#Overview}

The purpose of this guide is to assist Slurm users and administrators in selecting configuration options and composing command lines to manage the use of CPU resources by jobs, steps and tasks. The document is divided into the following sections:

- Overview
- CPU Management Steps performed by Slurm
- Getting Information about CPU usage by Jobs/Steps/Tasks
- CPU Management and Slurm Accounting
- CPU Management Examples

CPU Management through user commands is constrained by the configuration parameters chosen by the Slurm administrator. The interactions between different CPU management options are complex and often difficult to predict. Some experimentation may be required to discover the exact combination of options needed to produce a desired outcome. Users and administrators should refer to the man pages for [slurm.conf](slurm.conf.md), [cgroup.conf](cgroup.conf.md), [salloc](salloc.md), [sbatch](sbatch.md) and [srun](srun.md) for detailed explanations of each option. The following html documents may also be useful:

[Consumable Resources in Slurm](cons_tres.md)\
[Sharing Consumable Resources](cons_tres_share.md)\
[Support for Multi-core/Multi-thread Architectures](mc_support.md)\
[Plane distribution](dist_plane.md)

## CPU Management Steps performed by Slurm {#Section1}

Slurm uses four basic steps to manage CPU resources for a job/step:

- Step 1: Selection of Nodes
- Step 2: Allocation of CPUs from the selected Nodes
- Step 3: Distribution of Tasks to the selected Nodes
- Step 4: Optional Distribution and Binding of Tasks to CPUs within a Node

### Step 1: Selection of Nodes {#Step1}

In Step 1, Slurm selects the set of nodes from which CPU resources are to be allocated to a job or job step. Node selection is therefore influenced by many of the configuration and command line options that control the allocation of CPUs (Step 2 below). If SelectType=select/linear is configured, all resources on the selected nodes will be allocated to the job/step. If SelectType is configured to be select/cons_tres, individual sockets, cores and threads may be allocated from the selected nodes as [consumable resources](cons_tres.md). The consumable resource type is defined by SelectTypeParameters.\
\
Step 1 is performed by slurmctld and the select plugin.\

+----------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **slurm.conf parameter**                                       | **Possible values**                                                                    | **Description**                                                                                                                                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| [NodeName](slurm.conf.md#OPT_NodeName)                         | \<name of the node\>\                                                                  | Defines a node. This includes the number and layout of boards, sockets, cores, threads and processors (logical CPUs) on the node.                  |
|                                                                | \                                                                                      |                                                                                                                                                    |
|                                                                | Plus additional parameters. See man page for details.                                  |                                                                                                                                                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| [PartitionName](slurm.conf.md#OPT_PartitionName)               | \<name of the partition\>\                                                             | Defines a partition. Several parameters of the partition definition affect the selection of nodes (e.g., Nodes, OverSubscribe, MaxNodes)           |
|                                                                | \                                                                                      |                                                                                                                                                    |
|                                                                | Plus additional parameters. See man page for details.                                  |                                                                                                                                                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| [SlurmdParameters](slurm.conf.md#OPT_SlurmdParameters)         | config_overrides                                                                       | Controls how the information in a node definition is used.                                                                                         |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| [SelectType](slurm.conf.md#OPT_SelectType)                     | select/linear \| select/cons_tres                                                      | Controls whether CPU resources are allocated to jobs and job steps in units of whole nodes or as consumable resources (sockets, cores or threads). |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| [SelectTypeParameters](slurm.conf.md#OPT_SelectTypeParameters) | CR_CPU \| CR_CPU_Memory \| CR_Core \| CR_Core_Memory \| CR_Socket \| CR_Socket_Memory\ | Defines the consumable resource type and controls other aspects of CPU resource allocation by the select plugin.                                   |
|                                                                | \                                                                                      |                                                                                                                                                    |
|                                                                | Plus additional options. See man page for details.                                     |                                                                                                                                                    |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

: **slurm.conf options that control Step 1**

\

+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| **Command line option**                               | **Possible values**                                | **Description**                                                                              |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-B, \--extra-node-info](srun.md#OPT_extra-node-info) | \<sockets\[:cores\[:threads\]\]\>                  | Restricts node selection to nodes with a specified layout of sockets, cores and threads.     |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-C, \--constraint](srun.md#OPT_constraint)           | \<list\>                                           | Restricts node selection to nodes with specified attributes                                  |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--contiguous](srun.md#OPT_contiguous)               | N/A                                                | Restricts node selection to contiguous nodes                                                 |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--cores-per-socket](srun.md#OPT_cores-per-socket)   | \<cores\>                                          | Restricts node selection to nodes with at least the specified number of cores per socket     |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-c, \--cpus-per-task](srun.md#OPT_cpus-per-task)     | \<ncpus\>                                          | Controls the number of CPUs allocated per task                                               |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--exclusive](srun.md#OPT_exclusive)                 | N/A                                                | Prevents sharing of allocated nodes with other jobs. Suballocates CPUs to job steps.         |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-F, \--nodefile](salloc.md#OPT_nodefile)             | \<node file\>                                      | File containing a list of specific nodes to be selected for the job (salloc and sbatch only) |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--hint](srun.md#OPT_hint)                           | compute_bound \| memory_bound \| \[no\]multithread | Additional controls on allocation of CPU resources                                           |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--mincpus](srun.md#OPT_mincpus)                     | \<n\>                                              | Controls the minimum number of CPUs allocated per node                                       |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-N, \--nodes](srun.md#OPT_nodes)                     | \<minnodes\[-maxnodes\]\>                          | Controls the minimum/maximum number of nodes allocated to the job                            |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-n, \--ntasks](srun.md#OPT_ntasks)                   | \<number\>                                         | Controls the number of tasks to be created for the job                                       |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--ntasks-per-core](srun.md#OPT_ntasks-per-core)     | \<number\>                                         | Controls the maximum number of tasks per allocated core                                      |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--ntasks-per-socket](srun.md#OPT_ntasks-per-socket) | \<number\>                                         | Controls the maximum number of tasks per allocated socket                                    |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--ntasks-per-node](srun.md#OPT_ntasks-per-node)     | \<number\>                                         | Controls the maximum number of tasks per allocated node                                      |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-O, \--overcommit](srun.md#OPT_overcommit)           | N/A                                                | Allows fewer CPUs to be allocated than the number of tasks                                   |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-p, \--partition](srun.md#OPT_partition)             | \<partition_names\>                                | Controls which partition is used for the job                                                 |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-s, \--oversubscribe](srun.md#OPT_share)             | N/A                                                | Allows sharing of allocated nodes with other jobs                                            |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--sockets-per-node](srun.md#OPT_sockets-per-node)   | \<sockets\>                                        | Restricts node selection to nodes with at least the specified number of sockets              |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [\--threads-per-core](srun.md#OPT_threads-per-core)   | \<threads\>                                        | Restricts node selection to nodes with at least the specified number of threads per core     |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-w, \--nodelist](srun.md#OPT_nodelist)               | \<host1,host2,\... or filename\>                   | List of specific nodes to be allocated to the job                                            |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-x, \--exclude](srun.md#OPT_exclude)                 | \<host1,host2,\... or filename\>                   | List of specific nodes to be excluded from allocation to the job                             |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+
| [-Z, \--no-allocate](srun.md#OPT_no-allocate)         | N/A                                                | Bypass normal allocation (privileged option available to users "SlurmUser" and "root" only)  |
+-------------------------------------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------------+

: **srun/salloc/sbatch command line options that control Step 1**

\

### Step 2: Allocation of CPUs from the selected Nodes {#Step2}

In Step 2, Slurm allocates CPU resources to a job/step from the set of nodes selected in Step 1. CPU allocation is therefore influenced by the configuration and command line options that relate to node selection. If SelectType=select/linear is configured, all resources on the selected nodes will be allocated to the job/step. If SelectType is configured to be select/cons_tres, individual sockets, cores and threads may be allocated from the selected nodes as [consumable resources](cons_tres.md). The consumable resource type is defined by SelectTypeParameters.\

When using a SelectType of select/cons_tres, the default allocation method across nodes is block allocation (allocate all available CPUs in a node before using another node). The default allocation method within a node is cyclic allocation (allocate available CPUs in a round-robin fashion across the sockets within a node). Users may override the default behavior using the appropriate command line options described below. The choice of allocation methods may influence which specific CPUs are allocated to the job/step.\
\
Step 2 is performed by slurmctld and the select plugin.\

+----------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **slurm.conf parameter**                                       | **Possible values**                                                                    | **Description**                                                                                                                                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [NodeName](slurm.conf.md#OPT_NodeName)                         | \<name of the node\>\                                                                  | Defines a node. This includes the number and layout of boards, sockets, cores, threads and processors (logical CPUs) on the node.                         |
|                                                                | \                                                                                      |                                                                                                                                                           |
|                                                                | Plus additional parameters. See man page for details.                                  |                                                                                                                                                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [PartitionName](slurm.conf.md#OPT_PartitionName)               | \<name of the partition\>\                                                             | Defines a partition. Several parameters of the partition definition affect the allocation of CPU resources to jobs (e.g., Nodes, OverSubscribe, MaxNodes) |
|                                                                | \                                                                                      |                                                                                                                                                           |
|                                                                | Plus additional parameters. See man page for details.                                  |                                                                                                                                                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SlurmdParameters](slurm.conf.md#OPT_SlurmdParameters)         | config_overrides                                                                       | Controls how the information in a node definition is used.                                                                                                |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SelectType](slurm.conf.md#OPT_SelectType)                     | select/linear \| select/cons_tres                                                      | Controls whether CPU resources are allocated to jobs and job steps in units of whole nodes or as consumable resources (sockets, cores or threads).        |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SelectTypeParameters](slurm.conf.md#OPT_SelectTypeParameters) | CR_CPU \| CR_CPU_Memory \| CR_Core \| CR_Core_Memory \| CR_Socket \| CR_Socket_Memory\ | Defines the consumable resource type and controls other aspects of CPU resource allocation by the select plugin.                                          |
|                                                                | \                                                                                      |                                                                                                                                                           |
|                                                                | Plus additional options. See man page for details.                                     |                                                                                                                                                           |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

: **slurm.conf options that control Step 2**

\

+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Command line option**                               | **Possible values**                                | **Description**                                                                                                        |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-B, \--extra-node-info](srun.md#OPT_extra-node-info) | \<sockets\[:cores\[:threads\]\]\>                  | Restricts node selection to nodes with a specified layout of sockets, cores and threads.                               |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-C, \--constraint](srun.md#OPT_constraint)           | \<list\>                                           | Restricts node selection to nodes with specified attributes                                                            |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--contiguous](srun.md#OPT_contiguous)               | N/A                                                | Restricts node selection to contiguous nodes                                                                           |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--cores-per-socket](srun.md#OPT_cores-per-socket)   | \<cores\>                                          | Restricts node selection to nodes with at least the specified number of cores per socket                               |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-c, \--cpus-per-task](srun.md#OPT_cpus-per-task)     | \<ncpus\>                                          | Controls the number of CPUs allocated per task                                                                         |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--distribution, -m](srun.md#OPT_distribution)       | block\|cyclic\                                     | The second specified distribution (after the \":\") can be used to override the default allocation method within nodes |
|                                                       | \|arbitrary\|plane=\<options\>\[:block\|cyclic\]   |                                                                                                                        |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--exclusive](srun.md#OPT_exclusive)                 | N/A                                                | Prevents sharing of allocated nodes with other jobs                                                                    |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-F, \--nodefile](salloc.md#OPT_nodefile)             | \<node file\>                                      | File containing a list of specific nodes to be selected for the job (salloc and sbatch only)                           |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--hint](srun.md#OPT_hint)                           | compute_bound \| memory_bound \| \[no\]multithread | Additional controls on allocation of CPU resources                                                                     |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--mincpus](srun.md#OPT_mincpus)                     | \<n\>                                              | Controls the minimum number of CPUs allocated per node                                                                 |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-N, \--nodes](srun.md#OPT_nodes)                     | \<minnodes\[-maxnodes\]\>                          | Controls the minimum/maximum number of nodes allocated to the job                                                      |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-n, \--ntasks](srun.md#OPT_ntasks)                   | \<number\>                                         | Controls the number of tasks to be created for the job                                                                 |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--ntasks-per-core](srun.md#OPT_ntasks-per-core)     | \<number\>                                         | Controls the maximum number of tasks per allocated core                                                                |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--ntasks-per-socket](srun.md#OPT_ntasks-per-socket) | \<number\>                                         | Controls the maximum number of tasks per allocated socket                                                              |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--ntasks-per-node](srun.md#OPT_ntasks-per-node)     | \<number\>                                         | Controls the maximum number of tasks per allocated node                                                                |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-O, \--overcommit](srun.md#OPT_overcommit)           | N/A                                                | Allows fewer CPUs to be allocated than the number of tasks                                                             |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-p, \--partition](srun.md#OPT_partition)             | \<partition_names\>                                | Controls which partition is used for the job                                                                           |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-s, \--oversubscribe](srun.md#OPT_share)             | N/A                                                | Allows sharing of allocated nodes with other jobs                                                                      |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--sockets-per-node](srun.md#OPT_sockets-per-node)   | \<sockets\>                                        | Restricts node selection to nodes with at least the specified number of sockets                                        |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [\--threads-per-core](srun.md#OPT_threads-per-core)   | \<threads\>                                        | Restricts node selection to nodes with at least the specified number of threads per core                               |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-w, \--nodelist](srun.md#OPT_nodelist)               | \<host1,host2,\... or filename\>                   | List of specific nodes to be allocated to the job                                                                      |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-x, \--exclude](srun.md#OPT_exclude)                 | \<host1,host2,\... or filename\>                   | List of specific nodes to be excluded from allocation to the job                                                       |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| [-Z, \--no-allocate](srun.md#OPT_no-allocate)         | N/A                                                | Bypass normal allocation (privileged option available to users "SlurmUser" and "root" only)                            |
+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

: **srun/salloc/sbatch command line options that control Step 2**

\

### Step 3: Distribution of Tasks to the selected Nodes {#Step3}

In Step 3, Slurm distributes tasks to the nodes that were selected for the job/step in Step 1. Each task is distributed to only one node, but more than one task may be distributed to each node. Unless overcommitment of CPUs to tasks is specified for the job, the number of tasks distributed to a node is constrained by the number of CPUs allocated on the node and the number of CPUs per task. If consumable resources is configured, or resource sharing is allowed, tasks from more than one job/step may run on the same node concurrently.\
\
Step 3 is performed by slurmctld.\

+------------------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| **slurm.conf parameter**                             | **Possible values** | **Description**                                                                 |
+------------------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| [MaxTasksPerNode](slurm.conf.md#OPT_MaxTasksPerNode) | \<number\>          | Controls the maximum number of tasks that a job step can spawn on a single node |
+------------------------------------------------------+---------------------+---------------------------------------------------------------------------------+

: **slurm.conf options that control Step 3**

\

+-------------------------------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Command line option**                               | **Possible values**                              | **Description**                                                                                                                                                                                                                                                    |
+-------------------------------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\--distribution, -m](srun.md#OPT_distribution)       | block\|cyclic\                                   | The first specified distribution (before the \":\") controls the sequence in which tasks are distributed to each of the selected nodes. Note that this option does not affect the number of tasks distributed to each node, but only the sequence of distribution. |
|                                                       | \|arbitrary\|plane=\<options\>\[:block\|cyclic\] |                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\--ntasks-per-core](srun.md#OPT_ntasks-per-core)     | \<number\>                                       | Controls the maximum number of tasks per allocated core                                                                                                                                                                                                            |
+-------------------------------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\--ntasks-per-socket](srun.md#OPT_ntasks-per-socket) | \<number\>                                       | Controls the maximum number of tasks per allocated socket                                                                                                                                                                                                          |
+-------------------------------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\--ntasks-per-node](srun.md#OPT_ntasks-per-node)     | \<number\>                                       | Controls the maximum number of tasks per allocated node                                                                                                                                                                                                            |
+-------------------------------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [-r, \--relative](srun.md#OPT_relative)               | N/A                                              | Controls which node is used for a job step                                                                                                                                                                                                                         |
+-------------------------------------------------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: **srun/salloc/sbatch command line options that control Step 3**

\

### Step 4: Optional Distribution and Binding of Tasks to CPUs within a Node {#Step4}

In optional Step 4, Slurm distributes and binds each task to a specified subset of the allocated CPUs on the node to which the task was distributed in Step 3. Different tasks distributed to the same node may be bound to the same subset of CPUs or to different subsets. This step is known as task affinity or task/CPU binding.\
\
Step 4 is performed by slurmd and the task plugin.\

+--------------------------------------------+-------------------------------------------+--------------------------------------------------------------------+
| **slurm.conf parameter**                   | **Possible values**                       | **Description**                                                    |
+--------------------------------------------+-------------------------------------------+--------------------------------------------------------------------+
| [TaskPlugin](slurm.conf.md#OPT_TaskPlugin) | task/none \| task/affinity \| task/cgroup | Controls whether this step is enabled and which task plugin to use |
+--------------------------------------------+-------------------------------------------+--------------------------------------------------------------------+

: **slurm.conf options that control Step 4**

+----------------------------------+---------------------+---------------------------------------------------------------+
| **cgroup.conf parameter**        | **Possible values** | **Description**                                               |
+----------------------------------+---------------------+---------------------------------------------------------------+
| [ConstrainCores](cgroup.conf.md) | yes\|no             | Controls whether jobs are constrained to their allocated CPUs |
+----------------------------------+---------------------+---------------------------------------------------------------+

: **cgroup.conf options that control Step 4 (task/cgroup plugin only)**

\

+---------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Command line option**                           | **Possible values**                              | **Description**                                                                                                                                                       |
+---------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\--cpu-bind](srun.md#OPT_cpu-bind)               | See man page                                     | Controls binding of tasks to CPUs (srun only)                                                                                                                         |
+---------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\--ntasks-per-core](srun.md#OPT_ntasks-per-core) | \<number\>                                       | Controls the maximum number of tasks per allocated core                                                                                                               |
+---------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\--distribution, -m](srun.md#OPT_distribution)   | block\|cyclic\                                   | The second specified distribution (after the \":\") controls the sequence in which tasks are distributed to allocated CPUs within a node for binding of tasks to CPUs |
|                                                   | \|arbitrary\|plane=\<options\>\[:block\|cyclic\] |                                                                                                                                                                       |
+---------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: **srun/salloc/sbatch command line options that control Step 4**

\
\

## Additional Notes on CPU Management Steps {#notes}

For consumable resources, it is important for users to understand the difference between cpu allocation (Step 2) and task affinity/binding (Step 4). Exclusive (unshared) allocation of CPUs as consumable resources limits the number of jobs/steps/tasks that can use a node concurrently. But it does not limit the set of CPUs on the node that each task distributed to the node can use. Unless some form of CPU/task binding is used (e.g., a task or spank plugin), all tasks distributed to a node can use all of the CPUs on the node, including CPUs not allocated to their job/step. This may have unexpected adverse effects on performance, since it allows one job to use CPUs allocated exclusively to another job. For this reason, it may not be advisable to configure consumable resources without also configuring task affinity. Note that task affinity can also be useful when select/linear (whole node allocation) is configured, to improve performance by restricting each task to a particular socket or other subset of CPU resources on a node.

\
\

## Getting Information about CPU usage by Jobs/Steps/Tasks {#Section2}

There is no easy way to generate a comprehensive set of CPU management information for a job/step (allocation, distribution and binding). However, several commands/options provide limited information about CPU usage.

+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Command/Option**                                 | **Information**                                                                                                                                                                                                                                                      |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| scontrol show job option: \--details               | This option provides a list of the nodes selected for the job and the CPU ids allocated to the job on each node. Note that the CPU ids reported by this command are Slurm abstract CPU ids, not Linux/hardware CPU ids (as reported by, for example, /proc/cpuinfo). |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Linux command: env                                 | Man. Slurm environment variables provide information related to node and CPU usage:\                                                                                                                                                                                 |
|                                                    | \                                                                                                                                                                                                                                                                    |
|                                                    | SLURM_JOB_CPUS_PER_NODE\                                                                                                                                                                                                                                             |
|                                                    | SLURM_CPUS_PER_TASK\                                                                                                                                                                                                                                                 |
|                                                    | SLURM_CPU_BIND\                                                                                                                                                                                                                                                      |
|                                                    | SLURM_DISTRIBUTION\                                                                                                                                                                                                                                                  |
|                                                    | SLURM_JOB_NODELIST\                                                                                                                                                                                                                                                  |
|                                                    | SLURM_TASKS_PER_NODE\                                                                                                                                                                                                                                                |
|                                                    | SLURM_STEP_NODELIST\                                                                                                                                                                                                                                                 |
|                                                    | SLURM_STEP_NUM_NODES\                                                                                                                                                                                                                                                |
|                                                    | SLURM_STEP_NUM_TASKS\                                                                                                                                                                                                                                                |
|                                                    | SLURM_STEP_TASKS_PER_NODE\                                                                                                                                                                                                                                           |
|                                                    | SLURM_JOB_NUM_NODES\                                                                                                                                                                                                                                                 |
|                                                    | SLURM_NTASKS\                                                                                                                                                                                                                                                        |
|                                                    | SLURM_NPROCS\                                                                                                                                                                                                                                                        |
|                                                    | SLURM_CPUS_ON_NODE\                                                                                                                                                                                                                                                  |
|                                                    | SLURM_NODEID\                                                                                                                                                                                                                                                        |
|                                                    | SLURMD_NODENAME\                                                                                                                                                                                                                                                     |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| srun option: \--cpu-bind=verbose                   | This option provides a list of the CPU masks used by task affinity to bind tasks to CPUs. Note that the CPU ids represented by these masks are Linux/hardware CPU ids, not Slurm abstract CPU ids as reported by scontrol, etc.                                      |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| srun/salloc/sbatch option: -l                      | This option adds the task id as a prefix to each line of output from a task sent to stdout/stderr. This can be useful for distinguishing node-related and CPU-related information by task id for multi-task jobs/steps.                                              |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Linux command:\                                    | Given a task\'s pid (or \"self\" if the command is executed by the task itself), this command produces a list of the CPU ids bound to the task. This is the same information that is provided by \--cpu-bind=verbose, but in a more readable format.                 |
| cat /proc/\<pid\>/status \| grep Cpus_allowed_list |                                                                                                                                                                                                                                                                      |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\

### A Note on CPU Numbering {#numbering}

The number and layout of logical CPUs known to Slurm is described in the node definitions in slurm.conf. This may differ from the physical CPU layout on the actual hardware. For this reason, Slurm generates its own internal, or \"abstract\", CPU numbers. These numbers may not match the physical, or \"machine\", CPU numbers known to Linux.

\

## CPU Management and Slurm Accounting {#Section3}

CPU management by Slurm users is subject to limits imposed by Slurm Accounting. Accounting limits may be applied on CPU usage at the level of users, groups and clusters. For details, see the sacctmgr man page.

\

## CPU Management Examples {#Section4}

The following examples illustrate some scenarios for managing CPU resources using Slurm. Many additional scenarios are possible. In each example, it is assumed that all CPUs on each node are available for allocation.

- Example Node and Partition Configuration\
- Example 1: Allocation of whole nodes\
- Example 2: Simple allocation of cores as consumable resources
- Example 3: Consumable resources with balanced allocation across nodes
- Example 4: Consumable resources with minimization of resource fragmentation
- Example 5: Consumable resources with cyclic distribution of tasks to nodes
- Example 6: Consumable resources with default allocation and plane distribution of tasks to nodes
- Example 7: Consumable resources with overcommitment of CPUs to tasks
- Example 8: Consumable resources with resource sharing between jobs
- Example 9: Consumable resources on multithreaded node, allocating only one thread per core
- Example 10: Consumable resources with task affinity and core binding
- Example 11: Consumable resources with task affinity and socket binding, Case 1
- Example 12: Consumable resources with task affinity and socket binding, Case 2
- Example 13: Consumable resources with task affinity and socket binding, Case 3
- Example 14: Consumable resources with task affinity and customized allocation and distribution
- Example 15: Consumable resources with task affinity to optimize the performance of a multi-task, multi-thread job
- Example 16: Consumable resources with task cgroup

\

### Example Node and Partition Configuration {#Example}

For these examples, the Slurm cluster contains the following nodes:

  ----------------------------------- -------- -------- -------- --------
  **Nodename**                        **n0**   **n1**   **n2**   **n3**
  Number of Sockets                   2        2        2        2
  Number of Cores per Socket          4        4        4        4
  Total Number of Cores               8        8        8        8
  Number of Threads (CPUs) per Core   1        1        1        2
  Total Number of CPUs                8        8        8        16
  ----------------------------------- -------- -------- -------- --------

And the following partitions:

  ------------------- -------------- ---------------
  **PartitionName**   **regnodes**   **hypernode**
  Nodes               n0 n1 n2       n3
  Default             YES            \-
  ------------------- -------------- ---------------

These entities are defined in slurm.conf as follows:

    Nodename=n0 NodeAddr=node0 Sockets=2 CoresPerSocket=4 ThreadsPerCore=1 Procs=8
    Nodename=n1 NodeAddr=node1 Sockets=2 CoresPerSocket=4 ThreadsPerCore=1 Procs=8 State=IDLE
    Nodename=n2 NodeAddr=node2 Sockets=2 CoresPerSocket=4 ThreadsPerCore=1 Procs=8 State=IDLE
    Nodename=n3 NodeAddr=node3 Sockets=2 CoresPerSocket=4 ThreadsPerCore=2 Procs=16 State=IDLE
    PartitionName=regnodes Nodes=n0,n1,n2 OverSubscribe=YES Default=YES State=UP
    PartitionName=hypernode Nodes=n3 State=UP

These examples show the use of the cons_tres plugin.

\

### Example 1: Allocation of whole nodes {#Example1}

Allocate a minimum of two whole nodes to a job.

slurm.conf options:

    SelectType=select/linear

Command line:

    srun --nodes=2 ...

Comments:

The SelectType=select/linear configuration option specifies allocation in units of whole nodes. The \--nodes=2 srun option causes Slurm to allocate at least 2 nodes to the job.

\

### Example 2: Simple allocation of cores as consumable resources {#Example2}

A job requires 6 CPUs (2 tasks and 3 CPUs per task with no overcommitment). Allocate the 6 CPUs as consumable resources from a single node in the default partition.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core

Command line:

    srun --nodes=1-1 --ntasks=2 --cpus-per-task=3 ...

Comments:

The SelectType configuration options define cores as consumable resources. The \--nodes=1-1 srun option restricts the job to a single node. The following table shows a possible pattern of allocation for this job.

  ------------------------------ -------- -------- --------
  **Nodename**                   **n0**   **n1**   **n2**
  **Number of Allocated CPUs**   6        0        0
  **Number of Tasks**            2        0        0
  ------------------------------ -------- -------- --------

\

### Example 3: Consumable resources with balanced allocation across nodes {#Example3}

A job requires 9 CPUs (3 tasks and 3 CPUs per task with no overcommitment). Allocate 3 CPUs from each of the 3 nodes in the default partition.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core

Command line:

    srun --nodes=3-3 --ntasks=3 --cpus-per-task=3 ...

Comments:

The options specify the following conditions for the job: 3 tasks, 3 unique CPUs per task, using exactly 3 nodes. To satisfy these conditions, Slurm must allocate 3 CPUs from each node. The following table shows the allocation for this job.

  ------------------------------ -------- -------- --------
  **Nodename**                   **n0**   **n1**   **n2**
  **Number of Allocated CPUs**   3        3        3
  **Number of Tasks**            1        1        1
  ------------------------------ -------- -------- --------

\

### Example 4: Consumable resources with minimization of resource fragmentation {#Example4}

A job requires 12 CPUs (12 tasks and 1 CPU per task with no overcommitment). Allocate CPUs using the minimum number of nodes and the minimum number of sockets required for the job in order to minimize fragmentation of allocated/unallocated CPUs in the cluster.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core,CR_CORE_DEFAULT_DIST_BLOCK

Command line:

    srun --ntasks=12 ...

Comments:

The default allocation method across nodes is block. This minimizes the number of nodes used for the job. The configuration option CR_CORE_DEFAULT_DIST_BLOCK sets the default allocation method within a node to block. This minimizes the number of sockets used for the job within a node. The combination of these two methods causes Slurm to allocate the 12 CPUs using the minimum required number of nodes (2 nodes) and sockets (3 sockets).The following table shows a possible pattern of allocation for this job.

+------------------------------+-------+-------+-------+-------+-------+-------+
| **Nodename**                 | **n0**        | **n1**        | **n2**        |
+------------------------------+-------+-------+-------+-------+-------+-------+
| **Socket id**                | **0** | **1** | **0** | **1** | **0** | **1** |
+------------------------------+-------+-------+-------+-------+-------+-------+
| **Number of Allocated CPUs** | 4     | 4     | 4     | 0     | 0     | 0     |
+------------------------------+-------+-------+-------+-------+-------+-------+
| **Number of Tasks**          | 8             | 4             | 0             |
+------------------------------+---------------+---------------+---------------+

\

### Example 5: Consumable resources with cyclic distribution of tasks to nodes {#Example5}

A job requires 12 CPUs (6 tasks and 2 CPUs per task with no overcommitment). Allocate 6 CPUs each from 2 nodes in the default partition. Distribute tasks to nodes cyclically.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core

Command line:

    srun --nodes=2-2 --ntasks-per-node=3 --distribution=cyclic 

    --ntasks=6 --cpus-per-task=2 ...

Comments:

The options specify the following conditions for the job: 6 tasks, 2 unique CPUs per task, using exactly 2 nodes, and with 3 tasks per node. To satisfy these conditions, Slurm must allocate 6 CPUs from each of the 2 nodes. The \--distribution=cyclic option causes the tasks to be distributed to the nodes in a round-robin fashion. The following table shows a possible pattern of allocation and distribution for this job.

+------------------------------------------------+--------+--------+--------+
| **Nodename**                                   | **n0** | **n1** | **n2** |
+------------------------------------------------+--------+--------+--------+
| **Number of Allocated CPUs**                   | 6      | 6      | 0      |
+------------------------------------------------+--------+--------+--------+
| **Number of Tasks**                            | 3      | 3      | 0      |
+------------------------------------------------+--------+--------+--------+
| **Distribution of Tasks to Nodes, by Task id** | 0\     | 1\     | \-     |
|                                                | 2\     | 3\     |        |
|                                                | 4      | 5      |        |
+------------------------------------------------+--------+--------+--------+

\

### Example 6: Consumable resources with default allocation and plane distribution of tasks to nodes {#Example6}

A job requires 16 CPUs (8 tasks and 2 CPUs per task with no overcommitment). Use all 3 nodes in the default partition. Distribute tasks to each node in blocks of two in a round-robin fashion.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core

Command line:

    srun --nodes=3-3 --distribution=plane=2 --ntasks=8 --cpus-per-task=2 ...

Comments:

The options specify the following conditions for the job: 8 tasks, 2 unique CPUs per task, using all 3 nodes in the partition. To satisfy these conditions using the default allocation method across nodes (block), Slurm allocates 8 CPUs from the first node, 6 CPUs from the second node and 2 CPUs from the third node. The \--distribution=plane=2 option causes Slurm to distribute tasks in blocks of two to each of the nodes in a round-robin fashion, subject to the number of CPUs allocated on each node. So, for example, only 1 task is distributed to the third node because only 2 CPUs were allocated on that node and each task requires 2 CPUs. The following table shows a possible pattern of allocation and distribution for this job.

+------------------------------------------------+--------+--------+--------+
| **Nodename**                                   | **n0** | **n1** | **n2** |
+------------------------------------------------+--------+--------+--------+
| **Number of Allocated CPUs**                   | 8      | 6      | 2      |
+------------------------------------------------+--------+--------+--------+
| **Number of Tasks**                            | 4      | 3      | 1      |
+------------------------------------------------+--------+--------+--------+
| **Distribution of Tasks to Nodes, by Task id** | 0 1\   | 2 3\   | 4\     |
|                                                | 5 6    | 7      |        |
+------------------------------------------------+--------+--------+--------+

\

### Example 7: Consumable resources with overcommitment of CPUs to tasks {#Example7}

A job has 20 tasks. Run the job in a single node.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core

Command line:

    srun --nodes=1-1 --ntasks=20 --overcommit ...

Comments:

The \--overcommit option allows the job to run in only one node by overcommitting CPUs to tasks.The following table shows a possible pattern of allocation and distribution for this job.

  ------------------------------------------------ -------- -------- --------
  **Nodename**                                     **n0**   **n1**   **n2**
  **Number of Allocated CPUs**                     8        0        0
  **Number of Tasks**                              20       0        0
  **Distribution of Tasks to Nodes, by Task id**   0 - 19   \-       \-
  ------------------------------------------------ -------- -------- --------

\

### Example 8: Consumable resources with resource sharing between jobs {#Example8}

2 jobs each require 6 CPUs (6 tasks per job with no overcommitment). Run both jobs simultaneously in a single node.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core

Command line:

    srun --nodes=1-1 --nodelist=n0 --ntasks=6 --oversubscribe ...
    srun --nodes=1-1 --nodelist=n0 --ntasks=6 --oversubscribe ...

Comments:

The \--nodes=1-1 and \--nodelist=n0 srun options together restrict both jobs to node n0. The OverSubscribe=YES option in the partition definition plus the \--oversubscribe srun option allows the two jobs to oversubscribe CPUs on the node.

\

### Example 9: Consumable resources on multithreaded node, allocating only one thread per core {#Example9}

A job requires 8 CPUs (8 tasks with no overcommitment). Run the job on node n3, allocating only one thread per core.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_CPU

Command line:

    srun --partition=hypernode --ntasks=8 --hint=nomultithread ...

Comments:

The CR_CPU configuration option enables the allocation of only one thread per core. The \--hint=nomultithread srun option causes Slurm to allocate only one thread from each core to this job. The following table shows a possible pattern of allocation for this job.

+------------------------------+---------+---------+---------+---------+---------+---------+---------+---------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                 | **n3**                                                                                                                                                |
+------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Socket id**                | **0**                                                                         | **1**                                                                 |
+------------------------------+-------------------+-------------------+-------------------+-------------------+-----------------+-----------------+-----------------+-----------------+
| **Core id**                  | **0**             | **1**             | **2**             | **3**             | **0**           | **1**           | **2**           | **3**           |
+------------------------------+---------+---------+---------+---------+---------+---------+---------+---------+--------+--------+--------+--------+--------+--------+--------+--------+
| **CPU id**                   | **0**   | **1**   | **2**   | **3**   | **4**   | **5**   | **6**   | **7**   | **8**  | **9**  | **10** | **11** | **12** | **13** | **14** | **15** |
+------------------------------+---------+---------+---------+---------+---------+---------+---------+---------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Number of Allocated CPUs** | 4                                                                             | 4                                                                     |
+------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Allocated CPU ids**        | 0 2 4 6                                                                       | 8 10 12 14                                                            |
+------------------------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------+

\

### Example 10: Consumable resources with task affinity and core binding {#Example10}

A job requires 6 CPUs (6 tasks with no overcommitment). Run the job in a single node in the default partition. Apply core binding to each task.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core
    TaskPlugin=task/affinity

Command line:

    srun --nodes=1-1 --ntasks=6 --cpu-bind=cores ...

Comments:

Using the default allocation method within nodes (cyclic), Slurm allocates 3 CPUs on each socket of 1 node. Using the default distribution method within nodes (cyclic), Slurm distributes and binds each task to an allocated core in a round-robin fashion across the sockets. The following table shows a possible pattern of allocation, distribution and binding for this job. For example, task id 2 is bound to CPU id 1.

+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                                  | **n0**                                                                |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Socket id**                                 | **0**                             | **1**                             |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Number of Allocated CPUs**                  | 3                                 | 3                                 |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Allocated CPU ids**                         | 0 1 2                             | 4 5 6                             |
+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Binding of Tasks to CPUs** | **CPU id**     | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  |
|                              +----------------+--------+--------+--------+--------+--------+--------+--------+--------+
|                              | **Task id**    | 0      | 2      | 4      | \-     | 1      | 3      | 5      | \-     |
+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+

\

### Example 11: Consumable resources with task affinity and socket binding, Case 1 {#Example11}

A job requires 6 CPUs (6 tasks with no overcommitment). Run the job in a single node in the default partition. Apply socket binding to each task.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core
    TaskPlugin=task/affinity

Command line:

    srun --nodes=1-1 --ntasks=6 --cpu-bind=sockets ...

Comments:

Using the default allocation method within nodes (cyclic), Slurm allocates 3 CPUs on each socket of 1 node. Using the default distribution method within nodes (cyclic), Slurm distributes and binds each task to all of the allocated CPUs in one socket in a round-robin fashion across the sockets. The following table shows a possible pattern of allocation, distribution and binding for this job. For example, task ids 1, 3 and 5 are all bound to CPU ids 4, 5 and 6.

+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                                  | **n0**                                                                |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Socket id**                                 | **0**                             | **1**                             |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Number of Allocated CPUs**                  | 3                                 | 3                                 |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Allocated CPU ids**                         | 0 1 2                             | 4 5 6                             |
+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Binding of Tasks to CPUs** | **CPU id**     | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  |
|                              +----------------+--------+--------+--------+--------+--------+--------+--------+--------+
|                              | **Task ids**   | 0 2 4                    | \-     | 1 3 5                    | \-     |
+------------------------------+----------------+--------------------------+--------+--------------------------+--------+

\

### Example 12: Consumable resources with task affinity and socket binding, Case 2 {#Example12}

A job requires 6 CPUs (2 tasks with 3 cpus per task and no overcommitment). Run the job in a single node in the default partition. Allocate cores using the block allocation method. Distribute cores using the block distribution method. Apply socket binding to each task.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core,CR_CORE_DEFAULT_DIST_BLOCK
    TaskPlugin=task/affinity

Command line:

    srun --nodes=1-1 --ntasks=2 --cpus-per-task=3 --cpu-bind=sockets 

    --distribution=block:block ...

Comments:

Using the block allocation method, Slurm allocates 4 CPUs on one socket and 2 CPUs on the other socket of one node. Using the block distribution method within nodes, Slurm distributes 3 CPUs to each task. Applying socket binding, Slurm binds each task to all allocated CPUs in all sockets in which the task has a distributed CPU. The following table shows a possible pattern of allocation, distribution and binding for this job. In this example, using the block allocation method CPU ids 0-3 are allocated on socket id 0 and CPU ids 4-5 are allocated on socket id 1. Using the block distribution method, CPU ids 0-2 were distributed to task id 0, and CPU ids 3-5 were distributed to task id 1. Applying socket binding, task id 0 is therefore bound to the allocated CPUs on socket 0, and task id 1 is bound to the allocated CPUs on both sockets.

+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                                  | **n0**                                                                |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Socket id**                                 | **0**                             | **1**                             |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Number of Allocated CPUs**                  | 4                                 | 2                                 |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Allocated CPU ids**                         | 0 1 2 3                           | 4 5                               |
+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Binding of Tasks to CPUs** | **CPU id**     | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  |
|                              +----------------+--------+--------+--------+--------+--------+--------+--------+--------+
|                              | **Task ids**   | 0 1                               | 1               | \-              |
+------------------------------+----------------+-----------------------------------+-----------------+-----------------+

\

### Example 13: Consumable resources with task affinity and socket binding, Case 3 {#Example13}

A job requires 6 CPUs (2 tasks with 3 cpus per task and no overcommitment). Run the job in a single node in the default partition. Allocate cores using the block allocation method. Distribute cores using the cyclic distribution method. Apply socket binding to each task.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core,CR_CORE_DEFAULT_DIST_BLOCK
    TaskPlugin=task/affinity

Command line:

    srun --nodes=1-1 --ntasks=2 --cpus-per-task=3 --cpu-bind=sockets 

    --distribution=block:cyclic ...

Comments:

Using the block allocation method, Slurm allocates 4 CPUs on one socket and 2 CPUs on the other socket of one node. Using the cyclic distribution method within nodes, Slurm distributes 3 CPUs to each task. Applying socket binding, Slurm binds each task to all allocated CPUs in all sockets in which the task has a distributed CPU. The following table shows a possible pattern of allocation, distribution and binding for this job. In this example, using the block allocation method CPU ids 0-3 are allocated on socket id 0 and CPU ids 4-5 are allocated on socket id 1. Using the cyclic distribution method, CPU ids 0, 1 and 4 were distributed to task id 0, and CPU ids 2, 3 and 5 were distributed to task id 1. Applying socket binding, both tasks are therefore bound to the allocated CPUs on both sockets.

+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                                  | **n0**                                                                |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Socket id**                                 | **0**                             | **1**                             |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Number of Allocated CPUs**                  | 4                                 | 2                                 |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Allocated CPU ids**                         | 0 1 2 3                           | 4 5                               |
+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Binding of Tasks to CPUs** | **CPU id**     | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  |
|                              +----------------+--------+--------+--------+--------+--------+--------+--------+--------+
|                              | **Task ids**   | 0 1                               | 0 1             | \-              |
+------------------------------+----------------+-----------------------------------+-----------------+-----------------+

\

### Example 14: Consumable resources with task affinity and customized allocation and distribution {#Example14}

A job requires 18 CPUs (18 tasks with no overcommitment). Run the job in the default partition. Allocate 6 CPUs on each node using block allocation within nodes. Use cyclic distribution of tasks to nodes and block distribution of tasks for CPU binding.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core,CR_CORE_DEFAULT_DIST_BLOCK
    TaskPlugin=task/affinity

Command line:

    srun --nodes=3-3 --ntasks=18 --ntasks-per-node=6 

    --distribution=cyclic:block --cpu-bind=cores ...

Comments:

This example shows the use of task affinity with customized allocation of CPUs and distribution of tasks across nodes and within nodes for binding. The srun options specify the following conditions for the job: 18 tasks, 1 unique CPU per task, using all 3 nodes in the partition, with 6 tasks per node. The CR_CORE_DEFAULT_DIST_BLOCK configuration option specifies block allocation within nodes. To satisfy these conditions, Slurm allocates 6 CPUs on each node, with 4 CPUs allocated on one socket and 2 CPUs on the other socket. The \--distribution=cyclic:block option specifies cyclic distribution of tasks to nodes and block distribution of tasks to CPUs within nodes for binding. The following table shows a possible pattern of allocation, distribution and binding for this job. For example, task id 10 is bound to CPU id 3 on node n1.

+------------------------------+-------------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                                           | **n0**                                                                | **n1**                                                                | **n2**                                                                |
+--------------------------------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
| **Socket id**                                          | **0**                             | **1**                             | **0**                             | **1**                             | **0**                             | **1**                             |
+--------------------------------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
| **Number of Allocated CPUs**                           | 4                                 | 2                                 | 4                                 | 2                                 | 4                                 | 2                                 |
+--------------------------------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
| **Allocated CPU ids**                                  | 0 1 2 3 4 5                                                           | 0 1 2 3 4 5                                                           | 0 1 2 3 4 5                                                           |
+--------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Number of Tasks**                                    | 6                                                                     | 6                                                                     | 6                                                                     |
+--------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Distribution of Tasks to Nodes, by Task id**         | 0\                                                                    | 1\                                                                    | 2\                                                                    |
|                                                        | 3\                                                                    | 4\                                                                    | 5\                                                                    |
|                                                        | 6\                                                                    | 7\                                                                    | 8\                                                                    |
|                                                        | 9\                                                                    | 10\                                                                   | 11\                                                                   |
|                                                        | 12\                                                                   | 13\                                                                   | 14\                                                                   |
|                                                        | 15                                                                    | 16                                                                    | 17                                                                    |
+------------------------------+-------------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Binding of Tasks to CPUs** | **CPU id**              | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  |
|                              +-------------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
|                              | **Task id**             | 0      | 3      | 6      | 9      | 12     | 15     | \-     | \-     | 1      | 4      | 7      | 10     | 13     | 16     | \-     | \-     | 2      | 5      | 8      | 11     | 14     | 17     | \-     | \-     |
+------------------------------+-------------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

\

### Example 15: Consumable resources with task affinity to optimize the performance of a multi-task, multi-thread job {#Example15}

A job requires 9 CPUs (3 tasks and 3 CPUs per task with no overcommitment). Run the job in the default partition, managing the CPUs to optimize the performance of the job.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core,CR_CORE_DEFAULT_DIST_BLOCK
    TaskPlugin=task/affinity

Command line:

    srun --ntasks=3 --cpus-per-task=3 --ntasks-per-node=1 --cpu-bind=cores ...

Comments:

To optimize the performance of this job, the user wishes to allocate 3 CPUs from each of 3 sockets and bind each task to the 3 CPUs in a single socket. The SelectTypeParameters configuration option specifies a consumable resource type of cores and block allocation within nodes. The TaskPlugin configuration option enables task affinity. The srun options specify the following conditions for the job: 3 tasks, with 3 unique CPUs per task, with 1 task per node. To satisfy these conditions, Slurm allocates 3 CPUs from one socket in each of the 3 nodes in the default partition. The \--cpu-bind=cores option causes Slurm to bind each task to the 3 allocated CPUs on the node to which it is distributed. The following table shows a possible pattern of allocation, distribution and binding for this job. For example, task id 2 is bound to CPU ids 0, 1 and 2 on socket id 0 of node n2.

+------------------------------+-------------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                                           | **n0**                                                                | **n1**                                                                | **n2**                                                                |
+--------------------------------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
| **Socket id**                                          | **0**                             | **1**                             | **0**                             | **1**                             | **0**                             | **1**                             |
+--------------------------------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
| **Number of Allocated CPUs**                           | 3                                 | 0                                 | 3                                 | 0                                 | 3                                 | 0                                 |
+--------------------------------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------------------------+
| **Allocated CPU ids**                                  | 0 1 2                                                                 | 0 1 2                                                                 | 0 1 2                                                                 |
+--------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Number of Tasks**                                    | 1                                                                     | 1                                                                     | 1                                                                     |
+--------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Distribution of Tasks to Nodes, by Task id**         | 0                                                                     | 1                                                                     | 2                                                                     |
+------------------------------+-------------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Binding of Tasks to CPUs** | **CPU id**              | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  |
|                              +-------------------------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
|                              | **Task id**             | 0                        | \-                                         | 1                        | \-                                         | 2                        | \--                                        |
+------------------------------+-------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------------------------+

\

### Example 16: Consumable resources with task cgroup {#Example16}

A job requires 6 CPUs (6 tasks with no overcommitment). Run the job in a single node in the default partition.

slurm.conf options:

    SelectType=select/cons_tres
    SelectTypeParameters=CR_Core
    TaskPlugin=task/cgroup

cgroup.conf options:

    ConstrainCores=yes

Command line:

    srun --nodes=1-1 --ntasks=6 ...

Comments:

The task/cgroup plugin currently supports only the block method for allocating cores within nodes. Slurm distributes tasks to the cores but without cpu binding, each task has access to all the allocated CPUs. The following table shows a possible pattern of allocation, distribution and binding for this job.

+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Nodename**                                  | **n0**                                                                |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Socket id**                                 | **0**                             | **1**                             |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Number of Allocated CPUs**                  | 4                                 | 2                                 |
+-----------------------------------------------+-----------------------------------+-----------------------------------+
| **Allocated CPU ids**                         | 0 1 2 3                           | 4 5                               |
+------------------------------+----------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **Binding of Tasks to CPUs** | **CPU id**     | **0**  | **1**  | **2**  | **3**  | **4**  | **5**  | **6**  | **7**  |
|                              +----------------+--------+--------+--------+--------+--------+--------+--------+--------+
|                              | **Task id**    | 0-5                               | 0-5             | \-              |
+------------------------------+----------------+-----------------------------------+-----------------+-----------------+

The task/cgroup plugin does not bind tasks to CPUs. To bind tasks to CPUs and for access to all task distribution options, the task/affinity plugin can be used with the task/cgroup plugin:

    TaskPlugin=task/cgroup,task/affinity
