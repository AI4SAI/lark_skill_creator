# Prolog and Epilog Guide

Slurm supports a multitude of prolog and epilog programs. Note that for security reasons, these programs do not have a search path set. Either specify fully qualified path names in the program or set the [PATH]{.commandline} environment variable. The first table below identifies what prologs and epilogs are available for job allocations, when and where they run.

+-----------------------------------+-----------------------------------------+------------------+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| **Parameter**                     | **Location**                            | **Invoked by**   | **User**                        | **When executed**                                                                                                                    |
+-----------------------------------+-----------------------------------------+------------------+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Prolog (from slurm.conf)          | Compute node                            | slurmd daemon    | SlurmdUser (normally user root) | First job or job step initiation on that node (by default); PrologFlags=Alloc will force the script to be executed at job allocation |
+-----------------------------------+-----------------------------------------+------------------+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| PrologSlurmctld (from slurm.conf) | Head node (where slurmctld daemon runs) | slurmctld daemon | SlurmctldUser                   | At job allocation                                                                                                                    |
+-----------------------------------+-----------------------------------------+------------------+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Epilog (from slurm.conf)          | Compute node                            | slurmd daemon    | SlurmdUser (normally user root) | At job termination                                                                                                                   |
+-----------------------------------+-----------------------------------------+------------------+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| EpilogSlurmctld (from slurm.conf) | Head node (where slurmctld daemon runs) | slurmctld daemon | SlurmctldUser                   | At job termination                                                                                                                   |
+-----------------------------------+-----------------------------------------+------------------+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

\

This second table below identifies what prologs and epilogs are available for job step allocations, when and where they run.

+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+
| **Parameter**                                  | **Location**         | **Invoked by**    | **User**                   | **When executed**           |
+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+
| SrunProlog (from slurm.conf) or srun \--prolog | srun invocation node | srun command      | User invoking srun command | Prior to launching job step |
+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+
| TaskProlog (from slurm.conf)                   | Compute node         | slurmstepd daemon | User invoking srun command | Prior to launching job step |
+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+
| srun \--task-prolog                            | Compute node         | slurmstepd daemon | User invoking srun command | Prior to launching job step |
+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+
| TaskEpilog (from slurm.conf)                   | Compute node         | slurmstepd daemon | User invoking srun command | Completion job step         |
+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+
| srun \--task-epilog                            | Compute node         | slurmstepd daemon | User invoking srun command | Completion job step         |
+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+
| SrunEpilog (from slurm.conf) or srun \--epilog | srun invocation node | srun command      | User invoking srun command | Completion job step         |
+------------------------------------------------+----------------------+-------------------+----------------------------+-----------------------------+

By default the Prolog script is only run on any individual node when it first sees a job step from a new allocation; it does not run the Prolog immediately when an allocation is granted. If no job steps from an allocation are run on a node, it will never run the Prolog for that allocation. This Prolog behavior can be changed by the PrologFlags parameter. The Epilog, on the other hand, always runs on every node of an allocation when the allocation is released.

