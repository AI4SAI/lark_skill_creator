# slurmctld

Section: Slurm Daemon (8)\
Updated: Slurm Daemon\
Index

[ ]{#lbAB}

## NAME

slurmctld - The central management daemon of Slurm. [ ]{#lbAC}

## SYNOPSIS

**slurmctld** \[*OPTIONS*\...\] [ ]{#lbAD}

## DESCRIPTION

**slurmctld** is the central management daemon of Slurm. It monitors all other Slurm daemons and resources, accepts work (jobs), and allocates resources to those jobs. Given the critical functionality of **slurmctld**, there may be a backup server to assume these functions in the event that the primary server fails.

[ ]{#lbAE}

## OPTIONS

**-c**
:   Clear all previous **slurmctld** state from its last checkpoint. With this option, all jobs, including both running and queued, and all node states, will be deleted. Without this option, previously running jobs will be preserved along with node *State* of DOWN, DRAINED and DRAINING nodes and the associated *Reason* field for those nodes. **NOTE**: It is rare you would ever want to use this in production as all jobs will be killed.

:   

**-D**
:   Run **slurmctld** in the foreground with logging copied to stderr. This limits the resilience of \'scontrol reconfigure\' and should be avoided in production.

:   

**-f \<file\>**
:   Read configuration from the specified file. See **NOTES** below.

:   

**-h**
:   Help; print a brief summary of command options.

:   

**-i**
:   Ignore errors found while reading in state files on startup. Warning: Use of this option will mean losing the data that wasn\'t recovered from the state files.

:   

**-L \<file\>**
:   Write log messages to the specified file.

:   

**-n \<value\>**
:   Set the daemon\'s nice value to the specified value, typically a negative number.

:   

**-r**
:   Recover partial state from last checkpoint: jobs and node DOWN/DRAIN state and reason information state. No partition state is recovered. This is the default action.

:   

**-R**
:   Recover full state from last checkpoint: jobs, node, partition state, and power save settings. Without this option, previously running jobs will be preserved along with node *State* of DOWN, DRAINED and DRAINING nodes and the associated *Reason* field for those nodes. No other node or partition state will be preserved.

:   

**-s**
:   Change working directory of slurmctld to SlurmctldLogFile path if possible, or to Slurm\'s StateSaveLocation otherwise. If both of them fail it will fallback to /var/tmp.

:   

**\--systemd**
:   Use when starting the daemon with systemd. This will allow slurmctld to notify systemd of the new PID when using \'scontrol reconfigure\'.
    **NOTE**: The User and Group options in the slurmctld\'s systemd unit file need to both specify the SlurmUser.

:   

**-v**
:   Verbose operation. Multiple **v**\'s can be specified, with each \'**v**\' beyond the first increasing verbosity, up to 6 times (i.e. -vvvvvv).

:   

**-V**
:   Print version information and exit.

:   

[ ]{#lbAF}

## ENVIRONMENT VARIABLES

The following environment variables can be used to override settings compiled into slurmctld.

**ABORT_ON_FATAL**
:   When a fatal error is detected, use abort() instead of exit() to terminate the process. This allows backtraces to be captured without recompiling Slurm.

:   

**SLURM_CONF**
:   The location of the Slurm configuration file. This is overridden by explicitly naming a configuration file on the command line.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for the scheduler to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

[ ]{#lbAG}

## HTTP server

Unless disabled via *CommunicationParameters=disable_http* in **slurm.conf**, **slurmctld** will accept incoming HTTP/1.1 compliant requests to any socket listening as configured by **SlurmctldPort** in **slurm.conf**. Authentication of HTTP requests is not supported. TLS wrapping optionally supported without requiring **TLSType** in **slurm.conf**. The following endpoints are currently supported:

**GET /**
:   Get list of endpoints.

:   

**GET /healthz**
:   Test if **slurmctld** loaded successfully.

:   

**GET /livez**
:   Test if **slurmctld** loaded successfully.

:   

**GET /readyz**
:   Test if **slurmctld** is ready to accept incoming RPCs.

:   

**GET /metrics/jobs**
:   Get job metrics.

:   

**GET /metrics/nodes**
:   Get node metrics.

:   

**GET /metrics/partitions**
:   Get partition metrics.

:   

**GET /metrics/scheduler**
:   Return scheduler metrics.

:   

**GET /metrics/jobs-users-accts**
:   Return user and account job metrics.

:   

[ ]{#lbAH}

## CORE FILE LOCATION

If slurmctld is started with the **-D** option then the core file will be written to the current working directory. Otherwise if **SlurmctldLogFile** is a fully qualified path name (starting with a slash), the core file will be written to the same directory as the log file, provided SlurmUser has write permission on the directory. Otherwise the core file will be written to the **StateSaveLocation**, or \"/var/tmp/\" as a last resort. If none of the above directories have write permission for SlurmUser, no core file will be produced.

[ ]{#lbAI}

## SIGNALS

**SIGTERM SIGINT SIGQUIT**
:   **slurmctld** will shutdown cleanly, saving its current state to the state save directory.

:   

**SIGABRT**
:   **slurmctld** will shutdown cleanly, saving its current state, and perform a core dump.

:   

**SIGHUP**
:   Reloads the slurm configuration files, similar to \'scontrol reconfigure\'.

:   

**SIGTSTP**
:   Stop the process from a terminal. This also stops slurmscriptd.

:   

**SIGUSR2**
:   Reread the log level from the configs, and then reopen the log file. This should be used when setting up **logrotate**(8).

:   

**SIGPROF**
:   Logs connection manager state when debug level is at least info.

:   

**SIGCHLD SIGUSR1 SIGXCPU SIGPIPE SIGALRM**
:   These signals are explicitly ignored.

:   

[ ]{#lbAJ}

## NOTES

It may be useful to experiment with different **slurmctld** specific configuration parameters using a distinct configuration file (e.g. timeouts). However, this special configuration file will not be used by the **slurmd** daemon or the Slurm programs, unless you specifically tell each of them to use it. If you desire changing communication ports, the location of the temporary file system, or other parameters used by other Slurm components, change the common configuration file, **slurm.conf**.

[ ]{#lbAK}

## COPYING

Copyright (C) 2002-2007 The Regents of the University of California. Copyright (C) 2008-2010 Lawrence Livermore National Security. Copyright (C) 2010-2022 SchedMD LLC. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER). CODE-OCEC-09-009. All rights reserved.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAL}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[slurmd](slurmd.md)**(8)

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

HTTP server

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
