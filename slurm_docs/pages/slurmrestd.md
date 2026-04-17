# slurmrestd

Section: Slurm REST Daemon (8)\
Updated: Slurm REST Daemon\
Index

[ ]{#lbAB}

## NAME

slurmrestd - Interface to Slurm via REST API. [ ]{#lbAC}

## SYNOPSIS

**slurmrestd** \[*OPTIONS*\...\] \<*\[host\]:port*\|*unix:/path/to/socket*\>\... [ ]{#lbAD}

## DESCRIPTION

**slurmrestd** is REST API interface for Slurm. It can be used in two modes:

**Inetd Mode**: slurmrestd will read and write to STDIO. If STDIN is a socket file descriptor, then slurmrestd will detect this and use relevant functionality. This mode is designed to work with piped input, inetd, xinetd or systemd socket activation.

**Listen Mode**: slurmrestd will open a listening socket on each requested *host*:*port* pair or UNIX socket.

[ ]{#lbAE}

## OPTIONS

**\[https://\]\[host\]:port**https://\]\[host\]:port\" href=\"#OPT\_\[https://\]\[host\]:port\"\>
:   Hostname and port to listen against. *host* may be an IPv4/IPv6 IP or a resolvable hostname. Hostnames are only looked up at startup and do not change for the life of the process. *host* is optional; if not provided, slurmrestd will listen on all network interfaces. *https://* is optional; if not provided, slurmrestd will automatically use TLS plugin to encrypt traffic when possible. If *https://* is specified; slurmrestd will require the configured TLS plugin to encrypt traffic.

:   

**unix:///path/to/socket**unix:///path/to/socket\" href=\"#OPT_unix:///path/to/socket\"\>
:   Listen on local UNIX socket. Must have permission to create socket in filesystem.

:   

**-a \<plugin\>**\[,plugin\]\...
:   Comma-delimited list of authentication plugins to load. By default all available authentication plugins will be loaded.

    :   

        **list**
        :   Display a list of the possible plugins to load.

        :   

        **rest_auth/local**
        :   Allows authentication via UNIX sockets when **auth/munge** is active.\
            **NOTE**: slurmrestd and client processes must run under the same UID or the client requests will be rejected.

        :   

        **rest_auth/jwt**
        :   Allows authentication via TCP and UNIX sockets when **AuthAltTypes=auth/jwt** is active. User must specify the following HTTP cookies with each request:

            :   

                **X-SLURM-USER-NAME**:\<user name\>

                :   

                :   

                **X-SLURM-USER-TOKEN**:\<JSON Web Token\>

                :   

        :   **NOTE**: Tokens are usually generated via calling \"**scontrol token**\".

:   

**-d \<plugin\>**\[,plugin\]\...
:   Comma-delimited list of data_parser plugins, which will determine the output format. May include optional flags denoted by \'+\' symbol. By default all available data_parser plugins will be loaded without any optional flags. See also **-s** for OpenAPI plugins controlling the available content. Defaults: all builtin supported data_parser plugins.

    :   

        **list\[+flags\]**
        :   Display a list of the possible plugins to load.

        :   

        **latest**
        :   Automatically replaced with latest plugin version. See relevant plugin for description and potential flags.

        :   

        **\[data_parser/\]v0.0.40\[+fast\]**
        :   Load data_parser/\]v0.0.40 plugin to for formatting of data. Only compatible with **openapi/slurmctld** and **openapi/slurmdbd** content plugins.

            :   

                **+fast**
                :   Disable builtin warnings and other logic to strictly validate incoming requests. Should only ever be used in a production environment with very well tested clients and potentially malformatted requests will be accepted as given and no warnings will be generated about ignored or incorrect fields or values.

                :   

        :   

        **\[data_parser/\]v0.0.41\[+fast\]\[+prefer_refs\]**
        :   Load data_parser/\]v0.0.41 plugin to for formatting of data. Only compatible with **openapi/slurmctld** and **openapi/slurmdbd** content plugins.

            :   

                **+fast**
                :   Disable builtin warnings and other logic to strictly validate incoming requests. Should only ever be used in a production environment with very well tested clients and potentially malformatted requests will be accepted as given and no warnings will be generated about ignored or incorrect fields or values.

                :   

                **+prefer_refs**
                :   Prefer inline expansion of referenced schemas (via *\$ref*) in generated OpenAPI specifications if the schema is only referenced once.

                :   

        :   

        **\[data_parser/\]v0.0.42\[+fast\]\[+minimize_refs\]\[+inline_enums\]**
        :   Load data_parser/\]v0.0.42 plugin to for formatting of data. Only compatible with **openapi/slurmctld** and **openapi/slurmdbd** content plugins.

            :   

                **+fast**
                :   Disable builtin warnings and other logic to strictly validate incoming requests. Should only ever be used in a production environment with very well tested clients and potentially malformatted requests will be accepted as given and no warnings will be generated about ignored or incorrect fields or values.

                :   

                **+minimize_refs**
                :   Avoid inline expansion of referenced schemas (via *\$ref*) in generated OpenAPI specifications if the schema is only referenced once.

                :   

                **+inline_enums**
                :   Avoid inline expansion of referenced schemas (via *\$ref*) in generated OpenAPI specifications for enum arrays.

                :   

        :   

        **\[data_parser/\]v0.0.43\[+fast\]\[+minimize_refs\]**
        :   Load data_parser/\]v0.0.43 plugin to for formatting of data. Only compatible with **openapi/slurmctld** and **openapi/slurmdbd** content plugins.

            :   

                **+fast**
                :   Disable builtin warnings and other logic to strictly validate incoming requests. Should only ever be used in a production environment with very well tested clients and potentially malformatted requests will be accepted as given and no warnings will be generated about ignored or incorrect fields or values.

                :   

                **+minimize_refs**
                :   Avoid inline expansion of referenced schemas (via *\$ref*) in generated OpenAPI specifications if the schema is only referenced once.

                :   

        :   

        **\[data_parser/\]v0.0.44\[+fast\]\[+minimize_refs\]**
        :   Load data_parser/\]v0.0.44 plugin to for formatting of data. Only compatible with **openapi/slurmctld**, **openapi/slurmdbd**, and **openapi/util** content plugins.

            :   

                **+fast**
                :   Disable builtin warnings and other logic to strictly validate incoming requests. Should only ever be used in a production environment with very well tested clients and potentially malformatted requests will be accepted as given and no warnings will be generated about ignored or incorrect fields or values.

                :   

                **+minimize_refs**
                :   Avoid inline expansion of referenced schemas (via *\$ref*) in generated OpenAPI specifications if the schema is only referenced once.

                :   

        :   

