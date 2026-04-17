# Slurm REST API

::: app-desc
API to access and control Slurm
:::

::: app-desc
More information: https://www.schedmd.com/
:::

::: app-desc
Contact Info: sales@schedmd.com
:::

::: app-desc
Version: Slurm-25.11.4
:::

::: app-desc
BasePath:
:::

::: license-info
Apache 2.0
:::

::: license-url
https://www.apache.org/licenses/LICENSE-2.0.html
:::

## Access

1.  APIKey KeyParamName:X-SLURM-USER-NAME KeyInQuery:false KeyInHeader:true
2.  APIKey KeyParamName:X-SLURM-USER-TOKEN KeyInQuery:false KeyInHeader:true
3.  HTTP Basic Authentication

## [Methods]{#__Methods}

\[ Jump to Models \]

### Table of Contents

::: method-summary
:::

#### Slurm

- [`delete`]{.http-method}` /slurm/v0.0.44/job/{job_id}`
- [`delete`]{.http-method}` /slurm/v0.0.44/jobs/`
- [`delete`]{.http-method}` /slurm/v0.0.44/node/{node_name}`
- [`delete`]{.http-method}` /slurm/v0.0.44/reservation/{reservation_name}`
- [`get`]{.http-method}` /slurm/v0.0.44/diag/`
- [`get`]{.http-method}` /slurm/v0.0.44/job/{job_id}`
- [`get`]{.http-method}` /slurm/v0.0.44/jobs/`
- [`get`]{.http-method}` /slurm/v0.0.44/jobs/state/`
- [`get`]{.http-method}` /slurm/v0.0.44/licenses/`
- [`get`]{.http-method}` /slurm/v0.0.44/node/{node_name}`
- [`get`]{.http-method}` /slurm/v0.0.44/nodes/`
- [`get`]{.http-method}` /slurm/v0.0.44/partition/{partition_name}`
- [`get`]{.http-method}` /slurm/v0.0.44/partitions/`
- [`get`]{.http-method}` /slurm/v0.0.44/ping/`
- [`get`]{.http-method}` /slurm/v0.0.44/reconfigure/`
- [`get`]{.http-method}` /slurm/v0.0.44/reservation/{reservation_name}`
- [`get`]{.http-method}` /slurm/v0.0.44/reservations/`
- [`get`]{.http-method}` /slurm/v0.0.44/resources/{job_id}`
- [`get`]{.http-method}` /slurm/v0.0.44/shares`
- [`post`]{.http-method}` /slurm/v0.0.44/job/{job_id}`
- [`post`]{.http-method}` /slurm/v0.0.44/job/allocate`
- [`post`]{.http-method}` /slurm/v0.0.44/job/submit`
- [`post`]{.http-method}` /slurm/v0.0.44/new/node/`
- [`post`]{.http-method}` /slurm/v0.0.44/node/{node_name}`
- [`post`]{.http-method}` /slurm/v0.0.44/nodes/`
- [`post`]{.http-method}` /slurm/v0.0.44/reservation`
- [`post`]{.http-method}` /slurm/v0.0.44/reservations/`

#### Slurmdb

- [`delete`]{.http-method}` /slurmdb/v0.0.44/account/{account_name}`
- [`delete`]{.http-method}` /slurmdb/v0.0.44/association/`
- [`delete`]{.http-method}` /slurmdb/v0.0.44/associations/`
- [`delete`]{.http-method}` /slurmdb/v0.0.44/cluster/{cluster_name}`
- [`delete`]{.http-method}` /slurmdb/v0.0.44/qos/{qos}`
- [`delete`]{.http-method}` /slurmdb/v0.0.44/user/{name}`
- [`delete`]{.http-method}` /slurmdb/v0.0.44/wckey/{id}`
- [`get`]{.http-method}` /slurmdb/v0.0.44/account/{account_name}`
- [`get`]{.http-method}` /slurmdb/v0.0.44/accounts/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/association/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/associations/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/cluster/{cluster_name}`
- [`get`]{.http-method}` /slurmdb/v0.0.44/clusters/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/config`
- [`get`]{.http-method}` /slurmdb/v0.0.44/diag/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/instance/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/instances/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/job/{job_id}`
- [`get`]{.http-method}` /slurmdb/v0.0.44/jobs/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/ping/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/qos/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/qos/{qos}`
- [`get`]{.http-method}` /slurmdb/v0.0.44/tres/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/user/{name}`
- [`get`]{.http-method}` /slurmdb/v0.0.44/users/`
- [`get`]{.http-method}` /slurmdb/v0.0.44/wckey/{id}`
- [`get`]{.http-method}` /slurmdb/v0.0.44/wckeys/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/accounts/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/accounts_association/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/associations/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/clusters/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/config`
- [`post`]{.http-method}` /slurmdb/v0.0.44/job/{job_id}`
- [`post`]{.http-method}` /slurmdb/v0.0.44/jobs/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/qos/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/tres/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/users/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/users_association/`
- [`post`]{.http-method}` /slurmdb/v0.0.44/wckeys/`

# [Slurm]{#Slurm}

