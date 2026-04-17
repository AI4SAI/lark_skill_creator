# Topology Guide

Slurm can be configured to support topology-aware resource allocation to optimize job performance. Slurm supports several modes of operation, one to optimize performance on systems with a three-dimensional torus interconnect and another for a hierarchical interconnect. The hierarchical mode of operation supports both fat-tree or dragonfly networks, using slightly different algorithms.

Slurm\'s native mode of resource selection is to consider the nodes as a one-dimensional array. Jobs are allocated resources on a best-fit basis. For larger jobs, this minimizes the number of sets of consecutive nodes allocated to the job.

## Contents

- Three-dimensional Topology
- Tree Topology (Hierarchical Networks)
  - Configuration Generators
- Block Topology
  - Limitations
- Environment Variables
- Multiple Topologies
- Dynamic Topology

## Three-dimensional Topology {#topo_3d}

Some larger computers rely upon a three-dimensional torus interconnect. The Cray XT and XE systems also have three-dimensional torus interconnects, but do not require that jobs execute in adjacent nodes. On those systems, Slurm only needs to allocate resources to a job which are nearby on the network. Slurm accomplishes this using a http://en.wikipedia.org/wiki/Hilbert_curve to map the nodes from a three-dimensional space into a one-dimensional space. Slurm\'s native best-fit algorithm is thus able to achieve a high degree of locality for jobs.

## Tree Topology (Hierarchical Networks) {#hierarchical}

Slurm can also be configured to allocate resources to jobs on a hierarchical network to minimize network contention. The basic algorithm is to identify the lowest level switch in the hierarchy that can satisfy a job\'s request and then allocate resources on its underlying leaf switches using a best-fit algorithm. Use of this logic requires a configuration setting of *TopologyPlugin=topology/tree*.

Note that slurm uses a best-fit algorithm on the currently available resources. This may result in an allocation with more than the optimum number of switches. The user can request a maximum number of leaf switches for the job as well as a maximum time willing to wait for that number using the `--switches` option with the salloc, sbatch and srun commands. The parameters can also be changed for pending jobs using the scontrol and squeue commands.

At some point in the future Slurm code may be provided to gather network topology information directly. Now the network topology information must be included in a *topology.conf* configuration file as shown in the examples below. The first example describes a three level switch in which each switch has two children. Note that the *SwitchName* values are arbitrary and only used for bookkeeping purposes, but a name must be specified on each line. The leaf switch descriptions contain a *SwitchName* field plus a *Nodes* field to identify the nodes connected to the switch. Higher-level switch descriptions contain a *SwitchName* field plus a *Switches* field to identify the child switches. Slurm\'s hostlist expression parser is used, so the node and switch names need not be consecutive (e.g. \"Nodes=tux\[0-3,12,18-20\]\" and \"Switches=s\[0-2,4-8,12\]\" will parse fine).

An optional LinkSpeed option can be used to indicate the relative performance of the link. The units used are arbitrary and this information is currently not used. It may be used in the future to optimize resource allocations.

The first example shows what a topology would look like for an eight node cluster in which all switches have only two children as shown in the diagram (not a very realistic configuration, but useful for an example).

    # topology.conf
    # Switch Configuration
    SwitchName=s0 Nodes=tux[0-1]
    SwitchName=s1 Nodes=tux[2-3]
    SwitchName=s2 Nodes=tux[4-5]
    SwitchName=s3 Nodes=tux[6-7]
    SwitchName=s4 Switches=s[0-1]
    SwitchName=s5 Switches=s[2-3]
    SwitchName=s6 Switches=s[4-5]

![](topo_ex1.gif){width="600"}

The next example is for a network with two levels and each switch has four connections.

    # topology.conf
    # Switch Configuration
    SwitchName=s0 Nodes=tux[0-3]   LinkSpeed=900
    SwitchName=s1 Nodes=tux[4-7]   LinkSpeed=900
    SwitchName=s2 Nodes=tux[8-11]  LinkSpeed=900
    SwitchName=s3 Nodes=tux[12-15] LinkSpeed=1800
    SwitchName=s4 Switches=s[0-3]  LinkSpeed=1800
    SwitchName=s5 Switches=s[0-3]  LinkSpeed=1800
    SwitchName=s6 Switches=s[0-3]  LinkSpeed=1800
    SwitchName=s7 Switches=s[0-3]  LinkSpeed=1800

