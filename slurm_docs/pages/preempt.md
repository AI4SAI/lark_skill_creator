# Preemption

Slurm supports job preemption, the act of \"stopping\" one or more \"low-priority\" jobs to let a \"high-priority\" job run. Job preemption is implemented as a variation of Slurm\'s [Gang Scheduling](gang_scheduling.md) logic. When a job that can preempt others is allocated resources that are already allocated to one or more jobs that could be preempted by the first job, the preemptable job(s) are preempted. Based on the configuration the preempted job(s) can be cancelled, or can be requeued and started using other resources, or suspended and resumed once the preemptor job completes, or can even share resources with the preemptor using Gang Scheduling.

The PriorityTier of the Partition of the job or its Quality Of Service (QOS) can be used to identify which jobs can preempt or be preempted by other jobs. Slurm offers the ability to configure the preemption mechanism used on a per partition or per QOS basis. For example, jobs in a low priority queue may get requeued, while jobs in a medium priority queue may get suspended.

## Configuration {#config}

There are several important configuration parameters relating to preemption:

- **SelectType**: Slurm job preemption logic supports nodes allocated by the *select/linear* plugin, socket/core/CPU resources allocated by the *select/cons_tres* plugin.
- **SelectTypeParameter**: Since resources may be getting over-allocated with jobs (suspended jobs remain in memory), the resource selection plugin should be configured to track the amount of memory used by each job to ensure that memory page swapping does not occur. When *select/linear* is chosen, we recommend setting *SelectTypeParameter=CR_Memory*. When *select/cons_tres* is chosen, we recommend including Memory as a resource (e.g. *SelectTypeParameter=CR_Core_Memory*).\
  **NOTE**: Unless *PreemptMode=SUSPEND,GANG* these memory management parameters are not critical.
- **DefMemPerCPU**: Since job requests may not explicitly specify a memory requirement, we also recommend configuring *DefMemPerCPU* (default memory per allocated CPU) or *DefMemPerNode* (default memory per allocated node). It may also be desirable to configure *MaxMemPerCPU* (maximum memory per allocated CPU) or *MaxMemPerNode* (maximum memory per allocated node) in *slurm.conf*. Users can use the *\--mem* or *\--mem-per-cpu* option at job submission time to specify their memory requirements.\
  **NOTE**: Unless *PreemptMode=SUSPEND,GANG* these memory management parameters are not critical.
