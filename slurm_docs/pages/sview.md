# sview

Section: Slurm Commands (1)\
Updated: Slurm Commands\
Index

[ ]{#lbAB}

## NAME

sview - graphical user interface to view and modify Slurm state.

[ ]{#lbAC}

## SYNOPSIS

sview

[ ]{#lbAD}

## DESCRIPTION

sview can be used to view Slurm configuration, job, step, node and partitions state information. Authorized users can also modify select information.

The primary display modes are *Jobs* and *Partitions*, each with a selection tab. There is also an optional map of the nodes on the left side of the window which will show the nodes associated with each job or partition. Left-click on the tab of the display you would like to see. Right-click on the tab in order to control which fields will be displayed.

Within the display window, left-click on the header to control the sort order of entries (e.g. increasing or decreasing) in the display. You can also left-click and drag the headers to move them right or left in the display. If a JobID has an arrow next to it, click on that arrow to display or hide information about that job\'s steps. Right-click on a line of the display to get more information about the record.

There is an *Admin Mode* option which permits the user root to modify many of the fields displayed, such as node state or job time limit. In the mode, a *Slurm Reconfigure* Action is also available. It is recommended that *Admin Mode* be used only while modifications are actively being made. Disable *Admin Mode* immediately after the changes to avoid possibly making unintended changes.

[ ]{#lbAE}

## ENVIRONMENT VARIABLES

Some **sview** options may be set via environment variables. These environment variables, along with their corresponding options, are listed below. (Note: Command line options will always override these settings.)

**SLURM_CONF**
:   The location of the Slurm configuration file.

:   

[ ]{#lbAF}

## NOTES

The sview command can only be build if *gtk+-2.0* is installed. Systems lacking these libraries will have Slurm installed without the sview command.

At least some gtk themes are unable to display large numbers of lines (jobs, nodes, etc). The information is still in gtk\'s internal data structures, but not visible by scrolling down the window. The gtk2-engines-qtcurve theme does seem to have particularly good scalability.

Newer gtk3 themes do not allow the background colors used for the node map to be displayed.

On systems with the topology/tree plugin configured, the sview command will attempt to display the nodes on each switch on a separate line. Change the sview configuration for optimal viewing by selecting \"Options\" then \"Set Default Settings\". The \"Nodes in Row\" and \"Node Button Size in Pixels\" would be the mostly commonly changed options.

[ ]{#lbAG}

## COPYING

Copyright (C) 2006-2007 The Regents of the University of California. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2008-2011 Lawrence Livermore National Security.\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAH}

## SEE ALSO

**[sinfo](sinfo.md)**(1), **[squeue](squeue.md)**(1), **[scontrol](scontrol.md)**(1), **[slurm.conf](slurm.conf.md)**(5), **sched_setaffinity** (2), **numa** (3)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

SYNOPSIS

:   

DESCRIPTION

:   

ENVIRONMENT VARIABLES

:   

NOTES

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
