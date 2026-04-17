# Containers Guide

## Contents

- Overview
- Known limitations
- Prerequisites
- Required software
- Example configurations for various OCI Runtimes
- Testing OCI runtime outside of Slurm
- Requesting container jobs or steps
- Integration with Rootless Docker
- Integration with Podman
- OCI Container bundle
- Example OpenMPI v5 + PMIx v4 container
- Container support via Plugin
  - Shifter
  - ENROOT and Pyxis
  - Sarus

## Overview

Containers are being adopted in HPC workloads. Containers rely on existing kernel features to allow greater user control over what applications see and can interact with at any given time. For HPC Workloads, these are usually restricted to the http://man7.org/linux/man-pages/man7/mount_namespaces.7.html. Slurm natively supports the requesting of unprivileged OCI Containers for jobs and steps.

Setting up containers requires several steps:

1.  Set up the kernel and a container runtime.
2.  Deploy a suitable [oci.conf](oci.conf.md) file accessible to the compute nodes (examples below).
3.  Restart or reconfigure slurmd on the compute nodes.
4.  Generate OCI bundles for containers that are needed and place them on the compute nodes.
5.  Verify that you can run containers directly through the chosen OCI runtime.
6.  Verify that you can request a container through Slurm.

## Known limitations {#limitations}

The following is a list of known limitations of the Slurm OCI container implementation.

- All containers must run under unprivileged (i.e. rootless) invocation. All commands are called by Slurm as the user with no special permissions.
- Custom container networks are not supported. All containers should work with the https://docs.docker.com/network/host/.
- Slurm will not transfer the OCI container bundle to the execution nodes. The bundle must already exist on the requested path on the execution node.
- Containers are limited by the OCI runtime used. If the runtime does not support a certain feature, then that feature will not work for any job using a container.
- oci.conf must be configured on the execution node for the job, otherwise the requested container will be ignored by Slurm (but can be used by the job or any given plugin).

## Prerequisites {#prereq}

The host kernel must be configured to allow user land containers:

    sudo sysctl -w kernel.unprivileged_userns_clone=1
    sudo sysctl -w kernel.apparmor_restrict_unprivileged_unconfined=0
    sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

Docker also provides a tool to verify the kernel configuration:

    $ dockerd-rootless-setuptool.sh check --force
    [INFO] Requirements are satisfied

## Required software: {#software}

- Fully functional https://github.com/opencontainers/runtime-spec/blob/master/runtime.md. It needs to be able to run outside of Slurm first.
- Fully functional OCI bundle generation tools. Slurm requires OCI Container compliant bundles for jobs.

## Example configurations for various OCI Runtimes {#example}

The https://github.com/opencontainers/runtime-spec provides requirements for all compliant runtimes but does **not** expressly provide requirements on how runtimes will use arguments. In order to support as many runtimes as possible, Slurm provides pattern replacement for commands issued for each OCI runtime operation. This will allow a site to edit how the OCI runtimes are called as needed to ensure compatibility.

For *runc* and *crun*, there are two sets of examples provided. The OCI runtime specification only provides the *start* and *create* operations sequence, but these runtimes provides a much more efficient *run* operation. Sites are strongly encouraged to use the *run* operation (if provided) as the *start* and *create* operations require that Slurm poll the OCI runtime to know when the containers have completed execution. While Slurm attempts to be as efficient as possible with polling, it will result in a thread using CPU time inside of the job and slower response of Slurm to catch when container execution is complete.

The examples provided have been tested to work but are only suggestions. Sites are expected to ensure that the resultant root directory used will be secure from cross user viewing and modifications. The examples provided point to \"/run/user/%U\" where %U will be replaced with the numeric user id. Systemd manages \"/run/user/\" (independently of Slurm) and will likely need additional configuration to ensure the directories exist on compute nodes when the users will not log in to the nodes directly. This configuration is generally achieved by calling https://www.freedesktop.org/software/systemd/man/latest/loginctl.html#enable-linger%20USER%E2%80%A6. Be aware that the directory in this example will be cleaned up by systemd once the user session ends on the node.