![](topo_ex2.gif){width="600"}

As a practical matter, listing every switch connection definitely results in a slower scheduling algorithm for Slurm to optimize job placement. The application performance may achieve little benefit from such optimization. Listing the leaf switches with their nodes plus one top level switch should result in good performance for both applications and Slurm. The previous example might be configured as follows:

    # topology.conf
    # Switch Configuration
    SwitchName=s0 Nodes=tux[0-3]
    SwitchName=s1 Nodes=tux[4-7]
    SwitchName=s2 Nodes=tux[8-11]
    SwitchName=s3 Nodes=tux[12-15]
    SwitchName=s4 Switches=s[0-3]

Note that compute nodes on switches that lack a common parent switch can be used, but no job will span leaf switches without a common parent (unless the TopologyParam=TopoOptional option is used). For example, it is legal to remove the line \"SwitchName=s4 Switches=s\[0-3\]\" from the above topology.conf file. In that case, no job will span more than four compute nodes on any single leaf switch. This configuration can be useful if one wants to schedule multiple physical clusters as a single logical cluster under the control of a single slurmctld daemon.

If you have nodes that are in separate networks and are associated with unique switches in your **topology.conf** file, it\'s possible that you could get in a situation where a job isn\'t able to run. If a job requests nodes that are in the different networks, either by requesting the nodes directly or by requesting a feature, the job will fail because the requested nodes can\'t communicate with each other. We recommend placing nodes in separate network segments in disjoint partitions.

For systems with a dragonfly network, configure Slurm with *TopologyPlugin=topology/tree* plus *TopologyParam=dragonfly*. If a single job can not be entirely placed within a single network leaf switch, the job will be spread across as many leaf switches as possible in order to optimize the job\'s network bandwidth.

**NOTE**: When using the *topology/tree* plugin, Slurm identifies the network switches which provide the best fit for pending jobs. If nodes have a *Weight* defined, this will override the resource selection based on network topology.

### Configuration Generators {#config_generators}

The following independently maintained tools may be useful in generating the **topology.conf** file for certain switch types:

- Infiniband switch - **slurmibtopology**\
  https://github.com/OleHolmNielsen/Slurm_tools/tree/master/slurmibtopology
- Omni-Path (OPA) switch - **opa2slurm**\
  https://gitlab.com/jtfrey/opa2slurm
- AWS Elastic Fabric Adapter (EFA) - **ec2-topology**\
  https://github.com/aws-samples/ec2-topology-aware-for-slurm

## Block Topology {#block}

Slurm can be configured to allocate resources to jobs within a strictly enforced, hierarchical block structure using **TopologyPlugin=topology/block**. The block topology prioritizes the placement of jobs to minimize fragmentation across the cluster, as opposed to the tree topology, which focuses on fitting jobs on the first available resources. Small jobs will still be able to use the available space in a block that is partially used.

The block topology approach begins with \"base blocks\" (bblocks), which are fundamental, contiguous groups of nodes defined in [topology.conf](topology.conf.md). These base blocks can be combined with other adjacent base blocks to form \"aggregated blocks\". In turn, these higher-level blocks can be aggregated with other contiguous blocks of the same hierarchical level to construct progressively larger blocks. This hierarchical arrangement is designed to ensure optimized communication performance for jobs running within these blocks. The **BlockSizes** configuration parameter defines the specific, enforceable block sizes at each level of this hierarchy.

The allocation algorithm operates as follows:

1.  Identify the smallest block level, as defined by **BlockSizes**, that can satisfy the job\'s resource request
2.  Select a suitable subset of \"lower-level blocks\" (llblocks) that are components of this chosen aggregating block
3.  Allocate resources from the underlying base blocks that constitute this selected subset of llblocks, employing a best-fit algorithm for the precise placement of the job.

### Limitations {#block-limitations}

Since the block topology takes a different approach than the traditional tree topology, there are limitations that should be taken into consideration.

- **Ranges of nodes**\
  When using `-N`/`--nodes` to specify a range of acceptable node counts, the scheduler will have to evaluate each value of that range to find optimal placement on the available block(s). If using a range is necessary, the number of possible values should be kept as small as possible.
