# Gang Scheduling

Slurm supports timesliced gang scheduling in which two or more jobs are allocated to the same resources in the same partition and these jobs are alternately suspended to let one job at a time have dedicated access to the resources for a configured period of time.\
Slurm also supports preemptive job scheduling that allows a job in a higher *PriorityTier* partition, or in a preempting QOS, to preempt other jobs. [Preemption](preempt.md) is related to Gang scheduling because SUSPEND is one of the *PreemptionMode*s, and it uses the Gang scheduler to resume suspended jobs.

A workload manager that supports timeslicing can improve responsiveness and utilization by allowing more jobs to begin running sooner. Shorter-running jobs no longer have to wait in a queue behind longer-running jobs. Instead they can be run \"in parallel\" with the longer-running jobs, which will allow them to start and finish quicker. Throughput is also improved because overcommitting the resources provides opportunities for \"local backfilling\" to occur (see example below).

The gang scheduling logic works on each partition independently. If a new job has been allocated to resources in a partition that have already been allocated to an existing job, then the plugin will suspend the new job until the configured *SchedulerTimeslice* interval has elapsed. Then it will suspend the running job and let the new job make use of the resources for a *SchedulerTimeslice* interval. This will continue until one of the jobs terminates.

**NOTE**: Heterogeneous jobs are excluded from gang scheduling operations.

## Configuration {#config}

There are several important configuration parameters relating to gang scheduling:

- **SelectType**: The Slurm gang scheduler supports nodes allocated by the *select/linear* plugin, socket/core/CPU resources allocated by the *select/cons_tres* plugin.
- **SelectTypeParameters**: Since resources will be getting overallocated with jobs (suspended jobs remain in memory), the resource selection plugin should be configured to track the amount of memory used by each job to ensure that memory page swapping does not occur. When *select/linear* is chosen, we recommend setting *SelectTypeParameters=CR_Memory*. When *select/cons_tres* is chosen, we recommend including Memory as a resource (e.g. *SelectTypeParameters=CR_Core_Memory*).
- **DefMemPerCPU**: Since job requests may not explicitly specify a memory requirement, we also recommend configuring *DefMemPerCPU* (default memory per allocated CPU) or *DefMemPerNode* (default memory per allocated node). It may also be desirable to configure *MaxMemPerCPU* (maximum memory per allocated CPU) or *MaxMemPerNode* (maximum memory per allocated node) in *slurm.conf*. Users can use the *\--mem* or *\--mem-per-cpu* option at job submission time to specify their memory requirements. Note that in order to gang schedule jobs, all jobs must be able to fit into memory at the same time.
- **JobAcctGatherType and JobAcctGatherFrequency**: If you wish to enforce memory limits, either that task/cgroup must be configured to limit each job\'s memory use or accounting must be enabled using the *JobAcctGatherType* and *JobAcctGatherFrequency* parameters. If accounting is enabled and a job exceeds its configured memory limits, it will be canceled in order to prevent it from adversely affecting other jobs sharing the same resources.
- **PreemptMode**: set the *GANG* option. See the *slurm.conf* manpage for other options that may be specified to enable job [preemption](preempt.md) in addition to GANG. In order to use gang scheduling, the **GANG** option must be specified at the cluster level.\
  **NOTE**: Gang scheduling is performed independently for each partition, so if you only want time-slicing by *OverSubscribe*, without any preemption, then configuring partitions with overlapping nodes is not recommended. On the other hand, if you want to use *PreemptType=preempt/partition_prio* to allow jobs from higher *PriorityTier* partitions to Suspend jobs from lower *PriorityTier* partitions, then you will need overlapping partitions, and *PreemptMode=SUSPEND,GANG* to use the Gang scheduler to resume the suspended job(s). In any case, time-slicing won\'t happen between jobs on different partitions.
- **SchedulerTimeSlice**: The default timeslice interval is 30 seconds. To change this duration, set *SchedulerTimeSlice* to the desired interval (in seconds) in *slurm.conf*. For example, to set the timeslice interval to one minute, set *SchedulerTimeSlice=60*. Short values can increase the overhead of gang scheduling.
- **OverSubscribe**: Configure the partition\'s *OverSubscribe* setting to *FORCE* for all partitions in which timeslicing is to take place. The *FORCE* option supports an additional parameter that controls how many jobs can share a compute resource (FORCE\[:max_share\]). By default the max_share value is 4. To allow up to 6 jobs from this partition to be allocated to a common resource, set *OverSubscribe=FORCE:6*. To only let 2 jobs timeslice on the same resources, set *OverSubscribe=FORCE:2*.

