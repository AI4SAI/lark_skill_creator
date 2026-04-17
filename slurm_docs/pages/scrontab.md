# scrontab

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

scrontab - manage Slurm crontab files

[ ]{#lbAC}

## SYNOPSIS

scrontab \[-u user\] file\
scrontab \[-u user\] \[ -e \| -l \| -r \]

[ ]{#lbAD}

## DESCRIPTION

**scrontab** is used to set, edit, and remove a user\'s Slurm-managed crontab. This file can define a number of recurring batch jobs to run on a scheduled interval.

Lines must be either comments starting with \'#\', whitespace, valid crontab entries or custom variable settings.

Lines starting with **#SCRON** allow options to be defined for the single following crontab entry. Options are always reset in between each crontab entry. Options include most of those available to the **sbatch** command; details are available in the **[sbatch](sbatch.md)**(1) man page.

Note that jobs are not guaranteed to execute at the preferred time. Jobs will run no more frequently than requested, but are managed by setting the BeginTime field to the next valid iteration, and are then subject to queuing delays. The exact behavior will depend on the local site configuration. Because of this method of implementation, the next job in the series won\'t be submitted until after the previous job has completed. For example, if you have a monitoring job that is scheduled to run every minute on a busy system, if the job scheduled to start at 08:20:00 isn\'t able to start until 08:20:30 and it runs for 35 seconds then the job at 08:21:00 will be skipped and the next job will be scheduled for 08:22:00.

**scrontab** uses the same syntax for date and time specifiers as **cron**. Each line has five fields that have the following meanings:

:   field allowed values\
    \-\-\-\-- \-\-\-\-\-\-\-\-\-\-\-\-\--\
    minute 0-59\
    hour 0-23\
    day of month 1-31\
    month 1-12 (or name)\
    day of week 0-7 (0 and 7 are Sunday, or use name)

A field can contain an asterisk (\*) which means that it\'s valid for each of the allowed values for the given time period. Ranges are allowed where a range is two numbers with a hyphen between them. The second number must be greater than the first. Lists are allowed, with commas separating the numbers or ranges being separated. Step values can be specified by entering a slash (/), followed by the step value, causing the job to run at the specified interval appropriate for that field.

Custom variables can be defined as within a regular shell script. The \`\$\' character introduces variable expansion. Simple parameter expansion is the only currently accepted expansion variant (i.e. \${parameter} or \${parameter:-word} are not supported). The variable expansion will only occur within **scrontab** job commands. It is not possible to expand variables in other type of lines (other variable definitions, comments or crontab entries). The expansion will happen before submitting the job, but the variable definitions will remain in the **scrontab** script. Unlike crontab, the user environment variables are ignored.

[ ]{#lbAE}

## OPTIONS

The first form of this command is used to install a new crontab from some named file or standard input if the pseudo-filename \`\`-\'\' is given.

**-e**
:   Edit the crontab. If a crontab does not exist already, a default example (without any defined entries) will be provided in the editor.

:   

**-l**
:   List the crontab. (Prints directly to stdout.)

:   

**-r**
:   Remove the crontab. Any currently running crontab-defined jobs will continue to run but will no longer recur. All other crontab-defined jobs will be cancelled.

:   

**-u** \<*user*\>
:   Edit or view a different user\'s crontab. Listing is permitted for Operators and Admins. Editing/removal is only permitted for root and the *SlurmUser* account.

:   

[ ]{#lbAF}

## SCRONTAB OPTIONS

**scrontab** allows you to use shortcuts to specify some common time intervals for the specified script to run. These include the following:

**\@yearly** \| **\@annually**
:   Job will become eligible at *00:00 Jan 01* each year.

:   

**\@monthly**
:   Job will become eligible at *00:00* on the first day of each month.

:   

**\@weekly**
:   Job will become eligible at *00:00 Sunday* of each week.

:   

**\@daily** \| **\@midnight**
:   Job will become eligible at *00:00* each day.

:   

**\@hourly**
:   Job will become eligible at the first minute of each hour.

:   

**\@elevenses**
:   Job will become eligible at *11:00* each day. (This is a non-standard extension.)

:   

**\@fika**
:   Job will become eligible at *15:00* each day. (This is a non-standard extension.)

:   

**\@teatime**
:   Job will become eligible at *16:00* each day. (This is a non-standard extension.)

:   

[ ]{#lbAG}

## ENVIRONMENT VARIABLES

**VISUAL**
:   Used as the interactive editor if set.

:   

**EDITOR**
:   Used as the interactive editor if set and **VISUAL** is not defined.

:   

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

**SLURM_DEBUG_FLAGS**
:   Specify debug flags for scrontab to use. See DebugFlags in the **[slurm.conf](slurm.conf.md)**(5) man page for a full list of flags. The environment variable takes precedence over the setting in the slurm.conf.

:   

[ ]{#lbAH}

## NOTES

**scrontab** is only available if the **ScronParameters=enable** option has been enabled in the **slurm.conf**.

**scrontab** will create a temporary file in the directory set by **TMPDIR** environment variable. If the variable is not set /tmp is used.

Jobs created with **scrontab** are assigned a single job id. When cancelled all future runs of the job will also be cancelled. The job definition will be commented out in the users **scrontab** file.

Using \"**scontrol requeue** \<*job_id*\>\" will skip the next run of the cron job and reschedule it for the next available time based on the cron expression.

[ ]{#lbAI}

## EXAMPLES

To create a job that would run at the beginning of each hour, using the \'high\' partition, \'sub1\' account and have a walltime of 1 minute, you would add the following to **scrontab**:

:   DIR=/home/user1
        #SCRON -p high
        #SCRON -A sub1
        #SCRON -t 1:00
        @hourly $DIR/date.printer.job

To have a job run every Wednesday, every other hour during the work day, each of the first five minutes of the hour and again at the thirty minute mark, you would add the following to **scrontab**.

:   1-5,30 8-17/2 * * wed $DIR/example.job

[ ]{#lbAJ}

## LIMITATIONS

The Slurm controller\'s timezone is what will be used to evaluate each crontab\'s repetition intervals. User-specific timezones are not supported.

[ ]{#lbAK}

## COPYING

Copyright (C) 2020-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAL}

## SEE ALSO

**[sbatch](sbatch.md)**(1), **[squeue](squeue.md)**(1), **[slurm.conf](slurm.conf.md)**(5)

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

SCRONTAB OPTIONS

:   

ENVIRONMENT VARIABLES

:   

NOTES

:   

EXAMPLES

:   

LIMITATIONS

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
