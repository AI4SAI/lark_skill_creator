# scontrol

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

scontrol - view or modify Slurm configuration and state.

[ ]{#lbAC}

## SYNOPSIS

**scontrol** \[*OPTIONS*\...\] \[*COMMAND*\...\]

[ ]{#lbAD}

## DESCRIPTION

**scontrol** is used to view or modify Slurm configuration including: job, job step, node, partition, reservation, and overall system configuration. Most of the commands require elevated permissions to run (also see the **AUTHORIZATION** section). If a user runs a command without the required permissions, an error message will be printed and the requested action will not occur. If no command is entered on the execute line, **scontrol** will operate in an interactive mode and prompt for input. It will continue prompting for input and executing commands until explicitly terminated. If a command is entered on the execute line, **scontrol** will execute that command and terminate. All commands and options are case-insensitive, although node names, partition names, and reservation names are case-sensitive (node names \"LX\" and \"lx\" are distinct). All commands and options can be abbreviated to the extent that the specification is unique. A modified Slurm configuration can be written to a file using the *scontrol write config* command. The resulting file will be named using the convention \"slurm.conf.\<datetime\>\" and located in the same directory as the original \"slurm.conf\" file. The directory containing the original slurm.conf must be writable for this to occur.

[ ]{#lbAE}

## OPTIONS

**-a**, **\--all**
:   When the *show* command is used, then display all partitions, their jobs and jobs steps. This causes information to be displayed about partitions that are configured as hidden and partitions that are unavailable to user\'s group.

:   

**-M**, **\--clusters**=\<*string*\>
:   The cluster to issue commands to. Only one cluster name may be specified. Note that the **slurmdbd** must be up for this option to work properly, unless running in a federation with either **FederationParameters=fed_display** configured or the **\--federation** option set. This option implicitly sets the **\--local** option.

:   

**-d**, **\--details**
:   Causes the *show* command to provide additional details where available.

:   

**\--federation**
:   Report jobs from federation if a member of one.

:   

**-F**, **\--future**
:   Report nodes in FUTURE state.

:   

**-h**, **\--help**
:   Print a help message describing the usage of scontrol.

:   

**\--hide**
:   Do not display information about hidden partitions, their jobs and job steps. By default, neither partitions that are configured as hidden nor those partitions unavailable to user\'s group will be displayed (i.e. this is the default behavior).

:   

**\--json**, **\--json**=*list*, **\--json**=\<*data_parser*\>
:   Dump information as JSON using the default data_parser plugin or explicit data_parser with parameters. All information is dumped, even if it would normally not be. Sorting and formatting arguments passed to other options are ignored; however, most filtering arguments are still used. This option is not available for every command. This option implicitly sets the **\--details** option.

:   

**\--local**
:   Show only information local to this cluster. Ignore other clusters in the federated if a member of one. Overrides \--federation.

:   

**-o**, **\--oneliner**
:   Print information one line per record.

:   

**-Q**, **\--quiet**
:   Print no warning or informational messages, only fatal error messages.

:   

**\--sibling**
:   Show all sibling jobs on a federated cluster. Implies \--federation.

:   

**-u**, **\--uid**=\<*uid*\>
:   Attempt to update a job as user \<uid\> instead of the invoking user id.

:   

**-v**, **\--verbose**
:   Print detailed event logging. Multiple \'**-v**\'s will further increase the verbosity of logging. By default only errors will be displayed.

:   

**-V** , **\--version**
:   Print version information and exit.

:   

**\--yaml**, **\--yaml**=*list*, **\--yaml**=\<*data_parser*\>
:   Dump information as YAML using the default data_parser plugin or explicit data_parser with parameters. All information is dumped, even if it would normally not be. Sorting and formatting arguments passed to other options are ignored; however, most filtering arguments are still used. This option is not available for every command. This option implicitly sets the **\--details** option.

:   

[ ]{#lbAF}

## COMMANDS

**cancel_reboot** \<*NodeList*\>
:   Cancel pending reboots on nodes. The node will be undrain\'ed and the reason cleared if the node was drained by an ASAP reboot.

:   

**create** \<*SPECIFICATION*\>
:   Create a new node, partition, or reservation. See the full list of parameters below.

:   

**completing**
:   Display all jobs in a COMPLETING state along with associated nodes in either a COMPLETING or DOWN state.

:   

**delete** \<*SPECIFICATION*\>
:   Delete the entry with the specified *SPECIFICATION*. The following *SPECIFICATION* choices are available:

:   

    :   

        **NodeName**=\<*nodelist*\>
        :   Node name or list of node names to delete. Only dynamic nodes that have no running jobs and that are not part of a reservation can be deleted.
            Multiple node names may be specified using simple node range expressions (e.g., \"lx\[10-20\]\"). Nodesets can also be specified by themselves or mixed with node range expressions, using a comma as a list separator. If the keyword \"ALL\" is specified alone, then the delete will be attempted against all the nodes in the local cluster (and will fail on nodes ineligible for deletion).

        :   

        **PartitionName**=\<*name*\>
        :   Name of partition to delete. The partition must have no associated jobs running or pending, otherwise the request is denied. It may be helpful to modify pending jobs or to change the partition state ahead of time. Note that if this partition is present in the **slurm.conf** file, it will be recreated the next time the controller is restarted or reconfigured.

        :   

        **ReservationName**=\<*name*\>
        :   Name of reservation to delete. The reservation must have no associated jobs, otherwise the request is denied. It may be helpful to modify pending jobs to not use the reservation. You can also plan the reservation\'s deletion ahead of time by setting an **EndTime** or **Duration**.
            A privileged user can delete any reservation. An unprivileged user may be able to delete a reservation they have access to if **SlurmctldParameters=user_resv_delete** is set in *slurm.conf* or if **Flags=USER_DELETE** is set on the reservation.

        :   

:   

**errnumstr** \<*ERRNO*\>
:   Given a Slurm error number, return a descriptive string.

:   

**fsdampeningfactor** \<*FACTOR*\>
:   Set the FairShareDampeningFactor in slurmctld.

:   

**getaddrs** \<*NODES*\>
:   Get IP addresses of \<*NODES*\> from slurmctld.

:   

**help**
:   Display a description of scontrol options and commands.

:   

**hold** \<*job_list*\>

:   Prevent a pending job from being started (sets its priority to 0). The job_list argument is a space separated list of job IDs OR \"jobname=\" with the job\'s name, which will attempt to hold all jobs having that name.

    Only a privileged user, account coordinator, or job owner may hold jobs. If issued by a privileged user an admin-hold will be placed on the job, otherwise a user-hold will be placed on the job. The hold type determines which users may remove the hold with the **release** command (also see **uhold**).

    Additionally, attempting to hold a running job will not suspend or cancel it. But, it will set the job priority to 0 and update the job reason field, which would hold the job if it was requeued at a later time.

:   

**listjobs** \[\<*NodeName*\>\]
:   Print jobs running on the host that runs this. This contacts any slurmstepd\'s running locally, and does not contact slurmctld
    Use \<*NodeName*\> if using \--enable-multiple-slurmd.

:   

**listpids** \[\<*job_id*\>\[.\<*step_id*\>\]\] \[\<*NodeName*\>\]
:   Print a listing of the process IDs in a job step (if JOBID.STEPID is provided), or all of the job steps in a job (if *job_id* is provided), or all of the job steps in all of the jobs on the local node (if *job_id* is not provided or *job_id* is \"\*\"). This will work only with processes on the node on which scontrol is run, and only for those processes spawned by Slurm and their descendants. Note that some Slurm configurations (*ProctrackType* value of *pgid*) are unable to identify all processes associated with a job or job step.
    Note that the NodeName option is only really useful when you have multiple slurmd daemons running on the same host machine. Multiple slurmd daemons on one host are, in general, only used by Slurm developers.

:   

**liststeps** \[\<*NodeName*\>\]
:   Print steps running on the host that runs this. This contacts any slurmstepd\'s running locally, and does not contact slurmctld
    Use \<*NodeName*\> if using \--enable-multiple-slurmd.

:   

**notify** \<*job_id*\> \<*message*\>
:   Send a message to standard error of the salloc or srun command or batch job associated with the specified *job_id*.

:   

**pidinfo** \<*proc_id*\>
:   Print the Slurm job id and scheduled termination time corresponding to the supplied process id, *proc_id*, on the current node. This will work only with processes on node on which scontrol is run, and only for those processes spawned by Slurm and their descendants.

:   

**ping**
:   Ping the primary and secondary slurmctld daemon and report if they are responding. If **\--clusters** is specified it will only ping the primary slurmctld daemon of the specified cluster.

:   

**power** {up\|down} \[asap\|force\] {ALL\|\<*NodeList*\>\|\<*NodeSet*\>} \[Reason=\<*reason*\>\]

:   Control power state of the provided node list/set. For \'power down\', the optional ASAP/FORCE flag will be added to the power down request, but will otherwise be rejected for power up requests. All arguments will be processed insensitive of case except for the node list/set. Optional *reason* may be be specified only when powering down. This subcommand obsoletes the prior usage of scontrol\'s update command:

    scontrol update NodeName=\<*nodes*\>\
                    State={POWER_UP\|POWER_DOWN\|POWER_DOWN_ASAP\|POWER_DOWN_FORCE}

    :   Commands:

        **down**
        :   Will use the configured *SuspendProgram* program to explicitly place node(s) into power saving mode. If a node is already in the process of being powered down, the command will only change the state of the node but won\'t have any effect until the configured *SuspendTimeout* is reached. Use of this command can be useful in situations where a *ResumeProgram*, like *capmc* in Cray machines, is stalled and one wants to restore the node to \"IDLE\" manually. In this case rebooting the node and setting the state to \"power down\" will cancel the previous \"power up\" state and the node will become \"IDLE\".

        :   

        **down asap**
        :   Will drain the node(s) and mark them for power down. Currently running jobs will complete first and no additional jobs will be allocated to the node(s).

        :   

        **down force**
        :   Will cancel all jobs on the node(s), power them down, and reset their state to \"IDLE\".

        :   

        **up**
        :   Will use the configured *ResumeProgram* program to explicitly move node(s) out of power saving mode. If a node is already in the process of being powered up, the command will only change the state of the node but won\'t have any effect until the configured *ResumeTimeout* is reached.

        :   

:   

**reboot** \[ASAP\] \[nextstate={RESUME\|DOWN}\] \[reason=\<*reason*\>\] {ALL\|\<*NodeList*\>\|\<*NodeSet*\>}

:   Reboot the nodes in the system when they become idle using the **RebootProgram** as configured in Slurm\'s slurm.conf file. Each node will have the \"REBOOT\" flag added to its node state. After a node reboots and the slurmd daemon starts up again, the HealthCheckProgram will run once. Then, the slurmd daemon will register itself with the slurmctld daemon and the \"REBOOT\" flag will be cleared. The \"ASAP\" option adds the \"DRAIN\" flag to each node\'s state, preventing additional jobs from running on the node so it can be rebooted and returned to service \"As Soon As Possible\" (i.e. ASAP). \"ASAP\" will also set the node reason to \"Reboot ASAP\" if the \"reason\" option isn\'t specified and will set nextstate=UNDRAIN if nextstate isn\'t specified. If the \"nextstate\" option is specified as \"DOWN\", then the node will remain in a down state after rebooting. If \"nextstate\" is specified as \"RESUME\", then the nodes will resume as normal and the node\'s reason and \"DRAIN\" state will be cleared. Resuming nodes will be considered as available in backfill future scheduling and won\'t be replaced by idle nodes in a reservation. The \"reason\" option sets each node\'s reason to a user-defined message. A default reason of \"reboot requested\" is set if no other reason is set on the node. The reason will be appended with: \"reboot issued\" when the reboot is issued; \"reboot complete\" when the node registers and has a \"nextstate\" of \"DOWN\"; or \"reboot timed out\" when the node fails to register within **ResumeTimeout**. You must specify either a list of nodes or that ALL nodes are to be rebooted.

    **NOTE**: The reboot request will be ignored for hosts in the following states: FUTURE, POWER_DOWN, POWERED_DOWN, POWERING_DOWN, REBOOT_ISSUED, REBOOT_REQUESTED

    **NOTE**: By default, this command does not prevent additional jobs from being scheduled on any nodes before reboot. To do this, you can either use the \"ASAP\" option or explicitly drain the nodes beforehand. You can alternately create an advanced reservation to prevent additional jobs from being initiated on nodes to be rebooted. Pending reboots can be cancelled by using \"scontrol cancel_reboot \<node\>\" or setting the node state to \"CANCEL_REBOOT\". A node will be marked \"DOWN\" if it doesn\'t reboot within **ResumeTimeout**.

:   

**reconfigure**
:   Instruct all slurmctld and slurmd daemons to re-read the configuration file. This mechanism can be used to modify configuration parameters set in **[slurm.conf](slurm.conf.md)**(5) without interrupting running jobs. Starting in 23.11, this command operates by creating new processes for the daemons, then passing control to the new processes when or if they start up successfully. This allows it to gracefully catch configuration problems and keep running with the previous configuration if there is a problem. This will **not** be able to change the daemons\' listening TCP port settings or authentication mechanism.

:   

**release** \<*job_list*\>
:   Release a previously held job to begin execution. The job_list argument is a space separated list of job IDs OR \"jobname=\" with the job\'s name, which will attempt to release all jobs having that name. Note that a privileged user may release an admin-hold or a user-hold. An unprivileged job owner or coordinator may only release a user-hold. Also see **hold**.

:   

**requeue** \[\<*option*\>\] \<*job_list*\>
:   Requeue a running, suspended or finished Slurm batch job into pending state. The job_list argument is a comma separated list of job IDs. The command accepts the following option:

:   

    :   

        **Incomplete**
        :   Operate only on jobs (or tasks of a job array) which have not completed. Specifically only jobs in the following states will be requeued: CONFIGURING, RUNNING, STOPPED or SUSPENDED.

:   

**requeuehold** \[\<*option*\>\] \<*job_list*\>
:   Requeue a running, suspended or finished Slurm batch job into pending state, moreover the job is put in held state (priority zero). The job_list argument is a comma separated list of job IDs. A held job can be released using scontrol to reset its priority (e.g. \"scontrol release \<job_id\>\"). The command accepts the following options:

:   

    :   

        **Incomplete**
        :   Operate only on jobs (or tasks of a job array) which have not completed. Specifically only jobs in the following states will be requeued: CONFIGURING, RUNNING, STOPPED or SUSPENDED.

        :   

        **State**=SpecialExit
        :   The \"SpecialExit\" keyword specifies that the job has to be put in a special state **JOB_SPECIAL_EXIT**. The \"scontrol show job\" command will display the JobState as **SPECIAL_EXIT**, while the \"squeue\" command as **SE**.

:   

**resume** \<*job_list*\>
:   Resume a previously suspended job. The job_list argument is a comma separated list of job IDs. Also see **suspend**.
    **NOTE**: A suspended job releases its CPUs for allocation to other jobs. Resuming a previously suspended job may result in multiple jobs being allocated the same CPUs, which could trigger gang scheduling with some configurations or severe degradation in performance with other configurations. Use of the scancel command to send SIGSTOP and SIGCONT signals would stop a job without releasing its CPUs for allocation to other jobs and would be a preferable mechanism in many cases. If performing system maintenance you may want to use suspend/resume in the following way. Before suspending set all nodes to draining or set all partitions to down so that no new jobs can be scheduled. Then suspend jobs. Once maintenance is done resume jobs then resume nodes and/or set all partitions back to up. Use with caution. Only a privileged user or an account coordinator can resume jobs.

:   

**schedloglevel** \<*LEVEL*\>
:   Enable or disable scheduler logging. *LEVEL* may be \"0\", \"1\", \"disable\" or \"enable\". \"0\" has the same effect as \"disable\". \"1\" has the same effect as \"enable\". This value is temporary and will be overwritten when the slurmctld daemon reads the slurm.conf configuration file (e.g. when the daemon is restarted or **scontrol reconfigure** is executed) if the SlurmSchedLogLevel parameter is present.

:   

**setdebug** \<*LEVEL*\> \[nodes=\<*NODES*\>\]
:   Change the debug level of the slurmctld daemon for all active logging channels not originally configured off (quiet). *LEVEL* may be an integer value between zero and nine (using the same values as *SlurmctldDebug* in the *slurm.conf* file) or the name of the most detailed message type to be printed: \"quiet\", \"fatal\", \"error\", \"info\", \"verbose\", \"debug\", \"debug2\", \"debug3\", \"debug4\", or \"debug5\". This value is temporary, and will be overwritten whenever the daemon reads the slurm.conf configuration file. (Such as when the daemon is restarted or **scontrol reconfigure** is executed).

:   

    :   

        **nodes**=\<*NodeName*\>
        :   If set, the request to change debug level is sent to the slurmd processes on the nodes instead of to the slurmctld. A node range expression may be used for NodeName.

:   

**setdebugflags** {+\|-}\<*FLAG*\> \[{+\|-}\<*FLAG*\>\] \[nodes=\<*NODES*\>\]
:   Add or remove DebugFlags of the slurmctld daemon. See \"man slurm.conf\" for a list of supported DebugFlags.
    **NOTE**: Changing the value of some DebugFlags will have no effect without restarting the slurmctld daemon, which would set DebugFlags based upon the contents of the slurm.conf configuration file or the **SLURM_DEBUG_FLAGS** environment variable. The environment variable takes precedence over the setting in the slurm.conf.

:   

    :   

        **nodes**=\<*NodeName*\>
        :   The argument is optional and if used the request to change debug level is sent to slurmd instead of slurmctld. A node range expression may be used for NodeName.

:   

**show** \<*ENTITY*\>\[=\<*ID*\>\] or \<*ENTITY*\> \[\<*ID*\>\]
:   Display the state of the specified entity with the specified identification.

:   

    :   

        **aliases**
        :   Returns all *NodeName* values associated with a given *NodeHostname* (useful to get the list of virtual nodes associated with a real node in a configuration where multiple slurmd daemons execute on a single compute node).

        :   

        **assoc_mgr**
        :   Displays the current contents of the slurmctld\'s internal cache for users, associations and/or qos. The output can be filtered by different record types:

        :   

            :   

                **users**=\<*user1*\>\[\...,\<*userN*\>\]
                :   Limit the User Records displayed to those with the specified user name(s).
                    **NOTE**: If **PrivateData=users** is set in *slurm.conf*, unprivileged users will be limited to their own records. Privileged users will be able to see all records.

                :   

                **accounts**=\<*acct1*\>\[\...,\<*acctN*\>\]
                :   Limit the Association Records displayed to those with the specified account name(s).
                    **NOTE**: If **PrivateData=usage** is set in *slurm.conf*, unprivileged users will be limited to accounts where they are a member or coordinator. Privileged users will be able to see all records.

                :   

                **qos**=\<*qos1*\>\[\...,\<*qosN*\>\]
                :   Limit the QOS Records displayed to those with the specified QOS name(s).

                :   

                **flags**={users\|assoc\|qos}
                :   Specify the desired record type to be displayed. If no flags are specified, all record types are displayed.

        :   

        **bbstat**
        :   Displays output from the current burst buffer plugin\'s status tool (slurm_bb_get_status for lua or dwstat for datawarp). Options following **bbstat** are passed directly to the status tool by the slurmctld daemon and the response returned to the user. Equivalent to **dwstat**.

        :   

        **burstbuffer**
        :   Displays the current status of the BurstBuffer plugin.

        :   

        **config**
        :   Displays parameter names from the configuration files in mixed case (e.g. SlurmdPort=7003) while derived parameters names are in upper case only (e.g. SLURM_VERSION).

        :   

        **daemons**
        :   Reports which daemons should be running on this node.

        :   

        **dwstat**
        :   Displays output from the current burst buffer plugin\'s status tool (slurm_bb_get_status for lua or dwstat for datawarp). Options following **dwstat** are passed directly to the status tool by the slurmctld daemon and the response returned to the user. Equivalent to **bbstat**.

        :   

        **federation**
        :   The federation name that the controller is part of and the sibling clusters part of the federation will be listed.

        :   

        **hostlist**
        :   Takes a list of host names and prints the hostlist expression for them (the inverse of **hostnames**). **hostlist** can also take the absolute pathname of a file (beginning with the character \'/\') containing a list of hostnames, or a single \'-\' to have it read from stdin directly. Multiple node names may be specified using simple node range expressions (e.g. \"lx\[10-20\]\"). By default **hostlist** does not sort the node list or make it unique (e.g. tux2,tux1,tux2 = tux\[2,1-2\]). If you wanted a sorted list use **hostlistsorted** (e.g. tux2,tux1,tux2 = tux\[1-2,2\]).

        :   

        **hostlistsorted**
        :   Takes a list of host names and prints a sorted (but not unique) hostlist expression for them. See **hostlist**.

        :   

        **hostnames**
        :   Takes an optional hostlist expression as input and writes a list of individual host names to standard output (one per line). If no hostlist expression is supplied, the contents of the SLURM_JOB_NODELIST environment variable is used. For example \"tux\[1-3\]\" is mapped to \"tux1\",\"tux2\" and \"tux3\" (one hostname per line).

        :   

        **job**
        :   Displays statistics about all jobs by default. If an optional jobid is specified, details for just that job will be displayed. If the job does not specify socket-per-node, cores-per-socket or threads-per-core then it will display \'\*\' in the ReqS:C:T=\*:\*:\* field.

        :   

        **licenses**
        :   Displays statistics about all configured licenses (local and remote) by default. If an optional license name is specified, details for just that license will be displayed.

        **node**
        :   Displays statistics about all nodes by default. If an optional nodename is specified, details for just that node will be displayed.

        :   

        **partition**
        :   Displays statistics about all partitions by default. If an optional partition name is specified, details for just that partition will be displayed.

        :   

        **reservation**
        :   Displays statistics about all reservations by default. If an optional reservation name is specified, details for just that reservation will be displayed.

        :   

        **slurmd**
        :   Displays statistics for the slurmd running on the current node.

        :   

        **step**
        :   Displays statistics about all job steps by default. If an optional jobid is specified, details about steps for just that job will be displayed. If a jobid.stepid is specified, details for just that step will be displayed. If a container-id=\<*id*\> is specified, then the first matching step with the given container-id will be displayed.

        :   

        **topoconf**
        :   Displays running configurations of multiple topologies in the same format as *topology.yaml*.

        :   

        **topology** \[topology_name\] \[unit=NAME\] \[node=NAME\]

        :   Displays information about the selected topology layout. If no arguments are provided, the default topology will be returned.

            If a unit is specified, information about that unit will be shown. The **unit** keyword can be replaced with **switch** or **block** (e.g. block=b2).

            If one node name is specified, all units connected to that node (and their parent switches) will be shown. If more than one node name is specified, only units that connect to all named nodes will be shown.

:   

**shutdown** \<*OPTION*\>
:   Instruct Slurm daemons to save current state and terminate. By default, the Slurm controller (slurmctld) forwards the request all other daemons (slurmd daemon on each compute node). An *OPTION* of *slurmctld* or *controller* results in only the slurmctld daemon being shutdown and the slurmd daemons remaining active.

:   

**suspend** \<*job_list*\>
:   Suspend a running job. The job_list argument is a comma separated list of job IDs. Use the *resume* command to resume its execution. User processes must stop on receipt of SIGSTOP signal and resume upon receipt of SIGCONT for this operation to be effective. Not all architectures and configurations support job suspension. If a suspended job is requeued, it will be placed in a held state. The time a job is suspended will not count against a job\'s time limit. Only a privileged user or an account coordinator can suspend jobs.

:   

**takeover** \[\<*INDEX*\>\]
:   Instruct one of Slurm\'s backup controllers (slurmctld) to take over system control. By default the first backup controller (INDEX=1) requests control from the primary and waits for its termination. After that, it switches from backup mode to controller mode. If primary controller can not be contacted, it directly switches to controller mode. This can be used to speed up the Slurm controller fail-over mechanism when the primary node is down. This can be used to minimize disruption if the computer executing the primary Slurm controller is scheduled down.
    **NOTE**: The primary controller daemon will shut down to allow the secondary to take control. It will take control back at startup.

:   

**top** \<*job_list*\>
:   Move the specified job IDs to the top of the queue of jobs belonging to the identical user ID, partition name, account, and QOS. The job_list argument is a comma separated ordered list of job IDs. Any job not matching **all** of those fields will not be effected. Only jobs submitted to a single partition will be effected. This operation changes the order of jobs by adjusting job nice values. The net effect on that user\'s throughput will be negligible to slightly negative. This operation is disabled by default for unprivileged users, but may be enabled by including **SchedulerParameters=enable_user_top** in *slurm.conf*.

:   

**token** \[lifespan=\<*lifespan*\>\] \[username=\<*username*\>\]
:   Return an auth token which can be used to support JWT authentication if *AuthAltTypes=auth/jwt* has been enabled on the system. Supports two optional arguments. **lifespan=** may be used to specify the token\'s lifespan in seconds. **username** (only available to SlurmUser/root) may be used to request a token for a different username. Lifespan can be set to \"infinite\" to have a token that will not expire. Sites are suggested to use the smallest lifespan required and generate tokens more often instead of using longer lived tokens.

:   

**uhold** \<*job_list*\>
:   Similar to **hold**, but places a user-hold on the job even if the **uhold** command was issued by a privileged user. This allows the job owner or a coordinator to **release** the job without admin intervention.

:   

**update** \<*SPECIFICATION*\>
:   Update job, step, node, partition, or reservation configuration per the supplied specification. *SPECIFICATION* is in the same format as the Slurm configuration file and the output of the *show* command described above. It may be desirable to execute the *show* command (described above) on the specific entity you want to update, then use cut-and-paste tools to enter updated configuration values to the *update*. Note that while most configuration values can be changed using this command, not all can be changed using this mechanism. In particular, the hardware configuration of a node or the physical addition or removal of nodes from the cluster may only be accomplished through editing the Slurm configuration file and executing the *reconfigure* command (described above).

:   

**update** \<SuspendExc\*\>\[=\|+=\|-=\]\<*LIST*\>
:   Update *SuspendExcNodes*, *SuspendExcParts*, or *SuspendExcStates*. \<*LIST*\> is either a NodeList, list of partitions, or list of node states respectively. Use +=/-= to add/remove nodes, partitions, or states to/from the currently configured list. Use = to replace the current list. SuspendExcNodes does not support \"+=\"/\"-=\" when the \":\" option is used, however, direct assignment \"=\" is always supported. Consider using \"scontrol show config \| grep SuspendExc\" to see current state of these settings.

:   

**version**
:   Display the version number of scontrol being executed.

:   

**wait_job** \<*job_id*\>
:   Wait until a job and all of its nodes are ready for use or the job has entered some termination state. This option is particularly useful in the Slurm Prolog or in the batch script itself if nodes are powered down and restarted automatically as needed.
    **NOTE**: Don\'t use scontrol wait_job in PrologSlurmctld or Prolog with PrologFlags=Alloc as this will result in a deadlock.

:   **NOTE**: When using **wait_job** for an array job, use the **SLURM_JOB_ID** environment variable to reference the job rather than the **SLURM_ARRAY_JOB_ID** variable.

**write batch_script** \<*job_id*\> \[\<*optional_filename*\>\]
:   Write the batch script for a given job_id to a file or to stdout. The file will default to *slurm-\<job_id\>.sh* if the optional filename argument is not given. The script will be written to stdout if - is given instead of a filename. The batch script can only be retrieved by a privileged user, or by the owner of the job.

:   

**write config** \<*optional_filename*\>
:   Write the current configuration to a file with the naming convention of \"slurm.conf.\<datetime\>\" in the same directory as the original slurm.conf file. If a filename is given that file location with a .\<datetime\> suffix is created.

:   

[ ]{#lbAG}

## INTERACTIVE COMMANDS

**NOTE**: All commands listed below can be used in the interactive mode, but *NOT* on the initial command line.

**all**
:   Show all partitions, their jobs and jobs steps. This causes information to be displayed about partitions that are configured as hidden and partitions that are unavailable to user\'s group.

:   

**cluster** \<*CLUSTER_NAME*\>
:   The cluster to issue commands to. Only one cluster name may be specified.

:   

**details**
:   Causes the *show* command to provide additional details where available. Job information will include CPUs and NUMA memory allocated on each node. Note that on computers with hyperthreading enabled and Slurm configured to allocate cores, each listed CPU represents one physical core. Each hyperthread on that core can be allocated a separate task, so a job\'s CPU count and task count may differ. See the **\--cpu-bind** and **\--mem-bind** option descriptions in srun man pages for more information. The **details** option is currently only supported for the *show job* command.

:   

**exit**
:   Terminate scontrol interactive session.

:   

**hide**
:   Do not display partition, job or jobs step information for partitions that are configured as hidden or partitions that are unavailable to the user\'s group. This is the default behavior.

:   

**oneliner**
:   Print information one line per record.

:   

**quiet**
:   Print no warning or informational messages, only fatal error messages.

:   

**quit**
:   Terminate the execution of scontrol.

:   

**verbose**
:   Print detailed event logging. This includes time-stamps on data structures, record counts, etc.

:   

**!!**
:   Repeat the last command executed.

:   

[ ]{#lbAH}

## JOBS - SPECIFICATIONS FOR UPDATE COMMAND

An unprivileged user may modify their own jobs subject to certain restrictions, as well as jobs and steps in any accounts where they have Coordinator permissions. Most of these fields can only be updated on pending jobs. Some may be updated on running or suspended jobs. A privileged user can modify any jobs without policy restrictions. For instance, if an administrator changes the QOS on a pending job, certain limits such as the TimeLimit will not be changed automatically as changes made by privileged users are allowed to violate these restrictions.

**JobName**=\<*name*\>
:   Identify the name of jobs to be modified or set the job\'s name to the specified value. When used to identify jobs to be modified, all jobs belonging to all users are modified unless the *UserID* option is used to identify a specific user. Either *JobId* or *JobName* is required.

:   

**Account**=\<*account*\>
:   Account name to be changed for this job\'s resource use. Value may be cleared with blank data value, \"Account=\".

:   

**AdminComment**=\<*spec*\>
:   Arbitrary descriptive string. Can only be set by a Slurm administrator.

:   

**ArrayTaskThrottle**=\<*count*\>
:   Specify the maximum number of tasks in a job array that can execute at the same time. Set the count to zero in order to eliminate any limit. The task throttle count for a job array is reported as part of its ArrayTaskId field, preceded with a percent sign. For example \"ArrayTaskId=1-10%2\" indicates the maximum number of running tasks is limited to 2.

:   

**BurstBuffer**=\<*spec*\>
:   Burst buffer specification to be changed for this job\'s resource use. Value may be cleared with blank data value, \"BurstBuffer=\". Format is burst buffer plugin specific. Only a privileged user can change this parameter.

:   

**Clusters**=\<*spec*\>
:   Specifies the clusters that the federated job can run on.

:   

**ClusterFeatures**=\<*spec*\>
:   Specifies features that a federated cluster must have to have a sibling job submitted to it. Slurm will attempt to submit a sibling job to a cluster if it has at least one of the specified features.

:   

**Comment**=\<*spec*\>
:   Arbitrary descriptive string.

:   

**Contiguous**={yes\|no}
:   Set the job\'s requirement for contiguous (consecutive) nodes to be allocated. Possible values are \"YES\" and \"NO\". Only a privileged user can change this parameter to \"YES\".

:   

**CoreSpec**=\<*count*\>
:   Number of cores to reserve per node for system use. The job will be charged for these cores, but be unable to use them. Will be reported as \"\*\" if not constrained. Only a privileged user can change this parameter.

:   

**CPUsPerTask**=\<*count*\>
:   Change the CPUsPerTask job\'s value.

:   

**Deadline**=\<*time_spec*\>

:   Remove the job if no ending is possible before this deadline (start \> (deadline - time\[-min\])). Note that if neither **DefaultTime** nor **MaxTime** are configured on the partition the job is in, the job will need to specify some form of time limit (TimeMin/TimeLimit) if a deadline is to be used. The specified deadline must be later than the current time. Only a privileged user can change this parameter.

    Valid time formats are:\
    HH:MM\[:SS\] \[AM\|PM\]\
    MMDD\[YY\] or MM/DD\[/YY\] or MM.DD\[.YY\]\
    MM/DD\[/YY\]-HH:MM\[:SS\]\
    YYYY-MM-DD\[THH:MM\[:SS\]\]\
    now\[+*count*\[seconds(default)\|minutes\|hours\|days\|weeks\]\]\
    midnight, elevenses (11 AM), noon, fika (3 PM), teatime (4 PM), or tomorrow

    One or more time strings may be specified (e.g., \'tomorrow18:00\'). If there is a conflict between them, the last one will silently take precedence.

:   

**DelayBoot**=\<*time_spec*\>
:   Change the time to decide whether to reboot nodes in order to satisfy job\'s feature specification if the job has been eligible to run for less than this time period. See salloc/sbatch man pages option \--delay-boot.

:   

**Dependency**=\<*dependency_list*\>
:   Defer job\'s initiation until specified job dependency specification is satisfied. Once a dependency is satisfied, it is removed from the job. Cancel dependency with an empty dependency_list (e.g. \"Dependency=\"). \<*dependency_list*\> is of the form \<*type:job_id\[:job_id\]\[,type:job_id\[:job_id\]\]*\>. Many jobs can share the same dependency and these jobs may even belong to different users.

:   

    :   

        **after:job_id\[:jobid\...\]**
        :   This job can begin execution after the specified jobs have begun execution or been canceled.

        :   

        **afterany:job_id\[:jobid\...\]**
        :   This job can begin execution after the specified jobs have terminated.

        :   

        **afternotok:job_id\[:jobid\...\]**
        :   This job can begin execution after the specified jobs have terminated in some failed state (non-zero exit code, node failure, timed out, etc). This dependency must be added while the specified job is still active or within **MinJobAge** seconds after the specified job has ended.

        :   

        **afterok:job_id\[:jobid\...\]**
        :   This job can begin execution after the specified jobs have successfully executed (ran to completion with an exit code of zero). This dependency must be added while the specified job is still active or within **MinJobAge** seconds after the specified job has ended.

        :   

        **singleton**
        :   This job can begin execution after any previously launched jobs sharing the same job name and user have terminated. In other words, only one job by that name and owned by that user can be running or suspended at any point in time.

:   

**EligibleTime**=\<*time_spec*\>
:   See *StartTime*.

:   

**EndTime**=\<*time_spec*\>
:   Set the job\'s expected end time. The job\'s **TimeLimit** will be automatically recalculated to reflect the change. When the job ends, this field will be updated with the actual end time. Only a privileged user can extend a job\'s EndTime.

:   

**ExcNodeList**=\<*nodes*\>
:   Set the job\'s list of excluded node. Multiple node names may be specified using simple node range expressions (e.g. \"lx\[10-20\]\"). Value may be cleared with blank data value, \"ExcNodeList=\".

:   

**Extra**=\<*spec*\>
:   An arbitrary string enclosed in single or double quotes if using spaces or some special characters. See \<[https://slurm.schedmd.com/extra_constraints.html](extra_constraints.md)\> for more details.

:   

**Features**=\<*features*\>
:   Set the job\'s required node features. The list of features may include multiple feature names separated by ampersand (AND) and/or vertical bar (OR) operators. For example: **Features=\"opteron&video\"** or **Features=\"fast\|faster\"**. In the first example, only nodes having both the feature \"opteron\" AND the feature \"video\" will be used. There is no mechanism to specify that you want one node with feature \"opteron\" and another node with feature \"video\" in case no node has both features. If only one of a set of possible options should be used for all allocated nodes, then use the OR operator and enclose the options within square brackets. For example: \"**Features=\[rack1\|rack2\|rack3\|rack4\]\"** might be used to specify that all nodes must be allocated on a single rack of the cluster, but any of those four racks can be used. A request can also specify the number of nodes needed with some feature by appending an asterisk and count after the feature name. For example \"**Features=graphics\*4\"** indicates that at least four allocated nodes must have the feature \"graphics.\" Parenthesis are also supported for features to be ANDed together. For example \"**Features=\[(knl&a2a&flat)\*4&haswell\*2\]\"** indicates the resource allocation should include 4 nodes with ALL of the features \"knl\", \"a2a\", and \"flat\" plus 2 nodes with the feature \"haswell\". Constraints with node counts may only be combined with AND operators. Value may be cleared with blank data value, for example \"Features=\".

:   

**Gres**=\<*list*\>
:   Specifies a comma-delimited list of generic consumable resources requested per node. The format of each entry on the list is \"name\[:count\[\*cpu\]\]\". The name is that of the consumable resource. The count is the number of those resources with a default value of 1. The specified resources will be allocated to the job on each node allocated unless \"\*cpu\" is appended, in which case the resources will be allocated on a per cpu basis. The available generic consumable resources is configurable in slurm.conf. A list of available generic consumable resources will be printed and the command will exit if the option argument is \"help\". Examples of use include \"Gres=gpus:2\*cpu,disk=40G\" and \"Gres=help\".

:   

**JobId**=\<*job_list*\>
:   Identify the job(s) to be updated. The job_list may be a comma separated list of job IDs. Either *JobId* or *JobName* is required. If the *JobId* is equal to the *ArrayJobID* then the update will affect all of the individual jobs of the array. In that case, to update the specific individual job, the form \<*ArrayJobID*\>\_\<*ArrayTaskId*\> must be used.

:   

**Licenses**=\<*name*\>
:   Specification of licenses (or other resources available on all nodes of the cluster) as described in salloc/sbatch/srun man pages.
    An unprivileged user can modify the licenses of pending jobs. A privileged user can modify the licenses of pending or running jobs.

:   

**MailType**=\<*types*\>
:   Set the mail event types. Valid type values are NONE, BEGIN, END, FAIL, REQUEUE, ALL (equivalent to BEGIN, END, FAIL, REQUEUE, and STAGE_OUT), STAGE_OUT (burst buffer stage out and teardown completed), TIME_LIMIT, TIME_LIMIT_90 (reached 90 percent of time limit), TIME_LIMIT_80 (reached 80 percent of time limit), TIME_LIMIT_50 (reached 50 percent of time limit) and ARRAY_TASKS (send emails for each array task). Multiple type values may be specified in a comma separated list. Unless the ARRAY_TASKS option is specified, mail notifications on job BEGIN, END and FAIL apply to a job array as a whole rather than generating individual email messages for each task in the job array.

:   

**MailUser**=\<*name*\>
:   Set the user to receive email notification of state changes. A blank string will set the mail user to the default which is the submitting user.

:   

**MCSLabel**=\<*name*\>
:   Set the MCS label for the job, which will take effect only if a MCS plugin is loaded in slurmctld.

:   

**MinCPUsNode**=\<*count*\>
:   Set the job\'s minimum number of CPUs per node to the specified value.

:   

**MinMemoryCPU**=\<*megabytes*\>
:   Set the job\'s minimum real memory required per allocated CPU to the specified value. Either *MinMemoryCPU* or *MinMemoryNode* may be set, but not both.

:   

**MinMemoryNode**=\<*megabytes*\>
:   Set the job\'s minimum real memory required per node to the specified value. Either *MinMemoryCPU* or *MinMemoryNode* may be set, but not both.

:   

**MinTmpDiskNode**=\<*megabytes*\>
:   Set the job\'s minimum temporary disk space required per node to the specified value.

:   

**Name**\[=\<*name*\>\]
:   See JobName.

:   

**Nice**\[=\<*adjustment*\>\]
:   Update the job with an adjusted scheduling priority within Slurm. With no adjustment value the scheduling priority is decreased by 100. A negative nice value increases the priority, otherwise decreases it. The adjustment range is +/- 2147483645. Only a privileged user can specify a negative adjustment.

:   

**NodeList**=\<*nodes*\>
:   Change the nodes allocated to a running job to shrink its size. The specified list of nodes must be a subset of the nodes currently allocated to the job. Multiple node names may be specified using simple node range expressions (e.g. \"lx\[10-20\]\"). After a job\'s allocation is reduced, subsequent **srun** commands must explicitly specify node and task counts which are valid for the new allocation.
    **NOTE**: The allocated nodes of jobs with arbitrary distribution can not be updated.

:   

**NumCPUs**=\<*min_count*\>\[-\<*max_count*\>\]
:   Set the job\'s minimum and optionally maximum count of CPUs to be allocated.

:   

**NumNodes**=\<*min_count*\>\[-\<*max_count*\>\]
:   Set the job\'s minimum and optionally maximum count of nodes to be allocated. If the job is already running, use this to specify a node count less than currently allocated and resources previously allocated to the job will be relinquished. After a job\'s allocation is reduced, subsequent **srun** commands must explicitly specify node and task counts which are valid for the new allocation. Also see the *NodeList* parameter above. This is the same as ReqNodes.
    **NOTE**: The node count of jobs with arbitrary distribution can not be updated.

:   

**NumTasks**=\<*count*\>
:   Set the job\'s count of requested tasks to the specified value. The number of tasks started in a specific step inside the allocation may differ from this value, for instance when a different number of tasks is requested on step creation. This is the same as ReqProcs.

:   

**OverSubscribe**={yes\|no}
:   Set the job\'s ability to share compute resources (i.e. individual CPUs) with other jobs. Possible values are \"YES\" and \"NO\". This option can only be changed for pending jobs. Only a privileged user can change this parameter.

:   

**Partition**=\<*name*\>
:   Set the job\'s partition to the specified value.

:   

**Prefer**=\<*features*\>
:   Set the job\'s preferred node features. This list is only preferred, not required like *Features* is. This list will override what is requested in Features. See *Features* option above.

:   

**Priority**=\<*number*\>

:   Set the job\'s priority to the specified value. Note that a job priority of zero prevents the job from ever being scheduled. By setting a job\'s priority to zero it is held. Set the priority to a non-zero value to permit it to run and clear any previously set nice value.

    When a privileged user explicitly sets a job\'s priority, it is fixed and the priority plugin will no longer modify it. In order to restore the priority/multifactor plugin\'s ability to manage a job\'s priority, hold and then release the job.

    An unprivileged user can only decrease job priority, and the priority plugin may still manage the value. Consider increasing **Nice** instead.

:   

**QOS**=\<*name*\>
:   Set the job\'s QOS (Quality Of Service) to the specified value, or comma separated list of QOS. If requesting a list it will be ordered based on the priority of the QOS given with the first being the highest priority. Value may be cleared with blank data value, \"QOS=\".

:   

**Reboot**={yes\|no}
:   Set the job\'s flag that specifies whether to force the allocated nodes to reboot before starting the job. This is only supported with some system configurations and therefore it could be silently ignored. Only a Slurm administrator can change this parameter.

:   

**ReqCores**=\<*count*\>
:   Change the job\'s requested Cores count.

:   

**ReqNodeList**=\<*nodes*\>
:   Set the job\'s list of required node. Multiple node names may be specified using simple node range expressions (e.g. \"lx\[10-20\]\"). Value may be cleared with blank data value, \"ReqNodeList=\".

:   

**ReqNodes**=\<*min_count*\>\[-\<*max_count*\>\]
:   See NumNodes.

:   

**ReqProcs**=\<*count*\>
:   See NumTasks.

:   

**ReqSockets**=\<*count*\>
:   Change the job\'s requested socket count.

:   

**ReqThreads**=\<*count*\>
:   Change the job\'s requested threads count.

:   

**Requeue**={0\|1}
:   Stipulates whether a job should be requeued after a node failure: 0 for no, 1 for yes.

:   

**ReservationName**=\<*name*\>
:   Set the job\'s reservation to the specified value. Value may be cleared with blank data value, \"ReservationName=\".

:   

**ResetAccrueTime**
:   Set the job\'s accrue time value to \'now\' meaning it will lose any time previously accrued for priority. Helpful if you have a large queue of jobs already in the queue and want to start limiting how many jobs can accrue time without waiting for the queue to flush out.

:   

**SiteFactor**=\<*account*\>
:   Specify the job\'s site priority factor in the range of +/-2147483645. Only a privileged user can change this parameter.

:   

**StdErr**=\<*filepath*\>
:   Set the batch job\'s stderr file path. Value may be reset to job default with blank data value, \"StdErr=\".
    **NOTE**: By default, StdErr will be merged into StdOut.

:   

**StdIn**=\<*filepath*\>
:   Set the batch job\'s stdin file path. Value may be reset to job default with blank data value, \"StdIn=\".
    **NOTE**: By default, StdIn will be \'/dev/null\'.

:   

**StdOut**=\<*filepath*\>
:   Set the batch job\'s stdout file path. Value may be reset to job default with blank data value, \"StdOut=\".
    **NOTE**: By default, StdOut will be based on the *JobId*.

:   

**Shared**={yes\|no}
:   See *OverSubscribe* option above.

:   

**StartTime**=\<*time_spec*\>
:   Set the job\'s earliest initiation time. It accepts times of the form *HH:MM:SS* to run a job at a specific time of day (seconds are optional). (If that time is already past, the next day is assumed.) You may also specify *midnight*, *noon*, *elevenses* (11 AM), *fika* (3 PM) or *teatime* (4 PM) and you can have a time-of-day suffixed with *AM* or *PM* for running in the morning or the evening. You can also say what day the job will be run, by specifying a date of the form *MMDDYY* or *MM/DD/YY* or *MM.DD.YY*, or a date and time as *YYYY-MM-DD\[THH:MM\[:SS\]\]*. You can also give times like *now + count time-units*, where the time-units can be *seconds* (default), *minutes*, *hours*, *days*, or *weeks* and you can tell Slurm to run the job today with the keyword *today* and to run the job tomorrow with the keyword *tomorrow*.

:   

    :   Notes on date/time specifications:\
         - although the \'seconds\' field of the HH:MM:SS time specification is allowed by the code, note that the poll time of the Slurm scheduler is not precise enough to guarantee dispatch of the job on the exact second. The job will be eligible to start on the next poll following the specified time. The exact poll interval depends on the Slurm scheduler (e.g., 60 seconds with the default sched/builtin).\
         - if no time (HH:MM:SS) is specified, the default is (00:00:00).\
         - if a date is specified without a year (e.g., MM/DD) then the current year is assumed, unless the combination of MM/DD and HH:MM:SS has already passed for that year, in which case the next year is used.

:   

**Switches**=\<*count*\>\[@\<*max-time-to-wait*\>\]
:   When a tree topology is used, this defines the maximum count of switches desired for the job allocation. If Slurm finds an allocation containing more switches than the count specified, the job remain pending until it either finds an allocation with desired switch count or the time limit expires. By default there is no switch count limit and no time limit delay. Set the count to zero in order to clean any previously set count (disabling the limit). The job\'s maximum time delay may be limited by setting **SchedulerParameters=max_switch_wait=#** in *slurm.conf*. Also see *wait-for-switch*.

:   

**TasksPerNode**=\<*count*\>
:   Change the job\'s requested TasksPerNode. Only a privileged user can change this parameter.

:   

**ThreadSpec**=\<*count*\>
:   Number of threads to reserve per node for system use. The job will be charged for these threads, but be unable to use them. Will be reported as \"\*\" if not constrained.

:   

**TimeLimit**=\<*time*\>
:   The job\'s time limit. Output format is \[days-\]hours:minutes:seconds or \"UNLIMITED\". Input format (for **update** command) set is minutes, minutes:seconds, hours:minutes:seconds, days-hours, days-hours:minutes or days-hours:minutes:seconds. Time resolution is one minute and second values are rounded up to the next minute. If changing the time limit of a job, either specify a new time limit value or precede the time and equal sign with a \"+\" or \"-\" to increment or decrement the current time limit (e.g. \"TimeLimit+=30\"). In order to increment or decrement the current time limit, the *JobId* specification must precede the *TimeLimit* specification. Note that incrementing or decrementing the time limit for a job array is only allowed before the job array has been split into more than one job record. Only a privileged user can increase a running or suspended job\'s TimeLimit.

:   

**TimeMin**=\<*timespec*\>
:   Change TimeMin value which specifies the minimum time limit minutes of the job.

:   

**UserID**=\<*UID* or *name*\>
:   Used with the *JobName* option to identify jobs to be modified. Either a user name or numeric ID (UID), may be specified.

:   

**wait-for-switch**=\<*seconds*\>
:   Change max time to wait for a switch \<seconds\> secs.

:   

**WCKey**=\<*key*\>
:   Set the job\'s workload characterization key to the specified value.

:   

**WorkDir**=\<*directory_name*\>
:   Set the job\'s working directory to the specified value. Note that this may only be set for jobs in the PENDING state, and that jobs may fail to launch if they rely on relative paths to the originally submitted WorkDir.

:   

[ ]{#lbAI}

## JOBS - SPECIFICATIONS FOR SHOW COMMAND

The \"show\" command, when used with the \"job\" or \"job \<jobid\>\" entity displays detailed information about a job or jobs. Much of this information may be modified using the \"update job\" command as described above. However, the following fields displayed by the show job command are read-only and cannot be modified:

**AllocNode:Sid**
:   Local node and system id making the resource allocation.

:   

**BatchFlag**
:   Jobs submitted using the sbatch command have BatchFlag set to 1. The BatchFlag will be incremented past 1 if the job is requeued due to a failure. Jobs submitted using other commands have BatchFlag set to 0 and will not be incremented.

:   

**ExitCode**=\<*exit*\>:\<*sig*\>
:   Exit status reported for the job by the wait() function. The first number is the exit code, typically as set by the exit() function. The second number of the signal that caused the process to terminate if it was terminated by a signal.

:   

**GroupId**
:   The group under which the job was submitted.

:   

**JobState**
:   The current state of the job.

:   

**NodeListIndices**
:   The NodeIndices expose the internal indices into the node table associated with the node(s) allocated to the job.

:   

**NtasksPerN:B:S:C**=\<*tasks_per_node*\>:\<*tasks_per_baseboard*\>:\<*tasks_per_socket*\>:\<*tasks_per_core*\>
:   Specifies the number of tasks to be started per hardware component (node, baseboard, socket and core). Unconstrained values may be shown as \"0\" or \"\*\".

:   

**PreemptEligibleTime**
:   Time the job becomes eligible for preemption. Modified by PreemptExemptTime, either from the global option in slurm.conf or the job QOS. This is hidden if the job has not started or if PreemptMode=OFF.

:   

**PreemptTime**
:   Time at which job was signaled that it was selected for preemption. This value is only meaningful for *PreemptMode=CANCEL* and *PreemptMode=REQUEUE* and for jobs in a partition or QOS that has a GraceTime value designated. This is hidden if the job has not started or if *PreemptMode=OFF*.

:   

**PreSusTime**
:   Time the job ran prior to last suspend.

:   

**Reason**
:   The reason a job has not been started by the scheduler: e.g., waiting for \"Resources\". Details of job reason codes are found on this page: \<[https://slurm.schedmd.com/job_reason_codes.html](job_reason_codes.md)\>

:   

**ReqB:S:C:T**=\<*baseboard_count*\>:\<*socket_per_baseboard_count*\>:\<*core_per_socket_count*\>:\<*thread_per_core_count*\>
:   Specifies the count of various hardware components requested by the job. Unconstrained values may be shown as \"0\" or \"\*\".

:   

**SecsPreSuspend**=\<*seconds*\>
:   If the job is suspended, this is the run time accumulated by the job (in seconds) prior to being suspended.

:   

**SegmentSize**=\<*size*\>
:   Requested segment size for the job.

:   

**Socks/Node**=\<count\>
:   Count of desired sockets per node

:   

**SubmitTime**
:   The time and date stamp (in localtime) the job was submitted. The format of the output is identical to that of the EndTime field.
    **NOTE**: If a job is requeued, the submit time is reset. To obtain the original submit time it is necessary to use the \"sacct -j \<job_id\[.\<step_id\>\]\" command also designating the -D or \--duplicate option to display all duplicate entries for a job.

:   

**SuspendTime**
:   Time the job was last suspended or resumed.
    NOTE on information displayed for various job states: When you submit a request for the \"show job\" function the scontrol process makes an RPC request call to slurmctld with a REQUEST_JOB_INFO message type. If the state of the job is PENDING, then it returns some detail information such as: min_nodes, min_procs, cpus_per_task, etc. If the state is other than PENDING the code assumes that it is in a further state such as RUNNING, COMPLETE, etc. In these cases the code explicitly returns zero for these values. These values are meaningless once the job resources have been allocated and the job has started.

:   

[ ]{#lbAJ}

## STEPS - SPECIFICATIONS FOR UPDATE COMMAND

**StepId**=\<*job_id*\>\[.\<*step_id*\>\]
:   Identify the step to be updated. If the job_id is given, but no step_id is specified then all steps of the identified job will be modified. This specification is required.

:   

**TimeLimit**=\<*time*\>
:   The job\'s time limit. Output format is \[days-\]hours:minutes:seconds or \"UNLIMITED\". Input format (for **update** command) set is minutes, minutes:seconds, hours:minutes:seconds, days-hours, days-hours:minutes or days-hours:minutes:seconds. Time resolution is one minute and second values are rounded up to the next minute. If changing the time limit of a step, either specify a new time limit value or precede the time with a \"+\" or \"-\" to increment or decrement the current time limit (e.g. \"TimeLimit=+30\"). In order to increment or decrement the current time limit, the *StepId* specification must precede the *TimeLimit* specification.

:   

[ ]{#lbAK}

## NODES - SPECIFICATIONS FOR CREATE COMMAND

Provide the same NodeName configuration as found in the slurm.conf. See slurm.conf man page for details. Only State=CLOUD and State=FUTURE nodes are allowed.

[ ]{#lbAL}

## NODES - SPECIFICATIONS FOR UPDATE COMMAND

**NodeName**=\<*name*\>
:   Identify the node(s) to be updated. Multiple node names may be specified using simple node range expressions (e.g. \"lx\[10-20\]\"). Nodesets can also be specified by themselves or mixed with node range expressions, using a comma as a list separator. If the keyword \"ALL\" is specified alone, then the update will be attempted against all the nodes in the local cluster. This specification is required.

:   

**ActiveFeatures**=\<*features*\>
:   Identify the feature(s) currently active on the specified node. Any previously active feature specification will be overwritten with the new value. Also see *AvailableFeatures*. Typically *ActiveFeatures* will be identical to *AvailableFeatures*; however *ActiveFeatures* may be configured as a subset of the *AvailableFeatures*. For example, a node may be booted in multiple configurations. In that case, all possible configurations may be identified as *AvailableFeatures*, while *ActiveFeatures* would identify the current node configuration. When updating the ActiveFeatures with scontrol, the change is only made in slurmctld. When using a node_features plugin the state/features of the node must be updated on the node such that a new node start will report the updated state/features.

:   

**AvailableFeatures**=\<*features*\>
:   Identify the feature(s) available on the specified node. Any previously defined available feature specification will be overwritten with the new value. AvailableFeatures assigned via **scontrol** will only persist across the restart of the slurmctld daemon with the *-R* option and state files preserved or slurmctld\'s receipt of a SIGHUP. Update slurm.conf with any changes meant to be persistent across normal restarts of slurmctld or the execution of **scontrol reconfig**.
    **NOTE**: Available features being removed via **scontrol** must not be active (i.e. remove them from *ActiveFeatures* first).

:   

**CertToken**=\<*token*\>
:   Unique token string used by certmgr plugin interface to validate node identity.

:   

**Comment**=\<*comment*\>
:   Arbitrary descriptive string. Use quotes to enclose a comment having more than one word

:   

**CpuBind**=\<*node*\>
:   Specify the task binding mode to be used by default for this node. Supported options include: \"none\", \"socket\", \"ldom\" (NUMA), \"core\", \"thread\" and \"off\" (remove previous binding mode).

:   

**Extra**=\<*comment*\>
:   Arbitrary string on the node. Use quotes to enclose a string having more than one word. See \<[https://slurm.schedmd.com/extra_constraints.html](extra_constraints.md)\> for more details.

:   

**Gres**=\<*gres*\>
:   Identify generic resources to be associated with the specified node. Any previously defined generic resources will be overwritten with the new value. Specifications for multiple generic resources should be comma separated. Each resource specification consists of a name followed by an optional colon with a numeric value (default value is one) (e.g. \"Gres=bandwidth:10000\"). Modification of GRES count associated with specific files (e.g. GPUs) is not allowed other than to set their count on a node to zero. In order to change the GRES count to another value, modify your slurm.conf and gres.conf files and restart daemons. If GRES are associated with specific sockets, that information will be reported For example if all 4 GPUs on a node are all associated with socket zero, then \"Gres=gpu:4(S:0)\". If associated with sockets 0 and 1 then \"Gres=gpu:4(S:0-1)\". The information of which specific GPUs are associated with specific GPUs is not reported, but only available by parsing the gres.conf file. Generic resources assigned via **scontrol** will only persist across the restart of the slurmctld daemon with the *-R* option and state files preserved or slurmctld\'s receipt of a SIGHUP. Update slurm.conf with any changes meant to be persistent across normal restarts of slurmctld or the execution of **scontrol reconfig**.

:   

**InstanceId**=\<*instance_id*\>
:   Cloud instance ID.

:   

**InstanceType**=\<*instance_type*\>
:   Cloud instance type.

:   

**NodeAddr**=\<*node address*\>
:   Name that a node should be referred to in establishing a communications path. This name will be used as an argument to the getaddrinfo() function for identification. If a node range expression is used to designate multiple nodes, they must exactly match the entries in the *NodeName* (e.g. \"NodeName=lx\[0-7\] NodeAddr=elx\[0-7\]\"). *NodeAddr* may also contain IP addresses.

:   

**NodeHostname**=\<*node hostname*\>
:   Typically this would be the string that \"/bin/hostname -s\" returns. It may also be the fully qualified domain name as returned by \"/bin/hostname -f\" (e.g. \"foo1.bar.com\"), or any valid domain name associated with the host through the host database (/etc/hosts) or DNS, depending on the resolver settings. Note that if the short form of the hostname is not used, it may prevent use of hostlist expressions (the numeric portion in brackets must be at the end of the string). A node range expression can be used to specify a set of nodes. If an expression is used, the number of nodes identified by *NodeHostname* must be identical to the number of nodes identified by *NodeName*.

:   

**Reason**=\<*reason*\>
:   Identify the reason the node is in a \"DOWN\", \"DRAINED\", \"DRAINING\", \"FAILING\" or \"FAIL\" state. Use quotes to enclose a reason having more than one word.

:   

**ResumeAfter**=\<*seconds*\>
:   Schedule a node state resume after this amount of seconds, when its state is updated to \"DOWN\" or \"DRAIN\". Upon state resume, the node\'s state will be changed from **DRAIN**, **DRAINING**, **DOWN** or **REBOOT** to **IDLE** and **NoResp**. slurmctld will then attempt to contact slurmd to request that the node register itself.
    **NOTE**: A value of -1 will unschedule the node state resume.

:   

**State**=\<*state*\>
:   Assign one of the following states/actions to the node(s) specified by the update command.

:   

    :   

        **CANCEL_REBOOT**
        :   Cancels a pending reboot on the node (same as *scontrol cancel_reboot \<node\>*).

        :   

        **DOWN**
        :   Stop all running and suspended jobs and make the node unavailable for new jobs.

        :   

        **DRAIN**
        :   Indicates that no new jobs may be started on this node. Existing jobs are allowed to run to completion, leaving the node in a **DRAINED** state once all the jobs have completed.

        :   

        **FAIL**
        :   Similar to **DRAIN** except that some applications will seek to relinquish those nodes before the job completes.

        :   

        **FUTURE**
        :   Indicates the node is not fully configured, but is expected to be available at some point in the future.

        :   

        **IDLE**
        :   Will clear **DOWN**, **DRAIN** and **FAIL** states. Will set the state to **IDLE** and **NoResp**. slurmctld will then attempt to contact slurmd to request that the node register itself. Once registered, the node state will then remove the **NoResp** flag and will resume normal operations.

        :   

        **NoResp**
        :   This will set the \"Not Responding\" flag for a node without changing its underlying state.

        :   

        **RESUME**
        :   Not an actual node state, but will change a node state from **DRAIN**, **DRAINING**, **DOWN** or **REBOOT** to **IDLE** and **NoResp**. slurmctld will then attempt to contact slurmd to request that the node register itself. Once registered, the node state will then remove the **NoResp** flag and will resume normal operations. It will also clear the **POWERING_DOWN** state of a node and make it eligible to be allocated.

        :   

        **UNDRAIN**
        :   Clears the node from being drained (like **RESUME**), but will not change the node\'s base state (e.g. **DOWN**). **UNDRAIN** requires a valid node registration before new jobs can be scheduled on the node. Setting a node **DOWN** will cause all running and suspended jobs on that node to be terminated.

:   While all of the above states are valid, some of them are not valid new node states given their prior state.

    **NOTE**: The scontrol command should not be used to change node state on Cray systems. Use Cray tools such as *xtprocadmin* instead.

:   

**Topology**=\<*topology_name*\>:\<*topology_unit*\>\[,\<*topology_name*\>:\<*topology_unit*\>,\...\]
:   Where \<*topology_unit*\> is the block name or the name of a leaf switch. Intermediate switch names \-- \':\' delimited \-- can be provided and will be created if needed (e.g. Topology=topo-tree:sw_root:s1:s2). This configuration overrides node topology affiliation settings from *topology.conf* and *topology.yaml*.

:   

**Weight**=\<*weight*\>
:   Identify weight to be associated with specified nodes. This allows dynamic changes to weight associated with nodes, which will be used for the subsequent node allocation decisions. Weight assigned via **scontrol** will only persist across the restart of the slurmctld daemon with the *-R* option and state files preserved or slurmctld\'s receipt of a SIGHUP. Update slurm.conf with any changes meant to be persistent across normal restarts of slurmctld or the execution of **scontrol reconfig**.

:   

[ ]{#lbAM}

## NODES - SPECIFICATIONS FOR SHOW COMMAND

**AllocMem**
:   The total memory, in MB, currently allocated by jobs on the node.

:   

**CPULoad**
:   CPU load of a node as reported by the OS.

:   

**CPUSpecList**
:   The list of Slurm abstract CPU IDs on this node reserved for exclusive use by the Slurm compute node daemons (slurmd, slurmstepd).

:   

**FreeMem**
:   The total memory, in MB, currently free on the node as reported by the OS.

:   

**LastBusyTime**
:   The last time the node was busy (i.e. last time the node had jobs on it). This time is used in PowerSave to determine when to suspend nodes (e.g. now - LastBusy \> SuspendTime).

:   

**MemSpecLimit**
:   The combined memory limit, in megabytes, on this node for the Slurm compute node daemons (slurmd, slurmstepd).

:   

**RealMemory**
:   The total memory, in MB, on the node.

:   

**State**
:   Identify the state(s) assigned to the node with \'+\' delimited state flags.
    States:

:   

    :   

        **ALLOCATED**
        :   Indicates that the node has all CPUs allocated to job(s) running on the node.

        :   

        **DOWN**
        :   The node does not have any running jobs and is unavailable for new work.

        :   

        **ERROR**
        :   The node is in an error state. Consult the logs for more information about what caused this state.

        :   

        **FUTURE**
        :   The node is currently not fully configured, but expected to be available at some point in the indefinite future for use.

        :   

        **IDLE**
        :   Indicates that the node is available for work but does not currently have any jobs assigned to it.

        :   

        **MIXED**
        :   Indicates that the node is in multiple states. For instance if only part of the node is **ALLOCATED** and the rest of the node is **IDLE** the state will be **MIXED**.

        :   

        **UNKNOWN**
        :   The node has not yet registered with the controller and its state is not known.

:   Flags:

:   

    :   

        **CLOUD**
        :   Indicates that the node is configured as a cloud node, to be brought up on demand, but not currently running.

        :   

        **COMPLETING**
        :   Indicates that the only job on the node or that all jobs on the node are in the process of completing.

        :   

        **DRAIN**
        :   The node is not accepting any new jobs and any currently running jobs will complete.

        :   

        **DYNAMIC**
        :   Slurm allows you to define multiple types of nodes in a FUTURE state. When starting **slurmd** on a node you can specify the **-F** flag to have the node match and use an existing definition in your slurm.conf file. The DYNAMIC state indicates that the node was started as a Dynamic Future node.

        :   

        **INVALID_REG**
        :   The node did not register correctly with the controller. This happens when a node registers with less resources than configured in the slurm.conf file. The node will clear from this state with a valid registration (i.e. a slurmd restart is required).

        :   

        **MAINTENANCE**
        :   The node is currently in a reservation that includes the *maintenance* flag.

        :   

        **NOT_RESPONDING**
        :   Node is not responding.

        :   

        **PERFCTRS**
        :   Indicates that Network Performance Counters associated with this node are in use, rendering this node as not usable for any other jobs.

        :   

        **POWER_DOWN**
        :   Node is pending power down.

        :   

        **POWERED_DOWN**
        :   Node is currently powered down and not capable of running any jobs.

        :   

        **POWERING_DOWN**
        :   Node is in the process of powering down.

        :   

        **POWERING_UP**
        :   Node is in the process of powering up.

        :   

        **PLANNED**
        :   The node is earmarked for a job that will start in the future.

        :   

        **REBOOT_ISSUED**
        :   A reboot request has been sent to the agent configured to handle this request.

        :   

        **REBOOT_REQUESTED**
        :   A request to reboot this node has been made, but hasn\'t been handled yet.

        :   

        **RESERVED**
        :   Indicates the node is in an advanced reservation and not generally available.

        :   

The meaning of the energy information is as follows:

:   

:   

    :   

        **CurrentWatts**
        :   The instantaneous power consumption of the node at the time of the last node energy accounting sample, in watts.

        :   

        **LowestJoules**
        :   The energy consumed by the node between the last time it was powered on and the last time it was registered by slurmd, in joules.

        :   

        **ConsumedJoules**
        :   The energy consumed by the node between the last time it was registered by the slurmd daemon and the last node energy accounting sample, in joules.

        :   

        If the reported value is \"n/s\" (not supported), the node does not support the configured **AcctGatherEnergyType** plugin. If the reported value is zero, energy accounting for nodes is disabled.

[ ]{#lbAN}

## PARTITIONS - SPECIFICATIONS FOR CREATE AND UPDATE COMMANDS

**PartitionName**=\<*name*\>
:   Identify the partition to be updated. This specification is required.

:   

**AllocNodes**=\<*name*\>
:   Comma separated list of nodes from which users can execute jobs in the partition. Node names may be specified using the node range expression syntax described above. The default value is \"ALL\".

:   

**AllowAccounts**=\<*name*\>
:   Comma-separated list of accounts which may execute jobs in the partition. The default value is \"ALL\". This list is hierarchical, meaning subaccounts are included automatically. **NOTE**: If AllowAccounts is used then DenyAccounts will not be enforced. Also refer to DenyAccounts.

:   

**AllowGroups**=\<*name*\>
:   Identify the user groups which may use this partition. Multiple groups may be specified in a comma separated list. To permit all groups to use the partition specify \"AllowGroups=ALL\".

:   

**AllowQOS**=\<*name*\>
:   Identify the QOSs which may use this partition. Multiple QOSs may be specified in a comma separated list. To permit all QOSs to use the partition specify \"AllowQOS=ALL\".

:   

**Alternate**=\<*partition name*\>
:   Alternate partition to be used if the state of this partition is \"DRAIN\" or \"INACTIVE.\" The value \"NONE\" will clear a previously set alternate partition.

:   

**CpuBind**=\<*node*\>
:   Specify the task binding mode to be used by default for this partition. Supported options include: \"none\", \"socket\", \"ldom\" (NUMA), \"core\", \"thread\" and \"off\" (remove previous binding mode).

:   

**Default**={yes\|no}
:   Specify if this partition is to be used by jobs which do not explicitly identify a partition to use. Possible output values are \"YES\" and \"NO\". In order to change the default partition of a running system, use the scontrol update command and set Default=yes for the partition that you want to become the new default.

:   

**DefaultTime**=\<*time*\>
:   Run time limit used for jobs that don\'t specify a value. If not set then MaxTime will be used. Format is the same as for MaxTime.

:   

**DefMemPerCPU**=\<*MB*\>
:   Set the default memory to be allocated per CPU for jobs in this partition. The memory size is specified in megabytes.

:   

**DefMemPerNode**=\<*MB*\>
:   Set the default memory to be allocated per node for jobs in this partition. The memory size is specified in megabytes.

:   

**DenyAccounts**=\<*name*\>
:   Comma-separated list of accounts which may not execute jobs in the partition. By default, no accounts are denied access. This list is hierarchical, meaning subaccounts are included automatically. **NOTE**: If AllowAccounts is used then DenyAccounts will not be enforced. Also refer to AllowAccounts.

:   

**DenyQOS**=\<*name*\>
:   Identify the QOSs which should be denied access to this partition. Multiple QOSs may be specified in a comma separated list.

:   

**DisableRootJobs**={yes\|no}
:   Specify if jobs can be executed as user root. Possible values are \"YES\" and \"NO\".

:   

**ExclusiveUser**={yes\|no}
:   When enabled nodes will be exclusively allocated to users. Multiple jobs can be run simultaneously, but those jobs must be from a single user.

:   

**GraceTime**=\<*seconds*\>
:   Specifies, in units of seconds, the preemption grace time to be extended to a job which has been selected for preemption. The default value is zero, no preemption grace time is allowed on this partition or qos. (Meaningful only for *PreemptMode=CANCEL* and *PreemptMode=REQUEUE*)

:   

**Hidden**={yes\|no}
:   Specify if the partition and its jobs should be hidden from view. Hidden partitions will by default not be reported by Slurm APIs or commands. Possible values are \"YES\" and \"NO\".

:   

**JobDefaults**=\<*specs*\>
:   Specify job default values using a comma-delimited list of \"key=value\" pairs. Supported keys include

:   

    :   

        **DefCpuPerGPU**
        :   Default number of CPUs per allocated GPU.

        :   

        **DefMemPerGPU**
        :   Default memory limit (in megabytes) per allocated GPU.

:   

**LLN**={yes\|no}
:   Schedule jobs on the least loaded nodes (based on the number of idle CPUs).

:   

**MaxCPUsPerNode**=\<*count*\>
:   Set the maximum number of CPUs that can be allocated per node to all jobs in this partition.

:   

**MaxCPUsPerSocket**=\<*count*\>
:   Set the maximum number of CPUs that can be allocated per socket to all jobs in this partition.

:   

**MaxMemPerCPU**=\<*MB*\>
:   Set the maximum memory to be allocated per CPU for jobs in this partition. The memory size is specified in megabytes.

:   

**MaxMemPerNode**=\<*MB*\>
:   Set the maximum memory to be allocated per node for jobs in this partition. The memory size is specified in megabytes.

:   

**MaxNodes**=\<*count*\>
:   Set the maximum number of nodes which will be allocated to any single job in the partition. Specify a number, \"INFINITE\" or \"UNLIMITED\". Changing the *MaxNodes* of a partition has no effect upon jobs that have already begun execution.

:   

**MaxTime**=\<*time*\>
:   The maximum run time for jobs. Output format is \[days-\]hours:minutes:seconds or \"UNLIMITED\". Input format (for **update** command) is minutes, minutes:seconds, hours:minutes:seconds, days-hours, days-hours:minutes or days-hours:minutes:seconds. Time resolution is one minute and second values are rounded up to the next minute. Changing the *MaxTime* of a partition has no effect upon jobs that have already begun execution.

:   

**MinNodes**=\<*count*\>
:   Set the minimum number of nodes which will be allocated to any single job in the partition. Changing the *MinNodes* of a partition has no effect upon jobs that have already begun execution. Increasing this value may prevent pending jobs from starting, even if they were submitted without -N/\--nodes specification. If you do get in that situation, updating the *MinNodes* value of a pending job using the scontrol command will allow that job to be scheduled.

:   

**Nodes**=\<*name*\>
:   Identify the node(s) to be associated with this partition. Multiple node names may be specified using simple node range expressions (e.g. \"lx\[10-20\]\"). A specification of \"ALL\" will associate all nodes. You can add or remove nodes by adding a \'+\' or \'-\' sign before the \'=\' sign. It also works to do nodes=+lx0,-lx\[2-4\] if you want to remove lx\[2-4\] and add lx0 at the same time. Note that jobs may only be associated with one partition at any time. Specify a blank data value to remove all nodes from a partition: \"Nodes=\". Changing the *Nodes* in a partition has no effect upon jobs that have already begun execution.

:   

**OverSubscribe**={yes\|no\|exclusive\|force}\[:\<*job_count*\>\]
:   Specify if compute resources (i.e. individual CPUs) in this partition can be shared by multiple jobs. Possible values are \"YES\", \"NO\", \"EXCLUSIVE\" and \"FORCE\". An optional job count specifies how many jobs can be allocated to use each resource.

:   

**OverTimeLimit**=\<*count*\>
:   Number of minutes by which a job can exceed its time limit before being canceled. The configured job time limit is treated as a *soft* limit. Adding **OverTimeLimit** to the *soft* limit provides a *hard* limit, at which point the job is canceled. This is particularly useful for backfill scheduling, which bases upon each job\'s soft time limit. A partition-specific *OverTimeLimit* will override any global *OverTimeLimit* value. If not specified, the global *OverTimeLimit* value will take precedence. May not exceed 65533 minutes. An input value of \"UNLIMITED\" will clear any previously configured partition-specific *OverTimeLimit* value.

:   

**PowerDownOnIdle**
:   If set to \"YES\", then nodes allocated from this partition will immediately be requested to power down upon becoming IDLE. A power down request prevents further scheduling to the node until it has been put into power save mode by **SuspendProgram**.
    Also see **SuspendTime**.

:   

**PreemptMode**=\<*mode*\>
:   Reset the mechanism used to preempt jobs in this partition if *PreemptType* is configured to *preempt/partition_prio*. The default preemption mechanism is specified by the cluster-wide *PreemptMode* configuration parameter. Possible values are \"OFF\", \"CANCEL\", \"REQUEUE\" and \"SUSPEND\".

:   

**PriorityJobFactor**=\<*count*\>
:   Partition factor used by priority/multifactor plugin in calculating job priority. The value may not exceed 65533. Also see PriorityTier.

:   

**PriorityTier**=\<*count*\>
:   Jobs submitted to a partition with a higher priority tier value will be dispatched before pending jobs in partition with lower priority tier value and, if possible, they will preempt running jobs from partitions with lower priority tier values. Note that a partition\'s priority tier takes precedence over a job\'s priority. The value may not exceed 65533. Also see PriorityJobFactor.

:   

**QOS**=\<*QOSname*\|*blank to remove*\>
:   Set the partition QOS with a QOS name or to remove the Partition QOS leave the option blank.

:   

**ReqResv**={yes\|no}
:   Specify if only allocation requests designating a reservation will be satisfied. This is used to restrict partition usage to be allowed only within a reservation. Possible values are \"YES\" and \"NO\".

:   

**RootOnly**={yes\|no}
:   Specify if only allocation requests initiated by user root will be satisfied. This can be used to restrict control of the partition to some meta-scheduler. Possible values are \"YES\" and \"NO\".

:   

**Shared**={yes\|no\|exclusive\|force}\[:\<*job_count*\>\]
:   Renamed to *OverSubscribe*, see option descriptions above.

:   

**State**={up\|down\|drain\|inactive}
:   Specify if jobs can be allocated nodes or queued in this partition. Possible values are \"UP\", \"DOWN\", \"DRAIN\" and \"INACTIVE\".

:   

    :   

        **UP**
        :   Designates that new jobs may queued on the partition, and that jobs may be allocated nodes and run from the partition.

        :   

        **DOWN**
        :   Designates that new jobs may be queued on the partition, but queued jobs may not be allocated nodes and run from the partition. Jobs already running on the partition continue to run. The jobs must be explicitly canceled to force their termination.

        :   

        **DRAIN**
        :   Designates that no new jobs may be queued on the partition (job submission requests will be denied with an error message), but jobs already queued on the partition may be allocated nodes and run. See also the \"Alternate\" partition specification.

        :   

        **INACTIVE**
        :   Designates that no new jobs may be queued on the partition, and jobs already queued may not be allocated nodes and run. See also the \"Alternate\" partition specification.

:   

**Topology**=\<*topology name*\>
:   Name of the topology, defined in *topology.yaml*, used by jobs in this partition.

:   

**TRESBillingWeights**=\<*TRES Billing Weights*\>
:   TRESBillingWeights is used to define the billing weights of each TRES type that will be used in calculating the usage of a job. The calculated usage is used when calculating fairshare and when enforcing the TRES billing limit on jobs. Updates affect new jobs and not existing jobs. See the slurm.conf man page for more information.

:   

[ ]{#lbAO}

## RESERVATIONS - SPECIFICATIONS FOR CREATE AND UPDATE COMMANDS

A new reservation must specify at least one access control field: **Users**, **Groups**, **Accounts**, **QOS**, and **AllowedPartitions**. However, Users and Groups are mutually exclusive. If multiple access control fields are specified, a job must be approved by all of them to use the reservation.

**ReservationName**=\<*name*\>
:   Identify the name of the reservation to be created or updated. This parameter is required for update. If omitted when creating a reservation, a name will be created automatically (e.g., \"scontrol create reservation \...\").

:   

**Accounts**=\<*account list*\>
:   List of accounts permitted to use the reserved nodes, for example \"Accounts=physcode1,physcode2\". A user in any of the specified accounts or subaccounts may use the reserved nodes. Refer to the start of this section for general details about access control fields. Accounts can also be denied access to reservations by preceding all of the account names with \'-\'. Alternately precede the equal sign with \'-\'. For example, \"Accounts=-physcode1,-physcode2\" or \"Accounts-=physcode1,physcode2\" will permit any account except physcode1 and physcode2 to use the reservation. You can add or remove individual accounts from an existing reservation by using the update command and adding a \'+\' or \'-\' sign before the \'=\' sign. If accounts are denied access to a reservation (account name preceded by a \'-\'), then all other accounts are implicitly allowed to use the reservation and it is not possible to also explicitly specify allowed accounts. Root and the SlurmUser are given access to all reservations, regardless of the accounts set here.

:   

**AllowedPartitions**=\<*partition list*\>
:   List of Partitions permitted to use the reserved resources, for example \"Partition=debug,low\". A user using any of the specified Partition may use the reserved resources. Refer to the start of this section for general details about access control fields. Partition can also be denied access to reservations by preceding all of the partition names with \'-\'. Alternately precede the equal sign with \'-\'. For example, \"AllowedPartitions=-debug,-low\" or \"AllowedPartitions-=debug,low\" will permit any partition except debug and low to use the reservation. You can add or remove individual partitions from an existing reservation by using the update command and adding a \'+\' or \'-\' sign before the \'=\' sign. If any partitions are denied access to a reservation (partition name preceded by a \'-\'), then all other partitions are implicitly allowed to use the reservation and it is not possible to also explicitly specify allowed partitions. Root and the SlurmUser are given access to all reservations, regardless of the partition(s) set here.

:   

**BurstBuffer**=\<*buffer_spec*\>\[,\<*buffer_spec*\>,\...\]
:   Specification of burst buffer resources which are to be reserved. \"buffer_spec\" consists of four elements: \[plugin:\]\[type:\]#\[units\] \"plugin\" is the burst buffer plugin name, currently either \"datawarp\" or \"generic\". If no plugin is specified, the reservation applies to all configured burst buffer plugins. \"type\" specifies a Cray generic burst buffer resource, for example \"nodes\". if \"type\" is not specified, the number is a measure of storage space. The \"units\" may be \"N\" (nodes), \"K\|KiB\", \"M\|MiB\", \"G\|GiB\", \"T\|TiB\", \"P\|PiB\" (for powers of 1024) and \"KB\", \"MB\", \"GB\", \"TB\", \"PB\" (for powers of 1000). The default units are bytes for reservations of storage space. For example \"BurstBuffer=datawarp:2TB\" (reserve 2TB of storage plus 3 nodes from the Cray plugin) or \"BurstBuffer=100GB\" (reserve 100 GB of storage from all configured burst buffer plugins). Jobs using this reservation are not restricted to these burst buffer resources, but may use these reserved resources plus any which are generally available. **NOTE**: Usually Slurm interprets KB, MB, GB, TB, PB units as powers of 1024, but for Burst Buffers size specifications Slurm supports both IEC/SI formats. This is because the CRAY API for managing DataWarps supports both formats.

:   

**CoreCnt**=\<*num*\>
:   This option is only supported when *select/cons_tres* is used. Identify number of cores to be reserved. If NodeCnt or Nodelist is used this is the total number of cores to reserve where cores per node is CoreCnt/NodeCnt.

:   

**Duration**=\<*time*\>
:   The length of a reservation. A new reservation must specify an end time or a duration. Valid formats are minutes, minutes:seconds, hours:minutes:seconds, days-hours, days-hours:minutes, days-hours:minutes:seconds, or UNLIMITED. Time resolution is one minute and second values are rounded up to the next minute. Output format is always \[days-\]hours:minutes:seconds.

:   

**EndTime**=\<*time_spec*\>
:   The end time for the reservation. A new reservation must specify an end time or a duration. Valid formats are the same as for StartTime.

:   

**Flags**=\<*flags*\>
:   Flags associated with the reservation. You can add or remove individual flags from an existing reservation by adding a \'+\' or \'-\' sign before the \'=\' sign. For example: Flags-=DAILY (**NOTE**: This shortcut is not supported for all flags). Currently supported flags include:

:   

    :   

        **ANY_NODES**
        :   This is a reservation for burst buffers and/or licenses only and not compute nodes. If this flag is set, a job using this reservation may use the associated burst buffers and/or licenses plus any compute nodes. If this flag is not set, a job using this reservation may use only the nodes and licenses associated with the reservation.

        :   

        **DAILY**
        :   Repeat the reservation at the same time every day.

        :   

        **FLEX**
        :   Permit jobs requesting the reservation to begin prior to the reservation\'s start time, end after the reservation\'s end time, and use any resources inside and/or outside of the reservation regardless of any constraints possibly set in the reservation. A typical use case is to prevent jobs not explicitly requesting the reservation from using those reserved resources rather than forcing jobs requesting the reservation to use those resources in the time frame reserved. Another use case could be to always have a particular number of nodes with a specific feature reserved for a specific account so users in this account may use this nodes plus possibly other nodes without this feature.

        :   

        **FORCE_START**
        :   Allow reoccurring reservations to have a start time in the past, so reoccurring reservations will not be required to be made a day in advance. This flag must be used with a reoccurring reservation flag.

        :   

        **HOURLY**
        :   Repeat the reservation at the same time every hour.

        :   

        **IGNORE_JOBS**
        :   Ignore currently running jobs when creating the reservation. This can be especially useful when reserving all nodes in the system for maintenance.

        :   

        **LICENSE_ONLY**
        :   See *ANY_NODES*.

        :   

        **MAGNETIC**
        :   This flag allows jobs to be considered for this reservation even if they didn\'t request it.

        :   

        **MAINT**
        :   Maintenance mode, receives special accounting treatment. This reservation is permitted to use resources that are already in another reservation. The MAINT flag behaves similar to STATIC_ALLOC (see below) in that it will not replace nodes once they are set.

        :   

        **NO_HOLD_JOBS_AFTER**
        :   By default, when a reservation ends the reservation request will be removed from any pending jobs submitted to the reservation and will be put into a held state. Use this flag to let jobs run outside of the reservation after the reservation is gone. Flag removal with \'-=\' is not supported.

        :   

        **OVERLAP**
        :   This reservation can be allocated resources that are already in another reservation. Flag removal with \'-=\' is not supported.

        :   

        **PART_NODES**
        :   This flag can be used to reserve all nodes within the specified partition. PartitionName and Nodes=ALL must be specified with this flag.

        :   

        **PURGE_COMP**\[=\<*timespec*\>\]
        :   Purge the reservation if it is ever idle for timespec (no jobs associated with it). If timespec isn\'t given then 5 minutes is the default. Valid timespec formats are minutes, minutes:seconds, hours:minutes:seconds, days-hours, days-hours:minutes, days-hours:minutes:seconds. Time resolution is one minute and second values are rounded up to the next minute. Output format is always \[days-\]hours:minutes:seconds.

        :   

        **REPLACE**
        :   Nodes which are DOWN, DRAINED, or allocated to jobs are automatically replenished using idle resources. This option can be used to maintain a constant number of idle resources available for pending jobs (subject to availability of idle resources). This should be used with the *NodeCnt* reservation option; do not identify specific nodes to be included in the reservation. Flag removal with \'-=\' is not supported.
            **NOTE**: Removing a node from the cluster while in a reservation with the *REPLACE* flag will not cause it to be replaced.

        :   

        **REPLACE_DOWN**
        :   Nodes which are DOWN or DRAINED are automatically replenished using idle resources. This is the default behavior. This option can be used to maintain a constant sized pool of resources available for pending jobs (subject to availability of idle resources). Nodes in use by another reservation will not be considered as possible replacement nodes. This should be used with the *NodeCnt* reservation option; do not identify specific nodes to be included in the reservation. Flag removal with \'-=\' is not supported.
            **NOTE**: Removing a node from the cluster while in a reservation with the *REPLACE_DOWN* flag will not cause it to be replaced.

        :   

        **SPEC_NODES**
        :   Reservation is for specific nodes (output only).

        :   

        **STATIC_ALLOC**
        :   Make it so after the nodes are selected for a reservation they don\'t change. Without this option when nodes are selected for a reservation and one goes down the reservation will select a new node to fill the spot.

        :   

        **TIME_FLOAT**
        :   The reservation start time is relative to the current time and moves forward through time (e.g. a StartTime=now+10minutes will always be 10 minutes in the future). Repeating (e.g. DAILY) floating reservations are not supported. Flag cannot be added to or removed from an existing reservation.

        :   

        **USER_DELETE**
        :   Allow any user able to run in the reservation to delete it.

        :   

        **WEEKDAY**
        :   Repeat the reservation at the same time on every weekday (Monday, Tuesday, Wednesday, Thursday and Friday).

        :   

        **WEEKEND**
        :   Repeat the reservation at the same time on every weekend day (Saturday and Sunday).

        :   

        **WEEKLY**
        :   Repeat the reservation at the same time every week.

:   

**Features**=\<*features*\>
:   Set the reservation\'s required node features. Multiple values may be \"&\" separated if all features are required (AND operation) or separated by \"\|\" if any of the specified features are required (OR operation). Parenthesis are also supported for features to be ANDed together with counts of nodes having the specified features. For example \"**Features=\[(knl&a2a&flat)\*4&haswell\*2\]\"** indicates the advanced reservation should include 4 nodes with ALL of the features \"knl\", \"a2a\", and \"flat\" plus 2 nodes with the feature \"haswell\".
    Value may be cleared with blank data value, \"Features=\".

:   

**Groups**=\<*group list*\>

:   List of groups permitted to use the reserved nodes, for example \"Group=bio,chem\". Refer to the start of this section for general details about access control fields. Unlike users, you cannot deny access to reservations based on group membership. Root and the SlurmUser are given access to all reservations, regardless of the groups set here.

    You can add or remove individual groups from an existing reservation by using the update command and adding a \'+\' or \'-\' sign before the \'=\' sign. You can also unset the Groups field by updating the reservation with an empty string:

        group=''

    Prior to version 25.05, if a reservation used user- or group-based access controls and slurmctld ever failed to validate the user(s) or group(s), it would delete the reservation. Reservations are now resilient to temporary validation outages.

:   

**Licenses**=\<*license*\>
:   Specification of licenses (or other resources available on all nodes of the cluster) which are to be reserved. License names can be followed by a colon and count (the default count is one). Multiple license names should be comma separated (e.g. \"Licenses=foo:4,bar\"). A new reservation must specify one or more resource to be included: NodeCnt, Nodes and/or Licenses. If a reservation includes Licenses, but no NodeCnt or Nodes, then the option *Flags=LICENSE_ONLY* must also be specified. Jobs using this reservation are not restricted to these licenses, but may use these reserved licenses plus any which are generally available.

:   

**MaxStartDelay**\[=\<*timespec*\>\]
:   Change MaxStartDelay value which specifies the maximum time an eligible job not requesting this reservation can delay a job requesting it. Default is none. Valid formats are minutes, minutes:seconds, hours:minutes:seconds, days-hours, days-hours:minutes, days-hours:minutes:seconds. Time resolution is one minute and second values are rounded up to the next minute. Output format is always \[days-\]hours:minutes:seconds.

:   

**NodeCnt**=\<*num*\>\[,\<*num*\>,\...\]
:   Identify number of nodes to be reserved. The number can include a suffix of \"k\" or \"K\", in which case the number specified is multiplied by 1024. A new reservation must specify one or more resource to be included: NodeCnt, Nodes and/or Licenses.

:   

**Nodes**=\<*name*\>
:   Identify the node(s) to be reserved. Multiple node names may be specified using simple node range expressions (e.g. \"Nodes=lx\[10-20\]\"). When using **Nodes** to specify more or fewer nodes, **NodeCnt** will be updated to honor the new number of nodes. However, when setting an empty list (\"Nodes=\"), the nodelist will be filled with random nodes to fulfill the previous nodecnt and the *SPEC_NODES* flag will be removed. A new reservation must specify one or more resource to be included: NodeCnt, Nodes and/or Licenses. A specification of \"ALL\" will reserve all nodes. Set *Flags=PART_NODES* and *PartitionName=* in order for changes in the nodes associated with a partition to also be reflected in the nodes associated with a reservation. You can add or remove nodes from an existing reservation by adding a \'+\' or \'-\' sign before the \'=\' sign. It also works to do nodes=+lx0,-lx\[2-4\] if you want to remove lx\[2-4\] and add lx0 at the same time.
    **NOTE**: When updating a reservation, if Nodes and Nodecnt are set simultaneously, nodecnt will always be honored. The reservation will get a subset of nodes if nodes \> nodecnt, or it will add extra nodes to the list when nodes \< nodecnt.

:   

**PartitionName**=\<*name*\>
:   Partition used to reserve nodes from. This will attempt to allocate all nodes in the specified partition unless you request fewer resources than are available with *CoreCnt*, *NodeCnt* or *TRES*. If no partition is specified at submit time, this partition will override the job\'s default partition. Jobs explicitly requesting a different partition will still be allowed to use this reservation as long as there are enough overlapping nodes between both partitions to allocate the job. **NOTE**: If *AllowedPartitions* is used and *PartitionName* is not given, the first partition in *AllowedPartitions* is what is used as *PartitionName*.

:   

**QOS**=\<*qos list*\>
:   List of QOS permitted to use the reserved resources, for example \"QOS=normal,standby\". A user using any of the specified QOS may use the reserved resources. Refer to the start of this section for general details about access control fields. QOS can also be denied access to reservations by preceding all of the QOS names with \'-\'. Alternately precede the equal sign with \'-\'. For example, \"QOS=-normal,-standby\" or \"QOS-=normal,standby\" will permit any QOS except normal and standby to use the reservation. You can add or remove individual QOS from an existing reservation by using the update command and adding a \'+\' or \'-\' sign before the \'=\' sign. If QOS are denied access to a reservation (QOS name preceded by a \'-\'), then all other QOS are implicitly allowed to use the reservation and it is not possible to also explicitly specify allowed QOS. Root and the SlurmUser are given access to all reservations, regardless of the QOS set here.

:   

**Skip**
:   Used on a reoccurring reservation, skip to the next reservation iteration. Requires the same permissions as deleting a reservation. **NOTE**: Only available for update.

:   

**StartTime**=\<*time_spec*\>
:   The start time for the reservation. A new reservation must specify a start time. It accepts times of the form *HH:MM:SS* for a specific time of day (seconds are optional). (If that time is already past, the next day is assumed.) You may also specify *midnight*, *noon*, *elevenses* (11 AM), *fika* (3 PM) or *teatime* (4 PM) and you can have a time-of-day suffixed with *AM* or *PM* for running in the morning or the evening. You can also say what day the job will be run, by specifying a date of the form *MMDDYY* or *MM/DD/YY* or *MM.DD.YY*, or a date and time as *YYYY-MM-DD\[THH:MM\[:SS\]\]*. You can also give times like *now + count time-units*, where the time-units can be *seconds* (default), *minutes*, *hours*, *days*, or *weeks* and you can tell Slurm to run the job today with the keyword *today* and to run the job tomorrow with the keyword *tomorrow*. You cannot update the *StartTime* of a reservation in *ACTIVE* state.

:   

**TRES**=\<*tres_spec*\>

:   Comma-separated list of TRES required for the reservation. Current supported TRES types with reservations are: CPU, GRES, Node, License and BB. CPU and Node follow the same format as CoreCnt and NodeCnt parameters respectively. License names can be followed by an equal \'=\' and a count:

    License/\<name1\>=\<count1\>\[,License/\<name2\>=\<count2\>,\...\]

    BurstBuffer can be specified in a similar way as BurstBuffer parameter. The only difference is that colon symbol \':\' should be replaced by an equal \'=\' in order to follow the TRES format.

    Some examples of TRES valid specifications:

    TRES=cpu=5,bb/cray=4,license/iop1=1,license/iop2=3

    TRES=node=5k,license/iop1=2

    TRES=gres/gpu:a100=2

    Please note that CPU, Node, License and BB can override CoreCnt, NodeCnt, Licenses and BurstBuffer parameters respectively. Also CPU represents CoreCnt, in a reservation and will be adjusted if you have threads per core on your nodes.

    Note that a reservation that contains nodes or cores is associated with one partition, and can\'t span resources over multiple partitions. The only exception from this is when the reservation is created with explicitly requested nodes.

    Note that if GRES is requested those GRES must be TRES listed in AccountingStorageTRES to be valid.

    \
    **NOTE**: Reservations will automatically attempt to enforce binding on GRES. Multiple GRES cannot be reserved across multiple sockets.

:   

**TRESPerNode**=\<*tres_spec*\>

:   Comma-separated list of TRES required per node for the reservation. See **TRES** above for supported types.

    TRESPerNode=gres/gpu:a100=2

    Above will allocate 2 gpu:a100 per node as specified in nodecnt.

:   

**Users**=\<*user list*\>

:   List of users permitted to use the reserved nodes, for example \"User=jones1,smith2\". Users can also be denied access to a reservation, indicated by having a \'-\' sign before their name, e.g. \"User=-jones1,-smith2\". Refer to the start of this section for general details about access control fields.

    Root and the SlurmUser are given access to all reservations, regardless of the users set here.

    Each user in the system may be in one of three states in a reservation:\
     - Explicitly allowed\
     - Unspecified\
     - Explicitly denied

    If any users are explicitly allowed to use a reservation, all other users are implicitly denied access. If any users are explicitly denied access to a reservation, all other users are implicitly allowed access to the reservation.

    When updating existing reservations, you may use the \'+=\' and \'-=\' operators to move users up (+) or down (-) on the list of states. However, you cannot have a mix of explicitly allowed and explicitly denied users on the same reservation, and an update command that would result in that state will result in an error. The \'+\' or \'-\' sign can also be placed directly before the username. For example, the following are equivalent:

        User-=jones1,smith2

        User=-jones1,-smith2

    In these examples, if the users were explicitly allowed before, this assignment would remove their names from the allowed list and place them in the unspecified state. If the command was repeated again the users would be explicitly denied from the reservation.

    You can also unset the Users field (reverting all to a neutral/unspecified state) by updating the reservation with an empty string:

        user=''

    Prior to version 25.05, if a reservation used user- or group-based access controls and slurmctld ever failed to validate the user(s) or group(s), it would delete the reservation. Reservations are now resilient to temporary validation outages.

:   

[ ]{#lbAP}

## PERFORMANCE

Executing **scontrol** sends a remote procedure call to **slurmctld**. If enough calls from **scontrol** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **scontrol** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **scontrol** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAQ}

## ENVIRONMENT VARIABLES

Some **scontrol** options may be set via environment variables. These environment variables, along with their corresponding options, are listed below. (Note: Command line options will always override these settings.)

**SCONTROL_ALL**
:   **-a, \--all**

:   

**SCONTROL_FEDERATION**
:   **\--federation**

:   

**SCONTROL_FUTURE**
:   **-F, \--future**

:   

**SCONTROL_LOCAL**
:   **\--local**

:   

**SCONTROL_SIBLING**
:   **\--sibling**

:   

**SLURM_BITSTR_LEN**
:   Specifies the string length to be used for holding a job array\'s task ID expression. The default value is 64 bytes. A value of 0 will print the full expression with any length required. Larger values may adversely impact the application performance.

:   

**SLURM_CLUSTERS**
:   Same as **\--clusters**

:   

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_CONF_OUT**
:   When running \'write config\', the location of the Slurm configuration file to be written.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for scontrol to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

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

**SLURM_TOPO_LEN**
:   Specify the maximum size of the line when printing Topology. If not set, the default value is unlimited.

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

[ ]{#lbAR}

## AUTHORIZATION

Slurm generally classifies users into three authorization levels:\
 - **Administrators** include root, SlurmUser, and any users with \"AdminLevel=Administrator\"\
 - **Privileged Users** include all Administrators and any users with \"AdminLevel=Operator\"\
 - **Effective Owners** of a job or step include the direct owner and all Coordinators of the corresponding account.

Note that configuring AdminLevels or Coordinators requires the use of SlurmDBD. The authorization levels required to execute various commands are defined in the following table.

**scontrol update job:** Privileged or Effective Owner\
**scontrol requeue:** Privileged or Effective Owner\
**scontrol update step:** Privileged or Effective Owner\
**scontrol suspend:** Privileged or Coordinator\
**scontrol resume:** Privileged or Coordinator\
**scontrol notify:** Root, SlurmUser, or direct owner\
**scontrol write batch_script:** Privileged or direct owner\

**scontrol create node:** Admin\
**scontrol update node:** Admin\
**scontrol delete node:** Admin\

**scontrol create partition:** Admin\
**scontrol update partition:** Admin\
**scontrol delete partition:** Admin\

**scontrol create reservation:** Privileged\
**scontrol update reservation:** Privileged\
**scontrol delete reservation:** Privileged\

**scontrol reconfig:** Admin\
**scontrol shutdown:** Admin\
**scontrol takeover:** Admin\

\
The **scontrol show** commands are available to all users by default. If any PrivateData restrictions are defined in the slurm.conf file, the listed authorization levels will be required to access the corresponding data.

**scontrol show job(s):** Privileged or Effective Owner\
**scontrol show step(s):** Privileged or Effective Owner\

**scontrol show node:** Privileged\
**scontrol show host\*:** Privileged\

**scontrol show partition:** Privileged\
**scontrol show reservation:** Privileged or Access\

**scontrol show assoc_mgr:** See assoc_mgr description for details\

[ ]{#lbAS}

## EXAMPLES

    $ scontrol
    scontrol: show part debug
    PartitionName=debug
       AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
       AllocNodes=ALL Default=YES QoS=N/A
       DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO ExclusiveTopo=NO GraceTime=0 Hidden=NO
       MaxNodes=UNLIMITED MaxTime=UNLIMITED MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED MaxCPUsPerSocket=UNLIMITED
       NodeSets=ALL
       Nodes=snowflake[0-48]
       PriorityJobFactor=100 PriorityTier=100 RootOnly=NO ReqResv=NO OverSubscribe=NO
       OverTimeLimit=NONE PreemptMode=REQUEUE
       State=UP TotalCPUs=588 TotalNodes=49 SelectTypeParameters=NONE
       JobDefaults=(null)
       DefMemPerNode=UNLIMITED MaxMemPerNode=UNLIMITED
       TRES=cpu=588,mem=1204224M,node=49,billing=49
    scontrol: update PartitionName=debug MaxTime=60:00 MaxNodes=4
    scontrol: show job 71701
    JobId=71701 Name=hostname
       UserId=da(1000) GroupId=da(1000)
       Priority=66264 Account=none QOS=normal WCKey=*123
       JobState=COMPLETED Reason=None Dependency=(null)
       TimeLimit=UNLIMITED Requeue=1 Restarts=0 BatchFlag=0 ExitCode=0:0
       SubmitTime=2010-01-05T10:58:40 EligibleTime=2010-01-05T10:58:40
       StartTime=2010-01-05T10:58:40 EndTime=2010-01-05T10:58:40
       SuspendTime=None SecsPreSuspend=0
       Partition=debug AllocNode:Sid=snowflake:4702
       ReqNodeList=(null) ExcNodeList=(null)
       NodeList=snowflake0
       NumNodes=1 NumCPUs=10 CPUs/Task=2 ReqS:C:T=1:1:1
       MinCPUsNode=2 MinMemoryNode=0 MinTmpDiskNode=0
       Features=(null) Reservation=(null)
       OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
    scontrol: update JobId=71701 TimeLimit=30:00 Priority=500
    scontrol: show hostnames tux[1-3]
    tux1
    tux2
    tux3
    scontrol: create res StartTime=2009-04-01T08:00:00 Duration=5:00:00 Users=dbremer NodeCnt=10
    Reservation created: dbremer_1
    scontrol: update Reservation=dbremer_1 Flags=Maint NodeCnt=20
    scontrol: delete Reservation=dbremer_1
    scontrol: quit

[ ]{#lbAT}

## COPYING

Copyright (C) 2002-2007 The Regents of the University of California. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2008-2010 Lawrence Livermore National Security.\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. [ ]{#lbAU}

## FILES

/etc/slurm.conf [ ]{#lbAV}

## SEE ALSO

**[scancel](scancel.md)**(1), **[sinfo](sinfo.md)**(1), **[squeue](squeue.md)**(1), **slurm_create_partition** (3), **slurm_delete_partition** (3), **slurm_load_ctl_conf** (3), **slurm_load_jobs** (3), **slurm_load_node** (3), **slurm_load_partitions** (3), **slurm_reconfigure** (3), **slurm_requeue** (3), **slurm_resume** (3), **slurm_shutdown** (3), **slurm_suspend** (3), **slurm_takeover** (3), **slurm_update_job** (3), **slurm_update_node** (3), **slurm_update_partition** (3), **[slurm.conf](slurm.conf.md)**(5), **[slurmctld](slurmctld.md)**(8)

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

COMMANDS

:   

INTERACTIVE COMMANDS

:   

JOBS - SPECIFICATIONS FOR UPDATE COMMAND

:   

JOBS - SPECIFICATIONS FOR SHOW COMMAND

:   

STEPS - SPECIFICATIONS FOR UPDATE COMMAND

:   

NODES - SPECIFICATIONS FOR CREATE COMMAND

:   

NODES - SPECIFICATIONS FOR UPDATE COMMAND

:   

NODES - SPECIFICATIONS FOR SHOW COMMAND

:   

PARTITIONS - SPECIFICATIONS FOR CREATE AND UPDATE COMMANDS

:   

RESERVATIONS - SPECIFICATIONS FOR CREATE AND UPDATE COMMANDS

:   

PERFORMANCE

:   

ENVIRONMENT VARIABLES

:   

AUTHORIZATION

:   

EXAMPLES

:   

COPYING

:   

FILES

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