In order to enable gang scheduling after making the configuration changes described above, restart Slurm if it is already running. Any change to the plugin settings in Slurm requires a full restart of the daemons. If you just change the partition *OverSubscribe* setting, this can be updated with *scontrol reconfig*.

## Timeslicer Design and Operation {#time_slice}

When enabled, the gang scheduler keeps track of the resources allocated to all jobs. For each partition an \"active bitmap\" is maintained that tracks all concurrently running jobs in the Slurm cluster. Each time a new job is allocated to resources in a partition, the gang scheduler compares these newly allocated resources with the resources already maintained in the \"active bitmap\". If these two sets of resources are disjoint then the new job is added to the \"active bitmap\". If these two sets of resources overlap then the new job is suspended. All jobs are tracked in a per-partition job queue within the gang scheduler logic.

A separate *timeslicer thread* is spawned by the gang scheduler on startup. This thread sleeps for the configured *SchedulerTimeSlice* interval. When it wakes up, it checks each partition for suspended jobs. If suspended jobs are found then the *timeslicer thread* moves all running jobs to the end of the job queue. It then reconstructs the \"active bitmap\" for this partition beginning with the suspended job that has waited the longest to run (this will be the first suspended job in the run queue). Each following job is then compared with the new \"active bitmap\", and if the job can be run concurrently with the other \"active\" jobs then the job is added. Once this is complete then the *timeslicer thread* suspends any currently running jobs that are no longer part of the \"active bitmap\", and resumes jobs that are new to the \"active bitmap\".

This *timeslicer thread* algorithm for rotating jobs is designed to prevent jobs from starving (remaining in the suspended state indefinitely) and to be as fair as possible in the distribution of runtime while still keeping all of the resources as busy as possible.

The gang scheduler suspends jobs via the same internal functions that support *scontrol suspend* and *scontrol resume*. A good way to observe the operation of the timeslicer is by running *squeue -i\<time\>* in a terminal window where *time* is set equal to *SchedulerTimeSlice*.

## A Simple Example {#example1}

The following example is configured with *select/linear* and *OverSubscribe=FORCE*. This example takes place on a small cluster of 5 nodes:

    [user@n16 load]$ sinfo
    PARTITION AVAIL  TIMELIMIT NODES  STATE NODELIST
    active*      up   infinite     5   idle n[12-16]

Here are the Scheduler settings (excerpt of output):

    [user@n16 load]$ scontrol show config
    ...
    PreemptMode             = GANG
    ...
    SchedulerTimeSlice      = 30
    SchedulerType           = sched/builtin
    ...

The *myload* script launches a simple load-generating app that runs for the given number of seconds. Submit *myload* to run on all nodes:

    [user@n16 load]$ sbatch -N5 ./myload 300
    sbatch: Submitted batch job 3

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
        3    active  myload  user     0:05     5 n[12-16]

Submit it again and watch the gang scheduler suspend it:

    [user@n16 load]$ sbatch -N5 ./myload 300
    sbatch: Submitted batch job 4

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
        3    active  myload  user  R  0:13     5 n[12-16]
        4    active  myload  user  S  0:00     5 n[12-16]

After 30 seconds the gang scheduler swaps jobs, and now job 4 is the active one:

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
        4    active  myload  user  R  0:08     5 n[12-16]
        3    active  myload  user  S  0:41     5 n[12-16]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
        4    active  myload  user  R  0:21     5 n[12-16]
        3    active  myload  user  S  0:41     5 n[12-16]

After another 30 seconds the gang scheduler sets job 3 running again:

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
        3    active  myload  user  R  0:50     5 n[12-16]
        4    active  myload  user  S  0:30     5 n[12-16]

**A possible side effect of timeslicing**: Note that jobs that are immediately suspended may cause their *srun* commands to produce the following output:

    [user@n16 load]$ cat slurm-4.out
    srun: Job step creation temporarily disabled, retrying
    srun: Job step creation still disabled, retrying
    srun: Job step creation still disabled, retrying
    srun: Job step creation still disabled, retrying
    srun: Job step created

This occurs because *srun* is attempting to launch a jobstep in an allocation that has been suspended. The *srun* process will continue in a retry loop to launch the jobstep until the allocation has been resumed and the jobstep can be launched.

