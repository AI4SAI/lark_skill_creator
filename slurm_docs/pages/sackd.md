# sackd

Section: Slurm Auth and Cred Kiosk Daemon (8)\
Updated: Slurm Auth and Cred Kiosk Daemon\
Index

[ ]{#lbAB}

## NAME

sackd - Slurm Auth and Cred Kiosk Daemon.

[ ]{#lbAC}

## SYNOPSIS

**sackd** \[*OPTIONS*\...\]

[ ]{#lbAD}

## DESCRIPTION

**sackd** is the Slurm Auth and Cred Kiosk Daemon. It can be used on login nodes that are not running slurmd daemons to allow authentication to the cluster. The program will run as the *SlurmUser*. When running in Slurm\'s \"configless\" mode, in which case configuration files are retrieved and written under the /run/slurm/conf directory (unless **RUNTIME_DIRECTORY** is set).

[ ]{#lbAE}

## OPTIONS

**\--ca-cert-file \<file\>**
:   Absolute path to CA certificate used for fetching configuration when running configless in a TLS enabled cluster.

:   

**\--conf-server host\[:port\]**
:   Retrieve configs from slurmctld running at *host\[:port\]*. Requires slurmctld support provided by setting **enable_configless** in SlurmctldParameters.

:   

**-D**
:   Run **sackd** in the foreground with logging copied to stderr.

:   

**\--disable-reconfig**
:   Fetch configurations in configless mode once, but do not register with slurmctld for further reconfiguration updates.

:   

**-f config**
:   Read configuration from the specified file.

:   

**-h**
:   Help; print a brief summary of command options.

:   

**\--jwks-file \<file\>**
:   Read auth/slurm JWKS information from the specified file. Default value is slurm.jwks located in the same directory as slurm.conf.

:   

**\--key-file \<file\>**
:   Read auth/slurm authentication key from the specified file. Default value is slurm.key located in the same directory as slurm.conf.

:   

**\--port number**
:   Port socket number to listen for reconfiguration updates. This can be useful when multiple sackds co-exist on the same login node. The default value is **SlurmdPort**.

:   

**\--systemd**
:   To be used when started from a systemd unit file.

:   

**-v**
:   Verbose mode. Multiple -v\'s increase verbosity.

:   

[ ]{#lbAF}

## ENVIRONMENT VARIABLES

The following environment variables can be used to override settings compiled into sackd.

**ABORT_ON_FATAL**
:   When a fatal error is detected, use abort() instead of exit() to terminate the process. This allows backtraces to be captured without recompiling Slurm.

:   

**RUNTIME_DIRECTORY**

:   Absolute path governing the location for both the configuration cache sackd maintains, and the sack.socket unix socket used to provide authentication services.

    If multiple sackds need to be started on the same login node, the **RuntimeDirectory** systemd unit option should be set to **slurm-\<clustername\>**. Systemd v240+ automatically sets **RUNTIME_DIRECTORY** to **/run/\$RuntimeDirectory** for each sackd service, otherwise it requires manual setting (i.e. via **EnvironmentFile** unit option).

    If this is not set, the default value is **/run/slurm/**.

:   

**SACKD_DEBUG**
:   Set debug level explicitly for syslog and stderr. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5).

:   

**SACKD_DISABLE_RECONFIG**
:   Same as **\--disable-reconfig**.

:   

**SACKD_PORT**
:   Same as **\--port**.

:   

**SACKD_STDERR_DEBUG**
:   Set debug level explicitly for stderr. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5).

:   

**SACKD_SYSLOG_DEBUG**
:   Set debug level explicitly for syslog. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5).

:   

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for sackd to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

[ ]{#lbAG}

## SIGNALS

**SIGINT**
:   **sackd** will shutdown cleanly.

:   

**SIGHUP**
:   **sackd** will reconfigure.

:   

**SIGUSR2 SIGPIPE**
:   This signal is explicitly ignored.

:   

[ ]{#lbAH}

## COPYING

Copyright (C) SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAI}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[slurmctld](slurmctld.md)**(8)

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

SIGNALS

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
