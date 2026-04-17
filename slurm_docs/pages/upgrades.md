# Upgrade Guide

Slurm supports in-place upgrades between certain versions. This page provides important details about the steps necessary to perform an upgrade and the potential complications to prepare for.

See also [Quick Start Administrator Guide](quickstart_admin.md)

## Contents

- Release Cycle
  - Compatibility Window
  - EPEL Repository
  - Pre-Release Versions
- Reverting an Upgrade
- Minor Upgrades
- Upgrade Procedure
  - Preparation
  - Create Backups
  - slurmdbd (Accounting)
    - Database Server
  - slurmctld (Controller)
  - slurmd (Compute Nodes)
  - Other Slurm Commands
  - Customized Slurm Plugins
- Seamless Upgrades

## Release Cycle {#release_cycle}

The Slurm version number contains three period-separated numbers that represent both the major Slurm release and maintenance release level. For example, Slurm 23.11.4:

- **23.11** = major release
  - This matches the year and month of initial release (November 2023)
  - Major releases may contain changes to RPCs (remote procedure calls), state files, configuration options, and core functionality
- **.4** = maintenance version
  - Maintenance releases may contain bug fixes and performance improvements

Prior to the 24.05 release, Slurm operated on a 9-month release cycle for major versions. Slurm 24.05 represents the first release on the https://www.schedmd.com/slurm-releases-move-to-a-six-month-cycle/.

### Compatibility Window {#compatibility_window}

Slurm has long supported in-place upgrades from the previous two major releases. With the change to a 6-month cycle in 2024, Slurm 24.11 introduced compatibility with the **previous three major releases**. For example, slurmdbd 25.11.x is capable of accepting messages from slurmctld daemons and commands with a version of 25.11.x, 25.05.x, 24.11.x, or 24.05.x. It is also capable of updating the records in the database that were recorded by an instance of slurmdbd running these versions.

  ----------------------- ----------------------------- ------------------------------
  **Slurm Release**       **Revised End of Support**\   **Compatible Prior Version**
                          (total length)                

  23.11                   May 2025 (18 months)          23.02, 22.05

  24.05                   November 2025 (18 months)     23.11, 23.02

  24.11                   May 2026 (18 months)          24.05, 23.11, 23.02

  25.05                   November 2026 (18 months)     24.11, 24.05, 23.11

  25.11                   May 2027 (18 months)          25.05, 24.11, 24.05

  26.05                   November 2028 (18 months)     25.11, 25.05, 24.11
  ----------------------- ----------------------------- ------------------------------

\

Upgrades from incompatible versions will fail immediately upon startup. It is required to perform upgrades from incompatible prior versions in steps, going to newer versions compatible with the current running version. It may take several steps to upgrade to a current release of Slurm. For example, instead of upgrading directly from Slurm 20.11 to 23.11, first upgrade all systems to Slurm 22.05 and verify functionality, then proceed to upgrade to 23.11. This ensures that each upgrade performed is tested and can be supported by SchedMD. Compatibility requirements apply to running jobs and upgrading outside of their compatibility window will result in the jobs being killed and job accounting being lost.

### EPEL Repository {#epel_repository}

In the beginning of 2021, a version of Slurm was added to the EPEL repository. This version is not provided by or supported by SchedMD, and is not currently supported for customer use. Unfortunately, this inclusion could cause Slurm to be updated to a newer version outside of a planned maintenance period or result in conflicting packages. In order to prevent Slurm from being changed and broken unintentionally, we recommend you modify the EPEL Repository configuration to exclude all Slurm packages from automatic updates.

Add the following under the `[epel]` section of /etc/yum.repos.d/epel.repo:

    exclude=slurm*

### Pre-Release Versions {#prerelease}

