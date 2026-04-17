# Slurm Version 25.11 Configuration Tool

This form can be used to create a Slurm configuration file with you controlling many of the important configuration parameters.

This is the full version of the Slurm configuration tool. This version has all the configuration options to create a Slurm configuration file. There is a simplified version of the Slurm configuration tool available at [configurator.easy.html](configurator.easy.md).

**This tool supports Slurm version 25.11 only.** Configuration files for other versions of Slurm should be built using the tool distributed with it in *doc/html/configurator.html*. Some parameters will be set to default values, but you can manually edit the resulting *slurm.conf* as desired for greater flexibility. See *man slurm.conf* for more details about the configuration parameters.

Note the while Slurm daemons create log files and other files as needed, it treats the lack of parent directories as a fatal error. This prevents the daemons from running if critical file systems are not mounted and will minimize the risk of cold-starting (starting without preserving jobs).

Note that this configuration file must be installed on all nodes in your cluster.

After you have filled in the fields of interest, use the \"Submit\" button on the bottom of the page to build the *slurm.conf* file. It will appear on your web browser. Save the file in text format as *slurm.conf* for use by Slurm.

For more information about Slurm, see [https://slurm.schedmd.com/slurm.html](slurm.md)

## Cluster Name

**ClusterName**: The name of your cluster. Using different names for each of your clusters is important when using a single database to record information from multiple Slurm-managed clusters.

## Control Machines

Define the hostname of the computer on which the Slurm controller and optional backup controller will execute. Hostname values should not be the fully qualified domain name (e.g. use *tux* rather than *tux.abc.com*).

**SlurmctldHost**: Primary Controller Hostname

**BackupController**: Backup Controller Hostname (optional)

## Compute Machines

Define the machines on which user applications can run. You can also specify addresses of these computers if desired (defaults to their hostnames). Only a few of the possible parameters associated with the nodes will be set by this tool, but many others are available. Executing the command *slurmd -C* on each compute node will print its physical configuration (sockets, cores, real memory size, etc.), which can be used in constructing the *slurm.conf* file. All of the nodes will be placed into a single partition (or queue) with global access. Many options are available to group nodes into partitions with a wide variety of configuration parameters. Manually edit the *slurm.conf* produced to exercise these options. Node names and addresses may be specified using a numeric range specification.

**NodeName**: Compute nodes

**NodeAddr**: Compute node addresses (optional)

**PartitionName**: Name of the one partition to be created

**MaxTime**: Maximum time limit of jobs in minutes or INFINITE

The following parameters describe a node\'s configuration. Set a value for **CPUs**. The other parameters are optional, but provide more control over scheduled resources:

**CPUs**: Count of processors on each compute node. If CPUs is omitted, it will be inferred from: Sockets, CoresPerSocket, and ThreadsPerCore.

**Sockets**: Number of physical processor sockets/chips on the node. If Sockets is omitted, it will be inferred from: CPUs, CoresPerSocket, and ThreadsPerCore.

**CoresPerSocket**: Number of cores in a single physical processor socket. The CoresPerSocket value describes physical cores, not the logical number of processors per socket.

**ThreadsPerCore**: Number of logical threads in a single physical core.

**RealMemory**: Amount of real memory. This parameter is required when specifying Memory as a consumable resource with the select/cons_tres plug-in. See below under Resource Selection.

## Slurm User

The Slurm controller (slurmctld) can run without elevated privileges, so it is recommended that a user \"slurm\" be created for it. For testing purposes any user name can be used.

**SlurmUser**

## Slurm Port Numbers

The Slurm controller (slurmctld) requires a unique port for communications as do the Slurm compute node daemons (slurmd). If not set, slurm ports are set by checking for an entry in */etc/services* and if that fails by using an interval default set at Slurm build time.

**SlurmctldPort**

**SlurmdPort**

## State Preservation

Define the location of a directory where the slurmctld daemon saves its state. This should be a fully qualified pathname which can be read and written to by the Slurm user on both the control machine and backup controller (if configured). The location of a directory where slurmd saves state should also be defined. This must be a unique directory on each compute server (local disk). The use of a highly reliable file system (e.g. RAID) is recommended.

**StateSaveLocation**: Slurmctld state save directory **Must be writable by all SlurmctldHost nodes**

**SlurmdSpoolDir**: Slurmd state save directory

Define when a non-responding (DOWN) node is returned to service.\
Select one value for **ReturnToService**:\
**0**: When explicitly restored to service by an administrator.\
**1**:Upon registration with a valid configuration only if it was set DOWN due to being non-responsive.\
**2**:Upon registration with a valid configuration.\

## Scheduling

Define the mechanism to be used for controlling job ordering.\
Select one value for **SchedulerType**:\
**Backfill**: FIFO with backfill\
**Builtin**: First-In First-Out (FIFO)\

## Interconnect

Define the node interconnect used.\
Select one value for **SwitchType**:\
**HPE Slingshot**: HPE Slingshot proprietary interconnect\
**None**: No special

## Default MPI Type

Specify the type of MPI to be used by default. Slurm will configure environment variables accordingly. Users can over-ride this specification with an srun option.\
Select one value for **MpiDefault**:\
**MPI-PMI2** (For PMI2-supporting MPI implementations)\
**MPI-PMIx** (Exascale PMI implementation)\
**None**: This works for most other MPI types.\

## Process Tracking

Define the algorithm used to identify which processes are associated with a given job. This is used signal, kill, and account for the processes associated with a job step.\
Select one value for **ProctrackType**:\
**Cgroup**: Use Linux *cgroup* to create a job container and track processes. Build a *cgroup.conf* file as well\
**LinuxProc**: Use parent process ID records, processes can escape from Slurm control\
**Pgid**: Use Unix Process Group ID, processes changing their process group ID can escape from Slurm control\

## Resource Selection

Define resource (node) selection algorithm to be used.\
Select one value for **SelectType**:\
**cons_tres**: Allocate individual processors, memory, GPUs, and other trackable resources\
**Linear**: Node-base resource allocation, does not manage individual processor allocation\

## Task Launch

Define a task launch plugin. This may be used to provide resource management within a node (e.g. pinning tasks to specific processors). Select one value for **TaskPlugin**:\

**None**: No task launch actions\

**Affinity**: CPU affinity support (see srun man pages for the \--cpu-bind, \--mem-bind, and -E options)\

**Cgroup**: Allocated resources constraints enforcement using Linux Control Groups (see cgroup.conf man page)

## Prolog and Epilog

**Prolog/Epilog**: Path that will be executed as root on every node of a user\'s job before the job\'s tasks will be initiated there and after that job has terminated. These parameters are optional.

**Prolog**

**Epilog**

**SrunProlog/Epilog**: Fully qualified path to be executed by srun at job step initiation and termination. These parameters may be overridden by srun\'s \--prolog and \--epilog options These parameters are optional.

**SrunProlog**

**SrunEpilog**

**TaskProlog/Epilog**: Fully qualified path to be executed as the user before each task begins execution and after each task terminates. These parameters are optional.

**TaskProlog**

**TaskEpilog**

## Event Logging

Slurmctld and slurmd daemons can each be configured with different levels of logging verbosity from 0 (quiet) to 7 (extremely verbose). Each may also be configured to use debug files. Use fully qualified pathnames for the files.

**SlurmctldDebug** (default is info)

**SlurmctldLogFile** (if empty, log goes to syslog)

**SlurmdDebug** (default is info)

**SlurmdLogFile** (if empty, log goes to syslog. String \"%h\" in name gets replaced with hostname)

## Job Completion Logging

Define the job completion logging mechanism to be used. Defaults to None. Select one value for **JobCompType**:\
**None**: No job completion logging\
**Elasticsearch**: Write job completion info to an Elasticsearch server\
**FileTxt**: Write job completion status to a text file\
**Kafka**: Write job completion info to a Kafka server\
**Lua**: Use a script called jobcomp.lua to log job completion\
**Script**: Use an arbitrary script to log job completion\
**MySQL**: Write completion status to a MySQL or MariaDB database\

**JobCompLoc**: This is the location of the text file to be written to (if JobCompType=filetxt), or the script to be run (if JobCompType=script), or the URL to the Elasticsearch server (if JobCompType=elasticsearch), or file containing librdkafka parameters (if JobCompType=jobcomp/kafka), database name (for other values of JobCompType).

**Options below are for use with a database to specify where the database is running and how to connect to it**\
**JobCompHost**: Host the database is running on for Job completion\
**JobCompPort**: Port the database server is listening on for Job completion\
**JobCompUser**: User we are to use to talk to the database for Job completion\
**JobCompParams**: Pass arbitrary text string to Job completion plugin\
**JobCompPass**: Password we are to use to talk to the database for Job completion\

## Job Accounting Gather

Slurm accounts for resource use per job. System specifics can be polled determined by system type\
Select one value for **JobAcctGatherType**:\
**None**: No job accounting\
**cgroup**: Specific Linux cgroup information gathered, use with Linux systems only\
**Linux**: Specific Linux process table information gathered, use with Linux systems only\
**JobAcctGatherFrequency**: polling interval in seconds. Zero disables periodic sampling.\

## Job Accounting Storage

Used with the Job Accounting Gather Slurm can store the accounting information in many different fashions. Fill in your systems choice here\
Select one value for **AccountingStorageType**:\
**None**: No job accounting storage\
**SlurmDBD**: Write job accounting to SlurmDBD (database daemon) which can securely save the data from many Slurm managed clusters into a common database\

**Options below are for use with a database to specify where the database is running and how to connect to it**\
**AccountingStorageHost**: Host the database is running on for Job Accounting\
**AccountingStoragePort**: Port the database server is listening on for Job Accounting\
**AccountingStoreFlags**: Comma separated list. Options are:\
\'job_comment\' - store the job comment field in the database;\
\'job_env\' - store a batch job\'s env in the database;\
\'job_extra\' - store a batch job\'s extra field in the database;\
\'job_script\' - store the job batch script in the database.\

## Process ID Logging

Define the location into which we can record the daemon\'s process ID. This is used for locate the appropriate daemon for signaling. Specify a specify the fully qualified pathname for the file.

**SlurmctldPidFile**

**SlurmdPidFile**

## Timers

Slurm has a variety of timers to control when to consider a node DOWN, when to purge job records, how long to give a job to gracefully terminate, etc.

**SlurmctldTimeout**: How many seconds the backup controller waits before becoming the active controller

**SlurmdTimeout**: How many seconds the Slurm controller waits for the slurmd to respond to a request before considering the node DOWN

**InactiveLimit**: How many seconds the Slurm controller waits for srun commands to respond before considering the job or job step inactive and terminating it. A value of zero indicates unlimited wait

**MinJobAge**: How many seconds the Slurm controller waits after a job terminates before purging its record. A record of the job will persist in job completion and/or accounting records indefinitely, but will no longer be visible with the squeue command after puring

**KillWait**: How many seconds a job is given to gracefully terminate after reaching its time limit and being sent SIGTERM before sending a SIGKILLL

**WaitTime**: How many seconds after a job step\'s first task terminates before terminating all remaining tasks. A value of zero indicates unlimited wait

\
\