### oci.conf example for runc using create/start: {#runc_create_start}

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="runc --rootless=true --root=/run/user/%U/ state %n.%u.%j.%s.%t"
    RunTimeCreate="runc --rootless=true --root=/run/user/%U/ create %n.%u.%j.%s.%t -b %b"
    RunTimeStart="runc --rootless=true --root=/run/user/%U/ start %n.%u.%j.%s.%t"
    RunTimeKill="runc --rootless=true --root=/run/user/%U/ kill -a %n.%u.%j.%s.%t"
    RunTimeDelete="runc --rootless=true --root=/run/user/%U/ delete --force %n.%u.%j.%s.%t"

### oci.conf example for runc using run (recommended over using create/start): {#runc_run}

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="runc --rootless=true --root=/run/user/%U/ state %n.%u.%j.%s.%t"
    RunTimeKill="runc --rootless=true --root=/run/user/%U/ kill -a %n.%u.%j.%s.%t"
    RunTimeDelete="runc --rootless=true --root=/run/user/%U/ delete --force %n.%u.%j.%s.%t"
    RunTimeRun="runc --rootless=true --root=/run/user/%U/ run %n.%u.%j.%s.%t -b %b"

### oci.conf example for crun using create/start: {#crun_create_start}

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="crun --rootless=true --root=/run/user/%U/ state %n.%u.%j.%s.%t"
    RunTimeKill="crun --rootless=true --root=/run/user/%U/ kill -a %n.%u.%j.%s.%t"
    RunTimeDelete="crun --rootless=true --root=/run/user/%U/ delete --force %n.%u.%j.%s.%t"
    RunTimeCreate="crun --rootless=true --root=/run/user/%U/ create --bundle %b %n.%u.%j.%s.%t"
    RunTimeStart="crun --rootless=true --root=/run/user/%U/ start %n.%u.%j.%s.%t"

### oci.conf example for crun using run (recommended over using create/start): {#crun_run}

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="crun --rootless=true --root=/run/user/%U/ state %n.%u.%j.%s.%t"
    RunTimeKill="crun --rootless=true --root=/run/user/%U/ kill -a %n.%u.%j.%s.%t"
    RunTimeDelete="crun --rootless=true --root=/run/user/%U/ delete --force %n.%u.%j.%s.%t"
    RunTimeRun="crun --rootless=true --root=/run/user/%U/ run --bundle %b %n.%u.%j.%s.%t"

### oci.conf example for nvidia-container-runtime using create/start: {#nvidia_create_start}

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="nvidia-container-runtime --rootless=true --root=/run/user/%U/ state %n.%u.%j.%s.%t"
    RunTimeCreate="nvidia-container-runtime --rootless=true --root=/run/user/%U/ create %n.%u.%j.%s.%t -b %b"
    RunTimeStart="nvidia-container-runtime --rootless=true --root=/run/user/%U/ start %n.%u.%j.%s.%t"
    RunTimeKill="nvidia-container-runtime --rootless=true --root=/run/user/%U/ kill -a %n.%u.%j.%s.%t"
    RunTimeDelete="nvidia-container-runtime --rootless=true --root=/run/user/%U/ delete --force %n.%u.%j.%s.%t"

### oci.conf example for nvidia-container-runtime using run (recommended over using create/start): {#nvidia_run}

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="nvidia-container-runtime --rootless=true --root=/run/user/%U/ state %n.%u.%j.%s.%t"
    RunTimeKill="nvidia-container-runtime --rootless=true --root=/run/user/%U/ kill -a %n.%u.%j.%s.%t"
    RunTimeDelete="nvidia-container-runtime --rootless=true --root=/run/user/%U/ delete --force %n.%u.%j.%s.%t"
    RunTimeRun="nvidia-container-runtime --rootless=true --root=/run/user/%U/ run %n.%u.%j.%s.%t -b %b"

### oci.conf example for https://docs.sylabs.io/guides/4.1/admin-guide/installation.html using native runtime: {#singularity_native}

    IgnoreFileConfigJson=true
    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeRun="singularity exec --userns %r %@"
    RunTimeKill="kill -s SIGTERM %p"
    RunTimeDelete="kill -s SIGKILL %p"

