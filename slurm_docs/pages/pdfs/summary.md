# summary.pdf

Source: https://slurm.schedmd.com/pdfs/summary.pdf

## Extracted Text (Page 1)

```text
--gres=<name[:count]>
--job-name=<name>
--label
--licenses=<name[:count]
--mem=<MB>
--mem-per-cpu=<MB>
Generic resources required per
node.
Job name.
Prepend task ID to output. (srun
command only)
License resources required for
entire job.
Memory required per node.
Memory required per allocated
CPU.
Job Submission
--array=<indexes>
(e.g. "--array=1-10")
--account=<name>
--begin=<time>(e.g.
"--begin=18:00:00")
--clusters=<name>
--constraint=<features>
--cpus-per-task=<count>
--dependency=
<state:jobid>
--error=<filename>
--exclusive[=user]
--export=<name[=value]>
Job array specification.
Account to be charged for
resources used.
Initiate job after specified time.
Cluster(s) to run the job. (sbatch
command only)
Required node features.
Number of CPUs required per
task.
Defer job until specified job(s)
reach specified state.
File in which to store job error
messages.
Allocated nodes can not be
shared with other jobs/users.
Export identified environment
variables.
sbatch - Submit a batch script for later execution.
srun - Obtain a job allocation (as needed) and execute an application.
salloc - Obtain a job allocation.
cheat sheet
Copyright 2023 SchedMD LLC. All rights reserved.
www.schedmd.com
slurmctld
slurmd
Executes on cluster's "head" node to manage
workload.
Executes on each compute node to locally
manage resources.
Manages database of resources limits, licenses,
and archives accounting records. slurmdbd
Daemons
slurmrestd
-N<minnodes[-maxnodes]>
-n<count>
--nodelist=<names>
Node count required for the job.
Number of tasks to be launched.
Specific host names to include in
job allocation.
--output=<name> File in which to store job output.
--partition=<names>
--qos=<name>
--signal=[B:]<num>[@time]
--time=<time>
--wrap=<command_string>
Partition/queue in which to run
the job.
Quality Of Service.
Signal job when approaching
time limit.
Wall clock time limit.
Wrap specified command in a
simple "sh" shell.
(sbatch command only)
--allusers
--accounts=<name>
--endtime=<time>
--format=<spec>
Displays all users' jobs.
Displays jobs with specified accounts.
End of reporting period.
Specify the fields shown in the output.
--partition=<names>
--state=<state_list>
--starttime=<time>
Comma separated list of partitions to
select jobs and job steps from.
Display jobs with specified states.
Start of reporting period.
--immediate
--parsable
Commit changes immediately.
Output delimited by '|'
sacctmgr - View and modify account information.
Options:
Accounting
sacct - Display accounting data.
add <ENTITY> <SPECS>
create <ENTITY> <SPECS>
delete <ENTITY>
where <SPECS>
show <ENTITY> [<SPECS>]
modify <ENTITY> where
<SPECS> set <SPECS>
account
association
cluster
qos
Add an entity. Identical to the
create command.
Delete the specified entities.
Display information about the
specific entity.
Modify an entity.
Account used to group users.
Entity on cluster, consisting of cluster, account,
user and (optionally) partition.
ClusterName parameter in the slurm.conf.
Quality of Service.
Commands:
Entities:
sreport - Report job usage and cluster utilization.
--allusers
--accounts=<name>
Displays all users' jobs.
Displays jobs with specified accounts.
cluster
job
reservation
AccountUtilizationByUser, UserUtilizationByAccount,
UserUtilizationByWckey, Utilization,
WCKeyUtilizationByUser
SizesByAccount, SizesByAccountAndWckey,
SizesByWckey
Utilization
TopUsage
Report Types:
user
Interface to Slurm via REST API.
qos
--long Provides output with more fields listed. .create SPECIFICATION Create a new partition or reservation.
```

## Extracted Text (Page 2)

