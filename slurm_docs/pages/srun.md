# srun

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

srun - Run parallel jobs

[ ]{#lbAC}

## SYNOPSIS

**srun** \[*OPTIONS(0)*\... \[*executable(0)* \[*args(0)*\...\]\]\] \[ : \[*OPTIONS(N)*\...\]\] *executable(N)* \[*args(N)*\...\]

Option(s) define multiple jobs in a co-scheduled heterogeneous job. For more details about heterogeneous jobs see the document\
[https://slurm.schedmd.com/heterogeneous_jobs.html](heterogeneous_jobs.md)

[ ]{#lbAD}

## DESCRIPTION

Run a parallel job on cluster managed by Slurm. If necessary, srun will first create a resource allocation in which to run the parallel job.

The following document describes the influence of various options on the allocation of cpus to jobs and tasks.\
[https://slurm.schedmd.com/cpu_management.html](cpu_management.md)

[ ]{#lbAE}

## RETURN VALUE

srun will return the highest exit code of all tasks run or the highest signal (with the high-order bit set in an 8-bit integer \-- e.g. 128 + signal) of any task that exited with a signal.\
The value 253 is reserved for out-of-memory errors.

[ ]{#lbAF}

## EXECUTABLE PATH RESOLUTION

The executable is resolved in the following order:\

1\. If executable starts with \".\", then path is constructed as: current working directory / executable\
2. If executable starts with a \"/\", then path is considered absolute.\
3. If executable can be resolved through PATH. See **path_resolution**(7).\
4. If executable is in current working directory.\

Current working directory is the calling process working directory unless the **\--chdir** argument is passed, which will override the current working directory.

[ ]{#lbAG}

## OPTIONS

**-A**, **\--account**=\<*account*\>

Charge resources used by this job to specified account. The *account* is an arbitrary string. The account name may be changed after job submission using the **scontrol** command. This option applies to job allocations.

**\--acctg-freq**=\<*datatype*\>=\<*interval*\>\[,\<*datatype*\>=\<*interval*\>\...\]

Define the job accounting and profiling sampling intervals in seconds. This can be used to override the *JobAcctGatherFrequency* parameter in the slurm.conf file. \<*datatype*\>=\<*interval*\> specifies the task sampling interval for the jobacct_gather plugin or a sampling interval for a profiling type by the acct_gather_profile plugin. Multiple comma-separated \<*datatype*\>=\<*interval*\> pairs may be specified. Supported *datatype* values are:

:   

    **task**
    :   Sampling interval for the jobacct_gather plugins and for task profiling by the acct_gather_profile plugin.\
        **NOTE**: This frequency is used to monitor memory usage. If memory limits are enforced the highest frequency a user can request is what is configured in the slurm.conf file. It can not be disabled.

    :   

    **energy**
    :   Sampling interval for energy profiling using the acct_gather_energy plugin.

    :   

    **network**
    :   Sampling interval for infiniband profiling using the acct_gather_interconnect plugin.

    :   

    **filesystem**
    :   Sampling interval for filesystem profiling using the acct_gather_filesystem plugin.

    The default value for the task sampling interval is 30 seconds. The default value for all other intervals is 0. An interval of 0 disables sampling of the specified type. If the task sampling interval is 0, accounting information is collected only at job termination (reducing Slurm interference with the job).\
    Smaller (non-zero) values have a greater impact upon job performance, but a value of 30 seconds is not likely to be noticeable for applications having less than 10,000 tasks. This option applies to job allocations.

**\--bb**=\<*spec*\>

Burst buffer specification. The form of the specification is system dependent. Also see **\--bbf**. This option applies to job allocations. When the **\--bb** option is used, Slurm parses this option and creates a temporary burst buffer script file that is used internally by the burst buffer plugins. See Slurm\'s burst buffer guide for more information and examples:\
[https://slurm.schedmd.com/burst_buffer.html](burst_buffer.md)

**\--bbf**=\<*file_name*\>

Path of file containing burst buffer specification. The form of the specification is system dependent. Also see **\--bb**. This option applies to job allocations. See Slurm\'s burst buffer guide for more information and examples:\
[https://slurm.schedmd.com/burst_buffer.html](burst_buffer.md)

**\--bcast**\[=\<*dest_path*\>\]

Copy executable file to allocated compute nodes. If a file name is specified, copy the executable to the specified destination file path. If the path specified ends with \'/\' it is treated as a target directory, and the destination file name will be slurm_bcast\_\<job_id\>.\<step_id\>\_\<nodename\>. If no dest_path is specified and the slurm.conf **BcastParameters** **DestDir** is configured then it is used, and the filename follows the above pattern. If none of the previous is specified, then **\--chdir** is used, and the filename follows the above pattern too. For example, \"srun \--bcast=/tmp/mine -N3 a.out\" will copy the file \"a.out\" from your current directory to the file \"/tmp/mine\" on each of the three allocated compute nodes and execute that file. This option applies to step allocations.

**\--bcast-exclude**={NONE\|\<*exclude_path*\>\[,\<*exclude_path*\>\...\]}

Comma-separated list of absolute directory paths to be excluded when autodetecting and broadcasting executable shared object dependencies through **\--bcast**. If the keyword \"*NONE*\" is configured, no directory paths will be excluded. The default value is that of slurm.conf **BcastExclude** and this option overrides it. See also **\--bcast** and **\--send-libs**.

**-b**, **\--begin**=\<*time*\>

Defer initiation of this job until the specified time. It accepts times of the form *HH:MM:SS* to run a job at a specific time of day (seconds are optional). (If that time is already past, the next day is assumed.) You may also specify *midnight*, *noon*, *elevenses* (11 AM), *fika* (3 PM) or *teatime* (4 PM) and you can have a time-of-day suffixed with *AM* or *PM* for running in the morning or the evening. You can also say what day the job will be run, by specifying a date of the form *MMDDYY* or *MM/DD/YY* *YYYY-MM-DD*. Combine date and time using the following format *YYYY-MM-DD\[THH:MM\[:SS\]\]*. You can also give times like *now + count time-units*, where the time-units can be *seconds* (default), *minutes*, *hours*, *days*, or *weeks* and you can tell Slurm to run the job today with the keyword *today* and to run the job tomorrow with the keyword *tomorrow*. The value may be changed after job submission using the **scontrol** command. For example:

       --begin=16:00
       --begin=now+1hour
       --begin=now+60           (seconds by default)
       --begin=2010-01-20T12:34:00

:   Notes on date/time specifications:\
     - Although the \'seconds\' field of the HH:MM:SS time specification is allowed by the code, note that the poll time of the Slurm scheduler is not precise enough to guarantee dispatch of the job on the exact second. The job will be eligible to start on the next poll following the specified time. The exact poll interval depends on the Slurm scheduler (e.g., 60 seconds with the default sched/builtin).\
     - If no time (HH:MM:SS) is specified, the default is (00:00:00).\
     - If a date is specified without a year (e.g., MM/DD) then the current year is assumed, unless the combination of MM/DD and HH:MM:SS has already passed for that year, in which case the next year is used.\
    This option applies to job allocations.

**-D**, **\--chdir**=\<*path*\>

Have the remote processes do a chdir to *path* before beginning execution. The default is to chdir to the current working directory of the **srun** process. The path can be specified as full path or relative path to the directory where the command is executed. This option applies to job allocations.

**\--cluster-constraint**=\<*list*\>

Specifies features that a federated cluster must have to have a sibling job submitted to it. Slurm will attempt to submit a sibling job to a cluster if it has at least one of the specified features.

**-M**, **\--clusters**=\<*string*\>

Clusters to issue commands to. Multiple cluster names may be comma separated. The job will be submitted to the one cluster providing the earliest expected job initiation time. The default value is the current cluster. A value of \'*all*\' will query to run on all clusters. Note the **\--export** option to control environment variables exported between clusters. This option applies only to job allocations. Note that the **slurmdbd** must be up for this option to work properly, unless running in a federation with **FederationParameters=fed_display** configured.

**\--comment**=\<*string*\>

An arbitrary comment. This option applies to job allocations.

**\--compress**\[=*type*\]

Compress file before sending it to compute hosts. The optional argument specifies the data compression library to be used. The default is **BcastParameters** **Compression=** if set or \"lz4\" otherwise. Supported values are \"lz4\". Some compression libraries may be unavailable on some systems. For use with the **\--bcast** option. This option applies to step allocations.

**\--consolidate-segments**

Ensure that all segments from the allocation will be consolidated into one higher-level aggregated block.

This option applies to job allocations. **NOTE**: This option will only work with the **topology/block** plugin.

**-C**, **\--constraint**=\<*list*\>

Nodes can have **features** assigned to them by the Slurm administrator. Users can specify which of these **features** are required by their job using the constraint option. If you are looking for \'soft\' constraints please see **\--prefer** for more information. Only nodes having features matching the job constraints will be used to satisfy the request. Multiple constraints may be specified with AND, OR, matching OR, resource counts, etc. (some operators are not supported on all system types).

**NOTE**: Changeable features are features defined by a NodeFeatures plugin.

Supported **\--constraint** options include:

:   

    **Single Name**
    :   Only nodes which have the specified feature will be used. For example, **\--constraint=\"intel\"**

    :   

    **Node Count**
    :   A request can specify the number of nodes needed with some feature by appending an asterisk and count after the feature name. For example, **\--nodes=16 \--constraint=\"graphics\*4\"** indicates that the job requires 16 nodes and that at least four of those nodes must have the feature \"graphics.\" If requesting more than one feature and using node counts, the request must have square brackets surrounding it.
        **NOTE**: This option is not supported by the helpers NodeFeatures plugin. Heterogeneous jobs can be used instead.

    :   

    **AND**
    :   Only nodes with all of specified features will be used. The ampersand is used for an AND operator. For example, **\--constraint=\"intel&gpu\"**

    :   

    **OR**
    :   Only nodes with at least one of specified features will be used. The vertical bar is used for an OR operator. If changeable features are not requested, nodes in the allocation can have different features. For example, **salloc -N2 \--constraint=\"intel\|amd\"** can result in a job allocation where one node has the intel feature and the other node has the amd feature. However, if the expression contains a changeable feature, then all OR operators are automatically treated as Matching OR so that all nodes in the job allocation have the same set of features. For example, **salloc -N2 \--constraint=\"foo\|bar&baz\"** The job is allocated two nodes where both nodes have foo, or bar and baz (one or both nodes could have foo, bar, and baz). The helpers NodeFeatures plugin will find the first set of node features that matches all nodes in the job allocation; these features are set as active features on the node and passed to RebootProgram (see **[slurm.conf](slurm.conf.md)**(5)) and the helper script (see **[helpers.conf](helpers.conf.md)**(5)). In this case, the helpers plugin uses the first of \"foo\" or \"bar,baz\" that match the two nodes in the job allocation.

    :   

    **Matching OR**
    :   If only one of a set of possible options should be used for all allocated nodes, then use the OR operator and enclose the options within square brackets. For example, **\--constraint=\"\[rack1\|rack2\|rack3\|rack4\]\"** might be used to specify that all nodes must be allocated on a single rack of the cluster, but any of those four racks can be used.

    :   

    **Multiple Counts**

    :   Specific counts of multiple resources may be specified by using the AND operator and enclosing the options within square brackets. For example, **\--constraint=\"\[rack1\*2&rack2\*4\]\"** might be used to specify that two nodes must be allocated from nodes with the feature of \"rack1\" and four nodes must be allocated from nodes with the feature \"rack2\".

        **NOTE**: This option is not supported by the helpers NodeFeatures plugin.

        **NOTE**: Multiple Counts can cause jobs to be allocated with a non-optimal network layout.

    :   

    **Brackets**

    :   Brackets can be used to indicate that you are looking for a set of nodes with the different requirements contained within the brackets. For example, **\--constraint=\"\[(rack1\|rack2)\*1&(rack3)\*2\]\"** will get you one node with either the \"rack1\" or \"rack2\" features and two nodes with the \"rack3\" feature. If requesting more than one feature and using node counts, the request must have square brackets surrounding it.

        **NOTE**: Brackets are only reserved for **Multiple Counts** and **Matching OR** syntax. AND operators require a count for each feature inside square brackets (i.e. \"\[quad\*2&hemi\*1\]\"). Slurm will only allow a single set of bracketed constraints per job.

        **NOTE**: Square brackets are not supported by the helpers NodeFeatures plugin. Matching OR can be requested without square brackets by using the vertical bar character with at least one changeable feature.

    :   

    **Parentheses**
    :   Parentheses can be used to group like node features together. For example, **\--constraint=\"\[(knl&snc4&flat)\*4&haswell\*1\]\"** might be used to specify that four nodes with the features \"knl\", \"snc4\" and \"flat\" plus one node with the feature \"haswell\" are required. Parentheses can also be used to group operations. Without parentheses, node features are parsed strictly from left to right. For example, **\--constraint=\"foo&bar\|baz\"** requests nodes with foo and bar, or baz. **\--constraint=\"foo\|bar&baz\"** requests nodes with foo and baz, or bar and baz (note how baz was AND\'d with everything). **\--constraint=\"foo&(bar\|baz)\"** requests nodes with foo and at least one of bar or baz. **NOTE**: OR within parentheses should not be used with a KNL NodeFeatures plugin but is supported by the helpers NodeFeatures plugin.

<!-- -->

:   **WARNING**: When srun is executed from within salloc or sbatch, the constraint value can only contain a single feature name. None of the other operators are currently supported for job steps.\
    This option applies to job and step allocations.

**\--container**=\<*path_to_container*\>

Absolute path to OCI container bundle.

**\--container-id**=\<*container_id*\>

Unique name for OCI container.

**\--contiguous**

If set, then the allocated nodes must form a contiguous set.

**NOTE**: This option will only work with the **topology/flat** plugin. Other topology plugins modify the node ordering and prevent this option from taking effect. This option applies to job allocations.

**-S**, **\--core-spec**=\<*num*\>

Count of Specialized Cores per node reserved by the job for system operations and not used by the application. If AllowSpecResourcesUsage is enabled a job can override the CoreSpecCount of all its allocated nodes with this option. The overridden Specialized Cores will still be reserved for system processes. The job will get an implicit **\--exclusive** allocation for the rest of the Cores on the nodes, resulting in the job\'s processes being able to use (and being charged for) all the Cores on the nodes except for the overridden Specialized Cores. This option can not be used with the **\--thread-spec** option.

**NOTE**: Explicitly setting a job\'s specialized core value implicitly sets the \--exclusive option.

**NOTE**: This option may implicitly impact the number of tasks if **-n** was not specified.

This option applies to job allocations.

**\--cores-per-socket**=\<*cores*\>

Restrict node selection to nodes with at least the specified number of cores per socket. See additional information under **-B** option above when task/affinity plugin is enabled. This option applies to job allocations.

**\--cpu-bind**=\[{quiet\|verbose},\]\<*type*\>

Bind tasks to CPUs. Used only when the task/affinity plugin is enabled. **NOTE**: To have Slurm always report on the selected CPU binding for all commands executed in a shell, you can enable verbose mode by setting the SLURM_CPU_BIND environment variable value to \"verbose\".

The following informational environment variables are set when **\--cpu-bind** is in use:

            SLURM_CPU_BIND_VERBOSE
            SLURM_CPU_BIND_TYPE
            SLURM_CPU_BIND_LIST

See the **ENVIRONMENT VARIABLES** section for a more detailed description of the individual SLURM_CPU_BIND variables. These variables are available only if the task/affinity plugin is configured.

When using **\--cpus-per-task** to run multithreaded tasks, be aware that CPU binding is inherited from the parent of the process. This means that the multithreaded task should either specify or clear the CPU binding itself to avoid having all threads of the multithreaded task use the same mask/CPU as the parent. Alternatively, fat masks (masks which specify more than one allowed CPU) could be used for the tasks in order to provide multiple CPUs for the multithreaded tasks.

Note that a job step can be allocated different numbers of CPUs on each node or be allocated CPUs not starting at location zero. Therefore one of the options which automatically generate the task binding is recommended. Explicitly specified masks or bindings are only honored when the job step has been allocated every available CPU on the node.

Binding a task to a NUMA locality domain means to bind the task to the set of CPUs that belong to the NUMA locality domain or \"NUMA node\". If NUMA locality domain options are used on systems with no NUMA support, then each socket is considered a locality domain.

If the **\--cpu-bind** option is not used, the default binding mode will depend upon Slurm\'s configuration and the step\'s resource allocation. If all allocated nodes have the same configured CpuBind mode, that will be used. Otherwise if the job\'s Partition has a configured CpuBind mode, that will be used. Otherwise if Slurm has a configured TaskPluginParam value, that mode will be used. Otherwise automatic binding will be performed as described below.

:   

    **Auto Binding**
    :   Applies only when task/affinity is enabled. If the job step allocation includes an allocation with a number of sockets, cores, or threads equal to the number of tasks times cpus-per-task, then the tasks will by default be bound to the appropriate resources (auto binding). Disable this mode of operation by explicitly setting \"\--cpu-bind=none\". Use TaskPluginParam=autobind=\[threads\|cores\|sockets\] to set a default cpu binding in case \"auto binding\" doesn\'t find a match.

<!-- -->

:   Supported options include:

    :   

        **q\[uiet\]**

        :   

        :   Quietly bind before task runs (default)

        :   

        **v\[erbose\]**

        :   

        :   Verbosely report binding before task runs

        :   

        **no\[ne\]**

        :   

        :   Do not bind tasks to CPUs (default unless auto binding is applied)

        :   

        **map_cpu:\<list\>**

        :   

        :   Bind by setting CPU masks on tasks (or ranks) as specified where \<list\> is \<cpu_id_for_task_0\>,\<cpu_id_for_task_1\>,\... If the number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list. To simplify support for large task counts, the lists may follow a map with an asterisk and repetition count. For example \"map_cpu:0\*4,3\*4\".

        :   

        **mask_cpu:\<list\>**

        :   

        :   Bind by setting CPU masks on tasks (or ranks) as specified where \<list\> is \<cpu_mask_for_task_0\>,\<cpu_mask_for_task_1\>,\... The mapping is specified for a node and identical mapping is applied to the tasks on every node (i.e. the lowest task ID on each node is mapped to the first mask specified in the list, etc.). CPU masks are **always** interpreted as hexadecimal values but can be preceded with an optional \'0x\'. If the number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list. To simplify support for large task counts, the lists may follow a map with an asterisk and repetition count. For example \"mask_cpu:0x0f\*4,0xf0\*4\".

        :   

        **rank_ldom**

        :   

        :   Bind to a NUMA locality domain by rank. Not supported unless the entire node is allocated to the job.

        :   

        **map_ldom:\<list\>**

        :   

        :   Bind by mapping NUMA locality domain IDs to tasks as specified where \<list\> is \<ldom1\>,\<ldom2\>,\...\<ldomN\>. The locality domain IDs are interpreted as decimal values unless they are preceded with \'0x\' in which case they are interpreted as hexadecimal values. Not supported unless the entire node is allocated to the job.

        :   

        **mask_ldom:\<list\>**

        :   

        :   Bind by setting NUMA locality domain masks on tasks as specified where \<list\> is \<mask1\>,\<mask2\>,\...\<maskN\>. NUMA locality domain masks are **always** interpreted as hexadecimal values but can be preceded with an optional \'0x\'. Not supported unless the entire node is allocated to the job.

        :   

        **sockets**

        :   

        :   Automatically generate masks binding tasks to sockets. Only the CPUs on the socket which have been allocated to the job will be used. If the number of tasks differs from the number of allocated sockets this can result in sub-optimal binding.

        :   

        **cores**

        :   

        :   Automatically generate masks binding tasks to cores. If the number of tasks differs from the number of allocated cores this can result in sub-optimal binding.

        :   

        **threads**

        :   

        :   Automatically generate masks binding tasks to threads. If the number of tasks differs from the number of allocated threads this can result in sub-optimal binding.

        :   

        **ldoms**

        :   

        :   Automatically generate masks binding tasks to NUMA locality domains. If the number of tasks differs from the number of allocated locality domains this can result in sub-optimal binding.

        :   

        **help**

        :   

        :   Show help message for cpu-bind

    :   

    This option applies to job and step allocations.

    :   

**\--cpu-freq**=\<*p1*\>\[-*p2*\]\[:*p3*\]

Request that the job step initiated by this srun command be run at some requested frequency if possible, on the CPUs selected for the step on the compute node(s).

**p1** can be \[#### \| low \| medium \| high \| highm1\] which will set the frequency scaling_speed to the corresponding value, and set the frequency scaling_governor to UserSpace. See below for definition of the values.

**p1** can be \[Conservative \| OnDemand \| Performance \| PowerSave\] which will set the scaling_governor to the corresponding value. The governor has to be in the list set by the slurm.conf option CpuFreqGovernors.

When **p2** is present, **p1** will be the minimum scaling frequency and **p2** will be the maximum scaling frequency. In that case the governor **p3** or CpuFreqDef cannot be UserSpace since it doesn\'t support a range.

**p2** can be \[#### \| medium \| high \| highm1\]. p2 must be greater than p1 and is incompatible with UserSpace governor.

**p3** can be \[Conservative \| OnDemand \| Performance \| PowerSave \| SchedUtil \| UserSpace\] which will set the governor to the corresponding value.

If **p3** is UserSpace, the frequency scaling_speed, scaling_max_freq and scaling_min_freq will be statically set to the value defined by **p1**.

Any requested frequency below the minimum available frequency will be rounded to the minimum available frequency. In the same way, any requested frequency above the maximum available frequency will be rounded to the maximum available frequency.

The **CpuFreqDef** parameter in slurm.conf will be used to set the governor in absence of **p3**. If there\'s no **CpuFreqDef**, the default governor will be to use the system current governor set in each cpu. Specifying a range without **CpuFreqDef** or a specific governor is therefore not allowed.

Acceptable values at present include:

**\####**

frequency in kilohertz

**Low**

the lowest available frequency

**High**

the highest available frequency

**HighM1**

(high minus one) will select the next highest available frequency

**Medium**

attempts to set a frequency in the middle of the available range

**Conservative**

attempts to use the Conservative CPU governor

**OnDemand**

attempts to use the OnDemand CPU governor (the default value)

**Performance**

attempts to use the Performance CPU governor

**PowerSave**

attempts to use the PowerSave CPU governor

**UserSpace**

attempts to use the UserSpace CPU governor

The following informational environment variable is set in the job step when **\--cpu-freq** option is requested.

            SLURM_CPU_FREQ_REQ

This environment variable can also be used to supply the value for the CPU frequency request if it is set when the \'srun\' command is issued. The **\--cpu-freq** on the command line will override the environment variable value. The form on the environment variable is the same as the command line. See the **ENVIRONMENT VARIABLES** section for a description of the SLURM_CPU_FREQ_REQ variable.

**NOTE**: This parameter is treated as a request, not a requirement. If the job step\'s node does not support setting the CPU frequency, or the requested value is outside the bounds of the legal frequencies, an error is logged, but the job step is allowed to continue.

**NOTE**: Setting the frequency for just the CPUs of the job step implies that the tasks are confined to those CPUs. If task confinement (i.e. the task/affinity TaskPlugin is enabled, or the task/cgroup TaskPlugin is enabled with \"ConstrainCores=yes\" set in cgroup.conf) is not configured, this parameter is ignored.

**NOTE**: When the step completes, the frequency and governor of each selected CPU is reset to the previous values.

**NOTE**: When submitting jobs with the **\--cpu-freq** option with linuxproc as the ProctrackType can cause jobs to run too quickly before Accounting is able to poll for job information. As a result not all of accounting information will be present.

This option applies to job and step allocations.

**\--cpus-per-gpu**=\<*ncpus*\>

Request that *ncpus* processors be allocated per allocated GPU. This option implies \--exact. Not compatible with the **\--cpus-per-task** option.

This option applies to job and step allocations.

**-c**, **\--cpus-per-task**=\<*ncpus*\>

Request that *ncpus* be allocated **per process**. This may be useful if the job is multithreaded and requires more than one CPU per task for optimal performance. Explicitly requesting this option implies **\--exact**. The default is one CPU per process and does not imply **\--exact**. If **-c** is specified without **-n**, as many tasks will be allocated per node as possible while satisfying the **-c** restriction. For instance on a cluster with 8 CPUs per node, a job request for 4 nodes and 3 CPUs per task may be allocated 3 or 6 CPUs per node (1 or 2 tasks per node) depending upon resource consumption by other jobs. Such a job may be unable to execute more than a total of 4 tasks.

**WARNING**: There are configurations and options interpreted differently by job and job step requests which can result in inconsistencies for this option. For example *srun -c2 \--threads-per-core=1 prog* may allocate two cores for the job, but if each of those cores contains two threads, the job allocation will include four CPUs. The job step allocation will then launch two threads per CPU for a total of two tasks.

**WARNING**: When srun is executed from within salloc or sbatch, there are configurations and options which can result in inconsistent allocations when -c has a value greater than -c on salloc or sbatch.

**NOTE**: If **\--mem-per-cpu** is also specified, the number of allocated cpus can be increased if **MaxMemPerCPU** is exceeded. In the case **-n** is not specified, the number of tasks can be higher than expected.

This option applies to job and step allocations.

**\--deadline**=\<*OPT*\>

Remove the job if no ending is possible before this deadline (start \> (deadline - time\[-min\])). Default is no deadline. Note that if neither **DefaultTime** nor **MaxTime** are configured on the partition the job is in, the job will need to specify some form of time limit (\--time\[-min\]) if a deadline is to be used.

Valid time formats are:\
HH:MM\[:SS\] \[AM\|PM\]\
MMDD\[YY\] or MM/DD\[/YY\] or MM.DD\[.YY\]\
MM/DD\[/YY\]-HH:MM\[:SS\]\
YYYY-MM-DD\[THH:MM\[:SS\]\]\]\
now\[+*count*\[seconds(default)\|minutes\|hours\|days\|weeks\]\]

This option applies only to job allocations.

**\--delay-boot**=\<*minutes*\>

Do not reboot nodes in order to satisfied this job\'s feature specification if the job has been eligible to run for less than this time period. If the job has waited for less than the specified period, it will use only nodes which already have the specified features. The argument is in units of minutes. A default value may be set by a system administrator using the **delay_boot** option of the **SchedulerParameters** configuration parameter in the slurm.conf file, otherwise the default value is zero (no delay).

This option applies only to job allocations.

**-d**, **\--dependency**=\<*dependency_list*\>

Defer the start of this job until the specified dependencies have been satisfied. Once a dependency is satisfied, it is removed from the job. This option does not apply to job steps (executions of srun within an existing salloc or sbatch allocation) only to job allocations. \<*dependency_list*\> is of the form \<*type:job_id\[:job_id\]\[,type:job_id\[:job_id\]\]*\> or \<*type:job_id\[:job_id\]\[?type:job_id\[:job_id\]\]*\>. All dependencies must be satisfied if the \",\" separator is used. Any dependency may be satisfied if the \"?\" separator is used. Only one separator may be used. For instance:

    -d afterok:20:21,afterany:23

means that the job can run only after a 0 return code of jobs 20 and 21 AND the completion of job 23. However:

    -d afterok:20:21?afterany:23

means that any of the conditions (afterok:20 OR afterok:21 OR afterany:23) will be enough to release the job. Many jobs can share the same dependency and these jobs may even belong to different users. The value may be changed after job submission using the scontrol command. Dependencies on remote jobs are allowed in a federation. Once a job dependency fails due to the termination state of a preceding job, the dependent job will never be run, even if the preceding job is requeued and has a different termination state in a subsequent execution. This option applies to job allocations.

:   

    **after:job_id\[\[+time\]\[:jobid\[+time\]\...\]\]**
    :   After the specified jobs start or are cancelled and \'time\' in minutes from job start or cancellation happens, this job can begin execution. If no \'time\' is given then there is no delay after start or cancellation.

    :   

    **afterany:job_id\[:jobid\...\]**
    :   This job can begin execution after the specified jobs have terminated. This is the default dependency type.

    :   

    **afterburstbuffer:job_id\[:jobid\...\]**
    :   This job can begin execution after the specified jobs have terminated and any associated burst buffer stage out operations have completed.

    :   

    **aftercorr:job_id\[:jobid\...\]**
    :   A task of this job array can begin execution after the corresponding task ID in the specified job has completed successfully (ran to completion with an exit code of zero). If the specified job is not an array, this is treated the same as afterok.

    :   

    **afternotok:job_id\[:jobid\...\]**
    :   This job can begin execution after the specified jobs have terminated in some failed state (non-zero exit code, node failure, timed out, etc). This job must be submitted while the specified job is still active or within **MinJobAge** seconds after the specified job has ended. If the dependent job id is not found and is on the same cluster as the job submission, the job is rejected. If the dependent job id is not found and is on a different cluster from the job submission, the dependency is marked as failed.

    :   

    **afterok:job_id\[:jobid\...\]**
    :   This job can begin execution after the specified jobs have successfully executed (ran to completion with an exit code of zero). This job must be submitted while the specified job is still active or within **MinJobAge** seconds after the specified job has ended. If the dependent job id is not found and is on the same cluster as the job submission, the job is rejected. If the dependent job id is not found and is on a different cluster from the job submission, the dependency is marked as failed.

    :   

    **singleton**
    :   This job can begin execution after any previously launched jobs sharing the same job name and user have terminated. In other words, only one job by that name and owned by that user can be running or suspended at any point in time. In a federation, a singleton dependency must be fulfilled on all clusters unless DependencyParameters=disable_remote_singleton is used in slurm.conf.

**-X**, **\--disable-status**

Disable the display of task status when srun receives a single SIGINT (Ctrl-C). Instead immediately forward the SIGINT to the running job. Without this option a second Ctrl-C in one second is required to forcibly terminate the job and **srun** will immediately exit. May also be set via the environment variable SLURM_DISABLE_STATUS. This option applies to job allocations.

**-m**, **\--distribution**={\*\|block\|cyclic\|arbitrary\|plane=\<*size*\>}\[:{\*\|block\|cyclic\|fcyclic}\[:{\*\|block\|cyclic\|fcyclic}\]\]\[,{Pack\|NoPack}\]

Specify alternate distribution methods for remote processes. For job allocation, this sets environment variables that will be used by subsequent srun requests. Task distribution affects job allocation at the last stage of the evaluation of available resources by the cons_tres plugin. Consequently, other options (e.g. \--ntasks-per-node, \--cpus-per-task) may affect resource selection prior to task distribution. To ensure a specific task distribution, jobs should have access to entire nodes, which can be accomplished by using the **\--exclusive** flag or by requesting all the resources on the node(s).

This option controls the distribution of tasks to the nodes on which resources have been allocated, and the distribution of those resources to tasks for binding (task affinity). The first distribution method (before the first \":\") controls the distribution of tasks to nodes. The second distribution method (after the first \":\") controls the distribution of allocated CPUs across sockets for binding to tasks. The third distribution method (after the second \":\") controls the distribution of allocated CPUs across cores for binding to tasks. The second and third distributions apply only if task affinity is enabled. The third distribution is supported only if the task/cgroup plugin is configured. The default value for each distribution type is specified by \*.

Note that with select/cons_tres, the number of CPUs allocated to each socket and node may be different. Refer to the [mc_support](mc_support.md) document for more information on resource allocation, distribution of tasks to nodes, and binding of tasks to CPUs.

:   First distribution method (distribution of tasks across nodes):

    **\***

    :   

    :   Use the default method for distributing tasks to nodes (block).

    :   

    **block**

    :   

    :   The block distribution method will distribute tasks to a node such that consecutive tasks share a node. For example, consider an allocation of three nodes each with two cpus. A four-task block distribution request will distribute those tasks to the nodes with tasks one and two on the first node, task three on the second node, and task four on the third node. Block distribution is the default behavior if the number of tasks exceeds the number of allocated nodes.

    :   

    **cyclic**

    :   

    :   The cyclic distribution method will distribute tasks to a node such that consecutive tasks are distributed over consecutive nodes (in a round-robin fashion). For example, consider an allocation of three nodes each with two cpus. A four-task cyclic distribution request will distribute those tasks to the nodes with tasks one and four on the first node, task two on the second node, and task three on the third node. Note that when SelectType is select/cons_tres, the same number of CPUs may not be allocated on each node. Task distribution will be round-robin among all the nodes with CPUs yet to be assigned to tasks. Cyclic distribution is the default behavior if the number of tasks is no larger than the number of allocated nodes.

    :   

    **plane**

    :   

    :   The tasks are distributed in blocks of size \<*size*\>. The size must be given or SLURM_DIST_PLANESIZE must be set. The number of tasks distributed to each node is the same as for cyclic distribution, but the taskids assigned to each node depend on the plane size. Additional distribution specifications cannot be combined with this option. For more details (including examples and diagrams), please see the [mc_support](mc_support.md) document and [https://slurm.schedmd.com/dist_plane.html](dist_plane.md)

    :   

    **arbitrary**

    :   

    :   The arbitrary method of distribution will allocate processes in-order as listed in file designated by the environment variable SLURM_HOSTFILE. If this variable is listed it will override any other method specified. If not set the method will default to block. Inside the hostfile must contain at minimum the number of hosts requested and be one per line or comma separated. If specifying a task count (**-n**, **\--ntasks**=\<*number*\>), your tasks will be laid out on the nodes in the order of the file.\
        **NOTE**: The arbitrary distribution option on a job allocation only controls the nodes to be allocated to the job and not the allocation of CPUs on those nodes. This option is meant primarily to control a job step\'s task layout in an existing job allocation for the srun command.\
        **NOTE**: If the number of tasks is given and a list of requested nodes is also given, the number of nodes used from that list will be reduced to match that of the number of tasks if the number of nodes in the list is greater than the number of tasks.

    :   

    Second distribution method (distribution of CPUs across sockets for binding):

    **\***

    :   

    :   Use the default method for distributing CPUs across sockets (cyclic).

    :   

    **block**

    :   

    :   The block distribution method will distribute allocated CPUs consecutively from the same socket for binding to tasks, before using the next consecutive socket.

    :   

    **cyclic**

    :   

    :   The cyclic distribution method will distribute allocated CPUs for binding to a given task consecutively from the same socket, and from the next consecutive socket for the next task, in a round-robin fashion across sockets. Tasks requiring more than one CPU will have all of those CPUs allocated on a single socket if possible.\
        **NOTE**: In nodes with hyper-threading enabled, a task not requesting full cores may be distributed across sockets. This can be avoided by specifying **\--ntasks-per-core=1**, which forces tasks to allocate full cores.

    :   

    **fcyclic**

    :   

    :   The fcyclic distribution method will distribute allocated CPUs for binding to tasks from consecutive sockets in a round-robin fashion across the sockets. Tasks requiring more than one CPU will have each CPUs allocated in a cyclic fashion across sockets.

    :   

    Third distribution method (distribution of CPUs across cores for binding):

    **\***

    :   

    :   Use the default method for distributing CPUs across cores (inherited from second distribution method).

    :   

    **block**

    :   

    :   The block distribution method will distribute allocated CPUs consecutively from the same core for binding to tasks, before using the next consecutive core.

    :   

    **cyclic**

    :   

    :   The cyclic distribution method will distribute allocated CPUs for binding to a given task consecutively from the same core, and from the next consecutive core for the next task, in a round-robin fashion across cores.

    :   

    **fcyclic**

    :   

    :   The fcyclic distribution method will distribute allocated CPUs for binding to tasks from consecutive cores in a round-robin fashion across the cores.

    :   

    Optional control for task distribution over nodes:

    **Pack**

    :   

    :   Rather than evenly distributing a job step\'s tasks evenly across its allocated nodes, pack them as tightly as possible on the nodes. This only applies when the \"block\" task distribution method is used.

    :   

    **NoPack**

    :   

    :   Rather than packing a job step\'s tasks as tightly as possible on the nodes, distribute them evenly. This user option will supersede the SelectTypeParameters CR_Pack_Nodes configuration parameter.

    :   

    This option applies to job and step allocations.

    :   

**\--epilog**={none\|\<*executable*\>}

**srun** will run *executable* just after the job step completes. The command line arguments for *executable* will be the command and arguments of the job step. If *none* is specified, then no srun epilog will be run. This parameter overrides the SrunEpilog parameter in slurm.conf. This parameter is completely independent from the Epilog parameter in slurm.conf. This option applies to job allocations.

**-e**, **\--error**=\<*filename_pattern*\>

Specify how stderr is to be redirected. By default in interactive mode, **srun** redirects stderr to the same file as stdout, if one is specified. The **\--error** option is provided to allow stdout and stderr to be redirected to different locations. See **IO Redirection** below for more options. If the specified file already exists, it will be overwritten. This option applies to job and step allocations.

**\--exact**

Allow a step access to only the resources requested for the step. By default, all non-GRES resources on each node in the step allocation will be used. This option only applies to step allocations.\
**NOTE**: Parallel steps will either be blocked or rejected until requested step resources are available unless **\--overlap** is specified. Job resources can be held after the completion of an srun command while Slurm does job cleanup. Step epilogs and/or SPANK plugins can further delay the release of step resources.

**-x**, **\--exclude**={\<*host1*\[,\<*host2*\>\...\]\|\<*filename*\>}

Request that a specific list of hosts not be included in the resources allocated to this job. The host list will be assumed to be a filename if it contains a \"/\" character. This option applies to job and step allocations.

**\--exclusive**\[={user\|mcs\|topo}\]

This option applies to job and job step allocations, and has two slightly different meanings for each one.

When used to initiate a **job**, the job allocation can not share nodes (or topology segment with the \"=topo\") with other running jobs (or just other users with the \"=user\" option or \"=mcs\" option). If user/mcs/topo are not specified (i.e. the job allocation can not share nodes with other running jobs), the job allocation is allocated all CPUs and GRES on all nodes in the allocation, but is only allocated as much memory as it requested. This is by design to support gang scheduling, because suspended jobs still reside in memory. To request all the memory on a node, use **\--mem=0**. The default shared/exclusive behavior depends on system configuration and the partition\'s **OverSubscribe** option takes precedence over the job\'s option. **NOTE**: Since shared GRES (MPS) cannot be allocated at the same time as a sharing GRES (GPU) this option only allocates all sharing GRES and no underlying shared GRES.

This option can also be used when initiating more than one **job step** within an existing resource allocation (default), where you want separate processors to be dedicated to each job step. The job step is only allocated as much GRES as is requested. If sufficient processors are not available to initiate the job step, it will be deferred. This can be thought of as providing a mechanism for resource management to the job within its allocation (**\--exact** implied). The exclusive allocation of CPUs applies to job steps by default, but \--exact is **NOT** the default. In other words, the default behavior is this: job steps will not share CPUs, but job steps will be allocated all CPUs available to the job on all nodes allocated to the steps.

In order to share the resources use the **\--overlap** option.

**NOTE**: This option is mutually exclusive with **\--oversubscribe**.

See **EXAMPLE** below.

**\--export**={\[ALL,\]\<*environment_variables*\>\|ALL\|NONE}

Identify which environment variables from the submission environment are propagated to the launched application.

:   

    **\--export**=ALL
    :   Default mode if **\--export** is not specified. All of the user\'s environment will be loaded from the caller\'s environment.

    :   

    **\--export**=NONE
    :   None of the user environment will be defined. User must use absolute path to the binary to be executed that will define the environment. User can not specify explicit environment variables with \"NONE\".
        This option is particularly important for jobs that are submitted on one cluster and execute on a different cluster (e.g. with different paths). To avoid steps inheriting environment export settings (e.g. \"NONE\") from sbatch command, either set **\--export**=ALL or the environment variable SLURM_EXPORT_ENV should be set to \"ALL\".

    :   

    **\--export**=\[ALL,\]\<*environment_variables*\>
    :   Exports all SLURM\* environment variables along with explicitly defined variables. Multiple environment variable names should be comma separated. Environment variable names may be specified to propagate the current value (e.g. \"\--export=EDITOR\") or specific values may be exported (e.g. \"\--export=EDITOR=/bin/emacs\"). If \"ALL\" is specified, then all user environment variables will be loaded and will take precedence over any explicitly given environment variables.

    :   

        :   

            Example: **\--export**=EDITOR,ARG1=test
            :   In this example, the propagated environment will only contain the variable *EDITOR* from the user\'s environment, *SLURM\_\** environment variables, and *ARG1*=test.

            :   

            Example: **\--export**=ALL,EDITOR=/bin/emacs
            :   There are two possible outcomes for this example. If the caller has the *EDITOR* environment variable defined, then the job\'s environment will inherit the variable from the caller\'s environment. If the caller doesn\'t have an environment variable defined for *EDITOR*, then the job\'s environment will use the value given by **\--export**.

**\--external-launcher**

Create a special step on one or more allocated nodes which won\'t consume any resources, but will have access to all of the job\'s allocated resources on the nodes.

Options like \--ntasks-per-\*, \--mem\*, \--cpus\*, \--tres\*, \--gres\*, will be ignored.

This is meant for use MPI implementations that require their own launcher. This launches a step with access to all the resources and which will later spawn any number of user processes with access to all these resources.

The resource usage within this special step will still be accounted for if the accounting plugins are enabled. This special step can be overlapped with any other step.

**NOTE**: This option is not intended to be used directly.

**\--extra**=\<*string*\>

An arbitrary string enclosed in single or double quotes if using spaces or some special characters.

If **SchedulerParameters=extra_constraints** is enabled, this string is used for node filtering based on the *Extra* field in each node.

**-B**, **\--extra-node-info**=\<*sockets*\>\[:*cores*\[:*threads*\]\]

Restrict node selection to nodes with at least the specified number of sockets, cores per socket and/or threads per core.\
**NOTE**: These options do not specify the resource allocation size. Each value specified is considered a minimum. An asterisk (\*) can be used as a placeholder indicating that all available resources of that type are to be utilized. Values can also be specified as min-max. The individual levels can also be specified in separate options if desired:

        --sockets-per-node=<sockets>
        --cores-per-socket=<cores>
        --threads-per-core=<threads>

If task/affinity plugin is enabled, then specifying an allocation in this manner also sets a default **\--cpu-bind** option of *threads* if the **-B** option specifies a thread count, otherwise an option of *cores* if a core count is specified, otherwise an option of *sockets*. If SelectType is configured to select/cons_tres, it must have a parameter of CR_Core, CR_Core_Memory, CR_Socket, or CR_Socket_Memory for this option to be honored. If not specified, the scontrol show job will display \'ReqS:C:T=\*:\*:\*\'. This option applies to job allocations.\
**NOTE**: This option is mutually exclusive with **\--hint**, **\--threads-per-core** and **\--ntasks-per-core**.\
**NOTE**: If the number of sockets, cores and threads were all specified, the number of nodes was specified (as a fixed number, not a range) and the number of tasks was NOT specified, srun will implicitly calculate the number of tasks as one task per thread.

**\--gpu-bind**=\[verbose,\]\<*type*\>

Equivalent to \--tres-bind=gres/gpu:\[verbose,\]\<*type*\> See **\--tres-bind** for all options and documentation.

**\--gpu-freq**=\[\<*type*\]=*value*\>\[,\<*type*=*value*\>\]\[,verbose\]

Request that GPUs allocated to the job are configured with specific frequency values. This option can be used to independently configure the GPU and its memory frequencies. After the job is completed, the frequencies of all affected GPUs will be reset to the highest possible values. In some cases, system power caps may override the requested values. The field *type* can be \"memory\". If *type* is not specified, the GPU frequency is implied. The *value* field can either be \"low\", \"medium\", \"high\", \"highm1\" or a numeric value in megahertz (MHz). If the specified numeric value is not possible, a value as close as possible will be used. See below for definition of the values. The *verbose* option causes current GPU frequency information to be logged. Examples of use include \"\--gpu-freq=medium,memory=high\" and \"\--gpu-freq=450\".

Supported *value* definitions:

:   

    **low**
    :   the lowest available frequency.

    :   

    **medium**
    :   attempts to set a frequency in the middle of the available range.

    :   

    **high**
    :   the highest available frequency.

    :   

    **highm1**
    :   (high minus one) will select the next highest available frequency.

**-G**, **\--gpus**=\[*type*:\]\<*number*\>

Specify the total number of GPUs required for the job. An optional GPU type specification can be supplied. See also the **\--gpus-per-node**, **\--gpus-per-socket** and **\--gpus-per-task** options.\
**NOTE**: The allocation has to contain at least one GPU per node, or one of each GPU type per node if types are used. Use heterogeneous jobs if different nodes need different GPU types.

**\--gpus-per-node**=\[*type*:\]\<*number*\>

Specify the number of GPUs required for the job on each node included in the job\'s resource allocation. An optional GPU type specification can be supplied. For example \"\--gpus-per-node=volta:3\". Multiple options can be requested in a comma separated list, for example: \"\--gpus-per-node=volta:3,kepler:1\". See also the **\--gpus**, **\--gpus-per-socket** and **\--gpus-per-task** options.

**\--gpus-per-socket**=\[*type*:\]\<*number*\>

Specify the number of GPUs required for the job on each socket included in the job\'s resource allocation. An optional GPU type specification can be supplied. For example \"\--gpus-per-socket=volta:3\". Multiple options can be requested in a comma separated list, for example: \"\--gpus-per-socket=volta:3,kepler:1\". Requires job to specify a sockets per node count ( \--sockets-per-node). See also the **\--gpus**, **\--gpus-per-node** and **\--gpus-per-task** options. This option applies to job allocations.

**\--gpus-per-task**=\[*type*:\]\<*number*\>

Specify the number of GPUs required for the job on each task to be spawned in the job\'s resource allocation. An optional GPU type specification can be supplied. For example \"\--gpus-per-task=volta:1\". Multiple options can be requested in a comma separated list, for example: \"\--gpus-per-task=volta:3,kepler:1\". See also the **\--gpus**, **\--gpus-per-socket** and **\--gpus-per-node** options. This option requires an explicit task count, e.g. -n, \--ntasks or \"\--gpus=X \--gpus-per-task=Y\" rather than an ambiguous range of nodes with -N, \--nodes. This option will implicitly set \--tres-bind=gres/gpu:per_task:\<gpus_per_task\>, or if multiple gpu types are specified \--tres-bind=gres/gpu:per_task:\<gpus_per_task_type_sum\>. However, that can be overridden with an explicit \--tres-bind=gres/gpu specification.

**\--gres**=\<*list*\>

Specifies a comma-delimited list of generic consumable resources requested per node. The format for each entry in the list is \"name\[\[:type\]:count\]\". The *name* is the type of consumable resource (e.g. gpu). The *type* is an optional classification for the resource (e.g. a100). The *count* is the number of those resources with a default value of 1. The count can have a suffix of \"k\" or \"K\" (multiple of 1024), \"m\" or \"M\" (multiple of 1024 x 1024), \"g\" or \"G\" (multiple of 1024 x 1024 x 1024), \"t\" or \"T\" (multiple of 1024 x 1024 x 1024 x 1024), \"p\" or \"P\" (multiple of 1024 x 1024 x 1024 x 1024 x 1024). The specified resources will be allocated to the job on each node. The available generic consumable resources is configurable by the system administrator. A list of available generic consumable resources will be printed and the command will exit if the option argument is \"help\". Examples of use include \"\--gres=gpu:2\", \"\--gres=gpu:kepler:2\", and \"\--gres=help\". **NOTE**: This option applies to job and step allocations. By default, a job step is allocated all of the generic resources that have been requested by the job, except those implicitly requested when a job is exclusive. To change the behavior so that each job step is allocated no generic resources, explicitly set the value of \--gres to specify zero counts for each generic resource OR set \"\--gres=none\" OR set the SLURM_STEP_GRES environment variable to \"none\".

**\--gres-flags**=\<*type*\>

Specify generic resource task binding options.

:   

    **allow-task-sharing**

    :   

    :   Allow tasks access to each GPU within the job\'s allocation that is on the same node as the task. This is useful when using \--gpu-bind or \--tres-bind=gres/gpu to bind GPUs to specific tasks, but GPU communication between tasks is also desired.\
        **NOTE**: This option is specific to srun.

    :   

    **multiple-tasks-per-sharing**

    :   

    :   Negate **one-task-per-sharing**. This is useful if it is set by default in **SelectTypeParameters**.

    :   

    **disable-binding**

    :   

    :   Negate **enforce-binding**. This is useful if it is set by default in **SelectTypeParameters**.

    :   

    **enforce-binding**

    :   

    :   The only CPUs available to the job will be those bound to the selected GRES (i.e. the CPUs identified in the gres.conf file will be strictly enforced). This option may result in delayed initiation of a job. For example a job requiring two GPUs and one CPU will be delayed until both GPUs on a single socket are available rather than using GPUs bound to separate sockets, however, the application performance may be improved due to improved communication speed. Requires the node to be configured with more than one socket and resource filtering will be performed on a per-socket basis.\
        **NOTE**: This option can be set by default in **SelectTypeParameters**.\
        **NOTE**: This option is specific to **SelectType=cons_tres** for job allocations.\
        **NOTE**: This option can give undefined results if attempting to enforce binding on multiple gres on multiple sockets.

    :   

    **one-task-per-sharing**

    :   

    :   Do not allow different tasks in to be allocated shared gres from the same sharing gres.\
        **NOTE**: This flag is only enforced if shared gres are requested with \--tres-per-task.\
        **NOTE**: This option can be set by default with **SelectTypeParameters=ONE_TASK_PER_SHARING_GRES**.\
        **NOTE**: This option is specific to **SelectTypeParameters=MULTIPLE_SHARING_GRES_PJ**

**-h**, **\--help**

Display help information and exit.

**\--het-group**=\<*expr*\>

Identify each component in a heterogeneous job allocation for which a step is to be created. Applies only to srun commands issued inside a salloc allocation or sbatch script. \<*expr*\> is a set of integers corresponding to one or more options offsets on the salloc or sbatch command line. Examples: \"\--het-group=2\", \"\--het-group=0,4\", \"\--het-group=1,3-5\". The default value is \--het-group=0.

**\--hint**=\<*type*\>

Bind tasks according to application hints.\
**NOTE**: This option implies specific values for certain related options, which prevents its use with any user-specified values for **\--ntasks-per-core**, **\--cores-per-socket**, **\--sockets-per-node**, **\--threads-per-core**, **\--cpu-bind** (other than **\--cpu-bind=verbose**) or **-B**. These conflicting options will override **\--hint** when specified as command line arguments. If a conflicting option is specified as an environment variable, \--hint as a command line argument will take precedence.

:   

    **compute_bound**

    :   

    :   Select settings for compute bound applications: use all cores in each socket, one thread per core.

    :   

    **memory_bound**

    :   

    :   Select settings for memory bound applications: use only one core in each socket, one thread per core.

    :   

    **multithread**

    :   

    :   Use extra threads with in-core multi-threading which can benefit communication intensive applications. Only supported with the task/affinity plugin.

    :   

    **nomultithread**

    :   

    :   Don\'t use extra threads with in-core multi-threading; restricts tasks to one thread per core. Only supported with the task/affinity plugin.

    :   

    **help**

    :   

    :   show this help message

    :   

    This option applies to job allocations.

    :   

**-H, \--hold**

Specify the job is to be submitted in a held state (priority of zero). A held job can now be released using scontrol to reset its priority (e.g. \"*scontrol release \<job_id\>*\"). This option applies to job allocations.

**-I**, **\--immediate**\[=\<*seconds*\>\]

exit if resources are not available within the time period specified. If no argument is given (seconds defaults to 1), resources must be available immediately for the request to succeed. If **defer** is configured in **SchedulerParameters** and seconds=1 the allocation request will fail immediately; **defer** conflicts and takes precedence over this option. By default, **\--immediate** is off, and the command will block until resources become available. Since this option\'s argument is optional, for proper parsing the single letter option must be followed immediately with the value and not include a space between them. For example \"-I60\" and not \"-I 60\". This option applies to job and step allocations.

**-i**, **\--input**=\<*mode*\>

Specify how stdin is to be redirected. By default, **srun** redirects stdin from the terminal to all tasks. See **IO Redirection** below for more options. For OS X, the poll() function does not support stdin, so input from a terminal is not possible. This option applies to job and step allocations.

**-J**, **\--job-name**=\<*jobname*\>

Specify a name for the job. The specified name will appear along with the job id number when querying running jobs on the system. The default is the supplied **executable** program\'s name. **NOTE**: This information may be written to the slurm_jobacct.log file. This file is space delimited so if a space is used in the *jobname* name it will cause problems in properly displaying the contents of the slurm_jobacct.log file when the **sacct** command is used. This option applies to job and step allocations.

**\--jobid**=\<*jobid*\>

Initiate a job step under an already allocated job with job id *id*. Using this option will cause **srun** to behave exactly as if the SLURM_JOB_ID environment variable was set. This option applies to step allocations.

**-K**, **\--kill-on-bad-exit**\[=0\|1\]

Controls whether or not to terminate a step if any task exits with a non-zero exit code. If this option is not specified, the default action will be based upon the Slurm configuration parameter of **KillOnBadExit**. If this option is specified, it will take precedence over **KillOnBadExit**. An option argument of zero will not terminate the job. A non-zero argument or no argument will terminate the job. Note: This option takes precedence over the **-W**, **\--wait** option to terminate the job immediately if a task exits with a non-zero exit code. Since this option\'s argument is optional, for proper parsing the single letter option must be followed immediately with the value and not include a space between them. For example \"-K1\" and not \"-K 1\".

**-l**, **\--label**

Prepend task number to lines of stdout/err. The **\--label** option will prepend lines of output with the remote task id. This option applies to step allocations.

**-L**, **\--licenses**=\<*license*\>\[@*db*\]\[:*count*\]\[,*license*\[@*db*\]\[:*count*\]\...\]

Specification of licenses (or other resources available on all nodes of the cluster) which must be allocated to this job. License names can be followed by a colon and count (the default count is one). Multiple licenses can be requested. If they are separated by a comma (\',\' meaning AND), then all requested licenses are required for the job. For example, \"\--licenses=foo:4,bar\". If they are separated by a pipe (\'\|\' meaning OR), then only one of the license requests are required for the job. For example, \"\--licenses=foo:4\|bar\". AND and OR cannot both be used.

**NOTE**: When submitting heterogeneous jobs, license requests may only be made on the first component job. For example \"srun -L ansys:2 : myexecutable\".

**NOTE**: If licenses are tracked in AccountingStorageTres and OR is used, ReqTRES will display all requested tres separated by commas. AllocTRES will display only the license that was allocated to the job.

**NOTE**: When a job requests OR\'d licenses, Slurm will attempt to allocate the licenses in the order in which they are requested. This specified order will take precedence even if the rest of requested licenses could be satisfied on a requested reservation. This also applies to backfill planning when **SchedulerParameters=bf_licenses** is configured.

**\--mail-type**=\<*type*\>

Notify user by email when certain event types occur. Valid *type* values are NONE, BEGIN, END, FAIL, REQUEUE, ALL (equivalent to BEGIN, END, FAIL, INVALID_DEPEND, REQUEUE, and STAGE_OUT), INVALID_DEPEND (dependency never satisfied), STAGE_OUT (burst buffer stage out and teardown completed), TIME_LIMIT, TIME_LIMIT_90 (reached 90 percent of time limit), TIME_LIMIT_80 (reached 80 percent of time limit), and TIME_LIMIT_50 (reached 50 percent of time limit). Multiple *type* values may be specified in a comma separated list. NONE will suppress all event notifications, ignoring any other values specified. By default no email notifications are sent. The user to be notified is indicated with **\--mail-user**. This option applies to job allocations.

**\--mail-user**=\<*user*\>

User to receive email notification of state changes as defined by **\--mail-type**. This may be a full email address or a username. If a username is specified, the value from **MailDomain** in slurm.conf will be appended to create an email address. The default value is the submitting user. This option applies to job allocations.

**\--mcs-label**=\<*mcs*\>

Used only when a compatible **MCSPlugin** is enabled. This parameter is a group that the user belongs to (**mcs/group**) or an arbitrary label string (**mcs/label**). In both cases, no label will be assigned by default. This option applies to job allocations. Refer to the MCS documentation for more details: \<[https://slurm.schedmd.com/mcs.html](mcs.md)\>

**\--mem**=\<*size*\>\[*units*\]

Specify the real memory required per node. Default units are megabytes. Different units can be specified using the suffix \[K\|M\|G\|T\]. Default value is **DefMemPerNode** and the maximum value is **MaxMemPerNode**. If configured, both of parameters can be seen using the **scontrol show config** command. This parameter would generally be used if whole nodes are allocated to jobs (**SelectType=select/linear**). Specifying a memory limit of zero for a job step will restrict the job step to the amount of memory allocated to the job, but not remove any of the job\'s memory allocation from being available to other job steps. Also see **\--mem-per-cpu** and **\--mem-per-gpu**. The **\--mem**, **\--mem-per-cpu** and **\--mem-per-gpu** options are mutually exclusive. If **\--mem**, **\--mem-per-cpu** or **\--mem-per-gpu** are specified as command line arguments, then they will take precedence over the environment (potentially inherited from **salloc** or **sbatch**).

**NOTE**: A memory size specification of zero is treated as a special case and grants the job access to all of the memory on each node for newly submitted jobs and all available job memory to new job steps.

**NOTE**: The memory used by each slurmstepd process is included in the job\'s total memory usage. It typically consumes between 20MiB and 200MiB, though this can vary depending on system configuration and any loaded plugins.

**NOTE**: Memory requests will not be strictly enforced unless Slurm is configured to use an enforcement mechanism. See **ConstrainRAMSpace** in the **[cgroup.conf](cgroup.conf.md)**(5) man page and **OverMemoryKill** in the **[slurm.conf](slurm.conf.md)**(5) man page for more details.

This option applies to job and step allocations.

**\--mem-bind**=\[{quiet\|verbose},\]\<*type*\>

Bind tasks to memory. Used only when the task/affinity plugin is enabled and the NUMA memory functions are available. **Note that the resolution of CPU and memory binding may differ on some architectures.** For example, CPU binding may be performed at the level of the cores within a processor while memory binding will be performed at the level of nodes, where the definition of \"nodes\" may differ from system to system. By default no memory binding is performed; any task using any CPU can use any memory. This option is typically used to ensure that each task is bound to the memory closest to its assigned CPU. **The use of any type other than \"none\" or \"local\" is not recommended.** If you want greater control, try running a simple test code with the options \"\--cpu-bind=verbose,none \--mem-bind=verbose,none\" to determine the specific configuration.

**NOTE**: To have Slurm always report on the selected memory binding for all commands executed in a shell, you can enable verbose mode by setting the SLURM_MEM_BIND environment variable value to \"verbose\".

The following informational environment variables are set when **\--mem-bind** is in use:

            SLURM_MEM_BIND_LIST
            SLURM_MEM_BIND_PREFER
            SLURM_MEM_BIND_TYPE
            SLURM_MEM_BIND_VERBOSE

See the **ENVIRONMENT VARIABLES** section for a more detailed description of the individual SLURM_MEM_BIND\* variables.

Supported options include:

:   

    **help**

    :   

    :   show this help message

    :   

    **local**

    :   

    :   Use memory local to the processor in use

    :   

    **map_mem:\<list\>**

    :   

    :   Bind by setting memory masks on tasks (or ranks) as specified where \<list\> is \<numa_id_for_task_0\>,\<numa_id_for_task_1\>,\... The mapping is specified for a node and identical mapping is applied to the tasks on every node (i.e. the lowest task ID on each node is mapped to the first ID specified in the list, etc.). NUMA IDs are interpreted as decimal values unless they are preceded with \'0x\' in which case they interpreted as hexadecimal values. If the number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list. To simplify support for large task counts, the lists may follow a map with an asterisk and repetition count. For example \"map_mem:0x0f\*4,0xf0\*4\". For predictable binding results, all CPUs for each node in the job should be allocated to the job.

    :   

    **mask_mem:\<list\>**

    :   

    :   Bind by setting memory masks on tasks (or ranks) as specified where \<list\> is \<numa_mask_for_task_0\>,\<numa_mask_for_task_1\>,\... The mapping is specified for a node and identical mapping is applied to the tasks on every node (i.e. the lowest task ID on each node is mapped to the first mask specified in the list, etc.). NUMA masks are **always** interpreted as hexadecimal values. Note that masks must be preceded with a \'0x\' if they don\'t begin with \[0-9\] so they are seen as numerical values. If the number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list. To simplify support for large task counts, the lists may follow a mask with an asterisk and repetition count. For example \"mask_mem:0\*4,1\*4\". For predictable binding results, all CPUs for each node in the job should be allocated to the job.

    :   

    **no\[ne\]**

    :   

    :   don\'t bind tasks to memory (default)

    :   

    **nosort**

    :   

    :   avoid sorting free cache pages (default, LaunchParameters configuration parameter can override this default)

    :   

    **p\[refer\]**

    :   

    :   Prefer use of first specified NUMA node, but permit\
         use of other available NUMA nodes.

    :   

    **q\[uiet\]**

    :   

    :   quietly bind before task runs (default)

    :   

    **rank**

    :   

    :   bind by task rank (not recommended)

    :   

    **v\[erbose\]**

    :   

    :   verbosely report binding before task runs

    :   

    This option applies to job and step allocations.

    :   

**\--mem-per-cpu**=\<*size*\>\[*units*\]

Minimum memory required per usable allocated CPU. Default units are megabytes. Different units can be specified using the suffix \[K\|M\|G\|T\]. The default value is **DefMemPerCPU** and the maximum value is **MaxMemPerCPU** (see exception below). If configured, both parameters can be seen using the **scontrol show config** command. Note that if the job\'s **\--mem-per-cpu** value exceeds the configured **MaxMemPerCPU**, then the user\'s limit will be treated as a memory limit per task; **\--mem-per-cpu** will be reduced to a value no larger than **MaxMemPerCPU**; **\--cpus-per-task** will be set and the value of **\--cpus-per-task** multiplied by the new **\--mem-per-cpu** value will equal the original **\--mem-per-cpu** value specified by the user. This parameter would generally be used if individual processors are allocated to jobs (**SelectType=select/cons_tres**). If resources are allocated by core, socket, or whole nodes, then the number of CPUs allocated to a job may be higher than the task count and the value of **\--mem-per-cpu** should be adjusted accordingly. Specifying a memory limit of zero for a job step will restrict the job step to the amount of memory allocated to the job, but not remove any of the job\'s memory allocation from being available to other job steps. Also see **\--mem** and **\--mem-per-gpu**. The **\--mem**, **\--mem-per-cpu** and **\--mem-per-gpu** options are mutually exclusive.

**NOTE**: If the final amount of memory requested by a job can\'t be satisfied by any of the nodes configured in the partition, the job will be rejected. This could happen if **\--mem-per-cpu** is used with the **\--exclusive** option for a job allocation and **\--mem-per-cpu** times the number of CPUs on a node is greater than the total memory of that node.

**NOTE**: This applies to **usable** allocated CPUs in a job allocation. This is important when more than one thread per core is configured. If a job requests \--threads-per-core with fewer threads on a core than exist on the core (or \--hint=nomultithread which implies \--threads-per-core=1), the job will be unable to use those extra threads on the core and those threads will not be included in the memory per CPU calculation. But if the job has access to all threads on the core, those threads will be included in the memory per CPU calculation even if the job did not explicitly request those threads.

In the following examples, each core has two threads.

In this first example, two tasks can run on separate hyperthreads in the same core because \--threads-per-core is not used. The third task uses both threads of the second core. The allocated memory per cpu includes all threads:

    $ salloc -n3 --mem-per-cpu=100
    salloc: Granted job allocation 17199
    $ sacct -j $SLURM_JOB_ID -X -o jobid%7,reqtres%35,alloctres%35
      JobID                             ReqTRES                           AllocTRES
    ------- ----------------------------------- -----------------------------------
      17199     billing=3,cpu=3,mem=300M,node=1     billing=4,cpu=4,mem=400M,node=1

In this second example, because of \--threads-per-core=1, each task is allocated an entire core but is only able to use one thread per core. Allocated CPUs includes all threads on each core. However, allocated memory per cpu includes only the usable thread in each core.

    $ salloc -n3 --mem-per-cpu=100 --threads-per-core=1
    salloc: Granted job allocation 17200
    $ sacct -j $SLURM_JOB_ID -X -o jobid%7,reqtres%35,alloctres%35
      JobID                             ReqTRES                           AllocTRES
    ------- ----------------------------------- -----------------------------------
      17200     billing=3,cpu=3,mem=300M,node=1     billing=6,cpu=6,mem=300M,node=1

**\--mem-per-gpu**=\<*size*\>\[*units*\]

Minimum memory required per allocated GPU. Default units are megabytes. Different units can be specified using the suffix \[K\|M\|G\|T\]. Default value is **DefMemPerGPU** and is available on both a global and per partition basis. If configured, the parameters can be seen using the **scontrol show config** and **scontrol show partition** commands. Also see **\--mem**. The **\--mem**, **\--mem-per-cpu** and **\--mem-per-gpu** options are mutually exclusive.

**\--mincpus**=\<*n*\>

Specify a minimum number of logical cpus/processors per node. This option applies to job allocations.

**\--mpi**=\<*mpi_type*\>

Identify the type of MPI to be used. May result in unique initiation procedures.

:   

    **cray_shasta**

    :   

    :   To enable Cray PMI support. This is for applications built with the Cray Programming Environment. The PMI Control Port can be specified with the **\--resv-ports** option or with the **MpiParams**=**ports**=\<*port range*\> parameter in your slurm.conf. This plugin does not have support for heterogeneous jobs. Support for cray_shasta is included by default.

    :   

    **list**

    :   

    :   Lists available mpi types to choose from.

    :   

    **pmi2**

    :   

    :   To enable PMI2 support. The PMI2 support in Slurm works only if the MPI implementation supports it, in other words if the MPI has the PMI2 interface implemented. The \--mpi=pmi2 will load the library lib/slurm/mpi_pmi2.so which provides the server side functionality but the client side must implement PMI2_Init() and the other interface calls.

    :   

    **pmix**

    :   

    :   To enable PMIx support (https://pmix.github.io). The PMIx support in Slurm can be used to launch parallel applications (e.g. MPI) if it supports PMIx, PMI2 or PMI1. Slurm must be configured with pmix support by passing \"\--with-pmix=\<PMIx installation path\>\" option to its \"./configure\" script.
        At the time of writing PMIx is supported in Open MPI starting from version 2.0. PMIx also supports backward compatibility with PMI1 and PMI2 and can be used if MPI was configured with PMI2/PMI1 support pointing to the PMIx library (\"libpmix\"). If MPI supports PMI1/PMI2 but doesn\'t provide the way to point to a specific implementation, a hack\'ish solution leveraging LD_PRELOAD can be used to force \"libpmix\" usage.

    :   

    **none**

    :   

    :   No special MPI processing. This is the default and works with many other versions of MPI.

    :   

    This option applies to step allocations.

    :   

**\--msg-timeout**=\<*seconds*\>

Modify the job launch message timeout. The default value is **MessageTimeout** in the Slurm configuration file slurm.conf. Changes to this are typically not recommended, but could be useful to diagnose problems. This option applies to job allocations.

**\--multi-prog**

Run a job with different programs and different arguments for each task. In this case, the executable program specified is actually a configuration file specifying the executable and arguments for each task. See **MULTIPLE PROGRAM CONFIGURATION** below for details on the configuration file contents. This option applies to step allocations.

**\--network**=\<*type*\>

Specify information pertaining to the switch or network. The interpretation of *type* is system dependent. It is used to request using Network Performance Counters. Only one value per request is valid. All options are case in-sensitive. In this configuration supported values include:

:   

    **system**
    :   Use the system-wide network performance counters. Only nodes requested will be marked in use for the job allocation. If the job does not fill up the entire system the rest of the nodes are not able to be used by other jobs using NPC, if idle their state will appear as PerfCnts. These nodes are still available for other jobs not using NPC.

    :   

    **blade**
    :   Use the blade network performance counters. Only nodes requested will be marked in use for the job allocation. If the job does not fill up the entire blade(s) allocated to the job those blade(s) are not able to be used by other jobs using NPC, if idle their state will appear as PerfCnts. These nodes are still available for other jobs not using NPC.

In all cases the job allocation request **must specify the \--exclusive option** and the step cannot specify the **\--overlap** option. Otherwise the request will be denied.

Also with any of these options steps are not allowed to share blades, so resources would remain idle inside an allocation if the step running on a blade does not take up all the nodes on the blade.

The **network** option is also available on systems with HPE Slingshot networks. It can be used to request a job VNI (to be used for communication between job steps in a job). It also can be used to override the default network resources allocated for the job step. Multiple values may be specified in a comma-separated list.

:   

    **tcs**=\<*class1*\>\[:\<*class2*\>\]\...
    :   Set of traffic classes to configure for applications. Supported traffic classes are DEDICATED_ACCESS, LOW_LATENCY, BULK_DATA, and BEST_EFFORT. The traffic classes may also be specified as TC_DEDICATED_ACCESS, TC_LOW_LATENCY, TC_BULK_DATA, and TC_BEST_EFFORT. This option applies to the job allocation, but not to step allocations.

    :   

    **no_vni**
    :   Don\'t allocate any VNIs for this job (even if multi-node).

    :   

    **job_vni**
    :   Allocate a job VNI for this job.

    :   

    **single_node_vni**
    :   Allocate a job VNI for this job, even if it is a single-node job.

    :   

    **adjust_limits**
    :   If set, slurmd will set an upper bound on network resource reservations by taking the per-NIC maximum resource quantity and subtracting the reserved or used values (whichever is higher) for any system network services; this is the default.

    :   

    **no_adjust_limits**
    :   If set, slurmd will calculate network resource reservations based only upon the per-resource configuration default and number of tasks in the application; it will not set an upper bound on those reservation requests based on resource usage of already-existing system network services. Setting this will mean more application launches could fail based on network resource exhaustion, but if the application absolutely needs a certain amount of resources to function, this option will ensure that.

    :   

    **disable_rdzv_get**
    :   Disable rendezvous gets in Slingshot NICs, which can improve performance for certain applications.

    :   

    **nic_distribution_count**=\<*val*\>
    :   The number of NICs the user will evenly distribute their tasks over. Defaults to the number of NICs on each node.

    :   

    **def\_\<rsrc\>**=\<*val*\>
    :   Per-CPU reserved allocation for this resource.

    :   

    **res\_\<rsrc\>**=\<*val*\>
    :   Per-node reserved allocation for this resource. If set, overrides the per-CPU allocation.

    :   

    **max\_\<rsrc\>**=\<*val*\>
    :   Maximum per-node limit for this resource.

    :   

    **depth**=\<*depth*\>
    :   Multiplier for per-CPU resource allocation. Default is the number of reserved CPUs on the node.

The resources that may be requested are:

:   

    **txqs**
    :   Transmit command queues. The default is 2 per-CPU, maximum 1024 per-node.

    :   

    **tgqs**
    :   Target command queues. The default is 1 per-CPU, maximum 512 per-node.

    :   

    **eqs**
    :   Event queues. The default is 2 per-CPU, maximum 2047 per-node.

    :   

    **cts**
    :   Counters. The default is 1 per-CPU, maximum 2047 per-node.

    :   

    **tles**
    :   Trigger list entries. The default is 1 per-CPU, maximum 2048 per-node.

    :   

    **ptes**
    :   Portable table entries. The default is 6 per-CPU, maximum 2048 per-node.

    :   

    **les**
    :   List entries. The default is 16 per-CPU, maximum 16384 per-node.

    :   

    **acs**
    :   Addressing contexts. The default is 2 per-CPU, maximum 1022 per-node.

On systems configured with **SwitchType=switch/nvidia_imex**, the following options are supported:

:   

    **unique-channel-per-segment**
    :   Instead of one channel for the entire job, allocate one channel per segment in the job. This only takes effect when **topology/block** is configured.

This option applies to job and step allocations.

**\--nice**\[=*adjustment*\]

Run the job with an adjusted scheduling priority within Slurm. With no adjustment value the scheduling priority is decreased by 100. A negative nice value increases the priority, otherwise decreases it. The adjustment range is +/- 2147483645. Only privileged users can specify a negative adjustment.

**-Z**, **\--no-allocate**

Run the specified tasks on a set of nodes without creating a Slurm \"job\" in the Slurm queue structure, bypassing the normal resource allocation step. The list of nodes must be specified with the **-w**, **\--nodelist** option. This is a privileged option only available for the users \"SlurmUser\" and \"root\". This option applies to job allocations. If user namespaces are active, then the mapping of users in the namespace must match the same namespace as MUNGE. If not, then the job will be rejected by slurmd.

**-k**, **\--no-kill**\[=off\]

Do not automatically terminate a job if one of the nodes it has been allocated fails. This option applies to job and step allocations. The job will assume all responsibilities for fault-tolerance. Tasks launched using this option will not be considered terminated (e.g. **-K**, **\--kill-on-bad-exit** and **-W**, **\--wait** options will have no effect upon the job step). The active job step (MPI job) will likely suffer a fatal error, but subsequent job steps may be run if this option is specified.

Specify an optional argument of \"off\" disable the effect of the **SLURM_NO_KILL** environment variable.

The default action is to terminate the job upon node failure.

**-F**, **\--nodefile**=\<*node_file*\>

Much like **\--nodelist**, but the list is contained in a file of name *node file*. The node names of the list may also span multiple lines in the file. Duplicate node names in the file will be ignored. The order of the node names in the list is not important; the node names will be sorted by Slurm.

**-w**, **\--nodelist**={\<*node_name_list*\>\|\<*filename*\>}

Request a specific list of hosts. The job will contain *all* of these hosts and possibly additional hosts as needed to satisfy resource requirements. The list may be specified as a comma-separated list of hosts, a range of hosts (host\[1-5,7,\...\] for example), or a filename. The host list will be assumed to be a filename if it contains a \"/\" character. If you specify a minimum node or processor count larger than can be satisfied by the supplied host list, additional resources will be allocated on other nodes as needed. Rather than repeating a host name multiple times, an asterisk and a repetition count may be appended to a host name. For example \"host1,host1\" and \"host1\*2\" are equivalent. If the number of tasks is given and a list of requested nodes is also given, the number of nodes used from that list will be reduced to match that of the number of tasks if the number of nodes in the list is greater than the number of tasks. This option applies to job and step allocations.

**-N**, **\--nodes**=\<*minnodes*\>\[-*maxnodes*\]\|\<*size_string*\>

Request that a minimum of *minnodes* nodes be allocated to this job. A maximum node count may also be specified with *maxnodes*. If only one number is specified, this is used as both the minimum and maximum node count. Node count can be also specified as size_string. The size_string specification identifies what nodes values should be used. Multiple values may be specified using a comma separated list or with a step function by suffix containing a colon and number values with a \"-\" separator. For example, \"\--nodes=1-15:4\" is equivalent to \"\--nodes=1,5,9,13\". The partition\'s node limits supersede those of the job. If a job\'s node limits are outside of the range permitted for its associated partition, the job will be left in a PENDING state. This permits possible execution at a later time, when the partition limit is changed. If a job node limit exceeds the number of nodes configured in the partition, the job will be rejected. Note that the environment variable **SLURM_JOB_NUM_NODES** (and **SLURM_NNODES** for backwards compatibility) will be set to the count of nodes actually allocated to the job. See the **ENVIRONMENT VARIABLES** section for more information. If **-N** is not specified, the default behavior is to allocate enough nodes to satisfy the requested resources as expressed by per-job specification options, e.g. **-n**, **-c** and **\--gpus**. The job will be allocated as many nodes as possible within the range specified and without delaying the initiation of the job. If the number of tasks is given and a number of requested nodes is also given, the number of nodes used from that request will be reduced to match that of the number of tasks if the number of nodes in the request is greater than the number of tasks. The node count specification may include a numeric value followed by a suffix of \"k\" (multiplies numeric value by 1,024) or \"m\" (multiplies numeric value by 1,048,576). This option applies to job and step allocations.

**NOTE**: This option cannot be used in with arbitrary distribution.

**-n**, **\--ntasks**=\<*number*\>

Specify the number of tasks to run. Request that **srun** allocate resources for *ntasks* tasks. The default is one task per node, but note that the **\--cpus-per-task** option will change this default. This option applies to job and step allocations.

**\--ntasks-per-core**=\<*ntasks*\>

Request the maximum *ntasks* be invoked on each core. This option applies to job and step allocations. Meant to be used with the **\--ntasks** option. Related to **\--ntasks-per-node** except at the core level instead of the node level. If set to 1, it will imply **\--cpu-bind=cores**. Otherwise, if set to a value greater than 1, it will imply **\--cpu-bind=threads**. Automatic binding behavior can be avoided by also specifying **\--cpu-bind=none**. Slurm may allocate more cpus than what was requested in order to respect this option.\
**NOTE**: This option is not supported when using *SelectType=select/linear*. This value can not be greater than **\--threads-per-core**.

**\--ntasks-per-gpu**=\<*ntasks*\>

Request that there are *ntasks* tasks invoked for every GPU. This option can work in two ways: 1) either specify **\--ntasks** in addition, in which case a type-less GPU specification will be automatically determined to satisfy **\--ntasks-per-gpu**, or 2) specify the GPUs wanted (e.g. via **\--gpus** or **\--gres**) without specifying **\--ntasks**, and the total task count will be automatically determined. The number of CPUs needed will be automatically increased if necessary to allow for any calculated task count. This option will implicitly set **\--tres-bind=gres/gpu:single:\<ntasks\>**, but that can be overridden with an explicit **\--tres-bind=gres/gpu** specification. This option is not compatible with a node range (i.e. -N\<*minnodes*-*maxnodes*\>). This option is not compatible with **\--gpus-per-task**, **\--gpus-per-socket**, or **\--ntasks-per-node**. This option is not supported unless *SelectType=cons_tres* is configured (either directly or indirectly on Cray systems).

**\--ntasks-per-node**=\<*ntasks*\>

Request that *ntasks* be invoked on each node. If used with the **\--ntasks** option, the **\--ntasks** option will take precedence and the **\--ntasks-per-node** will be treated as a *maximum* count of tasks per node. Meant to be used with the **\--nodes** option. This is related to **\--cpus-per-task**=*ncpus*, but does not require knowledge of the actual number of cpus on each node. In some cases, it is more convenient to be able to request that no more than a specific number of tasks be invoked on each node. Examples of this include submitting a hybrid MPI/OpenMP app where only one MPI \"task/rank\" should be assigned to each node while allowing the OpenMP portion to utilize all of the parallelism present in the node, or submitting a single setup/cleanup/monitoring job to each node of a pre-existing allocation as one step in a larger job script. This option applies to job allocations.

**\--ntasks-per-socket**=\<*ntasks*\>

Request the maximum *ntasks* be invoked on each socket. This option applies to the job allocation, but not to step allocations. Meant to be used with the **\--ntasks** option. Related to **\--ntasks-per-node** except at the socket level instead of the node level. Masks will automatically be generated to bind the tasks to specific sockets unless **\--cpu-bind=none** is specified. **NOTE**: This option is not supported when using *SelectType=select/linear*.

**\--oom-kill-step**\[={0\|1}\]

Whether to kill the entire step if an OOM event is detected in any task of the step. This overwrites the \"OOMKillStep\" setting in TaskPluginParam from slurm.conf and the allocation settings. When unset it will use the setting in slurm.conf. When set, a value of \"0\" will disable killing the entire step, while a value of \"1\" will enable it. Default is \"1\" (enabled) when the option is found with no value.

**\--open-mode**={append\|truncate}

Open the output and error files using append or truncate mode as specified. For heterogeneous job steps the default value is \"append\". Otherwise the default value is specified by the system configuration parameter *JobFileAppend*. This option applies to job and step allocations.

See **EXAMPLE** below.

**-o**, **\--output**=\<*filename_pattern*\>

Specify the \"*filename pattern*\" for stdout redirection. By default in interactive mode, **srun** collects stdout from all tasks and sends this output via TCP/IP to the attached terminal. With **\--output** stdout may be redirected to a file, to one file per task, or to /dev/null. See section **IO Redirection** below for the various forms of *filename pattern*. If the specified file already exists, it will be overwritten.\

If **\--error** is not also specified on the command line, both stdout and stderr will directed to the file specified by **\--output**. This option applies to job and step allocations.

**-O**, **\--overcommit**

Overcommit resources. This option applies to job and step allocations.

When applied to a job allocation (not including jobs requesting exclusive access to the nodes) the resources are allocated as if only one task per node is requested. This means that the requested number of cpus per task (**-c**, **\--cpus-per-task**) are allocated per node rather than being multiplied by the number of tasks. Options used to specify the number of tasks per node, socket, core, etc. are ignored.

When applied to job step allocations (the **srun** command when executed within an existing job allocation), this option can be used to launch more than one task per CPU. Normally, **srun** will not allocate more than one process per CPU. By specifying **\--overcommit** you are explicitly allowing more than one process per CPU. However no more than **MAX_TASKS_PER_NODE** tasks are permitted to execute per node. **NOTE**: **MAX_TASKS_PER_NODE** is defined in the file *slurm.h* and is not a variable, it is set at Slurm build time.

**\--overlap**

Specifying \--overlap allows steps to share all resources (CPUs, memory, and GRES) with all other steps. A step using this option will overlap all other steps, even those that did not specify \--overlap.

By default steps do not share resources with other parallel steps. This option applies to step allocations.

**-s**, **\--oversubscribe**

The job allocation can over-subscribe resources with other running jobs. The resources to be over-subscribed can be nodes, sockets, cores, and/or hyperthreads depending upon configuration. The default over-subscribe behavior depends on system configuration and the partition\'s **OverSubscribe** option takes precedence over the job\'s option. This option may result in the allocation being granted sooner than if the \--oversubscribe option was not set and allow higher system utilization, but application performance will likely suffer due to competition for resources. This option applies to job allocations.

**NOTE**: This option is mutually exclusive with **\--exclusive**.

**-p**, **\--partition**=\<*partition_names*\>

Request a specific partition for the resource allocation. If not specified, the default behavior is to allow the slurm controller to select the default partition as designated by the system administrator. If the job can use more than one partition, specify their names in a comma separate list and the one offering earliest initiation will be used with no regard given to the partition name ordering (although higher priority partitions will be considered first). When the job is initiated, the name of the partition used will be placed first in the job record partition string. This option applies to job allocations.

**\--prefer**=\<*list*\>

Nodes can have **features** assigned to them by the Slurm administrator. Users can specify which of these **features** are desired but not required by their job using the prefer option. This option operates independently from **\--constraint** and will override whatever is set there if possible. When scheduling, the features in **\--prefer** are tried first. If a node set isn\'t available with those features then **\--constraint** is attempted. See **\--constraint** for more information, this option behaves the same way.

**-E**, **\--preserve-env**

Pass the current values of environment variables SLURM_JOB_NUM_NODES and SLURM_NTASKS through to the *executable*, rather than computing them from command line parameters. This option applies to job allocations.

**\--priority**=\<*value*\>

Request a specific job priority. May be subject to configuration specific constraints. *value* should either be a numeric value or \"TOP\" (for highest possible value). Only Slurm operators and administrators can set the priority of a job. This option applies to job allocations only.

**\--profile**={all\|none\|\<*type*\>\[,\<*type*\>\...\]}

Enables detailed data collection by the acct_gather_profile plugin. Detailed data are typically time-series that are stored in an HDF5 file for the job or an InfluxDB database depending on the configured plugin. This option applies to job and step allocations.

:   

    **All**
    :   All data types are collected. (Cannot be combined with other values.)

    :   

    **None**
    :   No data types are collected. This is the default.\
         (Cannot be combined with other values.)

    :   

Valid *type* values are:

:   

    **Energy**
    :   Energy data is collected.

    :   

    **Task**
    :   Task (I/O, Memory, \...) data is collected.

    :   

    **Filesystem**
    :   Filesystem data is collected.

    :   

    **Network**
    :   Network (InfiniBand) data is collected.

**\--prolog**=\<*executable*\>

**srun** will run *executable* just before launching the job step. The command line arguments for *executable* will be the command and arguments of the job step. If *executable* is \"none\", then no srun prolog will be run. This parameter overrides the SrunProlog parameter in slurm.conf. This parameter is completely independent from the Prolog parameter in slurm.conf. This option applies to job allocations.

**\--propagate**\[=*rlimit*\[,*rlimit*\...\]\]

Allows users to specify which of the modifiable (soft) resource limits to propagate to the compute nodes and apply to their jobs. If no *rlimit* is specified, then all resource limits will be propagated. The following rlimit names are supported by Slurm (although some options may not be supported on some systems):

:   

    **ALL**
    :   All limits listed below (default)

    :   

    **NONE**
    :   No limits listed below

    :   

    **AS**
    :   The maximum address space (virtual memory) for a process.

    :   

    **CORE**
    :   The maximum size of core file

    :   

    **CPU**
    :   The maximum amount of CPU time

    :   

    **DATA**
    :   The maximum size of a process\'s data segment

    :   

    **FSIZE**
    :   The maximum size of files created. Note that if the user sets FSIZE to less than the current size of the slurmd.log, job launches will fail with a \'File size limit exceeded\' error.

    :   

    **MEMLOCK**
    :   The maximum size that may be locked into memory

    :   

    **NOFILE**
    :   The maximum number of open files

    :   

    **NPROC**
    :   The maximum number of processes available

    :   

    **RSS**
    :   The maximum resident set size. Note that this only has effect with Linux kernels 2.4.30 or older or BSD.

    :   

    **STACK**
    :   The maximum stack size

    :   

    This option applies to job allocations.

    :   

**\--pty**, **\--pty**=\<*File Descriptor*\>

Execute task zero with pseudo terminal mode or using pseudo terminal specified by \<*File Descriptor*\>. Implicitly sets **\--unbuffered**. Implicitly sets **\--error** and **\--output** to /dev/null for all tasks except task zero, which may cause those tasks to exit immediately (e.g. shells will typically exit immediately in that situation). This option applies to step allocations.

**-q**, **\--qos**=\<*qos*\>

Request a quality of service for the job, or comma separated list of QOS. If requesting a list it will be ordered based on the priority of the QOS given with the first being the highest priority. QOS values can be defined for each user/cluster/account association in the Slurm database. Users will be limited to their association\'s defined set of qos\'s when the Slurm configuration parameter, AccountingStorageEnforce, includes \"qos\" in its definition. This option applies to job allocations.

**-Q**, **\--quiet**

Suppress informational messages from srun. Errors will still be displayed. This option applies to job and step allocations.

**\--quit-on-interrupt**

Quit immediately on single SIGINT (Ctrl-C). Use of this option disables the status feature normally available when **srun** receives a single Ctrl-C and causes **srun** to instead immediately terminate the running job. This option applies to step allocations.

**\--reboot**

Force the allocated nodes to reboot before starting the job. This is only supported with some system configurations and will otherwise be silently ignored. Only root, *SlurmUser* or admins can reboot nodes. This option applies to job allocations.

**-r**, **\--relative**=\<*n*\>

Run a job step relative to node *n* of the current allocation. This option may be used to spread several job steps out among the nodes of the current job. If **-r** is used, the current job step will begin at node *n* of the allocated nodelist, where the first node is considered node 0. The **-r** option is not permitted with **-w** or **-x** option and will result in a fatal error when not running within a prior allocation (i.e. when SLURM_JOB_ID is not set). The default for *n* is 0. If the value of **\--nodes** exceeds the number of nodes identified with the **\--relative** option, a warning message will be printed and the **\--relative** option will take precedence. This option applies to step allocations.

**\--reservation**=\<*reservation_names*\>

Allocate resources for the job from the named reservation. If the job can use more than one reservation, specify their names in a comma separate list and the one offering earliest initiation. Each reservation will be considered in the order it was requested. All reservations will be listed in scontrol/squeue through the life of the job. In accounting the first reservation will be seen and after the job starts the reservation used will replace it.

**\--resources**=\<*resource_names*\>

Specification of hierarchical resources which must be allocated to this job. Resources names can be followed by a colon and count (the default count is one). Multiple resources in Mode 1 and Mode 2 can be requested in a comma separated list but only one of Mode 3 can be requested. For example, \"\--resources=flat:2,natural:1\".

See *[https://slurm.schedmd.com/hres.html](hres.md)* for more information on use of Hierarchical Resource with Slurm.

**\--resv-ports**\[=*count*\]

Reserve communication ports for this job. Users can specify the number of port they want to reserve. The parameter MpiParams=ports=12000-12999 must be specified in *slurm.conf*. If the number of reserved ports is zero then no ports are reserved. Used for native Cray\'s PMI only. This option applies to job and step allocations.

**\--segment**=\<*segment_size*\>

When a block topology is used, this defines the size of the segments that will be used to create the job allocation. No requirement would be placed on all segments for a job needing to be placed within the same higher-level block.

**NOTE**: The requested node count must always be evenly divisible by the requested segment size.

**NOTE**: When used in conjunction with **\--nodelist=\<node_list\>**: The requested node count must be less than or equal to the total number of unique nodes specified in the **\--nodelist** argument. Requesting more nodes than available unique nodes in the provided **\--nodelist** will result in the job being rejected by slurmctld.

**\--send-libs**\[=yes\|no\]

If set to *yes* (or no argument), autodetect and broadcast the executable\'s shared object dependencies to allocated compute nodes. The files are placed in a directory alongside the executable. The **LD_LIBRARY_PATH** is automatically updated to include this cache directory as well. This overrides the default behavior configured in slurm.conf **SbcastParameters send_libs**. This option only works in conjunction with **\--bcast**. See also **\--bcast-exclude**.

**\--signal**=\[R:\]\<*sig_num*\>\[@*sig_time*\]

When a job is within *sig_time* seconds of its end time, send it the signal *sig_num*. Due to the resolution of event handling by Slurm, the signal may be sent up to 60 seconds earlier than specified. *sig_num* may either be a signal number or name (e.g. \"10\" or \"USR1\"). *sig_time* must have an integer value between 0 and 65535. By default, no signal is sent before the job\'s end time. If a *sig_num* is specified without any *sig_time*, the default time will be 60 seconds. This option applies to job allocations. Use the \"R:\" option to allow this job to overlap with a reservation with MaxStartDelay set. If the \"R:\" option is used, preemption must be enabled on the system, and if the job is preempted it will be requeued if allowed otherwise the job will be canceled. To have the signal sent at preemption time see the **send_user_signal** **PreemptParameter**.

**\--slurmd-debug**=\<*level*\>

Specify a debug level for this step. The *level* may be specified either as an integer value between 2 \[error\] and 6 \[debug2\], or as one of the *SlurmdDebug* tags.

:   

    **error**
    :   Log only errors

    :   

    **info**
    :   Log errors and general informational messages

    :   

    **verbose**
    :   Log errors and verbose informational messages

    :   

    **debug**
    :   Log errors and verbose informational messages and debugging messages

    :   

    **debug2**
    :   Log errors and verbose informational messages and more debugging messages

The slurmd debug information is copied onto the stderr of the job. By default only errors are displayed. This option applies to job and step allocations.

**\--sockets-per-node**=\<*sockets*\>

Restrict node selection to nodes with at least the specified number of sockets. See additional information under **-B** option above when task/affinity plugin is enabled. This option applies to job allocations.\
**NOTE**: This option may implicitly impact the number of tasks if **-n** was not specified.

**\--spread-job**

Spread the job allocation over as many nodes as possible and attempt to evenly distribute tasks across the allocated nodes. This option disables the topology/tree plugin. This option applies to job allocations.

**\--spread-segments**

Prevent nodes within the same base block from being allocated to separate segments within the same block.

This option applies to job allocations. **NOTE**: This option will only work with the **topology/block** plugin.

**\--stepmgr**

Enable slurmstepd step management per-job if it isn\'t enabled system wide. This enables job steps to be managed by a single extern slurmstepd associated with the job to manage steps. This is beneficial for jobs that submit many steps inside their allocations. **PrologFlags=contain** must be set. This option applies to job allocations.

**\--switches**=\<*count*\>\[@*max-time*\]

When a tree topology is used, this defines the maximum count of leaf switches desired for the job allocation and optionally the maximum time to wait for that number of switches. If Slurm finds an allocation containing more switches than the count specified, the job remains pending until it either finds an allocation with desired switch count or the time limit expires. It there is no switch count limit, there is no delay in starting the job. Acceptable time formats include \"minutes\", \"minutes:seconds\", \"hours:minutes:seconds\", \"days-hours\", \"days-hours:minutes\" and \"days-hours:minutes:seconds\". The job\'s maximum time delay may be limited by the system administrator using the **SchedulerParameters** configuration parameter with the **max_switch_wait** parameter option. On a dragonfly network the only switch count supported is 1 since communication performance will be highest when a job is allocate resources on one leaf switch or more than 2 leaf switches. The default max-time is the max_switch_wait SchedulerParameters. This option applies to job allocations.

**\--task-epilog**=\<*executable*\>

The **slurmstepd** daemon will run *executable* just after each task terminates. This will be executed before any TaskEpilog parameter in slurm.conf is executed. This is meant to be a very short-lived program. If it fails to terminate within a few seconds, it will be killed along with any descendant processes. This option applies to step allocations.

**\--task-prolog**=\<*executable*\>

The **slurmstepd** daemon will run *executable* just before launching each task. This will be executed after any TaskProlog parameter in slurm.conf is executed. Besides the normal environment variables, this has SLURM_TASK_PID available to identify the process ID of the task being started. Standard output from this program of the form \"export NAME=value\" will be used to set environment variables for the task being spawned. This option applies to step allocations.

**\--test-only**

Returns an estimate of when a job would be scheduled to run given the current job queue and all the other **srun** arguments specifying the job. This limits **srun\'s** behavior to just return information; no job is actually submitted. The program will be executed directly by the slurmd daemon. This option applies to job allocations.

**\--thread-spec**=\<*num*\>

Count of specialized threads per node reserved by the job for system operations and not used by the application. The application will not use these threads, but will be charged for their allocation. This option can not be used with the **\--core-spec** option. This option applies to job allocations.

**NOTE**: Explicitly setting a job\'s specialized thread value implicitly sets its \--exclusive option, reserving entire nodes for the job.

**-T**, **\--threads**=\<*nthreads*\>

Allows limiting the number of concurrent threads used to send the job request from the srun process to the slurmd processes on the allocated nodes. Default is to use one thread per allocated node up to a maximum of 60 concurrent threads. Specifying this option limits the number of concurrent threads to *nthreads* (less than or equal to 60). This should only be used to set a low thread count for testing on very small memory computers.

**\--threads-per-core**=\<*threads*\>

Restrict node selection to nodes with at least the specified number of threads per core. In task layout, use the specified maximum number of threads per core. Implies **\--cpu-bind=threads** unless overridden by command line or environment options. **NOTE**: \"Threads\" refers to the number of processing units on each core rather than the number of application tasks to be launched per core. See additional information under **-B** option above when task/affinity plugin is enabled. This option applies to job and step allocations.\
**NOTE**: This option may implicitly impact the number of tasks if **-n** was not specified.

**-t**, **\--time**=\<*time*\>

Set a limit on the total run time of the job allocation. If the requested time limit exceeds the partition\'s time limit, the job will be left in a PENDING state (possibly indefinitely). The default time limit is the partition\'s default time limit. When the time limit is reached, each task in each job step is sent SIGTERM followed by SIGKILL. The interval between signals is specified by the Slurm configuration parameter **KillWait**. The **OverTimeLimit** configuration parameter may permit the job to run longer than scheduled. Time resolution is one minute and second values are rounded up to the next minute.

A time limit of zero requests that no time limit be imposed. Acceptable time formats include \"minutes\", \"minutes:seconds\", \"hours:minutes:seconds\", \"days-hours\", \"days-hours:minutes\" and \"days-hours:minutes:seconds\". This option applies to job and step allocations.

**\--time-min**=\<*time*\>

Set a minimum time limit on the job allocation. If specified, the job may have its **\--time** limit lowered to a value no lower than **\--time-min** if doing so permits the job to begin execution earlier than otherwise possible. The job\'s time limit will not be changed after the job is allocated resources. This is performed by a backfill scheduling algorithm to allocate resources otherwise reserved for higher priority jobs. Acceptable time formats include \"minutes\", \"minutes:seconds\", \"hours:minutes:seconds\", \"days-hours\", \"days-hours:minutes\" and \"days-hours:minutes:seconds\". This option applies to job allocations.

**\--tmp**=\<*size*\>\[*units*\]

Specify a minimum amount of temporary disk space per node. Default units are megabytes. Different units can be specified using the suffix \[K\|M\|G\|T\]. This option applies to job allocations.

**\--treewidth**=\<*size*\>

Specify the width of the fanout. Default is the *TreeWidth* specified in the **slurm.conf**. The value may not exceed 65533. A value of \"off\" disables the fanout.

**\--tres-bind**=\<*tres*\>:\[verbose,\]\<*type*\>\[+\<*tres*\>:

\[verbose,\]\<*type*\>\...\] Specify a list of tres with their task binding options. Currently gres are the only supported tres for this options. Specify gres as \"gres/\<gres_name\>\" (e.g. gres/gpu)

Example: \--tres-bind=gres/gpu:verbose,map:0,1,2,3+gres/nic:closest

By default, most tres are not bound to individual tasks

Supported binding *type* options for **gres**:

:   

    **closest**
    :   Bind each task to the gres(s) which are closest. In a NUMA environment, each task may be bound to more than one gres (i.e. all gres in that NUMA environment).

    :   

    **map:\<list\>**
    :   Bind by setting gres masks on tasks (or ranks) as specified where \<list\> is \<gres_id_for_task_0\>,\<gres_id_for_task_1\>,\... gres IDs are interpreted as decimal values. If the number of tasks (or ranks) exceeds the number of elements in this list, elements in the list will be reused as needed starting from the beginning of the list. To simplify support for large task counts, the lists may follow a map with an asterisk and repetition count. For example \"map:0\*4,1\*4\". If the task/cgroup plugin is used and ConstrainDevices is set in cgroup.conf, then the gres IDs are zero-based indexes relative to the gress allocated to the job (e.g. the first gres is 0, even if the global ID is 3). Otherwise, the gres IDs are global IDs, and all gres on each node in the job should be allocated for predictable binding results.

    :   

    **mask:\<list\>**
    :   Bind by setting gres masks on tasks (or ranks) as specified where \<list\> is \<gres_mask_for_task_0\>,\<gres_mask_for_task_1\>,\... The mapping is specified for a node and identical mapping is applied to the tasks on every node (i.e. the lowest task ID on each node is mapped to the first mask specified in the list, etc.). gres masks are always interpreted as hexadecimal values but can be preceded with an optional \'0x\'. To simplify support for large task counts, the lists may follow a map with an asterisk and repetition count. For example \"mask:0x0f\*4,0xf0\*4\". If the task/cgroup plugin is used and ConstrainDevices is set in cgroup.conf, then the gres IDs are zero-based indexes relative to the gres allocated to the job (e.g. the first gres is 0, even if the global ID is 3). Otherwise, the gres IDs are global IDs, and all gres on each node in the job should be allocated for predictable binding results.

    :   

    **none**
    :   Do not bind tasks to this gres (turns off implicit binding from \--tres-per-task and \--gpus-per-task).

    :   

    **per_task:\<gres_per_task\>**
    :   Each task will be bound to the number of gres specified in *\<gres_per_task\>*. Tasks are preferentially assigned gres with affinity to cores in their allocation like in *closest*, though they will take any gres if they are unavailable. If no affinity exists, the first task will be assigned the first x number of gres on the node etc. Shared gres will prefer to bind one sharing device per task if possible.

    :   

    **single:\<tasks_per_gres\>**
    :   Like *closest*, except that each task can only be bound to a single gres, even when it can be bound to multiple gres that are equally close. The gres to bind to is determined by *\<tasks_per_gres\>*, where the first *\<tasks_per_gres\>* tasks are bound to the first gres available, the second *\<tasks_per_gres\>* tasks are bound to the second gres available, etc. This is basically a block distribution of tasks onto available gres, where the available gres are determined by the socket affinity of the task and the socket affinity of the gres as specified in gres.conf\'s *Cores* parameter.

    :   **NOTE**: Shared gres binding is currently limited to per_task or none

**\--tres-per-task**=\<*list*\>

Specifies a comma-delimited list of trackable resources required for the job on each task to be spawned in the job\'s resource allocation. The format for each entry in the list is \"trestype\[/tresname\]=count\". The *trestype* is the type of trackable resource requested (e.g. cpu, gres, license, etc). The *tresname* is the name of the trackable resource, as can be seen with *sacctmgr show tres*. This is required when it exists for tres types such as gres, license, etc. (e.g. gpu, gpu:a100). In order to request a license with this option, the license(s) must be defined in the **AccountingStorageTRES** parameter of slurm.conf. The *count* is the number of those resources.\
The count can have a suffix of\
\"k\" or \"K\" (multiple of 1024),\
\"m\" or \"M\" (multiple of 1024 x 1024),\
\"g\" or \"G\" (multiple of 1024 x 1024 x 1024),\
\"t\" or \"T\" (multiple of 1024 x 1024 x 1024 x 1024),\
\"p\" or \"P\" (multiple of 1024 x 1024 x 1024 x 1024 x 1024).\
Examples:

    --tres-per-task=cpu=4
    --tres-per-task=cpu=8,license/ansys=1
    --tres-per-task=gres/gpu=1
    --tres-per-task=gres/gpu:a100=2

The specified resources will be allocated to the job on each node. The available trackable resources are configurable by the system administrator.\
**NOTE**: This option with gres/gpu or gres/shard will implicitly set \--tres-bind=gres/\[gpu\|shard\]:per_task:\<tres_per_task\>, or if multiple gpu types are specified \--tres-bind=gres/gpu:per_task:\<gpus_per_task_type_sum\>. This can be overridden with an explicit \--tres-bind specification.\
**NOTE**: Invalid TRES for \--tres-per-task include bb,billing,energy,fs,mem,node,pages,vmem.\

**-u**, **\--unbuffered**

By default, the connection between slurmstepd and the user-launched application is over a pipe. The stdio output written by the application is buffered by the glibc until it is flushed or the output is set as unbuffered. See setbuf(3). If this option is specified the tasks are executed with a pseudo terminal so that the application output is unbuffered. This option applies to step allocations.

**\--usage**

Display brief help message and exit.

**\--use-min-nodes**

If a range of node counts is given, prefer the smaller count.

**-v**, **\--verbose**

Increase the verbosity of srun\'s informational messages. Multiple **-v**\'s will further increase srun\'s verbosity. By default only errors will be displayed. This option applies to job and step allocations.

**-V**, **\--version**

Display version information and exit.

**\--wait-for-children**

Wait for all processes in each task to finish before considering a task as ended. The default behavior without this option is to only wait for the parent process in each task to finish.

Depending on the setting of **\--kill-on-bad-exit**, the task may end if the parent process exits with a non-zero exit code. If **\--kill-on-bad-exit**=1 and the parent process exits with a non-zero exit code, the task will end. If **\--kill-on-bad-exit**=0 and the parent process exits with a non-zero exit code, the task will continue until all children processes have exited.

This option requires proctrack/cgroup and cgroup/v2.

**-W**, **\--wait**=\<*seconds*\>

Specify how long to wait after the first task terminates before terminating all remaining tasks. A value of 0 indicates an unlimited wait (a warning will be issued after 60 seconds). The default value is set by the WaitTime parameter in the slurm configuration file (see **[slurm.conf](slurm.conf.md)(5)**). This option can be useful to ensure that a job is terminated in a timely fashion in the event that one or more tasks terminate prematurely. Note: The **-K**, **\--kill-on-bad-exit** option takes precedence over **-W**, **\--wait** to terminate the job immediately if a task exits with a non-zero exit code. This option applies to job allocations.

**\--wckey**=\<*wckey*\>

Specify wckey to be used with job. If TrackWCKey=no (default) in the slurm.conf this value is ignored. This option applies to job allocations.

**\--x11**\[={all\|first\|last}\]

Sets up X11 forwarding on \"all\", \"first\" or \"last\" node(s) of the allocation. This option is only enabled if Slurm was compiled with X11 support and PrologFlags=x11 is defined in the slurm.conf. Default is \"all\".

**srun** will submit the job request to the slurm job controller, then initiate all processes on the remote nodes. If the request cannot be met immediately, **srun** will block until the resources are free to run the job. If the **-I** (**\--immediate**) option is specified **srun** will terminate if resources are not immediately available.

When initiating remote processes **srun** will propagate the current working directory, unless **\--chdir**=\<*path*\> is specified, in which case *path* will become the working directory for the remote processes.

The **-n, -c**, and **-N** options control how CPUs and nodes will be allocated to the job. When specifying only the number of processes to run with **-n**, a default of one CPU per process is allocated. By specifying the number of CPUs required per task (**-c**), more than one CPU may be allocated per process. If the number of nodes is specified with **-N**, **srun** will attempt to allocate *at least* the number of nodes specified.

Combinations of the above three options may be used to change how processes are distributed across nodes and cpus. For instance, by specifying both the number of processes and number of nodes on which to run, the number of processes per node is implied. However, if the number of CPUs per process is more important then number of processes (**-n**) and the number of CPUs per process (**-c**) should be specified.

**srun** will refuse to allocate more than one process per CPU unless **\--overcommit** (**-O**) is also specified.

**srun** will attempt to meet the above specifications \"at a minimum.\" That is, if 16 nodes are requested for 32 processes, and some nodes do not have 2 CPUs, the allocation of nodes will be increased in order to meet the demand for CPUs. In other words, a *minimum* of 16 nodes are being requested. However, if 16 nodes are requested for 15 processes, **srun** will consider this an error, as 15 processes cannot run across 16 nodes.

**IO Redirection**

By default, stdout and stderr will be redirected from all tasks to the stdout and stderr of **srun**, and stdin will be redirected from the standard input of **srun** to all remote tasks. If stdin is only to be read by a subset of the spawned tasks, specifying a file to read from rather than forwarding stdin from the **srun** command may be preferable as it avoids moving and storing data that will never be read.

For OS X, the poll() function does not support stdin, so input from a terminal is not possible.

This behavior may be changed with the **\--output**, **\--error**, and **\--input** (**-o**, **-e**, **-i**) options. Note that **\--error** won\'t redirect the stderr of srun itself, only the stderr from the tasks. Valid format specifications for these options are

**all**
:   stdout stderr is redirected from all tasks to srun. stdin is broadcast to all remote tasks. (This is the default behavior)

:   

**none**
:   stdout and stderr is not received from any task. stdin is not sent to any task (stdin is closed).

:   

**taskid**
:   stdout and/or stderr are redirected from only the task with relative id equal to *taskid*, where 0 \<= *taskid* \<= *ntasks*, where *ntasks* is the total number of tasks in the current job step. stdin is redirected from the stdin of **srun** to this same task. This file will be written on the node executing the task.

:   

**filename**
:   **srun** will redirect stdout and/or stderr to the named file from all tasks. stdin will be redirected from the named file and broadcast to all tasks in the job. *filename* refers to a path on the host that runs **srun**. Depending on the cluster\'s file system layout, this may result in the output appearing in different places depending on whether the job is run in batch mode.

:   

**filename pattern**
:   **srun** allows for a filename pattern to be used to generate the named IO file described above. The following list of format specifiers may be used in the format string to generate a filename that will be unique to a given jobid, stepid, node, or task. In each case, the appropriate number of files are opened and associated with the corresponding tasks. Note that any format string containing %t, %n, and/or %N will be written on the node executing the task rather than the node where **srun** executes.

:   

    :   

        **\\\\**
        :   Do not process any of the replacement symbols.

        :   

        **%%**
        :   The character \"%\".

        :   

        **%A**
        :   Job array\'s master job allocation number.

        :   

        **%a**
        :   Job array ID (index) number.

        :   

        **%J**
        :   jobid.stepid of the running job (e.g. \"128.0\"). The stepid is only expanded for regular steps, not for special steps like \"batch\" or \"extern\".

        :   

        **%j**
        :   jobid of the running job.

        :   

        **%S**
        :   SLUID of the running job.

        :   

        **%s**
        :   stepid of the running job.

        :   

        **%N**
        :   short hostname. This will create a separate IO file per node.

        :   

        **%n**
        :   Node identifier relative to current job (e.g. \"0\" is the first node of the running job) This will create a separate IO file per node.

        :   

        **%t**
        :   task identifier (rank) relative to current job. This will create a separate IO file per task.

        :   

        **%u**
        :   User name.

        :   

        **%x**
        :   Job name.

        :   

        A number placed between the percent character and format specifier may be used to zero-pad the result in the IO filename to at minimum of specified numbers. This number is ignored if the format specifier corresponds to non-numeric data (%N for example). The maximal number is 10, if a value greater than 10 is used the result is padding up to 10 characters. Some examples of how the format string may be used for a 4 task job step with a JobID of 128 and step id of 0 are included below:

        job%J.out
        :   job128.0.out

        :   

        job%4j.out
        :   job0128.out

        :   

        job%2j-%2t.out
        :   job128-00.out, job128-01.out, \...

        :   

[ ]{#lbAH}

## PERFORMANCE

Executing **srun** sends a remote procedure call to **slurmctld**. If enough calls from **srun** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **srun** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **srun** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAI}

## INPUT ENVIRONMENT VARIABLES

Upon startup, srun will read and handle the options set in the following environment variables. The majority of these variables are set the same way the options are set, as defined above. For flag options that are defined to expect no argument, the option can be enabled by setting the environment variable without a value (empty or NULL string), the string \'yes\', or a non-zero number. Any other value for the environment variable will result in the option not being set. There are a couple exceptions to these rules that are noted below.\
**NOTE**: Command line options always override environment variable settings.

**PMI_FANOUT**
:   This is used exclusively with PMI (MPICH2 and MVAPICH2) and controls the fanout of data communications. The srun command sends messages to application programs (via the PMI library) and those applications may be called upon to forward that data to up to this number of additional tasks. Higher values offload work from the srun command to the applications and likely increase the vulnerability to failures. The default value is 32.

:   

**PMI_FANOUT_OFF_HOST**
:   This is used exclusively with PMI (MPICH2 and MVAPICH2) and controls the fanout of data communications. The srun command sends messages to application programs (via the PMI library) and those applications may be called upon to forward that data to additional tasks. By default, srun sends one message per host and one task on that host forwards the data to other tasks on that host up to **PMI_FANOUT**. If **PMI_FANOUT_OFF_HOST** is defined, the user task may be required to forward the data to tasks on other hosts. Setting **PMI_FANOUT_OFF_HOST** may increase performance. Since more work is performed by the PMI library loaded by the user application, failures also can be more common and more difficult to diagnose. Should be disabled/enabled by setting to 0 or 1.

:   

**PMI_TIME**
:   This is used exclusively with PMI (MPICH2 and MVAPICH2) and controls how much the communications from the tasks to the srun are spread out in time in order to avoid overwhelming the srun command with work. The default value is 500 (microseconds) per task. On relatively slow processors or systems with very large processor counts (and large PMI data sets), higher values may be required.

:   

**SLURM_ACCOUNT**
:   Same as **-A, \--account**

:   

**SLURM_ACCTG_FREQ**
:   Same as **\--acctg-freq**

:   

**SLURM_BCAST**
:   Same as **\--bcast**

:   

**SLURM_BCAST_EXCLUDE**
:   Same as **\--bcast-exclude**

:   

**SLURM_BURST_BUFFER**
:   Same as **\--bb**

:   

**SLURM_CLUSTERS**
:   Same as **-M**, **\--clusters**

:   

**SLURM_COMPRESS**
:   Same as **\--compress**

:   

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_CONSTRAINT**
:   Same as **-C**, **\--constraint**

:   

**SLURM_CORE_SPEC**
:   Same as **\--core-spec**

:   

**SLURM_CPU_BIND**
:   Same as **\--cpu-bind**

:   

**SLURM_CPU_FREQ_REQ**
:   Same as **\--cpu-freq**.

:   

**SLURM_CPUS_PER_GPU**
:   Same as **\--cpus-per-gpu**

:   

**SLURM_CPUS_PER_TASK**
:   Same as **-c, \--cpus-per-task** or **\--tres-per-task=cpu=#**

:   

**SLURM_DEBUG**
:   Same as **-v, \--verbose**, when set to 1, when set to 2 gives -vv, etc.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for srun to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

**SLURM_DELAY_BOOT**
:   Same as **\--delay-boot**

:   

**SLURM_DEPENDENCY**
:   Same as **-d, \--dependency**=\<*jobid*\>

:   

**SLURM_DISABLE_STATUS**
:   Same as **-X, \--disable-status**

:   

**SLURM_DIST_PLANESIZE**
:   Plane distribution size. Only used if **\--distribution=plane**, without *=\<size\>*, is set.

:   

**SLURM_DISTRIBUTION**
:   Same as **-m, \--distribution**

:   

**SLURM_EPILOG**
:   Same as **\--epilog**

:   

**SLURM_EXACT**
:   Same as **\--exact**

:   

**SLURM_EXCLUSIVE**
:   Same as **\--exclusive**

:   

**SLURM_EXIT_ERROR**
:   Specifies the exit code generated when a Slurm error occurs (e.g. invalid options). This can be used by a script to distinguish application exit codes from various Slurm error conditions. Also see **SLURM_EXIT_IMMEDIATE**.

:   

**SLURM_EXIT_IMMEDIATE**
:   Specifies the exit code generated when the **\--immediate** option is used and resources are not currently available. This can be used by a script to distinguish application exit codes from various Slurm error conditions. Also see **SLURM_EXIT_ERROR**.

:   

**SLURM_EXPORT_ENV**
:   Same as **\--export**

:   

**SLURM_GPU_BIND**
:   Same as **\--gpu-bind**

:   

**SLURM_GPU_FREQ**
:   Same as **\--gpu-freq**

:   

**SLURM_GPUS**
:   Same as **-G, \--gpus**

:   

**SLURM_GPUS_PER_NODE**
:   Same as **\--gpus-per-node** except within an existing allocation, in which case it will be ignored if **\--gpus** is specified.

:   

**SLURM_GPUS_PER_TASK**
:   Same as **\--gpus-per-task**

:   

**SLURM_GRES**
:   Same as **\--gres**. Also see **SLURM_STEP_GRES**

:   

**SLURM_GRES_FLAGS**
:   Same as **\--gres-flags**

:   

**SLURM_HINT**
:   Same as **\--hint**

:   

**SLURM_IMMEDIATE**
:   Same as **-I, \--immediate**

:   

**SLURM_JOB_ID**
:   Same as **\--jobid**

:   

**SLURM_JOB_NAME**
:   Same as **-J, \--job-name** except within an existing allocation, in which case it is ignored to avoid using the batch job\'s name as the name of each job step.

:   

**SLURM_JOB_NUM_NODES**
:   Same as **-N, \--nodes**. Total number of nodes in the job\'s resource allocation.

:   

**SLURM_KILL_BAD_EXIT**
:   Same as **-K, \--kill-on-bad-exit**. Must be set to 0 or 1 to disable or enable the option.

:   

**SLURM_LABELIO**
:   Same as **-l, \--label**

:   

**SLURM_MEM_BIND**
:   Same as **\--mem-bind**

:   

**SLURM_MEM_PER_CPU**
:   Same as **\--mem-per-cpu**

:   

**SLURM_MEM_PER_GPU**
:   Same as **\--mem-per-gpu**

:   

**SLURM_MEM_PER_NODE**
:   Same as **\--mem**

:   

**SLURM_MPI_TYPE**
:   Same as **\--mpi**

:   

**SLURM_NETWORK**
:   Same as **\--network**

:   

**SLURM_NNODES**
:   Same as **-N, \--nodes**. Total number of nodes in the job\'s resource allocation. See **SLURM_JOB_NUM_NODES**. Included for backwards compatibility.

:   

**SLURM_NO_KILL**
:   Same as **-k**, **\--no-kill**

:   

**SLURM_NPROCS**
:   Same as **-n, \--ntasks**. See **SLURM_NTASKS**. Included for backwards compatibility.

:   

**SLURM_NTASKS**
:   Same as **-n, \--ntasks**

:   

**SLURM_NTASKS_PER_CORE**
:   Same as **\--ntasks-per-core**

:   

**SLURM_NTASKS_PER_GPU**
:   Same as **\--ntasks-per-gpu**

:   

**SLURM_NTASKS_PER_NODE**
:   Same as **\--ntasks-per-node**

:   

**SLURM_NTASKS_PER_SOCKET**
:   Same as **\--ntasks-per-socket**

:   

**SLURM_OOMKILLSTEP**
:   Same as **\--oom-kill-step**

:   

**SLURM_OPEN_MODE**
:   Same as **\--open-mode**

:   

**SLURM_OVERCOMMIT**
:   Same as **-O, \--overcommit**

:   

**SLURM_OVERLAP**
:   Same as **\--overlap**

:   

**SLURM_PARTITION**
:   Same as **-p, \--partition**

:   

**SLURM_PMI_KVS_NO_DUP_KEYS**
:   If set, then PMI key-pairs will contain no duplicate keys. MPI can use this variable to inform the PMI library that it will not use duplicate keys so PMI can skip the check for duplicate keys. This is the case for MPICH2 and reduces overhead in testing for duplicates for improved performance

:   

**SLURM_POWER**
:   Same as **\--power**

:   

**SLURM_PROFILE**
:   Same as **\--profile**

:   

**SLURM_PROLOG**
:   Same as **\--prolog**

:   

**SLURM_QOS**
:   Same as **\--qos**

:   

**SLURM_REMOTE_CWD**
:   Same as **-D, \--chdir=**

:   

**SLURM_REQ_SWITCH**
:   When a tree topology is used, this defines the maximum count of switches desired for the job allocation and optionally the maximum time to wait for that number of switches. See **\--switches**

:   

**SLURM_RESERVATION**
:   Same as **\--reservation**

:   

**SLURM_RESV_PORTS**
:   Same as **\--resv-ports**

:   

**SLURM_SEND_LIBS**
:   Same as **\--send-libs**

:   

**SLURM_SIGNAL**
:   Same as **\--signal**

:   

**SLURM_SPREAD_JOB**
:   Same as **\--spread-job**

:   

**SLURM_SRUN_REDUCE_TASK_EXIT_MSG**
:   if set and non-zero, successive task exit messages with the same exit code will be printed only once.

:   

**SRUN_ERROR**
:   Same as **-e, \--error**

:   

**SRUN_INPUT**
:   Same as **-i, \--input**

:   

**SRUN_OUTPUT**
:   Same as **-o, \--output**

:   

**SLURM_STEP_GRES**
:   Same as **\--gres** (only applies to job steps, not to job allocations). Also see **SLURM_GRES**

:   

**SLURM_STEP_KILLED_MSG_NODE_ID**=ID
:   If set, only the specified node will log when the job or step are killed by a signal.

:   

**SLURM_TASK_EPILOG**
:   Same as **\--task-epilog**

:   

**SLURM_TASK_PROLOG**
:   Same as **\--task-prolog**

:   

SLURM_TEST_EXEC
:   If defined, srun will verify existence of the executable program along with user execute permission on the node where srun was called before attempting to launch it on nodes in the step.

:   

**SLURM_THREAD_SPEC**
:   Same as **\--thread-spec**

:   

**SLURM_THREADS**
:   Same as **-T, \--threads**

:   

**SLURM_THREADS_PER_CORE**
:   Same as **\--threads-per-core**

:   

**SLURM_TIMELIMIT**
:   Same as **-t, \--time**

:   

**SLURM_TRES_BIND**
:   Same as **\--tres-bind** If **\--gpu-bind** is specified, it is also set in **SLURM_TRES_BIND** as if it were specified in **\--tres-bind**.

:   

**SLURM_TRES_PER_TASK**
:   Same as **\--tres-per-task**.

:   

**SLURM_UMASK**
:   If defined, Slurm will use the defined *umask* to set permissions when creating the output/error files for the job.

:   

**SLURM_UNBUFFEREDIO**
:   Same as **-u, \--unbuffered**

:   

**SLURM_USE_MIN_NODES**
:   Same as **\--use-min-nodes**

:   

**SLURM_WAIT**
:   Same as **-W, \--wait**

:   

**SLURM_WAIT4SWITCH**
:   Max time waiting for requested switches. See **\--switches**

:   

**SLURM_WCKEY**
:   Same as **-W, \--wckey**

:   

**SLURM_WORKING_DIR**
:   **-D, \--chdir**

:   

**SLURMD_DEBUG**
:   Same as **\--slurmd-debug**.

:   

**SRUN_CONTAINER**
:   Same as **\--container**.

:   

**SRUN_CONTAINER_ID**
:   Same as **\--container-id**.

:   

**SRUN_EXPORT_ENV**
:   Same as **\--export**, and will override any setting for **SLURM_EXPORT_ENV**.

:   

**SRUN_SEGMENT_SIZE**
:   Same as **\--segment**

:   

[ ]{#lbAJ}

## OUTPUT ENVIRONMENT VARIABLES

srun will set some environment variables in the environment of the executing tasks on the remote compute nodes. These environment variables are:

**SLURM\_\*\_HET_GROUP\_#**
:   For a heterogeneous job allocation, the environment variables are set separately for each component.

:   

**SLURM_CLUSTER_NAME**
:   Name of the cluster on which the job is executing.

:   

**SLURM_CPU_BIND_LIST**
:   **\--cpu-bind** map or mask list (list of Slurm CPU IDs or masks for this node, CPU_ID = Board_ID x threads_per_board + Socket_ID x threads_per_socket + Core_ID x threads_per_core + Thread_ID).

:   

**SLURM_CPU_BIND_TYPE**
:   **\--cpu-bind** type (none,map_cpu:,mask_cpu:,rank_ldom,map_ldom:,mask_ldom:).

:   

**SLURM_CPU_BIND_VERBOSE**
:   **\--cpu-bind** verbosity (quiet,verbose).

:   

**SLURM_CPU_FREQ_REQ**
:   Contains the value requested for cpu frequency on the srun command as a numerical frequency in kilohertz, or a coded value for a request of *low*, *medium*,*highm1* or *high* for the frequency. See the description of the **\--cpu-freq** option or the **SLURM_CPU_FREQ_REQ** input environment variable.

:   

**SLURM_CPUS_ON_NODE**
:   Number of CPUs available to the step on this node. **NOTE**: The **select/linear** plugin allocates entire nodes to jobs, so the value indicates the total count of CPUs on the node. For the **cons/tres** plugin, this number indicates the number of CPUs on this node allocated to the step.

:   

**SLURM_CPUS_PER_TASK**
:   Number of cpus requested per task. Only set if either the **\--cpus-per-task** option or the **\--tres-per-task=cpu=#** option is specified.

:   

**SLURM_DISTRIBUTION**
:   Distribution type for the allocated jobs. Set the distribution with **-m**, **\--distribution**.

:   

**SLURM_GPUS_ON_NODE**
:   Number of GPUs available to the step on this node.

:   

**SLURM_GTIDS**
:   Global task IDs running on this node. Zero origin and comma separated. It is read internally by pmi if Slurm was built with pmi support. Leaving the variable set may cause problems when using external packages from within the job (Abaqus and Ansys have been known to have problems when it is set - consult the appropriate documentation for 3rd party software).

:   

**SLURM_HET_SIZE**
:   Set to count of components in heterogeneous job.

:   

**SLURM_JOB_ACCOUNT**
:   Account name associated of the job allocation.

:   

**SLURM_JOB_CPUS_PER_NODE**
:   Count of CPUs available to the job on the nodes in the allocation, using the format *CPU_count*\[(x*number_of_nodes*)\]\[,*CPU_count* \[(x*number_of_nodes*)\] \...\]. For example: SLURM_JOB_CPUS_PER_NODE=\'72(x2),36\' indicates that on the first and second nodes (as listed by SLURM_JOB_NODELIST) the allocation has 72 CPUs, while the third node has 36 CPUs. **NOTE**: The **select/linear** plugin allocates entire nodes to jobs, so the value indicates the total count of CPUs on allocated nodes. The **select/cons_tres** plugin allocates individual CPUs to jobs, so this number indicates the number of CPUs allocated to the job.

:   

**SLURM_JOB_DEPENDENCY**
:   Set to value of the **\--dependency** option.

:   

**SLURM_JOB_END_TIME**
:   The UNIX timestamp for a job\'s projected end time.

:   

**SLURM_JOB_GPUS**
:   The global GPU IDs of the GPUs allocated to this job. The GPU IDs are not relative to any device cgroup, even if devices are constrained with task/cgroup. Only set in batch and interactive jobs.

:   

**SLURM_JOB_ID**
:   Job id of the executing job.

:   

**SLURM_JOB_LICENSES**
:   Name and count of any license(s) requested.

:   

**SLURM_JOB_NAME**
:   Set to the value of the **\--job-name** option or the command name when srun is used to create a new job allocation. Not set when srun is used only to create a job step (i.e. within an existing job allocation).

:   

**SLURM_JOB_NODELIST**
:   List of nodes allocated to the job.

:   

**SLURM_JOB_NODES**
:   Total number of nodes in the job\'s resource allocation.

:   

**SLURM_JOB_PARTITION**
:   Name of the partition in which the job is running.

:   

**SLURM_JOB_QOS**
:   Quality Of Service (QOS) of the job allocation.

:   

**SLURM_JOB_RESERVATION**
:   Advanced reservation containing the job allocation, if any.

:   

**SLURM_JOB_SEGMENT_SIZE**
:   The size of the segments that was used to create the job allocation. Only set if \--segment is specified.

:   

**SLURM_JOB_START_TIME**
:   The UNIX timestamp for a job\'s start time.

:   

**SLURM_JOBID**
:   Job id of the executing job. See **SLURM_JOB_ID**. Included for backwards compatibility.

:   

**SLURM_LAUNCH_NODE_IPADDR**
:   IP address of the node from which the task launch was initiated (where the srun command ran from).

:   

**SLURM_LOCALID**
:   Node local task ID for the process within a job.

:   

**SLURM_MEM_BIND_LIST**
:   **\--mem-bind** map or mask list (\<list of IDs or masks for this node\>).

:   

**SLURM_MEM_BIND_PREFER**
:   **\--mem-bind** prefer (prefer).

:   

**SLURM_MEM_BIND_TYPE**
:   **\--mem-bind** type (none,rank,map_mem:,mask_mem:,local).

:   

**SLURM_MEM_BIND_VERBOSE**
:   **\--mem-bind** verbosity (quiet,verbose).

:   

**SLURM_NETWORK**
:   Set to the value of the **\--network** option, if specified.

:   

**SLURM_NODEID**
:   The relative node ID of the current node.

:   

**SLURM_NPROCS**
:   Total number of processes in the current job or job step. See **SLURM_NTASKS**. Included for backwards compatibility.

:   

**SLURM_NTASKS**
:   Total number of processes in the current job or job step.

:   

**SLURM_OVERCOMMIT**
:   Set to **1** if **\--overcommit** was specified.

:   

**SLURM_PRIO_PROCESS**
:   The scheduling priority (nice value) at the time of job submission. This value is propagated to the spawned processes.

:   

**SLURM_PROCID**
:   The MPI rank (or relative process ID) of the current process.

:   

**SLURM_SRUN_COMM_HOST**
:   IP address of srun communication host.

:   

**SLURM_SRUN_COMM_PORT**
:   srun communication port.

:   

**SLURM_CONTAINER**
:   OCI Bundle for job. Only set if **\--container** is specified.

:   

**SLURM_CONTAINER_ID**
:   OCI id for job. Only set if **\--container_id** is specified.

:   

**SLURM_SHARDS_ON_NODE**
:   Number of GPU Shards available to the step on this node.

:   

**SLURM_STEP_GPUS**
:   The global GPU IDs of the GPUs allocated to this step (excluding batch and interactive steps). The GPU IDs are not relative to any device cgroup, even if devices are constrained with task/cgroup.

:   

**SLURM_STEP_ID**
:   The step ID of the current job.

:   

**SLURM_STEP_LAUNCHER_PORT**
:   Step launcher port.

:   

**SLURM_STEP_NODELIST**
:   List of nodes allocated to the step.

:   

**SLURM_STEP_NUM_NODES**
:   Number of nodes allocated to the step.

:   

**SLURM_STEP_NUM_TASKS**
:   Number of processes in the job step or whole heterogeneous job step.

:   

**SLURM_STEP_TASKS_PER_NODE**
:   Number of processes per node within the step.

:   

**SLURM_STEPID**
:   The step ID of the current job. See **SLURM_STEP_ID**. Included for backwards compatibility.

:   

**SLURM_SUBMIT_DIR**
:   The directory from which the allocation was invoked from.

:   

**SLURM_SUBMIT_HOST**
:   The hostname of the computer from which the allocation was invoked from.

:   

**SLURM_TASK_PID**
:   The process ID of the task being started.

:   

**SLURM_TASKS_PER_NODE**
:   Number of tasks to be initiated on each node. Values are comma separated and in the same order as SLURM_JOB_NODELIST. If two or more consecutive nodes are to have the same task count, that count is followed by \"(x#)\" where \"#\" is the repetition count. For example, \"SLURM_TASKS_PER_NODE=2(x3),1\" indicates that the first three nodes will each execute two tasks and the fourth node will execute one task.

:   

**SLURM_TOPOLOGY_ADDR**
:   This is set only if the system has the topology/tree plugin configured. The value will be set to the names network switches which may be involved in the job\'s communications from the system\'s top level switch down to the leaf switch and ending with node name. A period is used to separate each hardware component name.

:   

**SLURM_TOPOLOGY_ADDR_PATTERN**
:   This is set only if the system has the topology/tree plugin configured. The value will be set component types listed in **SLURM_TOPOLOGY_ADDR**. Each component will be identified as either \"switch\" or \"node\". A period is used to separate each hardware component type.

:   

**SLURM_TRES_PER_TASK**
:   Set to the value of **\--tres-per-task**. If **\--cpus-per-task** or **\--gpus-per-task** is specified, it is also set in **SLURM_TRES_PER_TASK** as if it were specified in **\--tres-per-task**.

:   

**SLURM_UMASK**
:   The *umask* in effect when the job was submitted.

:   

**SLURMD_NODENAME**
:   Name of the node running the task. In the case of a parallel job executing on multiple compute nodes, the various tasks will have this environment variable set to different values on each compute node.

:   

**SRUN_DEBUG**
:   Set to the logging level of the **srun** command. Default value is 3 (info level). The value is incremented or decremented based upon the **\--verbose** and **\--quiet** options.

:   

[ ]{#lbAK}

## SIGNALS AND ESCAPE SEQUENCES

Signals sent to the **srun** command are automatically forwarded to the tasks it is controlling with a few exceptions. The escape sequence **\<control-c\>** will report the state of all tasks associated with the **srun** command. If **\<control-c\>** is entered twice within one second, then the associated SIGINT signal will be sent to all tasks and a termination sequence will be entered sending SIGCONT, SIGTERM, and SIGKILL to all spawned tasks. If a third **\<control-c\>** is received, the srun program will be terminated without waiting for remote tasks to exit or their I/O to complete.

The escape sequence **\<control-z\>** is presently ignored.

[ ]{#lbAL}

## MPI SUPPORT

MPI use depends upon the type of MPI being used. There are three fundamentally different modes of operation used by these various MPI implementations.

1\. Slurm directly launches the tasks and performs initialization of communications through the PMI2 or PMIx APIs. For example: \"srun -n16 a.out\".

2\. Slurm creates a resource allocation for the job and then mpirun launches tasks using Slurm\'s infrastructure (OpenMPI).

3\. Slurm creates a resource allocation for the job and then mpirun launches tasks using some mechanism other than Slurm, such as SSH or RSH. These tasks are initiated outside of Slurm\'s monitoring or control. Slurm\'s epilog should be configured to purge these tasks when the job\'s allocation is relinquished, or the use of pam_slurm_adopt is highly recommended.

See *[https://slurm.schedmd.com/mpi_guide.html](mpi_guide.md)* for more information on use of these various MPI implementations with Slurm.

[ ]{#lbAM}

## MULTIPLE PROGRAM CONFIGURATION

Comments in the configuration file must have a \"#\" in column one. The configuration file contains the following fields separated by white space:

Task rank
:   One or more task ranks to use this configuration. Multiple values may be comma separated. Ranges may be indicated with two numbers separated with a \'-\' with the smaller number first (e.g. \"0-4\" and not \"4-0\"). To indicate all tasks not otherwise specified, specify a rank of \'\*\' as the last line of the file. If an attempt is made to initiate a task for which no executable program is defined, the following error message will be produced \"No executable program specified for this task\".

:   

Executable
:   The name of the program to execute. May be fully qualified pathname if desired.

:   

Arguments
:   Program arguments. The expression \"%t\" will be replaced with the task\'s number. The expression \"%o\" will be replaced with the task\'s offset within this range (e.g. a configured task rank value of \"1-5\" would have offset values of \"0-4\"). Single quotes may be used to avoid having the enclosed values interpreted. This field is optional. Any arguments for the program entered on the command line will be added to the arguments specified in the configuration file.

For example:

    $ cat silly.conf
    ###################################################################
    # srun multiple program configuration file
    #
    # srun -n8 -l --multi-prog silly.conf
    ###################################################################
    4-6       hostname
    1,7       echo  task:%t
    0,2-3     echo  offset:%o

    $ srun -n8 -l --multi-prog silly.conf
    0: offset:0
    1: task:1
    2: offset:1
    3: offset:2
    4: linux15.llnl.gov
    5: linux16.llnl.gov
    6: linux17.llnl.gov
    7: task:7

[ ]{#lbAN}

## EXAMPLES

**Example 1:**
:   This simple example demonstrates the execution of the command **hostname** in eight tasks. At least eight processors will be allocated to the job (the same as the task count) on however many nodes are required to satisfy the request. The output of each task will be proceeded with its task number. (The machine \"dev\" in the example below has a total of two CPUs per node)

:   $ srun -n8 -l hostname
        0: dev0
        1: dev0
        2: dev1
        3: dev1
        4: dev2
        5: dev2
        6: dev3
        7: dev3

**Example 2:**
:   The srun **-r** option is used within a job script to run two job steps on disjoint nodes in the following example. The script is run using allocate mode instead of as a batch job in this case.

:   $ cat test.sh
        #!/bin/sh
        echo $SLURM_JOB_NODELIST
        srun -lN2 -r2 hostname
        srun -lN2 hostname

        $ salloc -N4 test.sh
        dev[7-10]
        0: dev9
        1: dev10
        0: dev7
        1: dev8

**Example 3:**
:   The following script runs two job steps in parallel within an allocated set of nodes.

:   $ cat test.sh
        #!/bin/bash
        srun -lN2 -n4 -r 2 sleep 60 &
        srun -lN2 -r 0 sleep 60 &
        sleep 1
        squeue
        squeue -s
        wait

        $ salloc -N4 test.sh
          JOBID PARTITION     NAME     USER  ST      TIME  NODES NODELIST
          65641     batch  test.sh   grondo   R      0:01      4 dev[7-10]

        STEPID     PARTITION     USER      TIME NODELIST
        65641.0        batch   grondo      0:01 dev[7-8]
        65641.1        batch   grondo      0:01 dev[9-10]

**Example 4:**
:   This example demonstrates how one executes a simple MPI job. We use **srun** to build a list of machines (nodes) to be used by **mpirun** in its required format. A sample command line and the script to be executed follow.

:   $ cat test.sh
        #!/bin/sh
        MACHINEFILE="nodes.$SLURM_JOB_ID"

        # Generate Machinefile for mpi such that hosts are in the same
        #  order as if run via srun
        #
        srun -l /bin/hostname | sort -n | awk '{print $2}' > $MACHINEFILE

        # Run using generated Machine file:
        mpirun -np $SLURM_NTASKS -machinefile $MACHINEFILE mpi-app

        rm $MACHINEFILE

        $ salloc -N2 -n4 test.sh

**Example 5:**
:   This simple example demonstrates the execution of different jobs on different nodes in the same srun. You can do this for any number of nodes or any number of jobs. The executables are placed on the nodes sited by the SLURM_NODEID env var. Starting at 0 and going to the number specified on the srun command line.

:   $ cat test.sh
        case $SLURM_NODEID in
            0) echo "I am running on "
               hostname ;;
            1) hostname
               echo "is where I am running" ;;
        esac

        $ srun -N2 test.sh
        dev0
        is where I am running
        I am running on
        dev1

**Example 6:**
:   This example demonstrates use of multi-core options to control layout of tasks. We request that four sockets per node and two cores per socket be dedicated to the job.

:   $ srun -N2 -B 4-4:2-2 a.out

**Example 7:**
:   This example shows a script in which Slurm is used to provide resource management for a job by executing the various job steps as processors become available for their dedicated use.

:   $ cat my.script
        #!/bin/bash
        srun -n4 prog1 &
        srun -n3 prog2 &
        srun -n1 prog3 &
        srun -n1 prog4 &
        wait

**Example 8:**
:   This example shows how to launch an application called \"server\" with one task, 8 CPUs and 16 GB of memory (2 GB per CPU) plus another application called \"client\" with 16 tasks, 1 CPU per task (the default) and 1 GB of memory per task.

:   $ srun -n1 -c8 --mem-per-cpu=2gb server : -n16 --mem-per-cpu=1gb client

**Example 9:**
:   This example highlights the difference in behavior with srun\'s **\--exclusive** and **\--overlap** flags when run from inside a job allocation. The **\--overlap** flag allows both steps to start at the same time. The **\--exclusive** flag makes the second step wait until the first has finished.

:   $ salloc  -n1
        salloc: Granted job allocation 9553
        salloc: Waiting for resource configuration
        salloc: Nodes node01 are ready for job

        $ date +%T; srun -n1 --overlap -l sleep 3 &
        $ srun -n1 --overlap -l date +%T &
        14:36:04
        [1] 144341
        [2] 144342
        0: 14:36:04
        [2]+  Done                    srun -n1 --overlap -l date +%T
        [1]+  Done                    srun -n1 --overlap -l sleep 3

        $ date +%T; srun -n1 --exclusive -l sleep 3 &
        $ srun -n1 --exclusive -l date +%T &
        14:36:17
        [1] 144429
        [2] 144430
        srun: Job 9553 step creation temporarily disabled, retrying (Requested nodes are busy)
        srun: Step created for job 9553
        0: 14:36:20
        [1]-  Done                    srun -n1 --exclusive -l sleep 3
        [2]+  Done                    srun -n1 --exclusive -l date +%T

**Example 10:**
:   This example demonstrates how jobs that are not evenly split among multiple nodes can run into problems of tasks not being able to start when there are enough CPUs free to run that task on a single node. This example shows a job that was allocated 2 CPUs on one node and 24 CPUs on the other node.

:   $ echo $SLURM_NODELIST; echo $SLURM_JOB_CPUS_PER_NODE
        node[01-02]
        2,24

    If a task is started that occupies the CPUs on the node with fewer CPUs, then a subsequent task that should be able to start on the other node will not start because it inherits the requirement for the number of nodes from the job allocation. The job step will stay pending until the first job step completes or until it is cancelled.

        $ srun -n4 --exact sleep 1800 &
        [1] 151837

        $ srun -n2 --exact hostname
        ^Csrun: Cancelled pending job step with signal 2
        srun: error: Unable to create step for job 2677: Job/step already completing or completed

    If the job step is started, explicitly requesting a single node, then the step is able to run.

        $ srun -n2 -N1 --exact hostname
        node02
        node02

    This behavior can be changed by adding **SelectTypeParameters=CR_Pack_Nodes** to your slurm.conf. The logic to pack nodes will allow job steps to start on a single node without having to explicitly request a single node.

**Example 11:**

:   This example demonstrates that adding the **\--exclusive** flag to job allocation requests can give different results based on whether you also request a certain number of tasks.

    Requesting exclusive access with no additional requirements will allow the process to access all the CPUs on the allocated node.

        $ srun -l --exclusive  bash -c 'grep Cpus_allowed_list /proc/self/status'
        0: Cpus_allowed_list:   0-23

    Adding a request for a certain number of tasks will cause each task to only have access to a single CPU.

        $ srun -l --exclusive -n2 bash -c 'grep Cpus_allowed_list /proc/self/status'
        0: Cpus_allowed_list:   0
        1: Cpus_allowed_list:   12

    You can define the number of CPUs per task if you want to give them access to more than one CPU.

        $ srun -l --exclusive -n2 --cpus-per-task=12 bash -c 'grep Cpus_allowed_list /proc/self/status'
        0: Cpus_allowed_list:   0-5,12-17
        1: Cpus_allowed_list:   6-11,18-23

[ ]{#lbAO}

## COPYING

Copyright (C) 2006-2007 The Regents of the University of California. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2008-2010 Lawrence Livermore National Security.\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAP}

## SEE ALSO

**[salloc](salloc.md)**(1), **[sattach](sattach.md)**(1), **[sbatch](sbatch.md)**(1), **[sbcast](sbcast.md)**(1), **[scancel](scancel.md)**(1), **[scontrol](scontrol.md)**(1), **[squeue](squeue.md)**(1), **[slurm.conf](slurm.conf.md)**(5), **sched_setaffinity** (2), **numa** (3) **getrlimit** (2)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

SYNOPSIS

:   

DESCRIPTION

:   

RETURN VALUE

:   

EXECUTABLE PATH RESOLUTION

:   

OPTIONS

:   

PERFORMANCE

:   

INPUT ENVIRONMENT VARIABLES

:   

OUTPUT ENVIRONMENT VARIABLES

:   

SIGNALS AND ESCAPE SEQUENCES

:   

MPI SUPPORT

:   

MULTIPLE PROGRAM CONFIGURATION

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
