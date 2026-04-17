# job_container.conf

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

job_container.conf - Slurm configuration file for namespace plugins

[ ]{#lbAC}

## DESCRIPTION

**job_container.conf** is an ASCII file which defines parameters used by Slurm\'s namespace/tmpfs plugin. Based on these parameters, the plugin will create the appropriate job-specifc namespace(s).

The namespace/tmpfs plugin creates a filesystem namespace and will construct a private (or optionally shared) filesystem namespace and mount a list of directories (defaults to /tmp and /dev/shm) inside it, giving the job a private view of these directories. These paths are mounted inside the location specified by \'BasePath\' in the **job_container.conf** file.

When the job completes, the namespace is unmounted and all files therein are automatically removed.

To make use of this plugin, \'PrologFlags=Contain\' must also be present in your **slurm.conf** file, as shown:

    NamespaceType=namespace/tmpfs
    PrologFlags=Contain

The file will always be located in the same directory as the **slurm.conf**.

If using the **job_container.conf** file to define a namespace available to nodes the first parameter on the line should be **NodeName**. If configuring a namespace without specifying nodes, the first parameter on the line should be **BasePath**.

Parameter names are case insensitive. Any text following a \"#\" in the configuration file is treated as a comment through the end of that line. Changes to the configuration file take effect upon restart of Slurm daemons.

The following job_container.conf parameters are defined to control the behavior of the namespace/tmpfs plugin.

**AutoBasePath**
:   This determines if plugin should create the BasePath directory or not. Set it to \'true\' if directory is not pre-created before slurm startup. If set to true, the directory is created with permission 0755. Directory is not deleted during slurm shutdown. If set to \'false\' or not specified, plugin would expect directory to exist. This option can be used on a global or per-line basis. This parameter is optional.

:   

**BasePath**

:   Specify the *PATH* that the tmpfs plugin should use as a base to mount the private directories. This path must be readable and writable by the plugin. The plugin constructs a directory for each job inside this path, which is then used for mounting. The **BasePath** gets mounted as \'private\' during slurmd start and remains mounted until shutdown. The first \"%h\" within the name is replaced with the hostname on which the **slurmd** is running. The first \"%n\" within the name is replaced with the Slurm node name on which the **slurmd** is running. Set *PATH* to \'none\' to disable the tmpfs plugin on node subsets when there is a global setting.

    **NOTE**: The **BasePath** must be unique to each node. If BasePath is on a shared filesystem, you can use \"%h\" or \"%n\" to create node-unique directories.

    **NOTE**: The **BasePath** parameter cannot be set to any of the paths specified by **Dirs**. Using these directories will cause conflicts when trying to mount and unmount the private directories for the job.

:   

**CloneNSScript**
:   Specify fully qualified pathname of an optional initialization script. This script is run after the namespace construction of a job. This script will be provided the SLURM_NS environment variable containing the path to the namespace that can be used by the nsenter command. This variable will allow the script to join the newly created namespace and do further setup work. This parameter is optional.

:   

**CloneNSScript_Wait**
:   The number of seconds to wait for the CloneNSScript to complete before considering the script failed. The default value is 10 seconds.

:   

**CloneNSEpilog**
:   Specify fully qualified pathname of an optional epilog script. This script runs just before the namespace is torn down. This script will be provided the SLURM_NS environment variable containing the path to the namespace that can be used by the nsenter command. This variable will allow the script to join the soon to be removed namespace and do any cleanup work. This parameter is optional.

:   

**CloneNSEpilog_Wait**
:   The number of seconds to wait for the CloneNSEpilog to complete before considering the script failed. The default value is 10 seconds.

:   

**EntireStepInNS**
:   Specifying EntireStepInNS=true will pivot all slurmstepd processes (excluding the external step, which is tasked with creating the namespace) into the constructed namespace. This will cause issues if certain paths such as SlurmdSpoolDir are inaccessible. This parameter is optional.

:   

**InitScript**
:   Specify fully qualified pathname of an optional initialization script. This script is run before the namespace construction of a job. It can be used to make the job join additional namespaces prior to the construction of /tmp namespace or it can be used for any site-specific setup. This parameter is optional.

:   

**NodeName**
:   A NodeName specification can be used to permit one job_container.conf file to be used for all compute nodes in a cluster by specifying the node(s) that each line should apply to. The NodeName specification can use a Slurm hostlist specification as shown in the example below. This parameter is optional.

:   

**Shared**
:   Specifying Shared=true will propagate new mounts between the job specific filesystem namespace and the root filesystem namespace, enable using autofs on the node. This parameter is optional.

:   

[ ]{#lbAD}

## NOTES

If any parameters in job_container.conf are changed while slurm is running, then slurmd on the respective nodes will need to be restarted for changes to take effect (scontrol reconfigure is not sufficient). Additionally this can be disruptive to jobs already running on the node. So care must be taken to make sure no jobs are running if any changes to job_container.conf are deployed.

Restarting slurmd is safe and non-disruptive to running jobs, as long as job_container.conf is not changed between restarts in which case above point applies.

[ ]{#lbAE}

## EXAMPLE

**/etc/slurm/slurm.conf**:
:   These are the entries required in **slurm.conf** to activate the namespace/tmpfs plugin.

:   NamespaceType=namespace/tmpfs
        PrologFlags=Contain

**/etc/slurm/job_container.conf**:

:   The first sample file will define 1 basepath for all nodes and it will be automatically created.

        AutoBasePath=true
        BasePath=/var/nvme/storage

    The second sample file will define 2 basepaths. The first will only be on largemem\[1-2\] and it will be automatically created. The second will only be on gpu\[1-10\], will be expected to exist and will run an initscript before each job.

        NodeName=largemem[1-2] AutoBasePath=true BasePath=/var/nvme/storage_a
        NodeName=gpu[1-10] BasePath=/var/nvme/storage_b InitScript=/etc/slurm/init.sh

    The third sample file will Define 1 basepath that will be on all nodes, automatically created, with /tmp and /var/tmp as private mounts.

        AutoBasePath=true
        BasePath=/var/nvme/storage Dirs=/tmp,/var/tmp

:   

[ ]{#lbAF}

## COPYING

Copyright (C) 2021 Regents of the University of California Produced at Lawrence Berkeley National Laboratory\
Copyright (C) 2021-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAG}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

DESCRIPTION

:   

NOTES

:   

EXAMPLE

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
