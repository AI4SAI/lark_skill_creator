# Workload Characterization Key (WCKey) Management

A WCKey is an orthogonal way to do accounting against possibly unrelated accounts. This can be useful where users from different accounts are all working on the same project.

## slurm(dbd).conf settings {#conf}

Including \"WCKey\" in your **AccountingStorageEnforce** option in your slurm.conf file will enforce WCKeys per job. This means only jobs with valid WCKeys (WCKeys previously added through sacctmgr) will be allowed to run.

If you wish to track the value of a jobs WCKey you must set the **TrackWCKey** option in both the slurm.conf as well as the slurmdbd.conf files. This will assure the WCKey is tracked on each job. If you set \"WCKey\" in your **AccountingStorageEnforce** line **TrackWCKey** is set automatically, it still needs to be added to your slurmdbd.conf file though.

## sbatch/salloc/srun {#submit}

Each submitting tool has the \--wckey= option that can set the WCKey for a job. \[SBATCH\|SALLOC\|SLURM\]\_WCKEY can also be set in the environment to set the WCKey. If no WCKey is given the WCKey for the job will be set to the users default WCKey for the cluster, which can be set up with sacctmgr. Also if no WCKey is specified the accounting record is appended with a \'\*\' to signify the WCKey was not specified. This is useful for a manager to determine if a user is specifying their WCKey or not.

## sacct

Sacct can be used to view the WCKey by adding \"wckey\" to the \--format option. You can also single out jobs by using the \--wckeys= option which would only send information about jobs that ran with specific WCKeys.

## sacctmgr

Sacctmgr is used to manage WCKeys. You can add and remove WCKeys from users or list them.

You add a user to a WCKey much like you do an account, only the WCKey doesn\'t need to be created before hand. i.e.

    sacctmgr add user da wckey=secret_project

You can remove them from a WCKey in the same fashion.

    sacctmgr del user da wckey=secret_project

To alter the users default WCKey you can run a line like

    sacctmgr mod user da cluster=snowflake set defaultwckey=secret_project

Which will change the default WCKey for user \"da\" on cluster \"snowflake\" to be \"secret_project\". If you want this for all clusters just remove the cluster= option.

## sreport

Information about reports available for WCKeys can be found on the [sreport manpage](sreport.md).