If multiple prolog and/or epilog scripts are specified, (e.g. \"/etc/slurm/prolog.d/\*\") they will run in reverse alphabetical order (z-a -\> Z-A -\> 9-0).

Prolog and Epilog scripts should be designed to be as short as possible and should not call Slurm commands (e.g. squeue, scontrol, sacctmgr, etc). Long running scripts can cause scheduling problems when jobs take a long time to start or finish. Slurm commands in these scripts can potentially lead to performance issues and should not be used.

The task prolog is executed with the same environment as the user tasks to be initiated. The standard output of that program is read and processed as follows:\
[export name=value]{.commandline} sets an environment variable for the user task\
[unset name]{.commandline} clears an environment variable from the user task\
[print \...]{.commandline} writes to the task\'s standard output.\

A TaskProlog script can just be a bash script. Here is a very basic example:

    #!/bin/bash

    # The TaskProlog script can be used for any preliminary work needed
    # before running a job step, and it can also be used to modify the
    # user's environment. There are two main mechanisms for that, which
    # rely on printing commands to stdout:

    # Make a variable available for the user
    echo "export VARIABLE_1=HelloWorld"

    # Unset variables for the user
    echo "unset MANPATH"

    # We can also print messages if needed
    echo "print This message has been printed with TaskProlog"

The above functionality is limited to the task prolog script.

## Failure Handling {#failure_handling}

If the Epilog fails (returns a non-zero exit code), this will result in the node being set to a DRAIN state. If the EpilogSlurmctld fails (returns a non-zero exit code), this will only be logged. If the Prolog fails (returns a non-zero exit code), this will result in the node being set to a DRAIN state and the job requeued. The job will be placed in a held state unless nohold_on_prolog_fail is configured in SchedulerParameters. If the PrologSlurmctld fails (returns a non-zero exit code), this will cause the job to be requeued. Only batch jobs can be requeued. Interactive jobs (salloc and srun) will be cancelled if the PrologSlurmctld fails.

If a task epilog or srun epilog fails (returns a non-zero exit code) this will only be logged. If a task prolog fails (returns a non-zero exit code), the task will be canceled. If the srun prolog fails (returns a non-zero exit code), the step will be canceled.

## Environment Variables {#environment_variables}

Unless otherwise specified, these environment variables are available to all of the programs.

- **CUDA_MPS_ACTIVE_THREAD_PERCENTAGE** Specifies the percentage of a GPU that should be allocated to the job. The value is set only if the gres/mps plugin is configured and the job requests those resources. Available in Prolog and Epilog only.
- **CUDA_VISIBLE_DEVICES** Specifies the GPU devices for the job allocation. The value is set only if the gres/gpu or gres/mps plugin is configured and the job requests those resources. Note that the environment variable set for the job may differ from that set for the Prolog and Epilog if Slurm is configured to constrain the device files visible to a job using Linux cgroup. This is because the Prolog and Epilog programs run [outside]{.underline} of any Linux cgroup while the job runs [inside]{.underline} of the cgroup and may thus have a different set of visible devices. For example, if a job is allocated the device \"/dev/nvidia1\", then the Prolog and Epilog will have **CUDA_VISIBLE_DEVICES=1** set, while the job will have **CUDA_VISIBLE_DEVICES=0** set (i.e. the first GPU device visible to the job). **CUDA_VISIBLE_DEVICES** will be set unless otherwise excluded via the *Flags* or *AutoDetect* options in *gres.conf*. See also **SLURM_JOB_GPUS**. Available in Prolog and Epilog only.
- **GPU_DEVICE_ORDINAL** Specifies the GPU devices for the job allocation. The considerations for **CUDA_VISIBLE_DEVICES** also apply to **GPU_DEVICE_ORDINAL**.
- **ROCR_VISIBLE_DEVICES** Specifies the GPU devices for the job allocation. The considerations for **CUDA_VISIBLE_DEVICES** also apply to **ROCR_VISIBLE_DEVICES**.
- **SLURM_ARRAY_JOB_ID** If this job is part of a job array, this will be set to the job ID. Otherwise it will not be set. To reference this specific task of a job array, combine **SLURM_ARRAY_JOB_ID** with **SLURM_ARRAY_TASK_ID** (e.g. `scontrol update ${SLURM_ARRAY_JOB_ID}_{$SLURM_ARRAY_TASK_ID} ...`); Available in PrologSlurmctld, SrunProlog, TaskProlog, EpilogSlurmctld, SrunEpilog and TaskEpilog.
- **SLURM_ARRAY_TASK_COUNT** If this job is part of a job array, this will be set to the number of tasks in the array. Otherwise it will not be set. Available in PrologSlurmctld, SrunProlog, TaskProlog, EpilogSlurmctld, SrunEpilog and TaskEpilog.
- **SLURM_ARRAY_TASK_ID** If this job is part of a job array, this will be set to the task ID. Otherwise it will not be set. To reference this specific task of a job array, combine **SLURM_ARRAY_JOB_ID** with **SLURM_ARRAY_TASK_ID** (e.g. `scontrol update ${SLURM_ARRAY_JOB_ID}_{$SLURM_ARRAY_TASK_ID} ...`); Available in PrologSlurmctld, SrunProlog, TaskProlog, EpilogSlurmctld, SrunEpilog and TaskEpilog.
- **SLURM_ARRAY_TASK_MAX** If this job is part of a job array, this will be set to the maximum task ID. Otherwise it will not be set. Available in PrologSlurmctld, SrunProlog, TaskProlog, EpilogSlurmctld, SrunEpilog and TaskEpilog.
- **SLURM_ARRAY_TASK_MIN** If this job is part of a job array, this will be set to the minimum task ID. Otherwise it will not be set. Available in PrologSlurmctld, SrunProlog, TaskProlog, EpilogSlurmctld, SrunEpilog and TaskEpilog.
- **SLURM_ARRAY_TASK_STEP** If this job is part of a job array, this will be set to the step size of task IDs. Otherwise it will not be set. Available in PrologSlurmctld, SrunProlog, TaskProlog, EpilogSlurmctld, SrunEpilog and TaskEpilog.
- **SLURM_CLUSTER_NAME** Name of the cluster executing the job. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_CONF** Location of the slurm.conf file. Available in Prolog, SrunProlog, TaskProlog, Epilog, SrunEpilog and TaskEpilog.
- **SLURM_CPUS_ON_NODE** Count of processors available to the job on current node. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_DISTRIBUTION** Distribution type for the job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_GPUS** Count of the GPUs available to the job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_GTID** Global Task IDs running on this node. Zero origin and comma separated. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_JOB_ACCOUNT** Account name used for the job.
- **SLURM_JOB_COMMENT** Comment added to the job. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_CONSTRAINTS** Features required to run the job. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_CPUS_PER_NODE** Count of processors available per node.
- **SLURM_JOB_DERIVED_EC** The highest exit code of all of the job steps. Available in Epilog and EpilogSlurmctld.
- **SLURM_JOB_END_TIME** The UNIX timestamp for a job\'s end time.
- **SLURM_JOB_EXIT_CODE** The exit code of the job script (or salloc). The value is the status as returned by the `wait()` system call (See `wait(2)`). Available in Epilog and EpilogSlurmctld.
- **SLURM_JOB_EXIT_CODE2** The exit code of the job script (or salloc). The value has the format `<exit>:<sig>`. The first number is the exit code, typically as set by the `exit()` function. The second number is the signal that caused the process to terminate if it was terminated by a signal. Available in Epilog and EpilogSlurmctld.
- **SLURM_JOB_EXTRA** Extra field added to the job. Available in Prolog, PrologSlurmctld, Epilog, EpilogSlurmctld, and ResumeProgram (via SLURM_RESUME_FILE).
- **SLURM_JOB_GID** Group ID of the job\'s owner.
- **SLURM_JOB_GPUS** The GPU IDs of GPUs in the job allocation (if any). Available in the Prolog, SrunProlog, TaskProlog, Epilog, SrunEpilog and TaskProlog.
- **SLURM_JOB_GROUP** Group name of the job\'s owner. Available in PrologSlurmctld and EpilogSlurmctld.
- **SLURM_JOB_ID** Job ID.
- **SLURM_JOBID** Job ID.
- **SLURM_JOB_LICENSES** Name and count of any license(s) requested.
- **SLURM_JOB_NAME** Name of the job. Available in PrologSlurmctld, SrunProlog, TaskProlog, EpilogSlurmctld, SrunEpilog and TaskEpilog.
- **SLURM_JOB_NODELIST** Nodes assigned to job. A Slurm hostlist expression. `scontrol show hostnames` can be used to convert this to a list of individual host names.
- **SLURM_JOB_NUM_NODES** Number of nodes assigned to a job.
- **SLURM_JOB_OVERSUBSCRIBE** Job OverSubscribe status. See the [squeue man page](squeue.md#OPT_OverSubscribe) for possible values. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_PARTITION** Partition that job runs in.
- **SLURM_JOB_QOS** QOS assigned to job. Available in PrologSlurmctld, EpilogSlurmctld, SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_JOB_RESERVATION** Reservation requested for the job.
- **SLURM_JOB_RESTART_COUNT** Number of times the job has been restarted. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_SELINUX_CONTEXT** Selinux context for the job in available. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_SLUID** SLUID for the current run of the job. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_START_TIME** The UNIX timestamp of a job\'s start time.
- **SLURM_JOB_STDERR** Job\'s stderr path. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_STDIN** Job\'s stdin path. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_STDOUT** Job\'s stdout path. Available in Prolog, PrologSlurmctld, Epilog and EpilogSlurmctld.
- **SLURM_JOB_UID** User ID of the job\'s owner.
- **SLURM_JOB_USER** User name of the job\'s owner.
- **SLURM_JOB_WORK_DIR** Job\'s working directory. Available in Prolog, PrologSlurmctld, Epilog, EpilogSlurmctld.
- **SLURM_LOCAL_GLOBALS_FILE** Globals file used to set up the environment for the testsuite. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_LOCALID** Node local task ID for the process within a job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_NNODES** Number of nodes assigned to a job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_NODEID** ID of current node relative to other nodes in a multi-node job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_NTASKS** Number of tasks requested by the job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_PRIO_PROCESS** Scheduling priority (nice value) at the time of submission. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_PROCID** The MPI rank (or relative process ID) of the current process. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RESTART_COUNT** Number of times the job has been restarted. This is only set if the job has been restarted at least once. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_AS** Resource limit on the job\'s address space. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_CORE** Resource limit on the size of a core file the job is able to produce. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_CPU** Resource limit on the amount of CPU time a job is able to use. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_DATA** Resource limit on the size of a job\'s data segment. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_FSIZE** Resource limit on the maximum size of files a job may create. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_MEMLOCK** Resource limit on the bytes of data that may be locked into RAM. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_NOFILE** Resource limit on the number of file descriptors that can be opened by the job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_NPROC** Resource limit on the number of processes that can be opened by the calling process. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_RSS** Resource limit on the job\'s resident set size. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_RLIMIT_STACK** Resource limit on the job\'s process stack. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_SCRIPT_CONTEXT** Identifies which epilog or prolog program is currently running. The value is one of the following:
  - `prolog_slurmctld`
  - `epilog_slurmctld`
  - `prolog_slurmd`
  - `epilog_slurmd`
  - `prolog_task`
  - `epilog_task`
  - `prolog_srun`
  - `epilog_srun`
- **SLURM_STEP_ID** Step ID of the current job. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_STEPID** Step ID of the current job. Available in SrunProlog and SrunEpilog.
- **SLURM_SUBMIT_DIR** Directory from which the job was submitted or, if applicable, the directory specified by the `-D`/`--chdir` option. Available in SrunProlog, Taskprolog, SrunEpilog and TaskEpilog.
- **SLURM_SUBMIT_HOST** Host from which the job was submitted. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_TASK_PID** Process ID of the process started for the task. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_TASKS_PER_NODE** Number of tasks per node. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_TOPOLOGY_ADDR** Set to the names of network switches or nodes that may be involved in the job\'s communications. Starts with the top level switch down to the node name. A period is used to separate each hardware component name. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_TOPOLOGY_ADDR_PATTERN** Set to the network component types that corresponds with the list of names from **SLURM_TOPOLOGY_ADDR**. Each component will be identified as either [switch]{.underline} or [node]{.underline}. A period is used to separate each component type. Available in SrunProlog, TaskProlog, SrunEpilog and TaskEpilog.
- **SLURM_WCKEY** User name of the job\'s wckey (if any). Available in PrologSlurmctld and EpilogSlurmctld only.
- **SLURMD_NODENAME** Name of the node running the task. In the case of a parallel job executing on multiple compute nodes, the various tasks will have this environment variable set to different values on each compute node. Available in Prolog, SrunProlog, TaskProlog, Epilog, SrunEpilog and TaskEpilog.

Plugin functions may also be useful to execute logic at various well-defined points.

[SPANK](spank.md) is another mechanism that may be useful to invoke logic in the user commands, slurmd daemon, and slurmstepd daemon.

------------------------------------------------------------------------

Based upon work by Jason Sollom, Cray Inc. and used by permission.
