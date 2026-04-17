# Large Cluster Administration Guide

This document contains Slurm administrator information specifically for clusters containing 1,024 nodes or more. Some examples of large systems currently managed by Slurm are:

- Frontier at Oak Ridge National Laboratory (ORNL) with 8,699,904 cores.
- Tianhe-2 at the National University of Defense Technology in China with 4,981,760 cores.
- Perlmutter at National Energy Research Scientific Computing (NERSC) with 761,856 cores.

Slurm operation on systems orders of magnitude larger has been validated using emulation. Getting optimal performance at that scale does require some tuning and this document should help get you off to a good start. A working knowledge of Slurm should be considered a prerequisite for this material.

## Performance {#perf}

Times below are for execution of an MPI program printing \"Hello world\" and exiting and includes the time for processing output. Your performance may vary due to differences in hardware, software, and configuration.

- 1,966,080 tasks on 122,880 compute nodes of a BlueGene/Q: 322 seconds
- 30,000 tasks on 15,000 compute nodes of a Linux cluster: 30 seconds

## System Configuration {#sys_config}

Three system configuration parameters must be set to support a large number of open files and TCP connections with large bursts of messages. Changes can be made using the **/etc/rc.d/rc.local** or **/etc/sysctl.conf** script to preserve changes after reboot. In either case, you can write values directly into these files (e.g. *\"echo 388067 \> /proc/sys/fs/file-max\"*).

- **/proc/sys/fs/file-max**: The maximum number of concurrently open files. The appropriate amount is highly dependent on system specs and workload. We recommend starting with a minimum of 388067 or the default for your OS, whichever is greater. This may need to be adjusted upwards, depending on your needs.
- **/proc/sys/net/ipv4/tcp_max_syn_backlog**: Maximum number of remembered connection requests, which still have not received an acknowledgment from the connecting client. The default value is 1024 for systems with more than 128Mb of memory, and 128 for low memory machines. If server suffers of overload, try to increase this number.
- **/proc/sys/net/core/somaxconn**: Limit of socket listen() backlog, known in userspace as SOMAXCONN. Defaults to 128. The value should be raised substantially to support bursts of request. For example, to support a burst of 1024 requests, set somaxconn to 1024.

The transmit queue length (**txqueuelen**) may also need to be modified using the ifconfig command. A value of 4096 has been found to work well for one site with a very large cluster (e.g. *\"ifconfig txqueuelen 4096\"*).

### Thread/Process Limit {#process_limit}

There is a newly introduced limit in SLES 12 SP2 (used on Cray systems with CLE 6.0UP04, to be released mid-2017). The version of systemd shipped with SLES 12 SP2 contains support for the https://www.suse.com/releasenotes/x86_64/SUSE-SLES/12-SP2/#fate-320358. Under the new systemd version, each init script or systemd service is limited to 512 threads/processes by default. This could cause issues for the slurmctld and slurmd daemons on large clusters or systems with a high job throughput rate. To increase the limit beyond the default:

- If using a systemd service file: Add *TasksMax=N* to the \[Service\] section. N can be a specific number, or special value *infinity*.

- If using an init script: Create the file\
  /etc/systemd/system/\<init script name\>.service.d/override.conf\
  with these contents:

        [Service]
        TasksMax=N

Note: Earlier versions of systemd that don\'t support the PIDs cgroup controller simply ignore the TasksMax setting.

## User Limits {#limits}

The **ulimit** values in effect for the **slurmctld** daemon should be set quite high for memory size, open file count and stack size.

## Node Selection Plugin (SelectType) {#select_type}

While allocating individual processors within a node is great for smaller clusters, the overhead of keeping track of the individual processors and memory within each node adds significant overhead. For best scalability, allocate whole nodes using *select/linear* and avoid *select/cons_tres*.

## Job Accounting Gather Plugin (JobAcctGatherType) {#acct_gather}

Job accounting relies upon the *slurmstepd* daemon on each compute node periodically sampling data. This data collection will take compute cycles away from the application inducing what is known as *system noise*. For large parallel applications, this system noise can detract from application scalability. For optimal application performance, disabling job accounting is best (*jobacct_gather/none*). Consider use of job completion records (*JobCompType*) for accounting purposes as this entails far less overhead. If job accounting is required, configure the sampling interval to a relatively large size (e.g. *JobAcctGatherFrequency=task=300*). Some experimentation may be required to deal with collisions on data transmission.

## Node Configuration {#node_config}

While Slurm can track the amount of memory and disk space actually found on each compute node and use it for scheduling purposes, this entails extra overhead. Optimize performance by specifying the expected configuration using the available parameters (*RealMemory*, *CPUs*, and *TmpDisk*). If the node is found to contain less resources than configured, it will be marked DOWN and not used. While Slurm can easily handle a heterogeneous cluster, configuring the nodes using the minimal number of lines in *slurm.conf* will both make for easier administration and better performance.

## Timers

The *EioTimeout* configuration parameter controls how long the srun command will wait for the slurmstepd to close the TCP/IP connection used to relay data between the user application and srun when the user application terminates. The default value is 60 seconds. Larger systems and/or slower networks may need a higher value.

If a high throughput of jobs is anticipated (i.e. large numbers of jobs with brief execution times) then configure *MinJobAge* to the smallest interval practical for your environment. *MinJobAge* specifies the minimum number of seconds that a terminated job will be retained by Slurm\'s control daemon before purging. After this time, information about terminated jobs will only be available through accounting records.

The configuration parameter *SlurmdTimeout* determines the interval at which *slurmctld* routinely communicates with *slurmd*. Communications occur at half the *SlurmdTimeout* value. The purpose of this is to determine when a compute node fails and thus should not be allocated work. Longer intervals decrease system noise on compute nodes (we do synchronize these requests across the cluster, but there will be some impact upon applications). For really large clusters, *SlurmdTimeout* values of 120 seconds or more are reasonable.

If MPICH-2 is used, the srun command will manage the key-pairs used to bootstrap the application. Depending upon the processor speed and architecture, the communication of key-pair information may require extra time. This can be done by setting an environment variable PMI_TIME before executing srun to launch the tasks. The default value of PMI_TIME is 500 and this is the number of microseconds allotted to transmit each key-pair. We have executed up to 16,000 tasks with a value of PMI_TIME=4000.

The individual slurmd daemons on compute nodes will initiate messages to the slurmctld daemon only when they start up or when the epilog completes for a job. When a job allocated a large number of nodes completes, it can cause a very large number of messages to be sent by the slurmd daemons on these nodes to the slurmctld daemon all at the same time. In order to spread this message traffic out over time and avoid message loss, The *EpilogMsgTime* parameter may be used. Note that even if messages are lost, they will be retransmitted, but this will result in a delay for reallocating resources to new jobs.

## Other

Slurm uses hierarchical communications between the slurmd daemons in order to increase parallelism and improve performance. The *TreeWidth* configuration parameter controls the fanout of messages. The default value is 16, meaning each slurmd daemon can communicate with up to 16 other slurmd daemons and 4368 nodes can be contacted with three message hops. The default value will work well for most clusters. Optimal system performance can typically be achieved if *TreeWidth* is set to the cube root of the number of nodes in the cluster.

The srun command automatically increases its open file limit to the hard limit in order to process all of the standard input and output connections to the launched tasks. It is recommended that you set the open file hard limit to 8192 across the cluster.