When installing pre-release versions (e.g., 24.05.0rc1 or https://github.com/SchedMD/slurm), you should prepare for unexpected crashes, bugs, and loss of state information. SchedMD aims to use the NEWS file to indicate cases in which state information will be lost with pre-release versions. However, these pre-release versions receive **limited testing** and are not intended for production clusters. Sites are encouraged to actively run pre-release versions on test machines before each major release.

## Reverting an Upgrade {#revert}

Reverting an upgrade (or downgrading) is **not supported** once any of the Slurm daemons have been started. When starting up after an upgrade, the Slurm daemons (slurmctld, slurmdbd, and slurmd) will update their relevant state files and databases to the structure used in the new version. If you revert to an older version, the relevant Slurm daemon will not recognize the new state file or database, resulting in loss or corruption of state information or job accounting. The Slurm daemons will likely refuse to start unless configured to start with the risk of possible data loss.

By using recovery tools, like comprehensive file backups, disk images, and snapshots, it may be possible to revert components to the pre-upgrade state. In particular, restoring the contents of *StateSaveLocation* (as defined in *slurm.conf*) and (if configured) the accounting database will be required if you wish to revert an upgrade. Reverting an upgrade will wipe out anything that happened after the backups were created.

## Minor Upgrades {#minor_upgrades}

When upgrading to a newer minor maintenance release (as defined above), we recommend following the same upgrade procedure as with major releases. You will find that the process takes less time, and is more accommodating of mixed versions and in-place downgrades. However, you should always have current backups to solidify your recovery options.

## Upgrade Procedure {#procedure}

The upgrades procedure can be summarized as follows. Note the specific order in which the daemons should be upgraded:

1.  Prepare cluster for the upgrade
2.  Create backups
3.  Upgrade slurmdbd
4.  Upgrade slurmctld
5.  Upgrade slurmd (preferably with slurmctld)
6.  Upgrade login nodes and client commands
7.  Recompile/upgrade customized Slurm plugins
8.  Test key functionality
9.  Archive backup data

Before considering the upgrade complete, wait for all jobs that were already running to finish. Any jobs started before the **slurmd** system was upgraded will be running with the old version of **slurmstepd**, so starting another upgrade or trying to use new features in the new version may cause problems.

**NOTE**: If RPM/DEB packages are used, all packages present on each system must be upgraded together instead of piecewise. This is because the packages that contain Slurm daemons and client commands depend on the general **slurm** package. Avoid using low-level package managers like `rpm` or `dpkg` as they may not properly enforce these dependencies. After upgrading, daemons should be started in the order listed above.

### Preparation

#### RELEASE_NOTES and CHANGELOG {#release_notes}

Review relevant release notes in the **RELEASE_NOTES.md** file in root of Slurm source directory for the target release and any major versions between what you\'re currently running and the target you are upgrading to. Pay particular attention to any entries in which items are **removed** or **changed**. These are particularly likely to require specific attention or changes during the upgrade. Also look for changes in optional slurm components that you are using. You may also notice new items added to Slurm that you wish to start using after the upgrade.

Release notes for the latest major version are available [here](release_notes.md) or on GitHub (https://github.com/SchedMD/slurm/blob/master/RELEASE_NOTES.md). Release notes for other versions can be found in the source, which can be viewed on GitHub by selecting the branch or tag corresponding to the desired version. (Refer to https://github.com/SchedMD/slurm/blob/slurm-24.11/RELEASE_NOTES for Slurm 24.11 and older.) More detailed changes, including minor release changes, can be found in the **CHANGELOG** directory (formerly the NEWS file), but are usually not needed to prepare for upgrades.

#### Configuration Changes {#config_changes}

Always prepare and test configuration changes in a test environment before upgrading in production. Changes outlined in the release notes will need to be looked up in the man pages (such as [slurm.conf](slurm.conf.md) ) for details and new syntax. Certain options in your configuration files may need to be changed as features and functionality are improved in every major Slurm release. Typically, new naming and syntax conventions are introduced several versions before the old ones are removed, so you may be able to make the necessary changes before starting the upgrade process.

If **SlurmctldParameters=reconfig_on_restart** is enabled extra caution should be taken as the slurmd and sackd daemons could be upgraded earlier than anticipated. Temporarily disabling that option may be advisable.

#### Plan for Downtime {#downtime}

Refer to the expected downtime guidance in the following sections for each relevant Slurm daemon, particularly the slurmdbd. Notify affected users of the estimated downtime for the relevant services and the potential impact on their jobs. Whenever possible, try to plan upgrades during SchedMD\'s support hours. If you encounter an issue outside of these hours there will be a delay before assistance can be provided.

#### OpenAPI Changes {#openapi_changes}

Sites using `--json` or `--yaml` arguments with any CLI commands or running `slurmrestd` need to check for format compatibility and data_parser plugin removals before upgrading. The formats for the values parsed and dumped as JSON and YAML are handled by the data_parser plugins. Please see the following links for explanations of the changes in each release and how to account for them while upgrading:

- [OpenAPI Specification (OAS) changes](rest_clients.md#openapi-changes)
- [OpenAPI release notes](openapi_release_notes.md)

### Create Backups {#backups}

**Always** create full backups to restore all parts of Slurm, including the Mysql database, before upgrading in the event the upgrade must be reverted. SchedMD aims to make supported upgrades a seamless process but it is possible for unexpected issues to arise and **irreversibly corrupt** all of the data kept by Slurm. If something like this happens, it will not be possible to recover any corrupted data and you will be reliant on backed up data.

It is recommended to prepare recovery options (file backups, disk images, snapshots, database dumps) that will take you back to a known working cluster state. How backups are taken is specific to how the systems integrator designed and setup the cluster and procedures are not provided here.

At a minimum, back up the following:

- **StateSaveLocation** as defined in [slurm.conf](slurm.conf.md#OPT_StateSaveLocation), or it can be queried by calling

      scontrol show config | grep StateSaveLocation

- **Entire slurm configuration directory**, as defined by `configure --sysconfdir=DIR` during compilation. This is usually located in `/etc/slurm/`

- **MySQL database** (if slurmdbd is configured). Usually done by calling

      mysqldump --databases slurm_acct_db > /path/to/offline/storage/backup.sql

  This assumes that **slurmdbd** is not running while the dump is running.\
  If you wish to back it up while **slurmdbd** is running, you may use the `--single-transaction` flag with the **following limitations**:

  1.  Database operations may be slower while the dump is running
  2.  Restoring this dump will restore the database at the time the dump was **started**, losing any changes made during or after the dump
  3.  Certain cluster operations may lead to an incorrect or failed dump:
      - Creating a new database
      - Upgrading an existing database
      - Adding or Removing a cluster in the slurmdbd
      - [Archiving or Purging](accounting.md#slurmdbd-archive-purge) accounting data

### slurmdbd (Accounting) {#slurmdbd}

If **slurmdbd** is used in your environment, it must be at the same or higher major release number as the slurmctld daemon(s), and at a close enough version for compatibility. Thus, when performing upgrades, it should be upgraded first. When a backup slurmdbd host is in use, it should be upgraded at the same time as the primary.

Upgrades to the slurmdbd may require significant **downtime**. With large accounting databases, the precautionary database dump will take some time, and the upgraded daemon may be unresponsive for tens of minutes while it updates the database to the new schema. Sites are encouraged to use the [purge functionality](slurmdbd.conf.md#OPT_PurgeJobAfter) if older accounting data is not required for normal operations. Purging old records before attempting to upgrade can significantly decrease outage time.

The non-slurmdbd functionality of the cluster will continue to operate while the upgrade is in process, provided the activity does not fill up the slurmdbd Agent queue on the slurmctld node. While slurmdbd is offline, you should monitor the memory usage of slurmctld, and the **DBD Agent queue size**, as reported by **sdiag**, to ensure it does not exceed the configured **MaxDBDMsgs** in [slurm.conf](slurm.conf.md#OPT_MaxDBDMsgs). Cli commands [sacct](sacct.md) and [sacctmgr](sacctmgr.md) will not work while slurmdbd is down. `slurmrestd` queries that include slurmdb in the URL path will fail while slurmdbd is down.

It is preferred to create a backup of the database after shutting down the **slurmdbd** daemon, when the MySQL database is no longer changing. If you wish to take a backup with **mysqldump** while the slurmdbd is still running, you can add `--single-transaction` to the mysqldump command. Note that the slurmdbd will continue to execute operations that will not be contained in the dump, which may cause complications if you need to restore the database to this state.

The suggested upgrade procedure is as follows:

1.  Shutdown the slurmdbd daemon(s) gracefully:

        sacctmgr shutdown

    or via systemd:

        systemctl stop slurmdbd

    Wait until slurmdbd is fully down before proceeding or there may be data loss from data that was not fully saved.

        systemctl status slurmdbd

2.  Backup the Slurm database

3.  Verify that the innodb_buffer_pool_size in my.cnf is greater than the default. See the recommendation in the [accounting page](accounting.md#slurm-accounting-configuration-before-build).

4.  Upgrade the slurmdbd daemon binaries, libraries, and its systemd unit file (if used). If using [RPM/DEB packages](quickstart_admin.md#build_install), the package manager will take care of these, although systemd overrides may prevent the new unit from taking effect.\
    Only upgrade the slurmdbd system(s) at this time; other Slurm systems should remain on the old version.

5.  Start the primary slurmdbd daemon.\
    **NOTE**: If you typically use systemd, it is recommended to initially start the daemon directly as the configured SlurmUser:\
    `sudo -u slurm slurmdbd -D`\
    When the daemon starts up for the first time after upgrading, it will take some extra time to update existing records in the database. If it is started with systemd and reaches the configured timeout value, it may be killed prematurely potentially causing data loss. After it finishes starting up, you can use `Ctrl+C` to exit, then start it normally with systemd.

6.  Start the backup slurmdbd daemon (if applicable).

7.  Validate accounting operation, such as retrieving data through `sacct` or `sacctmgr`.

#### **Database Server** {#db_server}

When upgrading the database server that is used by slurmdbd (e.g., MySQL or MariaDB), usually no special procedures are required. It is recommended to use a database server that is supported by the publisher (or that was at the time when the chosen Slurm version was initially released). Database upgrades should be performed while the slurmdbd is stopped and according to the recommended procedure for the database used.

When upgrading an existing accounting database to **MariaDB 10.2.1** or later from an older version of MariaDB or any version of MySQL, ensure you are running **slurmdbd 22.05.7** or later. These versions will gracefully handle changes to MariaDB default values that can cause problems for slurmdbd.

### slurmctld (Controller) {#slurmctld}

It is preferred to upgrade the slurmctld system(s) at the same time as slurmd on the compute nodes and other Slurm commands on client machines and login nodes. The effects of downtime on slurmctld and slurmd daemons are largely the same, so upgrading them all together minimizes the total duration of these effects. Rolling upgrades are also possible if the slurmctld is upgraded first. When multiple slurmctld hosts are used, all should be upgraded simultaneously.

Upgrading the slurmctld involves a brief period of **downtime** during which job submissions are not accepted, queued jobs are not scheduled, and information about completing jobs is held. These functions will resume once the upgraded controller is started.

The recommended upgrade procedure is below, including optional steps for a simultaneous upgrade of slurmd systems:

1.  Increase configured SlurmdTimeout and SlurmctldTimeout values and execute `scontrol reconfig` for them to take effect.\
    The new timeout should be long enough to perform the upgrade using your preferred method. If the timeout is reached, nodes may be marked DOWN and their jobs killed.
2.  Shutdown the slurmctld daemon(s).
3.  (opt.) Shutdown the slurmd daemons on the compute nodes.
4.  Back up the contents of the configured StateSaveLocation.
5.  Upgrade the slurmctld (and optionally slurmd) daemons and their systemd service files (if used).
6.  (opt.) Restart the slurmd daemons on the compute nodes.
7.  Restart the slurmctld daemon(s).
8.  Validate proper operation, such as communication with nodes and a job\'s ability to successfully start and finish.
9.  Restore the preferred SlurmdTimeout and SlurmctldTimeout values and execute `scontrol reconfig` for them to take effect.

### slurmd (Compute Nodes) {#slurmd}

It is preferred to upgrade all slurmd nodes at the same time as the slurmctld. It is also possible to perform a rolling upgrade by upgrading the slurmd nodes later in any number of groups. Sites are encouraged to minimize the amount of time during which mixed versions are used in a cluster.

Upgrades will not interrupt running jobs as long as **SlurmdTimeout** is not reached during the process. However, while the slurmd is down for upgrades, new jobs will not be started and finishing jobs will wait to report back to the controller until it comes back online.

If you are upgrading the slurmd nodes separately from the controller, the following procedure can be followed:

1.  Increase the configured SlurmdTimeout value and execute `scontrol reconfig` for it to take effect.\
    The new timeout should be long enough to perform the upgrade using your preferred method. If the timeout is reached, nodes may be marked DOWN and their jobs killed.
2.  Shutdown the slurmd daemons on the compute nodes.
3.  Back up the contents of the configured StateSaveLocation.
4.  Upgrade the slurmd daemons and their systemd unit files (if used).
5.  Restart the slurmd daemons.
6.  Validate proper operation, such as communication with the controller and a job\'s ability to successfully start and finish.
7.  Repeat for any other groups of nodes that need to be upgraded.
8.  Restore the preferred SlurmdTimeout value and execute `scontrol reconfig` for it to take effect.

### Other Slurm Commands {#other_commands}

Other Slurm commands (including client commands) do not require special attention when upgrading, except where specifically noted in the release notes. You should also pay attention to any changes introduced in these additional components. After core Slurm components have been upgraded, upgrade additional components along with their systemd unit files (if used) and client commands using the normal method for your system, then restart any affected daemons.

### Customized Slurm Plugins {#custom_plugins}

Slurm\'s main public API library (libslurm.so.X.0.0) increases its version number with every major release, so any application linked against it should be recompiled after an upgrade. This includes locally developed Slurm plugins.

If you have built your own version of Slurm plugins, besides having to recompile them, they will likely need modification to support the new version of Slurm. It is common for plugins to add new functions and function arguments during major updates. See the RELEASE_NOTES file for details about these changes.

Slurm\'s PMI-1 (libpmi.so.0.0.0) and PMI-2 (libpmi2.so.0.0.0) public API libraries do not change between releases and are meant to be permanently fixed. This means that linking against either of them will not require you to recompile the application after a Slurm upgrade, except in the unlikely event that one of them changes. It is unlikely because these libraries must be compatible with any other PMI-1 and PMI-2 implementations. If there was a change, it would be announced in the RELEASE_NOTES and would only happen on a major release.

As an example, MPI stacks like OpenMPI and MVAPICH2 link against Slurm\'s PMI-1 and/or PMI-2 API, but not against our main public API. This means that at the time of writing this documentation, you don\'t need to recompile these stacks after a Slurm upgrade. One known exception is MPICH. When MPICH is compiled with Slurm support and with the Hydra Process Manager, it will use the Slurm API to obtain job information. This link means you will need to recompile the MPICH stack after an upgrade.

One easy way to know if an application requires a recompile is to inspect all of its ELF files with \'ldd\' and grep for \'slurm\'. If you see a versioned \'libslurm.so.x.y.z\' reference, then the application will likely need to be recompiled.

## Seamless Upgrades {#seamless_upgrades}

In environments where the Slurm build process is customized, it is possible to install a new version of Slurm to a unique directory and use a symbolic link to point the directory in your PATH to the version of Slurm you would like to use. This allows you to install the new version before you are in a maintenance period as well as easily switch between versions should you need to roll back for any reason. It also avoids potential problems with library conflicts that might arise from installing different versions to the same directory.
