# [Slurm Plugin API]{#top}

## Overview

A Slurm plugin is a dynamically linked code object which is loaded explicitly at run time by the Slurm libraries. A plugin provides a customized implementation of a well-defined API connected to tasks such as authentication, interconnect fabric, and task scheduling.

## Identification

A Slurm plugin identifies itself by a short character string formatted similarly to a MIME type: *\<major\>/\<minor\>*. The major type identifies which API the plugin implements. The minor type uniquely distinguishes a plugin from other plugins that implement that same API, by such means as the intended platform or the internal algorithm. For example, a plugin to interface to the Maui scheduler would give its type as \"sched/maui.\" It would implement the Slurm Scheduler API.

## Versioning

Slurm plugins must provide a plugin_version symbol exactly matching that of the process they are loaded into. This is to avoid any potential issues if, e.g., an underlying struct definition is changed by a maintenance release.

It is expected that the plugins are automatically build, packaged, and distributed alongside the libslurm library, Slurm commands, and daemons.

The only exception to this is the SPANK plugin interface which only requires the Slurm release to match, while the maintenance release (micro version) may be changed. This is to reflect the additional ABI stability commitment that is maintained exclusively for that plugin interface.

## Data Objects {#data_objects}

A plugin must define and export the following symbols:

- [char plugin_type\[\] = \"\";]{.commandline}\
  A unique, short, formatted string to identify the plugin\'s purpose as described above. A \"null\" plugin (i.e., one that implements the desired API as stubs) should have a minor type of \"none.\"
- [char plugin_name\[\] = \"\";]{.commandline}\
  A free-form string that identifies the plugin in human-readable terms, such as \"Kerberos authentication.\" Slurm will use this string to identify the plugin to end users.
- [const uint32_t plugin_version = SLURM_VERSION_NUMBER;]{.commandline}\
  Identifies the version of Slurm used to build this plugin and any attempt to load the plugin from a different version of Slurm will result in an error. The micro version is not considered for [SPANK](spank.md) plugins.

## API Functions in All Plugins {#api}

extern int init(void);

**Description**: If present, this function is called just after the plugin is loaded. This allows the plugin to perform any global initialization prior to any actual API calls.

**Arguments**: None.

**Returns**: SLURM_SUCCESS if the plugin\'s initialization was successful. Any other return value indicates to Slurm that the plugin should be unloaded and not used.

extern void fini(void);

**Description**: If present, this function is called just before the plugin is unloaded. This allows the plugin to do any finalization after the last plugin-specific API call is made.

**Arguments**: None.

**Returns**: None.

**Note**: These init and fini functions are not the same as those described in the [dlopen (3)]{.commandline} system library. The C run-time system co-opts those symbols for its own initialization. The system [\_init()]{.commandline} is called before the Slurm [init()]{.commandline}, and the Slurm [fini()]{.commandline} is called before the system\'s [\_fini()]{.commandline}.

The functions need not appear. The plugin may provide either [init()]{.commandline} or [fini()]{.commandline} or both.

## Thread Safety {#thread_safety}

Slurm is a multithreaded application. The Slurm plugin library may exercise the plugin functions in a re-entrant fashion. It is the responsibility of the plugin author to provide the necessarily mutual exclusion and synchronization in order to avoid the pitfalls of re-entrant code.

## Run-time Support {#run_time}

The standard system libraries are available to the plugin. The Slurm libraries are also available and plugin authors are encouraged to make use of them rather than develop their own substitutes. Plugins should use the Slurm log to print error messages.

The plugin author is responsible for specifying any specific non-standard libraries needed for correct operation. Plugins will not load if their dependent libraries are not available, so it is the installer\'s job to make sure the specified libraries are available.

## Performance

All plugin functions are expected to execute very quickly. If any function entails delays (e.g. transactions with other systems), it should be written to utilize a thread for that functionality. This thread may be created by the [init()]{.commandline} function and deleted by the [fini()]{.commandline} functions. See **plugins/sched/backfill** for an example of how to do this.

## Data Structure Consistency {#structure}

In certain situations Slurm iterates over different data structures elements using counters. For example, with environment variable arrays. In order to avoid buffer overflows and other undesired situations, when a plugin modifies certain elements it must also update these counters accordingly. Other situations may require other types of changes.

The following advice indicates which structures have arrays with associated counters that must be maintained when modifying data, plus other possible important information to take in consideration when manipulating these structures. This list is not fully exhaustive due to constant modifications in code, but it is a first start point and basic guideline for most common situations. Complete structure information can be seen in the *slurm/slurm.h.in* file.

### slurm_job_info_t (job_info_t) Data Structure {#slurm_job_info_t}

      uint32_t env_size;
      char **environment;

      uint32_t spank_job_env_size;
      char **spank_job_env;

      uint32_t gres_detail_cnt;
      char **gres_detail_str;

These pairs of array pointers and element counters must kept updated in order to avoid subsequent buffer overflows, so if you update the array you must also update the related counter.

      char *nodes;
      int32_t *node_inx;

      int32_t *req_node_inx;
      char *req_nodes;

*node_inx* and *req_node_inx* represents a list of index pairs for ranges of nodes defined in the *nodes* and *req_nodes* fields respectively. In each case, both array variables must match the count.

      uint32_t het_job_id;
      char *het_job_id_set;

The *het_job_id* field should be the first element of the *het_job_id_set* array.

### job_step_info_t Data Structure {#job_step_info_t}

      char *nodes;
      int32_t *node_inx;

*node_inx* represents a list of index pairs for range of nodes defined in *nodes*. Both variables must match the node count.

### priority_factors_object_t Data Structure {#priority_factors_object_t}

      uint32_t tres_cnt;
      char **tres_names;
      double *tres_weights;

This value must match the configured TRES on the system, otherwise iteration over the *tres_names* or *tres_weights* arrays can cause buffer overflows.

### job_step_pids_t Data Structure {#job_step_pids_t}

      uint32_t pid_cnt;
      uint32_t *pid;

Array *pid* represents the list of Process IDs for the job step, and *pid_cnt* is the counter that must match the size of the array.

### slurm_step_layout_t Data Structure {#slurm_step_layout_t}

      uint32_t node_cnt;
      char *node_list;

The *node_list* array size must match *node_cnt*.

      uint16_t *tasks;
      uint32_t node_cnt;
      uint32_t task_cnt;

In the *tasks* array, each element is the number of tasks assigned to the corresponding node, to its size must match *node_cnt*. Moreover *task_cnt* represents the sum of tasks registered in *tasks*.

      uint32_t **tids;

*tids* is an array of length *node_cnt* of task ID arrays. Each subarray is designated by the corresponding value in the *tasks* array, so *tasks*, *tids* and *task_cnt* must be set to match this layout.

### slurm_step_launch_params_t Data Structure {#slurm_step_launch_params_t}

      uint32_t envc;
      char **env;

When modifying the environment variables in the *env* array, you must also modify the *envc* counter accordingly to prevent buffer overflows in subsequent loops over that array.

      uint32_t het_job_nnodes;
      uint32_t het_job_ntasks;

      uint16_t *het_job_task_cnts;
      uint32_t **het_job_tids;
      uint32_t *het_job_node_list;

This *het_job\_\** related variables must match the current heterogeneous job configuration.\
For example, if for whatever reason you are reducing the number of tasks for a node in a heterogeneous job, you should at least remove that task ID from *het_job_tids*, decrement *het_job_ntasks* and *het_job_task_cnts*, and possibly decrement the number of nodes of the heterogeneous job in *het_job_nnodes* and *het_job_node_list*.

      char **spank_job_env;
      uint32_t spank_job_env_size;

When modifying the *spank_job_env* structure, the *spank_job_env_size* field must be updated to prevent buffer overflows in subsequent loops over that array.

### node_info_t Data Structure {#node_info_t}

      char *features;
      char *features_act;

In a system containing Intel KNL processors the *features_act* field is set by the plugin to match the currently running modes on the node. On other systems the *features_act* is not usually used. If you program such a plugin you must ensure that *features_act* contains a subset of *features*.

    char *reason;
    time_t reason_time;
    uint32_t reason_uid;

If *reason* is modified then *reason_time* and *reason_uid* should be updated.

### reserve_info_t Data Structure {#reserve_info_t}

      int32_t *node_inx;
      uint32_t node_cnt;

*node_inx* represents a list of index pairs for range of nodes associated with the reservation and its count must equal *node_cnt*.

### partition_info_t Data Structure {#partition_info_t}

No special advice.

### slurm_step_layout_req_t Data Structure {#slurm_step_layout_req_t}

No special advice.

### slurm_step_ctx_params_t

No special advice.