:::::::::::::::: method
[]{#slurmV0044DeleteJob}

::: method-path
[]{#slurmV0044DeleteJob} Up

``` delete
delete /slurm/v0.0.44/job/{job_id}
```
:::

::: method-summary
cancel or signal job ([slurmV0044DeleteJob]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters .field-label}

::::: field-items
::: param
job_id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Job ID default: null
:::
:::::

### Query parameters {#query-parameters .field-label}

::::::: field-items
::: param
signal (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Signal to send to Job default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Signalling flags default: null
:::
:::::::

### Return type {#return-type .field-label}

::: return-type
v0.0.44_openapi_kill_job_resp
:::

### Example data {#example-data .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "status" : [ {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  }, {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  } ]
}
```

### Produces {#produces .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses .field-label}

#### 200 {#section .field-label}

job signal result v0.0.44_openapi_kill_job_resp

#### default {#default .field-label}

job signal result v0.0.44_openapi_kill_job_resp
::::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044DeleteJobs}

::: method-path
[]{#slurmV0044DeleteJobs} Up

``` delete
delete /slurm/v0.0.44/jobs/
```
:::

::: method-summary
send signal to list of jobs ([slurmV0044DeleteJobs]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body .field-label}

::::: field-items
::: param
v0.0.44_kill_jobs_msg v0.0.44_kill_jobs_msg (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-1 .field-label}

::: return-type
v0.0.44_openapi_kill_jobs_resp
:::

### Example data {#example-data-1 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "status" : [ {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  }, {
    "federation" : {
      "sibling" : "sibling"
    },
    "job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "error" : {
      "code" : 0,
      "string" : "string",
      "message" : "message"
    },
    "step_id" : "step_id"
  } ]
}
```

### Produces {#produces-1 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-1 .field-label}

#### 200 {#section-1 .field-label}

description of jobs to signal v0.0.44_openapi_kill_jobs_resp

#### default {#default-1 .field-label}

description of jobs to signal v0.0.44_openapi_kill_jobs_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044DeleteNode}

::: method-path
[]{#slurmV0044DeleteNode} Up

``` delete
delete /slurm/v0.0.44/node/{node_name}
```
:::

::: method-summary
delete node ([slurmV0044DeleteNode]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-1 .field-label}

::::: field-items
::: param
node_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Node name default: null
:::
:::::

### Return type {#return-type-2 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-2 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-2 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-2 .field-label}

#### 200 {#section-2 .field-label}

node delete request result v0.0.44_openapi_resp

#### default {#default-2 .field-label}

node delete request result v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044DeleteReservation}

::: method-path
[]{#slurmV0044DeleteReservation} Up

``` delete
delete /slurm/v0.0.44/reservation/{reservation_name}
```
:::

::: method-summary
delete a reservation ([slurmV0044DeleteReservation]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-2 .field-label}

::::: field-items
::: param
reservation_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Reservation name default: null
:::
:::::

### Return type {#return-type-3 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-3 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-3 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-3 .field-label}

#### 200 {#section-3 .field-label}

reservation delete request result v0.0.44_openapi_resp

#### default {#default-3 .field-label}

reservation delete request result v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmV0044GetDiag}

::: method-path
[]{#slurmV0044GetDiag} Up

``` get
get /slurm/v0.0.44/diag/
```
:::

::: method-summary
get diagnostics ([slurmV0044GetDiag]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-4 .field-label}

::: return-type
v0.0.44_openapi_diag_resp
:::

### Example data {#example-data-4 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "statistics" : {
    "bf_cycle_max" : 7,
    "rpcs_by_message_type" : [ {
      "cycle_last" : 0,
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "type_id" : 7,
      "queued" : 0,
      "count" : 9,
      "dropped" : 9,
      "message_type" : "message_type",
      "total_time" : 5,
      "cycle_max" : 7
    }, {
      "cycle_last" : 0,
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "type_id" : 7,
      "queued" : 0,
      "count" : 9,
      "dropped" : 9,
      "message_type" : "message_type",
      "total_time" : 5,
      "cycle_max" : 7
    } ],
    "bf_backfilled_het_jobs" : 6,
    "bf_table_size" : 4,
    "schedule_cycle_depth" : 1,
    "bf_depth_sum" : 5,
    "job_states_ts" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "bf_queue_len" : 4,
    "jobs_started" : 8,
    "schedule_cycle_max" : 9,
    "server_thread_count" : 6,
    "bf_queue_len_sum" : 6,
    "bf_cycle_last" : 0,
    "bf_exit" : {
      "state_changed" : 3,
      "bf_max_time" : 8,
      "bf_max_job_start" : 0,
      "bf_node_space_size" : 7,
      "end_job_queue" : 6,
      "bf_max_job_test" : 4
    },
    "agent_thread_count" : 5,
    "jobs_completed" : 9,
    "bf_depth_mean" : 3,
    "bf_depth_try_sum" : 3,
    "schedule_cycle_mean" : 7,
    "bf_table_size_sum" : 1,
    "agent_queue_size" : 1,
    "jobs_failed" : 3,
    "bf_last_depth_try" : 7,
    "req_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "bf_cycle_counter" : 5,
    "schedule_queue_length" : 9,
    "bf_queue_len_mean" : 0,
    "schedule_exit" : {
      "max_sched_time" : 5,
      "licenses" : 9,
      "default_queue_depth" : 7,
      "max_job_start" : 1,
      "max_rpc_cnt" : 4,
      "end_job_queue" : 6
    },
    "jobs_canceled" : 6,
    "schedule_cycle_sum" : 2,
    "jobs_submitted" : 6,
    "schedule_cycle_mean_depth" : 1,
    "schedule_cycle_per_minute" : 1,
    "req_time_start" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "jobs_running" : 1,
    "bf_last_backfilled_jobs" : 6,
    "bf_last_depth" : 3,
    "bf_backfilled_jobs" : 2,
    "rpcs_by_user" : [ {
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user_id" : 4,
      "count" : 6,
      "total_time" : 8,
      "user" : "user"
    }, {
      "average_time" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user_id" : 4,
      "count" : 6,
      "total_time" : 8,
      "user" : "user"
    } ],
    "bf_cycle_mean" : 6,
    "pending_rpcs_by_hostlist" : [ {
      "type_id" : 0,
      "count" : [ "count", "count" ],
      "message_type" : "message_type"
    }, {
      "type_id" : 0,
      "count" : [ "count", "count" ],
      "message_type" : "message_type"
    } ],
    "dbd_agent_queue_size" : 2,
    "bf_table_size_mean" : 4,
    "jobs_pending" : 6,
    "agent_count" : 5,
    "bf_cycle_sum" : 7,
    "parts_packed" : 0,
    "bf_active" : true,
    "bf_depth_mean_try" : 3,
    "gettimeofday_latency" : 7,
    "pending_rpcs" : [ {
      "type_id" : 4,
      "count" : 3,
      "message_type" : "message_type"
    }, {
      "type_id" : 4,
      "count" : 3,
      "message_type" : "message_type"
    } ],
    "schedule_cycle_total" : 4,
    "bf_when_last_cycle" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "schedule_cycle_last" : 3
  }
}
```

### Produces {#produces-4 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-4 .field-label}

#### 200 {#section-4 .field-label}

diagnostic results v0.0.44_openapi_diag_resp

#### default {#default-4 .field-label}

diagnostic results v0.0.44_openapi_diag_resp
::::::::

------------------------------------------------------------------------

:::::::::::::::: method
[]{#slurmV0044GetJob}

::: method-path
[]{#slurmV0044GetJob} Up

``` get
get /slurm/v0.0.44/job/{job_id}
```
:::

::: method-summary
get job info ([slurmV0044GetJob]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-3 .field-label}

::::: field-items
::: param
job_id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Job ID default: null
:::
:::::

### Query parameters {#query-parameters-1 .field-label}

::::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query jobs updated more recently than this time (UNIX timestamp) default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::
:::::::

### Return type {#return-type-5 .field-label}

::: return-type
v0.0.44_openapi_job_info_resp
:::

### Example data {#example-data-5 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "last_backfill" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  } ],
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-5 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-5 .field-label}

#### 200 {#section-5 .field-label}

job(s) information v0.0.44_openapi_job_info_resp

#### default {#default-5 .field-label}

job(s) information v0.0.44_openapi_job_info_resp
::::::::::::::::

------------------------------------------------------------------------

::::::::::::: method
[]{#slurmV0044GetJobs}

::: method-path
[]{#slurmV0044GetJobs} Up

``` get
get /slurm/v0.0.44/jobs/
```
:::

::: method-summary
get list of jobs ([slurmV0044GetJobs]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-2 .field-label}

::::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query jobs updated more recently than this time (UNIX timestamp) default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::
:::::::

### Return type {#return-type-6 .field-label}

::: return-type
v0.0.44_openapi_job_info_resp
:::

### Example data {#example-data-6 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "last_backfill" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  } ],
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-6 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-6 .field-label}

#### 200 {#section-6 .field-label}

job(s) information v0.0.44_openapi_job_info_resp

#### default {#default-6 .field-label}

job(s) information v0.0.44_openapi_job_info_resp
:::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044GetJobsState}

::: method-path
[]{#slurmV0044GetJobsState} Up

``` get
get /slurm/v0.0.44/jobs/state/
```
:::

::: method-summary
get list of job states ([slurmV0044GetJobsState]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-3 .field-label}

::::: field-items
::: param
job_id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV list of Job IDs to search for default: null
:::
:::::

### Return type {#return-type-7 .field-label}

::: return-type
v0.0.44_openapi_job_info_resp
:::

### Example data {#example-data-7 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "last_backfill" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "time_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "memory_per_tres" : "memory_per_tres",
    "scheduled_nodes" : "scheduled_nodes",
    "qos" : "qos",
    "resize_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "eligible_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpus_per_tres" : "cpus_per_tres",
    "preemptable_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "system_comment" : "system_comment",
    "federation_siblings_active" : "federation_siblings_active",
    "tasks_per_tres" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "accrue_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "dependency" : "dependency",
    "group_name" : "group_name",
    "profile" : [ "NOT_SET", "NOT_SET" ],
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_per_job" : "tres_per_job",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "priority_by_partition" : [ {
      "partition" : "partition",
      "priority" : 6
    }, {
      "partition" : "partition",
      "priority" : 6
    } ],
    "maximum_switch_wait_time" : 9,
    "core_spec" : 6,
    "mcs_label" : "mcs_label",
    "required_nodes" : "required_nodes",
    "tres_bind" : "tres_bind",
    "user_id" : 9,
    "selinux_context" : "selinux_context",
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "federation_origin" : "federation_origin",
    "container_id" : "container_id",
    "shared" : [ "none", "none" ],
    "tasks_per_board" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "user_name" : "user_name",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "KILL_INVALID_DEPENDENCY", "KILL_INVALID_DEPENDENCY" ],
    "standard_input" : "standard_input",
    "admin_comment" : "admin_comment",
    "cores_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "step_id" : {
      "sluid" : "sluid",
      "job_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_het_component" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "step_id" : "step_id"
    },
    "job_state" : [ "PENDING", "PENDING" ],
    "tasks_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "current_working_directory" : "current_working_directory",
    "standard_error" : "standard_error",
    "array_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "cluster_features" : "cluster_features",
    "partition" : "partition",
    "segment_size" : 4,
    "threads_per_core" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_alloc_str" : "tres_alloc_str",
    "memory_per_cpu" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "cpu_frequency_minimum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "power" : {
      "flags" : [ "", "" ]
    },
    "deadline" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "mail_type" : [ "BEGIN", "BEGIN" ],
    "memory_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "state_reason" : "state_reason",
    "het_job_offset" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_board" : 5,
    "nice" : 1,
    "last_sched_evaluation" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tres_per_node" : "tres_per_node",
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "excluded_nodes" : "excluded_nodes",
    "array_max_tasks" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "het_job_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "sockets_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "prefer" : "prefer",
    "time_limit" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "minimum_cpus_per_node" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "tasks_per_socket" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_host" : "batch_host",
    "max_cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "job_size_str" : [ "job_size_str", "job_size_str" ],
    "hold" : true,
    "cpu_frequency_maximum" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "het_job_id_set" : "het_job_id_set",
    "state_description" : "state_description",
    "submit_line" : "submit_line",
    "array_task_id" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "licenses_allocated" : "licenses_allocated",
    "minimum_tmp_disk_per_node" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "tres_req_str" : "tres_req_str",
    "burst_buffer_state" : "burst_buffer_state",
    "cron" : "cron",
    "allocating_node" : "allocating_node",
    "tres_per_socket" : "tres_per_socket",
    "array_task_string" : "array_task_string",
    "submit_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "wckey" : "wckey",
    "max_nodes" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "batch_flag" : true,
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "name" : "name",
    "preempt_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "contiguous" : true,
    "job_resources" : {
      "nodes" : {
        "allocation" : [ {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        }, {
          "memory" : {
            "used" : 2,
            "allocated" : 4
          },
          "cpus" : {
            "count" : 9,
            "used" : 3
          },
          "name" : "name",
          "index" : 7,
          "sockets" : [ {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          }, {
            "cores" : [ {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            }, {
              "index" : 1,
              "status" : [ "INVALID", "INVALID" ]
            } ],
            "index" : 7
          } ]
        } ],
        "count" : 2,
        "select_type" : [ "AVAILABLE", "AVAILABLE" ],
        "whole" : true,
        "list" : "list"
      },
      "threads_per_core" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus" : 1,
      "select_type" : [ "CPU", "CPU" ]
    },
    "billable_tres" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "federation_siblings_viable" : "federation_siblings_viable",
    "cpus_per_task" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "batch_features" : "batch_features",
    "thread_spec" : 1,
    "cpu_frequency_governor" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres_detail" : [ "gres_detail", "gres_detail" ],
    "stdout_expanded" : "stdout_expanded",
    "network" : "network",
    "restart_cnt" : 1,
    "resv_name" : "resv_name",
    "extra" : "extra",
    "delay_boot" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "reboot" : true,
    "cpus" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "standard_output" : "standard_output",
    "pre_sus_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "suspend_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "association_id" : 0,
    "command" : "command",
    "tres_freq" : "tres_freq",
    "requeue" : true,
    "tres_per_task" : "tres_per_task",
    "mail_user" : "mail_user",
    "nodes" : "nodes",
    "group_id" : 5,
    "job_id" : 5,
    "comment" : "comment",
    "account" : "account",
    "required_switches" : 7
  } ],
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-7 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-7 .field-label}

#### 200 {#section-7 .field-label}

job(s) state information v0.0.44_openapi_job_info_resp

#### default {#default-7 .field-label}

job(s) state information v0.0.44_openapi_job_info_resp
:::::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmV0044GetLicenses}

::: method-path
[]{#slurmV0044GetLicenses} Up

``` get
get /slurm/v0.0.44/licenses/
```
:::

::: method-summary
get all Slurm tracked license info ([slurmV0044GetLicenses]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-8 .field-label}

::: return-type
v0.0.44_openapi_licenses_resp
:::

### Example data {#example-data-8 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "licenses" : [ {
    "Used" : 6,
    "LastUpdate" : 7,
    "Total" : 0,
    "Remote" : true,
    "LastConsumed" : 5,
    "LastDeficit" : 2,
    "LicenseName" : "LicenseName",
    "Free" : 1,
    "Nodes" : "Nodes",
    "Reserved" : 5
  }, {
    "Used" : 6,
    "LastUpdate" : 7,
    "Total" : 0,
    "Remote" : true,
    "LastConsumed" : 5,
    "LastDeficit" : 2,
    "LicenseName" : "LicenseName",
    "Free" : 1,
    "Nodes" : "Nodes",
    "Reserved" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-8 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-8 .field-label}

#### 200 {#section-8 .field-label}

results of get all licenses v0.0.44_openapi_licenses_resp

#### default {#default-8 .field-label}

results of get all licenses v0.0.44_openapi_licenses_resp
::::::::

------------------------------------------------------------------------

:::::::::::::::: method
[]{#slurmV0044GetNode}

::: method-path
[]{#slurmV0044GetNode} Up

``` get
get /slurm/v0.0.44/node/{node_name}
```
:::

::: method-summary
get node info ([slurmV0044GetNode]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-4 .field-label}

::::: field-items
::: param
node_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Node name default: null
:::
:::::

### Query parameters {#query-parameters-4 .field-label}

::::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query jobs updated more recently than this time (UNIX timestamp) default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::
:::::::

### Return type {#return-type-9 .field-label}

::: return-type
v0.0.44_openapi_nodes_resp
:::

### Example data {#example-data-9 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "nodes" : [ {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  }, {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-9 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-9 .field-label}

#### 200 {#section-9 .field-label}

node information v0.0.44_openapi_nodes_resp

#### default {#default-9 .field-label}

node information v0.0.44_openapi_nodes_resp
::::::::::::::::

------------------------------------------------------------------------

::::::::::::: method
[]{#slurmV0044GetNodes}

::: method-path
[]{#slurmV0044GetNodes} Up

``` get
get /slurm/v0.0.44/nodes/
```
:::

::: method-summary
get node(s) info ([slurmV0044GetNodes]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-5 .field-label}

::::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query jobs updated more recently than this time (UNIX timestamp) default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::
:::::::

### Return type {#return-type-10 .field-label}

::: return-type
v0.0.44_openapi_nodes_resp
:::

### Example data {#example-data-10 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "nodes" : [ {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  }, {
    "reason" : "reason",
    "gpu_spec" : "gpu_spec",
    "slurmd_start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "cores" : 6,
    "reason_changed_at" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "reservation" : "reservation",
    "tres" : "tres",
    "cpu_binding" : 5,
    "state" : [ "INVALID", "INVALID" ],
    "sockets" : 9,
    "energy" : {
      "current_watts" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "base_consumed_energy" : 3,
      "last_collected" : 7,
      "consumed_energy" : 2,
      "previous_consumed_energy" : 4,
      "average_watts" : 9
    },
    "partitions" : [ "partitions", "partitions" ],
    "topology" : "topology",
    "gres_drained" : "gres_drained",
    "weight" : 8,
    "version" : "version",
    "gres_used" : "gres_used",
    "mcs_label" : "mcs_label",
    "real_memory" : 1,
    "instance_id" : "instance_id",
    "burstbuffer_network_address" : "burstbuffer_network_address",
    "port" : 1,
    "name" : "name",
    "resume_after" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "temporary_disk" : 6,
    "tres_used" : "tres_used",
    "effective_cpus" : 7,
    "instance_type" : "instance_type",
    "external_sensors" : "{}",
    "cert_flags" : [ "TOKEN_SET", "TOKEN_SET" ],
    "res_cores_per_gpu" : 6,
    "boards" : 0,
    "alloc_cpus" : 1,
    "active_features" : [ "active_features", "active_features" ],
    "reason_set_by_user" : "reason_set_by_user",
    "free_mem" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_idle_cpus" : 4,
    "extra" : "extra",
    "operating_system" : "operating_system",
    "power" : "{}",
    "tls_cert_last_renewal" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "architecture" : "architecture",
    "owner" : "owner",
    "cluster_name" : "cluster_name",
    "address" : "address",
    "cpus" : 2,
    "tres_weighted" : 5.025004791520295,
    "gres" : "gres",
    "threads" : 9,
    "boot_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "alloc_memory" : 7,
    "specialized_memory" : 1,
    "specialized_cpus" : "specialized_cpus",
    "specialized_cores" : 1,
    "last_busy" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "comment" : "comment",
    "next_state_after_reboot" : [ "INVALID", "INVALID" ],
    "cpu_load" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-10 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-10 .field-label}

#### 200 {#section-10 .field-label}

node(s) information v0.0.44_openapi_nodes_resp

#### default {#default-10 .field-label}

node(s) information v0.0.44_openapi_nodes_resp
:::::::::::::

------------------------------------------------------------------------

:::::::::::::::: method
[]{#slurmV0044GetPartition}

::: method-path
[]{#slurmV0044GetPartition} Up

``` get
get /slurm/v0.0.44/partition/{partition_name}
```
:::

::: method-summary
get partition info ([slurmV0044GetPartition]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-5 .field-label}

::::: field-items
::: param
partition_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Partition name default: null
:::
:::::

### Query parameters {#query-parameters-6 .field-label}

::::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query partitions updated more recently than this time (UNIX timestamp) default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::
:::::::

### Return type {#return-type-11 .field-label}

::: return-type
v0.0.44_openapi_partition_resp
:::

### Example data {#example-data-11 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "partitions" : [ {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  }, {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-11 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-11 .field-label}

#### 200 {#section-11 .field-label}

partition information v0.0.44_openapi_partition_resp

#### default {#default-11 .field-label}

partition information v0.0.44_openapi_partition_resp
::::::::::::::::

------------------------------------------------------------------------

::::::::::::: method
[]{#slurmV0044GetPartitions}

::: method-path
[]{#slurmV0044GetPartitions} Up

``` get
get /slurm/v0.0.44/partitions/
```
:::

::: method-summary
get all partition info ([slurmV0044GetPartitions]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-7 .field-label}

::::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query partitions updated more recently than this time (UNIX timestamp) default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::
:::::::

### Return type {#return-type-12 .field-label}

::: return-type
v0.0.44_openapi_partition_resp
:::

### Example data {#example-data-12 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "partitions" : [ {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  }, {
    "cluster" : "cluster",
    "cpus" : {
      "task_binding" : 6,
      "total" : 1
    },
    "topology" : "topology",
    "timeouts" : {
      "resume" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "suspend" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "groups" : {
      "allowed" : "allowed"
    },
    "alternate" : "alternate",
    "select_type" : [ "CPU", "CPU" ],
    "suspend_time" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "priority" : {
      "tier" : 4,
      "job_factor" : 2
    },
    "node_sets" : "node_sets",
    "maximums" : {
      "shares" : 7,
      "nodes" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "over_time_limit" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_node" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "cpus_per_socket" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "oversubscribe" : {
        "jobs" : 9,
        "flags" : [ "force", "force" ]
      },
      "memory_per_cpu" : 2,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "nodes" : {
      "configured" : "configured",
      "total" : 0,
      "allowed_allocation" : "allowed_allocation"
    },
    "partition" : {
      "state" : [ "INACTIVE", "INACTIVE" ]
    },
    "qos" : {
      "deny" : "deny",
      "allowed" : "allowed",
      "assigned" : "assigned"
    },
    "defaults" : {
      "partition_memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "memory_per_cpu" : 5,
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "job" : "job",
      "partition_memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "name" : "name",
    "tres" : {
      "configured" : "configured",
      "billing_weights" : "billing_weights"
    },
    "accounts" : {
      "deny" : "deny",
      "allowed" : "allowed"
    },
    "minimums" : {
      "nodes" : 3
    },
    "grace_time" : 5
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-12 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-12 .field-label}

#### 200 {#section-12 .field-label}

partition information v0.0.44_openapi_partition_resp

#### default {#default-12 .field-label}

partition information v0.0.44_openapi_partition_resp
:::::::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmV0044GetPing}

::: method-path
[]{#slurmV0044GetPing} Up

``` get
get /slurm/v0.0.44/ping/
```
:::

::: method-summary
ping test ([slurmV0044GetPing]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-13 .field-label}

::: return-type
v0.0.44_openapi_ping_array_resp
:::

### Example data {#example-data-13 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "pings" : [ {
    "mode" : "mode",
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "pinged" : "pinged",
    "primary" : true
  }, {
    "mode" : "mode",
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "pinged" : "pinged",
    "primary" : true
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-13 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-13 .field-label}

#### 200 {#section-13 .field-label}

results of ping test v0.0.44_openapi_ping_array_resp

#### default {#default-13 .field-label}

results of ping test v0.0.44_openapi_ping_array_resp
::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmV0044GetReconfigure}

::: method-path
[]{#slurmV0044GetReconfigure} Up

``` get
get /slurm/v0.0.44/reconfigure/
```
:::

::: method-summary
request slurmctld reconfigure ([slurmV0044GetReconfigure]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-14 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-14 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-14 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-14 .field-label}

#### 200 {#section-14 .field-label}

reconfigure request result v0.0.44_openapi_resp

#### default {#default-14 .field-label}

reconfigure request result v0.0.44_openapi_resp
::::::::

------------------------------------------------------------------------

:::::::::::::: method
[]{#slurmV0044GetReservation}

::: method-path
[]{#slurmV0044GetReservation} Up

``` get
get /slurm/v0.0.44/reservation/{reservation_name}
```
:::

::: method-summary
get reservation info ([slurmV0044GetReservation]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-6 .field-label}

::::: field-items
::: param
reservation_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Reservation name default: null
:::
:::::

### Query parameters {#query-parameters-8 .field-label}

::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query reservations updated more recently than this time (UNIX timestamp) default: null
:::
:::::

### Return type {#return-type-15 .field-label}

::: return-type
v0.0.44_openapi_reservation_resp
:::

### Example data {#example-data-15 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-15 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-15 .field-label}

#### 200 {#section-15 .field-label}

reservation information v0.0.44_openapi_reservation_resp

#### default {#default-15 .field-label}

reservation information v0.0.44_openapi_reservation_resp
::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044GetReservations}

::: method-path
[]{#slurmV0044GetReservations} Up

``` get
get /slurm/v0.0.44/reservations/
```
:::

::: method-summary
get all reservation info ([slurmV0044GetReservations]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-9 .field-label}

::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query reservations updated more recently than this time (UNIX timestamp) default: null
:::
:::::

### Return type {#return-type-16 .field-label}

::: return-type
v0.0.44_openapi_reservation_resp
:::

### Example data {#example-data-16 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : "groups",
    "users" : "users",
    "max_start_delay" : 6,
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : "licenses",
    "partition" : "partition",
    "watts" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "core_specializations" : [ {
      "node" : "node",
      "core" : "core"
    }, {
      "node" : "node",
      "core" : "core"
    } ],
    "name" : "name",
    "tres" : "tres",
    "accounts" : "accounts",
    "node_count" : 1,
    "node_list" : "node_list",
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : 0
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "last_update" : {
    "number" : 2,
    "set" : true,
    "infinite" : true
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-16 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-16 .field-label}

#### 200 {#section-16 .field-label}

reservation information v0.0.44_openapi_reservation_resp

#### default {#default-16 .field-label}

reservation information v0.0.44_openapi_reservation_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044GetResources}

::: method-path
[]{#slurmV0044GetResources} Up

``` get
get /slurm/v0.0.44/resources/{job_id}
```
:::

::: method-summary
get resource layout info ([slurmV0044GetResources]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-7 .field-label}

::::: field-items
::: param
job_id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Job ID default: null
:::
:::::

### Return type {#return-type-17 .field-label}

::: return-type
v0.0.44_openapi_resource_layout_resp
:::

### Example data {#example-data-17 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "nodes" : [ {
    "node" : "node",
    "channel" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres" : [ {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    } ],
    "cores_per_socket" : 6,
    "mem_alloc" : 1,
    "core_bitmap" : "core_bitmap",
    "sockets_per_node" : 0
  }, {
    "node" : "node",
    "channel" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "gres" : [ {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 5,
      "index" : "index",
      "type" : "type"
    } ],
    "cores_per_socket" : 6,
    "mem_alloc" : 1,
    "core_bitmap" : "core_bitmap",
    "sockets_per_node" : 0
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-17 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-17 .field-label}

#### 200 {#section-17 .field-label}

resource layout information v0.0.44_openapi_resource_layout_resp

#### default {#default-17 .field-label}

resource layout information v0.0.44_openapi_resource_layout_resp
:::::::::::

------------------------------------------------------------------------

::::::::::::: method
[]{#slurmV0044GetShares}

::: method-path
[]{#slurmV0044GetShares} Up

``` get
get /slurm/v0.0.44/shares
```
:::

::: method-summary
get fairshare info ([slurmV0044GetShares]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-10 .field-label}

::::::: field-items
::: param
accounts (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Accounts to query default: null
:::

::: param
users (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Users to query default: null
:::
:::::::

### Return type {#return-type-18 .field-label}

::: return-type
v0.0.44_openapi_shares_resp
:::

### Example data {#example-data-18 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "shares" : {
    "shares" : [ {
      "cluster" : "cluster",
      "parent" : "parent",
      "shares_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "usage" : 1,
      "fairshare" : {
        "level" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        },
        "factor" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        }
      },
      "type" : [ "USER", "USER" ],
      "effective_usage" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "shares" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition" : "partition",
      "usage_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "name" : "name",
      "tres" : {
        "run_seconds" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ],
        "usage" : [ {
          "name" : "name",
          "value" : 6.027456183070403
        }, {
          "name" : "name",
          "value" : 6.027456183070403
        } ],
        "group_minutes" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ]
      },
      "id" : 0
    }, {
      "cluster" : "cluster",
      "parent" : "parent",
      "shares_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "usage" : 1,
      "fairshare" : {
        "level" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        },
        "factor" : {
          "number" : 4.145608029883936,
          "set" : true,
          "infinite" : true
        }
      },
      "type" : [ "USER", "USER" ],
      "effective_usage" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "shares" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "partition" : "partition",
      "usage_normalized" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "name" : "name",
      "tres" : {
        "run_seconds" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ],
        "usage" : [ {
          "name" : "name",
          "value" : 6.027456183070403
        }, {
          "name" : "name",
          "value" : 6.027456183070403
        } ],
        "group_minutes" : [ {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }, {
          "name" : "name",
          "value" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        } ]
      },
      "id" : 0
    } ],
    "total_shares" : 5
  },
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-18 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-18 .field-label}

#### 200 {#section-18 .field-label}

shares information v0.0.44_openapi_shares_resp

#### default {#default-18 .field-label}

shares information v0.0.44_openapi_shares_resp
:::::::::::::

------------------------------------------------------------------------

:::::::::::::: method
[]{#slurmV0044PostJob}

::: method-path
[]{#slurmV0044PostJob} Up

``` post
post /slurm/v0.0.44/job/{job_id}
```
:::

::: method-summary
update job ([slurmV0044PostJob]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-8 .field-label}

::::: field-items
::: param
job_id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Job ID default: null
:::
:::::

### Consumes {#consumes-1 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-1 .field-label}

::::: field-items
::: param
v0.0.44_job_desc_msg v0.0.44_job_desc_msg (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-19 .field-label}

::: return-type
v0.0.44_openapi_job_post_response
:::

### Example data {#example-data-19 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "results" : [ {
    "job_id" : 0,
    "why" : "why",
    "error_code" : 6,
    "step_id" : "step_id",
    "error" : "error"
  }, {
    "job_id" : 0,
    "why" : "why",
    "error_code" : 6,
    "step_id" : "step_id",
    "error" : "error"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-19 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-19 .field-label}

#### 200 {#section-19 .field-label}

job update result v0.0.44_openapi_job_post_response

#### default {#default-19 .field-label}

job update result v0.0.44_openapi_job_post_response
::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044PostJobAllocate}

::: method-path
[]{#slurmV0044PostJobAllocate} Up

``` post
post /slurm/v0.0.44/job/allocate
```
:::

::: method-summary
submit new job allocation without any steps that must be signaled to stop ([slurmV0044PostJobAllocate]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-2 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-2 .field-label}

::::: field-items
::: param
v0.0.44_job_alloc_req v0.0.44_job_alloc_req (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-20 .field-label}

::: return-type
v0.0.44_openapi_job_alloc_resp
:::

### Example data {#example-data-20 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "job_id" : 0,
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "job_submit_user_msg" : "job_submit_user_msg",
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-20 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-20 .field-label}

#### 200 {#section-20 .field-label}

job allocation response v0.0.44_openapi_job_alloc_resp

#### default {#default-20 .field-label}

job allocation response v0.0.44_openapi_job_alloc_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044PostJobSubmit}

::: method-path
[]{#slurmV0044PostJobSubmit} Up

``` post
post /slurm/v0.0.44/job/submit
```
:::

::: method-summary
submit new job ([slurmV0044PostJobSubmit]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-3 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-3 .field-label}

::::: field-items
::: param
v0.0.44_job_submit_req v0.0.44_job_submit_req (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-21 .field-label}

::: return-type
v0.0.44_openapi_job_submit_response
:::

### Example data {#example-data-21 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "job_id" : 0,
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "step_id" : "step_id",
  "job_submit_user_msg" : "job_submit_user_msg",
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-21 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-21 .field-label}

#### 200 {#section-21 .field-label}

job submission response v0.0.44_openapi_job_submit_response

#### default {#default-21 .field-label}

job submission response v0.0.44_openapi_job_submit_response
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044PostNewNode}

::: method-path
[]{#slurmV0044PostNewNode} Up

``` post
post /slurm/v0.0.44/new/node/
```
:::

::: method-summary
create node ([slurmV0044PostNewNode]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-4 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-4 .field-label}

::::: field-items
::: param
v0.0.44_openapi_create_node_req v0.0.44_openapi_create_node_req (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-22 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-22 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-22 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-22 .field-label}

#### 200 {#section-22 .field-label}

node create request result v0.0.44_openapi_resp

#### default {#default-22 .field-label}

node create request result v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

:::::::::::::: method
[]{#slurmV0044PostNode}

::: method-path
[]{#slurmV0044PostNode} Up

``` post
post /slurm/v0.0.44/node/{node_name}
```
:::

::: method-summary
update node properties ([slurmV0044PostNode]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-9 .field-label}

::::: field-items
::: param
node_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Node name default: null
:::
:::::

### Consumes {#consumes-5 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-5 .field-label}

::::: field-items
::: param
v0.0.44_update_node_msg v0.0.44_update_node_msg (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-23 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-23 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-23 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-23 .field-label}

#### 200 {#section-23 .field-label}

node update request result v0.0.44_openapi_resp

#### default {#default-23 .field-label}

node update request result v0.0.44_openapi_resp
::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044PostNodes}

::: method-path
[]{#slurmV0044PostNodes} Up

``` post
post /slurm/v0.0.44/nodes/
```
:::

::: method-summary
batch update node(s) ([slurmV0044PostNodes]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-6 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-6 .field-label}

::::: field-items
::: param
v0.0.44_update_node_msg v0.0.44_update_node_msg (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-24 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-24 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-24 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-24 .field-label}

#### 200 {#section-24 .field-label}

batch node update request result v0.0.44_openapi_resp

#### default {#default-24 .field-label}

batch node update request result v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044PostReservation}

::: method-path
[]{#slurmV0044PostReservation} Up

``` post
post /slurm/v0.0.44/reservation
```
:::

::: method-summary
create or update a reservation ([slurmV0044PostReservation]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-7 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-7 .field-label}

::::: field-items
::: param
v0.0.44_reservation_desc_msg v0.0.44_reservation_desc_msg (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-25 .field-label}

::: return-type
v0.0.44_openapi_reservation_mod_resp
:::

### Example data {#example-data-25 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-25 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-25 .field-label}

#### 200 {#section-25 .field-label}

reservation description v0.0.44_openapi_reservation_mod_resp

#### default {#default-25 .field-label}

reservation description v0.0.44_openapi_reservation_mod_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmV0044PostReservations}

::: method-path
[]{#slurmV0044PostReservations} Up

``` post
post /slurm/v0.0.44/reservations/
```
:::

::: method-summary
create or update reservations ([slurmV0044PostReservations]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-8 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-8 .field-label}

::::: field-items
::: param
v0.0.44_reservation_mod_req v0.0.44_reservation_mod_req (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-26 .field-label}

::: return-type
v0.0.44_openapi_reservation_mod_resp
:::

### Example data {#example-data-26 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "reservations" : [ {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  }, {
    "end_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "flags" : [ "MAINT", "MAINT" ],
    "groups" : [ "groups", "groups" ],
    "users" : [ "users", "users" ],
    "max_start_delay" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "duration" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "features" : "features",
    "start_time" : {
      "number" : 2,
      "set" : true,
      "infinite" : true
    },
    "burst_buffer" : "burst_buffer",
    "licenses" : [ "licenses", "licenses" ],
    "partition" : "partition",
    "name" : "name",
    "comment" : "comment",
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "accounts" : [ "accounts", "accounts" ],
    "node_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "node_list" : [ "node_list", "node_list" ],
    "purge_completed" : {
      "time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "core_count" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-26 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-26 .field-label}

#### 200 {#section-26 .field-label}

reservation descriptions v0.0.44_openapi_reservation_mod_resp

#### default {#default-26 .field-label}

reservation descriptions v0.0.44_openapi_reservation_mod_resp
:::::::::::

------------------------------------------------------------------------

# [Slurmdb]{#Slurmdb}

::::::::::: method
[]{#slurmdbV0044DeleteAccount}

::: method-path
[]{#slurmdbV0044DeleteAccount} Up

``` delete
delete /slurmdb/v0.0.44/account/{account_name}
```
:::

::: method-summary
Delete account ([slurmdbV0044DeleteAccount]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-10 .field-label}

::::: field-items
::: param
account_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Account name default: null
:::
:::::

### Return type {#return-type-27 .field-label}

::: return-type
v0.0.44_openapi_accounts_removed_resp
:::

### Example data {#example-data-27 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "removed_accounts" : [ "removed_accounts", "removed_accounts" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-27 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-27 .field-label}

#### 200 {#section-27 .field-label}

Status of account deletion request v0.0.44_openapi_accounts_removed_resp

#### default {#default-27 .field-label}

Status of account deletion request v0.0.44_openapi_accounts_removed_resp
:::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044DeleteAssociation}

::: method-path
[]{#slurmdbV0044DeleteAssociation} Up

``` delete
delete /slurmdb/v0.0.44/association/
```
:::

::: method-summary
Delete association ([slurmdbV0044DeleteAssociation]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-11 .field-label}

::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV accounts list default: null
:::

::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV clusters list default: null
:::

::: param
default_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
Include deleted associations (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Filter to only defaults (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include the raw QOS or delta_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include sub acct information (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude parent id/name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude limits from parents (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV ID list default: null
:::

::: param
parent_account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV names of parent account default: null
:::

::: param
partition (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV partition name list default: null
:::

::: param
qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
user (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV user list default: null
:::
:::::::::::::::::::::::::::::::::::::::

### Return type {#return-type-28 .field-label}

::: return-type
v0.0.44_openapi_assocs_removed_resp
:::

### Example data {#example-data-28 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "removed_associations" : [ "removed_associations", "removed_associations" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-28 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-28 .field-label}

#### 200 {#section-28 .field-label}

Status of associations delete request v0.0.44_openapi_assocs_removed_resp

#### default {#default-28 .field-label}

Status of associations delete request v0.0.44_openapi_assocs_removed_resp
:::::::::::::::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044DeleteAssociations}

::: method-path
[]{#slurmdbV0044DeleteAssociations} Up

``` delete
delete /slurmdb/v0.0.44/associations/
```
:::

::: method-summary
Delete associations ([slurmdbV0044DeleteAssociations]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-12 .field-label}

::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV accounts list default: null
:::

::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV clusters list default: null
:::

::: param
default_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
Include deleted associations (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Filter to only defaults (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include the raw QOS or delta_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include sub acct information (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude parent id/name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude limits from parents (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV ID list default: null
:::

::: param
parent_account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV names of parent account default: null
:::

::: param
partition (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV partition name list default: null
:::

::: param
qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
user (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV user list default: null
:::
:::::::::::::::::::::::::::::::::::::::

### Return type {#return-type-29 .field-label}

::: return-type
v0.0.44_openapi_assocs_removed_resp
:::

### Example data {#example-data-29 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "removed_associations" : [ "removed_associations", "removed_associations" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-29 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-29 .field-label}

#### 200 {#section-29 .field-label}

List of associations deleted v0.0.44_openapi_assocs_removed_resp

#### default {#default-29 .field-label}

List of associations deleted v0.0.44_openapi_assocs_removed_resp
:::::::::::::::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

:::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044DeleteCluster}

::: method-path
[]{#slurmdbV0044DeleteCluster} Up

``` delete
delete /slurmdb/v0.0.44/cluster/{cluster_name}
```
:::

::: method-summary
Delete cluster ([slurmdbV0044DeleteCluster]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-11 .field-label}

::::: field-items
::: param
cluster_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Cluster name default: null
:::
:::::

### Query parameters {#query-parameters-13 .field-label}

::::::::::::::::::::::: field-items
::: param
classification (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Type of machine default: null
:::

::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV cluster list default: null
:::

::: param
federation (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV federation list default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
rpc_version (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV RPC version list default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include deleted clusters default: null
:::

::: param
with_usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include usage default: null
:::
:::::::::::::::::::::::

### Return type {#return-type-30 .field-label}

::: return-type
v0.0.44_openapi_clusters_removed_resp
:::

### Example data {#example-data-30 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "deleted_clusters" : [ "deleted_clusters", "deleted_clusters" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-30 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-30 .field-label}

#### 200 {#section-30 .field-label}

Result of delete cluster request v0.0.44_openapi_clusters_removed_resp

#### default {#default-30 .field-label}

Result of delete cluster request v0.0.44_openapi_clusters_removed_resp
::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044DeleteSingleQos}

::: method-path
[]{#slurmdbV0044DeleteSingleQos} Up

``` delete
delete /slurmdb/v0.0.44/qos/{qos}
```
:::

::: method-summary
Delete QOS ([slurmdbV0044DeleteSingleQos]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-12 .field-label}

::::: field-items
::: param
qos (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" QOS name default: null
:::
:::::

### Return type {#return-type-31 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_qos_removed_resp
:::

### Example data {#example-data-31 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "removed_qos" : [ "removed_qos", "removed_qos" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-31 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-31 .field-label}

#### 200 {#section-31 .field-label}

results of ping test v0.0.44_openapi_slurmdbd_qos_removed_resp

#### default {#default-31 .field-label}

results of ping test v0.0.44_openapi_slurmdbd_qos_removed_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044DeleteUser}

::: method-path
[]{#slurmdbV0044DeleteUser} Up

``` delete
delete /slurmdb/v0.0.44/user/{name}
```
:::

::: method-summary
Delete user ([slurmdbV0044DeleteUser]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-13 .field-label}

::::: field-items
::: param
name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" User name default: null
:::
:::::

### Return type {#return-type-32 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-32 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-32 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-32 .field-label}

#### 200 {#section-32 .field-label}

Result of user delete request v0.0.44_openapi_resp

#### default {#default-32 .field-label}

Result of user delete request v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044DeleteWckey}

::: method-path
[]{#slurmdbV0044DeleteWckey} Up

``` delete
delete /slurmdb/v0.0.44/wckey/{id}
```
:::

::: method-summary
Delete wckey ([slurmdbV0044DeleteWckey]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-14 .field-label}

::::: field-items
::: param
id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" WCKey ID default: null
:::
:::::

### Return type {#return-type-33 .field-label}

::: return-type
v0.0.44_openapi_wckey_removed_resp
:::

### Example data {#example-data-33 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "deleted_wckeys" : [ "deleted_wckeys", "deleted_wckeys" ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-33 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-33 .field-label}

#### 200 {#section-33 .field-label}

Result of wckey deletion request v0.0.44_openapi_wckey_removed_resp

#### default {#default-33 .field-label}

Result of wckey deletion request v0.0.44_openapi_wckey_removed_resp
:::::::::::

------------------------------------------------------------------------

:::::::::::::::::: method
[]{#slurmdbV0044GetAccount}

::: method-path
[]{#slurmdbV0044GetAccount} Up

``` get
get /slurmdb/v0.0.44/account/{account_name}
```
:::

::: method-summary
Get account info ([slurmdbV0044GetAccount]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-15 .field-label}

::::: field-items
::: param
account_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Account name default: null
:::
:::::

### Query parameters {#query-parameters-14 .field-label}

::::::::: field-items
::: param
with_assocs (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include associations default: null
:::

::: param
with_coords (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include coordinators default: null
:::

::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include deleted default: null
:::
:::::::::

### Return type {#return-type-34 .field-label}

::: return-type
v0.0.44_openapi_accounts_resp
:::

### Example data {#example-data-34 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "accounts" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-34 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-34 .field-label}

#### 200 {#section-34 .field-label}

List of accounts v0.0.44_openapi_accounts_resp

#### default {#default-34 .field-label}

List of accounts v0.0.44_openapi_accounts_resp
::::::::::::::::::

------------------------------------------------------------------------

::::::::::::::::::::: method
[]{#slurmdbV0044GetAccounts}

::: method-path
[]{#slurmdbV0044GetAccounts} Up

``` get
get /slurmdb/v0.0.44/accounts/
```
:::

::: method-summary
Get account list ([slurmdbV0044GetAccounts]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-15 .field-label}

::::::::::::::: field-items
::: param
description (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV description list default: null
:::

::: param
DELETED (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" include deleted associations default: null
:::

::: param
WithAssociations (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" query includes associations default: null
:::

::: param
WithCoordinators (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" query includes coordinators default: null
:::

::: param
NoUsersAreCoords (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" remove users as coordinators default: null
:::

::: param
UsersAreCoords (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" users are coordinators default: null
:::
:::::::::::::::

### Return type {#return-type-35 .field-label}

::: return-type
v0.0.44_openapi_accounts_resp
:::

### Example data {#example-data-35 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "accounts" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-35 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-35 .field-label}

#### 200 {#section-35 .field-label}

List of accounts v0.0.44_openapi_accounts_resp

#### default {#default-35 .field-label}

List of accounts v0.0.44_openapi_accounts_resp
:::::::::::::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044GetAssociation}

::: method-path
[]{#slurmdbV0044GetAssociation} Up

``` get
get /slurmdb/v0.0.44/association/
```
:::

::: method-summary
Get association info ([slurmdbV0044GetAssociation]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-16 .field-label}

::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV accounts list default: null
:::

::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV clusters list default: null
:::

::: param
default_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
Include deleted associations (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Filter to only defaults (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include the raw QOS or delta_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include sub acct information (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude parent id/name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude limits from parents (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV ID list default: null
:::

::: param
parent_account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV names of parent account default: null
:::

::: param
partition (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV partition name list default: null
:::

::: param
qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
user (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV user list default: null
:::
:::::::::::::::::::::::::::::::::::::::

### Return type {#return-type-36 .field-label}

::: return-type
v0.0.44_openapi_assocs_resp
:::

### Example data {#example-data-36 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "associations" : [ {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  }, {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-36 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-36 .field-label}

#### 200 {#section-36 .field-label}

List of associations v0.0.44_openapi_assocs_resp

#### default {#default-36 .field-label}

List of associations v0.0.44_openapi_assocs_resp
:::::::::::::::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044GetAssociations}

::: method-path
[]{#slurmdbV0044GetAssociations} Up

``` get
get /slurmdb/v0.0.44/associations/
```
:::

::: method-summary
Get association list ([slurmdbV0044GetAssociations]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-17 .field-label}

::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV accounts list default: null
:::

::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV clusters list default: null
:::

::: param
default_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
Include deleted associations (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Filter to only defaults (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include the raw QOS or delta_qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Include sub acct information (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude parent id/name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
Exclude limits from parents (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV ID list default: null
:::

::: param
parent_account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV names of parent account default: null
:::

::: param
partition (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV partition name list default: null
:::

::: param
qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS list default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
user (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV user list default: null
:::
:::::::::::::::::::::::::::::::::::::::

### Return type {#return-type-37 .field-label}

::: return-type
v0.0.44_openapi_assocs_resp
:::

### Example data {#example-data-37 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "associations" : [ {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  }, {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-37 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-37 .field-label}

#### 200 {#section-37 .field-label}

List of associations v0.0.44_openapi_assocs_resp

#### default {#default-37 .field-label}

List of associations v0.0.44_openapi_assocs_resp
:::::::::::::::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

:::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044GetCluster}

::: method-path
[]{#slurmdbV0044GetCluster} Up

``` get
get /slurmdb/v0.0.44/cluster/{cluster_name}
```
:::

::: method-summary
Get cluster info ([slurmdbV0044GetCluster]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-16 .field-label}

::::: field-items
::: param
cluster_name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Cluster name default: null
:::
:::::

### Query parameters {#query-parameters-18 .field-label}

::::::::::::::::::::::: field-items
::: param
classification (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Type of machine default: null
:::

::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV cluster list default: null
:::

::: param
federation (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV federation list default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
rpc_version (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV RPC version list default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include deleted clusters default: null
:::

::: param
with_usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include usage default: null
:::
:::::::::::::::::::::::

### Return type {#return-type-38 .field-label}

::: return-type
v0.0.44_openapi_clusters_resp
:::

### Example data {#example-data-38 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "clusters" : [ {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  }, {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-38 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-38 .field-label}

#### 200 {#section-38 .field-label}

Cluster information v0.0.44_openapi_clusters_resp

#### default {#default-38 .field-label}

Cluster information v0.0.44_openapi_clusters_resp
::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044GetClusters}

::: method-path
[]{#slurmdbV0044GetClusters} Up

``` get
get /slurmdb/v0.0.44/clusters/
```
:::

::: method-summary
Get cluster list ([slurmdbV0044GetClusters]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-19 .field-label}

::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query reservations updated more recently than this time (UNIX timestamp) default: null
:::
:::::

### Return type {#return-type-39 .field-label}

::: return-type
v0.0.44_openapi_clusters_resp
:::

### Example data {#example-data-39 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "clusters" : [ {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  }, {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-39 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-39 .field-label}

#### 200 {#section-39 .field-label}

List of clusters v0.0.44_openapi_clusters_resp

#### default {#default-39 .field-label}

List of clusters v0.0.44_openapi_clusters_resp
:::::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmdbV0044GetConfig}

::: method-path
[]{#slurmdbV0044GetConfig} Up

``` get
get /slurmdb/v0.0.44/config
```
:::

::: method-summary
Dump all configuration information ([slurmdbV0044GetConfig]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-40 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_config_resp
:::

### Example data {#example-data-40 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "associations" : [ {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  }, {
    "lineage" : "lineage",
    "cluster" : "cluster",
    "shares_raw" : 1,
    "max" : {
      "jobs" : {
        "total" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "active" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "accruing" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "per" : {
          "submitted" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "tres" : {
        "total" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ],
        "minutes" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "per" : {
          "node" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "job" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "group" : {
          "minutes" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "active" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        }
      },
      "per" : {
        "account" : {
          "wall_clock" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      }
    },
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "is_default" : true,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "parent_account" : "parent_account",
    "default" : {
      "qos" : "qos"
    },
    "min" : {
      "priority_threshold" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "partition" : "partition",
    "qos" : [ "qos", "qos" ],
    "comment" : "comment",
    "id" : 7,
    "user" : "user",
    "account" : "account"
  } ],
  "qos" : [ {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  }, {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  } ],
  "wckeys" : [ {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  }, {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  } ],
  "instances" : [ {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  }, {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "tres" : [ {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  }, {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  } ],
  "accounts" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "organization" : "organization",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "description" : "description"
  } ],
  "clusters" : [ {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  }, {
    "associations" : {
      "root" : {
        "cluster" : "cluster",
        "partition" : "partition",
        "id" : 5,
        "user" : "user",
        "account" : "account"
      }
    },
    "controller" : {
      "port" : 0,
      "host" : "host"
    },
    "nodes" : "nodes",
    "flags" : [ "DELETED", "DELETED" ],
    "name" : "name",
    "rpc_version" : 6,
    "tres" : [ {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    }, {
      "name" : "name",
      "count" : 0,
      "id" : 7,
      "type" : "type"
    } ],
    "select_plugin" : "select_plugin"
  } ],
  "users" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-40 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-40 .field-label}

#### 200 {#section-40 .field-label}

slurmdbd configuration v0.0.44_openapi_slurmdbd_config_resp

#### default {#default-40 .field-label}

slurmdbd configuration v0.0.44_openapi_slurmdbd_config_resp
::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmdbV0044GetDiag}

::: method-path
[]{#slurmdbV0044GetDiag} Up

``` get
get /slurmdb/v0.0.44/diag/
```
:::

::: method-summary
Get slurmdb diagnostics ([slurmdbV0044GetDiag]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-41 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_stats_resp
:::

### Example data {#example-data-41 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "statistics" : {
    "time_start" : 0,
    "RPCs" : [ {
      "rpc" : "rpc",
      "count" : 7,
      "time" : {
        "average" : 1,
        "total" : 4
      }
    }, {
      "rpc" : "rpc",
      "count" : 7,
      "time" : {
        "average" : 1,
        "total" : 4
      }
    } ],
    "rollups" : {
      "daily" : {
        "duration" : {
          "last" : 3,
          "max" : 2,
          "time" : 4
        },
        "count" : 7,
        "last_run" : 9
      },
      "monthly" : {
        "duration" : {
          "last" : 1,
          "max" : 1,
          "time" : 6
        },
        "count" : 7,
        "last_run" : 1
      },
      "hourly" : {
        "duration" : {
          "last" : 5,
          "max" : 5,
          "time" : 2
        },
        "count" : 6,
        "last_run" : 1
      }
    },
    "users" : [ {
      "count" : 5,
      "time" : {
        "average" : 1,
        "total" : 4
      },
      "user" : "user"
    }, {
      "count" : 5,
      "time" : {
        "average" : 1,
        "total" : 4
      },
      "user" : "user"
    } ]
  }
}
```

### Produces {#produces-41 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-41 .field-label}

#### 200 {#section-41 .field-label}

Dictionary of statistics v0.0.44_openapi_slurmdbd_stats_resp

#### default {#default-41 .field-label}

