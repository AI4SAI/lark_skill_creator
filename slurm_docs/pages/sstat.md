# sstat

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

sstat - Display the status information of a running job/step.

[ ]{#lbAC}

## SYNOPSIS

**sstat** \[*OPTIONS*\...\]

[ ]{#lbAD}

## DESCRIPTION

Status information for running jobs invoked with Slurm.

The **sstat** command displays job status information for your analysis. The **sstat** command displays information pertaining to CPU, Task, Node, Resident Set Size (RSS) and Virtual Memory (VM). You can tailor the output with the use of the **\--fields=** option to specify the fields to be shown.

For the root user, the **sstat** command displays job status data for any job running on the system.

For the non-root user, the **sstat** output is limited to the user\'s jobs.

**NOTE**: The **sstat** command requires that the **jobacct_gather** plugin be installed and operational.

**NOTE**: Availability of metrics rely on the **jobacct_gather** plugin used. For example the jobacct_gather/cgroup in combination with cgroup/v2 does not provide Virtual Memory metrics due to limitations in the kernel cgroups interfaces and will show a 0 for the related fields. [ ]{#lbAE}

## OPTIONS

**-a**, **\--allsteps**
:   Print all steps for the given job(s) when no step is specified.

:   

**-o**, **\--format**, **\--fields**

:   Comma separated list of fields. (use \'\--helpformat\' for a list of available fields).

    **NOTE**: When using the format option for listing various fields you can put a %NUMBER afterwards to specify how many characters should be printed.

    i.e. format=name%30 will print 30 characters of field name right justified. A -30 will print 30 characters left justified.

:   

**-h**, **\--help**
:   Displays a general help message.

:   

**-e**, **\--helpformat**
:   Print a list of fields that can be specified with the \'\--format\' option.

:   

**-j**, **\--jobs**
:   Format is \<job(.step)\>. Stat this job step or comma-separated list of job steps. This option is required. The step portion will default to the lowest numbered (not batch, extern, etc) step running if not specified, unless the \--allsteps flag is set where not specifying a step will result in all running steps to be displayed. **NOTE**: A step id of \'batch\' will display the information about the batch step. **NOTE**: A step id of \'extern\' will display the information about the extern step. This step is only available when using PrologFlags=contain

:   

**\--noconvert**
:   Don\'t convert units from their original type (e.g. 2048M won\'t be converted to 2G).

:   

**-n**, **\--noheader**
:   No heading will be added to the output. The default action is to display a header.

:   

**-p**, **\--parsable**
:   output will be \'\|\' delimited with a \'\|\' at the end

:   

**-P**, **\--parsable2**
:   output will be \'\|\' delimited without a \'\|\' at the end

:   

**-i**, **\--pidformat**
:   Predefined format to list the pids running for each job step. (JobId,Nodes,Pids)

:   

**\--usage**
:   Display a command usage summary.

:   

**-v**, **\--verbose**
:   Primarily for debugging purposes, report the state of various variables during processing.

:   

**-V**, **\--version**
:   Print version.

:   

[ ]{#lbAF}

### Job Status Fields

Descriptions of each field option can be found below. Note that the Ave\*, Max\* and Min\* accounting fields look at the values for all the tasks of each step in a job and return the average, maximum or minimum values of the task for that job step. For example, for MaxRSS, the returned value is the maximum memory consumption seen by one of the tasks of the step, and MaxRSSTask shows which task it is.

:   

    **AllocTRES**
    :   Allocated TRES of all tasks in job.

    :   

    **AveCPU**
    :   Average (system + user) CPU time of all tasks in job.

    :   

    **AveCPUFreq**
    :   Average weighted CPU frequency of all tasks in job, in kHz.

    :   

    **AveDiskRead**
    :   Average number of bytes read by all tasks in job.

    :   

    **AveDiskWrite**
    :   Average number of bytes written by all tasks in job.

    :   

    **AvePages**
    :   Average number of page faults of all tasks in job.

    :   

    **AveRSS**
    :   Average resident set size of all tasks in job.

    :   

    **AveVMSize**
    :   Average Virtual Memory size of all tasks in job.

    :   

    **ConsumedEnergy**
    :   Total energy consumed by all tasks in job, in joules. Note: Only in case of exclusive job allocation this value reflects the jobs\' real energy consumption.

    :   

    **JobID**
    :   The number of the job or job step. It is in the form: *job.jobstep*

    :   

    **MaxDiskRead**
    :   Maximum number of bytes read by all tasks in job.

    :   

    **MaxDiskReadNode**
    :   The node on which the maxdiskread occurred.

    :   

    **MaxDiskReadTask**
    :   The task ID where the maxdiskread occurred.

    :   

    **MaxDiskWrite**
    :   Maximum number of bytes written by all tasks in job.

    :   

    **MaxDiskWriteNode**
    :   The node on which the maxdiskwrite occurred.

    :   

    **MaxDiskWriteTask**
    :   The task ID where the maxdiskwrite occurred.

    :   

    **MaxPages**
    :   Maximum number of page faults of all tasks in job.

    :   

    **MaxPagesNode**
    :   The node on which the maxpages occurred.

    :   

    **MaxPagesTask**
    :   The task ID where the maxpages occurred.

    :   

    **MaxRSS**
    :   Maximum resident set size of all tasks in job.

    :   

    **MaxRSSNode**
    :   The node on which the maxrss occurred.

    :   

    **MaxRSSTask**
    :   The task ID where the maxrss occurred.

    :   

    **MaxVMSize**
    :   Maximum Virtual Memory size of all tasks in job.

    :   

    **MaxVMSizeNode**
    :   The node on which the maxvsize occurred.

    :   

    **MaxVMSizeTask**
    :   The task ID where the maxvsize occurred.

    :   

    **MinCPU**
    :   Minimum (system + user) CPU time of all tasks in job.

    :   

    **MinCPUNode**
    :   The node on which the mincpu occurred.

    :   

    **MinCPUTask**
    :   The task ID where the mincpu occurred.

    :   

    **NTasks**
    :   Total number of tasks in a job or step.

    :   

    **ReqCPUFreq**
    :   Requested CPU frequency for the step, in kHz.

    :   

    **TresUsageInAve**
    :   Tres average usage in by all tasks in job. **NOTE**: If corresponding TresUsageInMaxTask is -1 the metric is node centric instead of task.

    :   

    **TresUsageInMax**
    :   Tres maximum usage in by all tasks in job. **NOTE**: If corresponding TresUsageInMaxTask is -1 the metric is node centric instead of task.

    :   

    **TresUsageInMaxNode**
    :   Node for which each maximum TRES usage out occurred.

    :   

    **TresUsageInMaxTask**
    :   Task for which each maximum TRES usage out occurred.

    :   

    **TresUsageOutAve**
    :   Tres average usage out by all tasks in job. **NOTE**: If corresponding TresUsageOutMaxTask is -1 the metric is node centric instead of task.

    :   

    **TresUsageOutMax**
    :   Tres maximum usage out by all tasks in job. **NOTE**: If corresponding TresUsageOutMaxTask is -1 the metric is node centric instead of task.

    :   

    **TresUsageOutMaxNode**
    :   Node for which each maximum TRES usage out occurred.

    :   

    **TresUsageOutMaxTask**
    :   Task for which each maximum TRES usage out occurred.

    :   

[ ]{#lbAG}

## PERFORMANCE

Executing **sstat** sends a remote procedure call to **slurmctld**. If enough calls from **sstat** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **sstat** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **sstat** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAH}

## ENVIRONMENT VARIABLES

Some **sstat** options may be set via environment variables. These environment variables, along with their corresponding options, are listed below. (Note: Command line options will always override these settings.)

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for sstat to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

[ ]{#lbAI}

## EXAMPLES

Display job step information for job 11 with the specified fields:

:   

:   $ sstat --format=AveCPU,AvePages,AveRSS,AveVMSize,JobID -j 11
        25:02.000  0K         1.37M      5.93M      9.0

Display job step information for job 11 with the specified fields in a parsable format:

:   

:   $ sstat -p --format=AveCPU,AvePages,AveRSS,AveVMSize,JobID -j 11
        25:02.000|0K|1.37M|5.93M|9.0|

[ ]{#lbAJ}

## COPYING

Copyright (C) 2009 Lawrence Livermore National Security. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAK}

## SEE ALSO

**[sacct](sacct.md)**(1)

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

    Job Status Fields

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
