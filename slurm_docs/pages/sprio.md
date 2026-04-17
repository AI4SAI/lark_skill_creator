# sprio

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

sprio - view the factors that comprise a job\'s scheduling priority

[ ]{#lbAC}

## SYNOPSIS

**sprio** \[*OPTIONS*\...\]

[ ]{#lbAD}

## DESCRIPTION

**sprio** is used to view the components of a job\'s scheduling priority when the multi-factor priority plugin is installed. **sprio** is a read-only utility that extracts information from the multi-factor priority plugin. By default, **sprio** returns information for all pending jobs. Options exist to display specific jobs by job ID and user name.

[ ]{#lbAE}

## OPTIONS

**-M**, **\--clusters**=\<*string*\>
:   The cluster to issue commands to. Only one cluster name may be specified. Note that the **slurmdbd** must be up for this option to work properly, unless running in a federation with either **FederationParameters=fed_display** configured or the **\--federation** option set. This option implicitly sets the **\--local** option.

:   

**\--federation**
:   Show jobs in federation if a member of one.

:   

**-o**, **\--format**=\<*output_format*\>
:   Specify the information to be displayed, its size and position (right or left justified). The default formats when all factors have been assigned non-zero weights are

:   

    :   

        *default*
        :   \"%.15i %9r %.10Y %.10S %.10A %.10B %.10F %.10J %.10P %.10Q %20T\"

        :   

        *-l, \--long*
        :   \"%.15i %9r %.8u %.8o %.10Y %.10S %.10A %.10B %.10F %.10J %.10P %.10n %.10Q %.11N %.20T\";

        :   

    The format of each field is \"%\[.\]\[size\]type\".

:   

    :   

        *size*
        :   is the minimum field size. If no size is specified, whatever is needed to print the information will be used.

        :   

        *.*
        :   indicates the output should be left justified. By default, output is right justified.

        :   

    Valid *type* specifications include:

:   

    :   

        **%a**
        :   Normalized age priority

        :   

        **%A**
        :   Weighted age priority

        :   

        **%b**
        :   Normalized association priority

        :   

        **%B**
        :   Weighted association priority

        :   

        **%c**
        :   Cluster name. Only applicable for federated clusters

        :   

        **%f**
        :   Normalized fair-share priority

        :   

        **%F**
        :   Weighted fair-share priority

        :   

        **%i**
        :   Job ID

        :   

        **%j**
        :   Normalized job size priority

        :   

        **%J**
        :   Weighted job size priority

        :   

        **%n**
        :   QOS name

        :   

        **%N**
        :   Nice adjustment

        :   

        **%o**
        :   Account name

        :   

        **%p**
        :   Normalized partition priority

        :   

        **%P**
        :   Weighted partition priority

        :   

        **%q**
        :   Normalized quality of service priority

        :   

        **%Q**
        :   Weighted quality of service priority

        :   

        **%r**
        :   Partition name

        :   

        **%S**
        :   Weighted admin priority.

        :   

        **%t**
        :   Normalized TRES priorities

        :   

        **%T**
        :   Weighted TRES priorities

        :   

        **%u**
        :   User name for a job

        :   

        **%Y**
        :   Job priority

        :   

        **%y**
        :   Normalized job priority

:   

**\--help**
:   Print a help message describing all options **sprio**.

:   

**-j**, **\--jobs**=\<*job_id_list*\>
:   Requests a comma separated list of job ids to display. Defaults to all jobs. Since this option\'s argument is optional, for proper parsing the single letter option must be followed immediately with the value and not include a space between them. For example \"-j1008,1009\" and not \"-j 1008,1009\".

:   

**\--local**
:   Show only jobs local to this cluster. Ignore other clusters in this federation (if any). Overrides \--federation.

:   

**-l**, **\--long**
:   Report more of the available information for the selected jobs.

:   

**-h**, **\--noheader**
:   Do not print a header on the output.

:   

**-n**, **\--norm**
:   Display the normalized priority factors for the selected jobs.

:   

**-p**, **\--partition**=\<*partition_list*\>
:   Requests a comma separated list of partitions to display. Defaults to all partitions.

:   

**\--sibling**
:   Show all sibling jobs on a federated cluster. Without this option in a federated cluster, each job in each partition will have its priority and its components reported for only one cluster. Each sibling job on the various clusters in the federation may have different priority, which will not be reported without using this option. Implicitly adds \"%c\" (cluster name) to the output format.

:   

**-S**, **\--sort**=\<*sort_list*\>
:   Specification of the order in which jobs should be reported. This uses the same field specification as \<output_format\>. Multiple sorts may be performed by listing multiple sort fields separated by commas. The field specifications may be preceded by \"+\" or \"-\" for ascending (default) or descending respectively. For example, a \<sort_list\> of \"u,r,-y\" will sort the job priority reports by username, partition name, and descending job priority, in that order. The default \<sort_list\> is \"i\" (ascending job id).

:   

**\--usage**
:   Print a brief help message listing the **sprio** options.

:   

**-u**, **\--user**=\<*user_list*\>
:   Request jobs from a comma separated list of users. The list can consist of user names or user id numbers.

:   

**-v**, **\--verbose**
:   Report details of sprios actions.

:   

**-V**, **\--version**
:   Print version information and exit.

:   

**-w**, **\--weights**
:   Display the configured weights for each factor. This is for information purposes only. Actual job data is suppressed.

:   

[ ]{#lbAF}

## PERFORMANCE

Executing **sprio** sends a remote procedure call to **slurmctld**. If enough calls from **sprio** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **sprio** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **sprio** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAG}

## ENVIRONMENT VARIABLES

If no corresponding command line option is specified, **sprio** will use the value of the following environment variables.

**SLURM_CLUSTERS**
:   Same as **\--clusters**

:   

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for sprio to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

**SPRIO_FEDERATION**
:   Same as **\--federation**

:   

**SPRIO_FORMAT**
:   Same as **-o \<output_format\>, \--format=\<output_format\>**

:   

**SPRIO_LOCAL**
:   Same as **\--local**

:   

**SPRIO_SIBLING**
:   Same as **\--sibling**

:   

[ ]{#lbAH}

## EXAMPLES

Print the list of all pending jobs with their weighted priorities

:   

:   $ sprio
          JOBID   PRIORITY        AGE  FAIRSHARE    JOBSIZE  PARTITION        QOS
          65539      62664          0      51664       1000      10000          0
          65540      62663          0      51663       1000      10000          0
          65541      62662          0      51662       1000      10000          0

Print the list of all pending jobs with their normalized priorities

:   

:   $ sprio -n
          JOBID PRIORITY   AGE        FAIRSHARE  JOBSIZE    PARTITION  QOS
          65539 0.00001459 0.0007180  0.5166470  1.0000000  1.0000000  0.0000000
          65540 0.00001459 0.0007180  0.5166370  1.0000000  1.0000000  0.0000000
          65541 0.00001458 0.0007180  0.5166270  1.0000000  1.0000000  0.0000000

Print the job priorities for specific jobs

:   

:   $ sprio --jobs=65548,65547
          JOBID   PRIORITY        AGE  FAIRSHARE    JOBSIZE  PARTITION        QOS
          65547      62078          0      51078       1000      10000          0
          65548      62077          0      51077       1000      10000          0

Print the job priorities for jobs of specific users

:   

:   $ sprio --users=fred,sally
          JOBID     USER  PRIORITY       AGE  FAIRSHARE   JOBSIZE  PARTITION     QOS
          65548     fred     62079         1      51077      1000      10000       0
          65549    sally     62080         1      51078      1000      10000       0

Print the configured weights for each priority component

:   

:   $ sprio -w
          JOBID   PRIORITY        AGE  FAIRSHARE    JOBSIZE  PARTITION        QOS
          Weights                1000     100000       1000      10000          1

[ ]{#lbAI}

## COPYING

Copyright (C) 2009 Lawrence Livermore National Security. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. [ ]{#lbAJ}

## SEE ALSO

**[squeue](squeue.md)**(1), **[sshare](sshare.md)**(1)

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