:   

**-f \<file\>**
:   Read Slurm configuration from the specified file. See **NOTES** below.

:   

**\--generate-openapi-spec**
:   Dump JSON formatted OpenAPI specification to stdout and exit immediately. Loads minimal plugins required. All \"content\" fields will only be in JSON format even if the *serializer/yaml* plugin is present and loadable. Loading of **[slurm.conf](slurm.conf.md)**(5) can be disabled by passing additional arguments **-f /dev/null** or setting **SLURM_CONF**=/dev/null in the environment.

:   

**-g \<group id\>**
:   Change group id (and drop supplemental groups) before processing client request. This should be a unique group with no write access or special permissions. Do not set this to the group belonging to to SlurmUser or root or the daemon won\'t start with the default settings.

:   

**-h**, **\--help**
:   Help; print a brief summary of command options.

:   

**\--max-connections \<count\>**
:   Set the maximum number of connections to process at any one time. This is independent of the number of connections that can connect to slurmrestd at any one time. The kernel allows any number of connections to be pending for processing at any one time when SYN cookies are active.

    :   

        **Caution**:
        :   Each connection could cause one RPC to the controller daemons, leading to potential overloading of the controller. Each connection can also hold memory for the duration of the life of the connection. Having too many connections processing at once could use considerably more memory. Process limits (**ulimit**(3)) may require adjustment when this value is increased.

        Default: 124

        :   

