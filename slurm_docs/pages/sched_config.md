# Scheduling Configuration Guide

## Overview

Slurm is designed to perform a quick and simple scheduling attempt at events such as job submission or completion and configuration changes. During these event-triggered scheduling events, **default_queue_depth** (default is 100) number of jobs will be considered.

At less frequent intervals, defined by **sched_interval**, the main scheduling loop will run, considering all jobs while still honoring the **partition_job_depth** limit.

In both cases, jobs are evaluated in a strict priority order and once any job or job array task in a partition is left pending, no other jobs in that partition will be scheduled to avoid taking resources from the higher-priority pending job.

A more comprehensive scheduling attempt is typically done by the backfill scheduling plugin, which considers job run time and resources required to determine if lower-priority jobs would actually take resources needed by higher-priority jobs. This allows the backfill scheduler to assign more specific [reasons](job_reason_codes.md) to pending jobs, or to start jobs that were previously pending.

## Scheduling Configuration {#config}

The **SchedulerType** configuration parameter specifies the scheduler plugin to use. Options are sched/backfill, which performs backfill scheduling, and sched/builtin, which attempts to schedule jobs in a strict priority order within each partition/queue.

There is also a **SchedulerParameters** configuration parameter which can specify a wide range of parameters as described below. This first set of parameters applies to all scheduling configurations. See the [slurm.conf(5)](slurm.conf.md) man page for more details.

- **default_queue_depth=#** - Specifies the number of jobs to consider for scheduling on each event that may result in a job being scheduled. Default value is 100 jobs. Since this happens frequently, a relatively small number is generally best.
- **defer** - Do not attempt to schedule jobs individually at submit time. Can be useful for high-throughput computing.
- **max_switch_wait=#** - Specifies the maximum time a job can wait for desired number of leaf switches. Default value is 300 seconds.
- **partition_job_depth=#** - Specifies how many jobs are tested in any single partition, default value is 0 (no limit).
- **sched_interval=#** - Specifies how frequently, in seconds, the main scheduling loop will execute and test all pending jobs, with the **partition_job_depth** limit in place. The default value is 60 seconds.

## Backfill Scheduling {#backfill}

The backfill scheduling plugin is loaded by default. Without backfill scheduling, each partition is scheduled strictly in priority order, which typically results in significantly lower system utilization and responsiveness than otherwise possible. Backfill scheduling will start lower priority jobs if doing so does not delay the expected start time of **any** higher priority jobs. Since the expected start time of pending jobs depends upon the expected completion time of running jobs, reasonably accurate time limits are important for backfill scheduling to work well.

Slurm\'s backfill scheduler takes into consideration every running job. It then considers pending jobs in priority order, determining when and where each will start, taking into consideration the possibility of [job preemption](preempt.md), [gang scheduling](gang_scheduling.md), [generic resource (GRES) requirements](gres.md), memory requirements, etc. If the job under consideration can start immediately without impacting the expected start time of any higher priority job, then it does so. Otherwise the resources required by the job will be reserved during the job\'s expected execution time. The backfill plugin will set the expected start time for pending jobs setting these reserved nodes into a **\'Planned\'** state. A job\'s expected start time can be seen using the **squeue \--start** command. For performance reasons, the backfill scheduler reserves whole nodes for jobs, even if jobs don\'t require whole nodes.

The scheduling logic builds a sorted list of job-partition pairs. Jobs submitted to multiple partitions will have as many entries in the list as requested partitions. By default, the backfill scheduler may evaluate all the job-partition pairs for a single job, potentially reserving resources for each pair, but only starting the job in the reservation offering the earliest start time.

Having a single job reserving resources for multiple partitions could impede other jobs (or hetjob components) from reserving resources already reserved for the partitions that don\'t offer the earliest start time. A single job that requests multiple partitions can also prevent itself from starting earlier in a lower priority partition if the partitions overlap nodes and a backfill reservation in the higher priority partition blocks nodes that are also in the lower priority partition.

Backfill scheduling is difficult without reasonable time limit estimates for jobs, but some configuration parameters that can help.

- **DefaultTime** - Default job time limit (specify value by partition)
- **MaxTime** - Maximum job time limit (specify value by partition)
- **OverTimeLimit** - Amount by which a job can exceed its time limit before it is killed. A system-wide configuration parameter.

Backfill scheduling is a time consuming operation. Locks are released briefly every two seconds so that other options can be processed, for example to process new job submission requests. Backfill scheduling can optionally continue execution after the lock release and ignore newly submitted jobs (**SchedulerParameters=bf_continue**). Doing so will permit consideration of more jobs, but may result in the delayed scheduling of newly submitted jobs. A partial list of **SchedulerParameters** configuration parameters related to backfill scheduling follows. For more details and a complete list of the backfill related SchedulerParameters see the [slurm.conf(5)](slurm.conf.md) man page.

- **bf_continue** - If set, then continue backfill scheduling after periodically releasing locks for other operations.
- **bf_interval=#** - Interval between backfill scheduling attempts. Default value is 30 seconds.
- **bf_max_job_part=#** - Maximum number of jobs to initiate per partition in each backfill cycle. Default value is 0 (no limit).
- **bf_max_job_start=#** - Maximum number of jobs to initiate in each backfill cycle. Default value is 0 (no limit).
- **bf_max_job_test=#** - Maximum number of jobs consider for backfill scheduling in each backfill cycle. Default value is 100 jobs.
- **bf_max_job_user=#** - Maximum number of jobs to initiate per user in each backfill cycle. Default value is 0 (no limit).
- **bf_max_time=#** - Maximum time in seconds the backfill scheduler can spend (including time spent sleeping when locks are released) before discontinuing. The default value is the value of **bf_interval**, which defaults to 30 seconds.
- **bf_one_resv_per_job** - Disallow adding more than one backfill reservation per job. This option makes it so that a job submitted to multiple partitions will stop reserving resources once the first job-partition pair has booked a backfill reservation. Subsequent pairs from the same job will only be tested to start now. This allows for other jobs to be able to book the other pairs resources at the cost of not guaranteeing that the multi-partition job will start in the partition offering the earliest start time (unless it can start immediately). This option is disabled by default.
- **bf_resolution=#** - Time resolution of backfill scheduling. Default value is 60 seconds. Larger values are appropriate if job time limits are imprecise and/or small delays in starting pending jobs in order to achieve higher system utilization is desired.
- **bf_window=#** - How long, in minutes, into the future to look when determining when and where jobs can start. Higher values result in more overhead and less responsiveness. A value at least as long as the highest allowed time limit is generally advisable to prevent job starvation. In order to limit the amount of data managed by the backfill scheduler, if the value of bf_window is increased, then it is generally advisable to also increase **bf_resolution**. The default value is 1440 minutes (one day).
- **bf_yield_interval=#** - The backfill scheduler will periodically relinquish locks in order for other pending operations to take place. This specifies the times when the locks are relinquished in microseconds. The default value is 2,000,000 microseconds (2 seconds). Smaller values may be helpful for high throughput computing when used in conjunction with the bf_continue option.
- **bf_yield_sleep=#** - The backfill scheduler will periodically relinquish locks in order for other pending operations to take place. This specifies the length of time for which the locks are relinquished in microseconds. The default value is 500,000 microseconds (0.5 seconds).