- **GraceTime**: Specifies a time period for a job to execute after it is selected to be preempted. This option can be specified by partition or QOS using the *slurm.conf* file or database respectively. The *GraceTime* is specified in seconds and the default value is zero, which results in no preemption delay. Once a job has been selected for preemption, its end time is set to the current time plus *GraceTime*. The job is immediately sent SIGCONT and SIGTERM signals in order to provide notification of its imminent termination. This is followed by the SIGCONT, SIGTERM and SIGKILL signal sequence upon reaching its new end time.\
  **NOTE**: This parameter is not used when *PreemptMode=SUSPEND* is configured or when suspending jobs with *scontrol suspend*. For setting the preemption grace time in these cases, see [suspend_grace_time](slurm.conf.md#OPT_suspend_grace_time).
- **JobAcctGatherType and JobAcctGatherFrequency**: The \"maximum data segment size\" and \"maximum virtual memory size\" system limits will be configured for each job to ensure that the job does not exceed its requested amount of memory. If you wish to enable additional enforcement of memory limits, configure job accounting with the *JobAcctGatherType* and *JobAcctGatherFrequency* parameters. When accounting is enabled and a job exceeds its configured memory limits, it will be canceled in order to prevent it from adversely affecting other jobs sharing the same resources.\
  **NOTE**: Unless *PreemptMode=SUSPEND,GANG* these memory management parameters are not critical.
- **PreemptMode**: Mechanism used to preempt jobs or enable gang scheduling. When the *PreemptType* parameter is set to enable preemption, the *PreemptMode* in the main section of slurm.conf selects the default mechanism used to preempt the preemptable jobs for the cluster.\
  *PreemptMode* may be specified on a per partition basis to override this default value if *PreemptType=preempt/partition_prio*. Alternatively, it can be specified on a per QOS basis if *PreemptType=preempt/qos*. In either case, a valid default *PreemptMode* value must be specified for the cluster as a whole when preemption is enabled.\
  The *GANG* option is used to enable gang scheduling independent of whether preemption is enabled (i.e. independent of *PreemptType*). It can be specified in addition to other *PreemptMode* settings, with the two options comma separated (e.g. *PreemptMode=SUSPEND,GANG*).
  - *OFF*: Is the default value and disables job preemption and gang scheduling. It is only compatible with *PreemptType=preempt/none*.
  - *CANCEL*: The preempted job will be cancelled.
  - *GANG*: Enables gang scheduling (time slicing) of jobs in the same partition, and allows the resuming of suspended jobs. In order to use gang scheduling, the **GANG** option must be specified at the cluster level.\
    **NOTE**: If **GANG** scheduling is enabled with *PreemptType=preempt/partition_prio*, the controller will ignore *PreemptExemptTime* and the following *PreemptParameters*: *reorder_count*, *strict_order*, and *youngest_first*.\
    **NOTE**: Gang scheduling is performed independently for each partition, so if you only want time-slicing by *OverSubscribe*, without any preemption, then configuring partitions with overlapping nodes is not recommended. On the other hand, if you want to use *PreemptType=preempt/partition_prio* to allow jobs from higher PriorityTier partitions to Suspend jobs from lower PriorityTier partitions, then you will need overlapping partitions, and *PreemptMode=SUSPEND,GANG* to use Gang scheduler to resume the suspended job(s). In either case, time-slicing won\'t happen between jobs on different partitions.
  - *REQUEUE*: Preempts jobs by requeuing them (if possible) or canceling them. For jobs to be requeued they must have the \"\--requeue\" sbatch option set or the cluster wide JobRequeue parameter in slurm.conf must be set to 1.
  - *SUSPEND*: The preempted jobs will be suspended, and later the Gang scheduler will resume them. Therefore, the *SUSPEND* preemption mode always needs the *GANG* option to be specified at the cluster level. Also, because the suspended jobs will still use memory on the allocated nodes, Slurm needs to be able to track memory resources to be able to suspend jobs.\
    **NOTE**: Because gang scheduling is performed independently for each partition, if using *PreemptType=preempt/partition_prio* then jobs in higher PriorityTier partitions will suspend jobs in lower PriorityTier partitions to run on the released resources. Only when the preemptor job ends then the suspended jobs will be resumed by the Gang scheduler. If *PreemptType=preempt/qos* is configured and if the preempted job(s) and the preemptor job from are on the same partition, then they will share resources with the Gang scheduler (time-slicing). If not (i.e. if the preemptees and preemptor are on different partitions) then the preempted jobs will remain suspended until the preemptor ends.
- **PreemptType**: Specifies the plugin used to identify which jobs can be preempted in order to start a pending job.
  - *preempt/none*: Job preemption is disabled (default).
  - *preempt/partition_prio*: Job preemption is based upon partition *PriorityTier*. Jobs in higher PriorityTier partitions may preempt jobs from lower PriorityTier partitions. This is not compatible with *PreemptMode=OFF*.
  - *preempt/qos*: Job preemption rules are specified by Quality Of Service (QOS) specifications in the Slurm database. In the case of *PreemptMode=SUSPEND*, a preempting job needs to be submitted to a partition with a higher PriorityTier or to the same partition. This option is not compatible with *PreemptMode=OFF*. A configuration of *PreemptMode=SUSPEND* is only supported by the *SelectType=select/cons_tres* plugin. See the [sacctmgr man page](sacctmgr.md) to configure the options of *preempt/qos*.
- **PreemptExemptTime**: Specifies minimum run time of jobs before they are considered for preemption. This is only honored when the *PreemptMode* is set to *REQUEUE* or *CANCEL*. It is specified as a time string: A time of -1 disables the option, equivalent to 0. Acceptable time formats include \"minutes\", \"minutes:seconds\", \"hours:minutes:seconds\", \"days\\-hours\", \"days\\-hours:minutes\", and \"days\\-hours:minutes:seconds\". PreemptEligibleTime is shown in the output of \"scontrol show job \<job id\>\"
- **PriorityTier**: Configure the partition\'s *PriorityTier* setting relative to other partitions to control the preemptive behavior when *PreemptType=preempt/partition_prio*. If two jobs from two different partitions are allocated to the same resources, the job in the partition with the greater *PriorityTier* value will preempt the job in the partition with the lesser *PriorityTier* value. If the *PriorityTier* values of the two partitions are equal then no preemption will occur. The default *PriorityTier* value is 1.\
  **NOTE**: In addition to being used for partition based preemption, *PriorityTier* also has an effect on scheduling. The scheduler will evaluate jobs in the partition(s) with the highest *PriorityTier* before evaluating jobs in other partitions, regardless of which jobs have the highest Priority. The scheduler will consider the job priority when evaluating jobs within the partition(s) with the same *PriorityTier*.
- **OverSubscribe**: Configure the partition\'s *OverSubscribe* setting to *FORCE* for all partitions in which job preemption using a suspend/resume mechanism is used. The *FORCE* option supports an additional parameter that controls how many jobs can oversubscribe a compute resource (FORCE\[:max_share\]). By default the max_share value is 4. In order to preempt jobs (and not gang schedule them), always set max_share to 1. To allow up to 2 jobs from this partition to be allocated to a common resource (and gang scheduled), set *OverSubscribe=FORCE:2*.\
  **NOTE**: *PreemptType=preempt/qos* will permit one additional job to be run on the partition if started due to job preemption. For example, a configuration of *OverSubscribe=FORCE:1* will only permit one job per resource normally, but a second job can be started if done so through preemption based upon QOS.
- **ExclusiveUser**: In partitions with *ExclusiveUser=YES*, jobs will be prevented from preempting or being preempted by any job from any other user. The one exception is that these ExclusiveUser jobs will be able to preempt (but not be preempted by) fully \"\--exclusive\" jobs from other users. This is for the same reason that \"\--exclusive=user\" blocks preemption, but this partition-level setting can only be overridden by making a job fully exclusive.
- **MCSParameters**: If [MCS](mcs.md) labels are set on jobs, preemption will be restricted to other jobs with the same MCS label. If this parameter is configured to use `enforced,select`, MCS labels will be set by default on jobs, causing this restriction to be universal.

To enable preemption after making the configuration changes described above, restart Slurm if it is already running. Any change to the plugin settings in Slurm requires a full restart of the daemons. If you just change the partition *PriorityTier* or *OverSubscribe* setting, this can be updated with *scontrol reconfig*.

If a job request restricts Slurm\'s ability to run jobs from multiple users or accounts on a node by using the \"\--exclusive=user\" or \"\--exclusive=mcs\" job options, the job will be prevented from preempting or being preempted by any job that does not match the user or MCS. The one exception is that these exclusive=user jobs will be able to preempt (but not be preempted by) fully \"\--exclusive\" jobs from other users. If preemption is used, it is generally advisable to disable the \"\--exclusive=user\" and \"\--exclusive=mcs\" job options by using a job_submit plugin (set the value of \"job_desc.shared\" to \"NO_VAL16\").

For heterogeneous job to be considered for preemption all components must be eligible for preemption. When a heterogeneous job is to be preempted the first identified component of the job with the highest order PreemptMode (*SUSPEND* (highest), *REQUEUE*, *CANCEL* (lowest)) will be used to set the PreemptMode for all components. The *GraceTime* and user warning signal for each component of the heterogeneous job remain unique.

Because licenses are not freed when jobs are suspended, jobs using licenses requested by higher priority jobs will only be prempted when PreemptMode is either *REQUEUE* or *CANCEL* and *PreemptParameters=reclaim_licenses* is set.

## Preemption Design and Operation {#operation}

The *SelectType* plugin will identify resources where a pending job can begin execution. When *PreemptMode* is configured to *CANCEL*, *SUSPEND* or *REQUEUE*, the select plugin will also preempt running jobs as needed to initiate the pending job. When *PreemptMode=SUSPEND,GANG* the select plugin will initiate the pending job and rely upon the gang scheduling logic to perform job suspend and resume, as described below.

The select plugin is passed an ordered list of preemptable jobs to consider for each pending job which is a candidate to start. This list is sorted by either:

1.  QOS priority,
2.  Partition priority and job size (to favor preempting smaller jobs), or
3.  Job start time (with *PreemptParameters=youngest_first*).

The select plugin will determine if the pending job can start without preempting any jobs and if so, starts the job using available resources. Otherwise, the select plugin will simulate the preemption of each job in the priority ordered list and test if the job can be started after each preemption. Once the job can be started, the higher priority jobs in the preemption queue will not be considered, but the jobs to be preempted in the original list may be sub-optimal. For example, to start an 8 node job, the ordered preemption candidates may be 2 node, 4 node and 8 node. Preempting all three jobs would allow the pending job to start, but by reordering the preemption candidates it is possible to start the pending job after preempting only one job. To address this issue, the preemption candidates are re-ordered with the final job requiring preemption placed first in the list and all of the other jobs to be preempted ordered by the number of nodes in their allocation which overlap the resources selected for the pending job. In the example above, the 8 node job would be moved to the first position in the list. The process of simulating the preemption of each job in the priority ordered list will then be repeated for the final decision of which jobs to preempt. This two stage process may preempt jobs which are not strictly in preemption priority order, but fewer jobs will be preempted than otherwise required. See the PreemptParameters configuration parameter options of *reorder_count* and *strict_order* for preemption tuning parameters.

When enabled, the gang scheduling logic (which is also supports job preemption) keeps track of the resources allocated to all jobs. For each partition an \"active bitmap\" is maintained that tracks all concurrently running jobs in the Slurm cluster. Each partition also maintains a job list for that partition, and a list of \"shadow\" jobs. The \"shadow\" jobs are high priority job allocations that \"cast shadows\" on the active bitmaps of the low priority jobs. Jobs caught in these \"shadows\" will be preempted.

Each time a new job is allocated to resources in a partition and begins running, the gang scheduler adds a \"shadow\" of this job to all lower priority partitions. The active bitmap of these lower priority partitions are then rebuilt, with the shadow jobs added first. Any existing jobs that were replaced by one or more \"shadow\" jobs are suspended (preempted). Conversely, when a high priority running job completes, its \"shadow\" goes away and the active bitmaps of the lower priority partitions are rebuilt to see if any suspended jobs can be resumed.

The gang scheduler plugin is designed to be *reactive* to the resource allocation decisions made by the \"select\" plugins. The \"select\" plugins have been enhanced to recognize when job preemption has been configured, and to factor in the priority of each partition when selecting resources for a job. When choosing resources for each job, the selector avoids resources that are in use by other jobs (unless sharing has been configured, in which case it does some load-balancing). However, when job preemption is enabled, the select plugins may choose resources that are already in use by jobs from partitions with a lower priority setting, even when sharing is disabled in those partitions.

This leaves the gang scheduler in charge of controlling which jobs should run on the over-allocated resources. If *PreemptMode=SUSPEND*, jobs are suspended using the same internal functions that support *scontrol suspend* and *scontrol resume*. A good way to observe the operation of the gang scheduler is by running *squeue -i\<time\>* in a terminal window.

## Limitations of Preemption During Backfill Scheduling {#limitations}

For performance reasons, the backfill scheduler reserves whole nodes for jobs, not partial nodes. If during backfill scheduling a job preempts one or more other jobs, the whole nodes for those preempted jobs are reserved for the preemptor job, even if the preemptor job requested fewer resources than that. These reserved nodes aren\'t available to other jobs during that backfill cycle, even if the other jobs could fit on the nodes. Therefore, jobs may preempt more resources during a single backfill iteration than they requested.

## A Simple Example {#example1}

The following example is configured with *select/linear* and *PreemptMode=SUSPEND,GANG*. This example takes place on a cluster of 5 nodes:

    [user@n16 ~]$ sinfo
    PARTITION AVAIL  TIMELIMIT NODES  STATE NODELIST
    active*      up   infinite     5   idle n[12-16]
    hipri        up   infinite     5   idle n[12-16]

Here are the Partition settings:

    [user@n16 ~]$ grep PartitionName /shared/slurm/slurm.conf
    PartitionName=DEFAULT OverSubscribe=FORCE:1 Nodes=n[12-16]
    PartitionName=active PriorityTier=1 Default=YES
    PartitionName=hipri  PriorityTier=2

The *runit.pl* script launches a simple load-generating app that runs for the given number of seconds. Submit 5 single-node *runit.pl* jobs to run on all nodes:

    [user@n16 ~]$ sbatch -N1 ./runit.pl 300
    sbatch: Submitted batch job 485
    [user@n16 ~]$ sbatch -N1 ./runit.pl 300
    sbatch: Submitted batch job 486
    [user@n16 ~]$ sbatch -N1 ./runit.pl 300
    sbatch: Submitted batch job 487
    [user@n16 ~]$ sbatch -N1 ./runit.pl 300
    sbatch: Submitted batch job 488
    [user@n16 ~]$ sbatch -N1 ./runit.pl 300
    sbatch: Submitted batch job 489
    [user@n16 ~]$ squeue -Si
    JOBID PARTITION     NAME   USER  ST   TIME  NODES NODELIST
      485    active runit.pl   user   R   0:06      1 n12
      486    active runit.pl   user   R   0:06      1 n13
      487    active runit.pl   user   R   0:05      1 n14
      488    active runit.pl   user   R   0:05      1 n15
      489    active runit.pl   user   R   0:04      1 n16

Now submit a short-running 3-node job to the *hipri* partition:

    [user@n16 ~]$ sbatch -N3 -p hipri ./runit.pl 30
    sbatch: Submitted batch job 490
    [user@n16 ~]$ squeue -Si
    JOBID PARTITION     NAME   USER  ST   TIME  NODES NODELIST
      485    active runit.pl   user   S   0:27      1 n12
      486    active runit.pl   user   S   0:27      1 n13
      487    active runit.pl   user   S   0:26      1 n14
      488    active runit.pl   user   R   0:29      1 n15
      489    active runit.pl   user   R   0:28      1 n16
      490     hipri runit.pl   user   R   0:03      3 n[12-14]

Job 490 in the *hipri* partition preempted jobs 485, 486, and 487 from the *active* partition. Jobs 488 and 489 in the *active* partition remained running.

This state persisted until job 490 completed, at which point the preempted jobs were resumed:

    [user@n16 ~]$ squeue
    JOBID PARTITION     NAME   USER  ST   TIME  NODES NODELIST
      485    active runit.pl   user   R   0:30      1 n12
      486    active runit.pl   user   R   0:30      1 n13
      487    active runit.pl   user   R   0:29      1 n14
      488    active runit.pl   user   R   0:59      1 n15
      489    active runit.pl   user   R   0:58      1 n16

## Another Example {#example2}

In this example we have three different partitions using three different job preemption mechanisms.

    # Excerpt from slurm.conf
    PartitionName=low Nodes=linux Default=YES OverSubscribe=NO      PriorityTier=10 PreemptMode=requeue
    PartitionName=med Nodes=linux Default=NO  OverSubscribe=FORCE:1 PriorityTier=20 PreemptMode=suspend
    PartitionName=hi  Nodes=linux Default=NO  OverSubscribe=FORCE:1 PriorityTier=30 PreemptMode=off

    $ sbatch tmp
    Submitted batch job 94
    $ sbatch -p med tmp
    Submitted batch job 95
    $ sbatch -p hi tmp
    Submitted batch job 96
    $ squeue
      JOBID PARTITION     NAME     USER  ST       TIME  NODES NODELIST(REASON)
         96        hi      tmp      moe   R       0:04      1 linux
         94       low      tmp      moe  PD       0:00      1 (Resources)
         95       med      tmp      moe   S       0:02      1 linux
    (after job 96 completes)
    $ squeue
      JOBID PARTITION     NAME     USER  ST       TIME  NODES NODELIST(REASON)
         94       low      tmp      moe  PD       0:00      1 (Resources)
         95       med      tmp      moe   R       0:24      1 linux

## Another Example {#example3}

In this example we have one partition on which we want to execute only one job per resource (e.g. core) at a time except when a job submitted to the partition from a high priority Quality Of Service (QOS) is submitted. In that case, we want that second high priority job to be started and be gang scheduled with the other jobs on overlapping resources.

    # Excerpt from slurm.conf
    PreemptMode=Suspend,Gang
    PreemptType=preempt/qos
    PartitionName=normal Nodes=linux Default=NO  OverSubscribe=FORCE:1

## Future Ideas {#future_work}

**More intelligence in the select plugins**: This implementation of preemption relies on intelligent job placement by the *select* plugins.

Take the following example:

    [user@n8 ~]$ sinfo
    PARTITION AVAIL  TIMELIMIT NODES  STATE NODELIST
    active*      up   infinite     5   idle n[1-5]
    hipri        up   infinite     5   idle n[1-5]
    [user@n8 ~]$ sbatch -N1 -n2 ./sleepme 60
    sbatch: Submitted batch job 17
    [user@n8 ~]$ sbatch -N1 -n2 ./sleepme 60
    sbatch: Submitted batch job 18
    [user@n8 ~]$ sbatch -N1 -n2 ./sleepme 60
    sbatch: Submitted batch job 19
    [user@n8 ~]$ squeue
      JOBID PARTITION     NAME     USER  ST       TIME  NODES NODELIST(REASON)
         17    active  sleepme  cholmes   R       0:03      1 n1
         18    active  sleepme  cholmes   R       0:03      1 n2
         19    active  sleepme  cholmes   R       0:02      1 n3
    [user@n8 ~]$ sbatch -N3 -n6 -p hipri ./sleepme 20
    sbatch: Submitted batch job 20
    [user@n8 ~]$ squeue -Si
      JOBID PARTITION     NAME     USER  ST       TIME  NODES NODELIST(REASON)
         17    active  sleepme  cholmes   S       0:16      1 n1
         18    active  sleepme  cholmes   S       0:16      1 n2
         19    active  sleepme  cholmes   S       0:15      1 n3
         20     hipri  sleepme  cholmes   R       0:03      3 n[1-3]
    [user@n8 ~]$ sinfo
    PARTITION AVAIL  TIMELIMIT NODES  STATE NODELIST
    active*      up   infinite     3  alloc n[1-3]
    active*      up   infinite     2   idle n[4-5]
    hipri        up   infinite     3  alloc n[1-3]
    hipri        up   infinite     2   idle n[4-5]

It would be more ideal if the \"hipri\" job were placed on nodes n\[3-5\], which would allow jobs 17 and 18 to continue running. However, a new \"intelligent\" algorithm would have to include factors such as job size and required nodes in order to support ideal placements such as this, which can quickly complicate the design. Any and all help is welcome here!
