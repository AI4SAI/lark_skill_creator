# Multi-Cluster Operation

A cluster is comprised of all the nodes managed by a single slurmctld daemon. Slurm offers the ability to target commands to other clusters instead of, or in addition to, the local cluster on which the command is invoked. When this behavior is enabled, users can submit jobs to one or many clusters and receive status from those remote clusters.

For example:

    juser@dawn> squeue -M dawn,dusk
    CLUSTER: dawn
    JOBID PARTITION   NAME   USER  ST   TIME NODES BP_LIST(REASON)
    76897    pdebug  myJob  juser   R   4:10   128 dawn001[8-15]
    76898    pdebug  myJob  juser   R   4:10   128 dawn001[16-23]
    16899    pdebug  myJob  juser   R   4:10   128 dawn001[24-31]

    CLUSTER: dusk
    JOBID PARTITION   NAME   USER  ST   TIME NODES BP_LIST(REASON)
    11950    pdebug   aJob  juser   R   4:20   128 dusk000[0-15]
    11949    pdebug   aJob  juser   R   5:01   128 dusk000[48-63]
    11946    pdebug   aJob  juser   R   6:35   128 dusk000[32-47]
    11945    pdebug   aJob  juser   R   6:36   128 dusk000[16-31]

Most of the Slurm client commands offer the \"-M, \--clusters=\" option which provides the ability to communicate to and from a comma separated list of clusters.

When **sbatch**, **salloc** or **srun** is invoked with a cluster list, Slurm will immediately submit the job to the cluster that offers the earliest start time subject its queue of pending and running jobs. Slurm will make no subsequent effort to migrate the job to a different cluster (from the list) whose resources become available when running jobs finish before their scheduled end times.

**NOTE**: In order for **salloc** or **srun** to work with the \"-M, \--clusters\" option in a multi-cluster environment, the compute nodes must be accessible to and from the submission host.

## Multi-Cluster Configuration {#multi_cluster}

The multi-cluster functionality requires the use of the SlurmDBD. The AccountingStorageType in the slurm.conf file must be set to the accounting_storage/slurmdbd plugin and the MUNGE or authentication keys must be installed to allow each cluster to communicate with the SlurmDBD. Note that MUNGE can be configured to use different keys for communications within a cluster and across clusters if desired. See [accounting](accounting.md) for details.

Once configured, Slurm commands specifying the \"-M, \--clusters=\" option will become active for all of the clusters listed by the **\"sacctmgr show clusters\"** command.

See also the [Slurm Federated Scheduling Guide](federation.html).
