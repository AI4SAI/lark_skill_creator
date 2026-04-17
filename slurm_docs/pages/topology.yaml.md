# topology.yaml

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

topology.yaml - Slurm configuration file for the topology plugins

[ ]{#lbAC}

## DESCRIPTION

**topology.yaml** is a YAML-formatted configuration file that defines multiple network topologies for optimizing job resource allocation in Slurm. The file must be located in the same directory as **slurm.conf**. Any text following a \"#\" in this file is treated as a comment through the end of that line.

Additional details are available in **[topology.conf](topology.conf.md)**(5) and in the Topology Guide: \<[https://slurm.schedmd.com/topology.html](topology.md)\>

**NOTE**: Slurm will first check for topology.yaml. If this file exists, topology.conf will be ignored.

[ ]{#lbAD}

## PARAMETERS

Each topology contains the following attributes:

**topology**
:   Unique name of the topology, will be used to identify it on partition configurations. Must be the first attribute.

:   

**cluster_default**
:   The first topology defined with **cluster_default: true** will be used for partitions without an explicitly specified topology and cluster-wide operations not tied to a partition (e.g., slurmctld-to-slurmd communication). Defaults to **false**.

:   

Each topology must also define exactly one of the following topology types:

:   

    **block**
    :   This topology will use the **topology/block** plugin. Must contain additional fields, see below.

    :   

    **flat**
    :   If set to **true**, this topology will use the **topology/flat** plugin, which is the default if no TopologyPlugin or topology.yaml is specified.

    :   

    **tree**
    :   This topology will use the **topology/tree** plugin. Must contain additional fields, see below.

    :   

[ ]{#lbAE}

### Block definitions

Each block topology contains the following attributes:

**block_sizes**
:   List of the planning base block size, alongside any higher-level block sizes that would be enforced. Successive **BlockSizes** must be a power of two larger than the prior values.

:   

**blocks**
:   List of blocks available in this topology. Each block contains the following attributes:

    :   

        **block**
        :   The name of a block. This name is internal to Slurm and arbitrary. Each block should have a unique name. This field must be specified.

        :   

        **nodes**
        :   Child nodes of the named block.

        :   

:   

[ ]{#lbAF}

### Tree definitions

Each tree topology contains the following attribute:

**switches**
:   List of switches available in this topology. Each switch contains the following attributes:

    :   

        **switch**
        :   The name of a switch. This name is internal to Slurm and arbitrary. Each switch should have a unique name. This field must be specified and cannot be longer than 64 characters.

        :   

        **children**
        :   Child switches of the named switch.

        :   

        **nodes**
        :   Child nodes of the named leaf switch.

        :   

:   

[ ]{#lbAG}

## EXAMPLE

    ---
    - topology: topo1
      cluster_default: true
      tree:
        switches:
          - switch: sw_root
            children: s[1-2]
          - switch: s1
            nodes: node[01-02]
          - switch: s2
            nodes: node[03-04]
    - topology: topo2
      cluster_default: false
      block:
        block_sizes:
          - 4
          - 16
        blocks:
          - block: b1
            nodes: node[01-04]
          - block: b2
            nodes: node[05-08]
          - block: b3
            nodes: node[09-12]
          - block: b4
            nodes: node[13-16]
    - topology: topo3
      cluster_default: false
      flat: true

[ ]{#lbAH}

## COPYING

Copyright (C) 2025 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAI}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[topology.conf](topology.conf.md)**(5)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

DESCRIPTION

:   

PARAMETERS

:   

    Block definitions

    :   

    Tree definitions

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
