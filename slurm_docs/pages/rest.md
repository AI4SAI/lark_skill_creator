# REST API Details

Slurm provides a https://restfulapi.net/ through the slurmrestd daemon, using [JSON Web Tokens](jwt.md) for authentication. This daemon is designed to allow clients to communicate with Slurm via a REST API (in addition to the command line interface (CLI) or C API).

See also:

- [REST API Quick Start Guide](rest_quickstart.md)
  - [Common Issues](rest_quickstart.md#common_issues)
- [REST API Methods and Models](rest_api.md)
- [slurmrestd man page](slurmrestd.md)
- [OpenAPI Plugin Release Notes](openapi_release_notes.md)
- [REST API Client Guide](rest_clients.md)

## Contents

Stateless

Run modes

- Inet Service Mode
- Listening Mode

Configuration

Plugins

High Availability

Security

- JSON Web Token (JWT) Authentication
- Local Authentication
- Authenticating Proxy

Python Guide

- Setup
- Usage Overview
- Job Submission
- Job, Node, and Reservation Control
- System Management

## Stateless

Slurmrestd is stateless as it does not cache or save any state between requests. Each request is handled in a thread and then all of that state is discarded. Any request to slurmrestd is completely synchronous with the Slurm controller (slurmctld or slurmdbd) and is only considered complete once the HTTP response code has been sent to the client. Slurmrestd will hold a client connection open while processing a request. Slurm database commands are committed at the end of every request, on the success of all API calls in the request.

Sites are strongly encouraged to setup a caching proxy between slurmrestd and clients to avoid having clients repeatedly call queries, causing usage to be higher than needed (and causing lock contention) on the controller.

## Run modes {#run_modes}

Slurmrestd currently supports two run modes: inet service mode and listening mode.

### Inet Service Mode {#inet}

The Slurmrestd daemon acts as an https://en.wikipedia.org/wiki/Inetd treating STDIN and STDOUT as the client. This mode allows clients to use inetd, xinetd, or systemd socket activated services and avoid the need to run a daemon on the host at all times. This mode creates an instance for each client and does not support reusing the same instance for different clients.

### Listening Mode {#listen}

The Slurmrestd daemon acts as a full UNIX service and continuously listens for new TCP connections. Each connection and request are independently authenticated.

## Configuration {#config}

slurmrestd can be configured either by environment variables or command line arguments. Please see the **doc/man/man1/slurmrestd.8** man page and [REST API Quick Start Guide](rest_quickstart.md#customization) for details.

## Plugins

As of Slurm 20.11, the REST API uses plugins for authentication and generating content. As of Slurm-21.08, the OpenAPI plugins are available outside of slurmrestd daemon and other slurm commands may provide or accept the latest version of the OpenAPI formatted output. This functionality is provided on a per command basis. Please refer to the [Data Parser Lifecycle](rest_clients.md#data_parser_lifecycle) documentation for the planned life cycles of versioned endpoints. These plugins can be optionally listed or selected via command line arguments as described in the [slurmrestd](slurmrestd.md) documentation.

## High Availability {#high_availability}

Slurmrestd is agnostic to its deployment in a highly available cluster. The daemon may be run on multiple nodes but does not provide any coordination with other instances for load balancing or failover. If such functionality is desired, a separate load balancer may be deployed. The load balancer should be able to forward any required authentication information on to the slurmrestd machines (see Security section).

The number of connections allowed by the slurmrestd system(s) should also be limited so that the slurmctld is not overwhelmed with requests. Pay attention to the `-t <THREAD COUNT>` and `--max-connections <count>` options to **slurmrestd**, the number of nodes deployed, and the specs of the machine running **slurmctld**.

## Security

The Slurm REST API is written to provide the necessary functionality for clients to control Slurm using REST commands. It is **not** designed to be directly internet facing. Only unencrypted and uncompressed HTTP communications are supported. Slurmrestd also has no protection against man in the middle or replay attacks. Slurmrestd should only be placed in a trusted network that will communicate with a trusted client.

Any site wishing to expose Slurm REST API to the internet or outside of the cluster should at the very least use a proxy to wrap all communications with TLS v1.3 (or later). You should also add monitoring to reject any client who repeatedly attempts invalid logins at either the network perimeter firewall or at the TLS proxy. Any client filtering that can be done via a proxy is suggested to avoid common internet crawlers from talking to slurmrestd and wasting system resource or even causing higher latency for valid clients. Sites are recommended to use shorter lived JWT tokens for clients and renew often, possibly via non-Slurm JWT generator to avoid having to enforce JWT lifespan limits. It is also suggested that sites use an authenticating proxy to handle all client authentication against the sites preferred Single Sign On (SSO) provider instead of Slurm **scontrol** generated tokens. This will prevent any unauthenticated client from connecting to slurmrestd.

The Slurm REST API is an HTTP server and all general possible precautions for security of any web server should be applied. As these precautions are site specific, it is highly recommended that you work with your site\'s security group to ensure all policies are enforced at the proxy before connecting to slurmrestd.

Slurm tries not to give potential attackers any hints when there are authentication failures. This results in the client getting this rather terse message: `Authentication failure`. When this happens, take a look at the logs for the relevant Slurm daemon (i.e. **slurmdbd**, **slurmctld**, or **slurmd**) for information about the actual issue.

### JSON Web Token (JWT) Authentication {#jwt}

slurmrestd supports using [JWT to authenticate users](jwt.html). JWT can be used to authenticate user over REST protocol.

- User Name Header: X-SLURM-USER-NAME
- JWT Header: X-SLURM-USER-TOKEN

SlurmUser or root can provide alternative user names to act as a proxy for the given user. While using JWT authentication, slurmrestd should be run as a unique, **unprivileged** user and group. Slurmrestd should be provided an invalid SLURM_JWT environment variable at startup to activate JWT authentication. This will allow users to provide their own JWT tokens while authenticating to the proxy and ensuring against any possible accidental authorizations.

When using JWT, it is important that [AuthAltTypes=auth/jwt]{.underline} be configured in both your slurm.conf and slurmdbd.conf for slurmrestd.

### Local Authentication {#local_auth}

slurmrestd supports using UNIX domain sockets to have the kernel authenticate local users. By default, slurmrestd will not start as root or SlurmUser or if the user\'s primary group belongs to root or SlurmUser. Slurmrestd must be located in the Munge security domain in order to function and communicate with Slurm in local authentication mode.

### Authenticating Proxy {#auth_proxy}

There is a wide array of authentication systems that a site could choose from, if using JWT authentication doesn\'t meet your requirements. An authenticating proxy is setup with a JWT token assigned to the SlurmUser that can then be used to proxy for any user on the cluster. This ability is only allowed for SlurmUser and the root users, all other tokens will only work with their locally assigned users.

If using a third-party authenticating proxy, it is expected that it will provide the correct HTTP headers (**X-SLURM-USER-NAME** and **X-SLURM-USER-TOKEN**) to slurmrestd along with the user\'s request.

Slurm places no requirements on the authenticating proxy beyond its being HTTP 1.1 compliant and that it provides the correct HTTP headers to allow client authentication. Slurm will explicitly trust the HTTP headers provided and has no way to verify them (beyond the proxy\'s trusted token **X-SLURM-USER-TOKEN**). Any authenticating proxy will need to follow your site\'s security policies and ensure that the proxied requests come from the correct user. These requirements are standard to any authenticated proxy and are not Slurm specific.

A working trivial example can be found in an https://gitlab.com/SchedMD/training/docker-scale-out/-/tree/master/proxy used for testing and training. It uses https://www.php.net/ and https://www.nginx.com/ to provide the authentication logic. This example should only be used as a basic starting place as it is not suitable for deployment in a production environment.

## Python Guide

OpenAPI tools can be used to generate a Python client to interact with the REST API. The examples below are for version 0.0.43 of the API, so there will be some differences with other versions.

### Setup {#python-setup}

1.  Install https://openapi-generator.tech/docs/installation/

2.  Compile the client library:

        slurmrestd --generate-openapi-spec > openapi.json
        openapi-generator-cli generate -i openapi.json -g python -o py_api_client

3.  (Optional, though recommended) Initialize and activate a Python virtual environment.

4.  Install the required packages:

        cd py_api_client/
        pip install -r requirements.txt

5.  Set up the Python script. These initial lines should be used for all subsequent examples, and assumes you have the \'SLURM_JWT\' environment variable set to a valid token:

        import os
        import time
        from openapi_client import SlurmApi
        from openapi_client import SlurmdbApi
        from openapi_client import ApiClient as Client
        from openapi_client import Configuration as Config

        c = Config()
        c.host = "http://localhost:8080/"
        c.access_token = os.getenv("SLURM_JWT")
        if not c.access_token:
            raise KeyError("No SLURM_JWT set")
        slurm = SlurmApi(Client(c))
        slurmdb = SlurmdbApi(Client(c))

        # Location of 'srun' binary + other relevant binaries in your slurm scripts
        environment=['PATH=/bin/:/sbin/:/home/slurm/bin/:/home/slurm/sbin/']
        curr_dir = '/tmp'

### Usage Overview {#python-usage-overview}

Once set up, you can use the `openapi_client` module to access classes and functions corresponding to the models and methods in the REST API. See below for examples and note the following naming conventions for converting between the REST API and the Python client:

- API model: `v0.0.43_job_desc_msg`\
  Corresponding Python class: `V0043JobDescMsg`
- API method: `POST /slurm/v0.0.43/job/submit`\
  Corresponding Python function: `slurm_v0043_post_job_submit()`

If you encounter any errors, check the common issues on the [REST Quickstart](rest_quickstart.md#common_issues) page.

### Job Submission {#python-job-submission}

This example shows how to populate a job submit request and job description message with desired submission parameters. It also illustrates how to send a POST request to submit the job.

    from openapi_client import V0043JobSubmitReq
    from openapi_client import V0043JobDescMsg

    # Populate a job submit request and job description message with desired parameters
    my_job = V0043JobSubmitReq(script='#!/bin/bash\nsrun sleep 300',
            job=V0043JobDescMsg(
                name='rest_test',
            partition='gpu',
            tres_per_job='gres:gpu:amd:4',
            time_limit={"set": True, "number": 5},
            required_nodes=["n2", "n4"],
            tasks=5,
                environment=environment,
                current_working_directory=curr_dir
        )
    )

    # Send POST request to submit the job
    submit_response = slurm.slurm_v0043_post_job_submit(my_job)

### Job, Node, and Reservation Control {#python-entity-control}

Jobs, nodes, and reservations can be managed through the Python client in similar ways. Each entity requires its own imports, and each has similar functions for viewing, modifying, and deleting. The GET functions and some of the POST/DELETE functions can also be used in the **plural** form, for example `slurm_v0043_get_jobs()`, to affect more than one entity. The relevant imports and functions are listed below.

- **Job Control**
  - Imports: `V0043JobSubmitReq`, `V0043JobDescMsg`
  - View: `slurm_v0043_get_job()`
  - Add (submit): `slurm_v0043_post_job_submit()`
  - Modify: `slurm_v0043_post_job()`
  - Delete (cancel): `slurm_v0043_delete_job()`
- **Node Control**
  - Imports: `V0043UpdateNodeMsg`
  - View: `slurm_v0043_get_node()`
  - Add (create): **N/A**
  - Modify: `slurm_v0043_post_node()`
  - Delete: `slurm_v0043_delete_node()`
- **Reservation Control**
  - Imports: `V0043ReservationDescMsg`
  - View: `slurm_v0043_get_reservation()`
  - Add (create): `slurm_v0043_post_reservation()`
  - Modify: `slurm_v0043_post_reservation()`
  - Delete: `slurm_v0043_delete_reservation()`

Here is an example for viewing, deleting, adding, and modifying reservations:

    from openapi_client import V0043ReservationDescMsg

    # GET request to query reservations
    resp = slurm.slurm_v0043_get_reservations()

    # Examine output of GET request
    if "important_jobs" in [resv.name for resv in resp.reservations]:
        resp = slurm.slurm_v0043_delete_reservation("important_jobs")

    # POST request to create a reservation with the desired parameters and flags
    slurm.slurm_v0043_post_reservation(
        V0043ReservationDescMsg(
            name="important_jobs",
            duration={"set": True, "number": 15},
            node_list=["n4", "n5"],
            start_time={"set": True, "number": int(time.time())},
            users=["slurm"],
            flags=["IGNORE_JOBS", "MAGNETIC", "DAILY"],
        )
    )

    # POST request to modify the reservation
    slurm.slurm_v0043_post_reservation(
        V0043ReservationDescMsg(
            name="important_jobs",
            duration={"set": True, "number": 20},
        )
    )

### System Management {#python-system-management}

A system reconfigure can be initiated with the function `slurm.slurm_v0043_get_reconfigure()`. System information can also be viewed with the following API functions:

- `slurm.slurm_v0043_get_partitions()`
- `slurm.slurm_v0043_get_diag()`
- `slurm.slurm_v0043_get_licenses()`

Here is an example for viewing partition info:

    # GET request to query partitions
    resp = slurm.slurm_v0043_get_partitions()

    # Examine request output to filter on a specific partition QOS
    qos_parts = [part for part in resp.partitions if 'sample' == part.qos.assigned]

    # GET request to query partitions with a specific name
    defq = slurm.slurm_v0043_get_partition("defq")

    # Examine request output to grab the nodes on a partition
    configured_nodes = defq.partitions[0].nodes.configured

------------------------------------------------------------------------
