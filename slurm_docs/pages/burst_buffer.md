# Slurm Burst Buffer Guide

- Overview
- Configuration (for system administrators)
  - Common Configuration
  - Datawarp
  - Lua
- Lua Implementation (for system administrators)
  - How does burst_buffer.lua run?
  - Warnings
- Burst Buffer Resources
  - Datawarp
  - Lua
- Job Submission Commands
  - Datawarp
  - Lua
- Persistent Burst Buffer Creation and Deletion Directives
- Heterogeneous Job Support
- Command-line Job Options
  - Datawarp
  - Lua
- Symbol Replacement
- Status Commands
- Advanced Reservations
- Job Dependencies
- Burst Buffer States and Job States

## Overview

This guide explains how to use Slurm burst buffer plugins. Where appropriate, it explains how these plugins work in order to give guidance about how to best use these plugins.

The Slurm burst buffer plugins call a script at different points during the lifetime of a job:

1.  At job submission
2.  While the job is pending after an estimated start time is established. This is called \"stage-in.\"
3.  Once the job has been scheduled but has not started running yet. This is called \"pre-run.\"
4.  Once the job has completed or been cancelled, but Slurm has not released resources for the job yet. This is called \"stage-out.\"
5.  Once the job has completed, and Slurm has released resources for the job. This is called \"teardown.\"

This script runs on the slurmctld node. These are the supported plugins:

- datawarp
- lua

### Datawarp {#overview-dw}

This plugin provides hooks to Cray\'s Datawarp APIs. Datawarp implements burst buffers, which are a shared high-speed storage resource. Slurm provides support for allocating these resources, staging files in, scheduling compute nodes for jobs using these resources, and staging files out. Burst buffers can also be used as temporary storage during a job\'s lifetime, without file staging. Another typical use case is for persistent storage, not associated with any specific job.

### Lua {#overview-lua}

This plugin provides hooks to an API that is defined by a Lua script. This plugin was developed to provide system administrators with a way to do any task (not only file staging) at different points in a job\'s life cycle. These tasks might include file staging, node maintenance, or any other task that is desired to run during one or more of the five job states listed above.

The burst buffer APIs will only be called for a job that specifically requests using them. The Job Submission Commands section explains how a job can request using the burst buffer APIs.

## Configuration (for system administrators) {#configuration}

### Common Configuration {#common_config}

- To enable a burst buffer plugin, set `BurstBufferType` in slurm.conf. If it is not set, then no burst buffer plugin will be loaded. Only one burst buffer plugin may be specified.
- In slurm.conf, you may set `DebugFlags=BurstBuffer` for detailed logging from the burst buffer plugin. This will result in very verbose logging and is not intended for prolonged use in a production system, but this may be useful for debugging.
- [TRES limits](resource_limits.md) for burst buffers can be configured by association or QOS in the same way that TRES limits can be configured for nodes, CPUs, or any GRES. To make Slurm track burst buffer resources, add `bb/datawarp` (for the datawarp plugin) or `bb/lua` (for the lua plugin) to `AccountingStorageTres` in slurm.conf.
- The size of a job\'s burst buffer requirements can be used as a factor in setting the job priority as described in the [multifactor priority document](priority_multifactor.md). The Burst Buffer Resources section explains how these resources are defined.
- Burst-buffer-specific configurations can be set in burst_buffer.conf. Configuration settings include things like which users may use burst buffers, timeouts, paths to burst buffer scripts, etc. See the [burst_buffer.conf](burst_buffer.conf.md) manual for more information.
- The JSON-C library must be installed in order to build Slurm\'s `burst_buffer/datawarp` and `burst_buffer/lua` plugins, which must parse JSON format data. See Slurm\'s [JSON installation information](related_software.md#json) for details.

### Datawarp {#datawarp_config}

slurm.conf:

    BurstBufferType=burst_buffer/datawarp

The datawarp plugin calls two scripts:

- **dw_wlm_cli** - the Slurm burst_buffer/datawarp plugin calls this script to perform burst buffer functions. It should have been provided by Cray. The location of this script is defined by GetSysState in burst_buffer.conf. A template of this script is provided with Slurm:
  `src/plugins/burst_buffer/datawarp/dw_wlm_cli`
