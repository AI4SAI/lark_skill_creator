# Quality of Service (QOS)

One can specify a Quality of Service (QOS) for each job submitted to Slurm. The QOSs are defined in the Slurm database using the *sacctmgr* command. Jobs request a QOS using the \"\--qos=\" option to the *sbatch*, *salloc*, and *srun* commands.

## Contents

- Effects on Jobs
  - [Scheduling Priority](#priority)
  - [Preemption](#preemption)
  - [Resource Limits](#limits)
- [Partition QOS](#partition)
- [Relative QOS](#relative)
- [Other QOS Options](#qos_other)
- [Configuration](#config)
- [Examples](#examples)

## Effects on Jobs {#effects}

The QOS associated with a job will affect the job in three key ways: scheduling priority, preemption, and resource limits.

### Job Scheduling Priority {#priority}

Job scheduling priority is made up of a number of factors as described in the [priority/multifactor](priority_multifactor.md) plugin. One of the factors is the QOS priority. Each QOS is defined in the Slurm database and includes an associated priority. Jobs that request and are permitted a QOS will incorporate the priority associated with that QOS in the job\'s [multi-factor priority calculation.](priority_multifactor.md#general)

To enable the QOS priority component of the multi-factor priority calculation, the \"PriorityWeightQOS\" configuration parameter must be defined in the slurm.conf file and assigned an integer value greater than zero.

A job\'s QOS only affects is scheduling priority when the multi-factor plugin is loaded.

### Job Preemption {#preemption}

Slurm offers two ways for a queued job to preempt a running job, free-up the running job\'s resources and allocate them to the queued job. See the [Preemption description](preempt.md) for details.

The preemption method is determined by the \"PreemptType\" configuration parameter defined in slurm.conf. When the \"PreemptType\" is set to \"preempt/qos\", a queued job\'s QOS will be used to determine whether it can preempt a running job. It is important to note that the QOS used to determine if a job is eligible for preemption is the QOS associated with the job and not a Partition QOS.

The QOS can be assigned (using *sacctmgr*) a list of other QOSs that it can preempt. When there is a queued job with a QOS that is allowed to preempt a running job of another QOS, the Slurm scheduler will preempt the running job.

The QOS option PreemptExemptTime specifies the minimum run time before the job is considered for preemption. The QOS option takes precedence over the global option of the same name. A Partition QOS with PreemptExemptTime takes precedence over a job QOS with PreemptExemptTime, unless the job QOS has the OverPartQOS flag enabled.

### Resource Limits {#limits}

Each QOS is assigned a set of limits which will be applied to the job. The limits mirror the limits imposed by the user/account/cluster/partition association defined in the Slurm database and described in the [Resource Limits page](resource_limits.md). When limits for a QOS have been defined, they will take precedence over the association\'s limits.

## Partition QOS {#partition}

A QOS can be attached to a partition. This means the partition will have all the same limits as the QOS. This does not associate jobs with the QOS, nor does it give the job any priority or preemption characteristics of the assigned QOS. Jobs may separately request the same QOS or a different QOS to gain those characteristics. However, the Partition QOS limits will override the job\'s QOS. If the opposite is desired you may configure the job\'s QOS with `Flags=OverPartQOS` which will reverse the order of precedence.

This functionality may be used to implement a true \"floating\" partition, in which a partition may access a limited amount of resources with no restrictions on which nodes it uses to get the resources. This is accomplished by assigning all nodes to the partition, then configuring a Partition QOS with `GrpTRES` set to the desired resource limits.

**NOTE**: Most QOS attributes are set using the **sacctmgr** command. However, setting a QOS as a partition QOS is accomplished in **slurm.conf** through the [QOS=](slurm.conf.md#OPT_QOS) option in the configuration of the associated partition. The QOS should be created using **sacctmgr** before it is assigned as a partition QOS. It is possible to delete a QOS attached to a partition without deleting the attachment in the **slurm.conf**. This is not recommended and could cause unintended behavior.

## Relative QOS {#relative}

Starting in Slurm 23.11, a QOS may be configured to contain relative resource limits instead of absolute limits by setting `Flags=Relative`. When this flag is set, all resource limits are treated as percentages of the total resources available. Values higher than 100 are interpreted as 100%. Memory limits should be set with no units. Although the default units (MB) will be displayed, the limits will be enforced as a percentage (1MB = 1%).

**NOTE**: When *Flags=Relative* is added to a QOS, **slurmctld** must be restarted or reconfigured for the flag to take effect.

Generally, the limits on a relative QOS will be calculated relative to the resources in the whole cluster. For example, `cpu=50` would be interpreted as 50% of all CPUs in the cluster.

However, when a relative QOS is also assigned as a partition QOS, some unique conditions will apply:

1.  Limits will be calculated relative to the partition\'s resources; for example, `cpu=50` would be interpreted as 50% of all CPUs in the associated partition.
2.  Only one partition may have this QOS as its partition QOS.
3.  Jobs will not be allowed to use it as a normal QOS.\
    **NOTE**: To avoid unexpected job submission errors, it is recommended not to add a relative partition QOS to any association-based entities.

## Other QOS Options {#qos_other}

**Flags** Used by the slurmctld to override or enforce certain characteristics. To clear a previously set value use the modify command with a new value of -1.\
Valid options are:

- **DenyOnLimit** If set, jobs using this QOS will be rejected at submission time if they do not conform to the QOS \'Max\' limits as stand-alone jobs. Jobs that go over these limits when other jobs are considered, but conform to the limits when considered individually will not be rejected. Instead they will pend until resources are available (as by default without DenyOnLimit). Group limits (e.g. **GrpTRES**) will also be treated like \'Max\' limits (e.g. **MaxTRESPerNode**) and jobs will be denied if they would violate the limit as stand-alone jobs. This currently only applies to QOS and Association limits.
- **EnforceUsageThreshold** If set, and the QOS also has a UsageThreshold, any jobs submitted with this QOS that fall below the UsageThreshold will be held until their Fairshare Usage goes above the Threshold.
- **NoDecay** If set, this QOS will not have its GrpTRESMins, GrpWall and UsageRaw decayed by the slurm.conf PriorityDecayHalfLife or PriorityUsageResetPeriod settings. This allows a QOS to provide aggregate limits that, once consumed, will not be replenished automatically. Such a QOS will act as a time-limited quota of resources for an association that has access to it. Account/user usage will still be decayed for associations using the QOS. The QOS GrpTRESMins and GrpWall limits can be increased or the QOS RawUsage value reset to 0 (zero) to again allow jobs submitted with this QOS to run (if pending with QOSGrp{TRES}MinutesLimit or QOSGrpWallLimit reasons, where {TRES} is some type of trackable resource).
- **NoReserve** If this flag is set and backfill scheduling is used, jobs using this QOS will not reserve resources in the backfill schedule\'s map of resources allocated through time. This flag is intended for use with a QOS that may be preempted by jobs associated with all other QOS (e.g use with a \"standby\" QOS). If this flag is used with a QOS which can not be preempted by all other QOS, it could result in starvation of larger jobs.
- **OverPartQOS** If set, jobs using this QOS will be able to override any limits used by the requested partition\'s QOS limits.
- **PartitionMaxNodes** If set, jobs using this QOS will be able to override the requested partition\'s MaxNodes limit.
- **PartitionMinNodes** If set, jobs using this QOS will be able to override the requested partition\'s MinNodes limit.
- **PartitionTimeLimit** If set, jobs using this QOS will be able to override the requested partition\'s TimeLimit.
- **Relative** If set, the QOS limits will be treated as percentages of the cluster or partition instead of absolute limits (numbers should be less than 100). The controller should be restarted or reconfigured after adding the *Relative* flag to the QOS.\
  If this is used as a partition QOS:
  1.  Limits will be calculated relative to the partition\'s resources.
  2.  Only one partition may have this QOS as its partition QOS.
  3.  Jobs will not be allowed to use it as a normal QOS.
- **RequiresReservation** If set, jobs using this QOS must designate a reservation when submitting a job. This option can be useful in restricting usage of a QOS that may have greater preemptive capability or additional resources to be allowed only within a reservation.
- **UsageFactorSafe** If set, and **AccountingStorageEnforce** includes **Safe**, jobs will only be able to run if the job can run to completion with the **UsageFactor** applied.

**GraceTime** Preemption grace time to be extended to a job which has been selected for preemption.

**UsageFactor** A float that is factored into a job\'s TRES usage (e.g. RawUsage, TRESMins, TRESRunMins). For example, if the usagefactor was 2, for every TRESBillingUnit second a job ran it would count for 2. If the usagefactor was .5, every second would only count for half of the time. A setting of 0 would add no timed usage from the job.

The usage factor only applies to the job\'s QOS and not the partition QOS.

If the **UsageFactorSafe** flag **is** set and **AccountingStorageEnforce** includes **Safe**, jobs will only be able to run if the job can run to completion with the **UsageFactor** applied.

If the **UsageFactorSafe** flag is **not** set and **AccountingStorageEnforce** includes **Safe**, a job will be able to be scheduled without the **UsageFactor** applied and will be able to run without being killed due to limits.

If the **UsageFactorSafe** flag is **not** set and **AccountingStorageEnforce** does not include **Safe**, a job will be able to be scheduled without the **UsageFactor** applied and could be killed due to limits.

See **AccountingStorageEnforce** in slurm.conf man page.

Default is 1. To clear a previously set value use the modify command with a new value of -1.

**UsageThreshold** A float representing the lowest fairshare of an association allowable to run a job. If an association falls below this threshold and has pending jobs or submits new jobs those jobs will be held until the usage goes back above the threshold. Use *sshare* to see current shares on the system.

## Configuration {#config}

To summarize the above, the QOSs and their associated limits are defined in the Slurm database using the *sacctmgr* utility. The QOS will only influence job scheduling priority when the multi-factor priority plugin is loaded and a non-zero \"PriorityWeightQOS\" has been defined in the slurm.conf file. The QOS will only determine job preemption when the \"PreemptType\" is defined as \"preempt/qos\" in the slurm.conf file. Limits defined for a QOS (and described above) will override the limits of the user/account/cluster/partition association.

## QOS examples {#examples}

QOS manipulation examples. All QOS operations are done using the sacctmgr command. The default output of \'sacctmgr show qos\' is very long given the large number of limits and options available so it is best to use the format option which filters the display.

By default when a cluster is added to the database a default qos named normal is created.

    $ sacctmgr show qos format=name,priority
          Name   Priority
    ---------- ----------
        normal          0

Add a new QOS

    $ sacctmgr add qos zebra
     Adding QOS(s)
      zebra
     Settings
      Description    = QOS Name

    $ sacctmgr show qos format=name,priority
          Name   Priority
    ---------- ----------
        normal          0
         zebra          0

Set QOS priority

    $ sacctmgr modify qos zebra set priority=10
     Modified qos...
      zebra

    $ sacctmgr show qos format=name,priority
          Name   Priority
    ---------- ----------
        normal          0
         zebra         10

Set some other limits

    $ sacctmgr modify qos zebra set GrpTRES=cpu=24
     Modified qos...
      zebra

    $ sacctmgr show qos format=name,priority,GrpTRES
          Name   Priority       GrpTRES
    ---------- ---------- -------------
        normal          0
         zebra         10        cpu=24

Add a QOS to a user account

    $ sacctmgr modify user crock set qos=zebra

    $ sacctmgr show assoc format=cluster,user,qos
       Cluster       User                  QOS
    ---------- ---------- --------------------
    canis_major                          normal
    canis_major      root                normal
    canis_major                          normal
    canis_major     crock                zebra

Users can belong to multiple QOSs

    $ sacctmgr modify user crock set qos+=alligator
    $ sacctmgr show assoc format=cluster,user,qos
       Cluster       User                  QOS
    ---------- ---------- --------------------
    canis_major                          normal
    canis_major      root                normal
    canis_major                          normal
    canis_major     crock       alligator,zebra

Finally, delete a QOS

    $ sacctmgr delete qos alligator
     Deleting QOS(s)...
      alligator
