# Quick Start Administrator Guide

## Contents

- Overview
- Super Quick Start
- Building and Installing Slurm
  - Installing Prerequisites
  - Building RPMs
  - Building Debian Packages
  - Installing Packages
  - Building Manually
- Node Types
- High Availability
- Infrastructure
- Configuration
- Security
- Starting the Daemons
- Administration Examples
- Upgrades
- FreeBSD

## Overview

Please see the [Quick Start User Guide](quickstart.md) for a general overview.

Also see [Platforms](platforms.md) for a list of supported computer platforms.

For information on performing an upgrade, please see the [Upgrade Guide](upgrades.md).

## Super Quick Start {#quick_start}

1.  Make sure the clocks, users and groups (UIDs and GIDs) are synchronized across the cluster.
2.  Install https://dun.github.io/munge/ for authentication. Make sure that all nodes in your cluster have the same *munge.key*. Make sure the MUNGE daemon, *munged*, is started before you start the Slurm daemons.
3.  https://www.schedmd.com/download-slurm/ the latest version of Slurm.
4.  Install Slurm using one of the following methods:
    - Build RPM or DEB packages (recommended for production)
    - Build Manually from source (for developers or advanced users)
    - **NOTE**: Some Linux distributions may have **unofficial** Slurm packages available in software repositories. SchedMD does not maintain or recommend these packages.
5.  Build a configuration file using your favorite web browser and the [Slurm Configuration Tool](configurator.md).\
    **NOTE**: The *SlurmUser* must exist prior to starting Slurm and must exist on all nodes of the cluster.\
    **NOTE**: The parent directories for Slurm\'s log files, process ID files, state save directories, etc. are not created by Slurm. They must be created and made writable by *SlurmUser* as needed prior to starting Slurm daemons.\
    **NOTE**: If any parent directories are created during the installation process (for the executable files, libraries, etc.), those directories will have access rights equal to read/write/execute for everyone minus the umask value (e.g. umask=0022 generates directories with permissions of \"drwxr-r-x\" and mask=0000 generates directories with permissions of \"drwxrwrwx\" which is a security problem).
6.  Install the configuration file in *\<sysconfdir\>/slurm.conf*.\
    **NOTE**: You will need to install this configuration file on all nodes of the cluster.
7.  systemd (optional): enable the appropriate services on each system:
    - Controller: `systemctl enable slurmctld`
    - Database: `systemctl enable slurmdbd`
    - Compute Nodes: `systemctl enable slurmd`
8.  Start the *slurmctld* and *slurmd* daemons.

FreeBSD administrators should see the FreeBSD section below.

## Building and Installing Slurm {#build_install}

### Installing Prerequisites {#prereqs}

Before building Slurm, consider which plugins you will need for your installation. Which plugins are built can vary based on the libraries that are available when running the configure script. Refer to the below list of possible plugins and what is required to build them.

