# [Consumable Resources in Slurm]{#top}

Slurm, using the default node allocation plug-in, allocates nodes to jobs in exclusive mode. This means that even when all the resources within a node are not utilized by a given job, another job will not have access to these resources. Nodes possess resources such as processors, memory, swap, local disk, etc. and jobs consume these resources. The exclusive use default policy in Slurm can result in inefficient utilization of the cluster and of its nodes resources. Slurm\'s *cons_tres* plugin is available to manage resources on a much more fine-grained basis as described below.

## Using the Consumable Trackable Resource Plugin: **select/cons_tres** {#using_cons_tres}

The Consumable Trackable Resources (**cons_tres**) plugin has been built to work with several resources. It can track a Board, Socket, Core, CPU, Memory as well as any combination of the logical processors with Memory:

- **CPU** (*CR_CPU*): CPU as a consumable resource.
  - No notion of sockets, cores, or threads.
  - On a multi-core system CPUs will be cores.
  - On a multi-core/hyperthread system CPUs will be threads.
  - On a single-core system CPUs are CPUs.
- **Board** (*CR_Board*): Baseboard as a consumable resource.
- **Socket** (*CR_Socket*): Socket as a consumable resource.
- **Core** (*CR_Core*): Core as a consumable resource.
- **Socket and Memory** (*CR_Socket_Memory*): Socket and Memory as consumable resources.
- **Core and Memory** (*CR_Core_Memory*): Core and Memory as consumable resources.
- **CPU and Memory** (*CR_CPU_Memory*) CPU and Memory as consumable resources.

All CR\_\* parameters assume **OverSubscribe=No** or **OverSubscribe=Force**.

The cons_tres plugin also provides functionality specifically related to GPUs.

Additional parameters available for the **cons_tres** plugin:

- **DefCpuPerGPU**: Default number of CPUs allocated per GPU.
- **DefMemPerGPU**: Default amount of memory allocated per GPU.

Additional job submit options available for the **cons_tres** plugin:

- **\--cpus-per-gpu=**: Number of CPUs for every GPU.
- **\--gpus=**: Count of GPUs for entire job allocation.
- **\--gpu-bind=**: Bind task to specific GPU(s).
- **\--gpu-freq=**: Request specific GPU/memory frequencies.
- **\--gpus-per-node=**: Number of GPUs per node.
- **\--gpus-per-socket=**: Number of GPUs per socket.
- **\--gpus-per-task=**: Number of GPUs per task.
- **\--mem-per-gpu=**: Amount of memory for each GPU.

srun\'s *-B* extension for sockets, cores, and threads is ignored within the node allocation mechanism when CR_CPU or CR_CPU_MEMORY is selected. It is used to compute the total number of tasks when *-n* is not specified.

In the cases where Memory is a consumable resource, the **RealMemory** parameter must be set in the slurm.conf to define a node\'s amount of real memory.

