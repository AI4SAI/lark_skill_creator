# Control Group in Slurm

## Contents

- Control Group Overview
- Slurm cgroup plugins design
- Use of cgroup in Slurm
- Slurm Cgroup Configuration Overview
- Currently Available Cgroup Plugins
  - proctrack/cgroup plugin
  - task/cgroup plugin
  - jobacct_gather/cgroup plugin
- Use of cgroup for Resource Specialization
- Slurm cgroup plugins
  - Main differences between cgroup/v1 and cgroup/v2
  - Main differences between controller interfaces
  - Other generalities

## Control Group Overview {#overview}

Control Group is a mechanism provided by the kernel to organize processes hierarchically and distribute system resources along the hierarchy in a controlled and configurable manner. Slurm can make use of cgroups to constrain different resources to jobs, steps and tasks, and to get accounting about these resources.

A cgroup provides different controllers (formerly \"subsystems\") for different resources. Slurm plugins can use several of these controllers, e.g.: *memory, cpu, devices, freezer, cpuset, cpuacct*. Each enabled controller gives the ability to constrain resources to a set of processes. If one controller is not available on the system, then Slurm cannot constrain the associated resources through a cgroup.

\"cgroup\" stands for \"control group\" and is never capitalized. The singular form is used to designate the whole feature and also as a qualifier as in \"cgroup controllers\". When explicitly referring to multiple individual control groups, the plural form \"cgroups\" is used.

Slurm supports two cgroup modes, Legacy mode (cgroup v1) and Unified Mode (cgroup v2). Hybrid mode where controllers from both version 1 and version 2 are mixed in a system is not supported.

**NOTE**: The cgroup/v1 plugin is deprecated and will not be supported in future Slurm versions. Newer GNU/Linux distributions are dropping, or have dropped, support for cgroup v1 and may even not provide kernel support for the required cgroup v1 interfaces. Systemd also deprecated cgroup v1. Starting with Slurm version 25.05, no new features will be added to cgroup v1. Support for critical bugs will be provided until its final removal.

See the kernel.org documentation for a more comprehensive description of cgroup:

- https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt
- https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html

## Slurm cgroup plugins design {#cgroup_design}

For extended information on Slurm\'s internal Cgroup plugin read:

- [cgroup/v2 plugin documentation](cgroup_v2.md)

## Use of cgroup in Slurm {#use}

Slurm provides cgroup versions of a number of plugins.

- proctrack/cgroup (for process tracking and management)
- task/cgroup (for constraining resources at step and task level)
- jobacct_gather/cgroup (for gathering statistics)

cgroups can also be used for resource specialization (constraining daemons to cores or memory).

## Slurm Cgroup Configuration Overview {#configuration}

There are several sets of configuration options for Slurm cgroups:

- [slurm.conf](slurm.conf.md) provides options to enable the cgroup plugins. Each plugin may be enabled or disabled independently of the others.
- [cgroup.conf](cgroup.conf.md) provides general options that are common to all cgroup plugins, plus additional options that apply only to specific plugins.
- System-level resource specialization is enabled using node configuration parameters.

## Currently Available Cgroup Plugins {#Plugins}

### proctrack/cgroup plugin {#proctrack}

The proctrack/cgroup plugin is an alternative to other proctrack plugins such as proctrack/linux for process tracking and suspend/resume capability.

proctrack/cgroup uses the freezer controller to keep track of all pids of a job. It basically stores the pids in a specific hierarchy in the cgroup tree and takes cares of signaling these pids when instructed. For example, if a user decides to cancel a job, Slurm will execute this order internally by calling the proctrack plugin and asking it to send a SIGTERM to the job. Since proctrack maintains a hierarchy of all Slurm-related pids in cgroup, it will easily know which ones will need to be signaled.\
Proctrack can also respond to queries for getting a list of all the pids of a job or a step.\
Alternatively, when using proctrack/linux, pids are stored by cgroup in a single file (cgroup.procs) which is read by the plugin to get all the pids of a part of the hierarchy. For example, when using proctrack/cgroup, a single step has its own cgroup.procs file, so getting the pids of the step is instantaneous. In proctrack/linux, we need to read recursively /proc to get all the descendants of a parent pid.

To enable this plugin, configure the following option in slurm.conf:

    ProctrackType=proctrack/cgroup

There are no specific options for this plugin in cgroup.conf, but the general options apply. See the [cgroup.conf](cgroup.conf.md) man page for details.

### task/cgroup plugin {#task}

The task/cgroup plugin allows constraining resources to a job, a step, or a task. This is the only plugin that can ensure that the boundaries of an allocation are not violated. Only jobacctgather/linux offers a very simplistic mechanism for constraining memory to a job but it is not reliable (there\'s a window of time where jobs can exceed its limits) and only for very rare systems where cgroup is not available.

task/cgroup provides the following features:

- Confine jobs and steps to their allocated cpuset.
- Confine jobs and steps to specific memory resources.
- Confine jobs, steps and tasks to their allocated gres, including gpus.

The task/cgroup plugin uses the cpuset, memory and devices subsystems.

To enable this plugin, add *task/cgroup* to the TaskPlugin configuration parameter in slurm.conf:

    TaskPlugin=task/cgroup

There are many specific options for this plugin in cgroup.conf. The general options also apply. See the [cgroup.conf](cgroup.conf.md) man page for details.

This plugin can be stacked with other task plugins, for example with *task/affinity*. This will allow it to constrain resources to a job plus getting the advantage of the affinity plugin (order doesn\'t matter):

    TaskPlugin=task/cgroup,task/affinity

### jobacct_gather/cgroup plugin {#jobacct_gather}

The *jobacct_gather/cgroup* plugin is an alternative to the *jobacct_gather/linux* plugin for the collection of accounting statistics for jobs, steps and tasks.\
*jobacct_gather/cgroup* uses the cpuacct and memory cgroup controllers.

The cpu and memory statistics collected by this plugin do not represent the same resources as the cpu and memory statistics collected by the *jobacct_gather/linux*. While the cgroup plugin just reads a cgroup.stats file and similar containing the information for the entire subtree of pids, the linux plugin gets information from /proc/pid/stat for every pid and then does the calculations, thus becoming a bit less efficient (thought not noticeable in the practice) than the cgroup one.

To enable this plugin, configure the following option in slurm.conf:

    JobacctGatherType=jobacct_gather/cgroup

There are no specific options for this plugin in cgroup.conf, but the general options apply. See the [cgroup.conf](cgroup.conf.md) man page for details.

## Use of cgroup for Resource Specialization {#Specialization}

Resource Specialization may be used to reserve a subset of cores or a specific amount of memory on each compute node for exclusive use by the Slurm compute node daemon, slurmd.

If cgroup/v1 is used the reserved resources will also be used by the slurmstepd processes. If cgroup/v2 is used, slurmstepd is not constrained by this resource specialization. Instead the slurmstepd is constrained to the resources allocated to the job, since it is considered part of the job and its consumption is completely dependent on the topology of the job. For example an MPI job can initialize many ranks with PMI and make slurmstepd consume more memory.

System-level resource specialization is enabled with special node configuration parameters. Read [slurm.conf](slurm.conf.md) and core specialization in [core_spec.html](core_spec.md) for more information.

## Slurm cgroup plugins {#cgroupplugins}

Both cgroup v1 and v2 plugins have very different ways of organizing their hierarchies and respond to different design constraints. The design is the responsibility of the kernel maintainers.

### Main differences between cgroup/v1 and cgroup/v2 {#differences}

The three main differences between v1 and v2 are:

- **Unified mode in v2**\

  In *cgroup/v1* there\'s a separate hierarchy for each controller, which means the job structure must be replicated and managed for every enabled controller. For example, for the same job, if using *memory* and *freezer* controllers, we will need to create the same slurm/uid/job_id/step_id/ hierarchy in both controller\'s directories. For example:

      /sys/fs/cgroup/memory/slurm/uid_1000/job_1/step_0/

      /sys/fs/cgroup/freezer/slurm/uid_1000/job_1/step_0/

  In *cgroup/v2* we have a *Unified* hierarchy, where controllers are enabled at the same level and presented to the user as different files.

      /sys/fs/cgroup/system.slice/slurmstepd.scope/job_1/step_0/

- **Top-down constraint in v2**\

  Resources are distributed top-down and a cgroup can further distribute a resource only if the resource has been distributed to it from the parent. Enabled controllers are listed in the *cgroup.controllers* file and enabled controllers in a subtree are listed in *cgroup.subtree_control*.

- **No-Internal-Process constraint in v2**\

  In *cgroup/v1* the hierarchy is free, which means one can create any directory in the tree and put pids in it. In *cgroup/v2* there\'s a kernel restriction which impedes adding a pid to non-leaf directories.

- **Systemd dependency on cgroup/v2 - separation of slurmd and stepds**

  This is not a kernel limitation but a systemd decision, which imposes an important restriction on services that decide to use *Delegate=yes*. Systemd, with pid 1, decided to be the complete owner of the cgroup hierarchy, */sys/fs/cgroup*, trying to impose a *single-writer* design. This means that everything related to cgroup must be under control of systemd. If one decides to manually modify the cgroup tree, creating directories and moving pids around, it is possible that at some point systemd may decide to enable or disable controllers on the entire tree, or move pids around. It\'s been experienced that a

      systemd reload

  or a

      systemd reset-failed

  removed controllers, at any level and directory of the tree, if there was not any \"systemd unit\" making use of it and there were not any \"Delegate=Yes\" started \"systemd unit\" on the system. This is because systemd wants to cleanup the cgroup tree and match it against its internal unit database. In fact, looking at the code of systemd one can see how cgroup directories related to units with \"Delegate=yes\" flag are ignored, while any other cgroup directories are modified. This makes it mandatory to start slurmd and slurmstepd processes under a unit with \"Delegate=yes\". This means we need to start, stop and restart slurmd with systemd. If we do that though, since we may have previously modified the tree where slurmd belongs (e.g. adding job directories) systemd will not be able to restart slurmd because of the *Top-down constraint* mentioned earlier. It will not be able to put the new slurmd pid into the root cgroup which is now a non-leaf. This forces us to separate the cgroup hierarchies of slurmstepd from the slurmd ones, and since we need to inform systemd about it and put slurmstepd into a new unit, we will do a dbus call to systemd to create a new scope for slurmstepds. See https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/ for more information.

The following differences shouldn\'t affect how other plugins interact with cgroup plugins, but instead they only show internal functional differences.

- A controller in *cgroup/v2* is enabled by writing to *cgroup.controllers*, while in *cgroup/v1* a new mount point must be mounted with filesystem type *\"-t cgroup\"* and corresponding options, e.g.*\"-o freezer\"*.
- In *cgroup/v2* the freezer controller is inherently present in the *cgroup.freeze* interface. In *cgroup/v1* it is a specific and separate controller which needs to be mounted.
- The devices controller does not exist in cgroup/v2, instead a new eBPF program must be inserted in the kernel.
- In *cgroup/v2*, memory.current is used to report RSS and memory.peak for MaxRSS. File cache (active_file and inactive_file fields from memory.stat) are counted unless *JobAcctGatherParam=no_file_cache* is set. If this option is enabled, MaxRSS is taken only from the periodic polling rather than *memory.peak*, so short memory spikes can be missed between *JobAcctGatherFrequency* intervals.
- In *cgroup/v2*, cpu.stat provides metrics in milis while puacct.stat in *cgroup/v1* provides metrics in USER_HZ.

### Main differences between controller interfaces {#interfaces}

  ----------------------------- ---------------------------------------
  [**cgroup/v1**]{.underline}   [**cgroup/v2**]{.underline}
  memory.limit_in_bytes         memory.max
  memory.soft_limit_in_bytes    memory.high
  memory.memsw_limit_in_bytes   memory.swap.max
  memory.swappiness             none
  freezer.state                 cgroup.freeze
  cpuset.cpus                   cpuset.cpus.effective and cpuset.cpus
  cpuset.mems                   cpuset.mems.effective and cpuset.mems
  cpuacct.stat                  cpu.stat
  device.\*                     ebpf program
  ----------------------------- ---------------------------------------

### Other generalities {#generalities}

- When using cgroup/v1, some configurations can exclude the swap cgroup accounting. This accounting is part of the features provided by the memory controller. If this feature is disabled from the kernel or boot parameters, trying to enable swap constraints will produce an error. If this is required, add the following parameters to the kernel command line:

      cgroup_enable=memory swapaccount=1

  This can usually be placed in /etc/default/grub inside the *GRUB_CMDLINE_LINUX* variable. A command such as *update-grub* must be run after updating the file. This feature can be disabled also at kernel config with the parameter:

      CONFIG_MEMCG_SWAP=

- In some Linux distributions, it was possible to use the systemd parameter JoinControllers, which is actually deprecated. This parameter allowed multiple controllers to be mounted in a single hierarchy in *cgroup/v1*, more or less trying to emulate the behavior of *cgroup/v2* in \"Unified\" mode. However, Slurm does not work correctly with this configuration, so please make sure your system.conf does not use JoinControllers and that all your cgroup controllers are under separate directories when using *cgroup/v1* legacy mode.