### oci.conf example for https://docs.sylabs.io/guides/4.0/admin-guide/installation.html in OCI mode: {#singularity_oci}

Singularity v4.x requires setuid mode for OCI support.

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="sudo singularity oci state %n.%u.%j.%s.%t"
    RunTimeRun="sudo singularity oci run --bundle %b %n.%u.%j.%s.%t"
    RunTimeKill="sudo singularity oci kill %n.%u.%j.%s.%t"
    RunTimeDelete="sudo singularity oci delete %n.%u.%j.%s.%t"

**WARNING**: Singularity (v4.0.2) requires *sudo* or setuid binaries for OCI support, which is a security risk since the user is able to modify these calls. This example is only provided for testing purposes.

**WARNING**: https://groups.google.com/a/lbl.gov/g/singularity/c/vUMUkMlrpQc/m/gIsEiiP7AwAJ of the OCI interface appears to have ceased and sites should use the user namespace support instead.

### oci.conf example for hpcng Singularity v3.8.0: {#singularity_hpcng}

    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeQuery="sudo singularity oci state %n.%u.%j.%s.%t"
    RunTimeCreate="sudo singularity oci create --bundle %b %n.%u.%j.%s.%t"
    RunTimeStart="sudo singularity oci start %n.%u.%j.%s.%t"
    RunTimeKill="sudo singularity oci kill %n.%u.%j.%s.%t"
    RunTimeDelete="sudo singularity oci delete %n.%u.%j.%s.%t

**WARNING**: Singularity (v3.8.0) requires *sudo* or setuid binaries for OCI support, which is a security risk since the user is able to modify these calls. This example is only provided for testing purposes.

**WARNING**: https://groups.google.com/a/lbl.gov/g/singularity/c/vUMUkMlrpQc/m/gIsEiiP7AwAJ of the OCI interface appears to have ceased and sites should use the user namespace support instead.

### oci.conf example for https://github.com/hpc/charliecloud (v0.30) {#charliecloud}

    IgnoreFileConfigJson=true
    CreateEnvFile=newline
    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeRun="env -i PATH=/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin/:/sbin/ USER=$(whoami) HOME=/home/$(whoami)/ ch-run -w --bind /etc/group:/etc/group --bind /etc/passwd:/etc/passwd --bind /etc/slurm:/etc/slurm --bind %m:/var/run/slurm/ --bind /var/run/munge/:/var/run/munge/ --set-env=%e --no-passwd %r -- %@"
    RunTimeKill="kill -s SIGTERM %p"
    RunTimeDelete="kill -s SIGKILL %p"

### oci.conf example for https://github.com/NVIDIA/enroot (3.3.0) {#enroot}

    IgnoreFileConfigJson=true
    CreateEnvFile=newline
    EnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeEnvExclude="^(SLURM_CONF|SLURM_CONF_SERVER)="
    RunTimeRun="/usr/local/bin/enroot-start-wrapper %b %m %e -- %@"
    RunTimeKill="kill -s SIGINT %p"
    RunTimeDelete="kill -s SIGTERM %p"

/usr/local/bin/enroot-start-wrapper:

    #!/bin/bash
    BUNDLE="$1"
    SPOOLDIR="$2"
    ENVFILE="$3"
    shift 4
    IMAGE=

    export USER=$(whoami)
    export HOME="$BUNDLE/"
    export TERM
    export ENROOT_SQUASH_OPTIONS='-comp gzip -noD'
    export ENROOT_ALLOW_SUPERUSER=n
    export ENROOT_MOUNT_HOME=y
    export ENROOT_REMAP_ROOT=y
    export ENROOT_ROOTFS_WRITABLE=y
    export ENROOT_LOGIN_SHELL=n
    export ENROOT_TRANSFER_RETRIES=2
    export ENROOT_CACHE_PATH="$SPOOLDIR/"
    export ENROOT_DATA_PATH="$SPOOLDIR/"
    export ENROOT_TEMP_PATH="$SPOOLDIR/"
    export ENROOT_ENVIRON="$ENVFILE"

    if [ ! -f "$BUNDLE" ]
    then
            IMAGE="$SPOOLDIR/container.sqsh"
            enroot import -o "$IMAGE" -- "$BUNDLE" && \
            enroot create "$IMAGE"
            CONTAINER="container"
    else
            CONTAINER="$BUNDLE"
    fi

    enroot start -- "$CONTAINER" "$@"
    rc=$?

    [ $IMAGE ] && unlink $IMAGE

    exit $rc

