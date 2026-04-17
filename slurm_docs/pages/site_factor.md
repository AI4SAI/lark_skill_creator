# [Slurm Priority Site Factor Plugin API]{#top}

## Overview

This document describes Slurm site_factor plugins and the API that defines them. It is intended as a resource to programmers wishing to write their own Slurm site_factor plugins.

Slurm site_factor plugins are Slurm plugins that implement the Slurm site_factor API described herein. They are designed to provide the site a way to build a custom [multifactor priority](priority_multifactor.md) factor, and will only be loaded and operated alongside [PriorityType=priority/multifactor]{.commandline}.

The plugins are meant to set and update the [site_factor]{.commandline} value in the [job_record_t]{.commandline} corresponding to a given job. Note that the [site_factor]{.commandline} itself is an unsigned integer, but uses [NICE_OFFSET]{.commandline} as an offset to allow the value to be positive or negative. The plugin itself must add [NICE_OFFSET]{.commandline} to the value stored to [site_factor]{.commandline} for proper operation, otherwise the value itself will be extremely negative, and the job priority will likely drop to 1. (The lowest value that does not correspond to a held job.)

Plugins must conform to the Slurm Plugin API with the following specifications:

[const char plugin_type\[\]=\"*major/minor*\"]{.commandline}\
The major type must be \"site_factor\" The minor type can be any recognizable abbreviation for the specific plugin.

[const char plugin_name\[\]]{.commandline}\
Some descriptive name for the plugin. There is no requirement with respect to its format.

[const uint32_t plugin_version]{.commandline}\
If specified, identifies the version of Slurm used to build this plugin and any attempt to load the plugin from a different version of Slurm will result in an error. If not specified, then the plugin may be loaded by Slurm commands and daemons from any version, however this may result in difficult to diagnose failures due to changes in the arguments to plugin functions or changes in other Slurm functions used by the plugin.

## API Functions {#api}

The following functions must appear. Functions which are not implemented must be stubbed, or the plugin will fail to load.

int init(void)

**Description**:\
Called when the plugin is loaded, before any other functions are called. Put global initialization here.

**Returns**:\
[SLURM_SUCCESS]{.commandline} on success, or\
[SLURM_ERROR]{.commandline} on failure.

void fini(void)

**Description**:\
Called when the plugin is removed. Clear any allocated storage here.

**Returns**: None.

**Note**: These init and fini functions are not the same as those described in the [dlopen (3)]{.commandline} system library. The C run-time system co-opts those symbols for its own initialization. The system [\_init()]{.commandline} is called before the Slurm [init()]{.commandline}, and the Slurm [fini()]{.commandline} is called before the system\'s [\_fini()]{.commandline}.

void site_factor_p_reconfig(void)

**Description**: Refresh the plugin\'s configuration. Called whenever slurmctld is reconfigured.

**Returns**: void

void site_factor_p_set(job_record_t \*job_ptr)

**Description**: Sets the site_priority of the job, if desired.

**Arguments**:\
[job_ptr]{.commandline} (input) pointer to the job record.

**Returns**: void

void site_factor_p_update(void)

**Description**: Handle periodic updates to all site_priority values in the job_list. Called every

**Returns**: void

## Parameters

These parameters can be used in the slurm.conf to configure the plugin and the frequency at which to gather information about running jobs.

[PrioritySiteFactorParameters]{.commandline}
:   Optional parameters for the site_factor plugin. Interpretation of any value is left to the site_factor plugin itself.

[PrioritySiteFactorPlugin]{.commandline}
:   Specifies which plugin should be used.

[PriorityCalcPeriod]{.commandline}
:   Interval between calls to [site_factor_p_update()]{.commandline}
