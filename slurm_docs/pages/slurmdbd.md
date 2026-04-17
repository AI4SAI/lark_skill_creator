# slurmdbd

Section: Slurm Daemon (8)\
Updated: Slurm Daemon\
Index

[ ]{#lbAB}

## NAME

slurmdbd - Slurm Database Daemon.

[ ]{#lbAC}

## SYNOPSIS

**slurmdbd** \[*OPTIONS*\...\]

[ ]{#lbAD}

## DESCRIPTION

**slurmdbd** provides a secure enterprise-wide interface to a database for Slurm. This is particularly useful for archiving accounting records.

[ ]{#lbAE}

## OPTIONS

**-D**
:   Run **slurmdbd** in the foreground with logging copied to stdout.

:   

**-h**
:   Help; print a brief summary of command options.

:   

**-n \<value\>**
:   Set the daemon\'s nice value to the specified value, typically a negative number.

:   

**-s**
:   Change working directory of slurmdbd to LogFile path if possible, or to /var/tmp otherwise.

:   

**-u**
:   Only display the Slurm Database version and if conversion is needed and exit without taking control. If no conversion is needed 0 is returned, if conversion is needed 1 is returned.

:   

**-v**
:   Verbose operation. Multiple **v**\'s can be specified, with each \'**v**\' beyond the first increasing verbosity, up to 6 times (i.e. -vvvvvv).

:   

**-V**
:   Print version information and exit.

:   

[ ]{#lbAF}

## ENVIRONMENT VARIABLES

The following environment variables can be used to override settings compiled into slurmdbd.

**ABORT_ON_FATAL**
:   When a fatal error is detected, use abort() instead of exit() to terminate the process. This allows backtraces to be captured without recompiling Slurm.

:   

[ ]{#lbAG}

## CORE FILE LOCATION

If slurmdbd is started with the **-D** option then the core file will be written to the current working directory. Otherwise if **LogFile** in \"slurmdbd.conf\" is a fully qualified path name (starting with a slash), the core file will be written to the same directory as the log file, provided SlurmUser has write permission on the directory. Otherwise the core file will be written to \"/var/tmp/\" as a last resort. If neither of the above directories have write permission for SlurmUser, no core file will be produced.

[ ]{#lbAH}

## SIGNALS

**SIGTERM SIGINT SIGQUIT**
:   **slurmdbd** will shutdown cleanly, waiting for in-progress rollups to finish.

:   

**SIGABRT**
:   **slurmdbd** will perform a core dump, then exit. In-progress operations are killed.

:   

**SIGHUP**
:   Reloads the slurm configuration files, similar to \'scontrol reconfigure\'.

:   

**SIGTSTP**
:   Stop the process from a terminal.

:   

**SIGUSR2**
:   Reread the log level from the configs, and then reopen the log file. This should be used when setting up **logrotate**(8).

:   

**SIGCHLD SIGUSR1 SIGXCPU SIGPIPE SIGALRM**
:   These signals are explicitly ignored.

:   

[ ]{#lbAI}

## NOTES

It may be useful to experiment with different **slurmctld** specific configuration parameters using a distinct configuration file (e.g. timeouts). However, this special configuration file will not be used by the **slurmd** daemon or the Slurm programs, unless you specifically tell each of them to use it. If you desire changing communication ports, the location of the temporary file system, or other parameters used by other Slurm components, change the common configuration file, **slurm.conf**.

[ ]{#lbAJ}

## COPYING

Copyright (C) 2008 Lawrence Livermore National Security. Copyright (C) 2010-2022 SchedMD LLC. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER). CODE-OCEC-09-009. All rights reserved.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAK}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[slurmdbd.conf](slurmdbd.conf.md)**(5), **[slurmctld](slurmctld.md)**(8)

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

ENVIRONMENT VARIABLES

:   

CORE FILE LOCATION

:   

SIGNALS

:   

NOTES

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
