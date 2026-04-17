# cgroup.conf

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

cgroup.conf - Slurm configuration file for the cgroup support

[ ]{#lbAC}

## DESCRIPTION

**cgroup.conf** is an ASCII file which defines parameters used by Slurm\'s Linux cgroup related plugins. The file will always be located in the same directory as the **slurm.conf**.

Parameter names are case insensitive. Any text following a \"#\" in the configuration file is treated as a comment through the end of that line. Changes to the configuration file take effect upon restart of Slurm daemons, daemon receipt of the SIGHUP signal, or execution of the command \"scontrol reconfigure\" unless otherwise noted.

For general Slurm cgroups information, see the Cgroups Guide at \<[https://slurm.schedmd.com/cgroups.html](cgroups.md)\>.

The following cgroup.conf parameters are defined to control the general behavior of Slurm cgroup plugins.

**CgroupMountpoint**=*PATH*
:   Only intended for development and testing. Specifies the *PATH* under which cgroup controllers should be mounted. The default *PATH* is /sys/fs/cgroup.

:   

**CgroupPlugin**=*\<cgroup/v1\|cgroup/v2\|autodetect\|disabled\>*
:   Specify the plugin to be used when interacting with the cgroup subsystem. Supported values are \"disabled\", to completely disable any interaction with the cgroups, \"cgroup/v1\" which supports the legacy interface of cgroup v1, \"cgroup/v2\" for the unified cgroup2 architecture, and \"autodetect\" which tries to determine which cgroup version does your system provide. \"autodetect\" is useful to have a single configuration in clusters where nodes can have different cgroup versions. The default value is \"autodetect\" on linux, otherwise the default is \"disabled\".
    NOTE: cgroup/v1 plugin is deprecated and no new features will be added to it. It is recommended that you switch to cgroup/v2 at your earliest convenience.

:   

**CgroupSlice**=*SLICE_NAME*
:   Start slurmd and the slurmstepd scope in the specified slice. If starting slurmd with systemd, you should also add the Slice= property under the \[Service\] section of slurmd.service file. Changing this parameter requires to stop all the slurmstepd scopes in the node and restart slurmd. Applies only to cgroup v2. The default is system.slice.

:   

**SystemdTimeout**=*\<number\>*
:   On slow systems like virtual machines or when systemd is busy, it can take a lot of time to initialize and prepare the scope for slurmd during startup. Slurm will wait a maximum of this amount of time (in milliseconds) for the scope to be ready before failing. Only applies to cgroup/v2. The default is 1000 ms.

:   

**IgnoreSystemd**=*\<yes\|no\>*
:   Only for cgroup/v2 and for development and testing. It will avoid any call to dbus and contact with systemd, and instead will prepare all the cgroup hierarchy manually. This option is dangerous in systems with systemd since the cgroup can be modified by systemd and cause issues to jobs.

:   

**IgnoreSystemdOnFailure**=*\<yes\|no\>*
:   Only for cgroup/v2 and for development and testing. It has similar functionality to **IgnoreSystemd** but only in the case that a dbus call does not succeed.

:   

**EnableControllers**=*\<yes\|no\>*
:   Only for cgroup/v2 and generally for development, testing, when running on old kernels and/or old systemd versions (e.g. RHEL8, systemd \< 244) where not all the controllers are enabled in the cgroup tree. With this parameter, slurmd gets the available controllers from root\'s cgroup.controllers file (**CgroupMountPoint**, by default /sys/fs/cgroup/cgroup.controllers) and makes them available in all levels of the cgroup tree until it reaches Slurm\'s cgroup leaf.

:   

**EnableExtraControllers**=*\<all\|controller1\[,controller2,\...\]\>*
:   This will enable extra controllers not natively used by Slurm in the job cgroup subtree. If combined with EnableControllers it will enable them in all the levels of the cgroup tree from the OS root cgroup. The controllers that can be enabled are io, pids, rdma, hugetlb and misc or all. If they do not exist in the system an error is logged. Only for cgroup/v2.

:   

[ ]{#lbAD}

## TASK/CGROUP PLUGIN

The following cgroup.conf parameters are defined to control the behavior of this particular plugin:

**AllowedRAMSpace**=\<number\>
:   Constrain the job/step cgroup RAM to this percentage of the allocated memory. The percentage supplied may be expressed as floating point number, e.g. 101.5. Sets the cgroup soft memory limit at the allocated memory size and then sets the job/step hard memory limit at the (AllowedRAMSpace/100) \* allocated memory. If the job/step exceeds the hard limit, then it might trigger Out Of Memory (OOM) events (including oom-kill) which will be logged to kernel log ring buffer (dmesg in Linux). Setting AllowedRAMSpace above 100 may cause system Out of Memory (OOM) events as it allows job/step to allocate more memory than configured to the nodes. Reducing configured node available memory to avoid system OOM events is suggested. Setting AllowedRAMSpace below 100 will result in jobs receiving less memory than allocated and soft memory limit will set to the same value as the hard limit. Also see **ConstrainRAMSpace**. The default value is 100.

:   

**AllowedSwapSpace**=\<number\>
:   Constrain the job cgroup swap space to this percentage of the allocated memory. The default value is 0, which means that RAM+Swap will be limited to **AllowedRAMSpace**. The supplied percentage may be expressed as a floating point number, e.g. 50.5. If the limit is exceeded, the job steps will be killed and a warning message will be written to standard error. Also see **ConstrainSwapSpace**. **NOTE**: Setting AllowedSwapSpace to 0 does not restrict the Linux kernel from using swap space. To control how the kernel uses swap space, see **MemorySwappiness**.

:   

**ConstrainCores**=\<yes\|no\>
:   If configured to \"yes\" then constrain allowed cores to the subset of allocated resources. This functionality makes use of the cpuset subsystem. Due to a bug fixed in version 1.11.5 of HWLOC, the task/affinity plugin may be required in addition to task/cgroup for this to function properly. The default value is \"no\".

:   

**ConstrainDevices**=\<yes\|no\>
:   If configured to \"yes\" then constrain the job\'s allowed devices based on GRES allocated resources. It uses the devices subsystem for that. The default value is \"no\".

:   

**ConstrainRAMSpace**=\<yes\|no\>

:   If configured to \"yes\" then constrain the job\'s RAM usage by setting the memory soft limit to the allocated memory and the hard limit to the allocated memory \* **AllowedRAMSpace**. The default value is \"no\", in which case the job\'s RAM limit will be set to its swap space limit if **ConstrainSwapSpace** is set to \"yes\". CR\_\*\_Memory must be set in slurm.conf for this parameter to take any effect. Also see **AllowedSwapSpace**, **AllowedRAMSpace** and **ConstrainSwapSpace**.

    **NOTE**: When using **ConstrainRAMSpace**, if the combined memory used by all processes in a step is greater than the limit, then the kernel will trigger an OOM event, killing one or more of the processes in the step. The step state will be marked as OOM, but the step itself will keep running and other processes in the step may continue to run as well. This differs from the behavior of **OverMemoryKill**, where the whole step will be killed/cancelled.

    **NOTE**: When enabled, ConstrainRAMSpace can lead to a noticeable decline in per-node job throughout. Sites with high-throughput requirements should carefully weigh the tradeoff between per-node throughput, versus potential problems that can arise from unconstrained memory usage on the node. See \<[https://slurm.schedmd.com/high_throughput.html](high_throughput.md)\> for further discussion.

:   

**ConstrainSwapSpace**=\<yes\|no\>
:   If configured to \"yes\" then constrain the job\'s swap space usage. The default value is \"no\". Note that when set to \"yes\" and ConstrainRAMSpace is set to \"no\", **AllowedRAMSpace** is automatically set to 100% in order to limit the RAM+Swap amount to 100% of job\'s requirement plus the percent of allowed swap space. This amount is thus set to both RAM and RAM+Swap limits. This means that in that particular case, ConstrainRAMSpace is automatically enabled with the same limit as the one used to constrain swap space. CR\_\*\_Memory must be set in slurm.conf for this parameter to take any effect. Also see **AllowedSwapSpace**.

:   

**MaxRAMPercent**=*PERCENT*
:   Set an upper bound in percent of total RAM (configured RealMemory of the node) on the RAM constraint for a job. This will be the memory constraint applied to jobs that are not explicitly allocated memory by Slurm (i.e. Slurm\'s select plugin is not configured to manage memory allocations). The *PERCENT* may be an arbitrary floating point number. The default value is 100.

:   

**MaxSwapPercent**=*PERCENT*
:   Set an upper bound (in percent of total RAM, configured RealMemory of the node) on the amount of RAM+Swap that may be used for a job. This will be the swap limit applied to jobs on systems where memory is not being explicitly allocated to job. The *PERCENT* may be an arbitrary floating point number between 0 and 100. The default value is 100.

:   

**MemorySwappiness**=\<number\>
:   Only for cgroup/v1. Configure the kernel\'s priority for swapping out anonymous pages (such as program data) verses file cache pages for the job cgroup. Valid values are between 0 and 100, inclusive. A value of 0 prevents the kernel from swapping out program data. A value of 100 gives equal priority to swapping out file cache or anonymous pages. If not set, then the kernel\'s default swappiness value will be used. **ConstrainSwapSpace** must be set to **yes** in order for this parameter to be applied.

:   

**MinRAMSpace**=\<number\>
:   Set a lower bound (in MB) on the memory limits defined by **AllowedRAMSpace** and **AllowedSwapSpace**. This prevents accidentally creating a memory cgroup with such a low limit that slurmstepd is immediately killed due to lack of RAM. If this happens, cleanup will not be performed and temporary files, sockets and directories can remain in the node. The default limit is 30M.

:   

[ ]{#lbAE}

## PROCTRACK/CGROUP PLUGIN

The following cgroup.conf parameters are defined to control the behavior of this particular plugin:

**SignalChildrenProcesses**=\<yes\|no\>
:   If configured to \"yes\", then send signals (for cancelling, suspending, resuming, etc.) to all children processes in a job/step. Otherwise, only send signals to the parent process of a job/step. The default setting is \"no\".

:   

[ ]{#lbAF}

## DISTRIBUTION-SPECIFIC NOTES

Debian and derivatives (e.g. Ubuntu) usually exclude the memory and memsw (swap) cgroups by default. To include them, add the following parameters to the kernel command line: **cgroup_enable=memory swapaccount=1**

This can usually be placed in /etc/default/grub inside the **GRUB_CMDLINE_LINUX** variable. A command such as update-grub must be run after updating the file.

[ ]{#lbAG}

## EXAMPLE

**/etc/slurm/cgroup.conf**:
:   This example cgroup.conf file shows a configuration that enables the more commonly used cgroup enforcement mechanisms.

:   ###
        # Slurm cgroup support configuration file.
        ###
        ConstrainCores=yes
        ConstrainDevices=yes
        ConstrainRAMSpace=yes
        ConstrainSwapSpace=yes

**/etc/slurm/slurm.conf**:
:   These are the entries required in **slurm.conf** to activate the cgroup enforcement mechanisms. Make sure that the node definitions in your **slurm.conf** closely match the configuration as shown by \"**slurmd -C**\". Either MemSpecLimit should be set or RealMemory should be defined with less than the actual amount of memory for a node to ensure that all system/non-job processes will have sufficient memory at all times. Sites should also configure **pam_slurm_adopt** to ensure users can not escape the cgroups via **ssh**.

:   ###
        # Slurm configuration entries for cgroups
        ###
        ProctrackType=proctrack/cgroup
        TaskPlugin=task/cgroup,task/affinity
        JobAcctGatherType=jobacct_gather/cgroup #optional for gathering metrics
        PrologFlags=Contain                     #X11 flag is also suggested

[ ]{#lbAH}

## COPYING

Copyright (C) 2010-2012 Lawrence Livermore National Security. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAI}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

DESCRIPTION

:   

TASK/CGROUP PLUGIN

:   

PROCTRACK/CGROUP PLUGIN

:   

DISTRIBUTION-SPECIFIC NOTES

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