When the gang scheduler is enabled, this type of output in the user jobs should be considered benign.

## More examples {#example2}

The following example shows how the timeslicer algorithm keeps the resources busy. Job 10 runs continually, while jobs 9 and 11 are timesliced:

    [user@n16 load]$ sbatch -N3 ./myload 300
    sbatch: Submitted batch job 9

    [user@n16 load]$ sbatch -N2 ./myload 300
    sbatch: Submitted batch job 10

    [user@n16 load]$ sbatch -N3 ./myload 300
    sbatch: Submitted batch job 11

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
        9    active  myload  user  R  0:11     3 n[12-14]
       10    active  myload  user  R  0:08     2 n[15-16]
       11    active  myload  user  S  0:00     3 n[12-14]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       10    active  myload  user  R  0:50     2 n[15-16]
       11    active  myload  user  R  0:12     3 n[12-14]
        9    active  myload  user  S  0:41     3 n[12-14]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       10    active  myload  user  R  1:04     2 n[15-16]
       11    active  myload  user  R  0:26     3 n[12-14]
        9    active  myload  user  S  0:41     3 n[12-14]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
        9    active  myload  user  R  0:46     3 n[12-14]
       10    active  myload  user  R  1:13     2 n[15-16]
       11    active  myload  user  S  0:30     3 n[12-14]

The next example displays \"local backfilling\":

    [user@n16 load]$ sbatch -N3 ./myload 300
    sbatch: Submitted batch job 12

    [user@n16 load]$ sbatch -N5 ./myload 300
    sbatch: Submitted batch job 13

    [user@n16 load]$ sbatch -N2 ./myload 300
    sbatch: Submitted batch job 14

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       12    active  myload  user  R  0:14     3 n[12-14]
       14    active  myload  user  R  0:06     2 n[15-16]
       13    active  myload  user  S  0:00     5 n[12-16]

Without timeslicing and without the backfill scheduler enabled, job 14 has to wait for job 13 to finish.

This is called \"local\" backfilling because the backfilling only occurs with jobs close enough in the queue to get allocated by the scheduler as part of oversubscribing the resources. Recall that the number of jobs that can overcommit a resource is controlled by the *OverSubscribe=FORCE:max_share* value, so this value effectively controls the scope of \"local backfilling\".

Normal backfill algorithms check [all]{.underline} jobs in the wait queue.

## Consumable Resource Examples {#example3}

The following two examples illustrate the primary difference between *CR_CPU* and *CR_Core* when consumable resource selection is enabled (*select/cons_tres*).

When *CR_CPU* (or *CR_CPU_Memory*) is configured then the selector treats the CPUs as simple, *interchangeable* computing resources [unless]{.underline} task affinity is enabled. However when task affinity is enabled with *CR_CPU* or *CR_Core* (or *CR_Core_Memory*) is enabled, the selector treats the CPUs as individual resources that are [specifically]{.underline} allocated to jobs. This subtle difference is highlighted when timeslicing is enabled.

In both examples 6 jobs are submitted. Each job requests 2 CPUs per node, and all of the nodes contain two quad-core processors. The timeslicer will initially let the first 4 jobs run and suspend the last 2 jobs. The manner in which these jobs are timesliced depends upon the configured *SelectTypeParameters*.

In the first example *CR_Core_Memory* is configured. Note that jobs 46 and 47 don\'t [ever]{.underline} get suspended. This is because they are not sharing their cores with any other job. Jobs 48 and 49 were allocated to the same cores as jobs 44 and 45. The timeslicer recognizes this and timeslices only those jobs:

    [user@n16 load]$ sinfo
    PARTITION AVAIL  TIMELIMIT NODES  STATE NODELIST
    active*      up   infinite     5   idle n[12-16]

    [user@n16 load]$ scontrol show config | grep Select
    SelectType              = select/cons_tres
    SelectTypeParameters    = CR_CORE_MEMORY

    [user@n16 load]$ sinfo -o "%20N %5D %5c %5z"
    NODELIST             NODES CPUS  S:C:T
    n[12-16]             5     8     2:4:1

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 44

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 45

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 46

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 47

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 48

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 49

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       44    active  myload  user  R  0:09     5 n[12-16]
       45    active  myload  user  R  0:08     5 n[12-16]
       46    active  myload  user  R  0:08     5 n[12-16]
       47    active  myload  user  R  0:07     5 n[12-16]
       48    active  myload  user  S  0:00     5 n[12-16]
       49    active  myload  user  S  0:00     5 n[12-16]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       46    active  myload  user  R  0:49     5 n[12-16]
       47    active  myload  user  R  0:48     5 n[12-16]
       48    active  myload  user  R  0:06     5 n[12-16]
       49    active  myload  user  R  0:06     5 n[12-16]
       44    active  myload  user  S  0:44     5 n[12-16]
       45    active  myload  user  S  0:43     5 n[12-16]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       44    active  myload  user  R  1:23     5 n[12-16]
       45    active  myload  user  R  1:22     5 n[12-16]
       46    active  myload  user  R  2:22     5 n[12-16]
       47    active  myload  user  R  2:21     5 n[12-16]
       48    active  myload  user  S  1:00     5 n[12-16]
       49    active  myload  user  S  1:00     5 n[12-16]

