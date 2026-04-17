# [Slurm Programmer\'s Guide]{#top}

## Contents

- Overview
- Plugins
- Directory Structure
- Documentation
- Source Code
- Source Code Management
- Adding New Modules
- Compiling
- Configuration
- Test Suite
- Adding Files and Directories
- Tricks of the Trade

## Overview {#Overview}

Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. Components include machine status, partition management, job management, scheduling, and stream copy modules. Slurm requires no kernel modifications for it operation and is relatively self-contained.

Slurm is written in the C language and uses a GNU **autoconf** configuration engine. While initially written for Linux, other UNIX-like operating systems should be easy porting targets. Code should adhere to the https://www.kernel.org/doc/html/latest/process/coding-style.html. *(Some components of Slurm have been taken from various sources. Some of these components do not conform to the Linux kernel coding style. However, new code written for Slurm should follow these standards.)*

## Plugins {#Plugins}

To make the use of different infrastructures possible, Slurm uses a general purpose plugin mechanism. A Slurm plugin is a dynamically linked code object that is loaded explicitly at run time by the Slurm libraries. It provides a customized implementation of a well-defined API connected to tasks such as authentication, interconnect fabric, task scheduling, etc. A set of functions is defined for use by all of the different infrastructures of a particular variety. When a Slurm daemon is initiated, it reads the configuration file to determine which of the available plugins should be used. A [plugin developer\'s guide](plugins.md) is available with general information about plugins.

## Directory Structure {#Directory-Structure}

The contents of the Slurm directory structure will be described below in increasing detail as the structure is descended. The top level directory contains the scripts and tools required to build the entire Slurm system. It also contains a variety of subdirectories for each type of file.

General build tools/files include: **acinclude.m4**, **configure.ac**, **Makefile.am**, **Make-rpm.mk**, **META**, **README**, **slurm.spec.in**, and the contents of the **auxdir** directory. [autoconf]{.commandline} and [make]{.commandline} commands are used to build and install Slurm in an automated fashion. **NOTE**: [autoconf]{.commandline} version 2.52 or higher is required to build Slurm. Execute [autoconf -V]{.commandline} to check your version number. The build process is described in the README file.

Copyright and disclaimer information are in the files COPYING and DISCLAIMER. All of the top-level subdirectories are described below.

**auxdir** --- Used for building Slurm.\
**contribs** --- Various contributed tools.\
**doc** --- Documentation including man pages.\
**etc** --- Sample configuration files.\
**slurm** --- Header files for API use. These files must be installed. Placing these header files in this location makes for better code portability.\
**src** --- Contains all source code and header files not in the \"slurm\" subdirectory described above.\
**testsuite** --- Check, Expect and Pytest tests are here.

## Documentation {#Documentation}

All of the documentation is in the subdirectory **doc**. Two directories are of particular interest:

**doc/man** --- contains the man pages for the APIs, configuration file, commands, and daemons.\
**doc/html** --- contains the web pages.

## Source Code {#Source-Code}

Functions are divided into several categories, each in its own subdirectory. The details of each directory\'s contents are provided below. The directories are as follows:

**api** --- Application Program Interfaces into the Slurm code. Used to send and get Slurm information from the central manager. These are the functions user applications might utilize.\
**common** --- General purpose functions for widespread use throughout Slurm.\
**database** --- Various database files that support the accounting storage plugin.\
**plugins** --- Plugin functions for various infrastructures or optional behavior. A separate subdirectory is used for each plugin class:\

- **accounting_storage** for specifying the type of storage for accounting,\
- **auth** for user authentication,\
- **cred** for job credential functions,\
- **jobacct_gather** for job accounting,\
- **jobcomp** for job completion logging,\
- **mpi** for MPI support,\
- **priority** calculates job priority based on a number of factors including fair-share,\
- **proctrack** for process tracking,\
- **sched** for job scheduler,\
- **select** for a job\'s node selection,\
- **switch** for switch (interconnect) specific functions,\
- **task** for task affinity to processors,\
- **topology** methods for assigning nodes to jobs based on node topology.\

**sacct** --- User command to view accounting information about jobs.\
**sacctmgr** --- User and administrator tool to manage accounting.\
**salloc** --- User command to allocate resources for a job.\
**sattach** --- User command to attach standard input, output and error files to a running job or job step.\
**sbatch** --- User command to submit a batch job (script for later execution).\
**sbcast** --- User command to broadcast a file to all nodes associated with an existing Slurm job.\
**scancel** --- User command to cancel (or signal) a job or job step.\
**scontrol** --- Administrator tool to manage Slurm.\
**sinfo** --- User command to get information on Slurm nodes and partitions.\
**slurmctld** --- Slurm central manager daemon code.\
**slurmd** --- Slurm daemon code to manage the compute server nodes including the execution of user applications.\
**slurmdbd** --- Slurm database daemon managing access to the accounting storage database.\
**sprio** --- User command to see the breakdown of a job\'s priority calculation when the Multifactor Job Priority plugin is installed.\
**squeue** --- User command to get information on Slurm jobs and job steps.\
**sreport** --- User command to view various reports about past usage across the enterprise.\
**srun** --- User command to submit a job, get an allocation, and/or initiation a parallel job step.\
**sshare** --- User command to view shares and usage when the Multifactor Job Priority plugin is installed.\
**sstat** --- User command to view detailed statistics about running jobs when a Job Accounting Gather plugin is installed.\
**strigger** --- User and administrator tool to manage event triggers.\
**sview** --- User command to view and update node, partition, and job state information.\

## Source Code Management {#Source-Code-Management}

The latest code is in github: https://github.com/SchedMD/slurm. Creating your own branch will make it easier to keep it synchronized with our work.

## Adding New Modules {#Adding-New-Modules}

Add the new file name to the Makefile.am file in the appropriate directory. Then execute autoreconf (at the top level of the Slurm source directory). Note that a relatively current version of automake is required. The autoreconf program will build Makefile.in files from the Makefile.am files. If any new files need to be installed, update the slurm.spec file to identify the RPM in which the new files should be placed

If new directories need to be added, add to the configure.ac file the path to the Makefile to be built in the new directory. In summary:\
[autoreconf]{.underline} translates [.am]{.underline} files into [.in]{.underline} files\
[configure]{.underline} translates [.in]{.underline} files, adding paths and version numbers.

## Compiling {#Compiling}

Sending the standard output of \"make\" to a file makes it easier to see any warning or error messages:\
*\"make -j install \>make.out\"*

## Configuration {#Configuration}

Sample configuration files are included in the **etc** subdirectory. The **slurm.conf** can be built using a [configuration tool](configurator.md). See **doc/man/man5/slurm.conf.5** and the man pages for other configuration files for more details. **init.d.slurm** is a script that determines which Slurm daemon(s) should execute on any node based upon the configuration file contents. It will also manage these daemons: starting, signaling, restarting, and stopping them.

## Test Suite {#Test-Suite}

The **testsuite** files use Check, Expect and Pytest for testing Slurm in different ways.

The Check tests are designed to unit test C code. Only with *make check*, without Slurm installed, they will validate that key C functions work correctly.

We also have a set of Expect Slurm tests available under the **testsuite/expect** directory. These tests are executed after Slurm has been installed and the daemons initiated. These tests exercise all Slurm commands and options including stress tests. The file **testsuite/expect/globals** contains the Expect test framework for all of the individual tests. At the very least, you will need to set the *slurm_dir* variable to the correct value. To avoid conflicts with other developers, you can override variable settings in a separate file named **testsuite/expect/globals.local**.

Set your working directory to **testsuite/expect** before starting these tests. Tests may be executed individually by name (e.g. *test1.1*) or the full test suite may be executed with the single command *regression.py*. See **testsuite/expect/README** for more information.

Slurm also has a Pytest environment that can work like the Expect one, but it also works together with an external QA framework to improve the overall QA of Slurm.

## Adding Files and Directories {#Adding-Files-and-Directories}

If you are adding files and directories to Slurm, it will be necessary to re-build configuration files before executing the **configure** command. Update **Makefile.am** files as needed then execute **autoreconf** before executing **configure**.

## Tricks of the Trade {#Tricks-of-the-Trade}

### Multiple slurmd support {#multiple_slurmd_support}

It is possible to run multiple slurmd daemons on a single node, each using a different port number and NodeName alias. This is very useful for testing networking and protocol changes, or anytime you want to simulate a larger cluster than you really have. The author uses this on his desktop to simulate multiple nodes. However, it is important to note that not all slurm functions will work with multiple slurmd support enabled (e.g. many switch plugins will not work, it is best not to use any).

Multiple support is enabled at configure-time with the \"\--enable-multiple-slurmd\" parameter. This enables a new parameter in the slurm.conf file on the NodeName line, \"Port=\", and adds a new command line parameter to slurmd, \"-N\".

Each slurmd needs to have its own NodeName, and its own TCP port number. Here is an example of the NodeName lines for running three slurmd daemons on each of ten nodes:

    NodeName=foo[1-10] NodeHostname=host[1-10]  Port=17001
    NodeName=foo[11-20] NodeHostname=host[1-10] Port=17002
    NodeName=foo[21-30] NodeHostname=host[1-10] Port=17003

It is likely that you will also want to use the \"%n\" symbol in any slurmd related paths in the slurm.conf file, for instance SlurmdLogFile, SlurmdPidFile, and especially SlurmdSpoolDir. Each slurmd replaces the \"%n\" with its own NodeName. Here is an example:

    SlurmdLogFile=/var/log/slurm/slurmd.%n.log
    SlurmdPidFile=/var/run/slurmd.%n.pid
    SlurmdSpoolDir=/var/spool/slurmd.%n

You can manually start each slurmd daemon with the proper NodeName. For example, to start the slurmd daemons for host1 from the above slurm.conf example:

    host1> slurmd -N foo1
    host1> slurmd -N foo11
    host1> slurmd -N foo21

If you have SysV init scripts, slurmd daemons will automatically be started by whenever MULTIPLE_SLURMD is set to yes in /etc/sysconfig/slurm. If your distribution uses systemd, you may want to use templating feature to define one slurmd.service file and registering each of your virtual nodes within it, for example:

    [Unit]
    Description=Slurm node daemon
    After=network.target munge.service remote-fs.target
    ConditionPathExists=/etc/slurm.conf

    [Service]
    Type=forking
    EnvironmentFile=-/etc/sysconfig/slurmd
    ExecStart=/usr/sbin/slurmd -N%i $SLURMD_OPTIONS
    ExecReload=/bin/kill -HUP $MAINPID
    PIDFile=/var/run/slurmd-%i.pid
    KillMode=process
    LimitNOFILE=51200
    LimitMEMLOCK=infinity
    LimitSTACK=infinity
    Delegate=yes

    [Install]
    WantedBy=multi-user.target

Then, enabling/managing a service like this (what is *%i* in the file will be replaced by what is after the *@* in the command line):

    systemctl enable slurmd@nodeXYZ
    systemctl start/stop/restart slurmd@nodeXYZ
