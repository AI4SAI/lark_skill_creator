# Multifactor Priority Plugin

## Contents

- [Introduction](#intro)
- [Multifactor Job Priority Plugin](#mfjppintro)
- [Job Priority Factors In General](#general)
- [Age Factor](#age)
- [Association Factor](#assoc)
- [Job Size Factor](#jobsize)
- [Nice Factor](#nice)
- [Partition Factor](#partition)
- [Quality of Service (QOS) Factor](#qos)
- [Site Factor](#site)
- [TRES Factors](#tres)
- [Fairshare Factor](#fairshare)
- [The *sprio* utility](#sprio)
- [Configuration](#config)
- [Configuration Example](#configexample)

## Introduction {#intro}

By default, Slurm has the priority/multifactor plugin set, which schedules jobs based on several factors

In most cases it is preferable to use the Multifactor Priority plugin, however basic First In, First Out scheduling is available by setting *PriorityType=priority/basic* in the slurm.conf file. FIFO scheduling should be configured when Slurm is controlled by an external scheduler. (See Configuration below)

There are several considerations the scheduler makes when making scheduling decisions. Jobs are selected to be evaluated by the scheduler in the following order:

1.  Jobs that can preempt
2.  Jobs with an advanced reservation
3.  Partition PriorityTier
4.  Job priority
5.  Job submit time
6.  Job ID

This is important to keep in mind because the job with the highest priority may not be the first to be evaluated by the scheduler. The job priority is considered when there are multiple jobs that can be evaluated at once, such as jobs requesting partitions with the same PriorityTier.

## Multifactor \'Factors\' {#mfjppintro}

There are nine factors in the Multifactor Job Priority plugin that influence job priority:

Age
:   the length of time a job has been waiting in the queue, eligible to be scheduled

Association
:   a factor associated with each association

Fair-share
:   the difference between the portion of the computing resource that has been promised and the amount of resources that has been consumed

Job size
:   the number of nodes or CPUs a job is allocated

Nice
:   a factor that can be controlled by users to prioritize their own jobs.

Partition
:   a factor associated with each node partition

QOS
:   a factor associated with each Quality Of Service

Site
:   a factor dictated by an administrator or a site-developed job_submit or site_factor plugin

TRES
:   each TRES Type has its own factor for a job which represents the number of requested/allocated TRES Type in a given partition

Additionally, a weight can be assigned to each of the above factors. This provides the ability to enact a policy that blends a combination of any of the above factors in any portion desired. For example, a site could configure fair-share to be the dominant factor (say 70%), set the job size and the age factors to each contribute 15%, and set the partition and QOS influences to zero.

## Job Priority Factors In General {#general}

The job\'s priority at any given time will be a weighted sum of all the factors that have been enabled in the slurm.conf file. Job priority can be expressed as:

    Job_priority =
        site_factor +
        (PriorityWeightAge) * (age_factor) +
        (PriorityWeightAssoc) * (assoc_factor) +
        (PriorityWeightFairshare) * (fair-share_factor) +
        (PriorityWeightJobSize) * (job_size_factor) +
        (PriorityWeightPartition) * (priority_job_factor) +
        (PriorityWeightQOS) * (QOS_factor) +
        SUM(TRES_weight_cpu * TRES_factor_cpu,
            TRES_weight_<type> * TRES_factor_<type>,
            ...)
        - nice_factor

All of the factors in this formula are floating point numbers that range from 0.0 to 1.0. The weights are unsigned, 32 bit integers. The job\'s priority is an integer that ranges between 0 and 4294967295. The larger the number, the higher the job will be positioned in the queue, and the sooner the job will be scheduled. A job\'s priority, and hence its order in the queue, can vary over time. For example, the longer a job sits in the queue, the higher its priority will grow when the age_weight is non-zero.

The default behavior is for slurmctld to \"normalize\" the priority values in relation to the one with the highest value. This makes it so that the most priority a job can get from any factor is equal to the *PriorityWeight\** value for that factor. Using Partitions as an example, if \'PartitionA\' had a *PriorityJobFactor* of 20 and \'PartitionB\' had a *PriorityJobFactor* of 10 and the *PriorityWeightPartition* was set to 5000, then the calculation for the priority that any job would gain for the partition would look like this:

    # PartitionA
    5000 * (20 / 20) = 5000

    # PartitionB
    5000 * (10 / 20) = 2500

You can change the default behavior so that it doesn\'t normalize the priority values, but uses the raw *PriorityJobFactor* values instead, with *PriorityFlags=NO_NORMAL_PART*. In that case the calculation of the partition based priority would look like this:

    # PartitionA
    5000 * 20 = 100000

    # PartitionB
    5000 * 10 = 50000

See the other priority factors you can configure to not be normalized in the [PriorityFlags](slurm.conf.md#OPT_PriorityFlags) section of the documentation.

**IMPORTANT:** The weight values should be high enough to get a good set of significant digits since all the factors are floating point numbers from 0.0 to 1.0. For example, one job could have a fair-share factor of .59534 and another job could have a fair-share factor of .50002. If the fair-share weight is only set to 10, both jobs would have the same fair-share priority. Therefore, set the weights high enough to avoid this scenario, starting around 1000 or so for those factors you want to make predominant.

## Age Factor {#age}

**Note:** Computing the age factor requires the installation and operation of the [Slurm Accounting Database](accounting.md).

The age factor represents the length of time a job has been sitting in the queue and eligible to run. In general, the longer a job waits in the queue, the larger its age factor grows. However, the age factor for a dependent job will not change while it waits for the job it depends on to complete. Also, the age factor will not change when scheduling is withheld for a job whose node or time limits exceed the cluster\'s current limits.

At some configurable length of time (*PriorityMaxAge*), the age factor will max out to 1.0.

## Association Factor {#assoc}

Each association can be assigned an integer priority. The larger the number, the greater the job priority will be for jobs that request this association. This priority value is normalized to the highest priority of all the association to become the association factor.

## Job Size Factor {#jobsize}

The job size factor correlates to the number of nodes or CPUs the job has requested. This factor can be configured to favor larger jobs or smaller jobs based on the state of the *PriorityFavorSmall* boolean in the slurm.conf file. When *PriorityFavorSmall* is NO, the larger the job, the greater its job size factor will be. A job that requests all the nodes on the machine will get a job size factor of 1.0. When the *PriorityFavorSmall* Boolean is YES, the single node job will receive the 1.0 job size factor.

The *PriorityFlags* value of *SMALL_RELATIVE_TO_TIME* alters this behavior as follows. The job size in CPUs is divided by the time limit in minutes. The result is divided by the total number of CPUs in the system. Thus a full-system job with a time limit of one will receive a job size factor of 1.0, while a tiny job with a large time limit will receive a job size factor close to 0.0.

## Nice Factor {#nice}

Users can adjust the priority of their own jobs by setting the nice value on their jobs. Like the system nice, positive values negatively impact a job\'s priority and negative values increase a job\'s priority. Only privileged users can specify a negative value. The adjustment range is +/-2147483645.

## Partition Factor {#partition}

Each node partition can be assigned an integer priority. The larger the number, the greater the job priority will be for jobs that request to run in this partition. This priority value is then normalized to the highest priority of all the partitions to become the partition factor.

## Quality of Service (QOS) Factor {#qos}

Each QOS can be assigned an integer priority. The larger the number, the greater the job priority will be for jobs that request this QOS. This priority value is then normalized to the highest priority of all the QOSs to become the QOS factor.

## Site Factor {#site}

The site factor is a factor that can be set either using scontrol, through a [job_submit](job_submit_plugins.md) or [site_factor](site_factor.md) plugin. An example use case might be a job_submit plugin that sets a specific priority based on how many resources are requested.

## TRES Factors {#tres}

Each TRES Type has its own priority factor for a job which represents the amount of TRES Type requested/allocated in a given partition. For global TRES Types, such as Licenses and Burst Buffers, the factor represents the number of TRES Type requested/allocated in the whole system. The more a given TRES Type is requested/allocated on a job, the greater the job priority will be for that job.

## Fair-share Factor {#fairshare}

**Note:** Computing the fair-share factor requires the installation and operation of the [Slurm Accounting Database](accounting.md) to provide the assigned shares and the consumed, computing resources described below.

The fair-share component to a job\'s priority influences the order in which a user\'s queued jobs are scheduled to run based on the portion of the computing resources they have been allocated and the resources their jobs have already consumed. The fair-share factor does not involve a fixed allotment, whereby a user\'s access to a machine is cut off once that allotment is reached.

Instead, the fair-share factor serves to prioritize queued jobs such that those jobs charging accounts that are under-serviced are scheduled first, while jobs charging accounts that are over-serviced are scheduled when the machine would otherwise go idle.

Slurm\'s fair-share factor is a floating point number between 0.0 and 1.0 that reflects the shares of a computing resource that a user has been allocated and the amount of computing resources the user\'s jobs have consumed. The higher the value, the higher is the placement in the queue of jobs waiting to be scheduled.

By default, the computing resource is the computing cycles delivered by a machine in the units of allocated_cpus\*seconds. Other resources can be taken into account by configuring a partition\'s TRESBillingWeights option. The TRESBillingWeights option allows you to account for consumed resources other than just CPUs by assigning different billing weights to different Trackable Resources (TRES) such as CPUs, nodes, memory, licenses and generic resources (GRES). For example, when billing only for CPUs, if a job requests 1CPU and 64GB of memory on a 16CPU, 64GB node the job will only be billed for 1CPU when it really used the whole node.

By default, when TRESBillingWeights is configured, a job is billed for each individual TRES used. The billable TRES is calculated as the sum of all TRES types multiplied by their corresponding billing weight.

For example, the following jobs on a partition configured with TRESBillingWeights=CPU=1.0,Mem=0.25G and 16CPU, 64GB nodes would be billed as:

          CPUs       Mem GB
    Job1: (1 *1.0) + (60*0.25) = (1 + 15) = 16
    Job2: (16*1.0) + (1 *0.25) = (16+.25) = 16.25
    Job3: (16*1.0) + (60*0.25) = (16+ 15) = 31

Another method of calculating the billable TRES is by taking the MAX of the individual TRESs on a node (e.g. cpus, mem, gres) plus the SUM of the global TRESs (e.g. licenses). For example the above job\'s billable TRES would be calculated as:

              CPUs      Mem GB
    Job1: MAX((1 *1.0), (60*0.25)) = 15
    Job2: MAX((15*1.0), (1 *0.25)) = 15
    Job3: MAX((16*1.0), (64*0.25)) = 16

This method is turned on by defining the MAX_TRES priority flags in the slurm.conf.

You can also calculate the billable TRES by taking the MAX of the individual TRESs on a node (e.g. cpus, mem) plus the billable gres (GPU), plus the SUM of the global TRESs (e.g. licenses). This method is turned on by defining the MAX_TRES_GRES priority flags in the slurm.conf.

### \"Fair Tree\" Fairshare {#tree}

As of the 19.05 release, the \"Fair Tree\" fairshare algorithm has been made the default. Please see the [Fair Tree Fairshare](fair_tree.md) documentation for further details.

### \"Classic\" Fairshare {#classic}

As of the 19.05 release, the \"classic\" fairshare algorithm is no longer the default, and will only be used if *PriorityFlags=NO_FAIR_TREE* is explicitly configured. Documentation describing that algorithm has been moved to a separate [Classic Fairshare](classic_fair_share.md) documentation page.

## The *sprio* utility {#sprio}

The *sprio* command provides a summary of the six factors that comprise each job\'s scheduling priority. While *squeue* has format options (%p and %Q) that display a job\'s composite priority, sprio can be used to display a breakdown of the priority components for each job. In addition, the *sprio -w* option displays the weights (PriorityWeightAge, PriorityWeightFairshare, etc.) for each factor as it is currently configured.

## Configuration {#config}

The following slurm.conf parameters are used to configure the Multifactor Job Priority Plugin. See slurm.conf(5) man page for more details.

PriorityType
:   Set this value to \"priority/multifactor\" to enable the Multifactor Job Priority Plugin.

PriorityDecayHalfLife
:   This determines the contribution of historical usage on the composite usage value. The larger the number, the longer past usage affects fair-share. If set to 0 no decay will be applied. This is helpful if you want to enforce hard time limits per association. If set to 0 PriorityUsageResetPeriod must be set to some interval. The unit is a time string (i.e. min, hr:min:00, days-hr:min:00, or days-hr). The default value is 7-0 (7 days).

PriorityCalcPeriod
:   The period of time in minutes in which the half-life decay will be re-calculated. The default value is 5 (minutes).

PriorityUsageResetPeriod
:   At this interval the usage of associations will be reset to 0. This is used if you want to enforce hard limits of time usage per association. If PriorityDecayHalfLife is set to be 0 no decay will happen and this is the only way to reset the usage accumulated by running jobs. By default this is turned off and it is advised to use the PriorityDecayHalfLife option to avoid not having anything running on your cluster, but if your schema is set up to only allow certain amounts of time on your system this is the way to do it. Applicable only if PriorityType=priority/multifactor. The unit is a time string (i.e. NONE, NOW, DAILY, WEEKLY). The default is NONE.
    - NONE: Never clear historic usage. The default value.
    - NOW: Clear the historic usage now. Executed at startup and reconfiguration time.
    - DAILY: Cleared every day at midnight.
    - WEEKLY: Cleared every week on Sunday at time 00:00.
    - MONTHLY: Cleared on the first day of each month at time 00:00.
    - QUARTERLY: Cleared on the first day of each quarter at time 00:00.
    - YEARLY: Cleared on the first day of each year at time 00:00.

PriorityFavorSmall
:   A boolean that sets the polarity of the job size factor. The default setting is NO which results in larger node sizes having a larger job size factor. Setting this parameter to YES means that the smaller the job, the greater the job size factor will be.

PriorityMaxAge
:   Specifies the queue wait time at which the age factor maxes out. The unit is a time string (i.e. min, hr:min:00, days-hr:min:00, or days-hr). The default value is 7-0 (7 days).

PriorityWeightAge
:   An unsigned integer that scales the contribution of the age factor.

PriorityWeightAssoc
:   An unsigned integer that scales the contribution of the association factor.

PriorityWeightFairshare
:   An unsigned integer that scales the contribution of the fair-share factor.

PriorityWeightJobSize
:   An unsigned integer that scales the contribution of the job size factor.

PriorityWeightPartition
:   An unsigned integer that scales the contribution of the partition factor.

PriorityWeightQOS
:   An unsigned integer that scales the contribution of the quality of service factor.

PriorityWeightTRES
:   A list of TRES Types and weights that scales the contribution of each TRES Type\'s factor.

PriorityFlags
:   Flags to modify priority behavior. Applicable only if PriorityType=priority/multifactor.
    - ACCRUE_ALWAYS: If set, priority age factor will be increased despite job dependencies or holds. Accrue limits are ignored.
    - CALCULATE_RUNNING: If set, priorities will be recalculated not only for pending jobs, but also running and suspended jobs.
    - DEPTH_OBLIVIOUS: If set, priority will be calculated based similar to the normal multifactor calculation, but depth of the associations in the tree do not adversely effect their priority. This option automatically enables NO_FAIR_TREE.
    - NO_FAIR_TREE: Disables the \"fair tree\" algorithm, and reverts to \"classic\" fair share priority scheduling.
    - INCR_ONLY: If set, priority values will only increase in value. Job priority will never decrease in value.
    - MAX_TRES: If set, the weighted TRES value (e.g. TRESBillingWeights) is calculated as the MAX of individual TRESs on a node (e.g. cpus, mem, gres) plus the sum of all global TRESs (e.g. licenses).
    - NO_NORMAL_ALL: If set, all NO_NORMAL\_\* flags are set.
    - NO_NORMAL_ASSOC: If set, the association factor is not normalized against the highest association priority.
    - NO_NORMAL_PART: If set, the partition factor is not normalized against the highest partition PriorityJobFactor.
    - NO_NORMAL_QOS: If set, the QOS factor is not normalized against the highest qos priority.
    - NO_NORMAL_TRES: If set, the TRES factor is not normalized against the job\'s partition TRES counts.
    - SMALL_RELATIVE_TO_TIME: If set, the job\'s size component will be based upon not the job size alone, but the job\'s size divided by its time limit.

**NOTE**: As stated above, the six priority factors range from 0.0 to 1.0. As such, the PriorityWeight terms may need to be set to a high enough value (say, 1000) to resolve very tiny differences in priority factors. This is especially true with the fair-share factor, where two jobs may differ in priority by as little as .001 (or less).

## Configuration Example {#configexample}

The following are sample slurm.conf file settings for the Multifactor Job Priority Plugin.

The first example is for running the plugin applying decay over time to reduce usage. Hard limits can be used in this configuration, but will have less effect since usage will decay over time instead of having no decay over time.

    # Activate the Multifactor Job Priority Plugin with decay
    PriorityType=priority/multifactor

    # 2 week half-life
    PriorityDecayHalfLife=14-0

    # The larger the job, the greater its job size priority.
    PriorityFavorSmall=NO

    # The job's age factor reaches 1.0 after waiting in the
    # queue for 2 weeks.
    PriorityMaxAge=14-0

    # This next group determines the weighting of each of the
    # components of the Multifactor Job Priority Plugin.
    # The default value for each of the following is 1.
    PriorityWeightAge=1000
    PriorityWeightFairshare=10000
    PriorityWeightJobSize=1000
    PriorityWeightPartition=1000
    PriorityWeightQOS=0 # don't use the qos factor

This example is for running the plugin with no decay on usage, thus making a reset of usage necessary.

    # Activate the Multifactor Job Priority Plugin with decay
    PriorityType=priority/multifactor

    # apply no decay
    PriorityDecayHalfLife=0

    # reset usage after 1 month
    PriorityUsageResetPeriod=MONTHLY

    # The larger the job, the greater its job size priority.
    PriorityFavorSmall=NO

    # The job's age factor reaches 1.0 after waiting in the
    # queue for 2 weeks.
    PriorityMaxAge=14-0

    # This next group determines the weighting of each of the
    # components of the Multifactor Job Priority Plugin.
    # The default value for each of the following is 1.
    PriorityWeightAge=1000
    PriorityWeightFairshare=10000
    PriorityWeightJobSize=1000
    PriorityWeightPartition=1000
    PriorityWeightQOS=0 # don't use the qos factor
