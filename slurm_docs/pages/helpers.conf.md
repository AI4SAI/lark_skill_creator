# helpers.conf

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

helpers.conf - Slurm configuration file for the helpers plugin.

[ ]{#lbAC}

## DESCRIPTION

**helpers.conf** is an ASCII file which defines parameters used by Slurm\'s \"helpers\" node feature plugin. The file will always be located in the same directory as the **slurm.conf**.

[ ]{#lbAD}

## PARAMETERS

Parameter names are case insensitive. Any text following a \"#\" in the configuration file is treated as a comment through the end of that line. The size of each line in the file is limited to 1024 characters. Changes to the configuration file take effect upon restart of Slurm daemons, daemon receipt of the SIGHUP signal, or execution of the command \"scontrol reconfigure\" unless otherwise noted.

**AllowUserBoot**=\<*user1*\>\[,\<*user2*\>\...\]
:   Controls which users are allowed to change the features with this plugin. Default is to allow ALL users.

:   

**BootTime**=\<*time*\>
:   Controls how much time a node has to reboot before a timeout occurs and a failure is assumed. Default value is 300 seconds.

:   

**ExecTime**=\<*time*\>
:   Controls how much time the Helper program can run before a timeout occurs and a failure is assumed. Default value is 10 seconds.

:   

**Feature**=\<*string*\> **Helper**=\<*file*\> \<**Flags**=\<*flags*\>

:   Defines **Feature(s)** and a corresponding **Helper** program that reports and modifies the status of the feature(s). Multiple **Feature** entries are allowed, one for each feature and corresponding program/script. A comma separated list of features can also be defined for one **Helper**.

    Features can be defined per node by creating a unique file for each node. The controller must have a **helpers.conf** that lists all possible helper features.

    :   

        Currently supported flags are:

        :   

        :   

        **rebootless**
        :   Indicate that the feature doesn\'t require a node reboot. If set, feature activation won\'t execute the *RebootProgram*, the node will just register that the node rebooted to slurmctld without an actual reboot.

:   A single **helpers.conf** can be created that defines features for specific nodes by prepending *NodeName=\<nodelist\>* to the front of the **Feature** line. A **Feature** not prepended with *NodeName* will apply to all nodes.

:   # helpers.conf
        NodeName=n1_[1-10] Feature=a1,a2 Helper=/path/helper.sh
        NodeName=n2_[1-10] Feature=b1,b2 Helper=/path/helper.sh
        Feature=c1,c2 Helper=/path/helper.sh

    If a feature is defined in the **helpers.conf** and is not defined on a specific node in the **helpers.conf** but is defined for that node in the slurm.conf, that feature is treated as a changeable/rebootable feature by the controller. For example, if feature *fa* is defined on node *node1* in the **slurm.conf** but is only listed on *node2* in the **helpers.conf**, the feature will still trigger the node to be rebooted if not active.

    The **Helper** is an arbitrary program or script that reports and modifies the feature set on a given node. The helpers are site-specific and are not included with Slurm. Features modified by the helpers require a reboot of the node using the **RebootProgram**. The **Helper** program/script must be executable by the **SlurmdUser**. The same program/script can be used to control multiple features. slurmd will execute the **Helper** in one of two ways:

:   

    :   1\. Execute with no arguments to query the status of node features. It must return an exit code of 0 and either print a superset of the features expected by Slurm, or it can print nothing. Otherwise, the node will be drained.

        2\. Execute with a single argument of the feature to be activated on node reboot. In the case of multiple features the script is called multiple times.

**MutuallyExclusive**=\<*feature_list*\>
:   Prevents certain features from being specified for the same job. There can be multiple **MutuallyExclusive** entries, each with their own list of features that are mutually exclusive among themselves (i.e. features on one line are only mutually exclusive with other features on the same line, but not mutually exclusive with features on other lines).

:   

[ ]{#lbAE}

## EXAMPLE

**/etc/slurm/slurm.conf**:
:   To enable the helpers plugin, the **slurm.conf** needs to have the following entry:

:   NodeFeaturesPlugins=node_features/helpers

**/etc/slurm/helpers.conf**:
:   The following example **helpers.conf** demonstrates that multiple features can use the same Helper script and that there can be multiple lists of features that are mutually exclusive. For example, with the following configuration a job cannot request both \"nps1\" and \"nps2\", nor can it request both \"mig=on\" and \"mig=off\". However, it could request \"nps1\" and \"mig=on\" at the same time.

:   # helpers.conf
        Feature=nps1,nps2,nps4 Helper=/usr/local/bin/nps
        Feature=mig=on Helper=/usr/local/bin/mig
        Feature=mig=off Helper=/usr/local/bin/mig
        MutuallyExclusive=nps1,nps2,nps4
        MutuallyExclusive=mig=on,mig=off
        ExecTime=60
        BootTime=60
        AllowUserBoot=user1,user2

**Example Helper script**:
:   Helper scripts need to have the executable bit set and must exist on the nodes, where they will be executed by slurmd. When the helper script is called with no arguments it should return the feature(s) that are currently active for the node, with multiple features being new-line delimited. When the helper script is called with a feature to be enabled for the node, it should configure the node in a way that the specified feature will be enabled when the node reboots. This example script just writes the active feature name to a file but production scripts will probably be more complex.

:   #!/bin/bash

        if [ "$1" = "nps1" ]; then
            echo "$1" > /etc/slurm/feature
        elif [ "$1" = "nps2" ]; then
            echo "$1" > /etc/slurm/feature
        elif [ "$1" = "nps4" ]; then
            echo "$1" > /etc/slurm/feature
        else
            cat /etc/slurm/feature
        fi

[ ]{#lbAF}

## COPYING

Copyright (C) 2021 NVIDIA CORPORATION. All rights reserved.\
Copyright (C) 2021 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAG}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

DESCRIPTION

:   

PARAMETERS

:   

EXAMPLE

:   

COPYING

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
