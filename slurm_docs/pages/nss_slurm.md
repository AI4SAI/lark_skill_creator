# nss_slurm

nss_slurm is an optional NSS plugin that can permit passwd, group and cloud node host resolution for a job on the compute node to be serviced through the local slurmstepd process, rather than through some alternate network-based service such as LDAP, DNS, SSSD, or NSLCD.

When enabled on the cluster, for each job, the job\'s user will have their full **struct passwd** info --- username, uid, primary gid, gecos info, home directory, and shell --- securely sent as part of each step launch, and cached within the slurmstepd process. This info will then be provided to any process launched by that step through the **getpwuid()**/**getpwnam()**/**getpwent()** system calls.

For group information --- from the **getgrgid()**/**getgrnam()**/**getgrent()** system calls ---, an abbreviated view of **struct group** will be provided. Within a given process, the response will include only those groups that the user belongs to, but with only the user themselves listed as a member. The full list of group members is not provided.

For host information --- from the **gethostbyname()**/**gethostbyname** system calls ---, an abbreviated view of **struct hostent** will be provided. Within a given process, the response will include only the cloud hosts that belong to allocation.

All of this information is populated by slurmctld as it is seen on the host running slurmctld.

## Installation {#INSTALLATION}

### Source:

In your Slurm build directory, navigate to **contribs/nss_slurm/** and run:

    make && make install

This will install libnss_slurm.so.2 alongside your other Slurm library files in your install path.

Depending on your Linux distribution, you will likely need to symlink this to the directory which includes your other NSS plugins to enable it. On Debian/Ubuntu, [/lib/x86_64-linux-gnu]{.commandline} is recommended, and for RHEL-based distributions [/usr/lib64]{.commandline} is recommended. If in doubt, a command such as [find /lib /usr/ -name \'libnss\*\']{.commandline} should help.

## Setup {#SETUP}

The slurmctld must be configured to look up and send the appropriate passwd and group details as part of the launch credential. This is handled by setting **LaunchParameters=enable_nss_slurm** in slurm.conf and restarting slurmctld.

Once enabled, the [scontrol getent]{.commandline} command can be used on a compute node to print all passwd and group info associated with job steps on that node. As an example:

    tim@node0001:~$ scontrol getent node0001
    JobId=1268.Extern:
    User:
    tim:x:1000:1000:Tim Wickberg:/home/tim:/bin/bash
    Groups:
    tim:x:1000:tim
    projecta:x:1001:tim

    JobId=1268.0:
    User:
    tim:x:1000:1000:Tim Wickberg:/home/tim:/bin/bash
    Groups:
    tim:x:1000:tim
    projecta:x:1001:tim

## NSS Slurm Configuration {#NSS_SLURM_CONFIG}

nss_slurm has an optional configuration file --- **/etc/nss_slurm.conf**. This configuration file is only needed if:

- The node\'s hostname does not match the NodeName, in which case you must explicitly set the NodeName option.
- The SlurmdSpoolDir does not match Slurm\'s default location of **/var/spool/slurmd**, in which case it must be provided as well.

NodeName and SlurmdSpoolDir are the only configuration options supported at this time.

## Initial Testing {#INITIAL_TESTING}

Before enabling NSS Slurm directly on the node, you should use the **-s slurm** option to **getent** within a newly launched job step to verify that the rest of the setup has been completed successfully. The **-s** option to getent allows it to query a specific database --- even if it has not been enabled by default through the system\'s **nsswitch.conf**. Note that nss_slurm only responds to requests from processes within the job step itself --- you must launch the getent command within a job step to see any data returned.

As an example of a successful query:

    tim@blackhole:~$ srun getent -s slurm passwd
    tim:x:1000:1000:Tim Wickberg:/home/tim:/bin/bash
    tim@blackhole:~$ srun getent -s slurm group
    tim:x:1000:tim
    projecta:x:1001:tim

## NSS Configuration {#NSS_CONFIG}

Enabling nss_slurm is as simple as adding **slurm** to the passwd and group database in **/etc/nsswitch.conf** (only on systems that will run **slurmd**). It is recommended that **slurm** is listed first, as the order (from left to right) determines the sequence in which the NSS databases will be queried, and this ensures Slurm handles the request if able before submitting the query to other sources.

To enable cloud node name resolution **slurm** needs to be added to the to hosts database in **/etc/nsswitch.conf**. It is recommended that **slurm** is listed last.

Once enabled, test it by launching **getent** queries such as:

    tim@blackhole:~$ srun getent passwd tim
    tim:x:1000:1000:Tim Wickberg:/home/tim:/bin/bash
    tim@blackhole:~$ srun getent group projecta
    projecta:x:1001:tim

## Limitations {#LIMITATIONS}

nss_slurm will only return results for processes within a given job step. It will not return any results for processes outside of these steps, such as system monitoring, node health checks, prolog or epilog scripts, and related node system processes.

nss_slurm is not meant as a full replacement for network directory services such as LDAP, but as a way to remove load from those systems to improve the performance of large-scale job launches. It accomplishes this by removing the \"thundering-herd\" issue should all tasks of a large job make simultaneous lookup requests --- generally for info related to the user themselves, which is the only information nss_slurm will be able to provide --- and overwhelm the underlying directory services.

nss_slurm is only able to communicate with a single slurmd. If running with \--enable-multiple-slurmd, you can specify which slurmd is used with NodeName and SlurmdSpoolDir parameters in the **nss_slurm.conf** file.

Since the information is gathered from the slurmctld node, there can be unexpected consequences if the information differs between the controller and the worker nodes. One possible scenario is if a user\'s shell is /sbin/nologin on the slurmctld machine but /bin/bash on the slurmd node. An interactive salloc may fail to launch since it will try to spawn the default shell, which according to the slurmctld is /sbin/nologin.

When using proctrack/pgid, nss_slurm will rely on the pgid of the process to determine if it can respond to that request. The login shell spawned with [srun \--pty]{.commandline} must be run in its own session, and therefore its own pgid, so nss_slurm will not respond to requests in an interactive session.
