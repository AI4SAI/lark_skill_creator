# \"Configless\" Slurm

\"Configless\" Slurm is a feature that allows the compute nodes --- specifically the slurmd process --- and user commands running on login nodes to pull configuration information directly from the slurmctld instead of from a pre-distributed local file. Your cluster does require a central set of configuration files on the Slurm controllers --- \"configless\" in Slurm\'s parlance means that the compute nodes, login nodes, and other cluster hosts do not need to be deployed with local copies of these files.

The slurmd on startup will reach out to a slurmctld that you specify and the config files will be pulled to the node. This slurmctld can be identified by either an explicit option, or --- preferably --- through DNS SRV records defined within the cluster itself.

If you have a [login node](quickstart_admin.md#login) you will be running client commands from, those client commands will have to use the DNS record to get the configuration information from the controller when they run. If you expect to have a lot of traffic from a login node, this can generate a lot of requests for the configuration files. In cases like this, [sackd](sackd.md) can be used to manage configuration files for the node reducing network requests.

## Installation {#INSTALLATION}

There are no extra steps required to install this feature. It is built in by default starting with Slurm 20.02.

## Setup {#SETUP}

The slurmctld must first be configured to run in the configless mode. This is handled by setting **SlurmctldParameters=enable_configless** in slurm.conf and restarting slurmctld.

Once enabled, you must configure the slurmd to get its configs from the slurmctld. This can be accomplished either by launching slurmd with the **\--conf-server** option, or by setting a DNS SRV record and ensuring there is no local configuration file on the compute node.

The **\--conf-server** options takes precedence over the DNS record.

The command line option takes \"\$host\[:\$port\]\", so an example would look like:

    slurmd --conf-server slurmctl-primary:6817

Specifying the port is optional and will default to 6817 if it is not present. Multiple slurmctlds can be specified as a comma-separated list, in priority order (highest to lowest).

    slurmd --conf-server slurmctl-primary:6817,slurmctl-secondary

The same information can be provided in a DNS SRV record. For example:

    _slurmctld._tcp 3600 IN SRV 10 0 6817 slurmctl-backup
    _slurmctld._tcp 3600 IN SRV 0 0 6817 slurmctl-primary

Will provide the required information to the slurmd on startup. As shown above, multiple SRV records can be specified if you have deployed Slurm in an HA setup. The DNS SRV entry with the lowest priority should be your primary slurmctld, with higher priority values for backup slurmctlds.

## Initial Testing {#INITIAL_TESTING}

With the slurmctld configured and slurmd started, you can check in a couple places to make sure the configs are present on the node. Config files will be in **SlurmdSpoolDir** under the **/conf-cache/**, and a symlink to this location will be created automatically in **/run/slurm/conf**. You can confirm that reloading is working by adding a comment to your slurm.conf on the slurmctld node and running [scontrol reconfig]{.commandline} and checking that the config was updated.

## Limitations {#LIMITATIONS}

Using \"%n\" in \"SlurmdSpoolDir\" or \"SlurmdPidFile\" will not be properly substituted for the NodeName unless slurmd is also launched with the \"-N\" option.

If you are using systemd to launch slurmd, you must ensure that \"ConditionPathExists=\*\" is not present in the unit file or the slurmd will not start. (The example slurmd.service file shipped in Slurm 20.02 and above does not include this entry.)

If any of the supported config files \"Include\" additional config files, the Included configs will **ONLY** be shipped if their \"Include\" filename reference has no path separators and the file is located adjacent to slurm.conf. Any additional config files will need to be shared a different way or added to the parent config.

If **Prolog**, **Epilog**, **TaskProlog**, and **TaskEpilog** scripts are specified in slurm.conf, the scripts will **ONLY** be shipped if the filenames referenced have no path separators and the file is located adjacent to slurm.conf.

## Notes {#NOTES}

Starting from Slurm 25.11, there\'s a new **SlurmctldParameters=reconfig_on_restart** option that will make every restart of slurmctld (process restart not triggered by \"scontrol reconfigure\") to trigger a reconfiguration request to all slurmd and sackd daemons. For \"configless\" systems this will ensure all processes are running the current configuration. Some caution should be taken if you intend to perform rolling upgrades on the cluster as this could lead to the daemons being upgraded sooner than expected.

The order of precedence for determining what configuration source to use is as follows:

1.  The slurmd \--conf-server \$host\[:\$port\] option
2.  The -f \$config_file option
3.  The SLURM_CONF environment variable (if set)
4.  A local slurm config file:
    1.  The default slurm config file (likely /etc/slurm.conf)
    2.  For user commands, a cached slurm config file (run/slurm/conf/slurm.conf)
5.  The SLURM_CONF_SERVER environment variable (if set)
6.  Any DNS SRV records (from lowest priority value to highest)
    - The TTL (Time To Live) of the SRV record does not affect the validity of the obtained configuration. The nodes will have to be notified of any changes to the configuration file through an [scontrol reconfig]{.commandline} or a slurmd restart.

Supported configuration files are:

- slurm.conf
- acct_gather.conf
- cgroup.conf
- cli_filter.lua
- gres.conf
- helpers.conf
- job_container.conf
- mpi.conf
- namespace.yaml
- oci.conf
- plugstack.conf
- scrun.lua
- topology.conf
- topology.yaml
