# Resource Limits

Familiarity with Slurm\'s [Accounting](accounting.md) web page is strongly recommended before use of this document.

## Hierarchy

Slurm\'s hierarchical limits are enforced in the following order with Job QOS and Partition QOS order being reversible by using the QOS flag \'OverPartQOS\':

1.  Partition QOS limit
2.  Job QOS limit
3.  User association
4.  Account association(s), ascending the hierarchy
5.  Root/Cluster association
6.  Partition limit
7.  None

Note: If limits are defined at multiple points in this hierarchy, the point in this list where the limit is first defined will be used. Consider the following example:

- MaxJobs=20 and MaxSubmitJobs is undefined in the partition QOS
- No limits are set in the job QOS and
- MaxJobs=4 and MaxSubmitJobs=50 in the user association

The limits in effect will be MaxJobs=20 and MaxSubmitJobs=50.

Note: The precedence order specified above is respected except for the following limits: Max\[Time\|Wall\], \[Min\|Max\]Nodes. For these limits, even if the job is enforced with QOS and/or Association limits, it can\'t go over the limit imposed at Partition level, even if it listed at the bottom. So the default for these 3 types of limits is that they are upper bound by the Partition one. This Partition level bound can be ignored if the respective QOS PartitionTimeLimit and/or Partition\[Max\|Min\]Nodes flags are set, then the job would be enforced the limits imposed at QOS and/or association level respecting the order above. **Grp\*** limits are also an exception. A more restrictive limit at the Account level will be enforced before a less restrictive limit at the User level. This is due to the nature of the limit being enforced, requiring that the limit at the highest level not be exceeded.

## Configuration {#config}

Scheduling policy information must be stored in a database as specified by the **AccountingStorageType** configuration parameter in the **slurm.conf** configuration file. Information can be recorded in a http://www.mysql.com/ or https://mariadb.org/ database. For security and performance reasons, the use of SlurmDBD (Slurm Database Daemon) as a front-end to the database is strongly recommended. SlurmDBD uses a Slurm authentication plugin (e.g. MUNGE). SlurmDBD also uses an existing Slurm accounting storage plugin to maximize code reuse. SlurmDBD uses data caching and prioritization of pending requests in order to optimize performance. While SlurmDBD relies upon existing Slurm plugins for authentication and database use, the other Slurm commands and daemons are not required on the host where SlurmDBD is installed. Only the *slurmdbd* and *slurm-plugins* RPMs are required for SlurmDBD execution.

Both accounting and scheduling policies are configured based upon an *association*. An *association* is a 4-tuple consisting of the cluster name, account, user and (optionally) the Slurm partition. In order to enforce scheduling policy, set the value of **AccountingStorageEnforce**. This option contains a comma separated list of options you may want to enforce. The valid options are:

- associations - This will prevent users from running jobs if their *association* is not in the database. This option will prevent users from accessing invalid accounts.
- limits - This will enforce limits set to associations. By setting this option, the \'associations\' option is also set.
- qos - This will require all jobs to specify (either overtly or by default) a valid qos (Quality of Service). QOS values are defined for each association in the database. By setting this option, the \'associations\' option is also set.
- safe - This will ensure a job will only be launched when using an association or qos that has a TRES-minutes limit set if the job will be able to run to completion. Without this option set, jobs will be launched as long as their usage hasn\'t reached the TRES-minutes limit which can lead to jobs being launched but then killed when the limit is reached. With the \'safe\' option set, a job won\'t be killed due to limits, even if the limits are changed after the job was started and the association or qos violates the updated limits. By setting this option, both the \'associations\' option and the \'limits\' option are set automatically.
- wckeys - This will prevent users from running jobs under a wckey that they don\'t have access to. By using this option, the \'associations\' option is also set. The \'TrackWCKey\' option is also set to true.

**NOTE**: The association is a combination of cluster, account, user names and optional partition name.\
Without AccountingStorageEnforce being set (the default behavior) jobs will be executed based upon policies configured in Slurm on each cluster.

## Tools

The tool used to manage accounting policy is *sacctmgr*. It can be used to create and delete cluster, user, account, and partition records plus their combined *association* record. See *man sacctmgr* for details on this tools and examples of its use.

Changes made to the scheduling policy are uploaded to the Slurm control daemons on the various clusters and take effect immediately. When an association is deleted, all running or pending jobs which belong to that association are immediately canceled. When limits are lowered, running jobs will not be canceled to satisfy the new limits, but the new lower limits will be enforced.

## Association specific limits and scheduling policies {#limits}

