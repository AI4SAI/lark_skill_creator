# sh5util

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

sh5util - Tool for merging HDF5 files from the acct_gather_profile plugin that gathers detailed data for jobs running under Slurm

[ ]{#lbAC}

## SYNOPSIS

sh5util

[ ]{#lbAD}

## DESCRIPTION

sh5util merges HDF5 files produced on each node for each step of a job into one HDF5 file for the job. The resulting file can be viewed and manipulated by common HDF5 tools such as HDF5View, h5dump, h5edit, or h5ls.

sh5util also has two extract modes. The first, writes a limited set of data for specific nodes, steps, and data series in \"comma separated value\" form to a file which can be imported into other analysis tools such as spreadsheets.

The second, (Item-Extract) extracts one data time from one time series for all the samples on all the nodes from a jobs HDF5 profile.

\- Finds sample with maximum value of the item.

\- Write CSV file with min, ave, max, and item totals for each node for each sample

[ ]{#lbAE}

## OPTIONS

**-E**, **\--extract**
:   Extract data series from a merged job file.

:   

    :   

        Extract mode options

        :   

        :   

        **-i**, **\--input**=*path*
        :   merged file to extract from (default ./job\_\$jobid.h5)

        :   

        **-N**, **\--node**=*nodename*
        :   Node name to extract (default is all)

        :   

        **-l**, **\--level**=\[Node:Totals \| Node:TimeSeries\]
        :   Level to which series is attached. (default Node:Totals)

        :   

        **-s**, **\--series**=\[Energy \| Filesystem \| Network \| Task \| Task\_#\]
        :   **Task** is all tasks, **Task\_#** (# is a task id) (default is everything)

:   

**-h**, **\--help**
:   Print this description of use.

:   

**-I**, **\--item-extract**
:   Extract one data item from all samples of one data series from all nodes in a merged job file.

:   

    :   

        Item-Extract mode options

        :   

        :   

        **-s**, **\--series**=\[Energy \| Filesystem \| Network \| Task\]

        :   

        :   

        **-d**, **\--data**
        :   Name of data item in series (See note below).

:   

**-j**, **\--jobs**=\<*job*\[.*step*\]\>
:   Format is \<*job*\[.*step*\]\>. Merge this job/step (or a comma-separated list of job steps). This option is required. Not specifying a step will result in all steps found to be processed.

:   

**-L**, **\--list**
:   Print the items of a series contained in a job file.

:   

    :   

        List mode options

        :   

        :   

        **-i**, **\--input**=*path*
        :   Merged file to extract from (default ./job\_\$jobid.h5)

        :   

        **-s**, **\--series**=\[Energy \| Filesystem \| Network \| Task\]

        :   

:   

**-o**, **\--output**=\<*path*\>
:   Path to a file into which to write. Default for merge is ./job\_\$jobid.h5 Default for extract is ./extract\_\$jobid.csv

:   

**-p**, **\--profiledir**=\<*dir*\>
:   Directory location where node-step files exist default is set in acct_gather.conf.

:   

**-S**, **\--savefiles**
:   Instead of removing node-step files after merging them into the job file, keep them around.

:   

**\--usage**
:   Display brief usage message.

:   

**\--user**=\<*user*\>
:   User who profiled job. (Handy for root user, defaults to user running this command.)

:   

[ ]{#lbAF}

## Data Items per Series

**Energy**

:   

    :   Power\
        CPU_Frequency

:   

**Filesystem**

:   

    :   Reads\
        Megabytes_Read\
        Writes\
        Megabytes_Write

:   

**Network**

:   

    :   Packets_In\
        Megabytes_In\
        Packets_Out\
        Megabytes_Out

:   

**Task**

:   

    :   CPU_Frequency\
        CPU_Time\
        CPU_Utilization\
        RSS\
        VM_Size\
        Pages\
        Read_Megabytes\
        Write_Megabytes

:   

[ ]{#lbAG}

## PERFORMANCE

Executing **sh5util** sends a remote procedure call to **slurmctld**. If enough calls from **sh5util** or other Slurm client commands that send remote procedure calls to the **slurmctld** daemon come in at once, it can result in a degradation of performance of the **slurmctld** daemon, possibly resulting in a denial of service.

Do not run **sh5util** or other Slurm client commands that send remote procedure calls to **slurmctld** from loops in shell scripts or other programs. Ensure that programs limit calls to **sh5util** to the minimum necessary for the information you are trying to gather.

[ ]{#lbAH}

## EXAMPLES

Merge node-step files (as part of a sbatch script):

:   

:   $ sbatch -n1 -d$SLURM_JOB_ID --wrap="sh5util --savefiles -j $SLURM_JOB_ID"

Extract all task data from a node:

:   

:   $ sh5util -j 42 -N snowflake01 --level=Node:TimeSeries --series=Tasks

Extract all energy data:

:   

:   $ sh5util -j 42 --series=Energy --data=power

[ ]{#lbAI}

## COPYING

Copyright (C) 2013 Bull.\
Copyright (C) 2013-2022 SchedMD LLC. Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAJ}

## SEE ALSO

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

Data Items per Series

:   

PERFORMANCE

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