- **Requesting specific nodes**\
  Using `-w`/`--nodelist` to request a specific node or nodes can conflict with the block placement and is not currently supported. You can use `-x`/`--exclude` to prevent a job from being scheduled on certain nodes.
- **Contiguous blocks**\
  The scheduler will attempt to place jobs on blocks that are adjacent to each other in the block structure. You cannot currently request that a job be placed on non-adjacent blocks.

## User Options {#user_opts}

For use with the **topology/tree** plugin, user can also specify the maximum number of leaf switches to be used for their job with the maximum time the job should wait for this optimized configuration. The syntax for this option is `--switches=count[@time]`. The system administrator can limit the maximum time that any job can wait for this optimized configuration using the **SchedulerParameters** configuration parameter with the [max_switch_wait](slurm.conf.md#OPT_max_switch_wait=#) option.

When **topology/tree** or **topology/block** is configured, hostlist functions may be used in place of or alongside regular hostlist expressions in commands or configuration files that interact with the slurmctld. Valid topology functions include:

- **block{blockX}** and **switch{switchY}** - expand to all nodes in the specified block/switch.
- **blockwith{nodeX}** and **switchwith{nodeY}** - expand to all nodes in the same block/switch as the specified node.

For example:

    scontrol update node=block{b1} state=resume
    sbatch --nodelist=blockwith{node0} -N 10 program
    PartitionName=Block10 Nodes=block{block10} ...

See also the hostlist function **feature{myfeature}** [here](slurm.conf.md#OPT_Features).

## Environment Variables {#env_vars}

If the topology/tree plugin is used, two environment variables will be set to describe that job\'s network topology. Note that these environment variables will contain different data for the tasks launched on each node. Use of these environment variables is at the discretion of the user.

**SLURM_TOPOLOGY_ADDR**: The value will be set to the names network switches which may be involved in the job\'s communications from the system\'s top level switch down to the leaf switch and ending with node name. A period is used to separate each hardware component name.

**SLURM_TOPOLOGY_ADDR_PATTERN**: This is set only if the system has the topology/tree plugin configured. The value will be set component types listed in SLURM_TOPOLOGY_ADDR. Each component will be identified as either \"switch\" or \"node\". A period is used to separate each hardware component type.

## Multiple Topologies {#multi_topo}

Slurm 25.05 introduced the ability to define multiple network topologies using the [topology.yaml](topology.yaml.md) configuration file. Each partition can be configured to use a specific topology by specifying the [Topology](slurm.conf.md#OPT_Topology_1) in its partition configuration line. The Slurm controller will use the selected topology to optimize resource allocation for jobs submitted to that partition. If no topology is explicitly specified for a partition, Slurm will default to the cluster_default topology.

## Dynamic Topology {#dynamic_topo}

Nodes can be dynamically added to and removed from topologies, defined in either *topology.conf* or *topology.yaml*, by either using **scontrol** to update the node\'s topology or by using the slurmd\'s **\--conf** option to specify the node\'s topology for dynamic or cloud nodes.

This is done by specifying the **Topology** option and providing the list of topology names and units. Note that the topology defined in the **topology.conf** file will always have the name \"default\". A **topology unit** is the block name or the name of a leaf switch. Intermediate switch names (\':\' delimited) can be provided and will be created if needed (e.g. Topology=topo-tree:sw_root:s1:s2).

For **cloud nodes**, the only field that can be set with the **\--conf** flag is **Topology**, and when the node is powered down the topology will be restored to what is defined in the configuration files.

Examples using `scontrol`:

    scontrol create NodeName=d[1-100] ... Topology=topo-switch:s1,topo-block:b1"

    scontrol update NodeName=d[1-2] Topology=topo-switch:s2,topo-block:b2"

    # Remove nodes from all topology
    scontrol update NodeName=d100 Topology=

Examples using `slurmd --conf`:

    slurmd -Z --conf "... Topology=topo-switch:s1,topo-block:b1"

    slurmd -Z --conf "... Topology=default:b1"

    # Omit -Z for cloud nodes
    slurmd --conf "Topology=topo-cloud:s1"
