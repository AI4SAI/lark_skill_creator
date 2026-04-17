# Hierarchical Resource (HRES) Scheduling

## Overview

Hierarchical Resources (HRES) were added in Slurm 25.05 in a **Beta** state. While in beta, the configuration file format and other aspects of this feature may undergo substantial changes in future versions and require major changes to avoid errors. Sites that utilize this feature while in a beta state should pay particularly close attention to changes noted in RELEASE_NOTES and the CHANGELOGs when [upgrading](upgrades.md).

Hierarchical Resources allow for [license](licenses.md)-like resources to be defined as part of independent hierarchical topologies and associated with specific nodes. Jobs may request any integer count of that resource. Multiple resources may be defined in the configuration (in a [resources.yaml](resources.yaml.md) file), and will use independently defined hierarchies.

Although these hierarchical topologies have some similarities to [network topologies](topology.md), the definitions for each are completely separate.

## Planning Modes {#modes}

Three modes of resource planning are provided. In either case, a layer may be defined with a count of zero or infinite (`count: -1`) resources, with the impact of this depending on the mode used.

### Mode 1 {#mode1}

In **Mode 1**, sufficient resources are only required on one layer that overlaps with job allocation. In many cases only a single level is needed. However, multiple levels may be defined if some additional flexibility in where resources are used is preferred, as described in the example below.

A layer with a **zero** count of a resource will have no impact on scheduling. Since that layer will never satisfy the request, it will never alter the calculated list of nodes eligible to run a given job. It would be semantically equivalent to removing that layer definition.

A layer with an **infinite** count of a resource will the always allow a new job allocation to succeed. Unless prevented due to other requirements, jobs will be able to execute immediately.

For example, consider the **natural** resource defined in the example resources.yaml file below. A job that requests this resource and is allocated `node[01-04]` will pull from the pool of 100 available to `node[01-16]`. With a count of 50 specified at the higher level (`node[01-32]`), they can be allocated in addition to the resources specified in each group of 16. That is, 100 each would be available to each group of 16, and 50 more would be available on any of them, for a total of 250 of this resource.

### Mode 2 {#mode2}

In **Mode 2**, sufficient resources must be available on all layers on all levels that overlap with job allocation. Note that scheduling stalls are possible if higher levels do not make enough resources available.

A layer with a **zero** count of a resource will have a significant impact on scheduling. All nodes underneath that layer would never be able to satisfy the allocation constraints. This could be used to mark that resource unavailable for a specific portion of the cluster, e.g., for hardware maintenance, without altering the individual lower-layer resource counts.

A layer with an **infinite** count of a resource will have no impact on scheduling. Since that layer will always satisfy the request, it will never constrain execution and would be semantically equivalent to removing that layer definition.

For example, consider the **flat** resource defined in the example resources.yaml file below. A job that requests this resource and is allocated `node[01-04]` will pull from all levels that include those nodes. So it would pull from the 12 available on `node[01-08]`, from the 16 available on `node[01-16]`, and from the 24 available on `node[01-32]`. Since the highest level only contains 24, that is the maximum that can be allocated, even though a larger total is available on lower levels. This example allows a fixed set of resources to have some flexibility in where they are used.

### Mode 3 {#mode3}

In **Mode 3**, resources are allocated on a per-node basis, with the total consumption being calculated from the most granular layer and summed up into the successively higher layers. This mode is specifically designed for consumable resources like power, where the total usage at a higher level (e.g., cluster-wide) is the sum of the usage of its components (e.g., chassis level, then rack level summing multiple chassis, then datacenter row ).

The scheduler ensures that the total summed resources at every layer in the hierarchy do not exceed that layer\'s defined count.

**Important Note:** Layers defined under **Mode 3** must be able to be represented as a **rooted uniform depth tree**.

For example, consider the **power** resource defined in the example resources.yaml file below. A job that requests 1000 of the **power** resource and is allocated `node[01-16]` will pull from all levels that include those nodes. So it would pull 8000 from `node[01-08]`, 8000 from `node[09-16]`, 16000 from `node[01-16]`, and 16000 from `node[01-32]`.

## Limitations

- The resource counts cannot be dynamically changed; all changes must be made through **resources.yaml** and applied with a restart or reconfigure
- Dynamic nodes are not supported
- This implementation is in a **beta** state (see overview)
- Resource names defined through the hierarchical resources configuration must not conflict with any cluster licenses

## Examples

After defining a resource hierarchy in **resources.yaml** (see below for example), you can interact with these resources in several ways, using the syntax already used for licenses:

- View HRES

      scontrol show license

- Reserve HRES

      scontrol create reservation account=root licenses=natural(node[01-016]):30,flat(node[09-12]):4,flat(node[29-32]):2

  Note that the layer must be specified for each reserved HRES, identified by the node list present available through that layer

- Request HRES on a job

      sbatch --license=flat:2,natural:1 my_script.sh

### resources.yaml {#resources_yaml}

    ---
    - resource: flat
      mode: MODE_2
      layers:
        - nodes:            # highest level
            - "node[01-32]"
          count: 24
        - nodes:            # middle levels
            - "node[01-16]"
          count: 16
        - nodes:
            - "node[17-32]"
          count: 16
        - nodes:            # lowest levels
            - "node[01-08]"
          count: 12
        - nodes:
            - "node[09-16]"
          count: 12
        - nodes:
            - "node[17-24]"
          count: 12
        - nodes:
            - "node[25-32]"
          count: 12
    - resource: natural
      mode: MODE_1
      layers:
        - nodes:            # highest level
            - "node[01-32]"
          count: 50
        - nodes:            # lowest levels
            - "node[01-16]"
          count: 100
        - nodes:
            - "node[17-32]"
          count: 100
    - resource: power
      mode: MODE_3
      topology: blok1
      variables:
        - name: full_node
          value: 1000
        - name: full_gpu_node
          value: 2000
      layers:
        - nodes:
            - "node[01-08]"
          count: 40000
          base:
            - name: storage
              value: 5000
        - nodes:
            - "node[17-24]"
          count: 40000
        - nodes:
            - "node[09-16]"
          count: 40000
        - nodes:
            - "node[25-32]"
          count: 40000
        - nodes:
            - "node[01-16]"
          count: 60000
          base:
            - name: network1
              value: 3000
        - nodes:
            - "node[17-32]"
          count: 80000
          base:
            - name: network2
              value: 2000
        - nodes:
            - "node[01-32]"
          count: 130000
          base:
            - name: acUnit1
              value: 10000
            - name: acUnit2
              value: 8000
