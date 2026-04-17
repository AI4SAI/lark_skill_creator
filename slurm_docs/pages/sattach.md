# sattach

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

sattach - Attach to a Slurm job step. [ ]{#lbAC}

## SYNOPSIS

sattach \[*options*\] \<jobid.stepid\> [ ]{#lbAD}

## DESCRIPTION

sattach attaches to a running Slurm job step. By attaching, it makes available the IO streams of all of the tasks of a running Slurm job step. It is also suitable for use with a parallel debugger like TotalView. It cannot be used to attach directly to extern or batch steps since the IO channels of these steps are not set or directly forwarded to a file.

[ ]{#lbAE}

## OPTIONS

**\--error-filter**\[=\]\<*task number*\>
:   Only transmit standard input to a single task, or print the standard output or standard error from a single task. The filtering is performed locally in sattach.

:   

**-h**, **\--help**
:   Display help information and exit.

:   

**\--input-filter**\[=\]\<*task number*\>
:   Only transmit standard input to a single task, or print the standard output or standard error from a single task. The filtering is performed locally in sattach.

:   

**-l**, **\--label**
:   Prepend each line of task standard output or standard error with the task number of its origin.

:   

**\--layout**
:   Contacts the slurmctld to obtain the task layout information for the job step, prints the task layout information, and then exits without attaching to the job step.

:   

**\--output-filter**\[=\]\<*task number*\>
:   Only transmit standard input to a single task, or print the standard output or standard error from a single task. The filtering is performed locally in sattach.

:   

**\--pty**
:   Execute task zero in pseudo terminal. Not compatible with the **\--input-filter**, **\--output-filter**, or **\--error-filter** options. Notes: The terminal size and resize events are ignored by sattach. Proper operation requires that the job step be initiated by srun using the \--pty option.

:   

**-Q**, **\--quiet**
:   Suppress informational messages from sattach. Errors will still be displayed.

:   

**-u**, **\--usage**
:   Display brief usage message and exit.

:   

**-V**, **\--version**
:   Display Slurm version number and exit.

:   

**-v**, **\--verbose**
:   Increase the verbosity of sattach\'s informational messages. Multiple **-v**\'s will further increase sattach\'s verbosity.

:   

[ ]{#lbAF}

## PERFORMANCE

Executing **sattach** sends a remote procedure call to **slurmctld**. If enough calls from **sattach** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **sattach** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **sattach** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAG}

## INPUT ENVIRONMENT VARIABLES

Upon startup, salloc will read and handle the options set in the following environment variables. Note: Command line options always override environment variables settings.

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for sattach to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

**SLURM_EXIT_ERROR**
:   Specifies the exit code generated when a Slurm error occurs (e.g. invalid options). This can be used by a script to distinguish application exit codes from various Slurm error conditions.

:   

[ ]{#lbAH}

## EXAMPLES

Attach to job 15, step 0:

:   

:   $ sattach 15.0

Limit the output to the 5th task of job 65386, step 15:

:   

:   $ sattach --output-filter 5 65386.15

[ ]{#lbAI}

## COPYING

Copyright (C) 2006-2007 The Regents of the University of California. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2008-2009 Lawrence Livermore National Security.\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAJ}

## SEE ALSO

**[sinfo](sinfo.md)**(1), **[salloc](salloc.md)**(1), **[sbatch](sbatch.md)**(1), **[squeue](squeue.md)**(1), **[scancel](scancel.md)**(1), **[scontrol](scontrol.md)**(1), **[slurm.conf](slurm.conf.md)**(5), **sched_setaffinity** (2), **numa** (3)

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

PERFORMANCE

:   

INPUT ENVIRONMENT VARIABLES

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