Note that in most cases, the required package is the corresponding development library, whose exact names may vary across different distributions. The typical naming convention on RHEL-based distros is **NAME-devel**, while the convention on Debian-based distros is **libNAME-dev**.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------
  **Component**                                                                                                                                                       **Development library required**

  `acct_gather_energy/ipmi`\                                                                                                                                          *freeipmi*
  Gathers [energy consumption](slurm.conf.md#OPT_AcctGatherEnergyType) through IPMI                                                                                   

  `acct_gather_interconnect/ofed`\                                                                                                                                    *libibmad*\
  Gathers [traffic data](slurm.conf.md#OPT_AcctGatherInterconnectType) for InfiniBand networks                                                                        *libibumad*

  `acct_gather_profile/hdf5`\                                                                                                                                         *hdf5*
  Gathers [detailed job profiling](slurm.conf.md#OPT_AcctGatherProfileType) through HDF5                                                                              

  `accounting_storage/mysql`\                                                                                                                                         *MySQL* or *MariaDB*
  Required for [accounting](accounting.md); a currently supported version of MySQL or MariaDB should be used                                                          

  `auth/slurm`\                                                                                                                                                       *jwt*
  (alternative to the traditional MUNGE [authentication method](slurm.conf.md#OPT_AuthType))                                                                          

  `auth/munge`\                                                                                                                                                       *MUNGE*
  (default [authentication method](slurm.conf.md#OPT_AuthType))                                                                                                       

  `AutoDetect=nvml`\                                                                                                                                                  *libnvidia-ml*
  Provides [autodetection](gres.conf.md#OPT_AutoDetect) of NVIDIA GPUs with MIGs and NVlinks (`AutoDetect=nvidia`, added in 24.11, does not have any prerequisites)   

  `AutoDetect=oneapi`\                                                                                                                                                *libvpl*
  Provides [autodetection](gres.conf.md#OPT_AutoDetect) of Intel GPUs                                                                                                 

  `AutoDetect=rsmi`\                                                                                                                                                  *ROCm*
  Provides [autodetection](gres.conf.md#OPT_AutoDetect) of AMD GPUs                                                                                                   

  **HTML man pages**\                                                                                                                                                 *man2html*
  This dependency is a command that must be present, typically provided by a package of the same name.                                                                

  **Lua API**                                                                                                                                                         *lua*

  **PAM support**                                                                                                                                                     *PAM*

  **PMIx support** (requires `--with-pmix` at build time)                                                                                                             *pmix*

  **Readline support** in `scontrol` and `sacctmgr` interactive modes                                                                                                 *readline*

  `slurmrestd`(restd node)                                                                                                                                            *[http_parser](related_software.md#httpparser)*\
                                                                                                                                                                      *[json-c](related_software.md#json)*\
                                                                                                                                                                      *[yaml](related_software.md#yaml)* (optional)\
                                                                                                                                                                      *[jwt](related_software.md#jwt)* (optional)\
                                                                                                                                                                      *[s2n](tls.md#s2n)* (optional)

  `sview` ([man page](sview.md))                                                                                                                                      *gtk+-2.0*

  `switch/hpe_slingshot`                                                                                                                                              *cray-libcxi*\
                                                                                                                                                                      *curl*\
                                                                                                                                                                      *json-c*

  NUMA support with `task/affinity`                                                                                                                                   *numa*

  `task/cgroup`\                                                                                                                                                      *hwloc*\
  Two packages packages are only required for cgroup/v2 support                                                                                                       *bpf* (cgroup/v2)\
                                                                                                                                                                      *dbus* (cgroup/v2)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------

\

Please see the [Related Software](related_software.md) page for references to required software to build these plugins.

If required libraries or header files are in non-standard locations, set `CFLAGS` and `LDFLAGS` environment variables accordingly.

### Building RPMs {#rpmbuild}

To build RPMs directly, copy the distributed tarball into a directory and execute (substituting the appropriate Slurm version number):\
`rpmbuild -ta slurm-23.02.7.tar.bz2`

The rpm files will be installed under the `$(HOME)/rpmbuild` directory of the user building them.

You can control some aspects of the RPM built with a *.rpmmacros* file in your home directory. **Special macro definitions will likely only be required if files are installed in unconventional locations.** A full list of *rpmbuild* options can be found near the top of the slurm.spec file. Some macro definitions that may be used in building Slurm include:

\_enable_debug
:   Specify if debugging logic within Slurm is to be enabled

\_prefix
:   Pathname of directory to contain the Slurm files

\_slurm_sysconfdir
:   Pathname of directory containing the slurm.conf configuration file (default /etc/slurm)

with_munge
:   Specifies the MUNGE (authentication library) installation location

An example .rpmmacros file:

    # .rpmmacros
    # Override some RPM macros from /usr/lib/rpm/macros
    # Set Slurm-specific macros for unconventional file locations
    #
    %_enable_debug     "--with-debug"
    %_prefix           /opt/slurm
    %_slurm_sysconfdir %{_prefix}/etc/slurm
    %_defaultdocdir    %{_prefix}/doc
    %with_munge        "--with-munge=/opt/munge"

### Building Debian Packages {#debuild}

Beginning with Slurm 23.11.0, Slurm includes the files required to build Debian packages. These packages conflict with the packages shipped with Debian based distributions, and are named distinctly to differentiate them. After downloading the desired version of Slurm, the following can be done to build the packages:

- Install basic Debian package build requirements:\
  `apt-get install build-essential fakeroot devscripts equivs`
- Unpack the distributed tarball:\
  `tar -xaf slurm*tar.bz2`
- `cd` to the directory containing the Slurm source
- Install the Slurm package dependencies:\
  `mk-build-deps -i debian/control`
- Build the Slurm packages:\
  `debuild -b -uc -us`

The packages will be in the parent directory after debuild completes.

### Installing Packages {#pkg_install}

The following packages are recommended to achieve basic functionality for the different node types. Other packages may be added to enable optional functionality:

  ------------------- ----------------------- ------- ------------ --------- -------
  **RPM name**        **DEB name**            Login   Controller   Compute   DBD
  `slurm`             `slurm-smd`             **X**   **X**        **X**     **X**
  `slurm-perlapi`     `slurm-smd-client`      **X**   **X**        **X**     
  `slurm-slurmctld`   `slurm-smd-slurmctld`           **X**                  
  `slurm-slurmd`      `slurm-smd-slurmd`                           **X**     
  `slurm-slurmdbd`    `slurm-smd-slurmdbd`                                   **X**
  ------------------- ----------------------- ------- ------------ --------- -------

\

#### Handling Dependencies {#dependencies}

The packages built as described above will have dependencies on external packages and on the general **slurm** package. However, we have observed gaps in the enforcement of these dependencies when using the low-level `dpkg` command. For this reason, we recommend avoiding low-level commands like `dpkg` and `rpm`, and instead using high-level commands like `dnf` and `apt` for all operations.

Users on Debian-based systems should also know that `apt` is willing to automatically remove Slurm packages due to dependency conflicts after the transaction. Always read through the transaction summary before instructing it to continue.

### Building Manually {#manual_build}

Instructions to build and install Slurm manually are shown below. This is significantly more complicated to manage than the RPM and DEB build procedures, so this approach is only recommended for developers or advanced users who are looking for a more customized install. See the README and INSTALL files in the source distribution for more details.

1.  Unpack the distributed tarball:\
    `tar -xaf slurm*tar.bz2`
2.  `cd` to the directory containing the Slurm source and type `./configure` with appropriate options (see below).
3.  Type `make install` to compile and install the programs, documentation, libraries, header files, etc.
4.  Type `ldconfig -n <library_location>` so that the Slurm libraries can be found by applications that intend to use Slurm APIs directly. The library location will be a subdirectory of PREFIX (described below) and depend upon the system type and configuration, typically lib or lib64. For example, if PREFIX is \"/usr\" and the subdirectory is \"lib64\" then you would find that a file named \"/usr/lib64/libslurm.so\" was installed and the command `ldconfig -n /usr/lib64` should be executed.

A full list of `configure` options will be returned by the command `configure --help`. The most commonly used arguments to the `configure` command include:

`--enable-debug`\
Enable additional debugging logic within Slurm.

`--prefix=`*`PREFIX`*\
Install architecture-independent files in PREFIX; default value is /usr/local.

`--sysconfdir=`*`DIR`*\
Specify location of Slurm configuration file. The default value is PREFIX/etc

## Node Types {#nodes}

A cluster consists of many different types of nodes that contribute to the overall functionality of the cluster. At least one compute node and controller node are required for an operational cluster. Other types of nodes can be added to enable optional functionality. It is recommended to have single-purpose nodes in a production cluster.

Most Slurm daemons should execute as a non-root service account. We recommend you create a Unix user named *slurm* for use by slurmctld and make sure it exists across the cluster. This user should be configured as the **SlurmUser** in the slurm.conf configuration file, and granted sufficient permissions to files used by the daemon. Refer to the [slurm.conf](slurm.conf.md#lbAP) man page for more details.

Below is a brief overview of the different types of nodes Slurm utilizes:

### Compute Node {#compute}

Compute nodes (frequently just referred to as \"nodes\") perform the computational work in the cluster. The [slurmd](slurmd.md) daemon executes on every compute node. It monitors all tasks running on the node, accepts work, launches tasks and kills running tasks upon request. Because slurmd initiates and manages user jobs, it must execute as the root user.

### Controller Node {#ctld}

The machine running [slurmctld](slurmctld.md) is sometimes referred to as the \"head node\" or the \"controller\". It orchestrates Slurm activities, including queuing of jobs, monitoring node states, and allocating resources to jobs. There is an optional backup controller that automatically assumes control in the event the primary controller fails (see the High Availability section below). The primary controller resumes control whenever it is restored to service. The controller saves its state to disk whenever there is a change in state (see \"StateSaveLocation\" in Configuration section below). This state can be recovered by the controller at startup time. State changes are saved so that jobs and other state information can be preserved when the controller moves (to or from a backup controller) or is restarted.

### DBD Node {#dbd}

If you want to save job accounting records to a database, the [slurmdbd](slurmdbd.md) (Slurm DataBase Daemon) should be used. It is good practice to run the slurmdbd daemon on a different machine than the controller. On larger systems, we also recommend that the database used by **slurmdbd** be on a separate machine. When getting started with Slurm, we recommend that you defer adding accounting support until after basic Slurm functionality is established on your system. Refer to the [Accounting](accounting.md) page for more information.

### Login Node {#login}

A login node, or submit host, is a shared system used to access a cluster. Users can use a login node to stage data, prepare their jobs for submission, submit those jobs once they are ready, check the status of their work, and perform other cluster related tasks. Workstations can be configured to be able to submit jobs, but having separate login nodes can be useful due to operating system compatibility or security implications. If users have root access on their local machine they would be able to access the security keys directly and could run jobs as root on the cluster.

Login nodes should have access to any Slurm client commands that users are expected to use. They should also have the cluster\'s \'slurm.conf\' file and other components necessary for the [authentication](authentication.md) method used in the cluster. They should not be configured to have jobs scheduled on them and users should not perform computationally demanding work on them while they\'re logged in. They do not typically need to have any Slurm daemons running. If using *auth/slurm*, [sackd](sackd.md) should be running to provide authentication. If running in [configless mode](configless_slurm.md), and not using *auth/slurm*, a [slurmd](slurmd.md) can be configured to manage your configuration files.

### Restd Node {#restd}

The [slurmrestd](slurmrestd.md) daemon can be deployed to provide a [REST API](rest.md) that can be used to interact with the Slurm cluster programmatically. See detailed [prerequisite](rest_quickstart.md#prereq), [installation](rest_quickstart.md#quick_start), and [systemd configuration](rest_quickstart.md#systemd) guides.

## High Availability {#HA}

Multiple SlurmctldHost entries can be configured, with any entry beyond the first being treated as a backup host. Any backup hosts configured should be on a different node than the node hosting the primary slurmctld. However, all hosts should mount a common file system containing the state information (see **StateSaveLocation** in the Configuration section below).

If more than one host is specified, when the primary fails the second listed SlurmctldHost will take over for it. When the primary returns to service, it notifies the backup. The backup then saves the state and returns to backup mode. The primary reads the saved state and resumes normal operation. Likewise, if both of the first two listed hosts fail the third SlurmctldHost will take over until the primary returns to service. Other than a brief period of non- responsiveness, the transition back and forth should go undetected. You can use [SlurmctldPrimaryOnProg](slurm.conf.md#OPT_SlurmctldPrimaryOnProg) and [SlurmctldPrimaryOffProg](slurm.conf.md#OPT_SlurmctldPrimaryOffProg) to define the actions taken when machines transition between primary and backup roles.

Any time the slurmctld daemon or hardware fails before state information reaches disk can result in lost state. Slurmctld writes state frequently (every five seconds by default), but with large numbers of jobs, the formatting and writing of records can take seconds and recent changes might not be written to disk. Another example is if the state information is written to file, but that information is cached in memory rather than written to disk when the node fails. The interval between state saves being written to disk can be configured at build time by defining SAVE_MAX_WAIT to a different value than five.

A backup instance of slurmdbd can also be configured by specifying [AccountingStorageBackupHost](slurm.conf.md#OPT_AccountingStorageBackupHost) in slurm.conf, as well as [DbdBackupHost](slurmdbd.conf.md#OPT_DbdBackupHost) in slurmdbd.conf. The backup host should be on a different machine than the one hosting the primary instance of slurmdbd. Both instances of slurmdbd should have access to the same database. The [network page](network.md#failover) has a visual representation of how this might look.

## Infrastructure

### User and Group Identification {#user_group}

There must be a uniform user and group name space (including UIDs and GIDs) across the cluster. It is not necessary to permit user logins to the control hosts (**SlurmctldHost**), but the users and groups must be resolvable on those hosts.

### Authentication of Slurm communications {#authentication}

All communications between Slurm components are authenticated. The authentication infrastructure is provided by a dynamically loaded plugin chosen at runtime via the **AuthType** keyword in the Slurm configuration file. Until 23.11.0, the only supported authentication type was https://dun.github.io/munge/, which requires the installation of the MUNGE package. When using MUNGE, all nodes in the cluster must be configured with the same *munge.key* file. The MUNGE daemon, *munged*, must also be started before Slurm daemons. Note that MUNGE does require clocks to be synchronized throughout the cluster, usually done by NTP.

As of 23.11.0, **AuthType** can also be set to [slurm](authentication.md#slurm), an internal authentication plugin. This plugin has similar requirements to MUNGE, requiring a key file shared to all Slurm daemons. The auth/slurm plugin requires installation of the jwt package.

MUNGE is currently the default and recommended option. The configure script in the top-level directory of this distribution will determine which authentication plugins may be built. The configuration file specifies which of the available plugins will be utilized.

### MPI support {#mpi}

Slurm supports many different MPI implementations. For more information, see [MPI](quickstart.md#mpi).

### Scheduler support {#scheduler}

Slurm can be configured with rather simple or quite sophisticated scheduling algorithms depending upon your needs and willingness to manage the configuration (much of which requires a database). The first configuration parameter of interest is **PriorityType** with two options available: *basic* (first-in-first-out) and *multifactor*. The *multifactor* plugin will assign a priority to jobs based upon a multitude of configuration parameters (age, size, fair-share allocation, etc.) and its details are beyond the scope of this document. See the [Multifactor Job Priority Plugin](priority_multifactor.md) document for details.

The **SchedType** configuration parameter controls how queued jobs are scheduled and several options are available.

- *builtin* will initiate jobs strictly in their priority order, typically (first-in-first-out)
- *backfill* will initiate a lower-priority job if doing so does not delay the expected initiation time of higher priority jobs; essentially using smaller jobs to fill holes in the resource allocation plan. Effective backfill scheduling does require users to specify job time limits.
- *gang* time-slices jobs in the same partition/queue and can be used to preempt jobs from lower-priority queues in order to execute jobs in higher priority queues.

For more information about scheduling options see [Gang Scheduling](gang_scheduling.md), [Preemption](preempt.md), [Resource Reservation Guide](reservations.md), [Resource Limits](resource_limits.md) and [Sharing Consumable Resources](cons_tres_share.md).

### Resource selection {#resource}

The resource selection mechanism used by Slurm is controlled by the **SelectType** configuration parameter. If you want to execute multiple jobs per node, but track and manage allocation of the processors, memory and other resources, the *cons_tres* (consumable trackable resources) plugin is recommended. For more information, please see [Consumable Resources in Slurm](cons_tres.md).

### Logging

Slurm uses syslog to record events if the `SlurmctldLogFile` and `SlurmdLogFile` locations are not set.

### Accounting

Slurm supports accounting records being written to a simple text file, directly to a database (MySQL or MariaDB), or to a daemon securely managing accounting data for multiple clusters. For more information see [Accounting](accounting.md).

### Compute node access {#node_access}

Slurm does not by itself limit access to allocated compute nodes, but it does provide mechanisms to accomplish this. There is a Pluggable Authentication Module (PAM) for restricting access to compute nodes available for download. When installed, the Slurm PAM module will prevent users from logging into any node that has not be assigned to that user. On job termination, any processes initiated by the user outside of Slurm\'s control may be killed using an *Epilog* script configured in *slurm.conf*.

## Configuration {#Config}

The Slurm configuration file includes a wide variety of parameters. This configuration file must be available on each node of the cluster and must have consistent contents. A full description of the parameters is included in the *slurm.conf* man page. Rather than duplicate that information, a minimal sample configuration file is shown below. Your slurm.conf file should define at least the configuration parameters defined in this sample and likely additional ones. Any text following a \"#\" is considered a comment. The keywords in the file are not case sensitive, although the argument typically is (e.g., \"SlurmUser=slurm\" might be specified as \"slurmuser=slurm\"). The control machine, like all other machine specifications, can include both the host name and the name used for communications. In this case, the host\'s name is \"mcri\" and the name \"emcri\" is used for communications. In this case \"emcri\" is the private management network interface for the host \"mcri\". Port numbers to be used for communications are specified as well as various timer values.

The *SlurmUser* must be created as needed prior to starting Slurm and must exist on all nodes in your cluster. The parent directories for Slurm\'s log files, process ID files, state save directories, etc. are not created by Slurm. They must be created and made writable by *SlurmUser* as needed prior to starting Slurm daemons.

The **StateSaveLocation** is used to store information about the current state of the cluster, including information about queued, running and recently completed jobs. The directory used should be on a low-latency local disk to prevent file system delays from affecting Slurm performance. If using a backup host, the StateSaveLocation should reside on a file system shared by the two hosts. We do not recommend using NFS to make the directory accessible to both hosts, but do recommend a shared mount that is accessible to the two controllers and allows low-latency reads and writes to the disk. If a controller comes up without access to the state information, queued and running jobs will be cancelled.

A description of the nodes and their grouping into partitions is required. A simple node range expression may optionally be used to specify ranges of nodes to avoid building a configuration file with large numbers of entries. The node range expression can contain one pair of square brackets with a sequence of comma separated numbers and/or ranges of numbers separated by a \"-\" (e.g. \"linux\[0-64,128\]\", or \"lx\[15,18,32-33\]\"). Up to two numeric ranges can be included in the expression (e.g. \"rack\[0-63\]\_blade\[0-41\]\"). If one or more numeric expressions are included, one of them must be at the end of the name (e.g. \"unit\[0-31\]rack\" is invalid), but arbitrary names can always be used in a comma separated list.

Node names can have up to three name specifications: **NodeName** is the name used by all Slurm tools when referring to the node, **NodeAddr** is the name or IP address Slurm uses to communicate with the node, and **NodeHostname** is the name returned by the command */bin/hostname -s*. Only **NodeName** is required (the others default to the same name), although supporting all three parameters provides complete control over naming and addressing the nodes. See the *slurm.conf* man page for details on all configuration parameters.

Nodes can be in more than one partition and each partition can have different constraints (permitted users, time limits, job size limits, etc.). Each partition can thus be considered a separate queue. Partition and node specifications use node range expressions to identify nodes in a concise fashion. This configuration file defines a 1154-node cluster for Slurm, but it might be used for a much larger cluster by just changing a few node range expressions. Specify the minimum processor count (CPUs), real memory space (RealMemory, megabytes), and temporary disk space (TmpDisk, megabytes) that a node should have to be considered available for use. Any node lacking these minimum configuration values will be considered DOWN and not scheduled. Note that a more extensive sample configuration file is provided in **etc/slurm.conf.example**. We also have a web-based [configuration tool](configurator.md) which can be used to build a simple configuration file, which can then be manually edited for more complex configurations.

    #
    # Sample /etc/slurm.conf for mcr.llnl.gov
    #
    SlurmctldHost=mcri(12.34.56.78)
    SlurmctldHost=mcrj(12.34.56.79)
    #
    AuthType=auth/munge
    Epilog=/usr/local/slurm/etc/epilog
    JobCompLoc=/var/tmp/jette/slurm.job.log
    JobCompType=jobcomp/filetxt
    PluginDir=/usr/local/slurm/lib/slurm
    Prolog=/usr/local/slurm/etc/prolog
    SchedulerType=sched/backfill
    SelectType=select/linear
    SlurmUser=slurm
    SlurmctldPort=7002
    SlurmctldTimeout=300
    SlurmdPort=7003
    SlurmdSpoolDir=/var/spool/slurmd.spool
    SlurmdTimeout=300
    StateSaveLocation=/var/spool/slurm.state
    TreeWidth=16
    #
    # Node Configurations
    #
    NodeName=DEFAULT CPUs=2 RealMemory=2000 TmpDisk=64000 State=UNKNOWN
    NodeName=mcr[0-1151] NodeAddr=emcr[0-1151]
    #
    # Partition Configurations
    #
    PartitionName=DEFAULT State=UP
    PartitionName=pdebug Nodes=mcr[0-191] MaxTime=30 MaxNodes=32 Default=YES
    PartitionName=pbatch Nodes=mcr[192-1151]

## Security

Besides authentication of Slurm communications based upon the value of the **AuthType**, digital signatures are used in job step credentials. This signature is used by *slurmctld* to construct a job step credential, which is sent to *srun* and then forwarded to *slurmd* to initiate job steps. This design offers improved performance by removing much of the job step initiation overhead from the *slurmctld* daemon. The digital signature mechanism is specified by the **CredType** configuration parameter and the default mechanism is MUNGE.

### Pluggable Authentication Module (PAM) support {#PAM}

A PAM module (Pluggable Authentication Module) is available for Slurm that can prevent a user from accessing a node which he has not been allocated, if that mode of operation is desired.

## Starting the Daemons {#starting_daemons}

For testing purposes you may want to start by just running slurmctld and slurmd on one node. By default, they execute in the background. Use the [-D]{.commandline} option for each daemon to execute them in the foreground and logging will be done to your terminal. The [-v]{.commandline} option will log events in more detail with more v\'s increasing the level of detail (e.g. [-vvvvvv]{.commandline}). You can use one window to execute \"*slurmctld -D -vvvvvv*\", a second window to execute \"*slurmd -D -vvvvv*\". You may see errors such as \"Connection refused\" or \"Node X not responding\" while one daemon is operative and the other is being started, but the daemons can be started in any order and proper communications will be established once both daemons complete initialization. You can use a third window to execute commands such as \"*srun -N1 /bin/hostname*\" to confirm functionality.

Another important option for the daemons is \"-c\" to clear previous state information. Without the \"-c\" option, the daemons will restore any previously saved state information: node state, job state, etc. With the \"-c\" option all previously running jobs will be purged and node state will be restored to the values specified in the configuration file. This means that a node configured down manually using the [scontrol]{.commandline} command will be returned to service unless noted as being down in the configuration file. In practice, Slurm consistently restarts with preservation.

## Administration Examples {#admin_examples}

[scontrol]{.commandline} can be used to print all system information and modify most of it. Only a few examples are shown below. Please see the scontrol man page for full details. The commands and options are all case insensitive.

Print detailed state of all jobs in the system.

    adev0: scontrol
    scontrol: show job
    JobId=475 UserId=bob(6885) Name=sleep JobState=COMPLETED
       Priority=4294901286 Partition=batch BatchFlag=0
       AllocNode:Sid=adevi:21432 TimeLimit=UNLIMITED
       StartTime=03/19-12:53:41 EndTime=03/19-12:53:59
       NodeList=adev8 NodeListIndecies=-1
       NumCPUs=0 MinNodes=0 OverSubscribe=0 Contiguous=0
       MinCPUs=0 MinMemory=0 Features=(null) MinTmpDisk=0
       ReqNodeList=(null) ReqNodeListIndecies=-1

    JobId=476 UserId=bob(6885) Name=sleep JobState=RUNNING
       Priority=4294901285 Partition=batch BatchFlag=0
       AllocNode:Sid=adevi:21432 TimeLimit=UNLIMITED
       StartTime=03/19-12:54:01 EndTime=NONE
       NodeList=adev8 NodeListIndecies=8,8,-1
       NumCPUs=0 MinNodes=0 OverSubscribe=0 Contiguous=0
       MinCPUs=0 MinMemory=0 Features=(null) MinTmpDisk=0
       ReqNodeList=(null) ReqNodeListIndecies=-1

Print the detailed state of job 477 and change its priority to zero. A priority of zero prevents a job from being initiated (it is held in \"pending\" state).

    adev0: scontrol
    scontrol: show job 477
    JobId=477 UserId=bob(6885) Name=sleep JobState=PENDING
       Priority=4294901286 Partition=batch BatchFlag=0
       more data removed....
    scontrol: update JobId=477 Priority=0

Print the state of node adev13 and drain it. To drain a node, specify a new state of DRAIN, DRAINED, or DRAINING. Slurm will automatically set it to the appropriate value of either DRAINING or DRAINED depending on whether the node is allocated or not. Return it to service later.

    adev0: scontrol
    scontrol: show node adev13
    NodeName=adev13 State=ALLOCATED CPUs=2 RealMemory=3448 TmpDisk=32000
       Weight=16 Partition=debug Features=(null)
    scontrol: update NodeName=adev13 State=DRAIN
    scontrol: show node adev13
    NodeName=adev13 State=DRAINING CPUs=2 RealMemory=3448 TmpDisk=32000
       Weight=16 Partition=debug Features=(null)
    scontrol: quit
    Later
    adev0: scontrol
    scontrol: show node adev13
    NodeName=adev13 State=DRAINED CPUs=2 RealMemory=3448 TmpDisk=32000
       Weight=16 Partition=debug Features=(null)
    scontrol: update NodeName=adev13 State=IDLE

Reconfigure all Slurm daemons on all nodes. This should be done after changing the Slurm configuration file.

    adev0: scontrol reconfig

Print the current Slurm configuration. This also reports if the primary and secondary controllers (slurmctld daemons) are responding. To just see the state of the controllers, use the command [ping]{.commandline}.

    adev0: scontrol show config
    Configuration data as of 2019-03-29T12:20:45
    ...
    SlurmctldAddr           = eadevi
    SlurmctldDebug          = info
    SlurmctldHost[0]        = adevi
    SlurmctldHost[1]        = adevj
    SlurmctldLogFile        = /var/log/slurmctld.log
    ...

    Slurmctld(primary) at adevi is UP
    Slurmctld(backup) at adevj is UP

Shutdown all Slurm daemons on all nodes.

    adev0: scontrol shutdown

## Upgrades {#upgrade}

Slurm supports in-place upgrades between certain versions. Important details about the steps necessary to perform an upgrade and the potential complications to prepare for are contained on this page: [Upgrade Guide](upgrades.md)

## FreeBSD {#FreeBSD}

FreeBSD administrators can install the latest stable Slurm as a binary package using:

    pkg install slurm-wlm

Or, it can be built and installed from source using:

    cd /usr/ports/sysutils/slurm-wlm && make install

The binary package installs a minimal Slurm configuration suitable for typical compute nodes. Installing from source allows the user to enable options such as mysql and gui tools via a configuration menu.