- **dwstat** - the Slurm burst_buffer/datawarp plugin calls this script to get status information. It should have been provided by Cray. The location of this script is defined by GetSysStatus in burst_buffer.conf. A template of this script is provided with Slurm:
  `src/plugins/burst_buffer/datawarp/dwstat`

### Lua {#lua_config}

slurm.conf:

    BurstBufferType=burst_buffer/lua

The lua plugin calls a single script which must be named burst_buffer.lua. This script needs to exist in the same directory as slurm.conf. The following functions are required to exist, although they may do nothing but return success:

- `slurm_bb_job_process`
- `slurm_bb_pools`
- `slurm_bb_job_teardown`
- `slurm_bb_setup`
- `slurm_bb_data_in`
- `slurm_bb_test_data_in`
- `slurm_bb_real_size`
- `slurm_bb_paths`
- `slurm_bb_pre_run`
- `slurm_bb_post_run`
- `slurm_bb_data_out`
- `slurm_bb_test_data_out`
- `slurm_bb_get_status`

A template of burst_buffer.lua is provided with Slurm: `etc/burst_buffer.lua.example`

This template documents many more details about the functions such as required parameters, when each function is called, return values for each function, and some simple examples.

## Lua Implementation

This purpose of this section is to provide additional information about the Lua plugin to help system administrators who desire to implement the Lua API. The most important points in this section are:

- Some functions in burst_buffer.lua must run quickly and cannot be killed; the remaining functions are allowed to run for as long as needed and can be killed.
- A maximum of 512 copies of burst_buffer.lua are allowed to run concurrently in order to avoid exceeding system limits.

### How does burst_buffer.lua run? {#burst_buffer_lua}

Lua scripts may either be run by themselves in a separate process via the `fork()` and `exec()` system calls, or they may be called via Lua\'s C API from within an existing process. One of the goals of the lua plugin was to avoid calling `fork()` from within slurmctld because it can severely harm performance of the slurmctld. The datawarp plugin calls `fork()` and `exec()` from slurmctld for every burst buffer API call, and this has been shown to severely harm slurmctld performance. Therefore, slurmctld calls burst_buffer.lua using Lua\'s C API instead of using `fork()`.

Some functions in burst_buffer.lua are allowed to run for a long time, but they may need to be killed if the job is cancelled, if slurmctld is restarted, or if they run for longer than the configured timeout in burst_buffer.conf. However, a call to a Lua script via Lua\'s C API cannot be killed from within the same process; only killing the entire process that called the Lua script can kill the Lua script.

To address this situation, burst_buffer.lua is called in two different ways:

- The `slurm_bb_job_process`, `slurm_bb_pools` and `slurm_bb_paths` functions are called from slurmctld. Because of the explanation above, a script running one of these functions cannot be killed. Since these functions are called while slurmctld holds some mutexes, it will be extremely harmful to slurmctld performance and responsiveness if they are slow. Because it is faster to call these functions directly than to call `fork()` to create a new process, this was deemed an acceptable tradeoff. As a result, *these functions cannot be killed*.
- The remaining functions in burst_buffer.lua are able to run longer without adverse effects. These need to be able to be killed. These functions are called from a lightweight Slurm daemon called slurmscriptd. Whenever one of these functions needs to run, slurmctld tells slurmscriptd to run that function; slurmscriptd then calls `fork()` to create a new process, then calls the appropriate function. This avoids calling `fork()` from slurmctld while still providing a way to kill running copies of burst_buffer.lua when needed. As a result, *these functions can be killed, and they will be killed if they run for longer than the appropriate timeout value as configured in burst_buffer.conf*.

The way in which each function is called is also documented in the burst_buffer.lua.example file.

### Warnings {#lua_warnings}

Do not install a signal handler in burst_buffer.lua because it is called directly from slurmctld. If slurmctld receives a signal, it could attempt to run the signal handler from burst_buffer.lua, even after a call to burst_buffer.lua is completed, which results in a crash.

## Burst Buffer Resources {#resources}

