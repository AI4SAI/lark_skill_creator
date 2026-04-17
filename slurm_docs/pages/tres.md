# Trackable RESources (TRES)

A TRES is a resource that can be tracked for usage or used to enforce limits against. A TRES is a combination of a Type and a Name. Types are predefined. Current TRES Types are:

- BB (burst buffers)
- Billing
- CPU
- Energy
- FS (filesystem)
- GRES
- IC (interconnect)
- License
- Mem (Memory)
- Node
- Pages
- VMem (Virtual Memory/Size)

The Billing TRES is calculated from a partition\'s TRESBillingWeights. See below for details.

Valid \'FS\' TRES are \'disk\' (local disk) and \'lustre\'. These are primarily there for reporting usage, not limiting access.

Valid \'IC\' TRES is \'ofed\'. These are primarily there for reporting usage, not limiting access.

## slurm.conf settings {#conf}

### TRES Tracking {#AccountingStorageTRES}

**AccountingStorageTRES**\
Used to define which TRES are to be tracked on the system. By default Billing, CPU, Energy, Memory, Node, FS/Disk, Pages and VMem are tracked. These default TRES cannot be disabled, but only appended to. The following example:

    AccountingStorageTRES=gres/gpu,license/iop1

will track billing, cpu, energy, memory, nodes, fs/disk, pages and vmem along with a GRES called gpu, as well as a license called iop1. Whenever these resources are used on the cluster they are recorded. TRES are automatically set up in the database on the start of the slurmctld.

The TRES that require associated names are BB, GRES, and License. As seen in the above example, GRES and License are typically different on each system. The BB TRES is named the same as the burst buffer plugin being used. In the above example we are using the *Cray* burst buffer plugin.

When including a specific GRES with a subtype, it is also recommended to include its generic type, otherwise a request with only the generic one won\'t be accounted for. For example, if we want to account for gres/gpu:tesla, we would also include gres/gpu for accounting gpus in requests like *srun \--gres=gpu:1*.

    AccountingStorageTRES=gres/gpu,gres/gpu:tesla

**NOTE**: Setting gres/gpu will also set gres/gpumem and gres/gpuutil. gres/gpumem and gres/gpuutil can be set individually when gres/gpu is not set.

### Priority Weights {#PriorityWeightTRES}

**PriorityWeightTRES**\
A comma separated list of TRES Types and weights that sets the degree that each TRES Type contributes to the job\'s priority.

    PriorityWeightTRES=CPU=1000,Mem=2000,GRES/gpu=3000

Applicable only if PriorityType=priority/multifactor and if AccountingStorageTRES is configured with each TRES Type. The default values are 0.

The Billing TRES is not available for priority calculations because the number isn\'t generated until after the job has been allocated resources --- since the number can change for different partitions.

### Billing Weights {#TRESBillingWeights}

**TRESBillingWeights**\
Comma-separated list of `<TRES Type>=<Numeric Weight>` pairs defining the billing weights of one or more tracked TRES types that will be used in calculating the usage of a job in each partition. The resulting usage amount is used when calculating [fairshare](priority_multifactor.md#fairshare) and when enforcing any [resource limits](resource_limits.md) that are configured for the **billing** TRES. See also [PriorityWeightTRES](slurm.conf.md#OPT_PriorityWeightTRES) to adjust job priority directly based on TRES usage.

Any TRES type tracked by [AccountingStorageTRES](slurm.conf.md#OPT_AccountingStorageTRES) is available for billing, except the **billing** TRES which is ignored since it is the result of this weighted calculation.

By default, jobs are billed against the total number of allocated CPUs i.e., `TRESBillingWeights="CPU=1"`.

The weighted amount of a resource can be adjusted by adding a suffix of `[KMGTP]` after the billing weight. The base unit for memory and burst buffers is Megabytes. For example, a memory weight of `mem=0.25` on a job allocated 8GB will result in 2048 billed units (8192MB \* 0.25). A memory weight of `mem=0.25G` on the same job will result in 2 billed units ((8192MB/1024) \* 0.25).

By default the billing of TRES is calculated as the sum of all TRES types multiplied by their corresponding billing weight. For example, consider a partition with these billing weights configured:

    TRESBillingWeights="CPU=1.0,Mem=0.25G,GRES/gpu=2.0,license/licA=1.5"

A job in this partition that gets allocated 1 CPU and 8 GB of memory would be billed as:

    (1*1.0) + (8*0.25) + (0*2.0) + (0*1.5) = 3.0

Note that TRES weights may be floating-point/decimal values, and that this precision will be retained during the billing calculation. However, the final billing amount is stored as an integer and truncated if needed. For example, consider how adding a license or adding additional memory and a license to the above example job would affect the billed amount:

    (1*1.0) + (8*0.25) + (0*2.0) + (1*1.5) = 4.5 => 4
    (1*1.0) + (10*0.25) + (0*2.0) + (1*1.5) = 5.0 => 5

### Priority Flags {#PriorityFlags}

Two of the available **PriorityFlags** relate to the interpretation of the **TRESBillingWeights** field.

**PriorityFlags=MAX_TRES**\
If this flag is set, the billable TRES is calculated as the sum of the following:

- MAX of individual TRESs (those tied to a specific node, e.g., cpus, mem, gres)
- SUM of all global TRESs (those available on any nodes, e.g., licenses)

Using the same example above, the billable TRES will be:

    MAX(1*1.0, 8*0.25, 0*2.0) + (0*1.5) = 2.0

**PriorityFlags=MAX_TRES_GRES**\
If this flag is set, the billable TRES is calculated as the sum of the following:

- SUM of all billable GRESs (e.g., GPUs)
- MAX of other individual TRESs (those tied to a specific node, e.g., cpus, mem)
- SUM of all global TRESs (those available on any nodes, e.g., licenses)

With this flag set, the billable TRES will be:

    (0*2.0) + MAX(1*1.0, 8*0.25) + (0*1.5) = 2.0

Adding a GPU to the example job, the billable TRES will be:

    (1*2.0) + MAX(1*1.0, 8*0.25) + (0*1.5) = 3.0

## sacct

sacct can be used to view the TRES of each job by adding \"tres\" to the \--format option.

## sacctmgr

sacctmgr is used to view the various TRES available globally in the system. *sacctmgr show tres* will do this.

## sreport

sreport reports on different TRES. Simply using the comma separated input option *\--tres=* will have sreport generate reports available for the requested TRES types. More information about these reports can be found on the [sreport manpage](sreport.md).

In *sreport*, the \"Reported\" Billing TRES is calculated from the largest Billing TRES of each node multiplied by the time frame. For example, if a node is part of multiple partitions and each has a different TRESBillingWeights defined the Billing TRES for the node will be the highest of the partitions. If TRESBillingWeights is not defined on any partition for a node then the Billing TRES will be equal to the number of CPUs on the node.
