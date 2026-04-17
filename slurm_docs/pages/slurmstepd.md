# slurmstepd

Section: Slurm Component (8)\
Updated: Slurm Component\
Index

[ ]{#lbAB}

## NAME

slurmstepd - The job step manager for Slurm. [ ]{#lbAC}

## SYNOPSIS

**slurmstepd** [ ]{#lbAD}

## DESCRIPTION

**slurmstepd** is a job step manager for Slurm. It is spawned by the **slurmd** daemon when a job step is launched and terminates when the job step does. It is responsible for managing input and output (stdin, stdout and stderr) for the job step along with its accounting and signal processing. **slurmstepd** should not be initiated by users or system administrators.

[ ]{#lbAE}

## ENVIRONMENT VARIABLES:

The following environment variables can be used to override settings compiled into slurmstepd.

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for slurmstepd to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

[ ]{#lbAF}

## SIGNALS

**SIGINT SIGTERM SIGQUIT**
:   **slurmstepd** will shutdown cleanly.

:   

**SIGPROF**
:   Logs connection manager state when debug level is at least info.

:   

**SIGTSTP SIGPIPE SIGUSR1 SIGUSR2 SIGALRM SIGHUP**
:   These signals are explicitly ignored.

:   

[ ]{#lbAG}

## COPYING

Copyright (C) 2006 The Regents of the University of California. Copyright (C) 2010-2022 SchedMD LLC. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER). CODE-OCEC-09-009. All rights reserved.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. [ ]{#lbAH}

## SEE ALSO

**[slurmd](slurmd.md)**(8)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

SYNOPSIS

:   

DESCRIPTION

:   

ENVIRONMENT VARIABLES:

:   

SIGNALS

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
