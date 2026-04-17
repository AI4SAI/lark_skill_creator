# sshare

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

sshare - Tool for listing the shares of associations to a cluster.

[ ]{#lbAC}

## SYNOPSIS

**sshare** \[*OPTIONS*\...\]

[ ]{#lbAD}

## DESCRIPTION

**sshare** is used to view Slurm share information. This command is only viable when running with the priority/multifactor plugin. The sshare information is derived from a database with the interface being provided by **slurmdbd** (Slurm Database daemon) which is read in from the slurmctld and used to process the shares available to a given association. sshare provides Slurm share information of Account, User, Raw Shares, Normalized Shares, Raw Usage, Normalized Usage, Effective Usage, the Fair-share factor, the GrpTRESMins limit, Partitions and accumulated currently running TRES-minutes for each association.

[ ]{#lbAE}

## OPTIONS

**-A**, **\--accounts**=\<*account*\>
:   Display information for specific accounts (comma separated list).

:   

**-a**, **\--all**
:   Display information for all users.

:   

**-M**, **\--clusters**=\<*string*\>
:   Clusters to issue commands to. Note that the **slurmdbd** must be up for this option to work properly, unless running in a federation with **FederationParameters=fed_display** configured.

:   

**-o**, **\--format**=\<*output_format*\>
:   Comma separated list of fields (use \"\--helpformat\" for a list of available fields).

:   

**\--help**
:   Display a description of sshare options and commands.

:   

**-l**, **\--long**
:   Long listing - includes the normalized usage information.

:   

**\--json**, **\--json**=*list*, **\--json**=\<*data_parser*\>
:   Dump information as JSON using the default data_parser plugin or explicit data_parser with parameters. Sorting and formatting arguments will be ignored.

:   

**-n**, **\--noheader**
:   No header will be added to the beginning of the output.

:   

**-p**, **\--parsable**
:   Output will be \'\|\' delimited with a \'\|\' at the end.

:   

**-P**, **\--parsable2**
:   Output will be \'\|\' delimited without a \'\|\' at the end.

:   

**-m**, **\--partition**
:   If there are association based partitions in the system print their names.

:   

**\--usage**
:   Display a description of sshare options and commands.

:   

**-u**, **\--users**=\<*user_list*\>
:   Display information for specific users (comma separated list).

:   

**-U**, **\--Users**
:   If specified only the users information are printed, the parent and ancestors are not displayed.

:   

**-v**, **\--verbose**
:   Display more information about the specified options.

:   

**-V**, **\--version**
:   Display the version number of sshare.

:   

**\--yaml**, **\--yaml**=*list*, **\--yaml**=\<*data_parser*\>
:   Dump information as YAML using the default data_parser plugin or explicit data_parser with parameters. Sorting and formatting arguments will be ignored.

:   

[ ]{#lbAF}

## SSHARE OUTPUT FIELDS

**Account**
:   The Account.

:   

**User**
:   The User.

:   

**Raw Shares**
:   The raw shares assigned to the user or account.

:   

**Norm Shares**
:   The shares assigned to the user or account normalized to the total number of assigned shares.

:   

**Raw Usage**
:   The number of tres-seconds (cpu-seconds if TRESBillingWeights is not defined) of all the jobs charged to the account or user. This number will decay over time when PriorityDecayHalfLife is defined.

:   

**Norm Usage** (only appears with **sshare -l** option)
:   The Raw Usage normalized to the total number of tres-seconds of all jobs run on the cluster, subject to the PriorityDecayHalfLife decay when defined.

:   

**Effectv Usage**
:   The Effective Usage augments the normalized usage to account for usage from sibling accounts.

:   

**FairShare**
:   The Fair-Share factor, based on a user\'s assigned shares and the effective usage charged to them.

:   

**GrpTRESMins**
:   The TRES-minutes limit set on the account. The total number of cpu minutes that can possibly be used by past, present and future jobs running from this account and its children.

:   

**GrpTRESRaw**
:   The raw TRES usage that has been used by jobs running from this account and its children.

:   

**TRESRunMins**
:   The number of TRES-minutes allocated by jobs currently running against the account. Used to limit the combined total number of TRES minutes used by all jobs running with this account and its children. This takes into consideration time limit of running jobs and consumes it, if the limit is reached no new jobs are started until other jobs finish to allow time to free up.

:   

[ ]{#lbAG}

## FAIR_TREE MODIFICATIONS

When PriorityFlags=FAIR_TREE is set (the default, unless NO_FAIR_TREE is set), calculations are done differently. As a result, the following fields are added or modified:

**Norm Shares**
:   The shares assigned to the user or account normalized to the total number of assigned shares within the level.

:   

**Effectv Usage**
:   Effectv Usage is the association\'s usage normalized with its parent.

:   

**Level FS** (only appears with **sshare -l** option)
:   This is the association\'s fairshare value compared to its siblings, calculated as Norm Shares / Effectv Usage. If an association is over-served, the value is between 0 and 1. If an association is under-served, the value is greater than 1. Associations with no usage receive the highest possible value, infinity.

:   

More information about Fair Tree can be found in doc/html/fair_tree.html or at [https://slurm.schedmd.com/fair_tree.html](fair_tree.md)

[ ]{#lbAH}

## PERFORMANCE

Executing **sshare** sends a remote procedure call to **slurmctld**. If enough calls from **sshare** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **sshare** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **sshare** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAI}

## ENVIRONMENT VARIABLES

Some **sshare** options may be set via environment variables. These environment variables, along with their corresponding options, are listed below. (Note: Command line options will always override these settings.)

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for sshare to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

**SLURM_JSON**
:   Control JSON serialization:

:   

    :   

        **compact**
        :   Output JSON as compact as possible.

        :   

        **pretty**
        :   Output JSON in pretty format to make it more readable.

        :   

**SLURM_YAML**
:   Control YAML serialization:

:   

    :   

        **compact** Output YAML as compact as possible.

        :   

        :   

        **pretty** Output YAML in pretty format to make it more readable.

        :   

:   

[ ]{#lbAJ}

## EXAMPLES

Display information about users in a particular account:

:   

:   $ sshare -A <Account>

Display information about a specific user in a parsable format:

:   

:   $ sshare --parsable --users=<User>

[ ]{#lbAK}

## COPYING

Copyright (C) 2008 Lawrence Livermore National Security. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAL}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[slurmdbd](slurmdbd.md)**(8)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

SYNOPSIS

:   

DESCRIPTION

:   

OPTIONS

:   

SSHARE OUTPUT FIELDS

:   

FAIR_TREE MODIFICATIONS

:   

PERFORMANCE

:   

ENVIRONMENT VARIABLES

:   

EXAMPLES

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
