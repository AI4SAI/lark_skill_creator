# Slurm Federated Scheduling Guide

- Overview
- Configuration
- Federated Job IDs
- Job Submission
- Job Scheduling
- Job Requeue
- Interactive Jobs
- Canceling Jobs
- Job Modification
- Job Arrays
- Status Commands
- Glossary
- Limitations

## Overview

Slurm includes support for creating a federation of clusters and scheduling jobs in a peer-to-peer fashion between them. Jobs submitted to a federation receive a unique job ID that is unique among all clusters in the federation. A job is submitted to the local cluster (the cluster defined in the slurm.conf) and is then replicated across the clusters in the federation. Each cluster then independently attempts to the schedule the job based off of its own scheduling policies. The clusters coordinate with the \"origin\" cluster (cluster the job was submitted to) to schedule the job.

**NOTE**: This is not intended as a high-throughput environment. If scheduling more than 50,000 jobs a day, consider configuring fewer clusters that the sibling jobs can be submitted to or directing load to the local cluster only (e.g. \--cluster-constraint= or -M submission options could be used to do this).

## Configuration

A federation is created using the sacctmgr command to create a federation in the database and by adding clusters to a federation.

\
To create a federation use:

    sacctmgr add federation <federation_name> [clusters=<list_of_clusters>]

Clusters can be added or removed from a federation using:\
**NOTE**: A cluster can only be a member of one federation at a time.

    sacctmgr modify federation <federation_name> set clusters[+-]=<list_of_clusters>
    sacctmgr modify cluster <cluster_name> set federation=<federation_name>
    sacctmgr modify federation <federation_name> set clusters=
    sacctmgr modify cluster <cluster_name> set federation=

**NOTE**: If a cluster is removed from a federation without first being drained, running jobs on the removed cluster, or that originated from the removed cluster, will continue to run as non-federated jobs. If a job is pending on the origin cluster, the job will remain pending on the origin cluster as a non-federated job and the remaining sibling jobs will be removed. If the origin cluster is being removed and the job is pending and is only viable on one cluster then it will remain pending on the viable cluster as a non-federated job. If the origin cluster is being removed and the job is pending and viable on multiple clusters other than the origin cluster, then the remaining pending jobs will remain pending as a federated job and the remaining sibling clusters will schedule amongst themselves to start the job.\
\
Federations can be deleted using:

    sacctmgr delete federation <federation_name>

Generic features can be assigned to clusters and can be requested at submission using the **\--cluster-constraint=\[!\]\<feature_list\>** option:

    sacctmgr modify cluster <cluster_name> set features[+-]=<feature_list>

A cluster\'s federated state can be set using:

    sacctmgr modify cluster <cluster_name> set fedstate=<state>

where possible states are:

- **ACTIVE:** Cluster will actively accept and schedule federated jobs
- **INACTIVE:** Cluster will not schedule or accept any jobs
- **DRAIN:** Cluster will not accept any new jobs and will let existing federated jobs complete
- **DRAIN+REMOVE:** Cluster will not accept any new jobs and will remove itself from the federation once all federated jobs have completed. When removed from the federation, the cluster will accept jobs as a non-federated cluster

Federation configuration can be viewed used using:

    sacctmgr show federation [tree]
    sacctmgr show cluster withfed

After clusters are added to a federation and the controllers are started their status can be viewed from the controller using:

    scontrol show federation

By default the status commands will show a local view. A default federated view can be set by configuring the following parameter in the slurm.conf:

    FederationParameters=fed_display

## Federated Job IDs {#jobids}

When a job is submitted to a federation it gets a federated job id. Job ids in the federation are unique across all clusters in the federation. A federated job ID is made by utilizing an unsigned 32 bit integer to assign the cluster\'s ID and the cluster\'s local ID.

    Bits 0-25:  Local Job ID
    Bits 26-31: Cluster Origin ID

Federated job IDs allow the controllers to know which cluster the job was submitted to by looking at the cluster origin id of the job.

## Job Submission {#jobsubmission}

When a federated cluster receives a job submission, it will submit copies of the job (**sibling jobs**) to each eligible cluster. Each cluster will then independently attempt to schedule the job.

Jobs can be directed to specific clusters in the federation using the **-M,\--clusters=\<cluster_list\>** and the new **\--cluster-constraint=\[!\]\<constraint_list\>** options.