### Handling multiple runtimes {#multiple-runtimes}

If you wish to accommodate multiple runtimes in your environment, it is possible to do so with a bit of extra setup. This section outlines one possible way to do so:

1.  Create a generic oci.conf that calls a wrapper script

        IgnoreFileConfigJson=true
        RunTimeRun="/opt/slurm-oci/run %b %m %u %U %n %j %s %t %@"
        RunTimeKill="kill -s SIGTERM %p"
        RunTimeDelete="kill -s SIGKILL %p"

2.  Create the wrapper script to check for user-specific run configuration (e.g., /opt/slurm-oci/run)

        #!/bin/bash
        if [[ -e ~/.slurm-oci-run ]]; then
            ~/.slurm-oci-run "$@"
        else
            /opt/slurm-oci/slurm-oci-run-default "$@"
        fi

3.  Create a generic run configuration to use as the default (e.g., /opt/slurm-oci/slurm-oci-run-default)

        #!/bin/bash --login
        # Parse
        CONTAINER="$1"
        SPOOL_DIR="$2"
        USER_NAME="$3"
        USER_ID="$4"
        NODE_NAME="$5"
        JOB_ID="$6"
        STEP_ID="$7"
        TASK_ID="$8"
        shift 8 # subsequent arguments are the command to run in the container
        # Run
        apptainer run --bind /var/spool --containall "$CONTAINER" "$@"

4.  Add executable permissions to both scripts

        chmod +x /opt/slurm-oci/run /opt/slurm-oci/slurm-oci-run-default

Once this is done, users may create a script at \'\~/.slurm-oci-run\' if they wish to customize the container run process, such as using a different container runtime. Users should model this file after the default \'/opt/slurm-oci/slurm-oci-run-default\'

## Testing OCI runtime outside of Slurm {#testing}

Slurm calls the OCI runtime directly in the job step. If it fails, then the job will also fail.

- Go to the directory containing the OCI Container bundle:

      cd $ABS_PATH_TO_BUNDLE

- Execute OCI Container runtime (You can find a few examples on how to build a bundle below):

      $OCIRunTime $ARGS create test --bundle $PATH_TO_BUNDLE

      $OCIRunTime $ARGS start test

      $OCIRunTime $ARGS kill test

      $OCIRunTime $ARGS delete test

  If these commands succeed, then the OCI runtime is correctly configured and can be tested in Slurm.

## Requesting container jobs or steps {#request}

*salloc*, *srun* and *sbatch* (in Slurm 21.08+) have the \'\--container\' argument, which can be used to request container runtime execution. The requested job container will not be inherited by the steps called, excluding the batch and interactive steps.

- Batch step inside of container:

      sbatch --container $ABS_PATH_TO_BUNDLE --wrap 'bash -c "cat /etc/*rel*"'

- Batch job with step 0 inside of container:

      sbatch --wrap 'srun bash -c "--container $ABS_PATH_TO_BUNDLE cat /etc/*rel*"'

- Interactive step inside of container:

      salloc --container $ABS_PATH_TO_BUNDLE bash -c "cat /etc/*rel*"

- Interactive job step 0 inside of container:

      salloc srun --container $ABS_PATH_TO_BUNDLE bash -c "cat /etc/*rel*"

- Job with step 0 inside of container:

      srun --container $ABS_PATH_TO_BUNDLE bash -c "cat /etc/*rel*"

- Job with step 1 inside of container:

      srun srun --container $ABS_PATH_TO_BUNDLE bash -c "cat /etc/*rel*"