The burst buffer API may define burst buffer resource \"pools\" from which a job may request a certain amount of pool space. If a pool does not have sufficient space to fulfill a job\'s request, that job will remain pending until the pool does have enough space. Once the pool has enough space, Slurm may begin stage-in for the job. When stage-in begins, Slurm subtracts the job\'s requested space from the pool\'s available space. When teardown completes, Slurm adds the job\'s requested space back into the pool\'s available space. The Job Submission Commands section explains how a job may request space from a pool. Pool space is a scalar quantity.

### Datawarp {#datawarp_resources}

- Pools are defined by `dw_wlm_cli`, and represent bytes. This script prints a JSON-formatted string defining the pools to stdout.
- If a job does not request a pool, then the pool defined by `DefaultPool` in burst_buffer.conf will be used. If a job does not request a pool and `DefaultPool` is not defined, then the job will be rejected.

### Lua {#lua_resources}

- Pools are optional in this plugin, and can represent anything.
- `DefaultPool` in burst_buffer.conf is not used in this plugin.
- Pools are defined by burst_buffer.lua in the function `slurm_bb_pools`. If pools are not desired, then this function should just return `slurm.SUCCESS`. If pools are desired, then this function should return two values: (1) `slurm.SUCCESS`, and (2) a JSON-formatted string defining the pools. An example is provided in burst_buffer.lua.example. The current valid fields in the JSON string are:
  - **id** - a string defining the name of the pool
  - **quantity** - a number defining the amount of space in the pool
  - **granularity** - a number defining the lowest resolution of space that may be allocated from this pool. If a job does not request a number that is a multiple of granularity, then the job\'s request will be rounded up to the nearest multiple of granularity. For example, if granularity equals 1000, then the smallest amount of space that may be allocated from this pool for a single job is 1000. If a job requests less than 1000 units from this pool, then the job\'s request will be rounded up to 1000.

## Job Submission Commands {#submit}

The normal mode of operation is for batch jobs to specify burst buffer requirements within the batch script. Commented batch script lines containing a specific directive (depending on which plugin is being used) will inform Slurm that it should run the burst buffer stages for that job. These lines will also describe the burst buffer requirements for the job.

The salloc and srun commands can specify burst buffer requirements with the `--bb` and `--bbf` options. This is described in the Command-line Job Options section.

All burst buffer directives should be specified in comments at the top of the batch script. They may be placed before, after, or interspersed with any `#SBATCH` directives. All burst buffer stages happen at specific points in the job\'s life cycle, as described in the Overview section; they do not happen during the job\'s execution. For example, all of the persistent burst buffer (used only by the datawarp plugin) creations and deletions happen before the job\'s compute portion happens. In a similar fashion, you can\'t run stage-in at various points in the script execution; burst buffer stage-in is performed before the job begins and stage-out is performed after the job completes.

For both plugins, a job may request a certain amount of space (size or **capacity**) from a burst buffer resource **pool**.

- A **pool** specification is simply a string that matches the name of the pool. For example: `pool=pool1`
- A **capacity** specification is a number indicating the amount of space required from the pool. A **capacity** specification can include a suffix of \"N\" (nodes), \"K\|KiB\", \"M\|MiB\", \"G\|GiB\", \"T\|TiB\", \"P\|PiB\" (for powers of 1024) and \"KB\", \"MB\", \"GB\", \"TB\", \"PB\" (for powers of 1000). **NOTE**: Usually Slurm interprets KB, MB, GB, TB, PB, units as powers of 1024, but for Burst Buffers size specifications Slurm supports both IEC/SI formats. This is because the CRAY API supports both formats.

At job submission, Slurm performs basic directive validation and also runs a function in the burst buffer script. This function can perform validation of the directives used in the job script. If Slurm determines options are invalid, or if the burst buffer script returns an error, the job will be rejected and an error message will be returned directly to the user.

Note that unrecognized options may be ignored in order to support backward compatibility (i.e. a job submission would not fail in the case of an option recognized by some versions of Slurm, but not recognized by other versions). If the job is accepted, but later fails (e.g. some problem staging files), the job will be held and its \"Reason\" field will be set to an error message provided by the underlying infrastructure.

