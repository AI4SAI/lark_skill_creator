# Core Specialization

Core specialization is a feature designed to isolate system overhead (system interrupts, etc.) to designated cores on a compute node. This can reduce context switching in applications to improve completion time. The job processes will not be able to directly use the specialized cores.

## Command Options {#command}

All job allocation commands (*salloc*, *sbatch* and *srun*) accept the *-S* or *\--core-spec* option with a core count value argument (e.g. \"-S 1\" or \"\--core-spec=2\"). The count identifies the number of cores to be reserved for system overhead on each allocated compute node. Note that the *\--core-spec* option will be ignored if **AllowSpecResourcesUsage** is not enabled in your slurm.conf. Each job\'s core specialization count can be viewed using the *scontrol*, *sview* or *squeue* command. Specification of a core specialization count for a job step is ignored (i.e. for the *srun* command within a job allocation created using the *salloc* or *sbatch* command). Use the *squeue* command with the \"%X\" format option to see the count (it is not reported in the default output format). The *scontrol* and *sview* commands can also be used to modify the count for pending jobs.

Explicitly setting a job\'s specialized core value implicitly sets its *\--exclusive* option, reserving entire nodes for the job. The job will be charged for all non-specialized CPUs on the node and the job\'s NumCPUs value reported by the *scontrol*, *sview* and *squeue* commands will reflect all non-specialized CPUS on all allocated nodes as will the job\'s accounting.

Note that, due to the implicit \--exclusive, if the requested specialized core/thread count is lower than the number of cores in the CoreSpecCount or in the CpuSpecList of the allocated node, then the step will have access to all of the non-specialized cores as well as the specialized cores freed for this job.

For example, suppose a node has **AllowSpecResourcesUsage=yes** and **CoreSpecCount=2** configured in the slurm.conf for a node with a total of 16 Cores. If a job specified **\--core-spec=1**, the implicit **\--exclusive** would lead to an exclusive allocation of the node, leaving 15 cores for use by the job, and keeping 1 core for system use.

In *sacct*, the step\'s allocated CPUs will include the specialized cores or threads that it has access to. However, the job\'s allocated CPU count never includes specialized cores or threads to ensure that utilization reports are accurate.

Here is an example configuration, setting cores 0 and 1 as specialized:

    AllowSpecResourcesUsage=yes
    Nodename=n0 Port=10100 CoresPerSocket=16 ThreadsPerCore=1 CpuSpecList=0-1

Submit a job requesting a core spec count of 1 (freeing up core number 1 for job use).

    $ salloc --core-spec=1
    salloc: Granted job allocation 4152
    $ srun bash -c 'cat /proc/self/status |grep Cpus_'
    Cpus_allowed:        fffe
    Cpus_allowed_list:   1-15

Notice the job CPU count vs the step CPU count.

    $ sacct -j 4152 -ojobid%20,alloccpus
                   JobID  AllocCPUS
    -------------------- ----------
                    4152         14
        4152.interactive         15
                  4152.0         15

## Core Selection {#core}

The specific resources to be used for specialization may be identified using the *CPUSpecList* configuration parameter associated with each node in the *slurm.conf* file. If *CoreSpecCount* is configured, but not *CPUSpecList*, the cores selected for specialization will follow the assignment algorithm described below . The first core selected will be the highest numbered core on the highest numbered socket. Subsequent cores selected will be the highest numbered core on lower numbered sockets. If additional cores are required, they will come from the next highest numbered cores on each socket. By way of example, consider a node with two sockets, each with four cores. The specialized cores will be selected in the following order:

1.  socket: 1 core: 3
2.  socket: 0 core: 3
3.  socket: 1 core: 2
4.  socket: 0 core: 2
5.  socket: 1 core: 1
6.  socket: 0 core: 1
7.  socket: 1 core: 0
8.  socket: 0 core: 0

Slurm can be configured to specialize the first, rather than the last cores by configuring SchedulerParameters=spec_cores_first. In that case, the first core selected will be the lowest numbered core on the lowest numbered socket. Subsequent cores selected will be the lowest numbered core on higher numbered sockets. If additional cores are required, they well come from the next lowest numbered cores on each socket.

Note that core specialization reservation may impact the use of some job allocation request options, especially \--cores-per-socket.

## System Configuration {#system}

Core specialization requires SelectType=cons_tres and the *task/cgroup* TaskPlugin. Specialized resources should be configured in slurm.conf on the node specification line using the *CoreSpecCount* or *CPUSpecList* options to identify the CPUs to reserve. The *MemSpecLimit* option can be used to reserve memory. These resources will be reserved using Linux cgroups. The compute node daemon, slurmd, will be constrained to the reserved resources unless *TaskPluginParam* *SlurmdOffSpec* is specified. If cgroup/v1 is used, the slurmstepd processes will also be constrained to the reserved resources. Users wanting a different number of specialized cores should use the *\--core-spec* option as described above.

A job\'s core specialization option will be silently cleared on other configurations. In addition, each compute node\'s core count must be configured or the CPUs count must be configured to the node\'s core count. If the core count is not configured and the CPUs value is configured to the count of hyperthreads, then hyperthreads rather than cores will be reserved for system use.

If users are to be granted the right to control the number of specialized cores for their job, the configuration parameter *AllowSpecResourcesUsage* must be set to a value of *1*.