Note the runtime of all 6 jobs in the output of the last *squeue* command. Jobs 46 and 47 have been running continuously, while jobs 44 and 45 are splitting their runtime with jobs 48 and 49.

The next example has *CR_CPU_Memory* configured and the same 6 jobs are submitted. Here the selector and the timeslicer treat the CPUs as countable resources which results in all 6 jobs sharing time on the CPUs:

    [user@n16 load]$ sinfo
    PARTITION AVAIL  TIMELIMIT NODES  STATE NODELIST
    active*      up   infinite     5   idle n[12-16]

    [user@n16 load]$ scontrol show config | grep Select
    SelectType              = select/cons_tres
    SelectTypeParameters    = CR_CPU_MEMORY

    [user@n16 load]$ sinfo -o "%20N %5D %5c %5z"
    NODELIST             NODES CPUS  S:C:T
    n[12-16]             5     8     2:4:1

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 51

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 52

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 53

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 54

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 55

    [user@n16 load]$ sbatch -n10 -N5 ./myload 300
    sbatch: Submitted batch job 56

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       51    active  myload  user  R  0:11     5 n[12-16]
       52    active  myload  user  R  0:11     5 n[12-16]
       53    active  myload  user  R  0:10     5 n[12-16]
       54    active  myload  user  R  0:09     5 n[12-16]
       55    active  myload  user  S  0:00     5 n[12-16]
       56    active  myload  user  S  0:00     5 n[12-16]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       51    active  myload  user  R  1:09     5 n[12-16]
       52    active  myload  user  R  1:09     5 n[12-16]
       55    active  myload  user  R  0:23     5 n[12-16]
       56    active  myload  user  R  0:23     5 n[12-16]
       53    active  myload  user  S  0:45     5 n[12-16]
       54    active  myload  user  S  0:44     5 n[12-16]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       53    active  myload  user  R  0:55     5 n[12-16]
       54    active  myload  user  R  0:54     5 n[12-16]
       55    active  myload  user  R  0:40     5 n[12-16]
       56    active  myload  user  R  0:40     5 n[12-16]
       51    active  myload  user  S  1:16     5 n[12-16]
       52    active  myload  user  S  1:16     5 n[12-16]

    [user@n16 load]$ squeue
    JOBID PARTITION    NAME  USER ST  TIME NODES NODELIST
       51    active  myload  user  R  3:18     5 n[12-16]
       52    active  myload  user  R  3:18     5 n[12-16]
       53    active  myload  user  R  3:17     5 n[12-16]
       54    active  myload  user  R  3:16     5 n[12-16]
       55    active  myload  user  S  3:00     5 n[12-16]
       56    active  myload  user  S  3:00     5 n[12-16]

Note that the runtime of all 6 jobs is roughly equal. Jobs 51-54 ran first so they\'re slightly ahead, but so far all jobs have run for at least 3 minutes.

At the core level this means that Slurm relies on the Linux kernel to move jobs around on the cores to maximize performance. This is different than when *CR_Core_Memory* was configured and the jobs would effectively remain \"pinned\" to their specific cores for the duration of the job. Note that *CR_Core_Memory* supports CPU binding, while *CR_CPU_Memory* does not.

Note that manually suspending a job (i.e. \"scontrol suspend \...\") releases its CPUs for allocation to other jobs. Resuming a previously suspended job may result in multiple jobs being allocated the same CPUs, which could trigger gang scheduling of jobs. Use of the scancel command to send SIGSTOP and SIGCONT signals would stop a job without releasing its CPUs for allocation to other jobs and would be a preferable mechanism in many cases.