:   

**-s \<plugin\>**\[,plugin\]\...
:   Comma-delimited list of OpenAPI plugins to load, which will determine the available content. By default, OpenAPI plugins loaded will be *slurmctld,slurmdbd* when **AccountingStorageType**=*accounting_storage/slurmdbd* is configured in **[slurm.conf](slurm.conf.md)**(5) or *slurmctld* for any other configuration. See also **-d** for the data_parser plugins controlling the output format.

    :   

        **list**
        :   Display a list of the possible plugins to load.

        :   

        **\[openapi/\]slurmctld**
        :   Provides \'slurm/\' endpoints for the loaded data_parser plugins.

        :   

        **\[openapi/\]slurmdbd**
        :   Provides \'slurmdb/\' endpoints for the loaded data_parser plugins. This plugin will fail if **accounting_storage/slurmdbd** is not used in the cluster.

        :   

        **\[openapi/\]util**
        :   Provides \'util/\' endpoints for the loaded data_parser plugins. Util is short for utility. It provides utilities available directly through slurmrestd.

        :   

:   

**-t \<THREAD COUNT\>**
:   Specify number of threads to use to process client connections. Ignored in inetd mode.

:   

**-u \<user id\>**
:   Change user id before processing client request. This should be a unique group with no write access or special permissions. Do not set this user to SlurmUser or root or the daemon won\'t start with the default settings.

:   

**-v**
:   Verbose operation. Multiple **v**\'s can be specified, with each \'**v**\' beyond the first increasing verbosity, up to 6 times (i.e. -vvvvvv). Higher verbosity levels will have significant performance impact. See **SLURMRESTD_DEBUG** for description of logging targets.

:   

**-V**
:   Print version information and exit.

:   