These represent the limits and scheduling policies relevant to Associations. When dealing with Associations, most of these limits are available not only for the user association, but also for each cluster and account. Limits and policies are applied in the following order:\
1. The option specified for the user association.\
2. The option specified for the account.\
3. The option specified for the cluster.\
4. If nothing is configured at the above levels, no limit will be applied.

These are just the limits and policies for Associations. For a more complete description of the columns available to be displayed, see the [sacctmgr](sacctmgr.md#SECTION_LIST/SHOW-ASSOCIATION-FORMAT-OPTIONS) man page.

**Fairshare**
:   Integer value used for determining priority. Essentially this is the amount of claim this association and its children have to the above system. Can also be the string \"parent\", when used on a user this means that the parent association is used for fairshare. If Fairshare=parent is set on an account, that account\'s children will be effectively re-parented for fairshare calculations to the first parent of their parent that is not Fairshare=parent. Limits remain the same, only its fairshare value is affected.

**GrpJobs**
:   The total number of jobs able to run at any given time from an association and its children. If this limit is reached, new jobs will be queued but only allowed to run after previous jobs complete from this group.

**GrpJobsAccrue**
:   The total number of pending jobs able to accrue age priority at any given time from an association and its children. If this limit is reached, new jobs will be queued but not accrue age priority until after previous jobs are removed from pending in this group. This limit does not determine if the job can run or not, it only limits the age factor of the priority.

**GrpSubmitJobs**
:   The total number of jobs able to be submitted to the system at any given time from an association and its children. If this limit is reached, new submission requests will be denied until previous jobs complete from this group.

**GrpTRES**
:   The total count of TRES able to be used at any given time from jobs running from an association and its children. If this limit is reached, new jobs will be queued but only allowed to run after resources have been relinquished from this group.

**GrpTRESMins**
:   The total number of TRES minutes that can possibly be used by past, present and future jobs running from an association and its children. If any limit is reached, all running jobs with that TRES in this group will be killed, and no new jobs will be allowed to run. This usage is decayed (at a rate of PriorityDecayHalfLife). It can also be reset (according to PriorityUsageResetPeriod) in order to allow jobs to run against the association tree. This limit only applies when using the Priority Multifactor plugin.

**GrpTRESRunMins**
:   Used to limit the combined total number of TRES minutes used by all jobs running with an association and its children. This takes into consideration time limit of running jobs and consumes it. If the limit is reached, no new jobs are started until other jobs finish to allow time to free up.

**GrpWall**
:   The maximum wall clock time running jobs are able to be allocated in aggregate for an association and its children. If this limit is reached, future jobs in this association will be queued until they are able to run inside the limit. This usage is decayed (at a rate of PriorityDecayHalfLife). It can also be reset (according to PriorityUsageResetPeriod) in order to allow jobs to run against the association tree again.

**MaxJobs**
:   The total number of jobs able to run at any given time for the given association. If this limit is reached, new jobs will be queued but only allowed to run after existing jobs in the association complete.

**MaxJobsAccrue**
:   The maximum number of pending jobs able to accrue age priority at any given time for the given association. If this limit is reached, new jobs will be queued but will not accrue age priority until after existing jobs in the association are moved from a pending state. This limit does not determine if the job can run, it only limits the age factor of the priority.

**MaxSubmitJobs**
:   The maximum number of jobs able to be submitted to the system at any given time from the given association. If this limit is reached, new submission requests will be denied until existing jobs in this association complete.

**MaxTRESMinsPerJob**
:   A limit of TRES minutes to be used by a job. If this limit is reached, the job will be killed if not running in Safe mode, otherwise the job will pend until enough time is given to complete the job.

**MaxTRESPerJob**
:   The maximum size in TRES any given job can have from the association.

**MaxTRESPerNode**
:   The maximum size in TRES each node in a job allocation can use.

**MaxWallDurationPerJob**
:   The maximum wall clock time any individual job can run for in the given association. If this limit is reached, the job will be denied at submission.

**MinPrioThreshold**
:   Minimum priority required to reserve resources in the given association. Used to override bf_min_prio_reserve. See [bf_min_prio_reserve](slurm.conf.md#OPT_bf_min_prio_reserve=#) for details.

**QOS**
:   comma separated list of QOSs an association is able to run.

**NOTE**: When modifying a TRES field with *sacctmgr*, one must specify which TRES to modify (see [TRES](tres.md) for complete list) as in the following examples:

    SET:
    sacctmgr modify user bob set GrpTRES=cpu=1500,mem=200,gres/gpu=50
    UNSET:
    sacctmgr modify user bob set GrpTRES=cpu=-1,mem=-1,gres/gpu=-1

## QOS specific limits and scheduling policies {#qos}

As noted above, the default behavior is that a limit set on a Partition QOS will be applied before a limit on the job\'s requested QOS. You can change this behavior with the *OverPartQOS* flag.

Unless noted, if a job request breaches a given limit on its own, the job will pend unless the job\'s QOS has the DenyOnLimit flag set, which will cause the job to be denied at submission. When Grp limits are considered with respect to this flag the Grp limit is treated as a Max limit.

**GraceTime**
:   Preemption grace time to be extended to a job which has been selected for preemption in the format of \<hh\>:\<mm\>:\<ss\>. The default value is zero, meaning no preemption grace time is allowed on this QOS. This value is only meaningful for QOS PreemptMode=CANCEL and PreemptMode=REQUEUE.

**GrpJobs**
:   The total number of jobs able to run at any given time from a QOS. If this limit is reached, new jobs will be queued but only allowed to run after previous jobs complete from this group.

**GrpJobsAccrue**
:   The total number of pending jobs able to accrue age priority at any given time from a QOS. If this limit is reached, new jobs will be queued but will not accrue age based priority until after previous jobs are removed from pending in this group. This limit does not determine if the job can run or not, it only limits the age factor of the priority. This limit only applies to the job\'s QOS and not the partition\'s QOS.

**GrpSubmitJobs**
:   The total number of jobs able to be submitted to the system at any given time from a QOS. If this limit is reached, new submission requests will be denied until previous jobs complete from this group.

**GrpTRES**
:   The total count of TRES able to be used at any given time from jobs running from a QOS. If this limit is reached, new jobs will be queued but only allowed to run after resources have been relinquished from this group.

**GrpTRESMins**
:   The total number of TRES minutes that can possibly be used by past, present and future jobs running from a QOS. If any limit is reached, all running jobs with that TRES in this group will be killed, and no new jobs will be allowed to run. This usage is decayed (at a rate of PriorityDecayHalfLife). It can also be reset (according to PriorityUsageResetPeriod) in order to allow jobs to run against the QOS again. QOS that have the NoDecay flag set do not decay GrpTRESMins, see [QOS Options](qos.md#qos_other) for details. This limit only applies when using the Priority Multifactor plugin.

**GrpTRESRunMins**
:   Used to limit the combined total number of TRES minutes used by all jobs running with a QOS. This takes into consideration the time limit of running jobs and consumes it. If the limit is reached, no new jobs are started until other jobs finish to allow time to free up.

**GrpWall**
:   The maximum wall clock time running jobs are able to be allocated in aggregate for a QOS. If this limit is reached, future jobs in this QOS will be queued until they are able to run inside the limit. This usage is decayed (at a rate of PriorityDecayHalfLife). It can also be reset (according to PriorityUsageResetPeriod) in order to allow jobs to run against the QOS again. QOS that have the NoDecay flag set do not decay GrpWall. See [QOS Options](qos.md#qos_other) for details.

**LimitFactor**
:   A float that is factored into an associations \[Grp\|Max\]TRES limits. For example, if the LimitFactor is 2, then an association with a GrpTRES of 30 CPUs would be allowed to allocate 60 CPUs when running under this QOS. **NOTE**: This factor is only applied to associations running in this QOS and is not applied to any limits in the QOS itself.

**MaxJobsAccruePerAccount**
:   The maximum number of pending jobs an account (or sub-account) can have accruing age priority at any given time. This limit does not determine if the job can run, it only limits the age factor of the priority.

**MaxJobsAccruePerUser**
:   The maximum number of pending jobs a user can have accruing age priority at any given time. This limit does not determine if the job can run, it only limits the age factor of the priority.

**MaxJobsPerAccount**
:   The maximum number of jobs an account (or sub-account) can have running at a given time.

**MaxJobsPerUser**
:   The maximum number of jobs a user can have running at a given time.

**MaxSubmitJobsPerAccount**
:   The maximum number of jobs an account (or sub-account) can have running and pending at a given time.

**MaxSubmitJobsPerUser**
:   The maximum number of jobs a user can have running and pending at a given time.

**MaxTRESMinsPerJob**
:   Maximum number of TRES minutes each job is able to use.

**MaxTRESPerAccount**
:   The maximum number of TRES an account can allocate at a given time.

**MaxTRESPerJob**
:   The maximum number of TRES each job is able to use.

**MaxTRESPerNode**
:   The maximum number of TRES each node in a job allocation can use.

**MaxTRESPerUser**
:   The maximum number of TRES a user can allocate at a given time.

**MaxWallDurationPerJob**
:   Maximum wall clock time each job is able to use. Format is \<min\> or \<min\>:\<sec\> or \<hr\>:\<min\>:\<sec\> or \<days\>-\<hr\>:\<min\>:\<sec\> or \<days\>-\<hr\>. The value is recorded in minutes with rounding as needed.

**MinPrioThreshold**
:   Minimum priority required to reserve resources when scheduling.

**MinTRESPerJob**
:   The minimum size in TRES any given job can have when using the requested QOS.

**UsageFactor**
:   A float that is factored into a job\'s TRES usage (e.g. RawUsage, TRESMins, TRESRunMins). For example, if the usagefactor was 2, for every TRESBillingUnit second a job ran it would count for 2. If the usagefactor was .5, every second would only count for half of the time. A setting of 0 would add no timed usage from the job. The usage factor only applies to the job\'s QOS and not the partition QOS.\
    If the UsageFactorSafe flag is set and AccountingStorageEnforce includes *Safe*, jobs will only be able to run if the job can run to completion with the UsageFactor applied, and won\'t be killed due to limits.\
    If the UsageFactorSafe flag is not set and AccountingStorageEnforce includes *Safe*, a job will be able to be scheduled without the UsageFactor applied and won\'t be killed due to limits.\
    If the UsageFactorSafe flag is not set and AccountingStorageEnforce does not include *Safe*, a job will be scheduled as long as the limits are not reached, but could be killed due to limits.\
    See [AccountingStorageEnforce](slurm.conf.md#OPT_AccountingStorageEnforce) in the slurm.conf man page.

The **MaxNodes** and **MaxTime** options already exist in Slurm\'s configuration on a per-partition basis, but the above options provide the ability to impose limits on a per-user basis. The **MaxJobs** option provides an entirely new mechanism for Slurm to control the workload any individual may place on a cluster in order to achieve some balance between users.

When assigning limits to a QOS to use for a Partition QOS, keep in mind that those limits are enforced at the QOS level, not individually for each partition. For example, if a QOS has a **GrpTRES=cpu=20** limit defined and the QOS is assigned to two unique partitions, users will be limited to 20 CPUs for the QOS rather than being allowed 20 CPUs for each partition.

Fair-share scheduling is based upon the hierarchical account data maintained in the Slurm database. More information can be found in the [priority/multifactor](priority_multifactor.md) plugin description.

### Specific limits over GRES {#gres_limits}

When a GRES has a type associated with it and a limit is applied over this specific type (e.g. *MaxTRESPerUser=gres/gpu:tesla=1*) if a user requests a generic gres, the type\'s limit will not be enforced. In this situation an additional lua job submit plugin to check the user request may become useful. For example, if one requests *\--gres=gpu:2* having a limit set of *MaxTRESPerUser=gres/gpu:tesla=1*, the limit won\'t be enforced so it will still be possible to get two teslas.

This is due to a design limitation. The only way to enforce such a limit is to combine the specification of the limit with a job submit plugin that forces the user to always request a specific type model.

An example of basic lua job submit plugin function could be:

    function slurm_job_submit(job_desc, part_list, submit_uid)
       gres_request = ""
       t = {job_desc.tres_per_job,
        job_desc.tres_per_socket,
        job_desc.tres_per_task,
        job_desc.tres_per_node}
       for k in pairs(t) do
        gres_request = gres_request .. t[k] .. ","
       end
       if (gres_request ~= nil)
       then
          for g in gres_request:gmatch("[^,]+")
          do
         bad = string.match(g,'^gres/gpu[:=]*[0-9]*$')
         if (bad ~= nil)
         then
            slurm.log_info("User specified gpu GRES without type: %s", bad)
            slurm.user_msg("You must always specify a type when requesting gpu GRES")
            return slurm.ERROR
         end
          end
       end
    end

Having this script and the limit in place will force the users to always specify a gpu with its type, thus enforcing the limits for each specific model.

When **TRESBillingWeights** are defined for a partition, both typed and non-typed resources should be included. For example, if you have \'tesla\' GPUs in one partition and you only define the billing weights for the \'tesla\' typed GPU resource, then those weights will not be applied to the generic GPUs.

It is also advisable to set **AccountingStorageTRES** for both generic and specific gres types, otherwise requests that ask for the generic instance of a gres won\'t be accounted for. For example, to track generic GPUs and Tesla GPUs, you would set this in your slurm.conf:

      AccountingStorageTRES=gres/gpu,gres/gpu:tesla

See [Trackable Resources TRES](tres.md) for details.

## Job Reason Codes {#reasons}

When a pending job is evaluated by the scheduler but found to exceed a configured resource limit, a corresponding reason will be assigned to the job. More details can be found on the [Job Reason Codes](job_reason_codes.md) page. More details about scheduling can be found in the [Scheduling Configuration Guide](sched_config.md).
