# namespace.yaml

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

namespace.yaml - Slurm configuration file for the namespace/linux plugin

[ ]{#lbAC}

## DESCRIPTION

**namespace.yaml** is a YAML-formatted configuration file that defines parameters used by Slurm\'s namespace/linux plugin. Based on these parameters, the plugin will create the appropriate job-specific namespace(s). The namespace/linux plugin can creates a filesystem namespace and will construct a private (or optionally shared) filesystem namespace and mount a list of directories (defaults to /tmp and /dev/shm) inside it, giving the job a private view of these directories. These paths are mounted inside the location specified by \'base_path\' in the **namespace.yaml** file. It also can create new User and PID namespaces for the job.

When the job completes, the namespace is unmounted and all files therein are automatically removed.

To make use of these plugins, \'PrologFlags=Contain\' must also be present in your **slurm.conf** file, as shown:

    NamespaceType=namespace/linux
    PrologFlags=Contain

The file will always be located in the same directory as the **slurm.conf**.

The file must be located in the same directory as **slurm.conf**. Any text following a \"#\" in this file is treated as a comment through the end of that line. Changes to the configuration file take effect upon restart of Slurm daemons.

[ ]{#lbAD}

## PARAMETERS

namespace.yaml contains the following attributes:

**defaults**
:   Default namespace configuration. If specified this contains the fields described in options.

:   

**disable_bpf_token**
:   If specified this disables the use of bpf tokens in the namespace plugin. Use of this option when ConstrainDevices is set in the cgroup.conf file will result in devices only being constrained at the job level, individual steps won\'t actually be constrained if requesting fewer devices than the job does. This will also permit ConstrainDevices to work on kernels where bpf tokens are not available.

:   

**node_confs**
:   List of node namespace configurations. The list element attributes are described below.

:   

[ ]{#lbAE}

### node_confs list element definitions

Each node_confs element contains the following attributes:

**nodes**
:   List of node names the options will be applied to.

:   

**options**
:   Namespace configuration options. Specified options will override those set by **defaults**.

:   

[ ]{#lbAF}

### options definitions

**options** contains the following attributes:

**auto_base_path**
:   This determines if plugin should create the BasePath directory or not. Set it to \'true\' if directory is not pre-created before slurm startup. If set to true, the directory is created with permission 0755. Directory is not deleted during slurm shutdown. If set to \'false\' or not specified, plugin would expect directory to exist. This option can be used on a global or per-line basis. This parameter is optional.

:   

**base_path**

:   Specify the *PATH* that the namespace plugin should use as a base to mount the private directories. This path must be readable and writable by the plugin. The plugin constructs a directory for each job inside this path, which is then used for mounting. The **base_path** gets mounted as \'private\' during slurmd start and remains mounted until shutdown. The first \"%h\" within the name is replaced with the hostname on which the **slurmd** is running. The first \"%n\" within the name is replaced with the Slurm node name on which the **slurmd** is running. Set *PATH* to \'none\' to disable the namespace/linux plugin on node subsets when there is a global setting in **defaults**.

    **NOTE**: The **base_path** must be unique to each node. If base_path is on a shared filesystem, you can use \"%h\" or \"%n\" to create node-unique directories.

    **NOTE**: The **base_path** parameter cannot be set to any of the paths specified by **dirs**. Using these directories will cause conflicts when trying to mount and unmount the private directories for the job.

:   

**clone_ns_script**
:   Specify fully qualified pathname of an optional initialization script. This script is run after the namespace construction of a job. This script will be provided the SLURM_NS environment variable containing the path to the namespace that can be used by the nsenter command. This variable will allow the script to join the newly created namespace and do further setup work. This parameter is optional.

:   

**clone_ns_script_wait**
:   The number of seconds to wait for the **clone_ns_script** to complete before considering the script failed. The default value is 10 seconds.

:   

**clone_ns_epilog**
:   Specify fully qualified pathname of an optional epilog script. This script runs just before the namespace is torn down. This script will be provided the SLURM_NS environment variable containing the path to the namespace that can be used by the nsenter command. This variable will allow the script to join the soon to be removed namespace and do any cleanup work. This parameter is optional.

:   

**clone_ns_epilog_wait**
:   The number of seconds to wait for the **clone_ns_epilog** to complete before considering the script failed. The default value is 10 seconds.

:   

**clone_ns_flags**
:   This contains a list of string flag values. This parameter defines what additional namespaces should be created for the job. Valid values are \"CLONE_NEWPID\" and \"CLONE_NEWUSER\" to create new PID and USER namespaces respectively. \"CLONE_NEWNS\" will also be accepted, but is always on. **NOTE**: When CLONE_NEWUSER is specified, bpf token support is also required if using ConstrainDevices in **cgroup.conf**.

:   

**dirs**

:   A comma-separated list of directories to create private mount points for. This parameter is optional and if not specified it defaults to \"/tmp,/dev/shm\".

    **NOTE**: /dev/shm has special handling, and instead of a bind mount is always a fresh tmpfs filesystem.

    **NOTE**: When CLONE_NEWPID is specified, a unique /proc filesystem for the container will be mounted automatically.

:   

**init_script**
:   Specify fully qualified pathname of an optional initialization script. This script is run before the namespace construction of a job. It can be used to make the job join additional namespaces prior to the construction of /tmp namespace or it can be used for any site-specific setup. This parameter is optional.

:   

**shared**
:   Specifying Shared=true will propagate new mounts between the job specific filesystem namespace and the root filesystem namespace, enable using autofs on the node. This parameter is optional.

:   

**user_ns_script**
:   Specifies the location of a script that will perform the user namespace setup. This script runs first when setting up the namespace. The environment variable \"SLURM_NS_PID\" is provided to allow constructing the path to the various map files that this script could write to. If not specified, every user and group will be mapped.

:   

[ ]{#lbAG}

## NOTES

If any parameters in namespace.yaml are changed while slurm is running, then slurmd on the respective nodes will need to be restarted for changes to take effect (scontrol reconfigure is not sufficient). Additionally this can be disruptive to jobs already running on the node. So care must be taken to make sure no jobs are running if any changes to job_container.conf are deployed.

Restarting slurmd is safe and non-disruptive to running jobs, as long as job_container.conf is not changed between restarts in which case above point applies.

[ ]{#lbAH}

## EXAMPLE

    ---
    defaults:
      auto_base_path: true
      base_path: "/var/nvme/storage_0"
      clone_ns_flags:
        - "CLONE_NEWPID"
        - "CLONE_NEWUSER"
        - "CLONE_NEWNS"
      clone_ns_epilog: "/path/to/epilog_script"
      clone_ns_epilog_wait: 10
      clone_ns_script: "/path/to/ns_script"
      init_script: "/path/to/init_script"
      shared: true
    node_confs:
      - nodes:
        - "n1"
        - "n[2-4,6]"
        options:
          auto_base_path: true
          base_path: "/var/nvme/storage_1"
          clone_ns_script_wait: 20
          dirs: "/tmp"
          shared: false
          user_ns_script: "/path/to/user_script"
      - nodes:
        - "n[7-10]"
        options:
          auto_base_path: true
          base_path: "/var/nvme/storage_2"
          init_script: "/etc/slurm/init.sh"

[ ]{#lbAI}

## COPYING

Copyright (C) 2025 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAJ}

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

    node_confs list element definitions

    :   

    options definitions

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