[ ]{#lbAF}

## TLS

slurmrestd supports TLS encrypion via the TLS plugin interface. For a detailed description of TLS support in Slurm, see \<[https://slurm.schedmd.com/tls.html](tls.md)\>.

slurmrestd supports TLS encryption for incoming HTTPS connections independently of how **TLSType** in **[slurm.conf](slurm.conf.md)**(5) is configured. The configuration of **TLSParameters** in **[slurm.conf](slurm.conf.md)**(5) is always applied. This allows the Slurm RPC layer to remain unencrypted via TLS while allowing slurmrestd to service HTTPS requests via TLS.

slurmrestd includes automatic detection of incoming TLS connections. If TLS plugin is fully configured and successfully loads at startup, then all new incoming connections will be fingerprinted for SSLv3 (per RFC#6101) and TLSv1.x (per RFC#8446) handshakes. Upon a matching fingerprint, each incoming connections will then be encrypted via the configured TLS plugin for the duration of the connection. Support for TLS is handled independently of if the connection is a \[**unix**(2)\] **socket**(2) or **pipe(2)** (in INETD mode). Listening connections created with **https://** will be required to be encrypted via the TLS plugin. Any incoming connections to these listeners without TLS encryption will be closed immediately without sending an error response the client.

TLS support in slurmrestd is dependent on the requirements of the TLS plugin. slurmrestd will attempt to load the first available TLS plugin (except *tls/none*) automatically at startup. The requirements for each plugin are listed below:

**tls/s2n**
:   The following files must be present and readable by the invoking user (before **-u \<user id\>** is applied) at startup:

:   

    :   

        **restd_cert_file.pem**
        :   TLS x509 server public certificate. Must be signed by CA trusted by clients. The certificate\'s *CN* (common name) must match the hostname. slurmrestd ignores the host in client HTTP requests but most TLS clients will require they match.
            Note: The certificate\'s file must be placed in the **autoconf(1)** installation directory variable sysconfdir which can be overridden via setting **TLSParameters**=**restd_cert_file=***/path/to/restd_cert_file.pem* in **[slurm.conf](slurm.conf.md)**(5).

        :   

        **restd_cert_key_file.pem**
        :   Private key for **restd_cert_file.pem**. This file must **only** be readable by the slurmrestd user.
            Note: The certificate\'s file must be placed in the **autoconf(1)** installation directory variable sysconfdir which can be overridden via setting **TLSParameters**=**restd_cert_key_file=***/path/to/restd_cert_key.pem* in **[slurm.conf](slurm.conf.md)**(5).

        :   

:   

[ ]{#lbAG}

## ENVIRONMENT VARIABLES

The following environment variables can be used to override settings compiled into slurmrestd.

**ABORT_ON_FATAL**
:   When a fatal error is detected, use abort() instead of exit() to terminate the process. This allows backtraces to be captured without recompiling Slurm.

:   

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for slurmrestd to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

**SLURM_DEBUG**
:   Set debug level explicitly. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5). Increased if **-v** passed as argument during invocation. Ignored if **SLURMRESTD_DEBUG** or **SLURMRESTD_DEBUG_STDERR** or **SLURMRESTD_DEBUG_SYSLOG** are set in environment. See **SLURMRESTD_DEBUG** for description of logging targets.

:   

**SLURMRESTD_JSON** or **SLURM_JSON**
:   Control JSON serialization:

:   

    :   

        **compact**
        :   Output JSON as compact as possible.

        :   

        **pretty**
        :   Output JSON in pretty format to make it more readable.

        :   

**SLURM_JWT**
:   This variable must be set to use JWT token authentication.

:   

**SLURMRESTD_AUTH_TYPES**
:   Set allowed authentication types. See **-a**

:   

**SLURMRESTD_DEBUG**
:   Set debug level explicitly. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5). If a controlling TTY is detected, interactive mode will automatically activate to provide additional logging information to stderr. If a controlling TTY is not detected, then logs are sent to syslog. Increased if **-v** passed as argument during invocation. Ignored if **SLURMRESTD_DEBUG_STDERR** or **SLURMRESTD_DEBUG_SYSLOG** are set in environment.

:   

**SLURMRESTD_DEBUG_STDERR**
:   Set debug level explicitly for logging to STDERR. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5). Increased if **-v** passed as argument during invocation.

:   

**SLURMRESTD_DEBUG_SYSLOG**
:   Set debug level explicitly for logging to syslog. Valid values are 0-9, or the same string values as the debug options such as SlurmctldDebug in [slurm.conf](slurm.conf.md)(5). Increased if **-v** passed as argument during invocation.

:   

**SLURMRESTD_DATA_PARSER_PLUGINS**
:   Comma-delimited list of data_parser plugins to load. See **-d**

:   

**SLURMRESTD_LISTEN**
:   Comma-delimited list of host:port pairs or unix sockets to listen on.

:   

**SLURMRESTD_MAX_CONNECTIONS**
:   Set the maximum number of connections to process at any one time. See **\--max-connections**

:   

**SLURMRESTD_OPENAPI_PLUGINS**
:   Comma-delimited list of OpenAPI plugins to load. See **-s**

:   

**SLURMRESTD_RESPONSE_STATUS_CODES**
:   Comma-delimited list of OpenAPI method responses to generate in OpenAPI specification. Default: 200,default

:   

**SLURMRESTD_SECURITY**
:   Control slurmrestd security functionality using the following comma-delimited values:

:   

    :   

        **become_user**
        :   Allows **slurmrestd** to be run as root in order to become the requesting user for all requests. When combined with **rest_auth/local, when a user connects via a named UNIX socket, slurmrestd** will setuid()/setgid() into that user/group and then complete all requests as the given user. This mode is only intended for inet mode as the user change is permanent for the life of the process. This mode is incompatible with **rest_auth/jwt** and it is suggested to start **slurmrestd** with \"-a **rest_auth/local**\" arguments.

        :   

        **disable_unshare_files**
        :   Disables unsharing file descriptors with parent process.

        :   

        **disable_unshare_sysv**
        :   Disables unsharing the SYSV namespace.

        :   

        **disable_user_check**
        :   Disables check that slurmrestd is not running as root or SlurmUser, or with the root or SlurmUser\'s primary group. Disabling this check will allow slurmrestd to run as root or SlurmUser which will allow anyone who can communicate with this daemon to run anything as the root user on the cluster.

:   

**SLURMRESTD_YAML** or **SLURM_YAML**
:   Control YAML serialization:

:   

    :   

        **compact**
        :   Output YAML as compact as possible.

        :   

        **no_tag**
        :   Output YAML without datatype !!tags.

        :   

        **pretty**
        :   Output YAML in pretty format to make it more readable.

:   

[ ]{#lbAH}

## SIGNALS

**SIGINT**
:   **slurmrestd** will shutdown cleanly.

:   

**SIGPIPE**
:   This signal is explicitly ignored.

:   

**SIGPROF**
:   Logs connection manager state when debug level is at least info.

:   

[ ]{#lbAI}

## NOTES

**SPANK** and **clifilter** plugins are not supported in **slurmrestd** due to their lack of thread safety. Active **SPANK** plugins and **JobSubmitPlugins** in **slurmctld** are independent of slurmrestd and can be used to enforce site policy on job submissions.

[ ]{#lbAJ}

## EXAMPLES

Generate OpenAPI schema without configuration

:   $ slurmrestd -f /dev/null  --generate-openapi-spec -s slurmdbd,slurmctld -d v0.0.42 > openapi.json

Start **slurmrestd** with a UNIX socket in listen mode:

:   $ export SLURMRESTD=/var/spool/slurm/restd/rest
        $ slurmrestd -s slurmctld,slurmdbd -d v0.0.42 unix:$SLURMRESTD

Verify connectivity with slurmctld with a ping, with **slurmrestd** running in listen mode:

:   $ export $(scontrol token)
        $ curl --unix-socket "${SLURMRESTD}" -H "X-SLURM-USER-TOKEN:${SLURM_JWT}" 'http://ignored_with_unix_sockets/slurm/v0.0.42/ping' | jq '.pings'
        [
          {
            "hostname": "omicronpersei8",
            "pinged": "UP",
            "latency": 314,
            "mode": "primary"
          }
        ]

Verify connectivity with slurmdbd with a diag request, with **slurmrestd** running in listen mode:

:   $ export $(scontrol token)
        $ curl --unix-socket "${SLURMRESTD}" -H "X-SLURM-USER-TOKEN:${SLURM_JWT}" 'http://ignored_with_unix_sockets/slurmdb/v0.0.42/diag' | jq '.pings'
        1722009793

Query the status of a node with **slurmrestd** running in INETD mode:

:   $ echo -e "GET http://ignored/slurm/v0.0.42/node/host1 HTTP/1.1\r\n" | slurmrestd
        HTTP/1.1 200 OK
        Content-Length: 3174
        Content-Type: application/json

        {
          "nodes": [
            {
              "architecture": "x86_64",
              "burstbuffer_network_address": "",
              "boards": 1,
              "boot_time": {
                "set": true,
                "infinite": false,
                "number": 1720820315
              },
              "cluster_name": "",
              "cores": 16,
              "specialized_cores": 0,
              "cpu_binding": 0,
              "cpu_load": 446,
              "free_mem": {
                "set": true,
                "infinite": false,
                "number": 39871
              },
              "cpus": 32,
              "effective_cpus": 32,
              "specialized_cpus": "",
              "energy": {
                "average_watts": 0,
                "base_consumed_energy": 0,
                "consumed_energy": 0,
                "current_watts": {
                  "set": false,
                  "infinite": false,
                  "number": 0
                },
                "previous_consumed_energy": 0,
                "last_collected": 0
              },
              "external_sensors": {},
              "extra": "",
              "power": {},
              "features": [],
              "active_features": [],
              "gpu_spec": "",
              "gres": "gpu:fake1:1(S:0),gpu:fake2:1(S:0)",
              "gres_drained": "N/A",
              "gres_used": "gpu:fake1:0(IDX:N/A),gpu:fake2:0(IDX:N/A)",
              "instance_id": "",
              "instance_type": "",
              "last_busy": {
                "set": true,
                "infinite": false,
                "number": 1722009794
              },
              "mcs_label": "",
              "specialized_memory": 0,
              "name": "host1",
              "next_state_after_reboot": [
                "INVALID"
              ],
              "address": "localhost",
              "hostname": "omicronpersei8",
              "state": [
                "IDLE"
              ],
              "operating_system": "Linux 6.5.0-44-generic #44-Ubuntu SMP PREEMPT_DYNAMIC Fri Jun  7 15:10:09 UTC 2024",
              "owner": "",
              "partitions": [
                "debug"
              ],
              "port": 5015,
              "real_memory": 127927,
              "res_cores_per_gpu": 0,
              "comment": "",
              "reason": "",
              "reason_changed_at": {
                "set": true,
                "infinite": false,
                "number": 0
              },
              "reason_set_by_user": "",
              "resume_after": {
                "set": true,
                "infinite": false,
                "number": 0
              },
              "reservation": "",
              "alloc_memory": 0,
              "alloc_cpus": 0,
              "alloc_idle_cpus": 32,
              "tres_used": "",
              "tres_weighted": 0.0,
              "slurmd_start_time": {
                "set": true,
                "infinite": false,
                "number": 1722009794
              },
              "sockets": 1,
              "threads": 2,
              "temporary_disk": 0,
              "weight": 1,
              "tres": "cpu=32,mem=127927M,billing=32,gres/gpu=2",
              "version": "24.11.0-0rc1"
            }
          ],
          "last_update": {
            "set": true,
            "infinite": false,
            "number": 1722010273
          },
          "meta": {
        <<< TRIMMED >>>
          },
          "errors": [],
          "warnings": []
        }

Submit a job to **slurmrestd** with it running in listen mode:

:   $ jq . example_job.json
        {
          "job": {
            "script": "#!/bin/bash\nsleep 30",
            "name": "ExampleJob",
            "account": "sub1",
            "environment": [
              "PATH=/usr/bin/:/bin/"
            ],
            "current_working_directory": "/tmp/",
            "tasks": 12,
            "memory_per_cpu": 100,
            "time_limit": 240
          }
        }

        $ curl -H "Content-Type: application/json" --data-binary @example_job.json --unix-socket "${SLURMRESTD}" 'http://ignored/slurm/v0.0.42/job/submit'
        {
          "job_id": 9,
          "step_id": "batch",
          "job_submit_user_msg": "",
          "meta": {
        <<< TRIMMED >>>
          },
          "errors": [],
          "warnings": []
        }

        $ curl -H "Content-Type: application/json" --data-binary @example_job.json --unix-socket "${SLURMRESTD}" 'http://ignored/slurm/v0.0.42/job/submit'
        {
          "job_id": 7,
          "step_id": "batch",
          "job_submit_user_msg": "",
          "meta": {
          },
          "errors": [],
          "warnings": [
            {
              "description": "Expected OpenAPI type=array (Slurm type=list) but got OpenAPI type=object (Slurm type=dictionary): {      "source": "#/job/environment/"
            }
          ]
        }

[ ]{#lbAK}

## COPYING

Copyright (C) 2019-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAL}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[slurmctld](slurmctld.md)**(8), **[slurmdbd](slurmdbd.md)**(8)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

SYNOPSIS

:   

DESCRIPTION

:   

OPTIONS

:   

TLS

:   

ENVIRONMENT VARIABLES

:   

SIGNALS

:   

NOTES

:   

EXAMPLES

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