The job submission commands (salloc, sbatch and srun) support the options *\--mem=MB* and *\--mem-per-cpu=MB*, permitting users to specify the maximum amount of real memory required per node or per allocated CPU. This option is required in the environments where Memory is a consumable resource. It is important to specify enough memory since Slurm will not allow the application to use more than the requested amount of real memory. The default value for \--mem is inherited from **DefMemPerNode**. See [srun](srun.md#OPT_mem)(1) for more details.

Using *\--overcommit* or *-O* is allowed. When the process to logical processor pinning is enabled by using an appropriate TaskPlugin configuration parameter, the extra processes will time share the allocated resources.

The Consumable Trackable Resource plugin is enabled via the SelectType parameter in the slurm.conf.

    # Excerpt from sample slurm.conf file
    SelectType=select/cons_tres

## General Comments {#general}

Slurm\'s default **select/linear** plugin is using a best fit algorithm based on number of consecutive nodes.

The **select/cons_tres** plugin is enabled or disabled cluster-wide.

In the case where **select/linear** is enabled, the normal Slurm behaviors are not disrupted. The major change users see when using the **select/cons_tres** plugin is that jobs can be co-scheduled on nodes when resources permit it. Generic resources (such as GPUs) can also be tracked individually with this plugin. The rest of Slurm, such as srun and its options (except srun -s \...), etc. are not affected by this plugin. Slurm is, from the user\'s point of view, working the same way as when using the default node selection scheme.

The *\--exclusive* srun option allows users to request nodes in exclusive mode even when consumable resources is enabled. See [srun](srun.md#OPT_exclusive)(1) for details.

srun\'s *-s* or *\--oversubscribe* is incompatible with the consumable resource environment and will therefore not be honored. Since this environment\'s nodes are shared by default, *\--exclusive* allows users to obtain dedicated nodes.

The *\--oversubscribe* and *\--exclusive* options are mutually exclusive when used at job submission. If both options are set when submitting a job, the job submission command used will fatal.

## Examples of CR_Socket_Memory, and CR_CPU_Memory type consumable resources {#example_mem}

    # sinfo -lNe
    NODELIST     NODES PARTITION  STATE  CPUS  S:C:T MEMORY
    hydra[12-16]     5 allNodes*  ...       4  2:2:1   2007

Using select/cons_tres plug-in with CR_Socket_Memory (2 sockets/node)

    Example 1:
    # srun -N 5 -n 5 --mem=1000 sleep 100 &        <-- running
    # srun -n 1 -w hydra12 --mem=2000 sleep 100 &  <-- queued and waiting for resources

    # squeue
    JOBID PARTITION   NAME   USER ST  TIME  NODES NODELIST(REASON)
     1890  allNodes  sleep sballe PD  0:00      1 (Resources)
     1889  allNodes  sleep sballe  R  0:08      5 hydra[12-16]

    Example 2:
    # srun -N 5 -n 10 --mem=10 sleep 100 & <-- running
    # srun -n 1 --mem=10 sleep 100 & <-- queued and waiting for resourcessqueue

    # squeue
    JOBID PARTITION   NAME   USER ST  TIME  NODES NODELIST(REASON)
     1831  allNodes  sleep sballe PD  0:00      1 (Resources)
     1830  allNodes  sleep sballe  R  0:07      5 hydra[12-16]

Using select/cons_tres plug-in with CR_CPU_Memory (4 CPUs/node)

    Example 1:
    # srun -N 5 -n 5 --mem=1000 sleep 100 &  <-- running
    # srun -N 5 -n 5 --mem=10 sleep 100 &    <-- running
    # srun -N 5 -n 5 --mem=1000 sleep 100 &  <-- queued and waiting for resources

    # squeue
    JOBID PARTITION   NAME   USER ST  TIME  NODES NODELIST(REASON)
     1835  allNodes  sleep sballe PD  0:00      5 (Resources)
     1833  allNodes  sleep sballe  R  0:10      5 hydra[12-16]
     1834  allNodes  sleep sballe  R  0:07      5 hydra[12-16]

    Example 2:
    # srun -N 5 -n 20 --mem=10 sleep 100 & <-- running
    # srun -n 1 --mem=10 sleep 100 &       <-- queued and waiting for resources

    # squeue
    JOBID PARTITION   NAME   USER ST  TIME  NODES NODELIST(REASON)
     1837  allNodes  sleep sballe PD  0:00      1 (Resources)
     1836  allNodes  sleep sballe  R  0:11      5 hydra[12-16]

## Example of Node Allocations Using Consumable Resource Plugin {#example_node}

The following example illustrates the different ways four jobs are allocated across a cluster using (1) Slurm\'s default allocation method (exclusive mode) and (2) a processor as consumable resource approach.

It is important to understand that the example listed below is a contrived example and is only given here to illustrate the use of CPUs as consumable resources. Job 2 and Job 3 call for the node count to equal the processor count. This would typically be done because that one task per node requires all of the memory, disk space, etc. The bottleneck would not be processor count.

Trying to execute more than one job per node will almost certainly severely impact a parallel job\'s performance. The biggest beneficiary of CPUs as consumable resources will be serial jobs or jobs with modest parallelism, which can effectively share resources. On many systems with larger processor count, jobs typically run one fewer task than there are processors to minimize interference by the kernel and daemons.

The example cluster is composed of 4 nodes (10 CPUs in total):

- linux01 (with 2 processors),
- linux02 (with 2 processors),
- linux03 (with 2 processors), and
- linux04 (with 4 processors).

The four jobs are the following:

- \[2\] srun -n 4 -N 4 sleep 120 &
- \[3\] srun -n 3 -N 3 sleep 120 &
- \[4\] srun -n 1 sleep 120 &
- \[5\] srun -n 3 sleep 120 &

The user launches them in the same order as listed above.

## Using Slurm\'s Default Node Allocation (Non-shared Mode) {#using_default}

The four jobs have been launched and 3 of the jobs are now pending, waiting to get resources allocated to them. Only Job 2 is running since it uses one CPU on all 4 nodes. This means that linux01 to linux03 each have one idle CPU and linux04 has 3 idle CPUs.

    # squeue
    JOBID PARTITION   NAME  USER  ST  TIME  NODES NODELIST(REASON)
        3       lsf  sleep  root  PD  0:00      3 (Resources)
        4       lsf  sleep  root  PD  0:00      1 (Resources)
        5       lsf  sleep  root  PD  0:00      1 (Resources)
        2       lsf  sleep  root   R  0:14      4 linux[01-04]

Once Job 2 is finished, Job 3 is scheduled and runs on linux01, linux02, and linux03. Job 3 is only using one CPU on each of the 3 nodes. Job 4 can be allocated onto the remaining idle node (linux04) so Job 3 and Job 4 can run concurrently on the cluster.

Job 5 has to wait for idle nodes to be able to run.

    # squeue
    JOBID PARTITION   NAME  USER  ST  TIME  NODES NODELIST(REASON)
        5       lsf  sleep  root  PD  0:00      1 (Resources)
        3       lsf  sleep  root   R  0:11      3 linux[01-03]
        4       lsf  sleep  root   R  0:11      1 linux04

Once Job 3 finishes, Job 5 is allocated resources and can run.

The advantage of the exclusive mode scheduling policy is that the a job gets all the resources of the assigned nodes for optimal parallel performance. The drawback is that jobs can tie up large amount of resources that it does not use and which cannot be shared with other jobs.

## Using a Processor Consumable Resource Approach {#using_proc}

We will run through the same scenario again using the **cons_tres** plugin and CPUs as the consumable resource. The output of squeue shows that we have 3 out of the 4 jobs allocated and running. This is a 2 running job increase over the default Slurm approach.

Job 2 is running on nodes linux01 to linux04. Job 2\'s allocation is the same as for Slurm\'s default allocation which is that it uses one CPU on each of the 4 nodes. Once Job 2 is scheduled and running, nodes linux01, linux02 and linux03 still have one idle CPU each and node linux04 has 3 idle CPUs. The main difference between this approach and the exclusive mode approach described above is that idle CPUs within a node are now allowed to be assigned to other jobs.

It is important to note that *assigned* doesn\'t mean *oversubscription*. The consumable resource approach tracks how much of each available resource (in our case CPUs) must be dedicated to a given job. This allows us to prevent per node oversubscription of resources (CPUs).

Once Job 2 is running, Job 3 is scheduled onto node linux01, linux02, and Linux03 (using one CPU on each of the nodes) and Job 4 is scheduled onto one of the remaining idle CPUs on Linux04.

Job 2, Job 3, and Job 4 are now running concurrently on the cluster.

    # squeue
    JOBID PARTITION   NAME  USER  ST  TIME  NODES NODELIST(REASON)
        5       lsf  sleep  root  PD  0:00      1 (Resources)
        2       lsf  sleep  root   R  0:13      4 linux[01-04]
        3       lsf  sleep  root   R  0:09      3 linux[01-03]
        4       lsf  sleep  root   R  0:05      1 linux04

    # sinfo -lNe
    NODELIST     NODES PARTITION       STATE CPUS MEMORY TMP_DISK WEIGHT FEATURES REASON
    linux[01-03]     3      lsf*   allocated    2   2981        1      1   (null) none
    linux04          1      lsf*   allocated    4   3813        1      1   (null) none

Once Job 2 finishes, Job 5, which was pending, is allocated available resources and is then running as illustrated below:

    # squeue
    JOBID PARTITION   NAME  USER  ST  TIME  NODES NODELIST(REASON)
       3       lsf   sleep  root   R  1:58      3 linux[01-03]
       4       lsf   sleep  root   R  1:54      1 linux04
       5       lsf   sleep  root   R  0:02      3 linux[01-03]
    # sinfo -lNe
    NODELIST     NODES PARTITION       STATE CPUS MEMORY TMP_DISK WEIGHT FEATURES REASON
    linux[01-03]     3      lsf*   allocated    2   2981        1      1   (null) none
    linux04          1      lsf*        idle    4   3813        1      1   (null) none

Job 3, Job 4, and Job 5 are now running concurrently on the cluster.

    # squeue
    JOBID PARTITION   NAME  USER  ST  TIME  NODES NODELIST(REASON)
        5       lsf  sleep  root   R  1:52      3 linux[01-03]

Job 3 and Job 4 have finished and Job 5 is still running on nodes linux\[01-03\].

The advantage of the consumable resource scheduling policy is that the job throughput can increase dramatically. The overall job throughput and productivity of the cluster increases, thereby reducing the amount of time users have to wait for their job to complete as well as increasing the overall efficiency of the use of the cluster. The drawback is that users do not have entire nodes dedicated to their jobs by default.

We have added the *\--exclusive* option to srun (see [srun](srun.md#OPT_exclusive)(1) for more details), which allows users to specify that they would like their nodes to be allocated in exclusive mode. This is to accommodate users who might have mpi/threaded/openMP programs that will take advantage of all the CPUs on a node but only need one mpi process per node.