Users may also request to be notified by email upon completion of burst buffer stage out using the `--mail-type=stage_out` or `--mail-type=all` option. The subject line of the email will be of this form:

    SLURM Job_id=12 Name=my_app Staged Out, StageOut time 00:05:07

The following plugin subsections give additional information that is specific to each plugin and provide example job scripts. Command-line examples are given in the Command-line Job Options section.

### Datawarp {#submit_dw}

The directive of `#DW` (for \"DataWarp\") is used for burst buffer directives when using the `burst_buffer/datawarp` plugin. Please reference Cray documentation for details about the DataWarp options. For DataWarp systems, the directive of `#BB` can be used to create or delete persistent burst buffer storage.\
**NOTE**: The `#BB` directive is used since the command is interpreted by Slurm and not by the Cray Datawarp software. This is discussed more in the Persistent Burst Buffer section.

For job-specific burst buffers, it is required to specify a burst buffer **capacity**. If the job does not specify **capacity** then the job will be rejected. A job may also specify the pool from which it wants resources; if the job does not specify a pool, then the pool specified by DefaultPool in burst_buffer.conf will be used (if configured).

The following job script requests burst buffer resources from the default pool and requests files to be staged in and staged out:

    #!/bin/bash
    #DW jobdw type=scratch capacity=1GB access_mode=striped,private pfs=/scratch
    #DW stage_in type=file source=/tmp/a destination=/ss/file1
    #DW stage_out type=file destination=/tmp/b source=/ss/file1
    srun application.sh

### Lua {#submit_lua}

The default directive for this plugin is `#BB_LUA`. The directive used by this plugin may be changed by setting the **Directive** option in burst_buffer.conf. Since the directive must always begin with a `#` sign (which starts a comment in a shell script) this option should specify only the string following the `#` sign. For example, if burst_buffer.conf contains the following:

    Directive=BB_EXAMPLE

then the burst buffer directive will be `#BB_EXAMPLE`.

If the **Directive** option is not specified in burst_buffer.conf, then the default directive for this plugin (`#BB_LUA`) will be used.

Since this plugin was designed to be generic and flexible, this plugin only requires the directive to be given. If the directive is given, Slurm will run all burst buffer stages for the job.

Example of the minimum information required for all burst buffer stages to run for the job:

    #!/bin/bash
    #BB_LUA
    srun application.sh

Because burst buffer pools are optional for this plugin (see the Burst Buffer Resources section), a job is not required to specify a pool or capacity. If pools are provided by the burst buffer API, then a job may request a pool and capacity:

    #!/bin/bash
    #BB_LUA pool=pool1 capacity=1K
    srun application.sh

A job may choose whether or not to specify a pool. If a job does not specify a pool, then the job is still allowed to run and the burst buffer stages will still run for this job (as long as the burst buffer directive was given). If the job specifies a pool but that pool is not found, then the job is rejected.

The system administrator may validate burst buffer options in the `slurm_bb_job_process` function in burst_buffer.lua. This might include requiring a job to specify a pool or validating any additional options that the system administrator decides to implement.

## Persistent Burst Buffer Creation and Deletion Directives {#persist}

This section only applies to the datawarp plugin, since persistent burst buffers are not used in any other burst buffer plugin.

These options are used to create and delete persistent burst buffers:

- `#BB create_persistent name=<name> capacity=<number> [access=<access>] [pool=<pool> [type=<type>]`
- `#BB destroy_persistent name=<name> [hurry]`

Options for creating and deleting persistent burst buffers:

- **name** - The persistent burst buffer name may not start with a numeric value (numeric names are reserved for job-specific burst buffers).
- **capacity** - Described in the Job Submission Commands section.
- **pool** - Described in the Job Submission Commands section.
- **access** - The access parameter identifies the buffer access mode. Supported access modes for the datawarp plugin include:
  - striped
  - private
  - ldbalance
- **type** - The type parameter identifies the buffer type. Supported type modes for the datawarp plugin include:
  - cache
  - scratch

Multiple persistent burst buffers may be created or deleted within a single job.

Example - Creating two persistent burst buffers:

    #!/bin/bash
    #BB create_persistent name=alpha capacity=32GB access=striped type=scratch
    #BB create_persistent name=beta capacity=16GB access=striped type=scratch
    srun application.sh

Example - Destroying two persistent burst buffers:

    #!/bin/bash
    #BB destroy_persistent name=alpha
    #BB destroy_persistent name=beta
    srun application.sh

Persistent burst buffers can be created and deleted by a job requiring no compute resources. Submit a job with the desired burst buffer directives and specify a node count of zero (e.g. `sbatch -N0 setup_buffers.bash`). Attempts to submit a zero size job without burst buffer directives or with job-specific burst buffer directives will generate an error. Note that zero size jobs are not supported for job arrays or heterogeneous job allocations.

**NOTE**: The ability to create and destroy persistent burst buffers may be limited by the `Flags` option in the burst_buffer.conf file. See the [burst_buffer.conf](burst_buffer.conf.md) man page for more information. By default only [privileged users](user_permissions.md) (i.e. Slurm operators and administrators) can create or destroy persistent burst buffers.

## Heterogeneous Job Support {#het-job-support}

Heterogeneous jobs may request burst buffers. Burst buffer hooks will run once for each component that has burst buffer directives. For example, if a heterogeneous job has three components and two of them have burst buffer directives, the burst buffer hooks will run once for each of the two components with burst buffer directives, but not for the third component without burst buffer directives. Further information and examples can be found in the [heterogeneous jobs](heterogeneous_jobs.html#burst_buffer) page.

## Command-line Job Options {#command-line}

In addition to putting burst buffer directives in the batch script, the command-line options `--bb` and `--bbf` may also include burst buffer directives. These command-line options are available for salloc, sbatch, and srun. Note that the `--bb` option cannot create or destroy persistent burst buffers.

The `--bbf` option takes as an argument a filename and that file should contain a collection of burst buffer operations identical to those used for batch jobs.

Alternatively, the `--bb` option may be used to specify burst buffer directives as the option argument. The behavior of this option depends on which burst buffer plugin is used. When the `--bb` option is used, Slurm parses this option and creates a temporary burst buffer script file that is used internally by the burst buffer plugins.

### Datawarp {#command-line-dw}

When using the `--bb` option, the format of the directives can either be identical to those used in a batch script OR a very limited set of options can be used, which are translated to the equivalent script for later processing. The following options are allowed:

- `access=&ltaccess>`
- `capacity=&ltnumber>`
- `swap=&ltnumber>`
- `type=&lttype>`
- `pool=&ltname>`

Multiple options should be space separated. If a swap option is specified, the job must also specify the required node count.

Example:

    # Sample execute line:
    srun --bb="capacity=1G access=striped type=scratch" a.out

    # Equivalent script as generated by Slurm's burst_buffer/datawarp plugin
    #DW jobdw capacity=1GiB access_mode=striped type=scratch

### Lua {#command-line-lua}

This plugin does not do any special parsing or translating of burst buffer directives given by the `--bb` option. When using the `--bb` option, the format is identical to the batch script: Slurm only enforces that the burst buffer directive must be specified. See additional information in the Lua subsection of Job Submission Commands.

Example:

    # Sample execute line:
    srun --bb="#BB_LUA pool=pool1 capacity=1K"

    # Equivalent script as generated by Slurm's burst_buffer/lua plugin
    #BB_LUA pool=pool1 capacity=1K

## Symbol Replacement {#symbols}

Slurm supports a number of symbols that can be used to automatically fill in certain job details, e.g. to make stage-in or stage-out directory paths vary with each job submission.

Supported symbols include:

  ------ -------------------------------------
  %%     \%
  %A     Array Master Job Id
  %a     Array Task Id
  %d     Workdir
  %j     Job Id
  %u     User Name
  %x     Job Name
  \\\\   Stop further processing of the line
  ------ -------------------------------------

## Status Commands {#status}

Burst buffer information that Slurm tracks is available by using the `scontrol show burst` command or by using the sview command\'s Burst Buffer tab. Examples follow.

Datawarp plugin example:

    $ scontrol show burst
    Name=datawarp DefaultPool=wlm_pool Granularity=200GiB TotalSpace=5800GiB FreeSpace=4600GiB UsedSpace=1600GiB
      Flags=EmulateCray
      StageInTimeout=86400 StageOutTimeout=86400 ValidateTimeout=5 OtherTimeout=300
      GetSysState=/home/marshall/slurm/master/install/c1/sbin/dw_wlm_cli
      GetSysStatus=/home/marshall/slurm/master/install/c1/sbin/dwstat
      Allocated Buffers:
        JobID=169509 CreateTime=2021-08-11T10:19:06 Pool=wlm_pool Size=1200GiB State=allocated UserID=marshall(1017)
        JobID=169508 CreateTime=2021-08-11T10:18:46 Pool=wlm_pool Size=400GiB State=staged-in UserID=marshall(1017)
      Per User Buffer Use:
        UserID=marshall(1017) Used=1600GiB

Lua plugin example:

    $ scontrol show burst
    Name=lua DefaultPool=(null) Granularity=1 TotalSpace=0 FreeSpace=0 UsedSpace=0
      PoolName[0]=pool1 Granularity=1KiB TotalSpace=10000KiB FreeSpace=9750KiB UsedSpace=250KiB
      PoolName[1]=pool2 Granularity=2 TotalSpace=10 FreeSpace=10 UsedSpace=0
      PoolName[2]=pool3 Granularity=1 TotalSpace=4 FreeSpace=4 UsedSpace=0
      PoolName[3]=pool4 Granularity=1 TotalSpace=5GB FreeSpace=4GB UsedSpace=1GB
      Flags=DisablePersistent
      StageInTimeout=86400 StageOutTimeout=86400 ValidateTimeout=5 OtherTimeout=300
      GetSysState=(null)
      GetSysStatus=(null)
      Allocated Buffers:
        JobID=169504 CreateTime=2021-08-11T10:13:38 Pool=pool1 Size=250KiB State=allocated UserID=marshall(1017)
        JobID=169502 CreateTime=2021-08-11T10:12:06 Pool=pool4 Size=1GB State=allocated UserID=marshall(1017)
      Per User Buffer Use:
        UserID=marshall(1017) Used=1000256KB

Access to a burst buffer status API is available from scontrol using the `scontrol show bbstat ...` or `scontrol show dwstat ...` commands. Options following `bbstat` or `dwstat` on the scontrol execute line are passed directly to the bbstat or dwstat commands, as shown below. In the datawarp plugin, this command calls Cray\'s dwstat script. See Cray Datawarp documentation for details about dwstat options and output. In the lua plugin, this command calls the `slurm_bb_get_status` function in burst_buffer.lua.

Datawarp plugin example:

    /opt/cray/dws/default/bin/dwstat
    $ scontrol show dwstat
        pool units quantity    free gran'
    wlm_pool bytes  7.28TiB 7.28TiB 1GiB'

    $ scontrol show dwstat sessions
     sess state      token creator owner             created expiration nodes
      832 CA---  783000000  tester 12345 2015-09-08T16:20:36      never    20
      833 CA---  784100000  tester 12345 2015-09-08T16:21:36      never     1
      903 D---- 1875700000  tester 12345 2015-09-08T17:26:05      never     0

    $ scontrol show dwstat configurations
     conf state inst    type access_type activs
      715 CA---  753 scratch      stripe      1
      716 CA---  754 scratch      stripe      1
      759 D--T-  807 scratch      stripe      0
      760 CA---  808 scratch      stripe      1

A Lua plugin example can be found in the `slurm_bb_get_status` function in the `etc/burst_buffer.lua.example` file provided with Slurm.

## Advanced Reservations {#reservation}

Burst buffer resources can be placed in an advanced reservation using the *BurstBuffer* option. The argument consists of four elements:\
`[plugin:][pool:]#[units]`

**plugin** is the burst buffer plugin name, currently either \"datawarp\" or \"lua\".

**pool** specifies a burst buffer resource pool. If \"type\" is not specified, the number is a measure of storage space.

**\#** (meaning number) should be replaced with a positive integer.

**units** has the same format as the suffix of capacity in the Job Submission Commands section.

Jobs using this reservation are not restricted to these burst buffer resources, but may use these reserved resources plus any which are generally available. Some examples follow.

    $ scontrol create reservation starttime=now duration=60 \
      users=alan flags=any_nodes \
      burstbuffer=datawarp:100G

    $ scontrol create reservation StartTime=noon duration=60 \
      users=brenda NodeCnt=8 \
      BurstBuffer=datawarp:20G

    $ scontrol create reservation StartTime=16:00 duration=60 \
      users=joseph flags=any_nodes \
      BurstBuffer=datawarp:pool_test:4G

## Job Dependencies {#dependencies}

If two jobs use burst buffers and one is dependent on the other (e.g. `sbatch --dependency=afterok:123 ...`) then the second job will not begin until the first job completes and its burst buffer stage-out completes. If the second job does not use a burst buffer, but is dependent upon the first job\'s completion, then it will not wait for the stage-out operation of the first job to complete. The second job can be made to wait for the first job\'s stage-out operation to complete using the \"afterburstbuffer\" dependency option (e.g. `sbatch --dependency=afterburstbuffer:123 ...`).

## Burst Buffer States and Job States {#states}

These are the different possible burst buffer states:

- `pending`
- `allocating`
- `allocated`
- `deleting`
- `deleted`
- `staging-in`
- `staged-in`
- `pre-run`
- `alloc-revoke`
- `running`
- `suspended`
- `post-run`
- `staging-out`
- `teardown`
- `teardown-fail`
- `complete`

These states appear in the \"BurstBufferState\" field in the output of `scontrol show job`. This field only appears for jobs that requested a burst buffer. The states `allocating`, `allocated`, `deleting` and `deleted` are used for persistent burst buffers only (not for job-specific burst buffers). The state `alloc-revoke` happens if a failure in Slurm\'s select plugin occurs in between Slurm allocating resources for a job and actually starting the job. This should never happen.

When a job requests a burst buffer, this is what the job and burst buffer state transitions look like:

1.  Job is submitted. Job state and burst buffer state are both `pending`.
2.  Burst buffer stage-in starts. Job state: `pending` with reason: `BurstBufferStageIn`. Burst buffer state: `staging-in`.
3.  When stage-in completes, the job is eligible to be scheduled (barring any other limits). Job state: `pending`. Burst buffer state: `staged-in`.
4.  When the job is scheduled and allocated resources, the burst buffer pre-run stage begins. Job state: `running+configuring`. Burst buffer state: `pre-run`.
5.  When pre-run finishes, the `configuring` flag is cleared from the job and the job can actually start running. Job state and burst buffer state are both `running`.
6.  When the job completes (even if it fails), burst buffer stage-out starts. Job state: `stage-out`. Burst buffer state: `staging-out`.
7.  When stage-out completes, teardown starts. Job state: `complete`. Burst buffer state: `teardown`.

There are some situations which will change the state transitions. Examples include:

- Burst buffer operation failures:
  - If teardown fails, then the burst buffer state changes to teardown-fail. Teardown will be retried. For the burst_buffer/lua plugin, teardown will run a maximum of 3 times before giving up and destroying the burst buffer.
  - If either stage-in or stage-out fail and Flags=teardownFailure is configured in burst_buffer.conf, then teardown runs. Otherwise, the job is held and the burst buffer remains in the same state so it may be inspected and manually destroyed with `scancel --hurry`.
  - If pre-run fails, then the job is held and teardown runs.
- When a job is cancelled, the current burst buffer script for that job (if running) is killed. If `scancel --hurry` was used, or if the job never ran, stage-out is skipped and it goes straight to teardown. Otherwise, stage-out begins.
- If slurmctld is stopped, Slurm kills all running burst buffer scripts for all jobs and burst buffer state is saved for each job. When slurmctld restarts, for each job it reads the burst buffer state and does one of the following:
  - **Pending** - Do nothing, since no burst buffer scripts were killed.
  - **Staging-in, staged-in** - run teardown, wait for a short time, then restart stage-in.
  - **Pre-run** - Restart pre-run.
  - **Running** - Do nothing, since no burst buffer scripts were killed.
  - **Post-run, staging-out** - Restart post-run.
  - **Teardown, teardown-fail** - Restart teardown.

**NOTE**: There are many other things not listed here that affect the job state. This document focuses on burst buffers and does not attempt to address all possible job state transitions.