**NOTE**: Commands run with the `--container` flag are resolved through PATH *before* they are sent to the container. If the container has a unique file structure, it may be necessary to give the full path to the command or specify `--export=NONE` to have the container define the PATH to be used:

    srun --container $ABS_PATH_TO_BUNDLE --export=NONE bash -c "cat /etc/*rel*"

## Integration with Rootless Docker (Docker Engine v20.10+ & Slurm-23.02+) {#docker-scrun}

Slurm\'s [scrun](scrun.md) can be directly integrated with https://docs.docker.com/engine/security/rootless/ to run containers as jobs. No special user permissions are required and **should not** be granted to use this functionality.

### Prerequisites {#prerequisites}

1.  [slurm.conf](slurm.conf.md) must be configured to use Munge authentication.

        AuthType=auth/munge

2.  [scrun.lua](scrun.html#SECTION_Example-%3CB%3Escrun.lua%3C/B%3E-scripts) must be configured for site storage configuration.

3.  https://docs.docker.com/engine/security/rootless/#routing-ping-packets

4.  https://docs.docker.com/engine/security/rootless/#exposing-privileged-ports

5.  [scrun.lua](scrun.md#SECTION_Example-%3CB%3Escrun.lua%3C/B%3E-scripts) must be present on any node where scrun may be run. The example should be sufficient for most environments but paths should be modified to match available local storage.

6.  [oci.conf](oci.conf.md) must be present on any node where any container job may be run. Example configurations for [known OCI runtimes](containers.md#example) are provided above. Examples may require paths to be correct to installation locations.

### Limitations {#limitations-1}

1.  JWT authentication is not supported.

2.  Docker container building is not currently functional pending merge of https://github.com/moby/moby/pull/41442.

3.  Docker does **not** expose configuration options to disable security options needed to run jobs. This requires that all calls to docker provide the following command line arguments. This can be done via shell variable, an alias, wrapper function, or wrapper script:

        --security-opt label:disable --security-opt seccomp=unconfined --security-opt apparmor=unconfined --net=none

    Docker\'s builtin security functionality is not required (or wanted) for containers being run by Slurm. Docker is only acting as a container image lifecycle manager. The containers will be executed remotely via Slurm following the existing security configuration in Slurm outside of unprivileged user control.

4.  All containers must use the https://docs.docker.com/network/drivers/none/. Attempting to use bridge, overlay, host, ipvlan, or macvlan can result in scrun being isolated from the network and not being able to communicate with the Slurm controller. The container is run by Slurm on the compute nodes which makes having Docker setup a network isolation layer ineffective for the container.

5.  `docker exec` command is not supported.

6.  `docker swarm` command is not supported.

7.  `docker compose`/`docker-compose` command is not supported.

8.  `docker pause` command is not supported.

9.  `docker unpause` command is not supported.

10. `docker swarm` command is not supported.

11. All `docker` commands are not supported inside of containers.

12. https://docs.docker.com/reference/api/engine/ is not supported inside of containers.

### Setup procedure

1.  https://docs.docker.com/engine/security/rootless/\
    Rootless Docker must be fully operational and able to run containers before continuing.

2.  Setup environment for all docker calls:

        export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock

    All commands following this will expect this environment variable to be set.

3.  Stop rootless docker:

        systemctl --user stop docker

4.  Configure Docker to call scrun instead of the default OCI runtime.

    - To configure for all users:

          /etc/docker/daemon.json

    - To configure per user:

          ~/.config/docker/daemon.json

    Set the following fields to configure Docker:

        {
            "experimental": true,
            "iptables": false,
            "bridge": "none",
            "no-new-privileges": true,
            "rootless": true,
            "selinux-enabled": false,
            "default-runtime": "slurm",
            "runtimes": {
                "slurm": {
                    "path": "/usr/local/bin/scrun"
                }
            },
            "data-root": "/run/user/${USER_ID}/docker/",
            "exec-root": "/run/user/${USER_ID}/docker-exec/"
        }

    Correct path to scrun as if installation prefix was configured. Replace \${USER_ID} with numeric user id or target a different directory with global write permissions and sticky bit. Rootless docker requires a different root directory than the system\'s default to avoid permission errors.

5.  It is strongly suggested that sites consider using inter-node shared filesystems to store Docker\'s containers. While it is possible to have a scrun.lua script to push and pull images for each deployment, there can be a massive performance penalty. Using a shared filesystem will avoid moving these files around.\
    Possible configuration additions to daemon.json to use a shared filesystem with https://docs.docker.com/storage/storagedriver/vfs-driver/:

        {
          "storage-driver": "vfs",
          "data-root": "/path/to/shared/filesystem/user_name/data/",
          "exec-root": "/path/to/shared/filesystem/user_name/exec/",
        }

    Any node expected to be able to run containers from Docker must have ability to at least read the filesystem used. Full write privileges are suggested and will be required if changes to the container filesystem are desired.

6.  Configure dockerd to not setup network namespace, which will break scrun\'s ability to talk to the Slurm controller.

    - To configure for all users:

          /etc/systemd/user/docker.service.d/override.conf

    - To configure per user:

          ~/.config/systemd/user/docker.service.d/override.conf

    <!-- -->

        [Service]
        Environment="DOCKERD_ROOTLESS_ROOTLESSKIT_PORT_DRIVER=none"
        Environment="DOCKERD_ROOTLESS_ROOTLESSKIT_NET=host"

7.  Reload docker\'s service unit in systemd:

        systemctl --user daemon-reload

8.  Start rootless docker:

        systemctl --user start docker

9.  Verify Docker is using scrun:

        export DOCKER_SECURITY="--security-opt label=disable --security-opt seccomp=unconfined  --security-opt apparmor=unconfined --net=none"
        docker run $DOCKER_SECURITY hello-world
        docker run $DOCKER_SECURITY alpine /bin/printenv SLURM_JOB_ID
        docker run $DOCKER_SECURITY alpine /bin/hostname
        docker run $DOCKER_SECURITY -e SCRUN_JOB_NUM_NODES=10 alpine /bin/hostname

## Integration with Podman (Slurm-23.02+) {#podman-scrun}

Slurm\'s [scrun](scrun.md) can be directly integrated with https://podman.io/ to run containers as jobs. No special user permissions are required and **should not** be granted to use this functionality.

### Prerequisites {#prerequisites-1}

1.  Slurm must be fully configured and running on host running podman.

2.  [slurm.conf](slurm.conf.md) must be configured to use Munge authentication.

        AuthType=auth/munge

3.  [scrun.lua](scrun.md) must be configured for site storage configuration.

4.  [scrun.lua](scrun.md#SECTION_Example-%3CB%3Escrun.lua%3C/B%3E-scripts) must be present on any node where scrun may be run. The example should be sufficient for most environments but paths should be modified to match available local storage.

5.  [oci.conf](oci.conf.md) must be present on any node where any container job may be run. Example configurations for [known OCI runtimes](containers.md#example) are provided above. Examples may require paths to be correct to installation locations.

### Limitations {#limitations-2}

1.  JWT authentication is not supported.
2.  All containers must use https://github.com/containers/podman/blob/main/docs/tutorials/basic_networking.md
3.  `podman exec` command is not supported.
4.  `podman-compose` command is not supported, due to only being partially implemented. Some compositions may work but each container may be run on different nodes. The network for all containers must be the `network_mode: host` device.
5.  `podman kube` command is not supported.
6.  `podman pod` command is not supported.
7.  `podman farm` command is not supported.
8.  All `podman` commands are not supported inside of containers.
9.  Podman REST API is not supported inside of containers.

### Setup procedure

1.  https://podman.io/docs/installation

2.  Verify rootless podman is configured

        $ podman info --format '{{.Host.Security.Rootless}}'
        true

3.  Verify rootless Podman is fully functional before adding Slurm support:
    - The value printed by the following commands should be the same:

          $ id
          $ podman run --userns keep-id alpine id

          $ sudo id
          $ podman run --userns nomap alpine id

4.  Configure Podman to call scrun instead of the https://github.com/opencontainers/runtime-spec. See https://github.com/containers/common/blob/main/docs/containers.conf.5.md for details on configuration locations and loading order for containers.conf.

    - To configure for all users: `/etc/containers/containers.conf`
    - To configure per user: `$XDG_CONFIG_HOME/containers/containers.conf` or `~/.config/containers/containers.conf` (if `$XDG_CONFIG_HOME` is not defined).

    Set the following configuration parameters to configure Podman\'s containers.conf:

        [containers]
        apparmor_profile = "unconfined"
        cgroupns = "host"
        cgroups = "enabled"
        default_sysctls = []
        label = false
        netns = "host"
        no_hosts = true
        pidns = "host"
        utsns = "host"
        userns = "host"
        log_driver = "journald"

        [engine]
        cgroup_manager = "systemd"
        runtime = "slurm"
        remote = false

        [engine.runtimes]
        slurm = [
            "/usr/local/bin/scrun",
            "/usr/bin/scrun"
        ]

    Correct path to scrun as if installation prefix was configured.

5.  The \"cgroup_manager\" field will need to be swapped to \"cgroupfs\" on systems not running systemd.

6.  It is strongly suggested that sites consider using inter-node shared filesystems to store Podman\'s containers. While it is possible to have a scrun.lua script to push and pull images for each deployment, there can be a massive performance penalty. Using a shared filesystem will avoid moving these files around.\

    - To configure for all users:

          /etc/containers/storage.conf

    - To configure per user:

          $XDG_CONFIG_HOME/containers/storage.conf

    Possible configuration additions to storage.conf to use a shared filesystem with https://docs.podman.io/en/latest/markdown/podman.1.html#storage-driver-value:

        [storage]
        driver = "vfs"
        runroot = "$HOME/containers"
        graphroot = "$HOME/containers"

        [storage.options]
        pull_options = {use_hard_links = "true", enable_partial_images = "true"}


        [storage.options.vfs]
        ignore_chown_errors = "true"

    Any node expected to be able to run containers from Podman must have ability to at least read the filesystem used. Full write privileges are suggested and will be required if changes to the container filesystem are desired.

7.  Verify Podman is using scrun:

        podman run hello-world
        podman run alpine printenv SLURM_JOB_ID
        podman run alpine hostname
        podman run alpine -e SCRUN_JOB_NUM_NODES=10 hostname
        salloc podman run --env-host=true alpine hostname
        salloc sh -c 'podman run -e SLURM_JOB_ID=$SLURM_JOB_ID alpine hostname'

8.  Optional: Create alias for Docker:

        alias docker=podman

    or

        alias docker='podman --config=/some/path "$@"'

### Troubleshooting

- Podman runs out of locks:

      $ podman run alpine uptime
      Error: allocating lock for new container: allocation failed; exceeded num_locks (2048)

  1.  Try renumbering:

          podman system renumber

  2.  Try resetting all storage:

          podman system reset

## OCI Container bundle {#bundle}

There are multiple ways to generate an OCI Container bundle. The instructions below are the method we found the easiest. The OCI standard provides the requirements for any given bundle: https://github.com/opencontainers/runtime-spec/blob/master/bundle.md

Here are instructions on how to generate a container using a few alternative container solutions:

Create an image and prepare it for use with runc:

Use an existing tool to create a filesystem image in /image/rootfs:

- debootstrap:

      sudo debootstrap stable /image/rootfs http://deb.debian.org/debian/

- yum:

      sudo yum --config /etc/yum.conf --installroot=/image/rootfs/ --nogpgcheck --releasever=${CENTOS_RELEASE} -y

- docker:

      mkdir -p ~/oci_images/alpine/rootfs
      cd ~/oci_images/
      docker pull alpine
      docker create --name alpine alpine
      docker export alpine | tar -C ~/oci_images/alpine/rootfs -xf -
      docker rm alpine

Configure a bundle for runtime to execute:

Use https://github.com/opencontainers/runc to generate a config.json:

    cd ~/oci_images/alpine
    runc --rootless=true spec --rootless

Test running image:

    srun --container ~/oci_images/alpine/ uptime

Use https://github.com/opencontainers/umoci and skopeo to generate a full image:

    mkdir -p ~/oci_images/
    cd ~/oci_images/
    skopeo copy docker://alpine:latest oci:alpine:latest
    umoci unpack --rootless --image alpine ~/oci_images/alpine
    srun --container ~/oci_images/alpine uptime

Use https://sylabs.io/guides/3.1/user-guide/oci_runtime.html to generate a full image:

    mkdir -p ~/oci_images/alpine/
    cd ~/oci_images/alpine/
    singularity pull alpine
    sudo singularity oci mount ~/oci_images/alpine/alpine_latest.sif ~/oci_images/alpine
    mv config.json singularity_config.json
    runc spec --rootless
    srun --container ~/oci_images/alpine/ uptime

## Example OpenMPI v5 + PMIx v4 container {#ex-ompi5-pmix4}

Minimalist Dockerfile to generate a image with OpenMPI and PMIx to test basic MPI jobs.

#### Dockerfile

    FROM almalinux:latest
    RUN dnf -y update && dnf -y upgrade && dnf install -y epel-release && dnf -y update
    RUN dnf -y install make automake gcc gcc-c++ kernel-devel bzip2 python3 wget libevent-devel hwloc-devel

    WORKDIR /usr/local/src/
    RUN wget --quiet 'https://github.com/openpmix/openpmix/releases/download/v5.0.7/pmix-5.0.7.tar.bz2' -O - | tar --no-same-owner -xvjf -
    WORKDIR /usr/local/src/pmix-5.0.7/
    RUN ./configure && make -j && make install

    WORKDIR /usr/local/src/
    RUN wget --quiet --inet4-only 'https://download.open-mpi.org/release/open-mpi/v5.0/openmpi-5.0.7.tar.bz2' -O - | tar --no-same-owner -xvjf -
    WORKDIR /usr/local/src/openmpi-5.0.7/
    RUN ./configure --disable-pty-support --enable-ipv6 --without-slurm --with-pmix --enable-debug && make -j && make install

    WORKDIR /usr/local/src/openmpi-5.0.7/examples
    RUN make && cp -v hello_c ring_c connectivity_c spc_example /usr/local/bin

## Container support via Plugin {#plugin}

Slurm allows container developers to create [SPANK Plugins](plugins.md) that can be called at various points of job execution to support containers. Any site using one of these plugins to start containers **should not** have an \"oci.conf\" configuration file. The \"oci.conf\" file activates the builtin container functionality which may conflict with the SPANK based plugin functionality.

The following projects are third party container solutions that have been designed to work with Slurm, but they have not been tested or validated by SchedMD.

### Shifter

https://github.com/NERSC/shifter is a container project out of http://www.nersc.gov/ to provide HPC containers with full scheduler integration.

- Shifter provides full https://github.com/NERSC/shifter/wiki/SLURM-Integration.
- Presentations about Shifter and Slurm:
  - [Never Port Your Code Again - Docker functionality with Shifter using SLURM](SLUG15/shifter.md)
  - https://www.slideshare.net/insideHPC/shifter-containers-in-hpc-environments

### ENROOT and Pyxis {#enroot1}

https://github.com/NVIDIA/enroot is a user namespace container system sponsored by https://www.nvidia.com/ that supports:

- Slurm integration via https://github.com/NVIDIA/pyxis
- Native support for Nvidia GPUs
- Faster Docker image imports

### Sarus

https://github.com/eth-cscs/sarus is a privileged container system sponsored by ETH Zurich https://user.cscs.ch/tools/containers/sarus/ that supports:

- https://sarus.readthedocs.io/en/latest/config/slurm-global-sync-hook.html
- Native OCI Image support
- NVIDIA GPU Support
- Similar design to Shifter

Overview slides of Sarus are http://hpcadvisorycouncil.com/events/2019/swiss-workshop/pdf/030419/K_Mariotti_CSCS_SARUS_OCI_ContainerRuntime_04032019.pdf.

------------------------------------------------------------------------
