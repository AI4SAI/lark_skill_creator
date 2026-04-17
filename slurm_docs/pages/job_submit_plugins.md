# [Job Submit Plugin API]{#top}

## Overview

This document describes Slurm job submit plugins and the API that defines them. It is intended as a resource to programmers wishing to write their own Slurm job submit plugins. This is version 100 of the API.

Slurm job submit plugins must conform to the Slurm Plugin API with the following specifications:

[const char plugin_name\[\]=\"*full text name*\"]{.commandline}

A free-formatted ASCII text string that identifies the plugin.

[const char plugin_type\[\]=\"*major/minor*\"]{.commandline}\

The major type must be \"job_submit.\" The minor type can be any suitable name for the type of job submission package. We include samples in the Slurm distribution for

- **all_partitions** --- Set default partition to all partitions on the cluster.
- **defaults** --- Set default values for job submission or modify requests.
- **logging** --- Log select job submission and modification parameters.
- **lua** --- Interface to http://www.lua.org/ scripts implementing these functions (actually a slight variation of them). Sample Lua scripts can be found with the Slurm distribution in the directory *contribs/lua*. The Lua script must be named \"job_submit.lua\" and must be located in the default configuration directory (typically the subdirectory \"etc\" of the installation directory). Slurmctld will fatal on startup if the configured lua script is invalid. Slurm will try to load the script for each job submission. If the script is broken or removed while slurmctld is running, Slurm will fallback to the previous working version of the script. **Warning**: slurmctld runs this script while holding internal locks, and only a single copy of this script can run at a time. This blocks most concurrency in slurmctld. Therefore, this script should run to completion as quickly as possible.
- **partition** --- Sets a job\'s default partition based upon job submission parameters and available partitions.
- **pbs** --- Translate PBS job submission options to Slurm equivalent (if possible).
- **require_timelimit** --- Force job submissions to specify a timelimit.

[const uint32_t plugin_version]{.commandline}\
If specified, identifies the version of Slurm used to build this plugin and any attempt to load the plugin from a different version of Slurm will result in an error. If not specified, then the plugin may be loaded by Slurm commands and daemons from any version, however this may result in difficult to diagnose failures due to changes in the arguments to plugin functions or changes in other Slurm functions used by the plugin.

Slurm can be configured to use multiple job_submit plugins if desired, however the lua plugin will only execute one lua script named \"job_submit.lua\" located in the default script directory (typically the subdirectory \"etc\" of the installation directory).

## API Functions {#api}

All of the following functions are required. Functions which are not implemented must be stubbed.

int init (void)

**Description**:\
Called when the plugin is loaded, before any other functions are called. Put global initialization here.

**Returns**:\
[SLURM_SUCCESS]{.commandline} on success, or\
[SLURM_ERROR]{.commandline} on failure.

void fini (void)

**Description**:\
Called when the plugin is removed. Clear any allocated storage here.

**Returns**: None.

**Note**: These init and fini functions are not the same as those described in the [dlopen (3)]{.commandline} system library. The C run-time system co-opts those symbols for its own initialization. The system [\_init()]{.commandline} is called before the Slurm [init()]{.commandline}, and the Slurm [fini()]{.commandline} is called before the system\'s [\_fini()]{.commandline}.

int job_submit(struct job_descriptor \*job_desc, uint32_t submit_uid, char \*\*error_msg)

**Description**:\
This function is called by the slurmctld daemon with the job submission parameters supplied by the user regardless of the command used (e.g. salloc, sbatch, slurmrestd). Only explicitly defined values will be represented. For values not defined at submit time [slurm.NO_VAL/16/64]{.commandline} or [nil]{.commandline} will be set. It can be used to log and/or modify the job parameters supplied by the user as desired. Note that this function has access to the slurmctld\'s global data structures, for example to examine the available partitions, reservations, etc.

**Arguments**:\
[job_desc]{.commandline} (input/output) the job allocation request specifications, before job defaults are set.\
[submit_uid]{.commandline} (input) user ID initiating the request.\
[error_msg]{.commandline} (output) If the argument is not null, then a plugin generated error message can be stored here. The error message is expected to have allocated memory which Slurm will release using the xfree function. The error message is always propagated to the caller, no matter the return code.\

**Returns**:\
[SLURM_SUCCESS]{.commandline} on success, or\
[SLURM_ERROR]{.commandline} on failure.

int job_modify(struct job_descriptor \*job_desc, job_record_t \*job_ptr, uint32_t modify_uid)

**Description**:\
This function is called by the slurmctld daemon with job modification parameters supplied by the user regardless of the command used (e.g. scontrol, sview, slurmrestd). It can be used to log and/or modify the job parameters supplied by the user as desired. Note that this function has access to the slurmctld\'s global data structures, for example to examine the available partitions, reservations, etc.

**Arguments**:\
[job_desc]{.commandline} (input/output) the job allocation request specifications, before job defaults are set.\
[job_ptr]{.commandline} (input/output) slurmctld daemon\'s current data structure for the job to be modified.\
[modify_uid]{.commandline} (input) user ID initiating the request.\

**Returns**:\
[SLURM_SUCCESS]{.commandline} on success, or\
[SLURM_ERROR]{.commandline} on failure.

## Lua Functions {#lua}

The Lua functions differ slightly from those implemented in C for better ease of use. Sample Lua scripts can be found with the Slurm distribution in the directory *contribs/lua*. The default installation location of the Lua scripts is the same location as the Slurm configuration file, *slurm.conf*. Reading and writing of job environment variables using Lua is possible by referencing the environment variables as a data structure containing named elements.

**NOTE**: Only sbatch sends the environment to slurmctld. salloc and srun do not send the environment to slurmctld, so *job_desc.environment* is not available in the job_submit plugin for these jobs.

For example:

    ...
        -- job_desc.environment is only available for batch jobs.
        if (job_desc.script) then
            if (job_desc.environment ~= nil) then
                if (job_desc.environment["FOO"] ~= nil) then
                    slurm.log_user("Found env FOO=%s",
                               job_desc.environment["FOO"])
                end
            end
        end
    ...

**NOTE**: To get/set the environment for all types of jobs, an alternate approach is to use [CliFilterPlugins](cli_filter_plugins.md).

int slurm_job_submit(job_desc_msg_t \*job_desc, List part_list, uint32_t submit_uid)

**Description**:\
This function is called by the slurmctld daemon with the job submission parameters supplied by the user regardless of the command used (e.g. salloc, sbatch, slurmrestd). Only explicitly defined values will be represented. For values not defined at submit time [slurm.NO_VAL/16/64]{.commandline} or [nil]{.commandline} will be set. It can be used to log and/or modify the job parameters supplied by the user as desired. Note that this function has access to the slurmctld\'s global data structures, for example to examine the available partitions, reservations, etc.

**Arguments**:\
[job_desc]{.commandline} (input/output) the job allocation request specifications.\
[part_list]{.commandline} (input) List of pointer to partitions which this user is authorized to use.\
[submit_uid]{.commandline} (input) user ID initiating the request.\
[]{#job_modify_returns}

**Returns**:\
[slurm.SUCCESS]{.commandline} --- Job submission accepted by plugin.\
[slurm.FAILURE]{.commandline} --- Job submission rejected due to error (Deprecated in 19.05).\
[slurm.ERROR]{.commandline} --- Job submission rejected due to error.\
[slurm.ESLURM\_\*]{.commandline} --- Job submission rejected due to error as defined by *slurm/slurm_errno.h* and *src/common/slurm_errno.c*.\

**NOTE**: As [job_desc]{.commandline} contains only user-specified values, undefined values can be recognized (before defaults are set) by either checking for [nil]{.commandline} or for the corresponding [slurm.NO_VAL/16/64]{.commandline}. This allows sites to apply policies, such as requiring users to define the number of nodes, as in the example below:

    ...
        -- Number of nodes must be defined at submit time
        if (job_desc.max_nodes == slurm.NO_VAL) then
            slurm.log_user("No max_nodes specified, please specify a number of nodes")
            return slurm.ERROR
        end
    ...

int slurm_job_modify(job_desc_msg_t \*job_desc, job_record_t \*job_ptr, List part_list, int modify_uid)

**Description**:\
This function is called by the slurmctld daemon with job modification parameters supplied by the user regardless of the command used (e.g. scontrol, sview, slurmrestd). It can be used to log and/or modify the job parameters supplied by the user as desired. Note that this function has access to the slurmctld\'s global data structures, for example to examine the available partitions, reservations, etc.

**Arguments**:\
[job_desc]{.commandline} (input/output) the job allocation request specifications.\
[job_ptr]{.commandline} (input/output) slurmctld daemon\'s current data structure for the job to be modified.\
[part_list]{.commandline} (input) List of pointer to partitions which this user is authorized to use.\
[modify_uid]{.commandline} (input) user ID initiating the request.\

**Returns**:\
Returns from job_modify() are the same as the returns from job_submit().

## Lua Job Attributes {#attr}

The available job attributes change occasionally with different versions of Slurm. To find the job attributes that are available for the version of Slurm you\'re using, go to the https://github.com/SchedMD/slurm. Navigate to **src/lua/slurm_lua.c** and look for function **slurm_lua_job_record_field()**, which contains the list of attributes available for the job_record (e.g. current record in Slurm). Navigate to **src/plugins/job_submit/lua/job_submit_lua.c** and look for function **\_get_job_req_field()**, which contains the list of attributes available for the job_descriptor (e.g. submission or modification request).

## Building

Generally using a LUA interface for a job submit plugin is best: It is simple to write and maintain with minimal dependencies upon the Slurm data structures. However using C does provide a mechanism to get more information than available using LUA including full access to all of the data structures and functions in the slurmctld daemon. The simplest way to build a C program would be to just replace one of the job submit plugins included in the Slurm distribution with your own code (i.e. use a patch with your own code). Then just build and install Slurm with that new code. Building a new plugin outside of the Slurm distribution is possible, but far more complex. It also requires access to a multitude of Slurm header files as shown in the procedure below.

1.  You will need to at least partly build Slurm first. The \"configure\" command must be executed in order to build the \"config.h\" file in the build directory.
2.  Create a local directory somewhere for your files to build with. Also create subdirectories named \".libs\" and \".deps\".
3.  Copy a \".deps/job_submit\_\*Plo\" file from another job_submit plugin\'s \".deps\" directory (made as part of the build process) into your local \".deps\" subdirectory. Rename the file as appropriate to reflect your plugins name (e.g. rename \"job_submit_partition.Plo\" to be something like \"job_submit_mine.Plo\").
4.  Compile and link your plugin. Those options might differ depending upon your build environment. Check the options used for building the other job_submit plugins and modify the example below as required.
5.  Install the plugin.

<!-- -->

    # Example:
    # The Slurm source is in ~/SLURM/slurm.git
    # The Slurm build directory is ~/SLURM/slurm.build
    # The plugin build is to take place in the directory
    #   "~/SLURM/my_submit"
    # The installation location is "/usr/local"

    # Build Slurm from ~/SLURM/slurm.build
    # (or at least run "~/SLURM/slurm.git/configure")

    # Set up your plugin files
    cd ~/SLURM
    mkdir my_submit
    cd my_submit
    mkdir .libs
    mkdir .deps
    # Create your plugin code
    vi job_submit_mine.c

    # Copy up a dependency file
    cp ~/SLURM/slurm.build/src/plugins/job_submit/partition/.deps/job_submit_partition.Plo \
       .deps/job_submit_mine.Plo

    # Compile
    gcc -DHAVE_CONFIG_H -I~/SLURM/slurm.build -I~/slurm.git \
       -g -O2 -pthread -fno-gcse -Werror -Wall -g -O0       \
       -fno-strict-aliasing -MT job_submit_mine.lo          \
       -MD -MP -MF .deps/job_submit_mine.Tpo                \
       -c job_submit_mine.c -o .libs/job_submit_mine.o

    # Some clean up
    mv -f .deps/job_submit_mine.Tpo .deps/job_submit_mine.Plo
    rm -fr .libs/job_submit_mine.a .libs/job_submit_mine.la \
       .libs/job_submit_mine.lai job_submit_mine.so

    # Link
    gcc -shared -fPIC -DPIC .libs/job_submit_mine.o -O2         \
       -pthread -O0 -pthread -Wl,-soname -Wl,job_submit_mine.so \
       -o job_submit_mine.so

    # Install
    cp job_submit_mine.so file \
       /usr/local/lib/slurm/job_submit_mine.so
