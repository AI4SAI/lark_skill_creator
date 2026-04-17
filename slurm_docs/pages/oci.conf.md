# oci.conf

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

oci.conf - Slurm configuration file for containers.

[ ]{#lbAC}

## DESCRIPTION

Slurm supports calling OCI compliant runtimes. **oci.conf** is an ASCII file which defines parameters used by OCI runtime interface. The file will always be located in the same directory as the **slurm.conf**.

Parameter names are case insensitive. Any text following a \"#\" in the configuration file is treated as a comment through the end of that line. Changes to the configuration file take effect upon restart of Slurm daemons.

[ ]{#lbAD}

## PARAMETERS

The following oci.conf parameters are defined to control the behavior of the **\--container** argument of **salloc**, **srun**, and **sbatch**

**ContainerPath**
:   Specifies an override path pattern for placing the per-step spool directory. If this option is set, the resulting per-task OCI container bundle path will be created as a subdirectory of this path. Refer to the **OCI Pattern** section for details on pattern substitution.
    By default, an uniquely generated subdirectory for each step is created under **SlurmdSpoolDir**.

:   

**CreateEnvFile=(null\|newline\|disabled)**

:   Create environment file for container. File will have one environment variable per line if value is \"newline\". File will have each environment variable terminated by a NUL (aka \'\\0\') if value is \"null\". If value is \"disabled\", then the environment file will not be created.

    Value of \"true\" is treated as \"null\" for backwards compatibility. Value of \"false\" is treated as \"disabled\" for backwards compatibility.

    Note: When CreateEnvFile=newline, any environment variables with a newline will be dropped before writing to the environment file.

    Default is \"disabled\".

:   

**DebugFlags**
:   Override debug flags during container operations. See **debugflags** in **slurm.conf**.
    Default: (disabled)

:   

**DisableCleanup**
:   Disable removal of the generated files handed to OCI runtime.
    Default: false

:   

**DisableHooks**
:   Comma separated list of hook types to disable.
    Default: allow all hooks.

:   

**EnvExclude**

:   Extended regular expression to filter environment before. This allows for excluding variables to avoid unwanted environment variables inside of containers.

    Example: **EnvExclude**=\"\^(SLURM_CONF\|SLURM_CONF_SERVER)=\"

    Default does not exclude any environment variables.

:   

**MountSpoolDir**
:   Override pattern for path inside of container to mount **ContainerPath**. See the section **OCI Pattern** for details on pattern replacement.
    Default: see **ContainerPath**

:   

**RunTimeEnvExclude**

:   Extended regular expression to filter environment before calling any **RunTime\*** commands. This allows for excluding variables to avoid unwanted inheritance inside of the OCI runtimes.

    Example: **RunTimeEnvExclude**=\"\^(SLURM_CONF\|SLURM_CONF_SERVER)=\"

    Default is not exclude any environment variables.

:   

**FileDebug**
:   Override default file logging level during container operations. See **SlurmdDebug** in **slurm.conf**.
    Default: (disabled)

:   

**IgnoreFileConfigJson=(true\|false)**
:   Ignore the existence of config.json in OCI bundle path and disable loading config.json if it is present.
    Default is false.

:   

**RunTimeCreate**
:   Pattern for OCI runtime create operation. See the section **OCI Pattern** for details on pattern replacement.
    Default: (disabled)

:   

**RunTimeDelete**
:   Pattern for OCI runtime delete operation. See the section **OCI Pattern** for details on pattern replacement.
    Default: (disabled)

:   

**RunTimeKill**
:   Pattern for OCI runtime kill operation. See the section **OCI Pattern** for details on pattern replacement.
    Default: (disabled)

:   

**RunTimeQuery**
:   Pattern for OCI runtime query operation (also known as state). See the section **OCI Pattern** for details on pattern replacement.
    Default: (disabled)

:   

**RunTimeRun**
:   Pattern for OCI runtime run operation. This is not provided in the OCI runtime specification (\<=v1.0) but is provided by multiple OCI runtimes to simplify execution of containers. If provided, it will be used in the place of create and start operations. It avoids the need to poll state of the container resulting in less monitoring overhead. See the section **OCI Pattern** for details on pattern replacement.
    Default: (disabled)

:   

**RunTimeStart**
:   Pattern for OCI runtime start operation. See the section **OCI Pattern** for details on pattern replacement.
    Default: (disabled)

:   

**SrunPath**
:   Absolute path to srun executable.
    Default: (search PATH)

:   

**SrunArgs**
:   Additional arguments to pass to srun. Add one **SrunArgs** entry per argument.
    Default: (disabled)

:   

**StdIODebug**
:   Override default STDIO logging level during container operations. See **SlurmdDebug** in **slurm.conf**.
    Default: (disabled)

:   

**SyslogDebug**
:   Override default syslog logging level during container operations. See **SlurmdSyslogDebug** in **slurm.conf**.
    Default: (disabled)

:   

[ ]{#lbAE}

## NOTES

OCI container support is disabled if oci.conf does not exist. If disabled, any user passing **\--container** will be doing so in a purely advisor manner.

[ ]{#lbAF}

## OCI Pattern

All of the OCI patterns will replace the following characters:

**Replacements**:

**%%**
:   Replace as \"%\".

:   

**%@**
:   Replace as the command and arguments. Each argument will be enclosed with single quotes and escaped.

:   

**%b**
:   Replace as OCI Bundle Path.

:   

**%e**
:   Replace as path to file containing environment if **CreateEnvFile=true**.

:   

**%j**
:   Replace as numeric job id.

:   

**%m**
:   Replace with the per-step spool directory path of the container as patterned by **ContainerPath**. If **ContainerPath** is not set, this is replaced with a uniquely generated subdirectory under **SlurmdSpoolDir** as defined in **[slurm.conf](slurm.conf.md)**(5), or defaults to \"/var/spool/slurmd\".

:   

**%n**
:   Replace as nodename.

:   

**%p**
:   Replace as PID of first processes forked off. Only for use in **RunTimeKill** or **RunTimeDelete**.

:   

**%r**
:   Replace as original path to rootfs.

:   

**%s**
:   Replace as numeric step id.

:   

**%t**
:   Replace as numeric step task id.

:   

**%u**
:   Replace as user name.

:   

**%U**
:   Replace as numeric user id.

:   

[ ]{#lbAG}

## COPYING

Copyright (C) 2021 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAH}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

DESCRIPTION

:   

PARAMETERS

:   

NOTES

:   

OCI Pattern

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