```text
delete SPECIFICATION
reconfigure
requeue JOB_LIST
show ENTITY ID
Delete the entry with the specified
SPECIFICATION.
All Slurm daemons will re-read the
configuration file.
Requeue a running, suspended or
completed batch job.
Display the state of the specified
entity with the specified identification.
Commands:
--account=<name>
--name=<name>
--partition=
<names>
--qos=<name>
--reservation=
<name>
--state=<names>
--user=<name>
--nodelist=
<names>
Operate only on jobs running in the
specified account.
Operate only on jobs with specified name.
Operate only on jobs in the specified
partition/queue.
Operate only on jobs using the
specified quality of service.
Operate only on jobs using the
specified reservation.
Operate only on jobs
in the specified state.
Operate only on jobs from the specified
user.
Operate only on jobs using the specified
compute nodes.
Job Management scancel - Signal jobs, job arrays, and/or job steps.
--account=<name>
--clusters=<name>
--format=<spec>
(e.g. "--format
=%i,%j")
--jobs<job_id_list>
View only jobs with specified accounts.
View jobs on specified clusters.
Output format to display. Specify fields,
size, order, etc.
Comma separated list of job IDs to
display.
squeue - View information about jobs.
--name=<name> View only jobs with specified names.
--partition=<names>
--priority
--qos=<name>
View only jobs in specified partitions.
Sort jobs by priority.
View only jobs with specified Qualities
Of Service.
--start
--state=<names>
--users=<names>
Report the expected start time and
resources to be allocated for pending
jobs in order of increasing start time.
View only jobs with specified states.
View only jobs for specified users.
--all
--dead
--format=<spec>
Display information about all partitions.
If set, only report state information for
non-responding (dead) nodes.
Output format to display.
sinfo - View all information about nodes and partitions.
--long
Print the state at specified interval.
Print more detailed information.
--Node
--partition=<names>
--reservation
-R
--state=<names>
Print information in a node-oriented
format.
View only specified partitions.
Display information about advanced
reservations.
Display reasons nodes are in the down,
drained, fail or failing state.
View only nodes in specified states.
--iterate=<seconds>
SLURM_JOB_NAME Job Name.
SLURM_JOB_NODELIST
SLURM_JOB_NUM_NODE
Names of nodes allocated to job.
Number of nodes allocated to
job.
SLURM_JOB_PARTITION Partition/queue running the job.
SLURM_JOB_UID
SLURM_JOB_USER
SLURM_RESTART_COUNT
User ID of the job's owner.
User name of the job's owner.
Number of times job has
restarted.
SLURM_PROCID
SLURM_STEP_ID
SLURM_STEP_NUM_TASKS
Task ID (MPI rank).
Job step ID.
Task count (number of MPI
ranks).
Copyright 2023 SchedMD LLC. All rights reserved.
www.schedmd.com
SLURM_ARRAY_JOB_ID
SLURM_ARRAY_TASK_ID
SLURM_CLUSTER_NAME
Set to the job ID if part of a job
array.
Set to the task ID if part of a job
array.
Name of the cluster executing
the job.
SLURM_CPUS_PER_TASK
SLURM_JOB_ACCOUNT
Number of CPUs requested per
task.
Account name.
SLURM_JOB_ID Job ID.
Environment Variables
SLURM_DEBUG_FLAGS Specify debug flags for sbatch
to use.
--all When show command is used, then display
all partitions, their jobs, and job steps.
scontrol - Used view and modify configuration and state.
Also see the sview graphical user interface version.
--details Causes show command to provide more
details when available.
--oneliner Print information on one line.
--future Report nodes in FUTURE state.
setdebugflags Add or remove DebugFlags of the
slurmctld daemon.
update SPECIFICATION Update job, step, node, partition, or
reservation configuration per the
supplied specification.
show ENTITY ID Display the state of the specified
entity with the specified identification.
```