Dictionary of statistics v0.0.44_openapi_slurmdbd_stats_resp
::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::: method
[]{#slurmdbV0044GetInstance}

::: method-path
[]{#slurmdbV0044GetInstance} Up

``` get
get /slurmdb/v0.0.44/instance/
```
:::

::: method-summary
Get instance info ([slurmdbV0044GetInstance]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-20 .field-label}

::::::::::::::::::: field-items
::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV clusters list default: null
:::

::: param
extra (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV extra list default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
instance_id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV instance_id list default: null
:::

::: param
instance_type (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV instance_type list default: null
:::

::: param
node_list (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ranged node string default: null
:::

::: param
time_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Time end (UNIX timestamp) default: null
:::

::: param
time_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Time start (UNIX timestamp) default: null
:::
:::::::::::::::::::

### Return type {#return-type-42 .field-label}

::: return-type
v0.0.44_openapi_instances_resp
:::

### Example data {#example-data-42 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "instances" : [ {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  }, {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-42 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-42 .field-label}

#### 200 {#section-42 .field-label}

List of instances v0.0.44_openapi_instances_resp

#### default {#default-42 .field-label}

List of instances v0.0.44_openapi_instances_resp
:::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::: method
[]{#slurmdbV0044GetInstances}

::: method-path
[]{#slurmdbV0044GetInstances} Up

``` get
get /slurmdb/v0.0.44/instances/
```
:::

::: method-summary
Get instance list ([slurmdbV0044GetInstances]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-21 .field-label}

::::::::::::::::::: field-items
::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV clusters list default: null
:::

::: param
extra (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV extra list default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
instance_id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV instance_id list default: null
:::

::: param
instance_type (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV instance_type list default: null
:::

::: param
node_list (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ranged node string default: null
:::

::: param
time_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Time end (UNIX timestamp) default: null
:::

::: param
time_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Time start (UNIX timestamp) default: null
:::
:::::::::::::::::::

### Return type {#return-type-43 .field-label}

::: return-type
v0.0.44_openapi_instances_resp
:::

### Example data {#example-data-43 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "instances" : [ {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  }, {
    "cluster" : "cluster",
    "instance_id" : "instance_id",
    "extra" : "extra",
    "node_name" : "node_name",
    "time" : {
      "time_start" : 1,
      "time_end" : 1
    },
    "instance_type" : "instance_type"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-43 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-43 .field-label}

#### 200 {#section-43 .field-label}

List of instances v0.0.44_openapi_instances_resp

#### default {#default-43 .field-label}

List of instances v0.0.44_openapi_instances_resp
:::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044GetJob}

::: method-path
[]{#slurmdbV0044GetJob} Up

``` get
get /slurmdb/v0.0.44/job/{job_id}
```
:::

::: method-summary
Get job info ([slurmdbV0044GetJob]{.nickname})
:::

::: method-notes
This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.
:::

### Path parameters {#path-parameters-17 .field-label}

::::: field-items
::: param
job_id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Job ID default: null
:::
:::::

### Return type {#return-type-44 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_jobs_resp
:::

### Example data {#example-data-44 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  } ],
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-44 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-44 .field-label}

#### 200 {#section-44 .field-label}

Job description v0.0.44_openapi_slurmdbd_jobs_resp

#### default {#default-44 .field-label}

Job description v0.0.44_openapi_slurmdbd_jobs_resp
:::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044GetJobs}

::: method-path
[]{#slurmdbV0044GetJobs} Up

``` get
get /slurmdb/v0.0.44/jobs/
```
:::

::: method-summary
Get job list ([slurmdbV0044GetJobs]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-22 .field-label}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV account list default: null
:::

::: param
association (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV association list default: null
:::

::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV cluster list default: null
:::

::: param
constraints (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV constraint list default: null
:::

::: param
scheduler_unset (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Schedule bits not set default: null
:::

::: param
scheduled_on_submit (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Job was started on submit default: null
:::

::: param
scheduled_by_main (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Job was started from main scheduler default: null
:::

::: param
scheduled_by_backfill (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Job was started from backfill default: null
:::

::: param
job_started (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Job start RPC was received default: null
:::

::: param
job_altered (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Job record has been altered default: null
:::

::: param
exit_code (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Job exit code (numeric) default: null
:::

::: param
show_duplicates (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include duplicate job entries default: null
:::

::: param
skip_steps (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Exclude job step details default: null
:::

::: param
disable_truncate_usage_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Do not truncate the time to usage_start and usage_end default: null
:::

::: param
whole_hetjob (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include details on all hetjob components default: null
:::

::: param
disable_whole_hetjob (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Only show details on specified hetjob components default: null
:::

::: param
disable_wait_for_result (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Tell dbd not to wait for the result default: null
:::

::: param
usage_time_as_submit_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Use usage_time as the submit_time of the job default: null
:::

::: param
show_batch_script (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include job script default: null
:::

::: param
show_job_environment (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include job environment default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
groups (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV group list default: null
:::

::: param
job_name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV job name list default: null
:::

::: param
partition (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV partition name list default: null
:::

::: param
qos (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS name list default: null
:::

::: param
reason (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV reason list default: null
:::

::: param
reservation (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV reservation name list default: null
:::

::: param
reservation_id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV reservation ID list default: null
:::

::: param
state (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV state list default: null
:::

::: param
step (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV step id list default: null
:::

::: param
end_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
start_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
node (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ranged node string where jobs ran default: null
:::

::: param
users (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV user name list default: null
:::

::: param
wckey (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV WCKey list default: null
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

### Return type {#return-type-45 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_jobs_resp
:::

### Example data {#example-data-45 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "jobs" : [ {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  }, {
    "container" : "container",
    "cluster" : "cluster",
    "stdin_expanded" : "stdin_expanded",
    "stdin" : "stdin",
    "stdout" : "stdout",
    "stderr_expanded" : "stderr_expanded",
    "flags" : [ "NONE", "NONE" ],
    "used_gres" : "used_gres",
    "association" : {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    },
    "allocation_nodes" : 0,
    "working_directory" : "working_directory",
    "qosreq" : "qosreq",
    "constraints" : "constraints",
    "required" : {
      "memory_per_node" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "CPUs" : 9,
      "memory_per_cpu" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      }
    },
    "stdout_expanded" : "stdout_expanded",
    "hold" : true,
    "restart_cnt" : 6,
    "partition" : "partition",
    "segment_size" : 9,
    "qos" : "qos",
    "array" : {
      "task" : "task",
      "job_id" : 6,
      "task_id" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "limits" : {
        "max" : {
          "running" : {
            "tasks" : 1
          }
        }
      }
    },
    "het" : {
      "job_id" : 5,
      "job_offset" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      }
    },
    "submit_line" : "submit_line",
    "extra" : "extra",
    "reservation" : {
      "requested" : "requested",
      "name" : "name",
      "id" : 8
    },
    "block" : "block",
    "tres" : {
      "requested" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ],
      "allocated" : [ {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      }, {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      } ]
    },
    "state" : {
      "reason" : "reason",
      "current" : [ "PENDING", "PENDING" ]
    },
    "mcs" : {
      "label" : "label"
    },
    "group" : "group",
    "wckey" : {
      "wckey" : "wckey",
      "flags" : [ "ASSIGNED_DEFAULT", "ASSIGNED_DEFAULT" ]
    },
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "stderr" : "stderr",
    "steps" : [ {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    }, {
      "nodes" : {
        "count" : 6,
        "range" : "range",
        "list" : [ "list", "list" ]
      },
      "task" : {
        "distribution" : "distribution"
      },
      "exit_code" : {
        "return_code" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "signal" : {
          "name" : "name",
          "id" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        },
        "status" : [ "INVALID", "INVALID" ]
      },
      "kill_request_user" : "kill_request_user",
      "CPU" : {
        "governor" : "governor",
        "requested_frequency" : {
          "min" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "max" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "pid" : "pid",
      "step" : {
        "stdin_expanded" : "stdin_expanded",
        "stdin" : "stdin",
        "stdout" : "stdout",
        "stderr_expanded" : "stderr_expanded",
        "name" : "name",
        "id" : "id",
        "stderr" : "stderr",
        "stdout_expanded" : "stdout_expanded"
      },
      "tres" : {
        "consumed" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "requested" : {
          "average" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "min" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "max" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ]
        },
        "allocated" : [ {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        }, {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        } ]
      },
      "time" : {
        "elapsed" : 6,
        "total" : {
          "seconds" : 2,
          "microseconds" : 6
        },
        "system" : {
          "seconds" : 6,
          "microseconds" : 1
        },
        "start" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "limit" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "end" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        },
        "user" : {
          "seconds" : 6,
          "microseconds" : 5
        },
        "suspended" : 3
      },
      "state" : [ "PENDING", "PENDING" ],
      "tasks" : {
        "count" : 3
      },
      "statistics" : {
        "CPU" : {
          "actual_frequency" : 3
        },
        "energy" : {
          "consumed" : {
            "number" : 2,
            "set" : true,
            "infinite" : true
          }
        }
      }
    } ],
    "script" : "script",
    "failed_node" : "failed_node",
    "derived_exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "licenses" : "licenses",
    "nodes" : "nodes",
    "job_id" : 9,
    "exit_code" : {
      "return_code" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "signal" : {
        "name" : "name",
        "id" : {
          "number" : 2,
          "set" : true,
          "infinite" : true
        }
      },
      "status" : [ "INVALID", "INVALID" ]
    },
    "name" : "name",
    "kill_request_user" : "kill_request_user",
    "comment" : {
      "administrator" : "administrator",
      "system" : "system",
      "job" : "job"
    },
    "time" : {
      "elapsed" : 7,
      "total" : {
        "seconds" : 6,
        "microseconds" : 7
      },
      "system" : {
        "seconds" : 1,
        "microseconds" : 1
      },
      "eligible" : 9,
      "start" : 4,
      "limit" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "end" : 3,
      "submission" : 7,
      "planned" : {
        "number" : 2,
        "set" : true,
        "infinite" : true
      },
      "user" : {
        "seconds" : 1,
        "microseconds" : 4
      },
      "suspended" : 1
    },
    "user" : "user",
    "account" : "account"
  } ],
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-45 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-45 .field-label}

#### 200 {#section-45 .field-label}

List of jobs v0.0.44_openapi_slurmdbd_jobs_resp

#### default {#default-45 .field-label}

List of jobs v0.0.44_openapi_slurmdbd_jobs_resp
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmdbV0044GetPing}

::: method-path
[]{#slurmdbV0044GetPing} Up

``` get
get /slurmdb/v0.0.44/ping/
```
:::

::: method-summary
ping test ([slurmdbV0044GetPing]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-46 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_ping_resp
:::

### Example data {#example-data-46 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "pings" : [ {
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "primary" : true
  }, {
    "responding" : true,
    "hostname" : "hostname",
    "latency" : 0,
    "primary" : true
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-46 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-46 .field-label}

#### 200 {#section-46 .field-label}

results of ping test v0.0.44_openapi_slurmdbd_ping_resp

#### default {#default-46 .field-label}

results of ping test v0.0.44_openapi_slurmdbd_ping_resp
::::::::

------------------------------------------------------------------------

::::::::::::::::::::: method
[]{#slurmdbV0044GetQos}

::: method-path
[]{#slurmdbV0044GetQos} Up

``` get
get /slurmdb/v0.0.44/qos/
```
:::

::: method-summary
Get QOS list ([slurmdbV0044GetQos]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-23 .field-label}

::::::::::::::: field-items
::: param
description (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV description list default: null
:::

::: param
Include deleted QOS (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS id list default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS name list default: null
:::

::: param
preempt_mode (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" PreemptMode used when jobs in this QOS are preempted default: null
:::
:::::::::::::::

### Return type {#return-type-47 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_qos_resp
:::

### Example data {#example-data-47 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "qos" : [ {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  }, {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-47 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-47 .field-label}

#### 200 {#section-47 .field-label}

List of QOS v0.0.44_openapi_slurmdbd_qos_resp

#### default {#default-47 .field-label}

List of QOS v0.0.44_openapi_slurmdbd_qos_resp
:::::::::::::::::::::

------------------------------------------------------------------------

:::::::::::::: method
[]{#slurmdbV0044GetSingleQos}

::: method-path
[]{#slurmdbV0044GetSingleQos} Up

``` get
get /slurmdb/v0.0.44/qos/{qos}
```
:::

::: method-summary
Get QOS info ([slurmdbV0044GetSingleQos]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-18 .field-label}

::::: field-items
::: param
qos (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" QOS name default: null
:::
:::::

### Query parameters {#query-parameters-24 .field-label}

::::: field-items
::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query includes deleted QOS default: null
:::
:::::

### Return type {#return-type-48 .field-label}

::: return-type
v0.0.44_openapi_slurmdbd_qos_resp
:::

### Example data {#example-data-48 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "qos" : [ {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  }, {
    "flags" : [ "NOT_SET", "NOT_SET" ],
    "name" : "name",
    "usage_threshold" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "description" : "description",
    "usage_factor" : {
      "number" : 4.145608029883936,
      "set" : true,
      "infinite" : true
    },
    "id" : 3,
    "priority" : {
      "number" : 5,
      "set" : true,
      "infinite" : true
    },
    "limits" : {
      "min" : {
        "priority_threshold" : {
          "number" : 5,
          "set" : true,
          "infinite" : true
        },
        "tres" : {
          "per" : {
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        }
      },
      "max" : {
        "jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          },
          "active_jobs" : {
            "per" : {
              "user" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              },
              "account" : {
                "number" : 5,
                "set" : true,
                "infinite" : true
              }
            }
          }
        },
        "accruing" : {
          "per" : {
            "user" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "account" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "tres" : {
          "total" : [ {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          }, {
            "name" : "name",
            "count" : 0,
            "id" : 7,
            "type" : "type"
          } ],
          "minutes" : {
            "total" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "per" : {
              "qos" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "job" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "user" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ],
              "account" : [ {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              }, {
                "name" : "name",
                "count" : 0,
                "id" : 7,
                "type" : "type"
              } ]
            }
          },
          "per" : {
            "node" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "job" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "user" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ],
            "account" : [ {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            }, {
              "name" : "name",
              "count" : 0,
              "id" : 7,
              "type" : "type"
            } ]
          }
        },
        "wall_clock" : {
          "per" : {
            "qos" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            },
            "job" : {
              "number" : 5,
              "set" : true,
              "infinite" : true
            }
          }
        },
        "active_jobs" : {
          "count" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          },
          "accruing" : {
            "number" : 5,
            "set" : true,
            "infinite" : true
          }
        }
      },
      "factor" : {
        "number" : 4.145608029883936,
        "set" : true,
        "infinite" : true
      },
      "grace_time" : 2
    },
    "preempt" : {
      "mode" : [ "DISABLED", "DISABLED" ],
      "exempt_time" : {
        "number" : 5,
        "set" : true,
        "infinite" : true
      },
      "list" : [ "list", "list" ]
    }
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-48 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-48 .field-label}

#### 200 {#section-48 .field-label}

QOS information v0.0.44_openapi_slurmdbd_qos_resp

#### default {#default-48 .field-label}

QOS information v0.0.44_openapi_slurmdbd_qos_resp
::::::::::::::

------------------------------------------------------------------------

:::::::: method
[]{#slurmdbV0044GetTres}

::: method-path
[]{#slurmdbV0044GetTres} Up

``` get
get /slurmdb/v0.0.44/tres/
```
:::

::: method-summary
Get TRES info ([slurmdbV0044GetTres]{.nickname})
:::

::: method-notes
:::

### Return type {#return-type-49 .field-label}

::: return-type
v0.0.44_openapi_tres_resp
:::

### Example data {#example-data-49 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "TRES" : [ {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  }, {
    "name" : "name",
    "count" : 0,
    "id" : 7,
    "type" : "type"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-49 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-49 .field-label}

#### 200 {#section-49 .field-label}

List of TRES v0.0.44_openapi_tres_resp

#### default {#default-49 .field-label}

List of TRES v0.0.44_openapi_tres_resp
::::::::

------------------------------------------------------------------------

:::::::::::::::::::: method
[]{#slurmdbV0044GetUser}

::: method-path
[]{#slurmdbV0044GetUser} Up

``` get
get /slurmdb/v0.0.44/user/{name}
```
:::

::: method-summary
Get user info ([slurmdbV0044GetUser]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-19 .field-label}

::::: field-items
::: param
name (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" User name default: null
:::
:::::

### Query parameters {#query-parameters-25 .field-label}

::::::::::: field-items
::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include deleted users default: null
:::

::: param
with_assocs (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include associations default: null
:::

::: param
with_coords (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include coordinators default: null
:::

::: param
with_wckeys (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include WCKeys default: null
:::
:::::::::::

### Return type {#return-type-50 .field-label}

::: return-type
v0.0.44_openapi_users_resp
:::

### Example data {#example-data-50 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "users" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-50 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-50 .field-label}

#### 200 {#section-50 .field-label}

List of users v0.0.44_openapi_users_resp

#### default {#default-50 .field-label}

List of users v0.0.44_openapi_users_resp
::::::::::::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::: method
[]{#slurmdbV0044GetUsers}

::: method-path
[]{#slurmdbV0044GetUsers} Up

``` get
get /slurmdb/v0.0.44/users/
```
:::

::: method-summary
Get user list ([slurmdbV0044GetUsers]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-26 .field-label}

::::::::::::::::::: field-items
::: param
admin_level (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Administrator level default: null
:::

::: param
default_account (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV default account list default: null
:::

::: param
default_wckey (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV default WCKey list default: null
:::

::: param
with_assocs (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" With associations default: null
:::

::: param
with_coords (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" With coordinators default: null
:::

::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" With deleted default: null
:::

::: param
with_wckeys (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" With WCKeys default: null
:::

::: param
without_defaults (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Exclude defaults default: null
:::
:::::::::::::::::::

### Return type {#return-type-51 .field-label}

::: return-type
v0.0.44_openapi_users_resp
:::

### Example data {#example-data-51 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "users" : [ {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  }, {
    "associations" : [ {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    }, {
      "cluster" : "cluster",
      "partition" : "partition",
      "id" : 5,
      "user" : "user",
      "account" : "account"
    } ],
    "default" : {
      "qos" : 1,
      "wckey" : "wckey",
      "account" : "account"
    },
    "administrator_level" : [ "Not Set", "Not Set" ],
    "old_name" : "old_name",
    "wckeys" : [ {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    }, {
      "cluster" : "cluster",
      "name" : "name",
      "flags" : [ "DELETED", "DELETED" ],
      "accounting" : [ {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      }, {
        "start" : 7,
        "id" : 5,
        "TRES" : {
          "name" : "name",
          "count" : 0,
          "id" : 7,
          "type" : "type"
        },
        "allocated" : {
          "seconds" : 5
        },
        "id_alt" : 2
      } ],
      "id" : 9,
      "user" : "user"
    } ],
    "coordinators" : [ {
      "name" : "name",
      "direct" : true
    }, {
      "name" : "name",
      "direct" : true
    } ],
    "flags" : [ "NONE", "NONE" ],
    "name" : "name"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-51 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-51 .field-label}

#### 200 {#section-51 .field-label}

List of users v0.0.44_openapi_users_resp

#### default {#default-51 .field-label}

List of users v0.0.44_openapi_users_resp
:::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044GetWckey}

::: method-path
[]{#slurmdbV0044GetWckey} Up

``` get
get /slurmdb/v0.0.44/wckey/{id}
```
:::

::: method-summary
Get wckey info ([slurmdbV0044GetWckey]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-20 .field-label}

::::: field-items
::: param
id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" WCKey ID default: null
:::
:::::

### Return type {#return-type-52 .field-label}

::: return-type
v0.0.44_openapi_wckey_resp
:::

### Example data {#example-data-52 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "wckeys" : [ {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  }, {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-52 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-52 .field-label}

#### 200 {#section-52 .field-label}

Description of wckey v0.0.44_openapi_wckey_resp

#### default {#default-52 .field-label}

Description of wckey v0.0.44_openapi_wckey_resp
:::::::::::

------------------------------------------------------------------------

::::::::::::::::::::::::::::: method
[]{#slurmdbV0044GetWckeys}

::: method-path
[]{#slurmdbV0044GetWckeys} Up

``` get
get /slurmdb/v0.0.44/wckeys/
```
:::

::: method-summary
Get wckey list ([slurmdbV0044GetWckeys]{.nickname})
:::

::: method-notes
:::

### Query parameters {#query-parameters-27 .field-label}

::::::::::::::::::::::: field-items
::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV cluster name list default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV ID list default: null
:::

::: param
name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV name list default: null
:::

::: param
only_defaults (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Only query defaults default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
user (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV user list default: null
:::

::: param
with_usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include usage default: null
:::

::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include deleted WCKeys default: null
:::
:::::::::::::::::::::::

### Return type {#return-type-53 .field-label}

::: return-type
v0.0.44_openapi_wckey_resp
:::

### Example data {#example-data-53 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "wckeys" : [ {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  }, {
    "cluster" : "cluster",
    "name" : "name",
    "flags" : [ "DELETED", "DELETED" ],
    "accounting" : [ {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    }, {
      "start" : 7,
      "id" : 5,
      "TRES" : {
        "name" : "name",
        "count" : 0,
        "id" : 7,
        "type" : "type"
      },
      "allocated" : {
        "seconds" : 5
      },
      "id_alt" : 2
    } ],
    "id" : 9,
    "user" : "user"
  } ],
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-53 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-53 .field-label}

#### 200 {#section-53 .field-label}

List of wckeys v0.0.44_openapi_wckey_resp

#### default {#default-53 .field-label}

List of wckeys v0.0.44_openapi_wckey_resp
:::::::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044PostAccounts}

::: method-path
[]{#slurmdbV0044PostAccounts} Up

``` post
post /slurmdb/v0.0.44/accounts/
```
:::

::: method-summary
Add/update list of accounts ([slurmdbV0044PostAccounts]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-9 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-9 .field-label}

::::: field-items
::: param
v0.0.44_openapi_accounts_resp v0.0.44_openapi_accounts_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-54 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-54 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-54 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-54 .field-label}

#### 200 {#section-54 .field-label}

Status of account update request v0.0.44_openapi_resp

#### default {#default-54 .field-label}

Status of account update request v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044PostAccountsAssociation}

::: method-path
[]{#slurmdbV0044PostAccountsAssociation} Up

``` post
post /slurmdb/v0.0.44/accounts_association/
```
:::

::: method-summary
Add accounts with conditional association ([slurmdbV0044PostAccountsAssociation]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-10 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-10 .field-label}

::::: field-items
::: param
v0.0.44_openapi_accounts_add_cond_resp v0.0.44_openapi_accounts_add_cond_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-55 .field-label}

::: return-type
v0.0.44_openapi_accounts_add_cond_resp_str
:::

### Example data {#example-data-55 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ],
  "added_accounts" : "added_accounts"
}
```

### Produces {#produces-55 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-55 .field-label}

#### 200 {#section-55 .field-label}

Status of account addition request v0.0.44_openapi_accounts_add_cond_resp_str

#### default {#default-55 .field-label}

Status of account addition request v0.0.44_openapi_accounts_add_cond_resp_str
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044PostAssociations}

::: method-path
[]{#slurmdbV0044PostAssociations} Up

``` post
post /slurmdb/v0.0.44/associations/
```
:::

::: method-summary
Set associations info ([slurmdbV0044PostAssociations]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-11 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-11 .field-label}

::::: field-items
::: param
v0.0.44_openapi_assocs_resp v0.0.44_openapi_assocs_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-56 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-56 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-56 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-56 .field-label}

#### 200 {#section-56 .field-label}

status of associations update v0.0.44_openapi_resp

#### default {#default-56 .field-label}

status of associations update v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

:::::::::::::: method
[]{#slurmdbV0044PostClusters}

::: method-path
[]{#slurmdbV0044PostClusters} Up

``` post
post /slurmdb/v0.0.44/clusters/
```
:::

::: method-summary
Get cluster list ([slurmdbV0044PostClusters]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-12 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-12 .field-label}

::::: field-items
::: param
v0.0.44_openapi_clusters_resp v0.0.44_openapi_clusters_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Query parameters {#query-parameters-28 .field-label}

::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query reservations updated more recently than this time (UNIX timestamp) default: null
:::
:::::

### Return type {#return-type-57 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-57 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-57 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-57 .field-label}

#### 200 {#section-57 .field-label}

Result of modify clusters request v0.0.44_openapi_resp

#### default {#default-57 .field-label}

Result of modify clusters request v0.0.44_openapi_resp
::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044PostConfig}

::: method-path
[]{#slurmdbV0044PostConfig} Up

``` post
post /slurmdb/v0.0.44/config
```
:::

::: method-summary
Load all configuration information ([slurmdbV0044PostConfig]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-13 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-13 .field-label}

::::: field-items
::: param
v0.0.44_openapi_slurmdbd_config_resp v0.0.44_openapi_slurmdbd_config_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-58 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-58 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-58 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-58 .field-label}

#### 200 {#section-58 .field-label}

slurmdbd configuration v0.0.44_openapi_resp

#### default {#default-58 .field-label}

slurmdbd configuration v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

:::::::::::::: method
[]{#slurmdbV0044PostJob}

::: method-path
[]{#slurmdbV0044PostJob} Up

``` post
post /slurmdb/v0.0.44/job/{job_id}
```
:::

::: method-summary
Update job ([slurmdbV0044PostJob]{.nickname})
:::

::: method-notes
:::

### Path parameters {#path-parameters-21 .field-label}

::::: field-items
::: param
job_id (required)
:::

::: param-desc
[Path Parameter]{.param-type} â€" Job ID default: null
:::
:::::

### Consumes {#consumes-14 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-14 .field-label}

::::: field-items
::: param
v0.0.44_job_modify v0.0.44_job_modify (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-59 .field-label}

::: return-type
v0.0.44_openapi_job_modify_resp
:::

### Example data {#example-data-59 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "results" : [ "results", "results" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-59 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-59 .field-label}

#### 200 {#section-59 .field-label}

Job update results v0.0.44_openapi_job_modify_resp

#### default {#default-59 .field-label}

Job update results v0.0.44_openapi_job_modify_resp
::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044PostJobs}

::: method-path
[]{#slurmdbV0044PostJobs} Up

``` post
post /slurmdb/v0.0.44/jobs/
```
:::

::: method-summary
Update jobs ([slurmdbV0044PostJobs]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-15 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-15 .field-label}

::::: field-items
::: param
v0.0.44_openapi_job_modify_req v0.0.44_openapi_job_modify_req (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-60 .field-label}

::: return-type
v0.0.44_openapi_job_modify_resp
:::

### Example data {#example-data-60 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "results" : [ "results", "results" ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-60 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-60 .field-label}

#### 200 {#section-60 .field-label}

Job update results v0.0.44_openapi_job_modify_resp

#### default {#default-60 .field-label}

Job update results v0.0.44_openapi_job_modify_resp
:::::::::::

------------------------------------------------------------------------

:::::::::::::::::::::::: method
[]{#slurmdbV0044PostQos}

::: method-path
[]{#slurmdbV0044PostQos} Up

``` post
post /slurmdb/v0.0.44/qos/
```
:::

::: method-summary
Add or update QOSs ([slurmdbV0044PostQos]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-16 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-16 .field-label}

::::: field-items
::: param
v0.0.44_openapi_slurmdbd_qos_resp v0.0.44_openapi_slurmdbd_qos_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Query parameters {#query-parameters-29 .field-label}

::::::::::::::: field-items
::: param
description (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV description list default: null
:::

::: param
Include deleted QOS (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS id list default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV QOS name list default: null
:::

::: param
preempt_mode (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" PreemptMode used when jobs in this QOS are preempted default: null
:::
:::::::::::::::

### Return type {#return-type-61 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-61 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-61 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-61 .field-label}

#### 200 {#section-61 .field-label}

QOS update response v0.0.44_openapi_resp

#### default {#default-61 .field-label}

QOS update response v0.0.44_openapi_resp
::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044PostTres}

::: method-path
[]{#slurmdbV0044PostTres} Up

``` post
post /slurmdb/v0.0.44/tres/
```
:::

::: method-summary
Add TRES ([slurmdbV0044PostTres]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-17 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-17 .field-label}

::::: field-items
::: param
v0.0.44_openapi_tres_resp v0.0.44_openapi_tres_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-62 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-62 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-62 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-62 .field-label}

#### 200 {#section-62 .field-label}

TRES update result v0.0.44_openapi_resp

#### default {#default-62 .field-label}

TRES update result v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

::::::::::: method
[]{#slurmdbV0044PostUsers}

::: method-path
[]{#slurmdbV0044PostUsers} Up

``` post
post /slurmdb/v0.0.44/users/
```
:::

::: method-summary
Update users ([slurmdbV0044PostUsers]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-18 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-18 .field-label}

::::: field-items
::: param
v0.0.44_openapi_users_resp v0.0.44_openapi_users_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Return type {#return-type-63 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-63 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-63 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-63 .field-label}

#### 200 {#section-63 .field-label}

Status of user update request v0.0.44_openapi_resp

#### default {#default-63 .field-label}

Status of user update request v0.0.44_openapi_resp
:::::::::::

------------------------------------------------------------------------

:::::::::::::::: method
[]{#slurmdbV0044PostUsersAssociation}

::: method-path
[]{#slurmdbV0044PostUsersAssociation} Up

``` post
post /slurmdb/v0.0.44/users_association/
```
:::

::: method-summary
Add users with conditional association ([slurmdbV0044PostUsersAssociation]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-19 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-19 .field-label}

::::: field-items
::: param
v0.0.44_openapi_users_add_cond_resp v0.0.44_openapi_users_add_cond_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Query parameters {#query-parameters-30 .field-label}

::::::: field-items
::: param
update_time (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query partitions updated more recently than this time (UNIX timestamp) default: null
:::

::: param
flags (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Query flags default: null
:::
:::::::

### Return type {#return-type-64 .field-label}

::: return-type
v0.0.44_openapi_users_add_cond_resp_str
:::

### Example data {#example-data-64 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "added_users" : "added_users",
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-64 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-64 .field-label}

#### 200 {#section-64 .field-label}

Add list of users with conditional association v0.0.44_openapi_users_add_cond_resp_str

#### default {#default-64 .field-label}

Add list of users with conditional association v0.0.44_openapi_users_add_cond_resp_str
::::::::::::::::

------------------------------------------------------------------------

:::::::::::::::::::::::::::::::: method
[]{#slurmdbV0044PostWckeys}

::: method-path
[]{#slurmdbV0044PostWckeys} Up

``` post
post /slurmdb/v0.0.44/wckeys/
```
:::

::: method-summary
Add or update wckeys ([slurmdbV0044PostWckeys]{.nickname})
:::

::: method-notes
:::

### Consumes {#consumes-20 .field-label}

This API call consumes the following media types via the [Content-Type]{.header} request header:

- `application/json`

### Request body {#request-body-20 .field-label}

::::: field-items
::: param
v0.0.44_openapi_wckey_resp v0.0.44_openapi_wckey_resp (optional)
:::

::: param-desc
[Body Parameter]{.param-type} â€"
:::
:::::

### Query parameters {#query-parameters-31 .field-label}

::::::::::::::::::::::: field-items
::: param
cluster (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV cluster name list default: null
:::

::: param
format (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Ignored; process JSON manually to control output format default: null
:::

::: param
id (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV ID list default: null
:::

::: param
name (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV name list default: null
:::

::: param
only_defaults (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Only query defaults default: null
:::

::: param
usage_end (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage end (UNIX timestamp) default: null
:::

::: param
usage_start (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Usage start (UNIX timestamp) default: null
:::

::: param
user (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" CSV user list default: null
:::

::: param
with_usage (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include usage default: null
:::

::: param
with_deleted (optional)
:::

::: param-desc
[Query Parameter]{.param-type} â€" Include deleted WCKeys default: null
:::
:::::::::::::::::::::::

### Return type {#return-type-65 .field-label}

::: return-type
v0.0.44_openapi_resp
:::

### Example data {#example-data-65 .field-label}

::: example-data-content-type
Content-Type: application/json
:::

``` example
{
  "meta" : {
    "slurm" : {
      "cluster" : "cluster",
      "release" : "release",
      "version" : {
        "major" : "major",
        "minor" : "minor",
        "micro" : "micro"
      }
    },
    "plugin" : {
      "accounting_storage" : "accounting_storage",
      "name" : "name",
      "type" : "type",
      "data_parser" : "data_parser"
    },
    "client" : {
      "source" : "source",
      "user" : "user",
      "group" : "group"
    },
    "command" : [ "command", "command" ]
  },
  "warnings" : [ {
    "description" : "description",
    "source" : "source"
  }, {
    "description" : "description",
    "source" : "source"
  } ],
  "errors" : [ {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  }, {
    "description" : "description",
    "source" : "source",
    "error" : "error",
    "error_number" : 7
  } ]
}
```

### Produces {#produces-65 .field-label}

This API call produces the following media types according to the [Accept]{.header} request header; the media type will be conveyed by the [Content-Type]{.header} response header.

- `application/json`

### Responses {#responses-65 .field-label}

#### 200 {#section-65 .field-label}

Result of wckey addition or update request v0.0.44_openapi_resp

#### default {#default-65 .field-label}

Result of wckey addition or update request v0.0.44_openapi_resp
::::::::::::::::::::::::::::::::

------------------------------------------------------------------------

## [Models]{#__Models}

\[ Jump to Methods \]

### Table of Contents

1.  `v0.0.44_account` -
2.  `v0.0.44_account_short` -
3.  `v0.0.44_accounting` -
4.  `v0.0.44_accounts_add_cond` -
5.  `v0.0.44_acct_gather_energy` -
6.  `v0.0.44_assoc` -
7.  `v0.0.44_assoc_rec_set` -
8.  `v0.0.44_assoc_shares_obj_wrap` -
9.  `v0.0.44_assoc_short` -
10. `v0.0.44_bf_exit_fields` -
11. `v0.0.44_cluster_rec` -
12. `v0.0.44_controller_ping` -
13. `v0.0.44_coord` -
14. `v0.0.44_cron_entry` -
15. `v0.0.44_float64_no_val_struct` -
16. `v0.0.44_instance` -
17. `v0.0.44_job` -
18. `v0.0.44_job_alloc_req` -
19. `v0.0.44_job_array_response_msg_entry` -
20. `v0.0.44_job_desc_msg` -
21. `v0.0.44_job_info` -
22. `v0.0.44_job_modify` -
23. `v0.0.44_job_res` -
24. `v0.0.44_job_res_core` -
25. `v0.0.44_job_res_node` -
26. `v0.0.44_job_res_socket` -
27. `v0.0.44_job_submit_req` -
28. `v0.0.44_kill_jobs_msg` -
29. `v0.0.44_kill_jobs_resp_job` -
30. `v0.0.44_license` -
31. `v0.0.44_node` -
32. `v0.0.44_node_gres_layout` -
33. `v0.0.44_node_resource_layout` -
34. `v0.0.44_openapi_accounts_add_cond_resp` -
35. `v0.0.44_openapi_accounts_add_cond_resp_str` -
36. `v0.0.44_openapi_accounts_removed_resp` -
37. `v0.0.44_openapi_accounts_resp` -
38. `v0.0.44_openapi_assocs_removed_resp` -
39. `v0.0.44_openapi_assocs_resp` -
40. `v0.0.44_openapi_clusters_removed_resp` -
41. `v0.0.44_openapi_clusters_resp` -
42. `v0.0.44_openapi_create_node_req` -
43. `v0.0.44_openapi_diag_resp` -
44. `v0.0.44_openapi_error` -
45. `v0.0.44_openapi_instances_resp` -
46. `v0.0.44_openapi_job_alloc_resp` -
47. `v0.0.44_openapi_job_info_resp` -
48. `v0.0.44_openapi_job_modify_req` -
49. `v0.0.44_openapi_job_modify_resp` -
50. `v0.0.44_openapi_job_post_response` -
51. `v0.0.44_openapi_job_submit_response` -
52. `v0.0.44_openapi_kill_job_resp` -
53. `v0.0.44_openapi_kill_jobs_resp` -
54. `v0.0.44_openapi_licenses_resp` -
55. `v0.0.44_openapi_meta` -
56. `v0.0.44_openapi_nodes_resp` -
57. `v0.0.44_openapi_partition_resp` -
58. `v0.0.44_openapi_ping_array_resp` -
59. `v0.0.44_openapi_reservation_mod_resp` -
60. `v0.0.44_openapi_reservation_resp` -
61. `v0.0.44_openapi_resource_layout_resp` -
62. `v0.0.44_openapi_resp` -
63. `v0.0.44_openapi_shares_resp` -
64. `v0.0.44_openapi_slurmdbd_config_resp` -
65. `v0.0.44_openapi_slurmdbd_jobs_resp` -
66. `v0.0.44_openapi_slurmdbd_ping_resp` -
67. `v0.0.44_openapi_slurmdbd_qos_removed_resp` -
68. `v0.0.44_openapi_slurmdbd_qos_resp` -
69. `v0.0.44_openapi_slurmdbd_stats_resp` -
70. `v0.0.44_openapi_tres_resp` -
71. `v0.0.44_openapi_users_add_cond_resp` -
72. `v0.0.44_openapi_users_add_cond_resp_str` -
73. `v0.0.44_openapi_users_resp` -
74. `v0.0.44_openapi_warning` -
75. `v0.0.44_openapi_wckey_removed_resp` -
76. `v0.0.44_openapi_wckey_resp` -
77. `v0.0.44_part_prio` -
78. `v0.0.44_partition_info` -
79. `v0.0.44_process_exit_code_verbose` -
80. `v0.0.44_qos` -
81. `v0.0.44_reservation_core_spec` -
82. `v0.0.44_reservation_desc_msg` -
83. `v0.0.44_reservation_info` -
84. `v0.0.44_reservation_mod_req` -
85. `v0.0.44_rollup_stats` -
86. `v0.0.44_schedule_exit_fields` -
87. `v0.0.44_shares_float128_tres` -
88. `v0.0.44_shares_resp_msg` -
89. `v0.0.44_shares_uint64_tres` -
90. `v0.0.44_slurm_step_id` -
91. `v0.0.44_slurmdbd_ping` -
92. `v0.0.44_stats_msg` -
93. `v0.0.44_stats_msg_rpc_dump` -
94. `v0.0.44_stats_msg_rpc_queue` -
95. `v0.0.44_stats_msg_rpc_type` -
96. `v0.0.44_stats_msg_rpc_user` -
97. `v0.0.44_stats_rec` -
98. `v0.0.44_stats_rpc` -
99. `v0.0.44_stats_user` -
100. `v0.0.44_step` -
101. `v0.0.44_tres` -
102. `v0.0.44_uint16_no_val_struct` -
103. `v0.0.44_uint32_no_val_struct` -
104. `v0.0.44_uint64_no_val_struct` -
105. `v0.0.44_update_node_msg` -
106. `v0.0.44_user` -
107. `v0.0.44_user_short` -
108. `v0.0.44_users_add_cond` -
109. `v0.0.44_wckey` -
110. `v0.0.44_wckey_tag_struct` -
111. `v0_0_44_accounting_allocated` -
112. `v0_0_44_assoc_default` -
113. `v0_0_44_assoc_max` -
114. `v0_0_44_assoc_max_jobs` -
115. `v0_0_44_assoc_max_jobs_per` -
116. `v0_0_44_assoc_max_per` -
117. `v0_0_44_assoc_max_per_account` -
118. `v0_0_44_assoc_max_tres` -
119. `v0_0_44_assoc_max_tres_group` -
120. `v0_0_44_assoc_max_tres_minutes` -
121. `v0_0_44_assoc_max_tres_per` -
122. `v0_0_44_assoc_min` -
123. `v0_0_44_assoc_shares_obj_wrap_fairshare` -
124. `v0_0_44_assoc_shares_obj_wrap_tres` -
125. `v0_0_44_cluster_rec_associations` -
126. `v0_0_44_cluster_rec_controller` -
127. `v0_0_44_cron_entry_line` -
128. `v0_0_44_instance_time` -
129. `v0_0_44_job_array` -
130. `v0_0_44_job_array_limits` -
131. `v0_0_44_job_array_limits_max` -
132. `v0_0_44_job_array_limits_max_running` -
133. `v0_0_44_job_comment` -
134. `v0_0_44_job_desc_msg_rlimits` -
135. `v0_0_44_job_het` -
136. `v0_0_44_job_info_power` -
137. `v0_0_44_job_mcs` -
138. `v0_0_44_job_modify_tres` -
139. `v0_0_44_job_required` -
140. `v0_0_44_job_res_node_cpus` -
141. `v0_0_44_job_res_node_memory` -
142. `v0_0_44_job_res_nodes` -
143. `v0_0_44_job_reservation` -
144. `v0_0_44_job_state` -
145. `v0_0_44_job_time` -
146. `v0_0_44_job_time_system` -
147. `v0_0_44_job_time_total` -
148. `v0_0_44_job_time_user` -
149. `v0_0_44_job_tres` -
150. `v0_0_44_kill_jobs_resp_job_error` -
151. `v0_0_44_kill_jobs_resp_job_federation` -
152. `v0_0_44_openapi_meta_client` -
153. `v0_0_44_openapi_meta_plugin` -
154. `v0_0_44_openapi_meta_slurm` -
155. `v0_0_44_openapi_meta_slurm_version` -
156. `v0_0_44_partition_info_accounts` -
157. `v0_0_44_partition_info_cpus` -
158. `v0_0_44_partition_info_defaults` -
159. `v0_0_44_partition_info_groups` -
160. `v0_0_44_partition_info_maximums` -
161. `v0_0_44_partition_info_maximums_oversubscribe` -
162. `v0_0_44_partition_info_minimums` -
163. `v0_0_44_partition_info_nodes` -
164. `v0_0_44_partition_info_partition` -
165. `v0_0_44_partition_info_priority` -
166. `v0_0_44_partition_info_qos` -
167. `v0_0_44_partition_info_timeouts` -
168. `v0_0_44_partition_info_tres` -
169. `v0_0_44_process_exit_code_verbose_signal` -
170. `v0_0_44_qos_limits` -
171. `v0_0_44_qos_limits_max` -
172. `v0_0_44_qos_limits_max_active_jobs` -
173. `v0_0_44_qos_limits_max_jobs` -
174. `v0_0_44_qos_limits_max_jobs_active_jobs` -
175. `v0_0_44_qos_limits_max_jobs_active_jobs_per` -
176. `v0_0_44_qos_limits_max_tres` -
177. `v0_0_44_qos_limits_max_tres_minutes` -
178. `v0_0_44_qos_limits_max_tres_minutes_per` -
179. `v0_0_44_qos_limits_max_tres_per` -
180. `v0_0_44_qos_limits_max_wall_clock` -
181. `v0_0_44_qos_limits_max_wall_clock_per` -
182. `v0_0_44_qos_limits_min` -
183. `v0_0_44_qos_limits_min_tres` -
184. `v0_0_44_qos_limits_min_tres_per` -
185. `v0_0_44_qos_preempt` -
186. `v0_0_44_reservation_info_purge_completed` -
187. `v0_0_44_rollup_stats_daily` -
188. `v0_0_44_rollup_stats_daily_duration` -
189. `v0_0_44_rollup_stats_hourly` -
190. `v0_0_44_rollup_stats_hourly_duration` -
191. `v0_0_44_rollup_stats_monthly` -
192. `v0_0_44_rollup_stats_monthly_duration` -
193. `v0_0_44_stats_rpc_time` -
194. `v0_0_44_step_CPU` -
195. `v0_0_44_step_CPU_requested_frequency` -
196. `v0_0_44_step_nodes` -
197. `v0_0_44_step_statistics` -
198. `v0_0_44_step_statistics_CPU` -
199. `v0_0_44_step_statistics_energy` -
200. `v0_0_44_step_step` -
201. `v0_0_44_step_task` -
202. `v0_0_44_step_tasks` -
203. `v0_0_44_step_time` -
204. `v0_0_44_step_time_system` -
205. `v0_0_44_step_time_total` -
206. `v0_0_44_step_time_user` -
207. `v0_0_44_step_tres` -
208. `v0_0_44_step_tres_consumed` -
209. `v0_0_44_step_tres_requested` -
210. `v0_0_44_user_default` -

:::::::::::::::::: model
### [`v0.0.44_account` -]{#v0.0.44_account} Up

::: model-description
:::

:::::::::::::::: field-items
::: param
associations (optional)
:::

::: param-desc
[array\[v0.0.44_assoc_short\]]{.param-type}
:::

::: param
coordinators (optional)
:::

::: param-desc
[array\[v0.0.44_coord\]]{.param-type}
:::

::: param
description
:::

::: param-desc
[String]{.param-type} Arbitrary string describing the account
:::

::: param
name
:::

::: param-desc
[String]{.param-type} Account name
:::

::: param
organization
:::

::: param-desc
[String]{.param-type} Organization to which the account belongs
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags associated with this account
:::

::: param-enum-header
Enum:
:::
::::::::::::::::
::::::::::::::::::

::::::::: model
### [`v0.0.44_account_short` -]{#v0.0.44_account_short} Up

::: model-description
:::

::::::: field-items
::: param
description (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string describing the account
:::

::: param
organization (optional)
:::

::: param-desc
[String]{.param-type} Organization to which the account belongs
:::
:::::::
:::::::::

::::::::::::::: model
### [`v0.0.44_accounting` -]{#v0.0.44_accounting} Up

::: model-description
:::

::::::::::::: field-items
::: param
allocated (optional)
:::

::: param-desc
[v0_0_44_accounting_allocated]{.param-type}
:::

::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} Association ID or Workload characterization key ID format: int32
:::

::: param
id_alt (optional)
:::

::: param-desc
[Integer]{.param-type} Alternate ID (not currently used) format: int32
:::

::: param
start (optional)
:::

::: param-desc
[Long]{.param-type} When the record was started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
TRES (optional)
:::

::: param-desc
[v0.0.44_tres]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::: model
### [`v0.0.44_accounts_add_cond` -]{#v0.0.44_accounts_add_cond} Up

::: model-description
:::

::::::::: field-items
::: param
accounts
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
association (optional)
:::

::: param-desc
[v0.0.44_assoc_rec_set]{.param-type}
:::

::: param
clusters (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::
:::::::::
:::::::::::

::::::::::::::::: model
### [`v0.0.44_acct_gather_energy` -]{#v0.0.44_acct_gather_energy} Up

::: model-description
:::

::::::::::::::: field-items
::: param
average_watts (optional)
:::

::: param-desc
[Integer]{.param-type} Average power consumption, in watts format: int32
:::

::: param
base_consumed_energy (optional)
:::

::: param-desc
[Long]{.param-type} The energy consumed between when the node was powered on and the last time it was registered by slurmd, in joules format: int64
:::

::: param
consumed_energy (optional)
:::

::: param-desc
[Long]{.param-type} The energy consumed between the last time the node was registered by the slurmd daemon and the last node energy accounting sample, in joules format: int64
:::

::: param
current_watts (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
previous_consumed_energy (optional)
:::

::: param-desc
[Long]{.param-type} Previous value of consumed_energy format: int64
:::

::: param
last_collected (optional)
:::

::: param-desc
[Long]{.param-type} Time when energy data was last retrieved (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::
:::::::::::::::
:::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_assoc` -]{#v0.0.44_assoc} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::: field-items
::: param
accounting (optional)
:::

::: param-desc
[array\[v0.0.44_accounting\]]{.param-type}
:::

::: param
account (optional)
:::

::: param-desc
[String]{.param-type} Account name
:::

::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment
:::

::: param
default (optional)
:::

::: param-desc
[v0_0_44_assoc_default]{.param-type}
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags on the association
:::

::: param-enum-header
Enum:
:::

::: param
max (optional)
:::

::: param-desc
[v0_0_44_assoc_max]{.param-type}
:::

::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} Unique ID (Association ID) format: int32
:::

::: param
is_default (optional)
:::

::: param-desc
[Boolean]{.param-type} Is default association for user
:::

::: param
lineage (optional)
:::

::: param-desc
[String]{.param-type} Complete path up the hierarchy to the root association
:::

::: param
min (optional)
:::

::: param-desc
[v0_0_44_assoc_min]{.param-type}
:::

::: param
parent_account (optional)
:::

::: param-desc
[String]{.param-type} Name of parent account
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition name
:::

::: param
priority (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
qos (optional)
:::

::: param-desc
[array\[String\]]{.param-type} List of QOS names
:::

::: param
shares_raw (optional)
:::

::: param-desc
[Integer]{.param-type} Allocated shares used for fairshare calculation format: int32
:::

::: param
user
:::

::: param-desc
[String]{.param-type} User name
:::
::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_assoc_rec_set` -]{#v0.0.44_assoc_rec_set} Up

::: model-description
:::

::::::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment
:::

::: param
defaultqos (optional)
:::

::: param-desc
[String]{.param-type} Default QOS
:::

::: param
grpjobs (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
grpjobsaccrue (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
grpsubmitjobs (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
grptres (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
grptresmins (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
grptresrunmins (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
grpwall (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
maxjobs (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
maxjobsaccrue (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
maxsubmitjobs (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
maxtresminsperjob (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
maxtresrunmins (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
maxtresperjob (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
maxtrespernode (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
maxwalldurationperjob (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
minpriothresh (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
parent (optional)
:::

::: param-desc
[String]{.param-type} Name of parent account
:::

::: param
priority (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
qoslevel (optional)
:::

::: param-desc
[array\[String\]]{.param-type} List of QOS names
:::

::: param
fairshare (optional)
:::

::: param-desc
[Integer]{.param-type} Allocated shares used for fairshare calculation format: int32
:::
:::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::: model
### [`v0.0.44_assoc_shares_obj_wrap` -]{#v0.0.44_assoc_shares_obj_wrap} Up

::: model-description
:::

:::::::::::::::::::::::::::::: field-items
::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} Association ID format: int32
:::

::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Share name
:::

::: param
parent (optional)
:::

::: param-desc
[String]{.param-type} Parent name
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition name
:::

::: param
shares_normalized (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::

::: param
shares (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_assoc_shares_obj_wrap_tres]{.param-type}
:::

::: param
effective_usage (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::

::: param
usage_normalized (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::

::: param
usage (optional)
:::

::: param-desc
[Long]{.param-type} Measure of tresbillableunits usage format: int64
:::

::: param
fairshare (optional)
:::

::: param-desc
[v0_0_44_assoc_shares_obj_wrap_fairshare]{.param-type}
:::

::: param
type (optional)
:::

::: param-desc
[array\[String\]]{.param-type} User or account association
:::

::: param-enum-header
Enum:
:::
::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::

::::::::::::::: model
### [`v0.0.44_assoc_short` -]{#v0.0.44_assoc_short} Up

::: model-description
:::

::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[String]{.param-type} Account name
:::

::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition name
:::

::: param
user
:::

::: param-desc
[String]{.param-type} User name
:::

::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} Numeric association ID format: int32
:::
:::::::::::::
:::::::::::::::

::::::::::::::::: model
### [`v0.0.44_bf_exit_fields` -]{#v0.0.44_bf_exit_fields} Up

::: model-description
:::

::::::::::::::: field-items
::: param
end_job_queue (optional)
:::

::: param-desc
[Integer]{.param-type} Reached end of queue format: int32
:::

::: param
bf_max_job_start (optional)
:::

::: param-desc
[Integer]{.param-type} Reached number of jobs allowed to start format: int32
:::

::: param
bf_max_job_test (optional)
:::

::: param-desc
[Integer]{.param-type} Reached number of jobs allowed to be tested format: int32
:::

::: param
bf_max_time (optional)
:::

::: param-desc
[Integer]{.param-type} Reached maximum allowed scheduler time format: int32
:::

::: param
bf_node_space_size (optional)
:::

::: param-desc
[Integer]{.param-type} Reached table size limit format: int32
:::

::: param
state_changed (optional)
:::

::: param-desc
[Integer]{.param-type} System state changed format: int32
:::
:::::::::::::::
:::::::::::::::::

:::::::::::::::::::::: model
### [`v0.0.44_cluster_rec` -]{#v0.0.44_cluster_rec} Up

::: model-description
:::

:::::::::::::::::::: field-items
::: param
controller (optional)
:::

::: param-desc
[v0_0_44_cluster_rec_controller]{.param-type}
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags
:::

::: param-enum-header
Enum:
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} ClusterName
:::

::: param
nodes (optional)
:::

::: param-desc
[String]{.param-type} Node names
:::

::: param
select_plugin (optional)
:::

::: param-desc
[String]{.param-type}
:::

::: param
associations (optional)
:::

::: param-desc
[v0_0_44_cluster_rec_associations]{.param-type}
:::

::: param
rpc_version (optional)
:::

::: param-desc
[Integer]{.param-type} RPC version used in the cluster format: int32
:::

::: param
tres (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
::::::::::::::::::::
::::::::::::::::::::::

::::::::::::::::: model
### [`v0.0.44_controller_ping` -]{#v0.0.44_controller_ping} Up

::: model-description
:::

::::::::::::::: field-items
::: param
hostname (optional)
:::

::: param-desc
[String]{.param-type} Target for ping
:::

::: param
pinged (optional)
:::

::: param-desc
[String]{.param-type} Ping result
:::

::: param
responding
:::

::: param-desc
[Boolean]{.param-type} If ping RPC responded with pong from controller
:::

::: param
latency (optional)
:::

::: param-desc
[Long]{.param-type} Number of microseconds it took to successfully ping or timeout format: int64
:::

::: param
mode (optional)
:::

::: param-desc
[String]{.param-type} The operating mode of the responding slurmctld
:::

::: param
primary
:::

::: param-desc
[Boolean]{.param-type} Is responding slurmctld the primary controller (Is responding slurmctld the primary controller)
:::
:::::::::::::::
:::::::::::::::::

::::::::: model
### [`v0.0.44_coord` -]{#v0.0.44_coord} Up

::: model-description
:::

::::::: field-items
::: param
name
:::

::: param-desc
[String]{.param-type} User name
:::

::: param
direct (optional)
:::

::: param-desc
[Boolean]{.param-type} Indicates whether the coordinator was directly assigned to this account
:::
:::::::
:::::::::

:::::::::::::::::::::::: model
### [`v0.0.44_cron_entry` -]{#v0.0.44_cron_entry} Up

::: model-description
:::

:::::::::::::::::::::: field-items
::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags
:::

::: param-enum-header
Enum:
:::

::: param
minute (optional)
:::

::: param-desc
[String]{.param-type} Ranged string specifying eligible minute values (e.g. 0-10,50)
:::

::: param
hour (optional)
:::

::: param-desc
[String]{.param-type} Ranged string specifying eligible hour values (e.g. 0-5,23)
:::

::: param
day_of_month (optional)
:::

::: param-desc
[String]{.param-type} Ranged string specifying eligible day of month values (e.g. 0-10,29)
:::

::: param
month (optional)
:::

::: param-desc
[String]{.param-type} Ranged string specifying eligible month values (e.g. 0-5,12)
:::

::: param
day_of_week (optional)
:::

::: param-desc
[String]{.param-type} Ranged string specifying eligible day of week values (e.g.0-3,7)
:::

::: param
specification (optional)
:::

::: param-desc
[String]{.param-type} Complete time specification (\* means valid for all allowed values) - minute hour day_of_month month day_of_week
:::

::: param
command (optional)
:::

::: param-desc
[String]{.param-type} Command to run
:::

::: param
line (optional)
:::

::: param-desc
[v0_0_44_cron_entry_line]{.param-type}
:::
::::::::::::::::::::::
::::::::::::::::::::::::

::::::::::: model
### [`v0.0.44_float64_no_val_struct` -]{#v0.0.44_float64_no_val_struct} Up

::: model-description
:::

::::::::: field-items
::: param
set (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set; False if number is unset
:::

::: param
infinite (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set to infinite; \"set\" and \"number\" will be ignored
:::

::: param
number (optional)
:::

::: param-desc
[Double]{.param-type} If \"set\" is True the number will be set with value; otherwise ignore number contents format: double
:::
:::::::::
:::::::::::

::::::::::::::::: model
### [`v0.0.44_instance` -]{#v0.0.44_instance} Up

::: model-description
:::

::::::::::::::: field-items
::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
extra (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string used for node filtering if extra constraints are enabled
:::

::: param
instance_id (optional)
:::

::: param-desc
[String]{.param-type} Cloud instance ID
:::

::: param
instance_type (optional)
:::

::: param-desc
[String]{.param-type} Cloud instance type
:::

::: param
node_name (optional)
:::

::: param-desc
[String]{.param-type} NodeName
:::

::: param
time (optional)
:::

::: param-desc
[v0_0_44_instance_time]{.param-type}
:::
:::::::::::::::
:::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_job` -]{#v0.0.44_job} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[String]{.param-type} Account the job ran under
:::

::: param
comment (optional)
:::

::: param-desc
[v0_0_44_job_comment]{.param-type}
:::

::: param
allocation_nodes (optional)
:::

::: param-desc
[Integer]{.param-type} List of nodes allocated to the job format: int32
:::

::: param
array (optional)
:::

::: param-desc
[v0_0_44_job_array]{.param-type}
:::

::: param
association (optional)
:::

::: param-desc
[v0.0.44_assoc_short]{.param-type}
:::

::: param
block (optional)
:::

::: param-desc
[String]{.param-type} The name of the block to be used (used with Blue Gene systems)
:::

::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
constraints (optional)
:::

::: param-desc
[String]{.param-type} Feature(s) the job requested as a constraint
:::

::: param
container (optional)
:::

::: param-desc
[String]{.param-type} Absolute path to OCI container bundle
:::

::: param
derived_exit_code (optional)
:::

::: param-desc
[v0.0.44_process_exit_code_verbose]{.param-type}
:::

::: param
time (optional)
:::

::: param-desc
[v0_0_44_job_time]{.param-type}
:::

::: param
exit_code (optional)
:::

::: param-desc
[v0.0.44_process_exit_code_verbose]{.param-type}
:::

::: param
extra (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string used for node filtering if extra constraints are enabled
:::

::: param
failed_node (optional)
:::

::: param-desc
[String]{.param-type} Name of node that caused job failure
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags associated with this job
:::

::: param-enum-header
Enum:
:::

::: param
group (optional)
:::

::: param-desc
[String]{.param-type} Group ID of the user that owns the job
:::

::: param
het (optional)
:::

::: param-desc
[v0_0_44_job_het]{.param-type}
:::

::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} Job ID format: int32
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Job name
:::

::: param
licenses (optional)
:::

::: param-desc
[String]{.param-type} License(s) required by the job
:::

::: param
mcs (optional)
:::

::: param-desc
[v0_0_44_job_mcs]{.param-type}
:::

::: param
nodes (optional)
:::

::: param-desc
[String]{.param-type} Node(s) allocated to the job
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition assigned to the job
:::

::: param
hold (optional)
:::

::: param-desc
[Boolean]{.param-type} Hold (true) or release (false) job (Job held)
:::

::: param
priority (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
qos (optional)
:::

::: param-desc
[String]{.param-type} Quality of Service assigned to the job
:::

::: param
qosreq (optional)
:::

::: param-desc
[String]{.param-type} Requested QOS
:::

::: param
required (optional)
:::

::: param-desc
[v0_0_44_job_required]{.param-type}
:::

::: param
kill_request_user (optional)
:::

::: param-desc
[String]{.param-type} User ID that requested termination of the job
:::

::: param
restart_cnt (optional)
:::

::: param-desc
[Integer]{.param-type} How many times this job has been requeued/restarted format: int32
:::

::: param
reservation (optional)
:::

::: param-desc
[v0_0_44_job_reservation]{.param-type}
:::

::: param
script (optional)
:::

::: param-desc
[String]{.param-type} Job batch script contents; only the first component in a HetJob is populated or honored
:::

::: param
segment_size (optional)
:::

::: param-desc
[Integer]{.param-type} Requested segment size format: int32
:::

::: param
stdin_expanded (optional)
:::

::: param-desc
[String]{.param-type} Job stdin with expanded fields
:::

::: param
stdout_expanded (optional)
:::

::: param-desc
[String]{.param-type} Job stdout with expanded fields
:::

::: param
stderr_expanded (optional)
:::

::: param-desc
[String]{.param-type} Job stderr with expanded fields
:::

::: param
stdout (optional)
:::

::: param-desc
[String]{.param-type} Path to stdout file
:::

::: param
stderr (optional)
:::

::: param-desc
[String]{.param-type} Path to stderr file
:::

::: param
stdin (optional)
:::

::: param-desc
[String]{.param-type} Path to stdin file
:::

::: param
state (optional)
:::

::: param-desc
[v0_0_44_job_state]{.param-type}
:::

::: param
steps (optional)
:::

::: param-desc
[array\[v0.0.44_step\]]{.param-type}
:::

::: param
submit_line (optional)
:::

::: param-desc
[String]{.param-type} Command used to submit the job
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_job_tres]{.param-type}
:::

::: param
used_gres (optional)
:::

::: param-desc
[String]{.param-type} Generic resources used by job
:::

::: param
user (optional)
:::

::: param-desc
[String]{.param-type} User that owns the job
:::

::: param
wckey (optional)
:::

::: param-desc
[v0.0.44_wckey_tag_struct]{.param-type}
:::

::: param
working_directory (optional)
:::

::: param-desc
[String]{.param-type} Path to current working directory
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::: model
### [`v0.0.44_job_alloc_req` -]{#v0.0.44_job_alloc_req} Up

::: model-description
:::

::::::: field-items
::: param
hetjob (optional)
:::

::: param-desc
[array\[v0.0.44_job_desc_msg\]]{.param-type}
:::

::: param
job (optional)
:::

::: param-desc
[v0.0.44_job_desc_msg]{.param-type}
:::
:::::::
:::::::::

::::::::::::::: model
### [`v0.0.44_job_array_response_msg_entry` -]{#v0.0.44_job_array_response_msg_entry} Up

::: model-description
:::

::::::::::::: field-items
::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} Job ID for updated job format: int32
:::

::: param
step_id (optional)
:::

::: param-desc
[String]{.param-type} Step ID for updated job
:::

::: param
error (optional)
:::

::: param-desc
[String]{.param-type} Verbose update status or error
:::

::: param
error_code (optional)
:::

::: param-desc
[Integer]{.param-type} Verbose update status or error format: int32
:::

::: param
why (optional)
:::

::: param-desc
[String]{.param-type} Update response message
:::
:::::::::::::
:::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_job_desc_msg` -]{#v0.0.44_job_desc_msg} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[String]{.param-type} Account associated with the job
:::

::: param
account_gather_frequency (optional)
:::

::: param-desc
[String]{.param-type} Job accounting and profiling sampling intervals in seconds
:::

::: param
admin_comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment made by administrator
:::

::: param
allocation_node_list (optional)
:::

::: param-desc
[String]{.param-type} Local node making the resource allocation
:::

::: param
allocation_node_port (optional)
:::

::: param-desc
[Integer]{.param-type} Port to send allocation confirmation to format: int32
:::

::: param
argv (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
array (optional)
:::

::: param-desc
[String]{.param-type} Job array index value specification
:::

::: param
batch_features (optional)
:::

::: param-desc
[String]{.param-type} Features required for batch script\'s node
:::

::: param
begin_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Job flags
:::

::: param-enum-header
Enum:
:::

::: param
burst_buffer (optional)
:::

::: param-desc
[String]{.param-type} Burst buffer specifications
:::

::: param
clusters (optional)
:::

::: param-desc
[String]{.param-type} Clusters that a federated job can run on
:::

::: param
cluster_constraint (optional)
:::

::: param-desc
[String]{.param-type} Required features that a federated cluster must have to have a sibling job submitted to it
:::

::: param
comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment made by user
:::

::: param
contiguous (optional)
:::

::: param-desc
[Boolean]{.param-type} True if job requires contiguous nodes
:::

::: param
container (optional)
:::

::: param-desc
[String]{.param-type} Absolute path to OCI container bundle
:::

::: param
container_id (optional)
:::

::: param-desc
[String]{.param-type} OCI container ID
:::

::: param
core_specification (optional)
:::

::: param-desc
[Integer]{.param-type} Specialized core count format: int32
:::

::: param
thread_specification (optional)
:::

::: param-desc
[Integer]{.param-type} Specialized thread count format: int32
:::

::: param
cpu_binding (optional)
:::

::: param-desc
[String]{.param-type} Method for binding tasks to allocated CPUs
:::

::: param
cpu_binding_flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags for CPU binding
:::

::: param-enum-header
Enum:
:::

::: param
cpu_frequency (optional)
:::

::: param-desc
[String]{.param-type} Requested CPU frequency range \[-p2\]\[:p3\]
:::

::: param
cpus_per_tres (optional)
:::

::: param-desc
[String]{.param-type} Semicolon delimited list of TRES=# values values indicating how many CPUs should be allocated for each specified TRES (currently only used for gres/gpu)
:::

::: param
crontab (optional)
:::

::: param-desc
[v0.0.44_cron_entry]{.param-type}
:::

::: param
deadline (optional)
:::

::: param-desc
[Long]{.param-type} Latest time that the job may start (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
delay_boot (optional)
:::

::: param-desc
[Integer]{.param-type} Number of seconds after job eligible start that nodes will be rebooted to satisfy feature specification format: int32
:::

::: param
dependency (optional)
:::

::: param-desc
[String]{.param-type} Other jobs that must meet certain criteria before this job can start
:::

::: param
end_time (optional)
:::

::: param-desc
[Long]{.param-type} Expected end time (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
environment (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
rlimits (optional)
:::

::: param-desc
[v0_0_44_job_desc_msg_rlimits]{.param-type}
:::

::: param
excluded_nodes (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
extra (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string used for node filtering if extra constraints are enabled
:::

::: param
constraints (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of features that are required
:::

::: param
group_id (optional)
:::

::: param-desc
[String]{.param-type} Group ID of the user that owns the job
:::

::: param
hetjob_group (optional)
:::

::: param-desc
[Integer]{.param-type} Unique sequence number applied to this component of the heterogeneous job format: int32
:::

::: param
immediate (optional)
:::

::: param-desc
[Boolean]{.param-type} If true, exit if resources are not available within the time period specified
:::

::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} Job ID format: int32
:::

::: param
kill_on_node_fail (optional)
:::

::: param-desc
[Boolean]{.param-type} If true, kill job on node failure
:::

::: param
licenses (optional)
:::

::: param-desc
[String]{.param-type} License(s) required by the job
:::

::: param
mail_type (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Mail event type(s)
:::

::: param-enum-header
Enum:
:::

::: param
mail_user (optional)
:::

::: param-desc
[String]{.param-type} User to receive email notifications
:::

::: param
mcs_label (optional)
:::

::: param-desc
[String]{.param-type} Multi-Category Security label on the job
:::

::: param
memory_binding (optional)
:::

::: param-desc
[String]{.param-type} Binding map for map/mask_cpu
:::

::: param
memory_binding_type (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Method for binding tasks to memory
:::

::: param-enum-header
Enum:
:::

::: param
memory_per_tres (optional)
:::

::: param-desc
[String]{.param-type} Semicolon delimited list of TRES=# values indicating how much memory in megabytes should be allocated for each specified TRES (currently only used for gres/gpu)
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Job name
:::

::: param
network (optional)
:::

::: param-desc
[String]{.param-type} Network specs for job step
:::

::: param
nice (optional)
:::

::: param-desc
[Integer]{.param-type} Requested job priority change format: int32
:::

::: param
tasks (optional)
:::

::: param-desc
[Integer]{.param-type} Number of tasks format: int32
:::

::: param
oom_kill_step (optional)
:::

::: param-desc
[Integer]{.param-type} Kill whole step in case of OOM in one of the tasks format: int32
:::

::: param
open_mode (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Open mode used for stdout and stderr files
:::

::: param-enum-header
Enum:
:::

::: param
reserve_ports (optional)
:::

::: param-desc
[Integer]{.param-type} Port to send various notification msg to format: int32
:::

::: param
overcommit (optional)
:::

::: param-desc
[Boolean]{.param-type} Overcommit resources
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition assigned to the job
:::

::: param
distribution_plane_size (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
power_flags (optional)
:::

::: param-desc
[array\[oas_any_type_not_mapped\]]{.param-type}
:::

::: param
prefer (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of features that are preferred but not required
:::

::: param
hold (optional)
:::

::: param-desc
[Boolean]{.param-type} Hold (true) or release (false) job (Job held)
:::

::: param
priority (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
profile (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Profile used by the acct_gather_profile plugin
:::

::: param-enum-header
Enum:
:::

::: param
qos (optional)
:::

::: param-desc
[String]{.param-type} Quality of Service assigned to the job
:::

::: param
reboot (optional)
:::

::: param-desc
[Boolean]{.param-type} Node reboot requested before start
:::

::: param
required_nodes (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
requeue (optional)
:::

::: param-desc
[Boolean]{.param-type} Determines whether the job may be requeued
:::

::: param
reservation (optional)
:::

::: param-desc
[String]{.param-type} Name of reservation to use
:::

::: param
script (optional)
:::

::: param-desc
[String]{.param-type} Job batch script contents; only the first component in a HetJob is populated or honored
:::

::: param
shared (optional)
:::

::: param-desc
[array\[String\]]{.param-type} How the job can share resources with other jobs, if at all
:::

::: param-enum-header
Enum:
:::

::: param
site_factor (optional)
:::

::: param-desc
[Integer]{.param-type} Site-specific priority factor format: int32
:::

::: param
spank_environment (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
step_id (optional)
:::

::: param-desc
[v0.0.44_slurm_step_id]{.param-type}
:::

::: param
distribution (optional)
:::

::: param-desc
[String]{.param-type} Layout
:::

::: param
time_limit (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
time_minimum (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
tres_bind (optional)
:::

::: param-desc
[String]{.param-type} Task to TRES binding directives
:::

::: param
tres_freq (optional)
:::

::: param-desc
[String]{.param-type} TRES frequency directives
:::

::: param
tres_per_job (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated for every job
:::

::: param
tres_per_node (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated for every node
:::

::: param
tres_per_socket (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated for every socket
:::

::: param
tres_per_task (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated for every task
:::

::: param
user_id (optional)
:::

::: param-desc
[String]{.param-type} User ID that owns the job
:::

::: param
wait_all_nodes (optional)
:::

::: param-desc
[Boolean]{.param-type} If true, wait to start until after all nodes have booted
:::

::: param
kill_warning_flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags related to job signals
:::

::: param-enum-header
Enum:
:::

::: param
kill_warning_signal (optional)
:::

::: param-desc
[String]{.param-type} Signal to send when approaching end time (e.g. \"10\" or \"USR1\")
:::

::: param
kill_warning_delay (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
current_working_directory (optional)
:::

::: param-desc
[String]{.param-type} Working directory to use for the job
:::

::: param
cpus_per_task (optional)
:::

::: param-desc
[Integer]{.param-type} Number of CPUs required by each task format: int32
:::

::: param
minimum_cpus (optional)
:::

::: param-desc
[Integer]{.param-type} Minimum number of CPUs required format: int32
:::

::: param
maximum_cpus (optional)
:::

::: param-desc
[Integer]{.param-type} Maximum number of CPUs required format: int32
:::

::: param
nodes (optional)
:::

::: param-desc
[String]{.param-type} Node count range specification (e.g. 1-15:4)
:::

::: param
minimum_nodes (optional)
:::

::: param-desc
[Integer]{.param-type} Minimum node count format: int32
:::

::: param
maximum_nodes (optional)
:::

::: param-desc
[Integer]{.param-type} Maximum node count format: int32
:::

::: param
minimum_boards_per_node (optional)
:::

::: param-desc
[Integer]{.param-type} Boards per node required format: int32
:::

::: param
minimum_sockets_per_board (optional)
:::

::: param-desc
[Integer]{.param-type} Sockets per board required format: int32
:::

::: param
sockets_per_node (optional)
:::

::: param-desc
[Integer]{.param-type} Sockets per node required format: int32
:::

::: param
threads_per_core (optional)
:::

::: param-desc
[Integer]{.param-type} Threads per core required format: int32
:::

::: param
tasks_per_node (optional)
:::

::: param-desc
[Integer]{.param-type} Number of tasks to invoke on each node format: int32
:::

::: param
tasks_per_socket (optional)
:::

::: param-desc
[Integer]{.param-type} Number of tasks to invoke on each socket format: int32
:::

::: param
tasks_per_core (optional)
:::

::: param-desc
[Integer]{.param-type} Number of tasks to invoke on each core format: int32
:::

::: param
tasks_per_board (optional)
:::

::: param-desc
[Integer]{.param-type} Number of tasks to invoke on each board format: int32
:::

::: param
ntasks_per_tres (optional)
:::

::: param-desc
[Integer]{.param-type} Number of tasks that can access each GPU format: int32
:::

::: param
minimum_cpus_per_node (optional)
:::

::: param-desc
[Integer]{.param-type} Minimum number of CPUs per node format: int32
:::

::: param
memory_per_cpu (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
memory_per_node (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
temporary_disk_per_node (optional)
:::

::: param-desc
[Integer]{.param-type} Minimum tmp disk space required per node format: int32
:::

::: param
selinux_context (optional)
:::

::: param-desc
[String]{.param-type} SELinux context
:::

::: param
required_switches (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
segment_size (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
standard_error (optional)
:::

::: param-desc
[String]{.param-type} Path to stderr file
:::

::: param
standard_input (optional)
:::

::: param-desc
[String]{.param-type} Path to stdin file
:::

::: param
standard_output (optional)
:::

::: param-desc
[String]{.param-type} Path to stdout file
:::

::: param
wait_for_switch (optional)
:::

::: param-desc
[Integer]{.param-type} Maximum time to wait for switches in seconds format: int32
:::

::: param
wckey (optional)
:::

::: param-desc
[String]{.param-type} Workload characterization key
:::

::: param
x11 (optional)
:::

::: param-desc
[array\[String\]]{.param-type} X11 forwarding options
:::

::: param-enum-header
Enum:
:::

::: param
x11_magic_cookie (optional)
:::

::: param-desc
[String]{.param-type} Magic cookie for X11 forwarding
:::

::: param
x11_target_host (optional)
:::

::: param-desc
[String]{.param-type} Hostname or UNIX socket if x11_target_port=0
:::

::: param
x11_target_port (optional)
:::

::: param-desc
[Integer]{.param-type} TCP port format: int32
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_job_info` -]{#v0.0.44_job_info} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[String]{.param-type} Account associated with the job
:::

::: param
accrue_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
admin_comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment made by administrator
:::

::: param
allocating_node (optional)
:::

::: param-desc
[String]{.param-type} Local node making the resource allocation
:::

::: param
array_job_id (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
array_task_id (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
array_max_tasks (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
array_task_string (optional)
:::

::: param-desc
[String]{.param-type} String expression of task IDs in this record
:::

::: param
association_id (optional)
:::

::: param-desc
[Integer]{.param-type} Unique identifier for the association format: int32
:::

::: param
batch_features (optional)
:::

::: param-desc
[String]{.param-type} Features required for batch script\'s node
:::

::: param
batch_flag (optional)
:::

::: param-desc
[Boolean]{.param-type} True if batch job
:::

::: param
batch_host (optional)
:::

::: param-desc
[String]{.param-type} Name of host running batch script
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Job flags
:::

::: param-enum-header
Enum:
:::

::: param
burst_buffer (optional)
:::

::: param-desc
[String]{.param-type} Burst buffer specifications
:::

::: param
burst_buffer_state (optional)
:::

::: param-desc
[String]{.param-type} Burst buffer state details
:::

::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
cluster_features (optional)
:::

::: param-desc
[String]{.param-type} List of required cluster features
:::

::: param
command (optional)
:::

::: param-desc
[String]{.param-type} Executed command
:::

::: param
comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment
:::

::: param
container (optional)
:::

::: param-desc
[String]{.param-type} Absolute path to OCI container bundle
:::

::: param
container_id (optional)
:::

::: param-desc
[String]{.param-type} OCI container ID
:::

::: param
contiguous (optional)
:::

::: param-desc
[Boolean]{.param-type} True if job requires contiguous nodes
:::

::: param
core_spec (optional)
:::

::: param-desc
[Integer]{.param-type} Specialized core count format: int32
:::

::: param
thread_spec (optional)
:::

::: param-desc
[Integer]{.param-type} Specialized thread count format: int32
:::

::: param
cores_per_socket (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
billable_tres (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::

::: param
cpus_per_task (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
cpu_frequency_minimum (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
cpu_frequency_maximum (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
cpu_frequency_governor (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
cpus_per_tres (optional)
:::

::: param-desc
[String]{.param-type} Semicolon delimited list of TRES=# values indicating how many CPUs should be allocated for each specified TRES (currently only used for gres/gpu)
:::

::: param
cron (optional)
:::

::: param-desc
[String]{.param-type} Time specification for scrontab job
:::

::: param
deadline (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
delay_boot (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
dependency (optional)
:::

::: param-desc
[String]{.param-type} Other jobs that must meet certain criteria before this job can start
:::

::: param
derived_exit_code (optional)
:::

::: param-desc
[v0.0.44_process_exit_code_verbose]{.param-type}
:::

::: param
eligible_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
end_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
excluded_nodes (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of nodes that may not be used
:::

::: param
exit_code (optional)
:::

::: param-desc
[v0.0.44_process_exit_code_verbose]{.param-type}
:::

::: param
extra (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string used for node filtering if extra constraints are enabled
:::

::: param
failed_node (optional)
:::

::: param-desc
[String]{.param-type} Name of node that caused job failure
:::

::: param
features (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of features that are required
:::

::: param
federation_origin (optional)
:::

::: param-desc
[String]{.param-type} Origin cluster\'s name (when using federation)
:::

::: param
federation_siblings_active (optional)
:::

::: param-desc
[String]{.param-type} Active sibling job names
:::

::: param
federation_siblings_viable (optional)
:::

::: param-desc
[String]{.param-type} Viable sibling job names
:::

::: param
gres_detail (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
group_id (optional)
:::

::: param-desc
[Integer]{.param-type} Group ID of the user that owns the job format: int32
:::

::: param
group_name (optional)
:::

::: param-desc
[String]{.param-type} Group name of the user that owns the job
:::

::: param
het_job_id (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
het_job_id_set (optional)
:::

::: param-desc
[String]{.param-type} Job ID range for all heterogeneous job components
:::

::: param
het_job_offset (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} Job ID format: int32
:::

::: param
job_resources (optional)
:::

::: param-desc
[v0.0.44_job_res]{.param-type}
:::

::: param
job_size_str (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
job_state (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Current state
:::

::: param-enum-header
Enum:
:::

::: param
last_sched_evaluation (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
licenses (optional)
:::

::: param-desc
[String]{.param-type} License(s) required by the job
:::

::: param
licenses_allocated (optional)
:::

::: param-desc
[String]{.param-type} License(s) allocated to the job
:::

::: param
mail_type (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Mail event type(s)
:::

::: param-enum-header
Enum:
:::

::: param
mail_user (optional)
:::

::: param-desc
[String]{.param-type} User to receive email notifications
:::

::: param
max_cpus (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
max_nodes (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
mcs_label (optional)
:::

::: param-desc
[String]{.param-type} Multi-Category Security label on the job
:::

::: param
memory_per_tres (optional)
:::

::: param-desc
[String]{.param-type} Semicolon delimited list of TRES=# values indicating how much memory in megabytes should be allocated for each specified TRES (currently only used for gres/gpu)
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Job name
:::

::: param
network (optional)
:::

::: param-desc
[String]{.param-type} Network specs for the job
:::

::: param
nodes (optional)
:::

::: param-desc
[String]{.param-type} Node(s) allocated to the job
:::

::: param
nice (optional)
:::

::: param-desc
[Integer]{.param-type} Requested job priority change format: int32
:::

::: param
tasks_per_core (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
tasks_per_tres (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
tasks_per_node (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
tasks_per_socket (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
tasks_per_board (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
cpus (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
node_count (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
tasks (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition assigned to the job
:::

::: param
prefer (optional)
:::

::: param-desc
[String]{.param-type} Feature(s) the job requested but that are not required
:::

::: param
memory_per_cpu (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
memory_per_node (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
minimum_cpus_per_node (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
minimum_tmp_disk_per_node (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
power (optional)
:::

::: param-desc
[v0_0_44_job_info_power]{.param-type}
:::

::: param
preempt_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
preemptable_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
pre_sus_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
hold (optional)
:::

::: param-desc
[Boolean]{.param-type} Hold (true) or release (false) job (Job held)
:::

::: param
priority (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
priority_by_partition (optional)
:::

::: param-desc
[array\[v0.0.44_part_prio\]]{.param-type}
:::

::: param
profile (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Profile used by the acct_gather_profile plugin
:::

::: param-enum-header
Enum:
:::

::: param
qos (optional)
:::

::: param-desc
[String]{.param-type} Quality of Service assigned to the job, if pending the QOS requested
:::

::: param
reboot (optional)
:::

::: param-desc
[Boolean]{.param-type} Node reboot requested before start
:::

::: param
required_nodes (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of required nodes
:::

::: param
required_switches (optional)
:::

::: param-desc
[Integer]{.param-type} Maximum number of switches format: int32
:::

::: param
requeue (optional)
:::

::: param-desc
[Boolean]{.param-type} Determines whether the job may be requeued
:::

::: param
resize_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
restart_cnt (optional)
:::

::: param-desc
[Integer]{.param-type} Number of job restarts format: int32
:::

::: param
resv_name (optional)
:::

::: param-desc
[String]{.param-type} Name of reservation to use
:::

::: param
scheduled_nodes (optional)
:::

::: param-desc
[String]{.param-type} List of nodes scheduled to be used for the job
:::

::: param
segment_size (optional)
:::

::: param-desc
[Integer]{.param-type} Requested segment size format: int32
:::

::: param
selinux_context (optional)
:::

::: param-desc
[String]{.param-type} SELinux context
:::

::: param
shared (optional)
:::

::: param-desc
[array\[String\]]{.param-type} How the job can share resources with other jobs, if at all
:::

::: param-enum-header
Enum:
:::

::: param
step_id (optional)
:::

::: param-desc
[v0.0.44_slurm_step_id]{.param-type}
:::

::: param
sockets_per_board (optional)
:::

::: param-desc
[Integer]{.param-type} Number of sockets per board required format: int32
:::

::: param
sockets_per_node (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
start_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
state_description (optional)
:::

::: param-desc
[String]{.param-type} Optional details for state_reason
:::

::: param
state_reason (optional)
:::

::: param-desc
[String]{.param-type} Reason for current Pending or Failed state
:::

::: param
standard_input (optional)
:::

::: param-desc
[String]{.param-type} Path to stdin file
:::

::: param
standard_output (optional)
:::

::: param-desc
[String]{.param-type} Path to stdout file
:::

::: param
standard_error (optional)
:::

::: param-desc
[String]{.param-type} Path to stderr file
:::

::: param
stdin_expanded (optional)
:::

::: param-desc
[String]{.param-type} Job stdin with expanded fields
:::

::: param
stdout_expanded (optional)
:::

::: param-desc
[String]{.param-type} Job stdout with expanded fields
:::

::: param
stderr_expanded (optional)
:::

::: param-desc
[String]{.param-type} Job stderr with expanded fields
:::

::: param
submit_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
submit_line (optional)
:::

::: param-desc
[String]{.param-type} Job submit line (e.g. \'sbatch -N3 job.sh job_arg\'
:::

::: param
suspend_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
system_comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment from slurmctld
:::

::: param
time_limit (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
time_minimum (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
threads_per_core (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
tres_bind (optional)
:::

::: param-desc
[String]{.param-type} Task to TRES binding directives
:::

::: param
tres_freq (optional)
:::

::: param-desc
[String]{.param-type} TRES frequency directives
:::

::: param
tres_per_job (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated per job
:::

::: param
tres_per_node (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated per node
:::

::: param
tres_per_socket (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated per socket
:::

::: param
tres_per_task (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of TRES=# values to be allocated per task
:::

::: param
tres_req_str (optional)
:::

::: param-desc
[String]{.param-type} TRES requested by the job
:::

::: param
tres_alloc_str (optional)
:::

::: param-desc
[String]{.param-type} TRES used by the job
:::

::: param
user_id (optional)
:::

::: param-desc
[Integer]{.param-type} User ID that owns the job format: int32
:::

::: param
user_name (optional)
:::

::: param-desc
[String]{.param-type} User name that owns the job
:::

::: param
maximum_switch_wait_time (optional)
:::

::: param-desc
[Integer]{.param-type} Maximum time to wait for switches in seconds format: int32
:::

::: param
wckey (optional)
:::

::: param-desc
[String]{.param-type} Workload characterization key
:::

::: param
current_working_directory (optional)
:::

::: param-desc
[String]{.param-type} Working directory to use for the job
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::: model
### [`v0.0.44_job_modify` -]{#v0.0.44_job_modify} Up

::: model-description
:::

::::::::::::: field-items
::: param
comment (optional)
:::

::: param-desc
[v0_0_44_job_comment]{.param-type}
:::

::: param
derived_exit_code (optional)
:::

::: param-desc
[v0.0.44_process_exit_code_verbose]{.param-type}
:::

::: param
extra (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string used for node filtering if extra constraints are enabled
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_job_modify_tres]{.param-type}
:::

::: param
wckey (optional)
:::

::: param-desc
[String]{.param-type} Workload characterization key
:::
:::::::::::::
:::::::::::::::

:::::::::::::: model
### [`v0.0.44_job_res` -]{#v0.0.44_job_res} Up

::: model-description
:::

:::::::::::: field-items
::: param
select_type
:::

::: param-desc
[array\[String\]]{.param-type} Scheduler consumable resource selection type
:::

::: param-enum-header
Enum:
:::

::: param
nodes (optional)
:::

::: param-desc
[v0_0_44_job_res_nodes]{.param-type}
:::

::: param
cpus
:::

::: param-desc
[Integer]{.param-type} Number of allocated CPUs format: int32
:::

::: param
threads_per_core
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::
::::::::::::
::::::::::::::

:::::::::: model
### [`v0.0.44_job_res_core` -]{#v0.0.44_job_res_core} Up

::: model-description
:::

:::::::: field-items
::: param
index
:::

::: param-desc
[Integer]{.param-type} Core index format: int32
:::

::: param
status
:::

::: param-desc
[array\[String\]]{.param-type} Core status
:::

::: param-enum-header
Enum:
:::
::::::::
::::::::::

::::::::::::::: model
### [`v0.0.44_job_res_node` -]{#v0.0.44_job_res_node} Up

::: model-description
:::

::::::::::::: field-items
::: param
index
:::

::: param-desc
[Integer]{.param-type} Node index format: int32
:::

::: param
name
:::

::: param-desc
[String]{.param-type} Node name
:::

::: param
cpus (optional)
:::

::: param-desc
[v0_0_44_job_res_node_cpus]{.param-type}
:::

::: param
memory (optional)
:::

::: param-desc
[v0_0_44_job_res_node_memory]{.param-type}
:::

::: param
sockets
:::

::: param-desc
[array\[v0.0.44_job_res_socket\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::: model
### [`v0.0.44_job_res_socket` -]{#v0.0.44_job_res_socket} Up

::: model-description
:::

::::::: field-items
::: param
index
:::

::: param-desc
[Integer]{.param-type} Core index format: int32
:::

::: param
cores
:::

::: param-desc
[array\[v0.0.44_job_res_core\]]{.param-type}
:::
:::::::
:::::::::

::::::::::: model
### [`v0.0.44_job_submit_req` -]{#v0.0.44_job_submit_req} Up

::: model-description
:::

::::::::: field-items
::: param
script (optional)
:::

::: param-desc
[String]{.param-type} Job batch script contents; Same as the script field in jobs\[0\] or job.
:::

::: param
jobs (optional)
:::

::: param-desc
[array\[v0.0.44_job_desc_msg\]]{.param-type}
:::

::: param
job (optional)
:::

::: param-desc
[v0.0.44_job_desc_msg]{.param-type}
:::
:::::::::
:::::::::::

::::::::::::::::::::::::::::::::: model
### [`v0.0.44_kill_jobs_msg` -]{#v0.0.44_kill_jobs_msg} Up

::: model-description
:::

::::::::::::::::::::::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific account
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Filter jobs according to flags
:::

::: param-enum-header
Enum:
:::

::: param
job_name (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific name
:::

::: param
jobs (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific partition
:::

::: param
qos (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific QOS
:::

::: param
reservation (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific reservation
:::

::: param
signal (optional)
:::

::: param-desc
[String]{.param-type} Signal to send to jobs
:::

::: param
job_state (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Filter jobs to a specific state
:::

::: param-enum-header
Enum:
:::

::: param
user_id (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific numeric user id
:::

::: param
user_name (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific user name
:::

::: param
wckey (optional)
:::

::: param-desc
[String]{.param-type} Filter jobs to a specific wckey
:::

::: param
nodes (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::
:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::

::::::::::::: model
### [`v0.0.44_kill_jobs_resp_job` -]{#v0.0.44_kill_jobs_resp_job} Up

::: model-description
:::

::::::::::: field-items
::: param
error (optional)
:::

::: param-desc
[v0_0_44_kill_jobs_resp_job_error]{.param-type}
:::

::: param
step_id
:::

::: param-desc
[String]{.param-type} Job or Step ID that signaling failed
:::

::: param
job_id
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
federation (optional)
:::

::: param-desc
[v0_0_44_kill_jobs_resp_job_federation]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::::::::::::: model
### [`v0.0.44_license` -]{#v0.0.44_license} Up

::: model-description
:::

::::::::::::::::::::::: field-items
::: param
LicenseName (optional)
:::

::: param-desc
[String]{.param-type} Name of the license
:::

::: param
Total (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of licenses present format: int32
:::

::: param
Used (optional)
:::

::: param-desc
[Integer]{.param-type} Number of licenses in use format: int32
:::

::: param
Free (optional)
:::

::: param-desc
[Integer]{.param-type} Number of licenses currently available format: int32
:::

::: param
Remote (optional)
:::

::: param-desc
[Boolean]{.param-type} Indicates whether licenses are served by the database
:::

::: param
Reserved (optional)
:::

::: param-desc
[Integer]{.param-type} Number of licenses reserved format: int32
:::

::: param
LastConsumed (optional)
:::

::: param-desc
[Integer]{.param-type} Last known number of licenses that were consumed in the license manager (Remote Only) format: int32
:::

::: param
LastDeficit (optional)
:::

::: param-desc
[Integer]{.param-type} Number of \"missing licenses\" from the cluster\'s perspective format: int32
:::

::: param
LastUpdate (optional)
:::

::: param-desc
[Long]{.param-type} When the license information was last updated (UNIX Timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
Nodes (optional)
:::

::: param-desc
[String]{.param-type} HRes nodes
:::
:::::::::::::::::::::::
:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_node` -]{#v0.0.44_node} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
architecture (optional)
:::

::: param-desc
[String]{.param-type} Computer architecture
:::

::: param
burstbuffer_network_address (optional)
:::

::: param-desc
[String]{.param-type} Alternate network path to be used for sbcast network traffic
:::

::: param
boards (optional)
:::

::: param-desc
[Integer]{.param-type} Number of Baseboards in nodes with a baseboard controller format: int32
:::

::: param
boot_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
tls_cert_last_renewal (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
cert_flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Certmgr status flags
:::

::: param-enum-header
Enum:
:::

::: param
cluster_name (optional)
:::

::: param-desc
[String]{.param-type} Cluster name (only set in federated environments)
:::

::: param
cores (optional)
:::

::: param-desc
[Integer]{.param-type} Number of cores in a single physical processor socket format: int32
:::

::: param
specialized_cores (optional)
:::

::: param-desc
[Integer]{.param-type} Number of cores reserved for system use format: int32
:::

::: param
cpu_binding (optional)
:::

::: param-desc
[Integer]{.param-type} Default method for binding tasks to allocated CPUs format: int32
:::

::: param
cpu_load (optional)
:::

::: param-desc
[Integer]{.param-type} CPU load as reported by the OS format: int32
:::

::: param
free_mem (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
cpus (optional)
:::

::: param-desc
[Integer]{.param-type} Total CPUs, including cores and threads format: int32
:::

::: param
effective_cpus (optional)
:::

::: param-desc
[Integer]{.param-type} Number of effective CPUs (excluding specialized CPUs) format: int32
:::

::: param
specialized_cpus (optional)
:::

::: param-desc
[String]{.param-type} Abstract CPU IDs on this node reserved for exclusive use by slurmd and slurmstepd
:::

::: param
energy (optional)
:::

::: param-desc
[v0.0.44_acct_gather_energy]{.param-type}
:::

::: param
external_sensors (optional)
:::

::: param-desc
[Object]{.param-type}
:::

::: param
extra (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string used for node filtering if extra constraints are enabled
:::

::: param
power (optional)
:::

::: param-desc
[Object]{.param-type}
:::

::: param
features (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
active_features (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
gpu_spec (optional)
:::

::: param-desc
[String]{.param-type} CPU cores reserved for jobs that also use a GPU
:::

::: param
gres (optional)
:::

::: param-desc
[String]{.param-type} Generic resources
:::

::: param
gres_drained (optional)
:::

::: param-desc
[String]{.param-type} Drained generic resources
:::

::: param
gres_used (optional)
:::

::: param-desc
[String]{.param-type} Generic resources currently in use
:::

::: param
instance_id (optional)
:::

::: param-desc
[String]{.param-type} Cloud instance ID
:::

::: param
instance_type (optional)
:::

::: param-desc
[String]{.param-type} Cloud instance type
:::

::: param
last_busy (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
mcs_label (optional)
:::

::: param-desc
[String]{.param-type} Multi-Category Security label
:::

::: param
specialized_memory (optional)
:::

::: param-desc
[Long]{.param-type} Combined memory limit, in MB, for Slurm compute node daemons format: int64
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} NodeName
:::

::: param
next_state_after_reboot (optional)
:::

::: param-desc
[array\[String\]]{.param-type} The state the node will be assigned after rebooting
:::

::: param-enum-header
Enum:
:::

::: param
address (optional)
:::

::: param-desc
[String]{.param-type} NodeAddr, used to establish a communication path
:::

::: param
hostname (optional)
:::

::: param-desc
[String]{.param-type} NodeHostname
:::

::: param
state (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Node state(s) applicable to this node
:::

::: param-enum-header
Enum:
:::

::: param
operating_system (optional)
:::

::: param-desc
[String]{.param-type} Operating system reported by the node
:::

::: param
owner (optional)
:::

::: param-desc
[String]{.param-type} User allowed to run jobs on this node (unset if no restriction)
:::

::: param
partitions (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
port (optional)
:::

::: param-desc
[Integer]{.param-type} TCP port number of the slurmd format: int32
:::

::: param
real_memory (optional)
:::

::: param-desc
[Long]{.param-type} Total memory in MB on the node format: int64
:::

::: param
res_cores_per_gpu (optional)
:::

::: param-desc
[Integer]{.param-type} Number of CPU cores per GPU restricted to GPU jobs format: int32
:::

::: param
comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment
:::

::: param
reason (optional)
:::

::: param-desc
[String]{.param-type} Describes why the node is in a \"DOWN\", \"DRAINED\", \"DRAINING\", \"FAILING\" or \"FAIL\" state
:::

::: param
reason_changed_at (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
reason_set_by_user (optional)
:::

::: param-desc
[String]{.param-type} User who set the reason
:::

::: param
resume_after (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
reservation (optional)
:::

::: param-desc
[String]{.param-type} Name of reservation containing this node
:::

::: param
alloc_memory (optional)
:::

::: param-desc
[Long]{.param-type} Total memory in MB currently allocated for jobs format: int64
:::

::: param
alloc_cpus (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of CPUs currently allocated for jobs format: int32
:::

::: param
alloc_idle_cpus (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of idle CPUs format: int32
:::

::: param
tres_used (optional)
:::

::: param-desc
[String]{.param-type} Trackable resources currently allocated for jobs
:::

::: param
tres_weighted (optional)
:::

::: param-desc
[Double]{.param-type} Ignored. Was weighted number of billable trackable resources allocated format: double
:::

::: param
slurmd_start_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
sockets (optional)
:::

::: param-desc
[Integer]{.param-type} Number of physical processor sockets/chips on the node format: int32
:::

::: param
threads (optional)
:::

::: param-desc
[Integer]{.param-type} Number of logical threads in a single physical core format: int32
:::

::: param
temporary_disk (optional)
:::

::: param-desc
[Integer]{.param-type} Total size in MB of temporary disk storage in TmpFS format: int32
:::

::: param
weight (optional)
:::

::: param-desc
[Integer]{.param-type} Weight of the node for scheduling purposes format: int32
:::

::: param
topology (optional)
:::

::: param-desc
[String]{.param-type} Topology
:::

::: param
tres (optional)
:::

::: param-desc
[String]{.param-type} Configured trackable resources
:::

::: param
version (optional)
:::

::: param-desc
[String]{.param-type} Slurmd version
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::: model
### [`v0.0.44_node_gres_layout` -]{#v0.0.44_node_gres_layout} Up

::: model-description
:::

::::::::::: field-items
::: param
name
:::

::: param-desc
[String]{.param-type} GRES name
:::

::: param
type (optional)
:::

::: param-desc
[String]{.param-type} GRES type (optional)
:::

::: param
count (optional)
:::

::: param-desc
[Long]{.param-type} Count format: int64
:::

::: param
index (optional)
:::

::: param-desc
[String]{.param-type} Index
:::
:::::::::::
:::::::::::::

::::::::::::::::::: model
### [`v0.0.44_node_resource_layout` -]{#v0.0.44_node_resource_layout} Up

::: model-description
:::

::::::::::::::::: field-items
::: param
node
:::

::: param-desc
[String]{.param-type} Node name
:::

::: param
sockets_per_node (optional)
:::

::: param-desc
[Integer]{.param-type} Sockets per node format: int32
:::

::: param
cores_per_socket (optional)
:::

::: param-desc
[Integer]{.param-type} Cores per socket format: int32
:::

::: param
mem_alloc (optional)
:::

::: param-desc
[Long]{.param-type} Allocated memory format: int64
:::

::: param
core_bitmap (optional)
:::

::: param-desc
[String]{.param-type} Abstract core bitmap
:::

::: param
channel (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
gres (optional)
:::

::: param-desc
[array\[v0.0.44_node_gres_layout\]]{.param-type}
:::
:::::::::::::::::
:::::::::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_accounts_add_cond_resp` -]{#v0.0.44_openapi_accounts_add_cond_resp} Up

::: model-description
:::

::::::::::::: field-items
::: param
association_condition
:::

::: param-desc
[v0.0.44_accounts_add_cond]{.param-type}
:::

::: param
account (optional)
:::

::: param-desc
[v0.0.44_account_short]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_accounts_add_cond_resp_str` -]{#v0.0.44_openapi_accounts_add_cond_resp_str} Up

::: model-description
:::

::::::::::: field-items
::: param
added_accounts
:::

::: param-desc
[String]{.param-type} added_accounts
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_accounts_removed_resp` -]{#v0.0.44_openapi_accounts_removed_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
removed_accounts
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_accounts_resp` -]{#v0.0.44_openapi_accounts_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
accounts
:::

::: param-desc
[array\[v0.0.44_account\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_assocs_removed_resp` -]{#v0.0.44_openapi_assocs_removed_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
removed_associations
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_assocs_resp` -]{#v0.0.44_openapi_assocs_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
associations
:::

::: param-desc
[array\[v0.0.44_assoc\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_clusters_removed_resp` -]{#v0.0.44_openapi_clusters_removed_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
deleted_clusters
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_clusters_resp` -]{#v0.0.44_openapi_clusters_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
clusters
:::

::: param-desc
[array\[v0.0.44_cluster_rec\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_create_node_req` -]{#v0.0.44_openapi_create_node_req} Up

::: model-description
:::

::::::::::: field-items
::: param
node_conf
:::

::: param-desc
[String]{.param-type} Node configuration line
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_diag_resp` -]{#v0.0.44_openapi_diag_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
statistics
:::

::: param-desc
[v0.0.44_stats_msg]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_error` -]{#v0.0.44_openapi_error} Up

::: model-description
:::

::::::::::: field-items
::: param
description (optional)
:::

::: param-desc
[String]{.param-type} Long form error description
:::

::: param
error_number (optional)
:::

::: param-desc
[Integer]{.param-type} Slurm numeric error identifier format: int32
:::

::: param
error (optional)
:::

::: param-desc
[String]{.param-type} Short form error description
:::

::: param
source (optional)
:::

::: param-desc
[String]{.param-type} Source of error or where error was first detected
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_instances_resp` -]{#v0.0.44_openapi_instances_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
instances
:::

::: param-desc
[array\[v0.0.44_instance\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_job_alloc_resp` -]{#v0.0.44_openapi_job_alloc_resp} Up

::: model-description
:::

::::::::::::: field-items
::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} Submitted Job ID format: int32
:::

::: param
job_submit_user_msg (optional)
:::

::: param-desc
[String]{.param-type} Job submission user message
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::::::: model
### [`v0.0.44_openapi_job_info_resp` -]{#v0.0.44_openapi_job_info_resp} Up

::: model-description
:::

::::::::::::::: field-items
::: param
jobs
:::

::: param-desc
[array\[v0.0.44_job_info\]]{.param-type}
:::

::: param
last_backfill
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
last_update
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::::
:::::::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_job_modify_req` -]{#v0.0.44_openapi_job_modify_req} Up

::: model-description
:::

::::::::::::: field-items
::: param
job_id_list (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
job_rec (optional)
:::

::: param-desc
[v0.0.44_job_modify]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_job_modify_resp` -]{#v0.0.44_openapi_job_modify_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
results
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_job_post_response` -]{#v0.0.44_openapi_job_post_response} Up

::: model-description
:::

::::::::::: field-items
::: param
results (optional)
:::

::: param-desc
[array\[v0.0.44_job_array_response_msg_entry\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::::: model
### [`v0.0.44_openapi_job_submit_response` -]{#v0.0.44_openapi_job_submit_response} Up

::: model-description
:::

::::::::::::::: field-items
::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} submitted Job ID format: int32
:::

::: param
step_id (optional)
:::

::: param-desc
[String]{.param-type} submitted Step ID
:::

::: param
job_submit_user_msg (optional)
:::

::: param-desc
[String]{.param-type} Job submission user message
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::::
:::::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_kill_job_resp` -]{#v0.0.44_openapi_kill_job_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
status
:::

::: param-desc
[array\[v0.0.44_kill_jobs_resp_job\]]{.param-type} List of jobs signal responses
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_kill_jobs_resp` -]{#v0.0.44_openapi_kill_jobs_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
status
:::

::: param-desc
[array\[v0.0.44_kill_jobs_resp_job\]]{.param-type} List of jobs signal responses
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_licenses_resp` -]{#v0.0.44_openapi_licenses_resp} Up

::: model-description
:::

::::::::::::: field-items
::: param
licenses
:::

::: param-desc
[array\[v0.0.44_license\]]{.param-type}
:::

::: param
last_update
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_meta` -]{#v0.0.44_openapi_meta} Up

::: model-description
:::

::::::::::: field-items
::: param
plugin (optional)
:::

::: param-desc
[v0_0_44_openapi_meta_plugin]{.param-type}
:::

::: param
client (optional)
:::

::: param-desc
[v0_0_44_openapi_meta_client]{.param-type}
:::

::: param
command (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
slurm (optional)
:::

::: param-desc
[v0_0_44_openapi_meta_slurm]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_nodes_resp` -]{#v0.0.44_openapi_nodes_resp} Up

::: model-description
:::

::::::::::::: field-items
::: param
nodes
:::

::: param-desc
[array\[v0.0.44_node\]]{.param-type}
:::

::: param
last_update
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_partition_resp` -]{#v0.0.44_openapi_partition_resp} Up

::: model-description
:::

::::::::::::: field-items
::: param
partitions
:::

::: param-desc
[array\[v0.0.44_partition_info\]]{.param-type}
:::

::: param
last_update
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_ping_array_resp` -]{#v0.0.44_openapi_ping_array_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
pings
:::

::: param-desc
[array\[v0.0.44_controller_ping\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_reservation_mod_resp` -]{#v0.0.44_openapi_reservation_mod_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
reservations
:::

::: param-desc
[array\[v0.0.44_reservation_desc_msg\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_reservation_resp` -]{#v0.0.44_openapi_reservation_resp} Up

::: model-description
:::

::::::::::::: field-items
::: param
reservations
:::

::: param-desc
[array\[v0.0.44_reservation_info\]]{.param-type}
:::

::: param
last_update
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_resource_layout_resp` -]{#v0.0.44_openapi_resource_layout_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
nodes
:::

::: param-desc
[array\[v0.0.44_node_resource_layout\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::: model
### [`v0.0.44_openapi_resp` -]{#v0.0.44_openapi_resp} Up

::: model-description
:::

::::::::: field-items
::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::
:::::::::::

::::::::::::: model
### [`v0.0.44_openapi_shares_resp` -]{#v0.0.44_openapi_shares_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
shares
:::

::: param-desc
[v0.0.44_shares_resp_msg]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::::::::::::::: model
### [`v0.0.44_openapi_slurmdbd_config_resp` -]{#v0.0.44_openapi_slurmdbd_config_resp} Up

::: model-description
:::

::::::::::::::::::::::::: field-items
::: param
clusters (optional)
:::

::: param-desc
[array\[v0.0.44_cluster_rec\]]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
accounts (optional)
:::

::: param-desc
[array\[v0.0.44_account\]]{.param-type}
:::

::: param
users (optional)
:::

::: param-desc
[array\[v0.0.44_user\]]{.param-type}
:::

::: param
qos (optional)
:::

::: param-desc
[array\[v0.0.44_qos\]]{.param-type}
:::

::: param
wckeys (optional)
:::

::: param-desc
[array\[v0.0.44_wckey\]]{.param-type}
:::

::: param
associations (optional)
:::

::: param-desc
[array\[v0.0.44_assoc\]]{.param-type}
:::

::: param
instances (optional)
:::

::: param-desc
[array\[v0.0.44_instance\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::::::::::::::
:::::::::::::::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_slurmdbd_jobs_resp` -]{#v0.0.44_openapi_slurmdbd_jobs_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
jobs
:::

::: param-desc
[array\[v0.0.44_job\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_slurmdbd_ping_resp` -]{#v0.0.44_openapi_slurmdbd_ping_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
pings
:::

::: param-desc
[array\[v0.0.44_slurmdbd_ping\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_slurmdbd_qos_removed_resp` -]{#v0.0.44_openapi_slurmdbd_qos_removed_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
removed_qos
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_slurmdbd_qos_resp` -]{#v0.0.44_openapi_slurmdbd_qos_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
qos
:::

::: param-desc
[array\[v0.0.44_qos\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_slurmdbd_stats_resp` -]{#v0.0.44_openapi_slurmdbd_stats_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
statistics
:::

::: param-desc
[v0.0.44_stats_rec]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_tres_resp` -]{#v0.0.44_openapi_tres_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
TRES
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::: model
### [`v0.0.44_openapi_users_add_cond_resp` -]{#v0.0.44_openapi_users_add_cond_resp} Up

::: model-description
:::

::::::::::::: field-items
::: param
association_condition
:::

::: param-desc
[v0.0.44_users_add_cond]{.param-type}
:::

::: param
user
:::

::: param-desc
[v0.0.44_user_short]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_users_add_cond_resp_str` -]{#v0.0.44_openapi_users_add_cond_resp_str} Up

::: model-description
:::

::::::::::: field-items
::: param
added_users
:::

::: param-desc
[String]{.param-type} added_users
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_users_resp` -]{#v0.0.44_openapi_users_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
users
:::

::: param-desc
[array\[v0.0.44_user\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::: model
### [`v0.0.44_openapi_warning` -]{#v0.0.44_openapi_warning} Up

::: model-description
:::

::::::: field-items
::: param
description (optional)
:::

::: param-desc
[String]{.param-type} Long form warning description
:::

::: param
source (optional)
:::

::: param-desc
[String]{.param-type} Source of warning or where warning was first detected
:::
:::::::
:::::::::

::::::::::::: model
### [`v0.0.44_openapi_wckey_removed_resp` -]{#v0.0.44_openapi_wckey_removed_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
deleted_wckeys
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_openapi_wckey_resp` -]{#v0.0.44_openapi_wckey_resp} Up

::: model-description
:::

::::::::::: field-items
::: param
wckeys
:::

::: param-desc
[array\[v0.0.44_wckey\]]{.param-type}
:::

::: param
meta (optional)
:::

::: param-desc
[v0.0.44_openapi_meta]{.param-type}
:::

::: param
errors (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_error\]]{.param-type}
:::

::: param
warnings (optional)
:::

::: param-desc
[array\[v0.0.44_openapi_warning\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::: model
### [`v0.0.44_part_prio` -]{#v0.0.44_part_prio} Up

::: model-description
:::

::::::: field-items
::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition name
:::

::: param
priority (optional)
:::

::: param-desc
[Integer]{.param-type} Prospective job priority if it runs in this partition format: int32
:::
:::::::
:::::::::

:::::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_partition_info` -]{#v0.0.44_partition_info} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
nodes (optional)
:::

::: param-desc
[v0_0_44_partition_info_nodes]{.param-type}
:::

::: param
accounts (optional)
:::

::: param-desc
[v0_0_44_partition_info_accounts]{.param-type}
:::

::: param
groups (optional)
:::

::: param-desc
[v0_0_44_partition_info_groups]{.param-type}
:::

::: param
qos (optional)
:::

::: param-desc
[v0_0_44_partition_info_qos]{.param-type}
:::

::: param
alternate (optional)
:::

::: param-desc
[String]{.param-type} Alternate - Partition name of alternate partition to be used if the state of this partition is DRAIN or INACTIVE
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_partition_info_tres]{.param-type}
:::

::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
select_type (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Scheduler consumable resource selection type
:::

::: param-enum-header
Enum:
:::

::: param
cpus (optional)
:::

::: param-desc
[v0_0_44_partition_info_cpus]{.param-type}
:::

::: param
defaults (optional)
:::

::: param-desc
[v0_0_44_partition_info_defaults]{.param-type}
:::

::: param
grace_time (optional)
:::

::: param-desc
[Integer]{.param-type} GraceTime - Grace time in seconds to be extended to a job which has been selected for preemption format: int32
:::

::: param
maximums (optional)
:::

::: param-desc
[v0_0_44_partition_info_maximums]{.param-type}
:::

::: param
minimums (optional)
:::

::: param-desc
[v0_0_44_partition_info_minimums]{.param-type}
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} PartitionName - Name by which the partition may be referenced
:::

::: param
node_sets (optional)
:::

::: param-desc
[String]{.param-type} NodeSets - Comma-separated list of nodesets which are associated with this partition
:::

::: param
priority (optional)
:::

::: param-desc
[v0_0_44_partition_info_priority]{.param-type}
:::

::: param
timeouts (optional)
:::

::: param-desc
[v0_0_44_partition_info_timeouts]{.param-type}
:::

::: param
topology (optional)
:::

::: param-desc
[String]{.param-type} Topology - Name of the topology, defined in topology.yaml, used by jobs in this partition
:::

::: param
partition (optional)
:::

::: param-desc
[v0_0_44_partition_info_partition]{.param-type}
:::

::: param
suspend_time (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::: model
### [`v0.0.44_process_exit_code_verbose` -]{#v0.0.44_process_exit_code_verbose} Up

::: model-description
:::

:::::::::: field-items
::: param
status (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Status given by return code
:::

::: param-enum-header
Enum:
:::

::: param
return_code (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
signal (optional)
:::

::: param-desc
[v0_0_44_process_exit_code_verbose_signal]{.param-type}
:::
::::::::::
::::::::::::

:::::::::::::::::::::::: model
### [`v0.0.44_qos` -]{#v0.0.44_qos} Up

::: model-description
:::

:::::::::::::::::::::: field-items
::: param
description (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary description
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags, to avoid modifying current values specify NOT_SET
:::

::: param-enum-header
Enum:
:::

::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} Unique ID format: int32
:::

::: param
limits (optional)
:::

::: param-desc
[v0_0_44_qos_limits]{.param-type}
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Name
:::

::: param
preempt (optional)
:::

::: param-desc
[v0_0_44_qos_preempt]{.param-type}
:::

::: param
priority (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
usage_factor (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::

::: param
usage_threshold (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::
::::::::::::::::::::::
::::::::::::::::::::::::

::::::::: model
### [`v0.0.44_reservation_core_spec` -]{#v0.0.44_reservation_core_spec} Up

::: model-description
:::

::::::: field-items
::: param
node (optional)
:::

::: param-desc
[String]{.param-type} Name of reserved node
:::

::: param
core (optional)
:::

::: param-desc
[String]{.param-type} IDs of reserved cores
:::
:::::::
:::::::::

:::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_reservation_desc_msg` -]{#v0.0.44_reservation_desc_msg} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::::::: field-items
::: param
accounts (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
burst_buffer (optional)
:::

::: param-desc
[String]{.param-type} BurstBuffer
:::

::: param
comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string
:::

::: param
core_count (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
duration (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
end_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
features (optional)
:::

::: param-desc
[String]{.param-type} Requested node features. Multiple values may be \"&\" separated if all features are required (AND operation) or separated by \"\|\" if any of the specified features are required (OR operation). Parenthesis are also supported for features to be ANDed together with counts of nodes having the specified features.
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags associated with this reservation. Note, to remove flags use \"NO\_\" prefixed flag excluding NO_HOLD_JOBS_AFTER_END
:::

::: param-enum-header
Enum:
:::

::: param
groups (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
licenses (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
max_start_delay (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} ReservationName
:::

::: param
node_count (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
node_list (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} Partition used to reserve nodes from. This will attempt to allocate all nodes in the specified partition unless you request fewer resources than are available with core_cnt, node_cnt or tres.
:::

::: param
purge_completed (optional)
:::

::: param-desc
[v0_0_44_reservation_info_purge_completed]{.param-type}
:::

::: param
start_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
users (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::
::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_reservation_info` -]{#v0.0.44_reservation_info} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::::::::::: field-items
::: param
accounts (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of permitted accounts
:::

::: param
burst_buffer (optional)
:::

::: param-desc
[String]{.param-type} BurstBuffer - Burst buffer resources reserved
:::

::: param
core_count (optional)
:::

::: param-desc
[Integer]{.param-type} CoreCnt - Number of cores reserved format: int32
:::

::: param
core_specializations (optional)
:::

::: param-desc
[array\[v0.0.44_reservation_core_spec\]]{.param-type}
:::

::: param
end_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
features (optional)
:::

::: param-desc
[String]{.param-type} Features - Expression describing the reservation\'s required node features
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags associated with this reservation
:::

::: param-enum-header
Enum:
:::

::: param
groups (optional)
:::

::: param-desc
[String]{.param-type} Groups - Comma-separated list of permitted groups
:::

::: param
licenses (optional)
:::

::: param-desc
[String]{.param-type} Licenses - Comma-separated list of licenses reserved
:::

::: param
max_start_delay (optional)
:::

::: param-desc
[Integer]{.param-type} MaxStartDelay - Maximum time an eligible job not requesting this reservation can delay a job requesting it in seconds format: int32
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} ReservationName - Name of the reservation
:::

::: param
node_count (optional)
:::

::: param-desc
[Integer]{.param-type} NodeCnt - Number of nodes reserved format: int32
:::

::: param
node_list (optional)
:::

::: param-desc
[String]{.param-type} Nodes - Comma-separated list of node names and/or node ranges reserved
:::

::: param
partition (optional)
:::

::: param-desc
[String]{.param-type} PartitionName - Partition used to reserve nodes from
:::

::: param
purge_completed (optional)
:::

::: param-desc
[v0_0_44_reservation_info_purge_completed]{.param-type}
:::

::: param
start_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
watts (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of required TRES
:::

::: param
users (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of permitted users
:::
::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

::::::: model
### [`v0.0.44_reservation_mod_req` -]{#v0.0.44_reservation_mod_req} Up

::: model-description
:::

::::: field-items
::: param
reservations (optional)
:::

::: param-desc
[array\[v0.0.44_reservation_desc_msg\]]{.param-type}
:::
:::::
:::::::

::::::::::: model
### [`v0.0.44_rollup_stats` -]{#v0.0.44_rollup_stats} Up

::: model-description
:::

::::::::: field-items
::: param
hourly (optional)
:::

::: param-desc
[v0_0_44_rollup_stats_hourly]{.param-type}
:::

::: param
daily (optional)
:::

::: param-desc
[v0_0_44_rollup_stats_daily]{.param-type}
:::

::: param
monthly (optional)
:::

::: param-desc
[v0_0_44_rollup_stats_monthly]{.param-type}
:::
:::::::::
:::::::::::

::::::::::::::::: model
### [`v0.0.44_schedule_exit_fields` -]{#v0.0.44_schedule_exit_fields} Up

::: model-description
:::

::::::::::::::: field-items
::: param
end_job_queue (optional)
:::

::: param-desc
[Integer]{.param-type} Reached end of queue format: int32
:::

::: param
default_queue_depth (optional)
:::

::: param-desc
[Integer]{.param-type} Reached number of jobs allowed to be tested format: int32
:::

::: param
max_job_start (optional)
:::

::: param-desc
[Integer]{.param-type} Reached number of jobs allowed to start format: int32
:::

::: param
max_rpc_cnt (optional)
:::

::: param-desc
[Integer]{.param-type} Reached RPC limit format: int32
:::

::: param
max_sched_time (optional)
:::

::: param-desc
[Integer]{.param-type} Reached maximum allowed scheduler time format: int32
:::

::: param
licenses (optional)
:::

::: param-desc
[Integer]{.param-type} Blocked on licenses format: int32
:::
:::::::::::::::
:::::::::::::::::

::::::::: model
### [`v0.0.44_shares_float128_tres` -]{#v0.0.44_shares_float128_tres} Up

::: model-description
:::

::::::: field-items
::: param
name (optional)
:::

::: param-desc
[String]{.param-type} TRES name
:::

::: param
value (optional)
:::

::: param-desc
[BigDecimal]{.param-type} TRES value
:::
:::::::
:::::::::

::::::::: model
### [`v0.0.44_shares_resp_msg` -]{#v0.0.44_shares_resp_msg} Up

::: model-description
:::

::::::: field-items
::: param
shares (optional)
:::

::: param-desc
[array\[v0.0.44_assoc_shares_obj_wrap\]]{.param-type}
:::

::: param
total_shares (optional)
:::

::: param-desc
[Long]{.param-type} Total number of shares format: int64
:::
:::::::
:::::::::

::::::::: model
### [`v0.0.44_shares_uint64_tres` -]{#v0.0.44_shares_uint64_tres} Up

::: model-description
:::

::::::: field-items
::: param
name (optional)
:::

::: param-desc
[String]{.param-type} TRES name
:::

::: param
value (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::::::::: model
### [`v0.0.44_slurm_step_id` -]{#v0.0.44_slurm_step_id} Up

::: model-description
:::

::::::::::: field-items
::: param
sluid (optional)
:::

::: param-desc
[String]{.param-type} SLUID (Slurm Lexicographically-sortable Unique ID)
:::

::: param
job_id (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
step_het_component (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
step_id (optional)
:::

::: param-desc
[String]{.param-type} Job step ID
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0.0.44_slurmdbd_ping` -]{#v0.0.44_slurmdbd_ping} Up

::: model-description
:::

::::::::::: field-items
::: param
hostname
:::

::: param-desc
[String]{.param-type} Target for ping
:::

::: param
responding
:::

::: param-desc
[Boolean]{.param-type} If ping RPC responded with pong from slurmdbd
:::

::: param
latency
:::

::: param-desc
[Long]{.param-type} Number of microseconds it took to successfully ping or timeout format: int64
:::

::: param
primary
:::

::: param-desc
[Boolean]{.param-type} Is responding slurmdbd the primary controller (Is responding slurmctld the primary controller)
:::
:::::::::::
:::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_stats_msg` -]{#v0.0.44_stats_msg} Up

::: model-description
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: field-items
::: param
parts_packed (optional)
:::

::: param-desc
[Integer]{.param-type} Zero if only RPC statistic included format: int32
:::

::: param
req_time (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
req_time_start (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
server_thread_count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of current active slurmctld threads format: int32
:::

::: param
agent_queue_size (optional)
:::

::: param-desc
[Integer]{.param-type} Number of enqueued outgoing RPC requests in an internal retry list format: int32
:::

::: param
agent_count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of agent threads format: int32
:::

::: param
agent_thread_count (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of active threads created by all agent threads format: int32
:::

::: param
dbd_agent_queue_size (optional)
:::

::: param-desc
[Integer]{.param-type} Number of messages for SlurmDBD that are queued format: int32
:::

::: param
gettimeofday_latency (optional)
:::

::: param-desc
[Integer]{.param-type} Latency of 1000 calls to the gettimeofday() syscall in microseconds, as measured at controller startup format: int32
:::

::: param
schedule_cycle_max (optional)
:::

::: param-desc
[Integer]{.param-type} Max time of any scheduling cycle in microseconds since last reset format: int32
:::

::: param
schedule_cycle_last (optional)
:::

::: param-desc
[Integer]{.param-type} Time in microseconds for last scheduling cycle format: int32
:::

::: param
schedule_cycle_sum (optional)
:::

::: param-desc
[Long]{.param-type} Total run time in microseconds for all scheduling cycles since last reset format: int64
:::

::: param
schedule_cycle_total (optional)
:::

::: param-desc
[Integer]{.param-type} Number of scheduling cycles since last reset format: int32
:::

::: param
schedule_cycle_mean (optional)
:::

::: param-desc
[Long]{.param-type} Mean time in microseconds for all scheduling cycles since last reset format: int64
:::

::: param
schedule_cycle_mean_depth (optional)
:::

::: param-desc
[Long]{.param-type} Mean of the number of jobs processed in a scheduling cycle format: int64
:::

::: param
schedule_cycle_per_minute (optional)
:::

::: param-desc
[Long]{.param-type} Number of scheduling executions per minute format: int64
:::

::: param
schedule_cycle_depth (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of jobs processed in scheduling cycles format: int32
:::

::: param
schedule_exit (optional)
:::

::: param-desc
[v0.0.44_schedule_exit_fields]{.param-type}
:::

::: param
schedule_queue_length (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs pending in queue format: int32
:::

::: param
jobs_submitted (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs submitted since last reset format: int32
:::

::: param
jobs_started (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs started since last reset format: int32
:::

::: param
jobs_completed (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs completed since last reset format: int32
:::

::: param
jobs_canceled (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs canceled since the last reset format: int32
:::

::: param
jobs_failed (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs failed due to slurmd or other internal issues since last reset format: int32
:::

::: param
jobs_pending (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs pending at the time of listed in job_state_ts format: int32
:::

::: param
jobs_running (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs running at the time of listed in job_state_ts format: int32
:::

::: param
job_states_ts (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
bf_backfilled_jobs (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs started through backfilling since last slurm start format: int32
:::

::: param
bf_last_backfilled_jobs (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs started through backfilling since last reset format: int32
:::

::: param
bf_backfilled_het_jobs (optional)
:::

::: param-desc
[Integer]{.param-type} Number of heterogeneous job components started through backfilling since last Slurm start format: int32
:::

::: param
bf_cycle_counter (optional)
:::

::: param-desc
[Integer]{.param-type} Number of backfill scheduling cycles since last reset format: int32
:::

::: param
bf_cycle_mean (optional)
:::

::: param-desc
[Long]{.param-type} Mean time in microseconds of backfilling scheduling cycles since last reset format: int64
:::

::: param
bf_depth_mean (optional)
:::

::: param-desc
[Long]{.param-type} Mean number of eligible to run jobs processed during all backfilling scheduling cycles since last reset format: int64
:::

::: param
bf_depth_mean_try (optional)
:::

::: param-desc
[Long]{.param-type} The subset of Depth Mean that the backfill scheduler attempted to schedule format: int64
:::

::: param
bf_cycle_sum (optional)
:::

::: param-desc
[Long]{.param-type} Total time in microseconds of backfilling scheduling cycles since last reset format: int64
:::

::: param
bf_cycle_last (optional)
:::

::: param-desc
[Integer]{.param-type} Execution time in microseconds of last backfill scheduling cycle format: int32
:::

::: param
bf_cycle_max (optional)
:::

::: param-desc
[Integer]{.param-type} Execution time in microseconds of longest backfill scheduling cycle format: int32
:::

::: param
bf_exit (optional)
:::

::: param-desc
[v0.0.44_bf_exit_fields]{.param-type}
:::

::: param
bf_last_depth (optional)
:::

::: param-desc
[Integer]{.param-type} Number of processed jobs during last backfilling scheduling cycle format: int32
:::

::: param
bf_last_depth_try (optional)
:::

::: param-desc
[Integer]{.param-type} Number of processed jobs during last backfilling scheduling cycle that had a chance to start using available resources format: int32
:::

::: param
bf_depth_sum (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of jobs processed during all backfilling scheduling cycles since last reset format: int32
:::

::: param
bf_depth_try_sum (optional)
:::

::: param-desc
[Integer]{.param-type} Subset of bf_depth_sum that the backfill scheduler attempted to schedule format: int32
:::

::: param
bf_queue_len (optional)
:::

::: param-desc
[Integer]{.param-type} Number of jobs pending to be processed by backfilling algorithm format: int32
:::

::: param
bf_queue_len_mean (optional)
:::

::: param-desc
[Long]{.param-type} Mean number of jobs pending to be processed by backfilling algorithm format: int64
:::

::: param
bf_queue_len_sum (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of jobs pending to be processed by backfilling algorithm since last reset format: int32
:::

::: param
bf_table_size (optional)
:::

::: param-desc
[Integer]{.param-type} Number of different time slots tested by the backfill scheduler in its last iteration format: int32
:::

::: param
bf_table_size_sum (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of different time slots tested by the backfill scheduler format: int32
:::

::: param
bf_table_size_mean (optional)
:::

::: param-desc
[Long]{.param-type} Mean number of different time slots tested by the backfill scheduler format: int64
:::

::: param
bf_when_last_cycle (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
bf_active (optional)
:::

::: param-desc
[Boolean]{.param-type} Backfill scheduler currently running
:::

::: param
rpcs_by_message_type (optional)
:::

::: param-desc
[array\[v0.0.44_stats_msg_rpc_type\]]{.param-type} RPCs by type
:::

::: param
rpcs_by_user (optional)
:::

::: param-desc
[array\[v0.0.44_stats_msg_rpc_user\]]{.param-type} RPCs by user
:::

::: param
pending_rpcs (optional)
:::

::: param-desc
[array\[v0.0.44_stats_msg_rpc_queue\]]{.param-type} Pending RPCs
:::

::: param
pending_rpcs_by_hostlist (optional)
:::

::: param-desc
[array\[v0.0.44_stats_msg_rpc_dump\]]{.param-type} Pending RPCs by hostlist
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::: model
### [`v0.0.44_stats_msg_rpc_dump` -]{#v0.0.44_stats_msg_rpc_dump} Up

::: model-description
:::

::::::::: field-items
::: param
type_id
:::

::: param-desc
[Integer]{.param-type} Message type as integer format: int32
:::

::: param
message_type
:::

::: param-desc
[String]{.param-type} Message type as string (Slurm RPC message type)
:::

::: param
count
:::

::: param-desc
[array\[String\]]{.param-type}
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0.0.44_stats_msg_rpc_queue` -]{#v0.0.44_stats_msg_rpc_queue} Up

::: model-description
:::

::::::::: field-items
::: param
type_id
:::

::: param-desc
[Integer]{.param-type} Message type as integer format: int32
:::

::: param
message_type
:::

::: param-desc
[String]{.param-type} Message type as string (Slurm RPC message type)
:::

::: param
count
:::

::: param-desc
[Integer]{.param-type} Number of pending RPCs queued format: int32
:::
:::::::::
:::::::::::

::::::::::::::::::::::: model
### [`v0.0.44_stats_msg_rpc_type` -]{#v0.0.44_stats_msg_rpc_type} Up

::: model-description
:::

::::::::::::::::::::: field-items
::: param
type_id
:::

::: param-desc
[Integer]{.param-type} Message type as integer format: int32
:::

::: param
message_type
:::

::: param-desc
[String]{.param-type} Message type as string (Slurm RPC message type)
:::

::: param
count
:::

::: param-desc
[Integer]{.param-type} Number of RPCs received format: int32
:::

::: param
queued
:::

::: param-desc
[Integer]{.param-type} Number of RPCs queued format: int32
:::

::: param
dropped
:::

::: param-desc
[Long]{.param-type} Number of RPCs dropped format: int64
:::

::: param
cycle_last
:::

::: param-desc
[Integer]{.param-type} Number of RPCs processed within the last RPC queue cycle format: int32
:::

::: param
cycle_max
:::

::: param-desc
[Integer]{.param-type} Maximum number of RPCs processed within a RPC queue cycle since start format: int32
:::

::: param
total_time
:::

::: param-desc
[Long]{.param-type} Total time spent processing RPC in seconds format: int64
:::

::: param
average_time
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::
:::::::::::::::::::::
:::::::::::::::::::::::

::::::::::::::: model
### [`v0.0.44_stats_msg_rpc_user` -]{#v0.0.44_stats_msg_rpc_user} Up

::: model-description
:::

::::::::::::: field-items
::: param
user_id
:::

::: param-desc
[Integer]{.param-type} User ID (numeric) format: int32
:::

::: param
user
:::

::: param-desc
[String]{.param-type} User name
:::

::: param
count
:::

::: param-desc
[Integer]{.param-type} Number of RPCs received format: int32
:::

::: param
total_time
:::

::: param-desc
[Long]{.param-type} Total time spent processing RPC in seconds format: int64
:::

::: param
average_time
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::::::: model
### [`v0.0.44_stats_rec` -]{#v0.0.44_stats_rec} Up

::: model-description
:::

::::::::::: field-items
::: param
time_start (optional)
:::

::: param-desc
[Long]{.param-type} When data collection started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
rollups (optional)
:::

::: param-desc
[v0.0.44_rollup_stats]{.param-type}
:::

::: param
RPCs (optional)
:::

::: param-desc
[array\[v0.0.44_stats_rpc\]]{.param-type}
:::

::: param
users (optional)
:::

::: param-desc
[array\[v0.0.44_stats_user\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::: model
### [`v0.0.44_stats_rpc` -]{#v0.0.44_stats_rpc} Up

::: model-description
:::

::::::::: field-items
::: param
rpc (optional)
:::

::: param-desc
[String]{.param-type} RPC type
:::

::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of RPCs processed format: int32
:::

::: param
time (optional)
:::

::: param-desc
[v0_0_44_stats_rpc_time]{.param-type}
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0.0.44_stats_user` -]{#v0.0.44_stats_user} Up

::: model-description
:::

::::::::: field-items
::: param
user (optional)
:::

::: param-desc
[String]{.param-type} User ID
:::

::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of RPCs processed format: int32
:::

::: param
time (optional)
:::

::: param-desc
[v0_0_44_stats_rpc_time]{.param-type}
:::
:::::::::
:::::::::::

:::::::::::::::::::::::::::::: model
### [`v0.0.44_step` -]{#v0.0.44_step} Up

::: model-description
:::

:::::::::::::::::::::::::::: field-items
::: param
time (optional)
:::

::: param-desc
[v0_0_44_step_time]{.param-type}
:::

::: param
exit_code (optional)
:::

::: param-desc
[v0.0.44_process_exit_code_verbose]{.param-type}
:::

::: param
nodes (optional)
:::

::: param-desc
[v0_0_44_step_nodes]{.param-type}
:::

::: param
tasks (optional)
:::

::: param-desc
[v0_0_44_step_tasks]{.param-type}
:::

::: param
pid (optional)
:::

::: param-desc
[String]{.param-type} Deprecated; Process ID
:::

::: param
CPU (optional)
:::

::: param-desc
[v0_0_44_step_CPU]{.param-type}
:::

::: param
kill_request_user (optional)
:::

::: param-desc
[String]{.param-type} User ID that requested termination of the step
:::

::: param
state (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Current state
:::

::: param-enum-header
Enum:
:::

::: param
statistics (optional)
:::

::: param-desc
[v0_0_44_step_statistics]{.param-type}
:::

::: param
step (optional)
:::

::: param-desc
[v0_0_44_step_step]{.param-type}
:::

::: param
task (optional)
:::

::: param-desc
[v0_0_44_step_task]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_step_tres]{.param-type}
:::
::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::

::::::::::::: model
### [`v0.0.44_tres` -]{#v0.0.44_tres} Up

::: model-description
:::

::::::::::: field-items
::: param
type
:::

::: param-desc
[String]{.param-type} TRES type (CPU, MEM, etc)
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} TRES name (if applicable)
:::

::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} ID used in the database format: int32
:::

::: param
count (optional)
:::

::: param-desc
[Long]{.param-type} TRES count (0 if listed generically) format: int64
:::
:::::::::::
:::::::::::::

::::::::::: model
### [`v0.0.44_uint16_no_val_struct` -]{#v0.0.44_uint16_no_val_struct} Up

::: model-description
:::

::::::::: field-items
::: param
set (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set; False if number is unset
:::

::: param
infinite (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set to infinite; \"set\" and \"number\" will be ignored
:::

::: param
number (optional)
:::

::: param-desc
[Integer]{.param-type} If \"set\" is True the number will be set with value; otherwise ignore number contents format: int32
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0.0.44_uint32_no_val_struct` -]{#v0.0.44_uint32_no_val_struct} Up

::: model-description
:::

::::::::: field-items
::: param
set (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set; False if number is unset
:::

::: param
infinite (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set to infinite; \"set\" and \"number\" will be ignored
:::

::: param
number (optional)
:::

::: param-desc
[Integer]{.param-type} If \"set\" is True the number will be set with value; otherwise ignore number contents format: int32
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0.0.44_uint64_no_val_struct` -]{#v0.0.44_uint64_no_val_struct} Up

::: model-description
:::

::::::::: field-items
::: param
set (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set; False if number is unset
:::

::: param
infinite (optional)
:::

::: param-desc
[Boolean]{.param-type} True if number has been set to infinite; \"set\" and \"number\" will be ignored
:::

::: param
number (optional)
:::

::: param-desc
[Long]{.param-type} If \"set\" is True the number will be set with value; otherwise ignore number contents format: int64
:::
:::::::::
:::::::::::

:::::::::::::::::::::::::::::::::::: model
### [`v0.0.44_update_node_msg` -]{#v0.0.44_update_node_msg} Up

::: model-description
:::

:::::::::::::::::::::::::::::::::: field-items
::: param
comment (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment
:::

::: param
cpu_bind (optional)
:::

::: param-desc
[Integer]{.param-type} Default method for binding tasks to allocated CPUs format: int32
:::

::: param
extra (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary string used for node filtering if extra constraints are enabled
:::

::: param
features (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
features_act (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
gres (optional)
:::

::: param-desc
[String]{.param-type} Generic resources
:::

::: param
address (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
hostname (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
name (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
state (optional)
:::

::: param-desc
[array\[String\]]{.param-type} New state to assign to the node
:::

::: param-enum-header
Enum:
:::

::: param
reason (optional)
:::

::: param-desc
[String]{.param-type} Reason for node being DOWN or DRAINING
:::

::: param
reason_uid (optional)
:::

::: param-desc
[String]{.param-type} User ID to associate with the reason (needed if user root is sending message)
:::

::: param
resume_after (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
topology_str (optional)
:::

::: param-desc
[String]{.param-type} Topology
:::

::: param
weight (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::: model
### [`v0.0.44_user` -]{#v0.0.44_user} Up

::: model-description
:::

::::::::::::::::::::: field-items
::: param
administrator_level (optional)
:::

::: param-desc
[array\[String\]]{.param-type} AdminLevel granted to the user
:::

::: param-enum-header
Enum:
:::

::: param
associations (optional)
:::

::: param-desc
[array\[v0.0.44_assoc_short\]]{.param-type}
:::

::: param
coordinators (optional)
:::

::: param-desc
[array\[v0.0.44_coord\]]{.param-type}
:::

::: param
default (optional)
:::

::: param-desc
[v0_0_44_user_default]{.param-type}
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags associated with this user
:::

::: param-enum-header
Enum:
:::

::: param
name
:::

::: param-desc
[String]{.param-type} User name
:::

::: param
old_name (optional)
:::

::: param-desc
[String]{.param-type} Previous user name
:::

::: param
wckeys (optional)
:::

::: param-desc
[array\[v0.0.44_wckey\]]{.param-type}
:::
:::::::::::::::::::::
:::::::::::::::::::::::

:::::::::::::: model
### [`v0.0.44_user_short` -]{#v0.0.44_user_short} Up

::: model-description
:::

:::::::::::: field-items
::: param
adminlevel (optional)
:::

::: param-desc
[array\[String\]]{.param-type} AdminLevel granted to the user
:::

::: param-enum-header
Enum:
:::

::: param
defaultqos (optional)
:::

::: param-desc
[Integer]{.param-type} Default QOS format: int32
:::

::: param
defaultaccount (optional)
:::

::: param-desc
[String]{.param-type} Default account
:::

::: param
defaultwckey (optional)
:::

::: param-desc
[String]{.param-type} Default WCKey
:::
::::::::::::
::::::::::::::

::::::::::::::::: model
### [`v0.0.44_users_add_cond` -]{#v0.0.44_users_add_cond} Up

::: model-description
:::

::::::::::::::: field-items
::: param
accounts (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
association (optional)
:::

::: param-desc
[v0.0.44_assoc_rec_set]{.param-type}
:::

::: param
clusters (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
partitions (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
users
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
wckeys (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::
:::::::::::::::
:::::::::::::::::

:::::::::::::::::: model
### [`v0.0.44_wckey` -]{#v0.0.44_wckey} Up

::: model-description
:::

:::::::::::::::: field-items
::: param
accounting (optional)
:::

::: param-desc
[array\[v0.0.44_accounting\]]{.param-type}
:::

::: param
cluster
:::

::: param-desc
[String]{.param-type} Cluster name
:::

::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} Unique ID for this user-cluster-wckey combination format: int32
:::

::: param
name
:::

::: param-desc
[String]{.param-type} WCKey name
:::

::: param
user
:::

::: param-desc
[String]{.param-type} User name
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags associated with this WCKey
:::

::: param-enum-header
Enum:
:::
::::::::::::::::
::::::::::::::::::

:::::::::: model
### [`v0.0.44_wckey_tag_struct` -]{#v0.0.44_wckey_tag_struct} Up

::: model-description
:::

:::::::: field-items
::: param
wckey
:::

::: param-desc
[String]{.param-type} WCKey name
:::

::: param
flags
:::

::: param-desc
[array\[String\]]{.param-type} Active flags
:::

::: param-enum-header
Enum:
:::
::::::::
::::::::::

::::::: model
### [`v0_0_44_accounting_allocated` -]{#v0_0_44_accounting_allocated} Up

::: model-description
:::

::::: field-items
::: param
seconds (optional)
:::

::: param-desc
[Long]{.param-type} Number of seconds allocated format: int64
:::
:::::
:::::::

::::::: model
### [`v0_0_44_assoc_default` -]{#v0_0_44_assoc_default} Up

::: model-description
:::

::::: field-items
::: param
qos (optional)
:::

::: param-desc
[String]{.param-type} Default QOS
:::
:::::
:::::::

::::::::::: model
### [`v0_0_44_assoc_max` -]{#v0_0_44_assoc_max} Up

::: model-description
:::

::::::::: field-items
::: param
jobs (optional)
:::

::: param-desc
[v0_0_44_assoc_max_jobs]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_assoc_max_tres]{.param-type}
:::

::: param
per (optional)
:::

::: param-desc
[v0_0_44_assoc_max_per]{.param-type}
:::
:::::::::
:::::::::::

::::::::::::: model
### [`v0_0_44_assoc_max_jobs` -]{#v0_0_44_assoc_max_jobs} Up

::: model-description
:::

::::::::::: field-items
::: param
per (optional)
:::

::: param-desc
[v0_0_44_assoc_max_jobs_per]{.param-type}
:::

::: param
active (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
accruing (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
total (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0_0_44_assoc_max_jobs_per` -]{#v0_0_44_assoc_max_jobs_per} Up

::: model-description
:::

::::::::::: field-items
::: param
count (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
accruing (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
submitted (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
wall_clock (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::::::::
:::::::::::::

::::::: model
### [`v0_0_44_assoc_max_per` -]{#v0_0_44_assoc_max_per} Up

::: model-description
:::

::::: field-items
::: param
account (optional)
:::

::: param-desc
[v0_0_44_assoc_max_per_account]{.param-type}
:::
:::::
:::::::

::::::: model
### [`v0_0_44_assoc_max_per_account` -]{#v0_0_44_assoc_max_per_account} Up

::: model-description
:::

::::: field-items
::: param
wall_clock (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::
:::::::

::::::::::::: model
### [`v0_0_44_assoc_max_tres` -]{#v0_0_44_assoc_max_tres} Up

::: model-description
:::

::::::::::: field-items
::: param
total (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
group (optional)
:::

::: param-desc
[v0_0_44_assoc_max_tres_group]{.param-type}
:::

::: param
minutes (optional)
:::

::: param-desc
[v0_0_44_assoc_max_tres_minutes]{.param-type}
:::

::: param
per (optional)
:::

::: param-desc
[v0_0_44_assoc_max_tres_per]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::: model
### [`v0_0_44_assoc_max_tres_group` -]{#v0_0_44_assoc_max_tres_group} Up

::: model-description
:::

::::::: field-items
::: param
minutes (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
active (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_assoc_max_tres_minutes` -]{#v0_0_44_assoc_max_tres_minutes} Up

::: model-description
:::

::::::: field-items
::: param
total (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
per (optional)
:::

::: param-desc
[v0_0_44_qos_limits_min_tres_per]{.param-type}
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_assoc_max_tres_per` -]{#v0_0_44_assoc_max_tres_per} Up

::: model-description
:::

::::::: field-items
::: param
job (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
node (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::
:::::::::

::::::: model
### [`v0_0_44_assoc_min` -]{#v0_0_44_assoc_min} Up

::: model-description
:::

::::: field-items
::: param
priority_threshold (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::
:::::::

::::::::: model
### [`v0_0_44_assoc_shares_obj_wrap_fairshare` -]{#v0_0_44_assoc_shares_obj_wrap_fairshare} Up

::: model-description
:::

::::::: field-items
::: param
factor (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::

::: param
level (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::::::: model
### [`v0_0_44_assoc_shares_obj_wrap_tres` -]{#v0_0_44_assoc_shares_obj_wrap_tres} Up

::: model-description
:::

::::::::: field-items
::: param
run_seconds (optional)
:::

::: param-desc
[array\[v0.0.44_shares_uint64_tres\]]{.param-type}
:::

::: param
group_minutes (optional)
:::

::: param-desc
[array\[v0.0.44_shares_uint64_tres\]]{.param-type}
:::

::: param
usage (optional)
:::

::: param-desc
[array\[v0.0.44_shares_float128_tres\]]{.param-type}
:::
:::::::::
:::::::::::

::::::: model
### [`v0_0_44_cluster_rec_associations` -]{#v0_0_44_cluster_rec_associations} Up

::: model-description
:::

::::: field-items
::: param
root (optional)
:::

::: param-desc
[v0.0.44_assoc_short]{.param-type}
:::
:::::
:::::::

::::::::: model
### [`v0_0_44_cluster_rec_controller` -]{#v0_0_44_cluster_rec_controller} Up

::: model-description
:::

::::::: field-items
::: param
host (optional)
:::

::: param-desc
[String]{.param-type} ControlHost
:::

::: param
port (optional)
:::

::: param-desc
[Integer]{.param-type} ControlPort format: int32
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_cron_entry_line` -]{#v0_0_44_cron_entry_line} Up

::: model-description
:::

::::::: field-items
::: param
start (optional)
:::

::: param-desc
[Integer]{.param-type} Start of this entry in file format: int32
:::

::: param
end (optional)
:::

::: param-desc
[Integer]{.param-type} End of this entry in file format: int32
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_instance_time` -]{#v0_0_44_instance_time} Up

::: model-description
:::

::::::: field-items
::: param
time_end (optional)
:::

::: param-desc
[Long]{.param-type} When the instance will end (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
time_start (optional)
:::

::: param-desc
[Long]{.param-type} When the instance will start (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::
:::::::
:::::::::

::::::::::::: model
### [`v0_0_44_job_array` -]{#v0_0_44_job_array} Up

::: model-description
:::

::::::::::: field-items
::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} Job ID of job array, or 0 if N/A format: int32
:::

::: param
limits (optional)
:::

::: param-desc
[v0_0_44_job_array_limits]{.param-type}
:::

::: param
task_id (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
task (optional)
:::

::: param-desc
[String]{.param-type} String expression of task IDs in this record
:::
:::::::::::
:::::::::::::

::::::: model
### [`v0_0_44_job_array_limits` -]{#v0_0_44_job_array_limits} Up

::: model-description
:::

::::: field-items
::: param
max (optional)
:::

::: param-desc
[v0_0_44_job_array_limits_max]{.param-type}
:::
:::::
:::::::

::::::: model
### [`v0_0_44_job_array_limits_max` -]{#v0_0_44_job_array_limits_max} Up

::: model-description
:::

::::: field-items
::: param
running (optional)
:::

::: param-desc
[v0_0_44_job_array_limits_max_running]{.param-type}
:::
:::::
:::::::

::::::: model
### [`v0_0_44_job_array_limits_max_running` -]{#v0_0_44_job_array_limits_max_running} Up

::: model-description
:::

::::: field-items
::: param
tasks (optional)
:::

::: param-desc
[Integer]{.param-type} Maximum number of simultaneously running tasks, 0 if no limit format: int32
:::
:::::
:::::::

::::::::::: model
### [`v0_0_44_job_comment` -]{#v0_0_44_job_comment} Up

::: model-description
:::

::::::::: field-items
::: param
administrator (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment made by administrator
:::

::: param
job (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment made by user
:::

::: param
system (optional)
:::

::: param-desc
[String]{.param-type} Arbitrary comment from slurmctld
:::
:::::::::
:::::::::::

::::::::::::::::::::::::: model
### [`v0_0_44_job_desc_msg_rlimits` -]{#v0_0_44_job_desc_msg_rlimits} Up

::: model-description
:::

::::::::::::::::::::::: field-items
::: param
cpu (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
fsize (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
data (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
stack (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
core (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
rss (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
nproc (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
nofile (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
memlock (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
as (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::
:::::::::::::::::::::::
:::::::::::::::::::::::::

::::::::: model
### [`v0_0_44_job_het` -]{#v0_0_44_job_het} Up

::: model-description
:::

::::::: field-items
::: param
job_id (optional)
:::

::: param-desc
[Integer]{.param-type} Heterogeneous job ID, if applicable format: int32
:::

::: param
job_offset (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::: model
### [`v0_0_44_job_info_power` -]{#v0_0_44_job_info_power} Up

::: model-description
:::

::::: field-items
::: param
flags (optional)
:::

::: param-desc
[array\[oas_any_type_not_mapped\]]{.param-type}
:::
:::::
:::::::

::::::: model
### [`v0_0_44_job_mcs` -]{#v0_0_44_job_mcs} Up

::: model-description
:::

::::: field-items
::: param
label (optional)
:::

::: param-desc
[String]{.param-type} Multi-Category Security label on the job
:::
:::::
:::::::

::::::: model
### [`v0_0_44_job_modify_tres` -]{#v0_0_44_job_modify_tres} Up

::: model-description
:::

::::: field-items
::: param
allocated (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::
:::::::

::::::::::: model
### [`v0_0_44_job_required` -]{#v0_0_44_job_required} Up

::: model-description
:::

::::::::: field-items
::: param
CPUs (optional)
:::

::: param-desc
[Integer]{.param-type} Minimum number of CPUs required format: int32
:::

::: param
memory_per_cpu (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
memory_per_node (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::
:::::::::
:::::::::::

::::::::: model
### [`v0_0_44_job_res_node_cpus` -]{#v0_0_44_job_res_node_cpus} Up

::: model-description
:::

::::::: field-items
::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of CPUs assigned to job format: int32
:::

::: param
used (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of CPUs used by job format: int32
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_job_res_node_memory` -]{#v0_0_44_job_res_node_memory} Up

::: model-description
:::

::::::: field-items
::: param
used (optional)
:::

::: param-desc
[Long]{.param-type} Total memory (MiB) used by job format: int64
:::

::: param
allocated (optional)
:::

::: param-desc
[Long]{.param-type} Total memory (MiB) allocated to job format: int64
:::
:::::::
:::::::::

:::::::::::::::: model
### [`v0_0_44_job_res_nodes` -]{#v0_0_44_job_res_nodes} Up

::: model-description
:::

:::::::::::::: field-items
::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of allocated nodes format: int32
:::

::: param
select_type (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Node scheduling selection method
:::

::: param-enum-header
Enum:
:::

::: param
list (optional)
:::

::: param-desc
[String]{.param-type} Node(s) allocated to the job
:::

::: param
whole (optional)
:::

::: param-desc
[Boolean]{.param-type} Whether whole nodes were allocated
:::

::: param
allocation (optional)
:::

::: param-desc
[array\[v0.0.44_job_res_node\]]{.param-type} Job resources for a node
:::
::::::::::::::
::::::::::::::::

::::::::::: model
### [`v0_0_44_job_reservation` -]{#v0_0_44_job_reservation} Up

::: model-description
:::

::::::::: field-items
::: param
id (optional)
:::

::: param-desc
[Integer]{.param-type} Unique identifier of requested reservation format: int32
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Name of reservation to use
:::

::: param
requested (optional)
:::

::: param-desc
[String]{.param-type} Comma-separated list of requested reservation names
:::
:::::::::
:::::::::::

:::::::::: model
### [`v0_0_44_job_state` -]{#v0_0_44_job_state} Up

::: model-description
:::

:::::::: field-items
::: param
current (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Current state
:::

::: param-enum-header
Enum:
:::

::: param
reason (optional)
:::

::: param-desc
[String]{.param-type} Reason for previous Pending or Failed state
:::
::::::::
::::::::::

::::::::::::::::::::::::::: model
### [`v0_0_44_job_time` -]{#v0_0_44_job_time} Up

::: model-description
:::

::::::::::::::::::::::::: field-items
::: param
elapsed (optional)
:::

::: param-desc
[Integer]{.param-type} Elapsed time in seconds format: int32
:::

::: param
eligible (optional)
:::

::: param-desc
[Long]{.param-type} Time when the job became eligible to run (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
end (optional)
:::

::: param-desc
[Long]{.param-type} End time (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
planned (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
start (optional)
:::

::: param-desc
[Long]{.param-type} Time execution began (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
submission (optional)
:::

::: param-desc
[Long]{.param-type} Time when the job was submitted (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
suspended (optional)
:::

::: param-desc
[Integer]{.param-type} Total time in suspended state in seconds format: int32
:::

::: param
system (optional)
:::

::: param-desc
[v0_0_44_job_time_system]{.param-type}
:::

::: param
limit (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
total (optional)
:::

::: param-desc
[v0_0_44_job_time_total]{.param-type}
:::

::: param
user (optional)
:::

::: param-desc
[v0_0_44_job_time_user]{.param-type}
:::
:::::::::::::::::::::::::
:::::::::::::::::::::::::::

::::::::: model
### [`v0_0_44_job_time_system` -]{#v0_0_44_job_time_system} Up

::: model-description
:::

::::::: field-items
::: param
seconds (optional)
:::

::: param-desc
[Long]{.param-type} System CPU time used by the job in seconds format: int64
:::

::: param
microseconds (optional)
:::

::: param-desc
[Long]{.param-type} System CPU time used by the job in microseconds format: int64
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_job_time_total` -]{#v0_0_44_job_time_total} Up

::: model-description
:::

::::::: field-items
::: param
seconds (optional)
:::

::: param-desc
[Long]{.param-type} Sum of System and User CPU time used by the job in seconds format: int64
:::

::: param
microseconds (optional)
:::

::: param-desc
[Long]{.param-type} Sum of System and User CPU time used by the job in microseconds format: int64
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_job_time_user` -]{#v0_0_44_job_time_user} Up

::: model-description
:::

::::::: field-items
::: param
seconds (optional)
:::

::: param-desc
[Long]{.param-type} User CPU time used by the job in seconds format: int64
:::

::: param
microseconds (optional)
:::

::: param-desc
[Long]{.param-type} User CPU time used by the job in microseconds format: int64
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_job_tres` -]{#v0_0_44_job_tres} Up

::: model-description
:::

::::::: field-items
::: param
allocated (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
requested (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::
:::::::::

::::::::::: model
### [`v0_0_44_kill_jobs_resp_job_error` -]{#v0_0_44_kill_jobs_resp_job_error} Up

::: model-description
:::

::::::::: field-items
::: param
string (optional)
:::

::: param-desc
[String]{.param-type} String error encountered signaling job
:::

::: param
code (optional)
:::

::: param-desc
[Integer]{.param-type} Numeric error encountered signaling job format: int32
:::

::: param
message (optional)
:::

::: param-desc
[String]{.param-type} Error message why signaling job failed
:::
:::::::::
:::::::::::

::::::: model
### [`v0_0_44_kill_jobs_resp_job_federation` -]{#v0_0_44_kill_jobs_resp_job_federation} Up

::: model-description
:::

::::: field-items
::: param
sibling (optional)
:::

::: param-desc
[String]{.param-type} Name of federation sibling (may be empty for non-federation)
:::
:::::
:::::::

::::::::::: model
### [`v0_0_44_openapi_meta_client` -]{#v0_0_44_openapi_meta_client} Up

::: model-description
:::

::::::::: field-items
::: param
source (optional)
:::

::: param-desc
[String]{.param-type} Client source description
:::

::: param
user (optional)
:::

::: param-desc
[String]{.param-type} Client user (if known)
:::

::: param
group (optional)
:::

::: param-desc
[String]{.param-type} Client group (if known)
:::
:::::::::
:::::::::::

::::::::::::: model
### [`v0_0_44_openapi_meta_plugin` -]{#v0_0_44_openapi_meta_plugin} Up

::: model-description
:::

::::::::::: field-items
::: param
type (optional)
:::

::: param-desc
[String]{.param-type} Slurm plugin type (if applicable)
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Slurm plugin name (if applicable)
:::

::: param
data_parser (optional)
:::

::: param-desc
[String]{.param-type} Slurm data_parser plugin
:::

::: param
accounting_storage (optional)
:::

::: param-desc
[String]{.param-type} Slurm accounting plugin
:::
:::::::::::
:::::::::::::

::::::::::: model
### [`v0_0_44_openapi_meta_slurm` -]{#v0_0_44_openapi_meta_slurm} Up

::: model-description
:::

::::::::: field-items
::: param
version (optional)
:::

::: param-desc
[v0_0_44_openapi_meta_slurm_version]{.param-type}
:::

::: param
release (optional)
:::

::: param-desc
[String]{.param-type} Slurm release string
:::

::: param
cluster (optional)
:::

::: param-desc
[String]{.param-type} Slurm cluster name
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0_0_44_openapi_meta_slurm_version` -]{#v0_0_44_openapi_meta_slurm_version} Up

::: model-description
:::

::::::::: field-items
::: param
major (optional)
:::

::: param-desc
[String]{.param-type} Slurm release major version
:::

::: param
micro (optional)
:::

::: param-desc
[String]{.param-type} Slurm release micro version
:::

::: param
minor (optional)
:::

::: param-desc
[String]{.param-type} Slurm release minor version
:::
:::::::::
:::::::::::

::::::::: model
### [`v0_0_44_partition_info_accounts` -]{#v0_0_44_partition_info_accounts} Up

::: model-description
:::

::::::: field-items
::: param
allowed (optional)
:::

::: param-desc
[String]{.param-type} AllowAccounts - Comma-separated list of accounts which may execute jobs in the partition
:::

::: param
deny (optional)
:::

::: param-desc
[String]{.param-type} DenyAccounts - Comma-separated list of accounts which may not execute jobs in the partition
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_partition_info_cpus` -]{#v0_0_44_partition_info_cpus} Up

::: model-description
:::

::::::: field-items
::: param
task_binding (optional)
:::

::: param-desc
[Integer]{.param-type} CpuBind - Default method controlling how tasks are bound to allocated resources format: int32
:::

::: param
total (optional)
:::

::: param-desc
[Integer]{.param-type} TotalCPUs - Number of CPUs available in this partition format: int32
:::
:::::::
:::::::::

::::::::::::::: model
### [`v0_0_44_partition_info_defaults` -]{#v0_0_44_partition_info_defaults} Up

::: model-description
:::

::::::::::::: field-items
::: param
memory_per_cpu (optional)
:::

::: param-desc
[Long]{.param-type} Raw value for DefMemPerCPU or DefMemPerNode format: int64
:::

::: param
partition_memory_per_cpu (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
partition_memory_per_node (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
time (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
job (optional)
:::

::: param-desc
[String]{.param-type} JobDefaults - Comma-separated list of job default values (this field is only used to set new defaults)
:::
:::::::::::::
:::::::::::::::

::::::: model
### [`v0_0_44_partition_info_groups` -]{#v0_0_44_partition_info_groups} Up

::: model-description
:::

::::: field-items
::: param
allowed (optional)
:::

::: param-desc
[String]{.param-type} AllowGroups - Comma-separated list of group names which may execute jobs in this partition
:::
:::::
:::::::

::::::::::::::::::::::::: model
### [`v0_0_44_partition_info_maximums` -]{#v0_0_44_partition_info_maximums} Up

::: model-description
:::

::::::::::::::::::::::: field-items
::: param
cpus_per_node (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
cpus_per_socket (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
memory_per_cpu (optional)
:::

::: param-desc
[Long]{.param-type} Raw value for MaxMemPerCPU or MaxMemPerNode format: int64
:::

::: param
partition_memory_per_cpu (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
partition_memory_per_node (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
nodes (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
shares (optional)
:::

::: param-desc
[Integer]{.param-type} OverSubscribe - Controls the ability of the partition to execute more than one job at a time on each resource format: int32
:::

::: param
oversubscribe (optional)
:::

::: param-desc
[v0_0_44_partition_info_maximums_oversubscribe]{.param-type}
:::

::: param
time (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
over_time_limit (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::
:::::::::::::::::::::::
:::::::::::::::::::::::::

:::::::::: model
### [`v0_0_44_partition_info_maximums_oversubscribe` -]{#v0_0_44_partition_info_maximums_oversubscribe} Up

::: model-description
:::

:::::::: field-items
::: param
jobs (optional)
:::

::: param-desc
[Integer]{.param-type} Maximum number of jobs allowed to oversubscribe resources format: int32
:::

::: param
flags (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Flags applicable to the OverSubscribe setting
:::

::: param-enum-header
Enum:
:::
::::::::
::::::::::

::::::: model
### [`v0_0_44_partition_info_minimums` -]{#v0_0_44_partition_info_minimums} Up

::: model-description
:::

::::: field-items
::: param
nodes (optional)
:::

::: param-desc
[Integer]{.param-type} MinNodes - Minimum count of nodes which may be allocated to any single job format: int32
:::
:::::
:::::::

::::::::::: model
### [`v0_0_44_partition_info_nodes` -]{#v0_0_44_partition_info_nodes} Up

::: model-description
:::

::::::::: field-items
::: param
allowed_allocation (optional)
:::

::: param-desc
[String]{.param-type} AllocNodes - Comma-separated list of nodes from which users can submit jobs in the partition
:::

::: param
configured (optional)
:::

::: param-desc
[String]{.param-type} Nodes - Comma-separated list of nodes which are associated with this partition
:::

::: param
total (optional)
:::

::: param-desc
[Integer]{.param-type} TotalNodes - Number of nodes available in this partition format: int32
:::
:::::::::
:::::::::::

:::::::: model
### [`v0_0_44_partition_info_partition` -]{#v0_0_44_partition_info_partition} Up

::: model-description
:::

:::::: field-items
::: param
state (optional)
:::

::: param-desc
[array\[String\]]{.param-type} Current state(s)
:::

::: param-enum-header
Enum:
:::
::::::
::::::::

::::::::: model
### [`v0_0_44_partition_info_priority` -]{#v0_0_44_partition_info_priority} Up

::: model-description
:::

::::::: field-items
::: param
job_factor (optional)
:::

::: param-desc
[Integer]{.param-type} PriorityJobFactor - Partition factor used by priority/multifactor plugin in calculating job priority format: int32
:::

::: param
tier (optional)
:::

::: param-desc
[Integer]{.param-type} PriorityTier - Controls the order in which the scheduler evaluates jobs from different partitions format: int32
:::
:::::::
:::::::::

::::::::::: model
### [`v0_0_44_partition_info_qos` -]{#v0_0_44_partition_info_qos} Up

::: model-description
:::

::::::::: field-items
::: param
allowed (optional)
:::

::: param-desc
[String]{.param-type} AllowQOS - Comma-separated list of Qos which may execute jobs in the partition
:::

::: param
deny (optional)
:::

::: param-desc
[String]{.param-type} DenyQOS - Comma-separated list of Qos which may not execute jobs in the partition
:::

::: param
assigned (optional)
:::

::: param-desc
[String]{.param-type} QOS - QOS name containing limits that will apply to all jobs in this partition
:::
:::::::::
:::::::::::

::::::::: model
### [`v0_0_44_partition_info_timeouts` -]{#v0_0_44_partition_info_timeouts} Up

::: model-description
:::

::::::: field-items
::: param
resume (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
suspend (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_partition_info_tres` -]{#v0_0_44_partition_info_tres} Up

::: model-description
:::

::::::: field-items
::: param
billing_weights (optional)
:::

::: param-desc
[String]{.param-type} TRESBillingWeights - Billing weights of each tracked TRES type that will be used in calculating the usage of a job
:::

::: param
configured (optional)
:::

::: param-desc
[String]{.param-type} TRES - Number of each applicable TRES type available in this partition
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_process_exit_code_verbose_signal` -]{#v0_0_44_process_exit_code_verbose_signal} Up

::: model-description
:::

::::::: field-items
::: param
id (optional)
:::

::: param-desc
[v0.0.44_uint16_no_val_struct]{.param-type}
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Signal sent to process (name)
:::
:::::::
:::::::::

::::::::::::: model
### [`v0_0_44_qos_limits` -]{#v0_0_44_qos_limits} Up

::: model-description
:::

::::::::::: field-items
::: param
grace_time (optional)
:::

::: param-desc
[Integer]{.param-type} GraceTime - Preemption grace time in seconds to be extended to a job which has been selected for preemption format: int32
:::

::: param
max (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max]{.param-type}
:::

::: param
factor (optional)
:::

::: param-desc
[v0.0.44_float64_no_val_struct]{.param-type}
:::

::: param
min (optional)
:::

::: param-desc
[v0_0_44_qos_limits_min]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::::: model
### [`v0_0_44_qos_limits_max` -]{#v0_0_44_qos_limits_max} Up

::: model-description
:::

::::::::::::: field-items
::: param
active_jobs (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_active_jobs]{.param-type}
:::

::: param
jobs (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_jobs]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_tres]{.param-type}
:::

::: param
wall_clock (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_wall_clock]{.param-type}
:::

::: param
accruing (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_jobs_active_jobs]{.param-type}
:::
:::::::::::::
:::::::::::::::

::::::::: model
### [`v0_0_44_qos_limits_max_active_jobs` -]{#v0_0_44_qos_limits_max_active_jobs} Up

::: model-description
:::

::::::: field-items
::: param
accruing (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
count (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::::::: model
### [`v0_0_44_qos_limits_max_jobs` -]{#v0_0_44_qos_limits_max_jobs} Up

::: model-description
:::

::::::::: field-items
::: param
count (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
active_jobs (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_jobs_active_jobs]{.param-type}
:::

::: param
per (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_jobs_active_jobs_per]{.param-type}
:::
:::::::::
:::::::::::

::::::: model
### [`v0_0_44_qos_limits_max_jobs_active_jobs` -]{#v0_0_44_qos_limits_max_jobs_active_jobs} Up

::: model-description
:::

::::: field-items
::: param
per (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_jobs_active_jobs_per]{.param-type}
:::
:::::
:::::::

::::::::: model
### [`v0_0_44_qos_limits_max_jobs_active_jobs_per` -]{#v0_0_44_qos_limits_max_jobs_active_jobs_per} Up

::: model-description
:::

::::::: field-items
::: param
account (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
user (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::::::: model
### [`v0_0_44_qos_limits_max_tres` -]{#v0_0_44_qos_limits_max_tres} Up

::: model-description
:::

::::::::: field-items
::: param
total (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
minutes (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_tres_minutes]{.param-type}
:::

::: param
per (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_tres_per]{.param-type}
:::
:::::::::
:::::::::::

::::::::: model
### [`v0_0_44_qos_limits_max_tres_minutes` -]{#v0_0_44_qos_limits_max_tres_minutes} Up

::: model-description
:::

::::::: field-items
::: param
total (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
per (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_tres_minutes_per]{.param-type}
:::
:::::::
:::::::::

::::::::::::: model
### [`v0_0_44_qos_limits_max_tres_minutes_per` -]{#v0_0_44_qos_limits_max_tres_minutes_per} Up

::: model-description
:::

::::::::::: field-items
::: param
qos (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
job (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
account (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
user (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0_0_44_qos_limits_max_tres_per` -]{#v0_0_44_qos_limits_max_tres_per} Up

::: model-description
:::

::::::::::: field-items
::: param
account (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
job (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
node (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
user (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::: model
### [`v0_0_44_qos_limits_max_wall_clock` -]{#v0_0_44_qos_limits_max_wall_clock} Up

::: model-description
:::

::::: field-items
::: param
per (optional)
:::

::: param-desc
[v0_0_44_qos_limits_max_wall_clock_per]{.param-type}
:::
:::::
:::::::

::::::::: model
### [`v0_0_44_qos_limits_max_wall_clock_per` -]{#v0_0_44_qos_limits_max_wall_clock_per} Up

::: model-description
:::

::::::: field-items
::: param
qos (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
job (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_qos_limits_min` -]{#v0_0_44_qos_limits_min} Up

::: model-description
:::

::::::: field-items
::: param
priority_threshold (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
tres (optional)
:::

::: param-desc
[v0_0_44_qos_limits_min_tres]{.param-type}
:::
:::::::
:::::::::

::::::: model
### [`v0_0_44_qos_limits_min_tres` -]{#v0_0_44_qos_limits_min_tres} Up

::: model-description
:::

::::: field-items
::: param
per (optional)
:::

::: param-desc
[v0_0_44_qos_limits_min_tres_per]{.param-type}
:::
:::::
:::::::

::::::: model
### [`v0_0_44_qos_limits_min_tres_per` -]{#v0_0_44_qos_limits_min_tres_per} Up

::: model-description
:::

::::: field-items
::: param
job (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::
:::::::

:::::::::::: model
### [`v0_0_44_qos_preempt` -]{#v0_0_44_qos_preempt} Up

::: model-description
:::

:::::::::: field-items
::: param
list (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::

::: param
mode (optional)
:::

::: param-desc
[array\[String\]]{.param-type} PreemptMode - Mechanism used to preempt jobs or enable gang scheduling
:::

::: param-enum-header
Enum:
:::

::: param
exempt_time (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
::::::::::
::::::::::::

::::::: model
### [`v0_0_44_reservation_info_purge_completed` -]{#v0_0_44_reservation_info_purge_completed} Up

::: model-description
:::

::::: field-items
::: param
time (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::
:::::::

::::::::::: model
### [`v0_0_44_rollup_stats_daily` -]{#v0_0_44_rollup_stats_daily} Up

::: model-description
:::

::::::::: field-items
::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of daily rollups since last_run format: int32
:::

::: param
last_run (optional)
:::

::: param-desc
[Long]{.param-type} Last time daily rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
duration (optional)
:::

::: param-desc
[v0_0_44_rollup_stats_daily_duration]{.param-type}
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0_0_44_rollup_stats_daily_duration` -]{#v0_0_44_rollup_stats_daily_duration} Up

::: model-description
:::

::::::::: field-items
::: param
last (optional)
:::

::: param-desc
[Long]{.param-type} Total time spent doing daily daily rollup (seconds) format: int64
:::

::: param
max (optional)
:::

::: param-desc
[Long]{.param-type} Longest daily rollup time (seconds) format: int64
:::

::: param
time (optional)
:::

::: param-desc
[Long]{.param-type} Total time spent doing daily rollups (seconds) format: int64
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0_0_44_rollup_stats_hourly` -]{#v0_0_44_rollup_stats_hourly} Up

::: model-description
:::

::::::::: field-items
::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of hourly rollups since last_run format: int32
:::

::: param
last_run (optional)
:::

::: param-desc
[Long]{.param-type} Last time hourly rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
duration (optional)
:::

::: param-desc
[v0_0_44_rollup_stats_hourly_duration]{.param-type}
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0_0_44_rollup_stats_hourly_duration` -]{#v0_0_44_rollup_stats_hourly_duration} Up

::: model-description
:::

::::::::: field-items
::: param
last (optional)
:::

::: param-desc
[Long]{.param-type} Total time spent doing last daily rollup (seconds) format: int64
:::

::: param
max (optional)
:::

::: param-desc
[Long]{.param-type} Longest hourly rollup time (seconds) format: int64
:::

::: param
time (optional)
:::

::: param-desc
[Long]{.param-type} Total time spent doing hourly rollups (seconds) format: int64
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0_0_44_rollup_stats_monthly` -]{#v0_0_44_rollup_stats_monthly} Up

::: model-description
:::

::::::::: field-items
::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of monthly rollups since last_run format: int32
:::

::: param
last_run (optional)
:::

::: param-desc
[Long]{.param-type} Last time monthly rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., \'\[MM/DD\[/YY\]-\]HH:MM\[:SS\]\')) format: int64
:::

::: param
duration (optional)
:::

::: param-desc
[v0_0_44_rollup_stats_monthly_duration]{.param-type}
:::
:::::::::
:::::::::::

::::::::::: model
### [`v0_0_44_rollup_stats_monthly_duration` -]{#v0_0_44_rollup_stats_monthly_duration} Up

::: model-description
:::

::::::::: field-items
::: param
last (optional)
:::

::: param-desc
[Long]{.param-type} Total time spent doing monthly daily rollup (seconds) format: int64
:::

::: param
max (optional)
:::

::: param-desc
[Long]{.param-type} Longest monthly rollup time (seconds) format: int64
:::

::: param
time (optional)
:::

::: param-desc
[Long]{.param-type} Total time spent doing monthly rollups (seconds) format: int64
:::
:::::::::
:::::::::::

::::::::: model
### [`v0_0_44_stats_rpc_time` -]{#v0_0_44_stats_rpc_time} Up

::: model-description
:::

::::::: field-items
::: param
average (optional)
:::

::: param-desc
[Long]{.param-type} Average RPC processing time in microseconds format: int64
:::

::: param
total (optional)
:::

::: param-desc
[Long]{.param-type} Total RPC processing time in microseconds format: int64
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_step_CPU` -]{#v0_0_44_step_CPU} Up

::: model-description
:::

::::::: field-items
::: param
requested_frequency (optional)
:::

::: param-desc
[v0_0_44_step_CPU_requested_frequency]{.param-type}
:::

::: param
governor (optional)
:::

::: param-desc
[String]{.param-type} Requested CPU frequency governor in kHz
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_step_CPU_requested_frequency` -]{#v0_0_44_step_CPU_requested_frequency} Up

::: model-description
:::

::::::: field-items
::: param
min (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
max (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::
:::::::
:::::::::

::::::::::: model
### [`v0_0_44_step_nodes` -]{#v0_0_44_step_nodes} Up

::: model-description
:::

::::::::: field-items
::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Number of nodes in the job step format: int32
:::

::: param
range (optional)
:::

::: param-desc
[String]{.param-type} Node(s) allocated to the job step
:::

::: param
list (optional)
:::

::: param-desc
[array\[String\]]{.param-type}
:::
:::::::::
:::::::::::

::::::::: model
### [`v0_0_44_step_statistics` -]{#v0_0_44_step_statistics} Up

::: model-description
:::

::::::: field-items
::: param
CPU (optional)
:::

::: param-desc
[v0_0_44_step_statistics_CPU]{.param-type}
:::

::: param
energy (optional)
:::

::: param-desc
[v0_0_44_step_statistics_energy]{.param-type}
:::
:::::::
:::::::::

::::::: model
### [`v0_0_44_step_statistics_CPU` -]{#v0_0_44_step_statistics_CPU} Up

::: model-description
:::

::::: field-items
::: param
actual_frequency (optional)
:::

::: param-desc
[Long]{.param-type} Average weighted CPU frequency of all tasks in kHz format: int64
:::
:::::
:::::::

::::::: model
### [`v0_0_44_step_statistics_energy` -]{#v0_0_44_step_statistics_energy} Up

::: model-description
:::

::::: field-items
::: param
consumed (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::
:::::
:::::::

::::::::::::::::::::: model
### [`v0_0_44_step_step` -]{#v0_0_44_step_step} Up

::: model-description
:::

::::::::::::::::::: field-items
::: param
id (optional)
:::

::: param-desc
[String]{.param-type} Step ID (Slurm job step ID)
:::

::: param
name (optional)
:::

::: param-desc
[String]{.param-type} Step name
:::

::: param
stderr (optional)
:::

::: param-desc
[String]{.param-type} Path to stderr file
:::

::: param
stdin (optional)
:::

::: param-desc
[String]{.param-type} Path to stdin file
:::

::: param
stdout (optional)
:::

::: param-desc
[String]{.param-type} Path to stdout file
:::

::: param
stderr_expanded (optional)
:::

::: param-desc
[String]{.param-type} Step stderr with expanded fields
:::

::: param
stdin_expanded (optional)
:::

::: param-desc
[String]{.param-type} Step stdin with expanded fields
:::

::: param
stdout_expanded (optional)
:::

::: param-desc
[String]{.param-type} Step stdout with expanded fields
:::
:::::::::::::::::::
:::::::::::::::::::::

::::::: model
### [`v0_0_44_step_task` -]{#v0_0_44_step_task} Up

::: model-description
:::

::::: field-items
::: param
distribution (optional)
:::

::: param-desc
[String]{.param-type} The layout of the step was when it was running
:::
:::::
:::::::

::::::: model
### [`v0_0_44_step_tasks` -]{#v0_0_44_step_tasks} Up

::: model-description
:::

::::: field-items
::: param
count (optional)
:::

::: param-desc
[Integer]{.param-type} Total number of tasks format: int32
:::
:::::
:::::::

::::::::::::::::::::: model
### [`v0_0_44_step_time` -]{#v0_0_44_step_time} Up

::: model-description
:::

::::::::::::::::::: field-items
::: param
elapsed (optional)
:::

::: param-desc
[Integer]{.param-type} Elapsed time in seconds format: int32
:::

::: param
end (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
start (optional)
:::

::: param-desc
[v0.0.44_uint64_no_val_struct]{.param-type}
:::

::: param
suspended (optional)
:::

::: param-desc
[Integer]{.param-type} Total time in suspended state in seconds format: int32
:::

::: param
system (optional)
:::

::: param-desc
[v0_0_44_step_time_system]{.param-type}
:::

::: param
limit (optional)
:::

::: param-desc
[v0.0.44_uint32_no_val_struct]{.param-type}
:::

::: param
total (optional)
:::

::: param-desc
[v0_0_44_step_time_total]{.param-type}
:::

::: param
user (optional)
:::

::: param-desc
[v0_0_44_step_time_user]{.param-type}
:::
:::::::::::::::::::
:::::::::::::::::::::

::::::::: model
### [`v0_0_44_step_time_system` -]{#v0_0_44_step_time_system} Up

::: model-description
:::

::::::: field-items
::: param
seconds (optional)
:::

::: param-desc
[Long]{.param-type} System CPU time used by the step in seconds format: int64
:::

::: param
microseconds (optional)
:::

::: param-desc
[Integer]{.param-type} System CPU time used by the step in microseconds format: int32
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_step_time_total` -]{#v0_0_44_step_time_total} Up

::: model-description
:::

::::::: field-items
::: param
seconds (optional)
:::

::: param-desc
[Long]{.param-type} Total CPU time used by the step in seconds format: int64
:::

::: param
microseconds (optional)
:::

::: param-desc
[Integer]{.param-type} Total CPU time used by the step in microseconds format: int32
:::
:::::::
:::::::::

::::::::: model
### [`v0_0_44_step_time_user` -]{#v0_0_44_step_time_user} Up

::: model-description
:::

::::::: field-items
::: param
seconds (optional)
:::

::: param-desc
[Long]{.param-type} User CPU time used by the step in seconds format: int64
:::

::: param
microseconds (optional)
:::

::: param-desc
[Integer]{.param-type} User CPU time used by the step in microseconds format: int32
:::
:::::::
:::::::::

::::::::::: model
### [`v0_0_44_step_tres` -]{#v0_0_44_step_tres} Up

::: model-description
:::

::::::::: field-items
::: param
requested (optional)
:::

::: param-desc
[v0_0_44_step_tres_requested]{.param-type}
:::

::: param
consumed (optional)
:::

::: param-desc
[v0_0_44_step_tres_consumed]{.param-type}
:::

::: param
allocated (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::::
:::::::::::

::::::::::::: model
### [`v0_0_44_step_tres_consumed` -]{#v0_0_44_step_tres_consumed} Up

::: model-description
:::

::::::::::: field-items
::: param
max (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
min (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
average (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
total (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::::: model
### [`v0_0_44_step_tres_requested` -]{#v0_0_44_step_tres_requested} Up

::: model-description
:::

::::::::::: field-items
::: param
max (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
min (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
average (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::

::: param
total (optional)
:::

::: param-desc
[array\[v0.0.44_tres\]]{.param-type}
:::
:::::::::::
:::::::::::::

::::::::::: model
### [`v0_0_44_user_default` -]{#v0_0_44_user_default} Up

::: model-description
:::

::::::::: field-items
::: param
qos (optional)
:::

::: param-desc
[Integer]{.param-type} Default QOS format: int32
:::

::: param
account (optional)
:::

::: param-desc
[String]{.param-type} Default account
:::

::: param
wckey (optional)
:::

::: param-desc
[String]{.param-type} Default WCKey
:::
:::::::::
:::::::::::
