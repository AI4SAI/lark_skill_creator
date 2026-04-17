# squeue

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

squeue - view information about jobs located in the Slurm scheduling queue.

[ ]{#lbAC}

## SYNOPSIS

**squeue** \[*OPTIONS*\...\]

[ ]{#lbAD}

## DESCRIPTION

**squeue** is used to view job and job step information for jobs managed by Slurm.

[ ]{#lbAE}

## OPTIONS

**-A**, **\--account**=\<*account_list*\>
:   Specify the accounts of the jobs to view. Accepts a comma separated list of account names. This has no effect when listing job steps.

:   

**-a**, **\--all**
:   Display information about jobs and job steps in all partitions. This causes information to be displayed about partitions that are configured as hidden, partitions that are unavailable to a user\'s group, and federated jobs that are in a \"revoked\" state.

:   

**-r**, **\--array**
:   Display one job array element per line. Without this option, the display will be optimized for use with job arrays (pending job array elements will be combined on one line of output with the array index values printed using a regular expression).

:   

**-M**, **\--clusters**=\<*cluster_name*\>
:   Clusters to issue commands to. Multiple cluster names may be comma separated. A value of \'*all*\' will query to run on all clusters. Note that the **slurmdbd** must be up for this option to work properly, unless running in a federation with either **FederationParameters=fed_display** configured or the **\--federation** option set. This option implicitly sets the **\--local** option.

:   

**\--expand-patterns**
:   Expand any filename patterns from in **StdOut**, **StdErr** and **StdIn**. Fields that map to a range of values will use the first value of the range. For example \"%t\" for task id will be replaced by \"0\".

:   

**\--federation**
:   Show jobs from the federation if a member of one.

:   

**-o**, **\--format**=\<*output_format*\>
:   Specify the information to be displayed, its size and position (right or left justified). Also see the **-O**, **\--Format**=\<*output_format*\> option described below (which supports less flexibility in formatting, but supports access to all fields). If the command is executed in a federated cluster environment and information about more than one cluster is to be displayed and the **-h, \--noheader** option is used, then the cluster name will be displayed before the default output formats shown below.
    The default formats with various options are:

:   

    :   

        *default*
        :   \"%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R\"

        :   

        *-l, \--long*
        :   \"%.18i %.9P %.8j %.8u %.8T %.10M %.9l %.6D %R\"

        :   

        *-s, \--steps*
        :   \"%.15i %.8j %.9P %.8u %.9M %N\"

        :   

    The format of each field is \"%\[\[.\]size\]type\[suffix\]\"

:   

    :   

        *size*
        :   Minimum field size. If no size is specified, whatever is needed to print the information will be used.

        :   

        *.*
        :   Indicates the output should be right justified and size must be specified. By default output is left justified.

        :   

        *suffix*
        :   Arbitrary string to append to the end of the field.

        :   

    Note that many of these *type* specifications are valid only for jobs while others are valid only for job steps. Valid *type* specifications include:

:   

    :   

        **%all**
        :   Print all fields available for this data type with a vertical bar separating each field.

        :   

        **%a**
        :   Account associated with the job. (Valid for jobs only)

        :   

        **%A**
        :   Number of tasks created by a job step. This reports the value of the **srun \--ntasks** option. (Valid for job steps only)

        :   

        **%A**
        :   Job id. This will have a unique value for each element of job arrays. (Valid for jobs only)

        :   

        **%B**
        :   Executing (batch) host. For an allocated session, this is the host on which the session is executing (i.e. the node from which the **srun** or the **salloc** command was executed). For a batch job, this is the node executing the batch script. In the case of a typical Linux cluster, this would be the compute node zero of the allocation.

        :   

        **%c**
        :   Minimum number of CPUs (processors) per node requested by the job. This reports the value of the **srun \--mincpus** option with a default value of zero. (Valid for jobs only)

        :   

        **%C**
        :   Number of CPUs (processors) requested by the job or allocated to it if already running. As a job is completing this number will reflect the current number of CPUs allocated. (Valid for jobs only)

        :   

        **%d**
        :   Minimum size of temporary disk space (in MB) requested by the job. (Valid for jobs only)

        :   

        **%D**
        :   Number of nodes allocated to the job or the minimum number of nodes required by a pending job. The actual number of nodes allocated to a pending job may exceed this number if the job specified a node range count (e.g. minimum and maximum node counts) or the job specifies a processor count instead of a node count. As a job is completing this number will reflect the current number of nodes allocated. (Valid for jobs only)

        :   

        **%e**
        :   Time at which the job ended or is expected to end (based upon its time limit). (Valid for jobs only)

        :   

        **%E**
        :   Job dependencies remaining. This job will not begin execution until these dependent jobs complete. In the case of a job that can not run due to job dependencies never being satisfied, the full original job dependency specification will be reported. Once a dependency is satisfied, it is removed from the job. A value of NULL implies this job has no dependencies. (Valid for jobs only)

        :   

        **%f**
        :   Features required by the job. (Valid for jobs only)

        :   

        **%F**
        :   Job array\'s job ID. This is the base job ID. For non-array jobs, this is the job ID. (Valid for jobs only)

        :   

        **%g**
        :   Group name of the job. (Valid for jobs only)

        :   

        **%G**
        :   Group ID of the job. (Valid for jobs only)

        :   

        **%h**
        :   Can the compute resources allocated to the job be over subscribed by other jobs. The resources to be over subscribed can be nodes, sockets, cores, or hyperthreads depending upon configuration. The value will be \"YES\" if the job was submitted with the oversubscribe option or the partition is configured with OverSubscribe=Force, \"NO\" if the job requires exclusive node access, \"USER\" if the allocated compute nodes are dedicated to a single user, \"MCS\" if the allocated compute nodes are dedicated to a single security class (See MCSPlugin and MCSParameters configuration parameters for more information), \"OK\" otherwise (typically allocated dedicated CPUs), (Valid for jobs only)

        :   

        **%H**
        :   Number of sockets per node requested by the job. This reports the value of the **srun \--sockets-per-node** option. When \--sockets-per-node has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **%i**
        :   Job or job step id. In the case of job arrays, the job ID format will be of the form \"\<base_job_id\>\_\<index\>\". By default, the job array index field size will be limited to 64 bytes. Use the environment variable SLURM_BITSTR_LEN to specify larger field sizes. (Valid for jobs and job steps) In the case of heterogeneous job allocations, the job ID format will be of the form \"#+#\" where the first number is the \"heterogeneous job leader\" and the second number the zero origin offset for each component of the job.

        :   

        **%I**
        :   Number of cores per socket requested by the job. This reports the value of the **srun \--cores-per-socket** option. When \--cores-per-socket has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **%j**
        :   Job or job step name. (Valid for jobs and job steps)

        :   

        **%J**
        :   Number of threads per core requested by the job. This reports the value of the **srun \--threads-per-core** option. When \--threads-per-core has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **%k**
        :   Comment associated with the job. (Valid for jobs only)

        :   

        **%K**
        :   Job array index. By default, this field size will be limited to 64 bytes. Use the environment variable SLURM_BITSTR_LEN to specify larger field sizes. (Valid for jobs only)

        :   

        **%l**
        :   Time limit of the job or job step in days-hours:minutes:seconds. The value may be \"NOT_SET\" if not yet established or \"UNLIMITED\" for no limit. (Valid for jobs and job steps)

        :   

        **%L**
        :   Time left for the job to execute in days-hours:minutes:seconds. This value is calculated by subtracting the job\'s time used from its time limit. The value may be \"NOT_SET\" if not yet established or \"UNLIMITED\" for no limit. (Valid for jobs only)

        :   

        **%m**
        :   Minimum size of memory (in MB) requested by the job. (Valid for jobs only) If memory was request per CPU, or per GPU the value is shown with the assumption that at least one CPU, GPU will be allocated respectively.

        :   

        **%M**
        :   Time used by the job or job step in days-hours:minutes:seconds. The days and hours are printed only as needed. For job steps this field shows the elapsed time since execution began and thus will be inaccurate for job steps which have been suspended. Clock skew between nodes in the cluster will cause the time to be inaccurate. If the time is obviously wrong (e.g. negative), it displays as \"INVALID\". (Valid for jobs and job steps)

        :   

        **%n**
        :   List of node names explicitly requested by the job. (Valid for jobs only)

        :   

        **%N**
        :   List of nodes allocated to the job or job step. In the case of a *COMPLETING* job, the list of nodes will comprise only those nodes that have not yet been returned to service. (Valid for jobs and job steps)

        :   

        **%o**
        :   The command to be executed.

        :   

        **%O**
        :   Are contiguous nodes requested by the job. (Valid for jobs only)

        :   

        **%p**
        :   Priority of the job (converted to a floating point number between 0.0 and 1.0). Also see **%Q**. (Valid for jobs only)

        :   

        **%P**
        :   Partition of the job or job step. (Valid for jobs and job steps)

        :   

        **%q**
        :   Quality of service associated with the job. (Valid for jobs only)

        :   

        **%Q**
        :   Priority of the job (generally a very large unsigned integer). Also see **%p**. (Valid for jobs only)

        :   

        **%r**
        :   The reason a job is in its current state. See the **JOB REASON CODES** section below for more information. (Valid for jobs only)

        :   

        **%R**
        :   For pending jobs: the reason a job has not been started by the scheduler is printed within parenthesis. For terminated jobs with failure: an explanation as to why the job failed is printed within parenthesis. For all other job states: the list of allocate nodes. See the **JOB REASON CODES** section below for more information. (Valid for jobs only)

        :   

        **%s**
        :   SLUID (Valid for jobs only)

        :   

        **%S**
        :   Actual or expected start time of the job or job step. (Valid for jobs and job steps)

        :   

        **%t**
        :   Job state in compact form. See the **JOB STATE CODES** section below for a list of possible states. (Valid for jobs only)

        :   

        **%T**
        :   Job state in extended form. See the **JOB STATE CODES** section below for a list of possible states. (Valid for jobs only)

        :   

        **%u**
        :   User name for a job or job step. (Valid for jobs and job steps)

        :   

        **%U**
        :   User ID for a job or job step. (Valid for jobs and job steps)

        :   

        **%v**
        :   Reservation for the job. (Valid for jobs only)

        :   

        **%V**
        :   The job\'s submission time.

        :   

        **%w**
        :   Workload Characterization Key (wckey). (Valid for jobs only)

        :   

        **%W**
        :   Licenses requested by the job. (Valid for jobs only)

        :   

        **%x**
        :   List of node names explicitly excluded by the job. (Valid for jobs only)

        :   

        **%X**
        :   Count of cores reserved on each node for system use (core specialization). (Valid for jobs only)

        :   

        **%y**
        :   Nice value (adjustment to a job\'s scheduling priority). (Valid for jobs only)

        :   

        **%Y**
        :   For pending jobs, a list of the nodes expected to be used when the job is started.

        :   

        **%z**
        :   Number of requested sockets, cores, and threads (S:C:T) per node for the job. When (S:C:T) has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **%Z**
        :   The job\'s working directory.

:   

**-O**, **\--Format**=\<*output_format*\>
:   Specify the information to be displayed. Also see the **-o**, **\--format**=\<*output_format*\> option described above (which supports greater flexibility in formatting, but does not support access to all fields because we ran out of letters). Requests a comma separated list of job information to be displayed.
    The format of each field is \"type\[:\[.\]\[size\]\[suffix\]\]\"

:   

    :   

        *size*
        :   Minimum field size. If no size is specified, 20 characters will be allocated to print the information.

        :   

        *.*
        :   Indicates the output should be right justified and size must be specified. By default output is left justified.

        :   

        *suffix*
        :   Arbitrary string to append to the end of the field.

        :   

    Note that many of these *type* specifications are valid only for jobs while others are valid only for job steps. Valid *type* specifications include:

:   

    :   

        **Account**
        :   Print the account associated with the job. (Valid for jobs only)

        :   

        **AccrueTime**
        :   Print the accrue time associated with the job. (Valid for jobs only)

        :   

        **admin_comment**
        :   Administrator comment associated with the job. (Valid for jobs only)

        :   

        **AllocNodes**
        :   Print the nodes allocated to the job. (Valid for jobs only)

        :   

        **AllocSID**
        :   Print the session ID used to submit the job. (Valid for jobs only)

        :   

        **ArrayJobID**
        :   Prints the job ID of the job array. (Valid for jobs and job steps)

        :   

        **ArrayTaskID**
        :   Prints the task ID of the job array. (Valid for jobs and job steps)

        :   

        **AssocID**
        :   Prints the ID of the job association. (Valid for jobs only)

        :   

        **BatchFlag**
        :   Prints whether the batch flag has been set. (Valid for jobs only)

        :   

        **BatchHost**
        :   Executing (batch) host. For an allocated session, this is the host on which the session is executing (i.e. the node from which the **srun** or the **salloc** command was executed). For a batch job, this is the node executing the batch script. In the case of a typical Linux cluster, this would be the compute node zero of the allocation. (Valid for jobs only)

        :   

        **BoardsPerNode**
        :   Prints the number of boards per node allocated to the job. (Valid for jobs only)

        :   

        **BurstBuffer**
        :   Burst Buffer specification (Valid for jobs only)

        :   

        **BurstBufferState**
        :   Burst Buffer state (Valid for jobs only)

        :   

        **Cluster**
        :   Name of the cluster that is running the job or job step.

        :   

        **ClusterFeature**
        :   Cluster features required by the job. (Valid for jobs only)

        :   

        **Command**
        :   The command to be executed. (Valid for jobs only)

        :   

        **Comment**
        :   Comment associated with the job. (Valid for jobs only)

        :   

        **Contiguous**
        :   Are contiguous nodes requested by the job. (Valid for jobs only)

        :   

        **Container**
        :   OCI container bundle path.

        :   

        **ContainerID**
        :   OCI container assigned ID.

        :   

        **Cores**
        :   Number of cores per socket requested by the job. This reports the value of the **srun \--cores-per-socket** option. When **\--cores-per-socket** has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **CoreSpec**
        :   Count of cores reserved on each node for system use (core specialization). (Valid for jobs only)

        :   

        **CPUFreq**
        :   Prints the frequency of the allocated CPUs. (Valid for job steps only)

        :   

        **cpus-per-task**
        :   Prints the number of CPUs per tasks allocated to the job. (Valid for jobs only)

        :   

        **cpus-per-tres**
        :   Print the memory required per trackable resources allocated to the job or job step.

        :   

        **CronJob**
        :   Print Yes/No depending on whether the job has been generated by scrontab or not. (Valid for jobs only)

        :   

        **Deadline**
        :   Prints the deadline affected to the job (Valid for jobs only)

        :   

        **DelayBoot**
        :   Delay boot time. (Valid for jobs only)

        :   

        **Dependency**
        :   Job dependencies remaining. This job will not begin execution until these dependent jobs complete. In the case of a job that can not run due to job dependencies never being satisfied, the full original job dependency specification will be reported. Once a dependency is satisfied, it is removed from the job. A value of NULL implies this job has no dependencies. (Valid for jobs only)

        :   

        **DerivedEC**
        :   The highest exit code returned by the job\'s job steps (srun invocations). Following the colon is the signal that caused the process to terminate if it was terminated by a signal. (Valid for jobs only)

        :   

        **EligibleTime**
        :   Time the job is eligible for running. (Valid for jobs only)

        :   

        **EndTime**
        :   The time of job termination, actual or expected. (Valid for jobs only)

        :   

        **ExcNodes**
        :   The nodes requested to be excluded when allocating this job. (Valid for jobs only)

        :   

        **exit_code**
        :   The exit code returned by the job, typically as set by the exit() function. Following the colon is the signal that caused the process to terminate if it was terminated by a signal. (Valid for jobs only)

        :   

        **Feature**
        :   Features required by the job. (Valid for jobs only)

        :   

        **GroupID**
        :   Group ID of the job. (Valid for jobs only)

        :   

        **GroupName**
        :   Group name of the job. (Valid for jobs only)

        :   

        **HetJobID**
        :   Job ID of the heterogeneous job leader.

        :   

        **HetJobIDSet**
        :   Expression identifying all components job IDs within a heterogeneous job.

        :   

        **HetJobOffset**
        :   Zero origin offset within a collection of heterogeneous job components.

        :   

        **JobArrayID**
        :   Job array\'s job ID. This is the base job ID. For non-array jobs, this is the job ID. (Valid for jobs only)

        :   

        **JobID**
        :   Job ID. This will have a unique value for each element of job arrays and each component of heterogeneous jobs. (Valid for jobs only)

        :   

        **LastSchedEval**
        :   Prints the last time the job was evaluated for scheduling. (Valid for jobs only)

        :   

        **Licenses**
        :   Licenses requested by the job. (Valid for jobs only)

        :   

        **LicensesAlloc**
        :   Licenses allocated to the job. (Valid for jobs only)

        :   

        **MaxCPUs**
        :   Prints the max number of CPUs allocated to the job. (Valid for jobs only)

        :   

        **MaxNodes**
        :   Prints the max number of nodes allocated to the job. (Valid for jobs only)

        :   

        **MCSLabel**
        :   Prints the MCS_label of the job. (Valid for jobs only)

        :   

        **mem-per-tres**
        :   Print the memory (in MB) required per trackable resources allocated to the job or job step.

        :   

        **MinCpus**
        :   Minimum number of CPUs (processors) per node requested by the job. This reports the value of the **srun \--mincpus** option with a default value of zero. (Valid for jobs only)

        :   

        **MinMemory**
        :   Minimum size of memory (in MB) requested by the job. (Valid for jobs only)

        :   

        **MinTime**
        :   Minimum time limit of the job (Valid for jobs only)

        :   

        **MinTmpDisk**
        :   Minimum size of temporary disk space (in MB) requested by the job. (Valid for jobs only)

        :   

        **Name**
        :   Job or job step name. (Valid for jobs and job steps)

        :   

        **Network**
        :   The network that the job is running on. (Valid for jobs and job steps)

        :   

        **Nice**
        :   Nice value (adjustment to a job\'s scheduling priority). (Valid for jobs only)

        :   

        **NodeList**
        :   List of nodes allocated to the job or job step. In the case of a *COMPLETING* job, the list of nodes will comprise only those nodes that have not yet been returned to service. (Valid for jobs only)

        :   

        **Nodes**
        :   List of nodes allocated to the job or job step. In the case of a *COMPLETING* job, the list of nodes will comprise only those nodes that have not yet been returned to service. (Valid job steps only)

        :   

        **NTPerBoard**
        :   The number of tasks per board allocated to the job. (Valid for jobs only)

        :   

        **NTPerCore**
        :   The number of tasks per core allocated to the job. (Valid for jobs only)

        :   

        **NTPerNode**
        :   The number of tasks per node allocated to the job. (Valid for jobs only)

        :   

        **NTPerSocket**
        :   The number of tasks per socket allocated to the job. (Valid for jobs only)

        :   

        **NumCPUs**
        :   Number of CPUs (processors) requested by the job or allocated to it if already running. As a job is completing, this number will reflect the current number of CPUs allocated. (Valid for jobs and job steps)

        :   

        **NumNodes**
        :   Number of nodes allocated to the job or the minimum number of nodes required by a pending job. The actual number of nodes allocated to a pending job may exceed this number if the job specified a node range count (e.g. minimum and maximum node counts) or the job specifies a processor count instead of a node count. As a job is completing this number will reflect the current number of nodes allocated. (Valid for jobs only)

        :   

        **NumTasks**
        :   Number of tasks requested by a job or job step. This reports the value of the **\--ntasks** option. (Valid for jobs and job steps)

        :   

        **Origin**
        :   Cluster name where federated job originated from. (Valid for federated jobs only)

        :   

        **OriginRaw**
        :   Cluster ID where federated job originated from. (Valid for federated jobs only)

        :   

        **OverSubscribe**
        :   Can the compute resources allocated to the job be over subscribed by other jobs. The resources to be over subscribed can be nodes, sockets, cores, or hyperthreads depending upon configuration. The value will be \"YES\" if the job was submitted with the oversubscribe option or the partition is configured with OverSubscribe=Force, \"NO\" if the job requires exclusive node access, \"USER\" if the allocated compute nodes are dedicated to a single user, \"MCS\" if the allocated compute nodes are dedicated to a single security class (See MCSPlugin and MCSParameters configuration parameters for more information), \"OK\" otherwise (typically allocated dedicated CPUs), (Valid for jobs only)

        :   

        **Partition**
        :   Partition of the job or job step. (Valid for jobs and job steps)

        :   

        **PendingTime**
        :   The time (in seconds) between start time and submit time of the job. If the job has not started yet, then the time (in seconds) between now and the submit time of the job. (Valid for jobs only)

        :   

        **PreemptTime**
        :   The preempt time for the job. (Valid for jobs only)

        :   

        **Prefer**
        :   The preferred features of a pending job. (Valid for jobs only)

        :   

        **Priority**
        :   Priority of the job (converted to a floating point number between 0.0 and 1.0). Also see **prioritylong**. (Valid for jobs only)

        :   

        **PriorityLong**
        :   Priority of the job (generally a very large unsigned integer). Also see **priority**. (Valid for jobs only)

        :   

        **Profile**
        :   Profile of the job. (Valid for jobs only)

        :   

        **QOS**
        :   Quality of service associated with the job. (Valid for jobs only)

        :   

        **Reason**
        :   The reason a job is in its current state. See the **JOB REASON CODES** section below for more information. (Valid for jobs only)

        :   

        **ReasonList**
        :   For pending jobs: the reason a job is waiting for execution is printed within parenthesis. For terminated jobs with failure: an explanation as to why the job failed is printed within parenthesis. For all other job states: the list of allocate nodes. See the **JOB REASON CODES** section below for more information. (Valid for jobs only)

        :   

        **Reboot**
        :   Indicates if the allocated nodes should be rebooted before starting the job. (Valid on jobs only)

        :   

        **ReqNodes**
        :   List of node names explicitly requested by the job. (Valid for jobs only)

        :   

        **ReqSwitch**
        :   The max number of requested switches by for the job. (Valid for jobs only)

        :   

        **Requeue**
        :   Prints whether the job will be requeued on failure. (Valid for jobs only)

        :   

        **Reservation**
        :   Reservation for the job. (Valid for jobs only)

        :   

        **ResizeTime**
        :   The amount of time changed for the job to run. (Valid for jobs only)

        :   

        **RestartCnt**
        :   The number of restarts for the job. (Valid for jobs only)

        :   

        **ResvPort**
        :   Reserved ports of the job. (Valid for job steps only)

        :   

        **SchedNodes**
        :   For pending jobs, a list of the nodes expected to be used when the job is started. (Valid for jobs only)

        :   

        **SCT**
        :   Number of requested sockets, cores, and threads (S:C:T) per node for the job. When (S:C:T) has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **SegmentSize**
        :   Segment size requested by the job. (Valid for jobs only)

        :   

        **SiblingsActive**
        :   Cluster names of where federated sibling jobs exist. (Valid for federated jobs only)

        :   

        **SiblingsActiveRaw**
        :   Cluster IDs of where federated sibling jobs exist. (Valid for federated jobs only)

        :   

        **SiblingsViable**
        :   Cluster names of where federated sibling jobs are viable to run. (Valid for federated jobs only)

        :   

        **SiblingsViableRaw**
        :   Cluster IDs of where federated sibling jobs viable to run. (Valid for federated jobs only)

        :   

        **Sockets**
        :   Number of sockets per node requested by the job. This reports the value of the **srun \--sockets-per-node** option. When **\--sockets-per-node** has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **SPerBoard**
        :   Number of sockets per board allocated to the job. (Valid for jobs only)

        :   

        **StartTime**
        :   Actual or expected start time of the job or job step. (Valid for jobs and job steps)

        :   

        **State**
        :   Job state in extended form. See the **JOB STATE CODES** section below for a list of possible states. (Valid for jobs only)

        :   

        **StateCompact**
        :   Job state in compact form. See the **JOB STATE CODES** section below for a list of possible states. (Valid for jobs only)

        :   

        **STDERR**
        :   The directory for standard error to output to. (Valid for jobs and steps)

        :   

        **STDIN**
        :   The directory for standard in. (Valid for jobs and steps)

        :   

        **STDOUT**
        :   The directory for standard out to output to. (Valid for jobs and steps)

        :   

        **StepID**
        :   Job or job step ID. In the case of job arrays, the job ID format will be of the form \"\<base_job_id\>\_\<index\>\". (Valid for job steps only)

        :   

        **StepName**
        :   Job step name. (Valid for job steps only)

        :   

        **StepState**
        :   The state of the job step. (Valid for job steps only)

        :   

        **SubmitTime**
        :   The time that the job was submitted at. (Valid for jobs only)

        :   

        **system_comment**
        :   System comment associated with the job. (Valid for jobs only)

        :   

        **Threads**
        :   Number of threads per core requested by the job. This reports the value of the **srun \--threads-per-core** option. When **\--threads-per-core** has not been set, \"\*\" is displayed. (Valid for jobs only)

        :   

        **TimeLeft**
        :   Time left for the job to execute in days-hours:minutes:seconds. This value is calculated by subtracting the job\'s time used from its time limit. The value may be \"NOT_SET\" if not yet established or \"UNLIMITED\" for no limit. (Valid for jobs only)

        :   

        **TimeLimit**
        :   Timelimit for the job or job step. (Valid for jobs and job steps)

        :   

        **TimeUsed**
        :   Time used by the job or job step in days-hours:minutes:seconds. The days and hours are printed only as needed. For job steps this field shows the elapsed time since execution began and thus will be inaccurate for job steps which have been suspended. Clock skew between nodes in the cluster will cause the time to be inaccurate. If the time is obviously wrong (e.g. negative), it displays as \"INVALID\". (Valid for jobs and job steps)

        :   

        **tres-alloc**
        :   Print the trackable resources allocated to the job if running. If not running, then print the trackable resources requested by the job.

        :   

        **tres-bind**
        :   Print the trackable resources task binding requested by the job or job step.

        :   

        **tres-freq**
        :   Print the trackable resources frequencies requested by the job or job step.

        :   

        **tres-per-job**
        :   Print the trackable resources requested by the job.

        :   

        **tres-per-node**
        :   Print the trackable resources per node requested by the job or job step.

        :   

        **tres-per-socket**
        :   Print the trackable resources per socket requested by the job or job step.

        :   

        **tres-per-step**
        :   Print the trackable resources requested by the job step.

        :   

        **tres-per-task**
        :   Print the trackable resources per task requested by the job or job step.

        :   

        **UserID**
        :   User ID for a job or job step. (Valid for jobs and job steps)

        :   

        **UserName**
        :   User name for a job or job step. (Valid for jobs and job steps)

        :   

        **Wait4Switch**
        :   The amount of time to wait for the desired number of switches. (Valid for jobs only)

        :   

        **WCKey**
        :   Workload Characterization Key (wckey). (Valid for jobs only)

        :   

        **WorkDir**
        :   The job\'s working directory. (Valid for jobs only)

:   

**\--help**
:   Print a help message describing all options **squeue**.

:   

**\--hide**
:   Do not display information about jobs and job steps in all partitions. By default, information about partitions that are configured as hidden or are not available to the user\'s group will not be displayed (i.e. this is the default behavior).

:   

**-i**, **\--iterate**=\<*seconds*\>
:   Repeatedly gather and report the requested information at the interval specified (in seconds). By default, prints a time stamp with the header.

:   

**-j**, **\--jobs**\[=\<*job_id_list*\>\]
:   Specify a comma separated list of job IDs to display. Defaults to all jobs. The **\--jobs**=\<*job_id_list*\> option may be used in conjunction with the **\--steps** option to print step information about specific jobs. Note: If a list of job IDs is provided, the jobs are displayed even if they are on hidden partitions. Since this option\'s argument is optional, for proper parsing the single letter option must be followed immediately with the value and not include a space between them. For example \"-j1008\" and not \"-j 1008\". The job ID format is \"job_id\[\_array_id\]\". Performance of the command can be measurably improved for systems with large numbers of jobs when a single job ID is specified. By default, this field size will be limited to 64 bytes. Use the environment variable SLURM_BITSTR_LEN to specify larger field sizes.

:   

**\--json**, **\--json**=*list*, **\--json**=\<*data_parser*\>
:   Dump information as JSON using the default data_parser plugin or explicit data_parser with parameters. All information is dumped, even if it would normally not be. Sorting and formatting arguments passed to other options are ignored; however, most filtering arguments are still used.

:   

**-L**, **\--licenses**=\<*license_list*\>
:   Request jobs requesting or using one or more of the named licenses. The license list consists of a comma separated list of license names.

:   

**\--local**
:   Show only jobs local to this cluster. Ignore other clusters in this federation (if any). Overrides \--federation.

:   

**-l**, **\--long**
:   Report more of the available information for the selected jobs or job steps, subject to any constraints specified.

:   

**\--me**
:   Equivalent to **\--user=\<my username\>**.

:   

**-n**, **\--name**=\<*name_list*\>
:   Request jobs or job steps having one of the specified names. The list consists of a comma separated list of job names.

:   

**\--noconvert**
:   Don\'t convert units from their original type (e.g. 2048M won\'t be converted to 2G).

:   

**-w**, **\--nodelist**=\<*hostlist*\>
:   Report only on jobs allocated to the specified node or list of nodes. This may either be the **NodeName** or **NodeHostname** as defined in **[slurm.conf](slurm.conf.md)(5)** in the event that they differ. A node_name of **localhost** is mapped to the current host name.

:   

**-h**, **\--noheader**
:   Do not print a header on the output.

:   

**\--notme**
:   Opposite of **\--me**; only display jobs that are not from the invoking user.

:   

**\--only-job-state**
:   Only query for the job state. Query utilizes RPC that only retains JobID and State information, reducing work required by slurmctld to respond.

:   

**-p**, **\--partition**=\<*part_list*\>
:   Specify the partitions of the jobs or steps to view. Accepts a comma separated list of partition names.

:   

**-P**, **\--priority**
:   For pending jobs submitted to multiple partitions, list the job once per partition. In addition, if jobs are sorted by priority, consider both the partition and job priority. This option can be used to produce a list of pending jobs in the same order considered for scheduling by Slurm with appropriate additional options (e.g. \"\--sort=-p,i \--states=PD\").

:   

**-q**, **\--qos**=\<*qos_list*\>
:   Specify the qos(s) of the jobs or steps to view. Accepts a comma separated list of qos\'s.

:   

**-R**, **\--reservation**=\<*reservation_list*\>
:   Specify the reservations of the jobs to view. Accepts a comma separated list of reservation names. Jobs matching any reservation will satisfy the filter (logic works like an OR).

:   

**\--running-over**=\<*time*\>
:   Display only jobs that have been running over the amount of specified time. Acceptable time formats include \"minutes\", \"minutes:seconds\", \"hours:minutes:seconds\", \"days-hours\", \"days-hours:minutes\" and \"days-hours:minutes:seconds\".

:   

**\--running-under**=\<*time*\>
:   Display only jobs that have been running under the amount of specified time. Acceptable time formats include \"minutes\", \"minutes:seconds\", \"hours:minutes:seconds\", \"days-hours\", \"days-hours:minutes\" and \"days-hours:minutes:seconds\".

:   

**\--sibling**
:   Show all sibling jobs on a federated cluster. Implies \--federation.

:   

**-S**, **\--sort**=\<*sort_list*\>
:   Specification of the order in which records should be reported. This uses the same field specification as the \<output_format\>. The long format option \"cluster\" can also be used to sort jobs or job steps by cluster name (e.g. federated jobs). Multiple sorts may be performed by listing multiple sort fields separated by commas. The field specifications may be preceded by \"+\" or \"-\" for ascending (default) and descending order respectively. For example, a sort value of \"P,U\" will sort the records by partition name then by user id. The default value of sort for jobs is \"P,t,-p\" (increasing partition name then within a given partition by increasing job state and then decreasing priority). The default value of sort for job steps is \"P,i\" (increasing partition name then within a given partition by increasing step id).

:   

**\--start**
:   Report the expected start time and resources to be allocated for pending jobs in order of increasing start time. This is equivalent to the following options: **\--format=\"%.18i %.9P %.8j %.8u %.2t %.19S %.6D %20Y %R\"**, **\--sort=S** and **\--states=PENDING**. Any of these options may be explicitly changed as desired by combining the **\--start** option with other option values (e.g. to use a different output format). The expected start time of pending jobs is only available if the Slurm is configured to use the backfill scheduling plugin.

:   

**-t**, **\--states**=\<*state_list*\>
:   Specify the states of jobs to view. Accepts a comma separated list of state names or \"all\". If \"all\" is specified then jobs of all states will be reported. If no state is specified then pending, running, and completing jobs are reported. See the **JOB STATE CODES** section below for a list of valid states. Both extended and compact forms are valid. Note the **\<state_list\>** supplied is case insensitive (\"pd\" and \"PD\" are equivalent).

:   

**-s**, **\--steps**\[=\<*step_list*\>\]
:   Specify the job steps to view. This flag indicates that a comma separated list of job steps to view follows without an equal sign (see examples). The job step format is \"job_id\[\_array_id\].step_id\". Defaults to all job steps. Since this option\'s argument is optional, for proper parsing the single letter option must be followed immediately with the value and not include a space between them. For example \"-s1008.0\" and not \"-s 1008.0\".

:   

**\--usage**
:   Print a brief help message listing the **squeue** options.

:   

**-u**, **\--user**=\<*user_list*\>
:   Request jobs or job steps from a comma separated list of users. The list can consist of user names or user id numbers. Performance of the command can be measurably improved for systems with large numbers of jobs when a single user is specified.

:   

**-v**, **\--verbose**
:   Report details of squeues actions.

:   

**-V** , **\--version**
:   Print version information and exit.

:   

**\--yaml**, **\--yaml**=*list*, **\--yaml**=\<*data_parser*\>
:   Dump information as YAML using the default data_parser plugin or explicit data_parser with parameters. All information is dumped, even if it would normally not be. Sorting and formatting arguments passed to other options are ignored; however, most filtering arguments are still used.

:   

[ ]{#lbAF}

## JOB REASON CODES

These codes identify the reason that a job has not been started by the scheduler. There may be multiple reasons why a job cannot start yet, in which case only the reason that was encountered by the attempted scheduling method will be displayed.

The Reasons listed below are some of the more common ones you might see. For a full list of Reason codes refer to this page: \<[https://slurm.schedmd.com/job_reason_codes.html](job_reason_codes.md)\>

**AssocGrp\*Limit**
:   The job\'s association has reached an aggregate limit on some resource.

:   

**AssociationJobLimit**
:   The job\'s association has reached its maximum job count.

:   

**AssocMax\*Limit**
:   The job requests a resource that violates a per-job limit on the requested association.

:   

**AssociationResourceLimit**
:   The job\'s association has reached some resource limit.

:   

**AssociationTimeLimit**
:   The job\'s association has reached its time limit.

:   

**BadConstraints**
:   The job\'s constraints can not be satisfied.

:   

**BeginTime**
:   The job\'s earliest start time has not yet been reached.

:   

**Cleaning**
:   The job is being requeued and still cleaning up from its previous execution.

:   

**Dependency**
:   This job has a dependency on another job that has not been satisfied.

:   

**DependencyNeverSatisfied**
:   This job has a dependency on another job that will never be satisfied.

:   

**InactiveLimit**
:   The job reached the system InactiveLimit.

:   

**InvalidAccount**
:   The job\'s account is invalid.

:   

**InvalidQOS**
:   The job\'s QOS is invalid.

:   

**JobHeldAdmin**
:   The job is held by a system administrator.

:   

**JobHeldUser**
:   The job is held by the user.

:   

**JobLaunchFailure**
:   The job could not be launched. This may be due to a file system problem, invalid program name, etc.

:   

**Licenses**
:   The job is waiting for a license.

:   

**NodeDown**
:   A node required by the job is down.

:   

**NonZeroExitCode**
:   The job terminated with a non-zero exit code.

:   

**PartitionDown**
:   The partition required by this job is in a DOWN state.

:   

**PartitionInactive**
:   The partition required by this job is in an Inactive state and not able to start jobs.

:   

**PartitionNodeLimit**
:   The number of nodes required by this job is outside of its partition\'s current limits. Can also indicate that required nodes are DOWN or DRAINED.

:   

**PartitionTimeLimit**
:   The job\'s time limit exceeds its partition\'s current time limit.

:   

**Priority**
:   One or more higher priority jobs exist for this partition or advanced reservation.

:   

**Prolog**
:   Its Prolog program is still running.

:   

**QOSGrp\*Limit**
:   The job\'s QOS has reached an aggregate limit on some resource.

:   

**QOSJobLimit**
:   The job\'s QOS has reached its maximum job count.

:   

**QOSMax\*Limit**
:   The job requests a resource that violates a per-job limit on the requested QOS.

:   

**QOSResourceLimit**
:   The job\'s QOS has reached some resource limit.

:   

**QOSTimeLimit**
:   The job\'s QOS has reached its time limit.

:   

**QOSUsageThreshold**
:   Required QOS threshold has been breached.

:   

**ReqNodeNotAvail**
:   Some node specifically required by the job is not currently available. The node may currently be in use, reserved for another job, in an advanced reservation, DOWN, DRAINED, or not responding. Nodes which are DOWN, DRAINED, or not responding will be identified as part of the job\'s \"reason\" field as \"UnavailableNodes\". Such nodes will typically require the intervention of a system administrator to make available.

:   

**Reservation**
:   The job is waiting its advanced reservation to become available.

:   

**Resources**
:   The job is waiting for resources to become available.

:   

**SystemFailure**
:   Failure of the Slurm system, a file system, the network, etc.

:   

**TimeLimit**
:   The job exhausted its time limit.

:   

**WaitingForScheduling**
:   No reason has been set for this job yet. Waiting for the scheduler to determine the appropriate reason.

:   

[ ]{#lbAG}

## JOB STATE CODES

Jobs typically pass through several states in the course of their execution. The typical states are PENDING, RUNNING, SUSPENDED, COMPLETING, and COMPLETED. The following states are recognized by squeue. A full list of possible states is available at \<[https://slurm.schedmd.com/job_state_codes.html](job_state_codes.md)\>.

**BF BOOT_FAIL**
:   Job terminated due to launch failure, typically due to a hardware failure (e.g. unable to boot the node or block and the job can not be requeued).

:   

**CA CANCELLED**
:   Job was explicitly cancelled by the user or system administrator. The job may or may not have been initiated.

:   

**CD COMPLETED**
:   Job has terminated all processes on all nodes with an exit code of zero.

:   

**CF CONFIGURING**
:   Job has been allocated resources, but are waiting for them to become ready for use (e.g. booting).

:   

**CG COMPLETING**
:   Job is in the process of completing. Some processes on some nodes may still be active.

:   

**DL DEADLINE**
:   Job terminated on deadline.

:   

**F FAILED**
:   Job terminated with non-zero exit code or other failure condition.

:   

**NF NODE_FAIL**
:   Job terminated due to failure of one or more allocated nodes.

:   

**OOM OUT_OF_MEMORY**
:   Job experienced out of memory error.

:   

**PD PENDING**
:   Job is awaiting resource allocation.

:   

**PR PREEMPTED**
:   Job terminated due to preemption.

:   

**R RUNNING**
:   Job currently has an allocation.

:   

**RD RESV_DEL_HOLD**
:   Job is being held after requested reservation was deleted.

:   

**RF REQUEUE_FED**
:   Job is being requeued by a federation.

:   

**RH REQUEUE_HOLD**
:   Held job is being requeued.

:   

**RQ REQUEUED**
:   Completing job is being requeued.

:   

**RS RESIZING**
:   Job is about to change size.

:   

**RV REVOKED**
:   Sibling was removed from cluster due to other cluster starting the job.

:   

**SI SIGNALING**
:   Job is being signaled.

:   

**SE SPECIAL_EXIT**
:   The job was requeued in a special state. This state can be set by users, typically in EpilogSlurmctld, if the job has terminated with a particular exit value.

:   

**SO STAGE_OUT**
:   Job is staging out files.

:   

**ST STOPPED**
:   Job has an allocation, but execution has been stopped with SIGSTOP signal. CPUS have been retained by this job.

:   

**S SUSPENDED**
:   Job has an allocation, but execution has been suspended and CPUs have been released for other jobs.

:   

**TO TIMEOUT**
:   Job terminated upon reaching its time limit.

:   

[ ]{#lbAH}

## PERFORMANCE

Executing **squeue** sends a remote procedure call to **slurmctld**. If enough calls from **squeue** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **squeue** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **squeue** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAI}

## ENVIRONMENT VARIABLES

Some **squeue** options may be set via environment variables. These environment variables, along with their corresponding options, are listed below. (Note: Command line options will always override these settings.)

**SLURM_BITSTR_LEN**
:   Specifies the string length to be used for holding a job array\'s task ID expression. The default value is 64 bytes. A value of 0 will print the full expression with any length required. Larger values may adversely impact the application performance.

:   

**SLURM_CLUSTERS**
:   Same as **\--clusters**

:   

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for squeue to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

**SLURM_JSON**
:   Control JSON serialization:

:   

    :   

        **compact**
        :   Output JSON as compact as possible.

        :   

        **pretty**
        :   Output JSON in pretty format to make it more readable.

        :   

**SLURM_TIME_FORMAT**
:   Specify the format used to report time stamps. A value of *standard*, the default value, generates output in the form \"year-month-dateThour:minute:second\". A value of *relative* returns only \"hour:minute:second\" if the current day. For other dates in the current year it prints the \"hour:minute\" preceded by \"Tomorr\" (tomorrow), \"Ystday\" (yesterday), the name of the day for the coming week (e.g. \"Mon\", \"Tue\", etc.), otherwise the date (e.g. \"25 Apr\"). For other years it returns a date month and year without a time (e.g. \"6 Jun 2012\"). All of the time stamps use a 24 hour format.
    A valid strftime() format can also be specified. For example, a value of \"%a %T\" will report the day of the week and a time stamp (e.g. \"Mon 12:34:56\").

:   

**SLURM_YAML**
:   Control YAML serialization:

:   

    :   

        **compact** Output YAML as compact as possible.

        :   

        :   

        **pretty** Output YAML in pretty format to make it more readable.

        :   

:   

**SQUEUE_ACCOUNT**
:   **-A \<account_list\>, \--account=\<account_list\>**

:   

**SQUEUE_ALL**
:   **-a, \--all**

:   

**SQUEUE_ARRAY**
:   **-r, \--array**

:   

**SQUEUE_NAMES**
:   **\--name=\<name_list\>**

:   

**SQUEUE_FEDERATION**
:   **\--federation**

:   

**SQUEUE_FORMAT**
:   **-o \<output_format\>, \--format=\<output_format\>**

:   

**SQUEUE_FORMAT2**
:   **-O \<output_format\>, \--Format=\<output_format\>**

:   

**SQUEUE_LICENSES**
:   **-p-l \<license_list\>, \--license=\<license_list\>**

:   

**SQUEUE_LOCAL**
:   **\--local**

:   

**SQUEUE_PARTITION**
:   **-p \<part_list\>, \--partition=\<part_list\>**

:   

**SQUEUE_PRIORITY**
:   **-P**, **\--priority**

:   

**SQUEUE_QOS**
:   **-p \<qos_list\>, \--qos=\<qos_list\>**

:   

**SQUEUE_SIBLING**
:   **\--sibling**

:   

**SQUEUE_SORT**
:   **-S \<sort_list\>, \--sort=\<sort_list\>**

:   

**SQUEUE_STATES**
:   **-t \<state_list\>, \--states=\<state_list\>**

:   

**SQUEUE_USERS**
:   **-u \<user_list\>, \--users=\<user_list\>**

:   

[ ]{#lbAJ}

## EXAMPLES

Print the jobs scheduled in the debug partition and in the COMPLETED state in the format with six right justified digits for the job id followed by the priority with an arbitrary fields size:

:   

:   $ squeue -p debug -t COMPLETED -o "%.6i %p"
         JOBID PRIORITY
         65543 99993
         65544 99992
         65545 99991

Print the job steps in the debug partition sorted by user:

:   

:   $ squeue -s -p debug -S u
          STEPID        NAME PARTITION     USER      TIME NODELIST
         65552.1       test1     debug    alice      0:23 dev[1-4]
         65562.2     big_run     debug      bob      0:18 dev22
         65550.1      param1     debug  candice   1:43:21 dev[6-12]

Print information only about jobs 12345, 12346 and 12348:

:   

:   $ squeue --jobs 12345,12346,12348
         JOBID PARTITION NAME USER ST  TIME  NODES NODELIST(REASON)
         12345     debug job1 dave  R   0:21     4 dev[9-12]
         12346     debug job2 dave PD   0:00     8 (Resources)
         12348     debug job3 ed   PD   0:00     4 (Priority)

Print information only about job step 65552.1:

:   

:   $ squeue --steps 65552.1
          STEPID     NAME PARTITION    USER    TIME  NODELIST
         65552.1    test2     debug   alice   12:49  dev[1-4]

[ ]{#lbAK}

## COPYING

Copyright (C) 2002-2007 The Regents of the University of California. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2008-2010 Lawrence Livermore National Security.\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. [ ]{#lbAL}

## SEE ALSO

**[scancel](scancel.md)**(1), **[scontrol](scontrol.md)**(1), **[sinfo](sinfo.md)**(1), **[srun](srun.md)**(1), **slurm_load_ctl_conf** (3), **slurm_load_jobs** (3), **slurm_load_node** (3), **slurm_load_partitions** (3)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

SYNOPSIS

:   

DESCRIPTION

:   

OPTIONS

:   

JOB REASON CODES

:   

JOB STATE CODES

:   

PERFORMANCE

:   

ENVIRONMENT VARIABLES

:   

EXAMPLES

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