Using the **-M,\--clusters=\<cluster_list\>** the submission command (sbatch, salloc, srun) will pick one cluster from the list of clusters to submit the job to and will also pass along the list of clusters with the job. The clusters in the list will be the only viable clusters that siblings jobs can be submitted to. For example the submission:

    cluster1$ sbatch -Mcluster2,cluster3 script.sh

will submit the job to either cluster2 or cluster3 and will only submit sibling jobs to cluster2 and cluster3 even if there are more clusters in the federation.

Using the **\--cluster-constraint=\[!\]\<constraint_list\>** option will submit sibling jobs to only the clusters that have the requested cluster feature(s) \-- or don\'t have the feature(s) if using **!**. Cluster features are added using the **sacctmgr modify cluster \<cluster_name\> set features\[+-\]=\<feature_list\>** option.

**NOTE**: When using the **!** option, add quotes around the option to prevent the shell from interpreting the **!** (e.g \--cluster-constraint=\'!highmem\').

When using both the **\--cluster-constraint=** and **\--clusters=** options together, the origin cluster will only submit sibling jobs to clusters that meet both requirements.

Held or dependent jobs are kept on the origin cluster until they are released or are no longer dependent, at which time they are submitted to other viable clusters in the federation. If a job becomes held or dependent after being submitted, the job is removed from every cluster but the origin.

## Job Scheduling {#jobscheduling}

Each cluster in the federation independently attempts to schedule each job with the exception of coordinating with the **origin cluster** (cluster where the job was submitted to) to allocate resources to a federated job. When a cluster determines it can attempt to allocate resources for a job it communicates with the origin cluster to verify that no other cluster is attempting to allocate resources at the same time. If no other cluster is attempting to allocate resources the cluster will attempt to allocate resources for the job. If it succeeds then it will notify the origin cluster that it started the job and the origin cluster will notify the clusters with sibling jobs to remove the sibling jobs and put them in a **revoked** state. If the cluster was unable to allocate resources to the job then it lets the origin cluster know so that other clusters can attempt to schedule the job. If it was the main scheduler attempting to allocate resources then the main scheduler will stop looking at further jobs in the job\'s partition. If it was the backfill scheduler attempting to allocate resources then the resources will be reserved for the job.

If an origin cluster is down, then the remote siblings will coordinate with a job\'s viable siblings to schedule the job. When the origin cluster comes back up, it will sync with the other siblings.

## Job Requeue {#jobrequeue}

When a federated job is requeued the origin cluster is notified and the origin cluster will then submit new sibling jobs to viable clusters and the federated job is eligible to start on a different cluster than the one it ran on.

slurm.conf options **RequeueExit** and **RequeueExitHold** are controlled by the origin cluster.

## Interactive Jobs {#interactivejobs}

Interactive jobs \-- jobs submitted with srun and salloc \-- can be submitted to the local cluster and get an allocation from a different cluster. When an salloc job allocation is granted by a cluster other than the local cluster, a new environment variable, SLURM_WORKING_CLUSTER, will be set with the remote sibling cluster\'s IP address, port and RPC version so that any sruns will know which cluster to communicate with.

**NOTE**: It is required that all compute nodes must be accessible to all submission hosts for this to work.\
**NOTE**: The current implementation of the MPI interfaces in Slurm require the SlurmdSpooldir to be the same on the host where the srun is being run as it is on the compute nodes in the allocation. If they aren\'t, a workaround is to get an allocation that puts the user on the actual compute node. Then the sruns on the compute nodes will be using the slurm.conf that corresponds to the correct cluster. Setting **LaunchParameters=use_interactive_step** slurm.conf will put the user on an actual compute node when using salloc.

## Canceling Jobs {#jobcancel}

Cancel requests in the federation will cancel the running sibling job or all pending sibling jobs. Specific pending sibling jobs can be removed by using **scancel**\'s **\--sibling=\<cluster_name\>** option to remove the sibling job from the job\'s active sibling list.

## Job Modification {#jobmodify}

Job modifications are routed to the origin cluster where the origin cluster will push out the changes to each sibling job.

## Job Arrays {#jobarrays}

Currently, job arrays only run on the origin cluster.

## Status Commands {#statuscmds}

By default, status commands, such as: squeue, sinfo, sprio, sacct, sreport, will show a view local to the local cluster. A unified view of the jobs in the federation can be viewed using the **\--federation** option to each status command. The **\--federation** command causes the status command to first check if the local cluster is part of a federation. If it is then the command will query each cluster in parallel for job info and will combine the information into one unified view.

A new **FederationParameters=fed_display** slurm.conf parameter has been added so that all status commands will present a federated view by default \-- equivalent to setting the **\--federation** option for each status command. The federated view can be overridden using the **\--local** option. Using the **\--clusters,-M** option will also override the federated view and give a local view for the given cluster(s).

Using the existing **\--clusters,-M option**, the status commands will output the information in the same format that exists today where each cluster\'s information is listed separately.

### squeue

squeue also has a new **\--sibling** option that will show each sibling job rather than merge them into one.

Several new long format options have been added to display the job\'s federated information:

- **cluster:** Name of the cluster that is running the job or job step.
- **siblingsactive:** Cluster names of where federated sibling jobs exist.
- **siblingsactiveraw:** Cluster IDs of where federated sibling jobs exist.
- **siblingsviable:** Cluster names of where federated sibling jobs are viable to run.
- **siblingsviableraw:** Cluster names of where federated sibling jobs are viable to run.

squeue output can be sorted using the **-S cluster** option.

### sinfo

sinfo will show the partitions from each cluster in one view. In a federated view, the cluster name is displayed with each partition. The cluster name can be specified in the format options using the short format **%V** or the long format **cluster** options. The output can be sorted by cluster names using the **-S %\[+-\]V** option.

### sprio

In a federated view, sprio displays the job information from the local cluster or from the first cluster to report the job. Since each sibling job could have a different priority on each cluster it may be helpful to use the **\--sibling** option to show all records of a job to get a better picture of a job\'s priority. The name of the cluster reporting the job record can be displayed using the **%c** format option. The cluster name is shown by default when using **\--sibling** option.

### sacct

By default, sacct will not display \"revoked\" jobs and will show the job from the cluster that ran the job. However, \"revoked\" jobs can be viewed using the **\--duplicate/-D** option.

### sreport

sreport will combine the reports from each cluster and display them as one.

### scontrol

The following scontrol options will display a federated view:

- show \[\--federation\|\--sibling\] jobs
- show \[\--federation\] steps
- completing

The following scontrol options are handled in a federation. If the command is run from a cluster other than the federated cluster it will be routed to the origin cluster.

- hold
- uhold
- release
- requeue
- requeuehold
- suspend
- update job

All other scontrol options should be directed to the specific cluster either by issuing the command on the cluster or using the **\--cluster/-M** option.

## Glossary

- **Federated Job:** A job that is submitted to the federated cluster. It has a unique job ID across all clusters (Origin Cluster ID + Local Job ID).
- **Sibling Job:** A copy of the federated job that is submitted to other federated clusters.
- **Local Cluster:** The cluster found in the slurm.conf that the commands will talk to by default.
- **Origin Cluster:** The cluster that the federated job was originally submitted to. The origin cluster submits sibling jobs to other clusters in the federation. The origin cluster determines whether a sibling job can run or not. Communications for the federated job are routed through the origin cluster.
- **Sibling Cluster:** The cluster that is associated with a sibling job.
- **Origin Job:** The federated job that resides on the cluster that it was originally submitted to.
- **Revoked (RV) State:** The state that the origin job is in while the origin job is not actively being scheduled on the origin cluster (e.g. not a viable sibling or one of the sibling jobs is running on a remote cluster). Or the state that a remote sibling job is put in when another sibling is allocated nodes.
- **Viable Sibling:** a cluster that is eligible to run a sibling job based off of the requested clusters, cluster features and state of the cluster (e.g. active, draining, etc.).
- **Active Sibling:** a sibling job that actively has a sibling job and is able to schedule the job.

## Limitations

- A federated job that fails due to resources (partition, node counts, etc.) on the local cluster will be rejected and won\'t be submitted to other sibling clusters even if it could run on them.
- Job arrays only run on the cluster that they were submitted to.
- Job modification must succeed on the origin cluster for the changes to be pushed to the sibling jobs on remote clusters.
- Modifications to anything other than jobs are disabled in sview.
- sview grid is disabled in a federated view.
