# User Permissions

Slurm supports several special user permissions as described below.

## Operator

These users can add, modify, and remove any database object (user, account, etc), and add other operators. On a SlurmDBD served cluster, these users can

- View information that is blocked to regular uses by a PrivateData flag
- Create/Alter/Delete Reservations

Set using an **AdminLevel** option in the user\'s database record. For configuration information, see [Accounting and Resource Limits](accounting.md).

## Admin

These users have the same level of privileges as an operator in the database. They can also alter anything on a served slurmctld as if they were the SlurmUser or root.

An **AdminLevel** option in the user\'s database record. For configuration information, see [Accounting and Resource Limits](accounting.md).

## Coordinator {#coord}

A special privileged user, usually an account manager, that can add users or sub-accounts to the account they are coordinator over. This should be a trusted person since they can change limits on account and user associations, as well as cancel, requeue or reassign accounts of jobs inside their realm. Note that a coordinator may not increase job limits above the parent ones.

Set using a table in Slurm\'s database defining users and accounts for which they can serve as coordinators. For configuration information, see the [sacctmgr](sacctmgr.md) man page.
