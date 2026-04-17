# [Slurm Troubleshooting Guide]{#top}

This guide is meant as a tool to help system administrators or operators troubleshoot Slurm failures and restore services. The [Frequently Asked Questions](faq.md) document may also prove useful.

- Slurm is not responding
- Jobs are not getting scheduled
- Jobs and nodes are stuck in COMPLETING state
- Nodes are getting set to a DOWN state
- Networking and configuration problems

## Slurm is not responding {#resp}

1.  Execute \"*scontrol ping*\" to determine if the primary and backup controllers are responding.
2.  If it responds for you, this could be a networking or configuration problem specific to some user or node in the cluster.
3.  If not responding, directly login to the machine and try again to rule out network and configuration problems.
4.  If still not responding, check if there is an active slurmctld daemon by executing \"*ps -el \| grep slurmctld*\".
5.  If slurmctld is not running, restart it (typically as user root using the command \"*/etc/init.d/slurm start*\"). You should check the log file (*SlurmctldLog* in the *slurm.conf* file) for an indication of why it failed.
6.  If slurmctld is running but not responding (a very rare situation), then kill and restart it (typically as user root using the commands \"*/etc/init.d/slurm stop*\" and then \"*/etc/init.d/slurm start*\").
7.  If it hangs again, increase the verbosity of debug messages (increase *SlurmctldDebug* in the *slurm.conf* file) and restart. Again check the log file for an indication of why it failed.
8.  If it continues to fail without an indication as to the failure mode, restart without preserving state (typically as user root using the commands \"*/etc/init.d/slurm stop*\" and then \"*/etc/init.d/slurm startclean*\"). Note: All running jobs and other state information will be lost.

## Jobs are not getting scheduled {#sched}

This is dependent upon the scheduler used by Slurm. Executing the command \"*scontrol show config \| grep SchedulerType*\" to determine this. For any scheduler, you can check priorities of jobs using the command \"*scontrol show job*\".

- If the scheduler type is *builtin*, then jobs will be executed in the order of submission for a given partition. Even if resources are available to initiate jobs immediately, it will be deferred until no previously submitted job is pending.
- If the scheduler type is *backfill*, then jobs will generally be executed in the order of submission for a given partition with one exception: later submitted jobs will be initiated early if doing so does not delay the expected execution time of an earlier submitted job. In order for backfill scheduling to be effective, users jobs should specify reasonable time limits. If jobs do not specify time limits, then all jobs will receive the same time limit (that associated with the partition), and the ability to backfill schedule jobs will be limited. The backfill scheduler does not alter job specifications of required or excluded nodes, so jobs which specify nodes will substantially reduce the effectiveness of backfill scheduling. See the [backfill documentation](faq.md#backfill) for more details.

## Jobs and nodes are stuck in COMPLETING state {#completing}

This is typically due to non-killable processes associated with the job. Slurm will continue to attempt terminating the processes with SIGKILL, but some jobs may be stuck performing I/O and non-killable. This is typically due to a file system problem and may be addressed in a couple of ways.

1.  Fix the file system and/or reboot the node. **-OR-**
2.  Set the node to a DOWN state and then return it to service (\"*scontrol update NodeName=\<node\> State=down Reason=hung_proc*\" and \"*scontrol update NodeName=\<node\> State=resume*\"). This permits other jobs to use the node, but leaves the non-killable process in place. If the process should ever complete the I/O, the pending SIGKILL should terminate it immediately. **-OR-**
3.  Use the **UnkillableStepProgram** and **UnkillableStepTimeout** configuration parameters to automatically respond to processes which can not be killed, by sending email or rebooting the node. For more information, see the *slurm.conf* documentation.

If it doesn\'t look like your job is stuck because of filesystem problems it may take some debugging to find the cause. If you can reproduce the behavior you can set the SlurmdDebug level to \'debug\' and restart slurmd on a node you\'ll use to reproduce the problem. The slurmd.log file should then have more information to help troubleshoot the issue. Looking at slurmctld.log may also provide clues. If nodes stop responding, you may want to look into why since they may prevent job cleanup and cause jobs to remain in a COMPLETING state. When looking for connectivity problems, the relevant log entries should look something like this:

    error: Nodes node[00,03,25] not responding
    Node node00 now responding

## Nodes are getting set to a DOWN state {#nodes}

1.  Check the reason why the node is down using the command \"*scontrol show node \<name\>*\". This will show the reason why the node was set down and the time when it happened. If there is insufficient disk space, memory space, etc. compared to the parameters specified in the *slurm.conf* file then either fix the node or change *slurm.conf*.
2.  If the reason is \"Not responding\", then check communications between the control machine and the DOWN node using the command \"*ping \<address\>*\" being sure to specify the NodeAddr values configured in *slurm.conf*. If ping fails, then fix the network or addresses in *slurm.conf*.
3.  Next, login to a node that Slurm considers to be in a DOWN state and check if the slurmd daemon is running with the command \"*ps -el \| grep slurmd*\". If slurmd is not running, restart it (typically as user root using the command \"*/etc/init.d/slurm start*\"). You should check the log file (*SlurmdLog* in the *slurm.conf* file) for an indication of why it failed. You can get the status of the running slurmd daemon by executing the command \"*scontrol show slurmd*\" on the node of interest. Check the value of \"Last slurmctld msg time\" to determine if the slurmctld is able to communicate with the slurmd.
4.  If slurmd is running but not responding (a very rare situation), then kill and restart it (typically as user root using the commands \"*/etc/init.d/slurm stop*\" and then \"*/etc/init.d/slurm start*\").
5.  If still not responding, try again to rule out network and configuration problems.
6.  If still not responding, increase the verbosity of debug messages (increase *SlurmdDebug* in the *slurm.conf* file) and restart. Again check the log file for an indication of why it failed.
7.  If still not responding without an indication as to the failure mode, restart without preserving state (typically as user root using the commands \"*/etc/init.d/slurm stop*\" and then \"*/etc/init.d/slurm startclean*\"). Note: All jobs and other state information on that node will be lost.

## Networking and configuration problems {#network}

1.  Check the controller and/or slurmd log files (*SlurmctldLog* and *SlurmdLog* in the *slurm.conf* file) for an indication of why it is failing.
2.  Check for consistent *slurm.conf* and credential files on the node(s) experiencing problems.
3.  If this is user-specific problem, check that the user is configured on the controller computer(s) as well as the compute nodes. The user doesn\'t need to be able to login, but his user ID must exist.
4.  Check that compatible versions of Slurm exists on all of the nodes (execute \"*sinfo -V*\" or \"*rpm -qa \| grep slurm*\"). The Slurm version number contains three period-separated numbers that represent both the major Slurm release and maintenance release level. The first two parts combine together to represent the major release, and match the year and month of that major release. The third number in the version designates a specific maintenance level: year.month.maintenance-release (e.g. 17.11.5 is major Slurm release 17.11, and maintenance version 5). Thus version 17.11.x was initially released in November 2017. Slurm daemons will support RPCs and state files from the two previous major releases (e.g. a version 17.11.x SlurmDBD will support slurmctld daemons and commands with a version of 17.11.x, 17.02.x or 16.05.x).
