# Frequently Asked Questions

## For Management

- Is Slurm really free?
- Why should I use Slurm or other free software?
- Why should I pay for free software?
- What does \"Slurm\" stand for?

## For Researchers

- How should I cite work involving Slurm?

## For Users

### Designing Jobs

- How can I run multiple jobs from within a single script?
- How can I run a job within an existing job allocation?
- Slurm documentation refers to CPUs, cores and threads. What exactly is considered a CPU?
- How do I run specific tasks on certain nodes in my allocation?
- How can I get the task ID in the output or error file name for a batch job?
- How does Slurm establish the environment for my job?
- Can the *make* command utilize the resources allocated to a Slurm job?
- How can I run an Ansys program with Slurm?

### Submitting Jobs

- Why are my srun options ignored?
- Why does the srun \--overcommit option not permit multiple jobs to run on nodes?
- Why is the srun \--u/\--unbuffered option adding a carriage return to my output?
- What is the difference between the sbatch and srun commands?
- Can tasks be launched with a remote (pseudo) terminal?
- How can I get shell prompts in interactive mode?
- Can Slurm export an X11 display on an allocated compute node?

### Scheduling

- Why is my job not running?
- Why is the Slurm backfill scheduler not starting my job?

### Killed Jobs

- Why is my job killed prematurely?
- Why is my batch job that launches no job steps being killed?
- What does \"srun: Force Terminated job\" indicate?
- What does this mean: \"srun: First task exited 30s ago\" followed by \"srun Job Failed\"?

### Managing Jobs

- How can I temporarily prevent a job from running (e.g. place it into a *hold* state)?
- Can I change my job\'s size after it has started running?
- Why does squeue (and \"scontrol show jobid\") sometimes not display a job\'s estimated start time?
- Can squeue output be color coded?
- Why is my job/node in a COMPLETING state?
- How can a job in a complete or failed state be requeued?
- Why is sview not coloring/highlighting nodes properly?
- Why is my MPICH2 or MVAPICH2 job not running with Slurm? Why does the DAKOTA program not run with Slurm?

### Resource Limits

- Why are my resource limits not propagated?
- Why are jobs not getting the appropriate memory limit?
- Why is my MPI job failing due to the locked memory (memlock) limit being too low?

## For Administrators

### Test Environments

- Can multiple Slurm systems be run in parallel for testing purposes?
- Can Slurm emulate a larger cluster?
- Can Slurm emulate nodes with more resources than physically exist on the node?

### Build and Install

- Why aren\'t pam_slurm.so, auth_none.so, or other components in a Slurm RPM?
- How can I build Slurm with debugging symbols?
- How can a patch file be generated from a Slurm commit in GitHub?
- How can I apply a patch to my Slurm source?
- Why am I being offered an automatic update for Slurm?

### Cluster Management

- How should I relocate the primary or backup controller?
- Do I need to maintain synchronized clocks on the cluster?
- How can I stop Slurm from scheduling jobs?
- How can I dry up the workload for a maintenance period?
- What should I be aware of when upgrading Slurm?
- Is there anything exceptional to be aware of when upgrading my database server?
- When adding a new cluster, how can the Slurm cluster configuration be copied from an existing cluster to the new cluster?
- How could some jobs submitted immediately before the slurmctld daemon crashed be lost?
- Is resource limit propagation useful on a homogeneous cluster?
- Why are the resource limits set in the database not being enforced?
- Can Slurm be configured to manage licenses?
- How easy is it to switch from PBS or Torque to Slurm?
- What might account for MPI performance being below the expected level?
- How do I safely remove partitions?
- How can a routing queue be configured?
- What happened to the \"none\" plugins?

### Accounting Database

- Why should I use the slurmdbd instead of the regular database plugins?
- How critical is configuring high availability for my database?
- How can I use double quotes in MySQL queries?

### Compute Nodes (slurmd)

- Why is a node shown in state DOWN when the node has registered for service?
- What happens when a node crashes?
- How can I control the execution of multiple jobs per node?
- Why are jobs allocated nodes and then unable to initiate programs on some nodes?
- Why does *slurmctld* log that some nodes are not responding even if they are not in any partition?
- How can I easily preserve drained node information between major Slurm updates?
- Does anyone have an example node health check script for Slurm?
- Why doesn\'t the *HealthCheckProgram* execute on DOWN nodes?
- How can I prevent the *slurmd* and *slurmstepd* daemons from being killed when a node\'s memory is exhausted?
- I see the host of my calling node as 127.0.1.1 instead of the correct IP address. Why is that?
- How should I add nodes to Slurm?
- How should I remove nodes from Slurm?
- Why is a compute node down with the reason set to \"Node unexpectedly rebooted\"?
- How do I convert my nodes to Control Group (cgroup) v2?
- Can Slurm be used to run jobs on Amazon\'s EC2?

### User Management

- How can PAM be used to control a user\'s limits on or access to compute nodes?
- How can I exclude some users from pam_slurm?
- Can a user\'s account be changed in the database?
- I had to change a user\'s UID and now they cannot submit jobs. How do I get the new UID to take effect?
- How can I get SSSD to work with Slurm?

### Jobs

- How is job suspend/resume useful?
- How can I suspend, resume, hold or release all of the jobs belonging to a specific user, partition, etc?
- After manually setting a job priority value, how can its priority value be returned to being managed by the priority/multifactor plugin?
- Can I update multiple jobs with a single *scontrol* command?
- How could I automatically print a job\'s Slurm job ID to its standard output?
- Is it possible to write to user stdout?
- Why are user processes and *srun* running even though the job is supposed to be completed?
- How can a job which has exited with a specific exit code be requeued?
- Why is Slurm unable to set the CPU frequency for jobs?
- Can the salloc command be configured to launch a shell on a node in the job\'s allocation?
- How can I set up a private /tmp and /dev/shm for jobs on my machine?
- How do I configure Slurm to work with System V IPC enabled applications?

### General Troubleshooting

- If a Slurm daemon core dumps, where can I find the core file?
- How can I get a backtrace from a core file?

### Error Messages

- \"Cannot resolve X plugin operations\" on daemon startup
- \"Credential replayed\" in *SlurmdLogFile*
- \"Invalid job credential\"
- \"Task launch failed on node \... Job credential replayed\"
- \"Unable to accept new connection: Too many open files\"
- *SlurmdDebug* fails to log job step information at the appropriate level
- \"Batch JobId=# missing from batch node \<node\> (not found BatchStartTime after startup)\"
- Multi-Instance GPU not working with Slurm and PMIx; GPUs are \"In use by another client\"
- \"srun: error: Unable to accept connection: Resources temporarily unavailable\"
- \"Warning: Note very large processing time\" in *SlurmctldLogFile*
- \"Duplicate entry\" causes slurmdbd to fail
- \"Unable to find plugin: serializer/json\"

### Third Party Integrations

- Can Slurm be used with Globus?
- How can TotalView be configured to operate with Slurm?

## For Management

[**Is Slurm really free?**]{#free}\
Yes, Slurm is free and open source:

- Slurm is free as defined by the https://www.gnu.org/philosophy/free-sw.en.html
- Slurmâ€™s https://github.com/SchedMD/slurm and [documentation](documentation.md) are publicly available under the GNU GPL v2
- Slurm can be https://www.schedmd.com/download-slurm/, used, modified, and redistributed at no monetary cost

[**Why should I use Slurm or other free software?**]{#foss}\
Free software, as with proprietary software, varies widely in quality, but the mechanism itself has proven to be capable of producing high-quality software that is trusted by companies around the world. The Linux kernel is a prominent example, which is often trusted on web servers, infrastructure servers, supercomputers, and mobile devices.

Likewise, Slurm has become a trusted tool in the supercomputing world since its initial release in 2002 and the founding of SchedMD in 2010 to continue developing Slurm. Today, Slurm powers a majority of the https://www.top500.org/ supercomputers. Customers switching from commercial workload managers to Slurm typically report higher scalability, better performance and lower costs.

[**Why should I pay for free software?**]{#support}\
Free software does not mean that it is without cost. Software requires significant time and expertise to write, test, distribute, and maintain. If the software is large and complex, like Slurm or the Linux kernel, these costs can become very substantial.

Slurm is often used for highly important tasks at major computing clusters around the world. Due to the extensive features available and the complexity of the code required to provide those features, many organizations prefer to have experts available to provide tailored recommendations and troubleshooting assistance. While Slurm has a global development community incorporating leading edge technology, https://www.schedmd.com/ personnel have developed most of the code and can provide competitively priced commercial support and on-site training.

[**What does \"Slurm\" stand for?**]{#acronym}\
Nothing.

Originally, \"SLURM\" (completely capitalized) was an acronym for \"Simple Linux Utility for Resource Management\". In 2012 the preferred capitalization was changed to Slurm, and the acronym was dropped --- the developers preferred to think of Slurm as \"sophisticated\" rather than \"Simple\" by this point. And, as Slurm continued to expand it\'s scheduling capabilities, the \"Resource Management\" label was also viewed as outdated.

## For Researchers

[**How should I cite work involving Slurm?**]{#cite}\
We recommend citing the peer-reviewed paper from JSSPP 2023: https://doi.org/10.1007/978-3-031-43943-8_1

    Jette, M.A., Wickberg, T. (2023). Architecture of the Slurm Workload Manager.
    In: KlusÃ¡Äek, D., CorbalÃ¡n, J., Rodrigo, G.P. (eds) Job Scheduling Strategies
    for Parallel Processing. JSSPP 2023. Lecture Notes in Computer Science,
    vol 14283. Springer, Cham. https://doi.org/10.1007/978-3-031-43943-8_1

## For Users

### Designing Jobs

[**How can I run multiple jobs from within a single script?**]{#steps}\
A Slurm job is just a resource allocation. You can execute many job steps within that allocation, either in parallel or sequentially. Some jobs actually launch thousands of job steps this way. The job steps will be allocated nodes that are not already allocated to other job steps. This essentially provides a second level of resource management within the job for the job steps.

[**How can I run a job within an existing job allocation?**]{#multi_batch}\
There is an srun option *\--jobid* that can be used to specify a job\'s ID. For a batch job or within an existing resource allocation, the environment variable *SLURM_JOB_ID* has already been defined, so all job steps will run within that job allocation unless otherwise specified. The one exception to this is when submitting batch jobs. When a batch job is submitted from within an existing batch job, it is treated as a new job allocation request and will get a new job ID unless explicitly set with the *\--jobid* option. If you specify that a batch job should use an existing allocation, that job allocation will be released upon the termination of that batch job.

[**Slurm documentation refers to CPUs, cores and threads. What exactly is considered a CPU?**]{#cpu_count}\
If your nodes are configured with hyperthreading, then a CPU is equivalent to a hyperthread. Otherwise a CPU is equivalent to a core. You can determine if your nodes have more than one thread per core using the command \"scontrol show node\" and looking at the values of \"ThreadsPerCore\".

Note that even on systems with hyperthreading enabled, the resources will generally be allocated to jobs at the level of a core (see NOTE below). Two different jobs will not share a core except through the use of a partition OverSubscribe configuration parameter. For example, a job requesting resources for three tasks on a node with ThreadsPerCore=2 will be allocated two full cores. Note that Slurm commands contain a multitude of options to control resource allocation with respect to base boards, sockets, cores and threads.

(**NOTE**: An exception to this would be if the system administrator configured SelectTypeParameters=CR_CPU and each node\'s CPU count without its socket/core/thread specification. In that case, each thread would be independently scheduled as a CPU. This is not a typical configuration.)

[**How do I run specific tasks on certain nodes in my allocation?**]{#arbitrary}\
One of the distribution methods for srun \'**-m** or **\--distribution**\' is \'arbitrary\'. This means you can tell Slurm to layout your tasks in any fashion you want. For instance if I had an allocation of 2 nodes and wanted to run 4 tasks on the first node and 1 task on the second and my nodes allocated from SLURM_JOB_NODELIST where tux\[0-1\] my srun line would look like this:\
\
*srun -n5 -m arbitrary -w tux\[0,0,0,0,1\] hostname*\
\
If I wanted something similar but wanted the third task to be on tux 1 I could run this:\
\
*srun -n5 -m arbitrary -w tux\[0,0,1,0,0\] hostname*\
\
Here is a simple Perl script named arbitrary.pl that can be ran to easily lay out tasks on nodes as they are in SLURM_JOB_NODELIST.

    #!/usr/bin/perl
    my @tasks = split(',', $ARGV[0]);
    my @nodes = `scontrol show hostnames $SLURM_JOB_NODELIST`;
    my $node_cnt = $#nodes + 1;
    my $task_cnt = $#tasks + 1;

    if ($node_cnt < $task_cnt) {
      print STDERR "ERROR: You only have $node_cnt nodes, but requested layout on $task_cnt nodes.\n";
      $task_cnt = $node_cnt;
    }

    my $cnt = 0;
    my $layout;
    foreach my $task (@tasks) {
      my $node = $nodes[$cnt];
      last if !$node;
      chomp($node);
      for(my $i=0; $i < $task; $i++) {
        $layout .= "," if $layout;
        $layout .= "$node";
      }
      $cnt++;
    }
    print $layout;

We can now use this script in our srun line in this fashion.\
\
*srun -m arbitrary -n5 -w \`arbitrary.pl 4,1\` -l hostname*\
\
This will layout 4 tasks on the first node in the allocation and 1 task on the second node.

[**How can I get the task ID in the output or error file name for a batch job?**]{#batch_out}\
If you want separate output by task, you will need to build a script containing this specification. For example:

    $ cat test
    #!/bin/sh
    echo begin_test
    srun -o out_%j_%t hostname

    $ sbatch -n7 -o out_%j test
    sbatch: Submitted batch job 65541

    $ ls -l out*
    -rw-rw-r--  1 jette jette 11 Jun 15 09:15 out_65541
    -rw-rw-r--  1 jette jette  6 Jun 15 09:15 out_65541_0
    -rw-rw-r--  1 jette jette  6 Jun 15 09:15 out_65541_1
    -rw-rw-r--  1 jette jette  6 Jun 15 09:15 out_65541_2
    -rw-rw-r--  1 jette jette  6 Jun 15 09:15 out_65541_3
    -rw-rw-r--  1 jette jette  6 Jun 15 09:15 out_65541_4
    -rw-rw-r--  1 jette jette  6 Jun 15 09:15 out_65541_5
    -rw-rw-r--  1 jette jette  6 Jun 15 09:15 out_65541_6

    $ cat out_65541
    begin_test

    $ cat out_65541_2
    tdev2

[**How does Slurm establish the environment for my job?**]{#user_env}\
Slurm processes are not run under a shell, but directly exec\'ed by the *slurmd* daemon (assuming *srun* is used to launch the processes). The environment variables in effect at the time the *srun* command is executed are propagated to the spawned processes. The *\~/.profile* and *\~/.bashrc* scripts are not executed as part of the process launch. You can also look at the *\--export* option of srun and sbatch. See man pages for details.

[**Can the *make* command utilize the resources allocated to a Slurm job?**]{#parallel_make}\
Yes. There is a patch available for GNU make version 3.81 available as part of the Slurm distribution in the file *contribs/make-3.81.slurm.patch*. For GNU make version 4.0 you can use the patch in the file *contribs/make-4.0.slurm.patch*. This patch will use Slurm to launch tasks across a job\'s current resource allocation. Depending upon the size of modules to be compiled, this may or may not improve performance. If most modules are thousands of lines long, the use of additional resources should more than compensate for the overhead of Slurm\'s task launch. Use with make\'s *-j* option within an existing Slurm allocation. Outside of a Slurm allocation, make\'s behavior will be unchanged.

[**How can I run an Ansys program with Slurm?**]{#ansys}\
If you are talking about an interactive run of the Ansys app, then you can use this simple script (it is for Ansys Fluent):

    $ cat ./fluent-srun.sh
    #!/usr/bin/env bash
    HOSTSFILE=.hostlist-job$SLURM_JOB_ID
    if [ "$SLURM_PROCID" == "0" ]; then
        srun hostname -f > $HOSTSFILE
        fluent -t $SLURM_NTASKS -cnf=$HOSTSFILE -ssh 3d
        rm -f $HOSTSFILE
    fi
    exit 0

To run an interactive session, use srun like this:

    $ srun -n <tasks> ./fluent-srun.sh

### Submitting Jobs

[**Why are my srun options ignored?**]{#opts}\
Everything after the command [srun]{.commandline} is examined to determine if it is a valid option for srun. The first token that is not a valid option for srun is considered the command to execute and everything after that is treated as an option to the command. For example:

> [srun -N2 uptime -pdebug]{.commandline}

srun processes \"-N2\" as an option to itself. \"uptime\" is the command to execute and \"-pdebug\" is treated as an option to the uptime command. Depending on the command and options provided, you may get an invalid option message or unexpected behavior if the options happen to be valid.

Options for srun should appear before the command to be run:

> [srun -N2 -pdebug uptime]{.commandline}

[**Why does the srun \--overcommit option not permit multiple jobs to run on nodes?**]{#sharing}\
The **\--overcommit** option is a means of indicating that a job or job step is willing to execute more than one task per processor in the job\'s allocation. For example, consider a cluster of two processor nodes. The srun execute line may be something of this sort

> [srun \--ntasks=4 \--nodes=1 a.out]{.commandline}

This will result in not one, but two nodes being allocated so that each of the four tasks is given its own processor. Note that the srun **\--nodes** option specifies a minimum node count and optionally a maximum node count. A command line of

> [srun \--ntasks=4 \--nodes=1-1 a.out]{.commandline}

would result in the request being rejected. If the **\--overcommit** option is added to either command line, then only one node will be allocated for all four tasks to use.

More than one job can execute simultaneously on the same compute resource (e.g. CPU) through the use of srun\'s **\--oversubscribe** option in conjunction with the **OverSubscribe** parameter in Slurm\'s partition configuration. See the man pages for srun and slurm.conf for more information.

[**Why is the srun \--u/\--unbuffered option adding a carriage character return to my output?**]{#unbuffered_cr}\
The libc library used by many programs internally buffers output rather than writing it immediately. This is done for performance reasons. The only way to disable this internal buffering is to configure the program to write to a pseudo terminal (PTY) rather than to a regular file. This configuration causes [some]{.underline} implementations of libc to prepend the carriage return character before all line feed characters. Removing the carriage return character would result in desired formatting in some instances, while causing bad formatting in other cases. In any case, Slurm is not adding the carriage return character, but displaying the actual program\'s output.

[**What is the difference between the sbatch and srun commands?**]{#sbatch_srun}\
The srun command has two different modes of operation. First, if not run within an existing job (i.e. not within a Slurm job allocation created by salloc or sbatch), then it will create a job allocation and spawn an application. If run within an existing allocation, the srun command only spawns the application. For this question, we will only address the first mode of operation and compare creating a job allocation using the sbatch and srun commands.

The srun command is designed for interactive use, with someone monitoring the output. The output of the application is seen as output of the srun command, typically at the user\'s terminal. The sbatch command is designed to submit a script for later execution and its output is written to a file. Command options used in the job allocation are almost identical. The most noticeable difference in options is that the sbatch command supports the concept of [job arrays](job_array.md), while srun does not. Another significant difference is in fault tolerance. Failures involving sbatch jobs typically result in the job being requeued and executed again, while failures involving srun typically result in an error message being generated with the expectation that the user will respond in an appropriate fashion.

[**Can tasks be launched with a remote (pseudo) terminal?**]{#terminal}\
The best method is to use `salloc` with **use_interactive_step** set in the **LaunchParameters** option in *slurm.conf*. See getting shell prompts in interactive mode.

[**How can I get shell prompts in interactive mode?**]{#prompt}\
Starting in 20.11, the recommended way to get an interactive shell prompt is to configure **use_interactive_step** in *slurm.conf*:

    LaunchParameters=use_interactive_step

This configures `salloc` to automatically launch an interactive shell via `srun` on a node in the allocation whenever `salloc` is called without a program to execute.

By default, **use_interactive_step** creates an *interactive step* on a node in the allocation and runs the shell in that step. An interactive step is to an interactive shell what a batch step is to a batch script - both have access to all resources in the allocation on the node they are running on, but do not \"consume\" them.

Note that beginning in 20.11, steps created by srun are now exclusive. This means that the previously-recommended way to get an interactive shell, [srun \--pty \$SHELL]{.commandline}, will no longer work, as the shell\'s step will now consume all resources on the node and cause subsequent [srun]{.commandline} calls to pend.

An alternative but not recommended method is to make use of srun\'s *\--pty* option, (e.g. *srun \--pty bash -i*). Srun\'s *\--pty* option runs task zero in pseudo terminal mode. Bash\'s *-i* option instructs it to run in interactive mode (with prompts). However, unlike the batch or interactive steps, this launches a step which consumes all resources in the job. This means that subsequent steps cannot be launched in the job unless they use the *\--overlap* option. If task plugins are configured, the shell is limited to CPUs of the first task. Subsequent steps (which must be launched with *\--overlap*) may be limited to fewer resources than expected or may fail to launch tasks altogether if multiple nodes were requested. Therefore, this alternative should rarely be used; `salloc` should be used instead.

[**Can Slurm export an X11 display on an allocated compute node?**]{#x11}\
You can use the X11 builtin feature starting at version 17.11. It is enabled by setting *PrologFlags=x11* in *slurm.conf*. Other X11 plugins must be deactivated.\
Run it as shown:

    $ ssh -X user@login1
    $ srun -n1 --pty --x11 xclock

An alternative for older versions is to build and install an optional SPANK plugin for that functionality. Instructions to build and install the plugin follow. This SPANK plugin will not work if used in combination with native X11 support so you must disable it compiling Slurm with *\--disable-x11*. This plugin relies on openssh library and it provides features such as GSSAPI support.\
Update the Slurm installation path as needed:

    # It may be obvious, but don't forget the -X on ssh
    $ ssh -X alex@testserver.com

    # Get the plugin
    $ mkdir git
    $ cd git
    $ git clone https://github.com/hautreux/slurm-spank-x11.git
    $ cd slurm-spank-x11

    # Manually edit the X11_LIBEXEC_PROG macro definition
    $ vi slurm-spank-x11.c
    $ vi slurm-spank-x11-plug.c
    $ grep "define X11_" slurm-spank-x11.c
    #define X11_LIBEXEC_PROG "/opt/slurm/17.02/libexec/slurm-spank-x11"
    $ grep "define X11_LIBEXEC_PROG" slurm-spank-x11-plug.c
    #define X11_LIBEXEC_PROG "/opt/slurm/17.02/libexec/slurm-spank-x11"


    # Compile
    $ gcc -g -o slurm-spank-x11 slurm-spank-x11.c
    $ gcc -g -I/opt/slurm/17.02/include -shared -fPIC -o x11.so slurm-spank-x11-plug.c

    # Install
    $ mkdir -p /opt/slurm/17.02/libexec
    $ install -m 755 slurm-spank-x11 /opt/slurm/17.02/libexec
    $ install -m 755 x11.so /opt/slurm/17.02/lib/slurm

    # Configure
    $ echo -e "optional x11.so" >> /opt/slurm/17.02/etc/plugstack.conf
    $ cd ~/tests

    # Run
    $ srun -n1 --pty --x11 xclock
    alex@node1's password:

### Scheduling

[**Why is my job not running?**]{#pending}\
The answer to this question depends on a lot of factors. The main one is which scheduler is used by Slurm. Executing the command

> [scontrol show config \| grep SchedulerType]{.commandline}

will supply this information. If the scheduler type is **builtin**, then jobs will be executed in the order of submission for a given partition. Even if resources are available to initiate your job immediately, it will be deferred until no previously submitted job is pending. If the scheduler type is **backfill**, then jobs will generally be executed in the order of submission for a given partition with one exception: later submitted jobs will be initiated early if doing so does not delay the expected execution time of an earlier submitted job. In order for backfill scheduling to be effective, users\' jobs should specify reasonable time limits. If jobs do not specify time limits, then all jobs will receive the same time limit (that associated with the partition), and the ability to backfill schedule jobs will be limited. The backfill scheduler does not alter job specifications of required or excluded nodes, so jobs which specify nodes will substantially reduce the effectiveness of backfill scheduling. See the backfill section for more details. For any scheduler, you can check priorities of jobs using the command [scontrol show job]{.commandline}. Other reasons can include waiting for resources, memory, qos, reservations, etc. As a guideline, issue an [scontrol show job \<jobid\>]{.commandline} and look at the field *State* and *Reason* to investigate the cause. A full list and explanation of the different Reasons can be found in the [resource limits](resource_limits.md#reasons) page.

[**Why is the Slurm backfill scheduler not starting my job?**]{#backfill}\
The most common problem is failing to set job time limits. If all jobs have the same time limit (for example the partition\'s time limit), then backfill will not be effective. Note that partitions can have both default and maximum time limits, which can be helpful in configuring a system for effective backfill scheduling.

In addition, there are a multitude of backfill scheduling parameters which can impact which jobs are considered for backfill scheduling, such as the maximum number of jobs tested per user. For more information see the slurm.conf man page and check the configuration of SchedulerParameters on your system.

### Killed Jobs

[**Why is my job killed prematurely?**]{#purge}\
Slurm has a job purging mechanism to remove inactive jobs (resource allocations) before reaching its time limit, which could be infinite. This inactivity time limit is configurable by the system administrator. You can check its value with the command

> [scontrol show config \| grep InactiveLimit]{.commandline}

The value of InactiveLimit is in seconds. A zero value indicates that job purging is disabled. A job is considered inactive if it has no active job steps or if the srun command creating the job is not responding. In the case of a batch job, the srun command terminates after the job script is submitted. Therefore batch job pre- and post-processing is limited to the InactiveLimit. Contact your system administrator if you believe the InactiveLimit value should be changed.

[**Why is my batch job that launches no job steps being killed?**]{#inactive}\
Slurm has a configuration parameter *InactiveLimit* intended to kill jobs that do not spawn any job steps for a configurable period of time. Your system administrator may modify the *InactiveLimit* to satisfy your needs. Alternately, you can just spawn a job step at the beginning of your script to execute in the background. It will be purged when your script exits or your job otherwise terminates. A line of this sort near the beginning of your script should suffice:\
*srun -N1 -n1 sleep 999999 &*

[**What does \"srun: Force Terminated job\" indicate?**]{#force}\
The srun command normally terminates when the standard output and error I/O from the spawned tasks end. This does not necessarily happen at the same time that a job step is terminated. For example, a file system problem could render a spawned task non-killable at the same time that I/O to srun is pending. Alternately a network problem could prevent the I/O from being transmitted to srun. In any event, the srun command is notified when a job step is terminated, either upon reaching its time limit or being explicitly killed. If the srun has not already terminated, the message \"srun: Force Terminated job\" is printed. If the job step\'s I/O does not terminate in a timely fashion thereafter, pending I/O is abandoned and the srun command exits.

[**What does this mean: \"srun: First task exited 30s ago\" followed by \"srun Job Failed\"?**]{#early_exit}\
The srun command monitors when tasks exit. By default, 30 seconds after the first task exits, the job is killed. This typically indicates some type of job failure and continuing to execute a parallel job when one of the tasks has exited is not normally productive. This behavior can be changed using srun\'s *\--wait=\<time\>* option to either change the timeout period or disable the timeout altogether. See srun\'s man page for details.

### Managing Jobs

[**How can I temporarily prevent a job from running (e.g. place it into a *hold* state)?**]{#hold}\
The easiest way to do this is to change a job\'s earliest begin time (optionally set at job submit time using the *\--begin* option). The example below places a job into hold state (preventing its initiation for 30 days) and later permitting it to start now.

    $ scontrol update JobId=1234 StartTime=now+30days
    ... later ...
    $ scontrol update JobId=1234 StartTime=now

[**Can I change my job\'s size after it has started running?**]{#job_size}\
Slurm supports the ability to decrease the size of jobs. Requesting fewer hardware resources, and changing partition, qos, reservation, licenses, etc. is only allowed for pending jobs.

Use the *scontrol* command to change a job\'s size either by specifying a new node count (*NumNodes=*) for the job or identify the specific nodes (*NodeList=*) that you want the job to retain. Any job steps running on the nodes which are relinquished by the job will be killed unless initiated with the *\--no-kill* option. After the job size is changed, some environment variables created by Slurm containing information about the job\'s environment will no longer be valid and should either be removed or altered (e.g. SLURM_JOB_NUM_NODES, SLURM_JOB_NODELIST and SLURM_NTASKS). The *scontrol* command will generate a script that can be executed to reset local environment variables. You must retain the SLURM_JOB_ID environment variable in order for the *srun* command to gather information about the job\'s current state and specify the desired node and/or task count in subsequent *srun* invocations. A new accounting record is generated when a job is resized, showing the job to have been resubmitted and restarted at the new size. An example is shown below.

    #!/bin/bash
    srun my_big_job
    scontrol update JobId=$SLURM_JOB_ID NumNodes=2
    . slurm_job_${SLURM_JOB_ID}_resize.sh
    srun -N2 my_small_job
    rm slurm_job_${SLURM_JOB_ID}_resize.*

[**Why does squeue (and \"scontrol show jobid\") sometimes not display a job\'s estimated start time?**]{#estimated_start_time}\
When the backfill scheduler is configured, it provides an estimated start time for jobs that are candidates for backfill. Pending jobs with dependencies will not have an estimate as it is difficult to predict what resources will be available when the jobs they are dependent on terminate. Also note that the estimate is better for jobs expected to start soon, as most running jobs end before their estimated time. There are other restrictions on backfill that may apply. See the backfill section for more details.

[**Can squeue output be color coded?**]{#squeue_color}\
The squeue command output is not color coded, but other tools can be used to add color. One such tool is ColorWrapper (https://github.com/rrthomas/cw). A sample ColorWrapper configuration file and output are shown below.

    path /bin:/usr/bin:/sbin:/usr/sbin:<env>
    usepty
    base green+
    match red:default (Resources)
    match black:default (null)
    match black:cyan N/A
    regex cyan:default  PD .*$
    regex red:default ^\d*\s*C .*$
    regex red:default ^\d*\s*CG .*$
    regex red:default ^\d*\s*NF .*$
    regex white:default ^JOBID.*

![](https://slurm.schedmd.com/squeue_color.png){width="600"}

[**Why is my job/node in a COMPLETING state?**]{#comp}\
When a job is terminating, both the job and its nodes enter the COMPLETING state. As the Slurm daemon on each node determines that all processes associated with the job have terminated, that node changes state to IDLE or some other appropriate state for use by other jobs. When every node allocated to a job has determined that all processes associated with it have terminated, the job changes state to COMPLETED or some other appropriate state (e.g. FAILED). Normally, this happens within a second. However, if the job has processes that cannot be terminated with a SIGKILL signal, the job and one or more nodes can remain in the COMPLETING state for an extended period of time. This may be indicative of processes hung waiting for a core file to complete I/O or operating system failure. If this state persists, the system administrator should check for processes associated with the job that cannot be terminated then use the [scontrol]{.commandline} command to change the node\'s state to DOWN (e.g. \"scontrol update NodeName=*name* State=DOWN Reason=hung_completing\"), reboot the node, then reset the node\'s state to IDLE (e.g. \"scontrol update NodeName=*name* State=RESUME\"). Note that setting the node DOWN will terminate all running or suspended jobs associated with that node. An alternative is to set the node\'s state to DRAIN until all jobs associated with it terminate before setting it DOWN and re-booting.

Note that Slurm has two configuration parameters that may be used to automate some of this process. *UnkillableStepProgram* specifies a program to execute when non-killable processes are identified. *UnkillableStepTimeout* specifies how long to wait for processes to terminate. See the \"man slurm.conf\" for more information about these parameters.

[**How can a job in a complete or failed state be requeued?**]{#req}\
Slurm supports requeuing jobs in a done or failed state. Use the command:

**scontrol requeue job_id**

The job will then be requeued back in the PENDING state and scheduled again. See man(1) scontrol.

Consider a simple job like this:

    $cat zoppo
    #!/bin/sh
    echo "hello, world"
    exit 10

    $sbatch -o here ./zoppo
    Submitted batch job 10

The job finishes in FAILED state because it exits with a non zero value. We can requeue the job back to the PENDING state and the job will be dispatched again.

    $ scontrol requeue 10
    $ squeue
          JOBID PARTITION  NAME     USER   ST   TIME  NODES NODELIST(REASON)
          10      mira    zoppo    david  PD   0:00    1   (NonZeroExitCode)
    $ squeue
        JOBID PARTITION   NAME     USER ST     TIME  NODES NODELIST(REASON)
          10      mira    zoppo    david  R    0:03    1      alanz1

Slurm supports requeuing jobs in a hold state with the command:

**scontrol requeuehold job_id**

The job can be in state RUNNING, SUSPENDED, COMPLETED or FAILED before being requeued.

    $ scontrol requeuehold 10
    $ squeue
        JOBID PARTITION  NAME     USER ST       TIME  NODES NODELIST(REASON)
        10      mira    zoppo    david PD       0:00      1 (JobHeldUser)

[**Why is sview not coloring/highlighting nodes properly?**]{#sview_colors}\
sview color-coding is affected by the GTK theme. The node status grid is made up of button widgets and certain GTK themes don\'t show the color setting as desired. Changing GTK themes can restore proper color-coding.

[**Why is my MPICH2 or MVAPICH2 job not running with Slurm? Why does the DAKOTA program not run with Slurm?**]{#mpi_symbols}\
The Slurm library used to support MPICH2 or MVAPICH2 references a variety of symbols. If those symbols resolve to functions or variables in your program rather than the appropriate library, the application will fail. For example http://dakota.sandia.gov/, versions 5.1 and older, contains a function named regcomp, which will get used rather than the POSIX regex functions. Rename DAKOTA\'s function and references from regcomp to something else to make it work properly.

### Resource Limits

[**Why are my resource limits not propagated?**]{#rlimit}\
When the [srun]{.commandline} command executes, it captures the resource limits in effect at submit time on the node where srun executes. These limits are propagated to the allocated nodes before initiating the user\'s job. The Slurm daemons running on the allocated nodes then try to establish identical resource limits for the job being initiated. There are several possible reasons for not being able to establish those resource limits.

- The hard resource limits applied to Slurm\'s slurmd daemon are lower than the user\'s soft resources limits on the submit host. Typically the slurmd daemon is initiated by the init daemon with the operating system default limits. This may be addressed either through use of the ulimit command in the /etc/sysconfig/slurm file or enabling PAM in Slurm.
- The user\'s hard resource limits on the allocated node are lower than the same user\'s soft hard resource limits on the node from which the job was submitted. It is recommended that the system administrator establish uniform hard resource limits for users on all nodes within a cluster to prevent this from occurring.
- PropagateResourceLimits or PropagateResourceLimitsExcept parameters are configured in slurm.conf and avoid propagation of specified limits.

**NOTE**: This may produce the error message \"Can\'t propagate RLIMIT\_\...\". The error message is printed only if the user explicitly specifies that the resource limit should be propagated or the srun command is running with verbose logging of actions from the slurmd daemon (e.g. \"srun -d6 \...\").

[**Why are jobs not getting the appropriate memory limit?**]{#mem_limit}\
This is probably a variation on the locked memory limit problem described above. Use the same solution for the AS (Address Space), RSS (Resident Set Size), or other limits as needed.

[**Why is my MPI job failing due to the locked memory (memlock) limit being too low?**]{#memlock}\
By default, Slurm propagates all of your resource limits at the time of job submission to the spawned tasks. This can be disabled by specifically excluding the propagation of specific limits in the *slurm.conf* file. For example *PropagateResourceLimitsExcept=MEMLOCK* might be used to prevent the propagation of a user\'s locked memory limit from a [login node](quickstart_admin.md#login) to a dedicated node used for his parallel job. If the user\'s resource limit is not propagated, the limit in effect for the *slurmd* daemon will be used for the spawned job. A simple way to control this is to ensure that user *root* has a sufficiently large resource limit and ensuring that *slurmd* takes full advantage of this limit. For example, you can set user root\'s locked memory limit ulimit to be unlimited on the compute nodes (see *\"man limits.conf\"*) and ensuring that *slurmd* takes full advantage of this limit (e.g. by adding *\"LimitMEMLOCK=infinity\"* to your systemd\'s *slurmd.service* file). It may also be desirable to lock the slurmd daemon\'s memory to help ensure that it keeps responding if memory swapping begins. A sample */etc/sysconfig/slurm* which can be read from systemd is shown below. Related information about PAM is also available.

    #
    # Example /etc/sysconfig/slurm
    #
    # Memlocks the slurmd process's memory so that if a node
    # starts swapping, the slurmd will continue to respond
    SLURMD_OPTIONS="-M"

## For Administrators

### Test Environments

[**Can multiple Slurm systems be run in parallel for testing purposes?**]{#multi_slurm}\
Yes, this is a great way to test new versions of Slurm. Just install the test version in a different location with a different *slurm.conf*. The test system\'s *slurm.conf* should specify different pathnames and port numbers to avoid conflicts. The only problem is if more than one version of Slurm is configured with *burst_buffer/\** plugins or others that may interact with external system APIs. In that case, there can be conflicting API requests from the different Slurm systems. This can be avoided by configuring the test system with *burst_buffer/none*.

[**Can Slurm emulate a larger cluster?**]{#multi_slurmd}\
Yes, this can be useful for testing purposes. It has also been used to partition \"fat\" nodes into multiple Slurm nodes. There are two ways to do this. The best method for most conditions is to run one *slurmd* daemon per emulated node in the cluster as follows.

1.  When executing the *configure* program, use the option *\--enable-multiple-slurmd* (or add that option to your *\~/.rpmmacros* file).
2.  Build and install Slurm in the usual manner.
3.  In *slurm.conf* define the desired node names (arbitrary names used only by Slurm) as *NodeName* along with the actual address of the physical node in *NodeHostname*. Multiple *NodeName* values can be mapped to a single *NodeHostname*. Note that each *NodeName* on a single physical node needs to be configured to use a different port number (set *Port* to a unique value on each line for each node). You will also want to use the \"%n\" symbol in slurmd related path options in slurm.conf (*SlurmdLogFile* and *SlurmdPidFile*).
4.  When starting the *slurmd* daemon, include the *NodeName* of the node that it is supposed to serve on the execute line (e.g. \"slurmd -N hostname\").
5.  This is an example of the *slurm.conf* file with the emulated nodes and ports configuration. Any valid value for the CPUs, memory or other valid node resources can be specified.

<!-- -->

    NodeName=dummy26[1-100] NodeHostName=achille Port=[6001-6100] NodeAddr=127.0.0.1 CPUs=4 RealMemory=6000
    PartitionName=mira Default=yes Nodes=dummy26[1-100]

See the [Programmers Guide](programmer_guide.md#multiple_slurmd_support) for more details about configuring multiple slurmd support.

[**Can Slurm emulate nodes with more resources than physically exist on the node?**]{#extra_procs}\
Yes. In the slurm.conf file, configure *SlurmdParameters=config_overrides* and specify any desired node resource specifications (*CPUs*, *Sockets*, *CoresPerSocket*, *ThreadsPerCore*, and/or *TmpDisk*). Slurm will use the resource specification for each node that is given in *slurm.conf* and will not check these specifications against those actually found on the node. The system would best be configured with *TaskPlugin=task/none*, so that launched tasks can run on any available CPU under operating system control.

### Build and Install

[**Why aren\'t pam_slurm.so, auth_none.so, or other components in a Slurm RPM?**]{#rpm}\
It is possible that at build time the required dependencies for building the library are missing. If you want to build the library then install pam-devel and compile again. See the file slurm.spec in the Slurm distribution for a list of other options that you can specify at compile time with rpmbuild flags and your *rpmmacros* file.

The auth_none plugin is in a separate RPM and not built by default. Using the auth_none plugin means that Slurm communications are not authenticated, so you probably do not want to run in this mode of operation except for testing purposes. If you want to build the auth_none RPM then add *\--with auth_none* on the rpmbuild command line or add *%\_with_auth_none* to your \~/rpmmacros file. See the file slurm.spec in the Slurm distribution for a list of other options.

[**How can I build Slurm with debugging symbols?**]{#debug}\
When configuring, run the configure script with *\--enable-developer* option. That will provide asserts, debug messages and the *-Werror* flag, that will in turn activate *\--enable-debug*.\
With the *\--enable-debug* flag, the code will be compiled with *-ggdb3* and *-g -O1 -fno-strict-aliasing* flags that will produce extra debugging information. Another possible option to use is *\--disable-optimizations* that will set *-O0*. See also *auxdir/x_ac_debug.m4* for more details.

[**How can a patch file be generated from a Slurm commit in GitHub?**]{#git_patch}\
Find and open the commit in GitHub then append \".patch\" to the URL and save the resulting file. For an example, see: https://github.com/SchedMD/slurm/commit/91e543d433bed11e0df13ce0499be641774c99a3.patch

[**How can I apply a patch to my Slurm source?**]{#apply_patch}\
If you have a patch file that you need to apply to your source, such as a security or bug fix patch supplied by SchedMD\'s support, you can do so with the **patch** command. You would first extract the contents of the source tarball for the version you are using. You can then apply the patch to the extracted source. Below is an example of how to do this with the source for Slurm 23.11.1:

    $ tar xjvf slurm-23.11.1.tar.bz2 > /dev/null
    $ patch -p1 -d slurm-23.11.1/ < example.patch
    patching file src/slurmctld/step_mgr.c

Once the patch has been applied to the source code, you can proceed to build Slurm as you would normally if you build with **make**. If you use **rpmbuild** to build Slurm, you will have to create a tarball with the patched files. The filename of the tarball must match the original filename to avoid errors.

    $ tar cjvf slurm-23.11.1.tar.bz2 slurm-23.11.1/ > /dev/null
    $ rpmbuild -ta slurm-23.11.1.tar.bz2 > /dev/null

Alternatively, as of Slurm 24.11.0 when using **rpmbuild**, a patched package may be created directly by placing the patch file in the same directory as the source tarball and executing the following command:

    $ rpmbuild -ta --define 'patch security.patch' slurm-24.11.0.tar.bz2

[**Why am I being offered an automatic update for Slurm?**]{#epel}\
EPEL has added Slurm packages to their repository to make them more widely available to the Linux community. However, this packaged version is not supported or maintained by SchedMD, and is not recommend for customers at this time. If you are using the EPEL repo you could be offered an update for Slurm that you may not anticipate. In order to prevent Slurm from being upgraded unintentionally, we recommend you modify the EPEL repository configuration file to exclude all Slurm packages from automatic updates.

    exclude=slurm*

### Cluster Management

[**How should I relocate the primary or backup controller?**]{#controller}\
If the cluster\'s computers used for the primary or backup controller will be out of service for an extended period of time, it may be desirable to relocate them. In order to do so, follow this procedure:

1.  (Slurm 23.02 and older) Drain the cluster of running jobs
2.  Stop all Slurm daemons
3.  Modify the *SlurmctldHost* values in the *slurm.conf* file
4.  Distribute the updated *slurm.conf* file to all nodes
5.  Copy the *StateSaveLocation* directory to the new host and make sure the permissions allow the *SlurmUser* to read and write it.
6.  Restart all Slurm daemons

Starting with Slurm 23.11, jobs that were started by the old controller will receive the updated controller address and will continue and finish normally. On older versions, jobs started by the old controller will still try to report back to the older controller. In both cases, there should be no loss of any pending jobs. Ensure that any nodes added to the cluster have a current *slurm.conf* file installed.

**CAUTION:** If two nodes are simultaneously configured as the primary controller (two nodes on which *SlurmctldHost* specify the local host and the *slurmctld* daemon is executing on each), system behavior will be destructive. If a compute node has an incorrect *SlurmctldHost* parameter, that node may be rendered unusable, but no other harm will result.

[**Do I need to maintain synchronized clocks on the cluster?**]{#clock}\
In general, yes. Having inconsistent clocks may cause nodes to be unusable and generate errors in Slurm log files regarding expired credentials. For example:

    error: Munge decode failed: Expired credential
    ENCODED: Wed May 12 12:34:56 2008
    DECODED: Wed May 12 12:01:12 2008

[**How can I stop Slurm from scheduling jobs?**]{#stop_sched}\
You can stop Slurm from scheduling jobs on a per partition basis by setting that partition\'s state to DOWN. Set its state UP to resume scheduling. For example:

    $ scontrol update PartitionName=foo State=DOWN
    $ scontrol update PartitionName=bar State=UP

[**How can I dry up the workload for a maintenance period?**]{#maint_time}\
Create a resource reservation as described in Slurm\'s [Resource Reservation Guide](reservations.md).

[**What should I be aware of when upgrading Slurm?**]{#upgrade}\
Refer to the [Upgrade Guide](upgrades.md) for details.

[**Is there anything exceptional to be aware of when upgrading my database server?**]{#db_upgrade}\
Generally, no. Special cases are noted in the [Database server](upgrades.md#db_server) section of the Upgrade Guide.

[**When adding a new cluster, how can the Slurm cluster configuration be copied from an existing cluster to the new cluster?**]{#cluster_acct}\
Accounts need to be configured for the cluster. An easy way to copy information from an existing cluster is to use the sacctmgr command to dump that cluster\'s information, modify it using some editor, the load the new information using the sacctmgr command. See the sacctmgr man page for details, including an example.

[**How could some jobs submitted immediately before the slurmctld daemon crashed be lost?**]{#state_info}\
Any time the slurmctld daemon or hardware fails before state information reaches disk can result in lost state. Slurmctld writes state frequently (every five seconds by default), but with large numbers of jobs, the formatting and writing of records can take seconds and recent changes might not be written to disk. Another example is if the state information is written to file, but that information is cached in memory rather than written to disk when the node fails. The interval between state saves being written to disk can be configured at build time by defining SAVE_MAX_WAIT to a different value than five.

[**Is resource limit propagation useful on a homogeneous cluster?**]{#limit_propagation}\
Resource limit propagation permits a user to modify resource limits and submit a job with those limits. By default, Slurm automatically propagates all resource limits in effect at the time of job submission to the tasks spawned as part of that job. System administrators can utilize the *PropagateResourceLimits* and *PropagateResourceLimitsExcept* configuration parameters to change this behavior. Users can override defaults using the *srun \--propagate* option. See *\"man slurm.conf\"* and *\"man srun\"* for more information about these options.

[**Why are the resource limits set in the database not being enforced?**]{#enforce_limits}\
In order to enforce resource limits, set the value of **AccountingStorageEnforce** in each cluster\'s slurm.conf configuration file appropriately. If **AccountingStorageEnforce** does not contains an option of \"limits\", then resource limits will not be enforced on that cluster. See [Resource Limits](resource_limits.md) for more information.

[**Can Slurm be configured to manage licenses?**]{#licenses}\
Slurm does not provide a native integration with third party license managers, but it does provide for the allocation of global resources called licenses. Use the Licenses configuration parameter in your slurm.conf file (e.g. \"Licenses=foo:10,bar:20\"). Jobs can request licenses and be granted exclusive use of those resources (e.g. \"sbatch \--licenses=foo:2,bar:1 \...\"). It is not currently possible to change the total number of licenses on a system without restarting the slurmctld daemon, but it is possible to dynamically reserve licenses and remove them from being available to jobs on the system (e.g. \"scontrol update reservation=licenses_held licenses=foo:5,bar:2\"). For more information see the [Licenses Guide](licenses.md).

[**How easy is it to switch from PBS or Torque to Slurm?**]{#torque}\
A lot of users don\'t even notice the difference. Slurm has wrappers available for the mpiexec, pbsnodes, qdel, qhold, qrls, qstat, and qsub commands (see contribs/torque in the distribution and the \"slurm-torque\" RPM). There is also a wrapper for the showq command at https://github.com/pedmon/slurm_showq.

Slurm recognizes and translates the \"#PBS\" options in batch scripts. Most, but not all options are supported.

Slurm also includes a SPANK plugin that will set all of the PBS environment variables based upon the Slurm environment (e.g. PBS_JOBID, PBS_JOBNAME, PBS_WORKDIR, etc.). One environment not set by PBS_ENVIRONMENT, which if set would result in the failure of some MPI implementations. The plugin will be installed in\
\<install_directory\>/lib/slurm/spank_pbs.so\
See the SPANK man page for configuration details.

[**What might account for MPI performance being below the expected level?**]{#mpi_perf}\
Starting the slurmd daemons with limited locked memory can account for this. Adding the line \"ulimit -l unlimited\" to the */etc/sysconfig/slurm* file can fix this.

[**How do I safely remove partitions?**]{#delete_partition}\
Partitions should be removed using the \"scontrol delete PartitionName=\<partition\>\" command. This is because scontrol will prevent any partitions from being removed that are in use. Partitions need to be removed from the slurm.conf after being removed using scontrol or they will return after a restart. An existing job\'s partition(s) can be updated with the \"scontrol update JobId=\<jobid\> Partition=\<partition(s)\>\" command. Removing a partition from the slurm.conf and restarting will cancel any existing jobs that reference the removed partitions.

[**How can a routing queue be configured?**]{#routing_queue}\
A job submit plugin is designed to have access to a job request from a user, plus information about all of the available system partitions/queue. An administrator can write a C plugin or LUA script to set an incoming job\'s partition based upon its size, time limit, etc. See the [Job Submit Plugin API](job_submit_plugins.md) guide for more information. Also see the available job submit plugins distributed with Slurm for examples (look in the \"src/plugins/job_submit\" directory).

[**What happened to the \"none\" plugins?**]{#none_plugins}\
In Slurm 23.02 and earlier, several parameters had a plugin named \"none\" that would essentially disable the setting. In version 23.11, those plugins named \"none\" were removed. To disable a setting you just need to leave it unset. If you still have a plugin defined as \"none\", Slurm will still recognize it and treat it as though it was unset. Parameters that previously had a \"none\" plugin are:

- AccountingStorageType
- AcctGatherEnergyType
- AcctGatherInterconnectType
- AcctGatherFilesystemType
- AcctGatherProfileType
- CliFilterPlugins
- CoreSpecPlugin
- ExtSensorsType
- JobAcctGatherType
- JobCompType
- JobContainerType
- MCSPlugin
- MpiDefault
- PowerParameters
- PreemptType
- PrioritySiteFactorPlugin
- SwitchType
- TaskPlugin
- TopologyPlugin

### Accounting Database

[**Why should I use the slurmdbd instead of the regular database plugins?**]{#slurmdbd}\
While the normal storage plugins will work fine without the added layer of the slurmdbd there are some great benefits to using the slurmdbd.

1.  Added security. Using the slurmdbd you can have an authenticated connection to the database.
2.  Offloading processing from the controller. With the slurmdbd there is no slowdown to the controller due to a slow or overloaded database.
3.  Keeping enterprise wide accounting from all Slurm clusters in one database. The slurmdbd is multi-threaded and designed to handle all the accounting for the entire enterprise.
4.  With the database plugins you can query with sacct accounting stats from any node Slurm is installed on. With the slurmdbd you can also query any cluster using the slurmdbd from any other cluster\'s nodes. Other tools like sreport are also available.

[**How critical is configuring high availability for my database?**]{#ha_db}

- Consider if you really need a high-availability MySQL setup. A short outage of slurmdbd is not a problem, because slurmctld will store all data in memory and send it to slurmdbd when it resumes operations. The slurmctld daemon will also cache all user limits and fair share information.
- You cannot use NDB, since SlurmDBD\'s MySQL implementation uses keys on BLOB values (and potentially other features on the incompatibility list).
- You can set up \"classical\" Linux HA, with heartbeat/corosync to migrate IP between primary/backup mysql servers and:
  - Configure one way replication of mysql, and change primary/backup roles on failure
  - Use shared storage for primary/backup mysql servers database, and start backup on primary mysql failure.

[**How can I use double quotes in MySQL queries?**]{#sql}\
Execute:

    SET session sql_mode='ANSI_QUOTES';

This will allow double quotes in queries like this:

    show columns from "tux_assoc_table" where Field='is_def';

### Compute Nodes (slurmd)

[**Why is a node shown in state DOWN when the node has registered for service?**]{#return_to_service}\
The configuration parameter *ReturnToService* in *slurm.conf* controls how DOWN nodes are handled. Set its value to one in order for DOWN nodes to automatically be returned to service once the *slurmd* daemon registers with a valid node configuration. A value of zero is the default and results in a node staying DOWN until an administrator explicitly returns it to service using the command \"scontrol update NodeName=whatever State=RESUME\". See \"man slurm.conf\" and \"man scontrol\" for more details.

[**What happens when a node crashes?**]{#down_node}\
A node is set DOWN when the slurmd daemon on it stops responding for *SlurmdTimeout* as defined in *slurm.conf*. The node can also be set DOWN when certain errors occur or the node\'s configuration is inconsistent with that defined in *slurm.conf*. Any active job on that node will be killed unless it was submitted with the srun option *\--no-kill*. Any active job step on that node will be killed. See the slurm.conf and srun man pages for more information.

[**How can I control the execution of multiple jobs per node?**]{#multi_job}\
There are two mechanisms to control this. If you want to allocate individual processors on a node to jobs, configure *SelectType=select/cons_tres*. See [Consumable Resources in Slurm](cons_tres.md) for details about this configuration. If you want to allocate whole nodes to jobs, configure configure *SelectType=select/linear*. Each partition also has a configuration parameter *OverSubscribe* that enables more than one job to execute on each node. See *man slurm.conf* for more information about these configuration parameters.

[**Why are jobs allocated nodes and then unable to initiate programs on some nodes?**]{#time}\
This typically indicates that the time on some nodes is not consistent with the node on which the *slurmctld* daemon executes. In order to initiate a job step (or batch job), the *slurmctld* daemon generates a credential containing a time stamp. If the *slurmd* daemon receives a credential containing a time stamp later than the current time or more than a few minutes in the past, it will be rejected. If you check in the *SlurmdLogFile* on the nodes of interest, you will likely see messages of this sort: \"*Invalid job credential from \<some IP address\>: Job credential expired*.\" Make the times consistent across all of the nodes and all should be well.

[**Why does *slurmctld* log that some nodes are not responding even if they are not in any partition?**]{#ping}\
The *slurmctld* daemon periodically pings the *slurmd* daemon on every configured node, even if not associated with any partition. You can control the frequency of this ping with the *SlurmdTimeout* configuration parameter in *slurm.conf*.

[**How can I easily preserve drained node information between major Slurm updates?**]{#state_preserve}\
Major Slurm updates generally have changes in the state save files and communication protocols, so a cold-start (without state) is generally required. If you have nodes in a DRAIN state and want to preserve that information, you can easily build a script to preserve that information using the *sinfo* command. The following command line will report the *Reason* field for every node in a DRAIN state and write the output in a form that can be executed later to restore state.

    sinfo -t drain -h -o "scontrol update nodename='%N' state=drain reason='%E'"

[**Does anyone have an example node health check script for Slurm?**]{#health_check_example}\
Probably the most comprehensive and lightweight health check tool out there is https://github.com/mej/nhc. It has integration with Slurm as well as Torque resource managers.

[**Why doesn\'t the *HealthCheckProgram* execute on DOWN nodes?**]{#health_check}\
Hierarchical communications are used for sending this message. If there are DOWN nodes in the communications hierarchy, messages will need to be re-routed. This limits Slurm\'s ability to tightly synchronize the execution of the *HealthCheckProgram* across the cluster, which could adversely impact performance of parallel applications. The use of CRON or node startup scripts may be better suited to ensure that *HealthCheckProgram* gets executed on nodes that are DOWN in Slurm.

[**How can I prevent the *slurmd* and *slurmstepd* daemons from being killed when a node\'s memory is exhausted?**]{#slurmd_oom}\
You can set the value in the */proc/self/oom_adj* for *slurmd* and *slurmstepd* by initiating the *slurmd* daemon with the *SLURMD_OOM_ADJ* and/or *SLURMSTEPD_OOM_ADJ* environment variables set to the desired values. A value of -17 typically will disable killing.

[**I see the host of my calling node as 127.0.1.1 instead of the correct IP address. Why is that?**]{#ubuntu}\
Some systems by default will put your host in the /etc/hosts file as something like

    127.0.1.1   snowflake.llnl.gov  snowflake

This will cause srun and Slurm commands to use the 127.0.1.1 address instead of the correct address and prevent communications between nodes. The solution is to either remove this line or configure a different NodeAddr that is known by your other nodes.

The CommunicationParameters=NoInAddrAny configuration parameter is subject to this same problem, which can also be addressed by removing the actual node name from the \"127.0.1.1\" as well as the \"127.0.0.1\" addresses in the /etc/hosts file. It is ok if they point to localhost, but not the actual name of the node.

[**How should I add nodes to Slurm?**]{#add_nodes}\
The slurmctld daemon has many bitmaps to track state of nodes and cores in the cluster. Adding nodes to a running cluster would require the slurmctld daemon to rebuild all of those bitmaps, which required restarting the daemon in older versions of Slurm. Communications from the slurmd daemons on the compute nodes to the slurmctld daemon include a configuration file checksum, so you should maintain the same slurm.conf file on all nodes.

The following procedure is recommended on **Slurm 24.05** and older (see below for 24.11 and newer):

1.  Stop the slurmctld daemon (e.g. `systemctl stop slurmctld` on the head node)
2.  Update the **slurm.conf** file on all nodes in the cluster
3.  Restart the slurmd daemons on all nodes (e.g. `systemctl restart slurmd` on all nodes)
4.  Restart the slurmctld daemon (e.g. `systemctl start slurmctld` on the head node)

The following procedure is sufficient on **Slurm 24.11** and newer:

1.  Update the **slurm.conf** file on all nodes in the cluster
2.  Run `scontrol reconfigure`

**NOTE**: Jobs submitted with srun, and that are waiting for an allocation, prior to new nodes being added to the slurm.conf can fail if the job is allocated one of the new nodes.

[**How should I remove nodes from Slurm?**]{#rem_nodes}\
To safely remove a node from a cluster, it\'s best to drain the node of all jobs. This ensures that job processes aren\'t running on the node after removal. On restart of the controller, if a node is removed from a running job the controller will kill the job on any remaining allocated nodes and attempt to requeue the job if possible.

The following procedure is recommended on **Slurm 24.05** and older (see below for 24.11 and newer):

1.  Drain node of all jobs (e.g. `scontrol update nodename='%N' state=drain reason='removing nodes'` )
2.  Stop the slurmctld daemon (e.g. `systemctl stop slurmctld` on the head node)
3.  Update the **slurm.conf** file on all nodes in the cluster
4.  Restart the slurmd daemons on all nodes (e.g. `systemctl restart slurmd` on all nodes)
5.  Restart the slurmctld daemon (e.g. `systemctl start slurmctld` on the head node)

The following procedure is sufficient on **Slurm 24.11** and newer:

1.  Drain node of all jobs (e.g. `scontrol update nodename='%N' state=drain reason='removing nodes'` )
2.  Update the **slurm.conf** file on all nodes in the cluster
3.  Run `scontrol reconfigure`

**NOTE**: Removing nodes from the cluster may cause some errors in the logs. Verify that any errors in the logs are for nodes that you intended to remove.

[**Why is a compute node down with the reason set to \"Node unexpectedly rebooted\"?**]{#reboot}\
This is indicative of the slurmctld daemon running on the cluster\'s head node as well as the slurmd daemon on the compute node when the compute node reboots. If you want to prevent this condition from setting the node into a DOWN state then configure ReturnToService to 2. See the slurm.conf man page for details. Otherwise use scontrol or sview to manually return the node to service.

[**How do I convert my nodes to Control Group (cgroup) v2?**]{#cgroupv2}\
Refer to the [cgroup v2](cgroup_v2.md#conversion) documentation for the conversion procedure.

[**Can Slurm be used to run jobs on Amazon\'s EC2?**]{#amazon_ec2}\
Yes, here is a description of Slurm use with http://aws.amazon.com/ec2/ courtesy of Ashley Pittman:

I do this regularly and have no problem with it, the approach I take is to start as many instances as I want and have a wrapper around ec2-describe-instances that builds a /etc/hosts file with fixed hostnames and the actual IP addresses that have been allocated. The only other step then is to generate a slurm.conf based on how many node you\'ve chosen to boot that day. I run this wrapper script on my laptop and it generates the files and they rsyncs them to all the instances automatically.

One thing I found is that Slurm refuses to start if any nodes specified in the slurm.conf file aren\'t resolvable, I initially tried to specify cloud\[0-15\] in slurm.conf, but then if I configure less than 16 nodes in /etc/hosts this doesn\'t work so I dynamically generate the slurm.conf as well as the hosts file.

As a comment about EC2 I run just run generic AMIs and have a persistent EBS storage device which I attach to the first instance when I start up. This contains a /usr/local which has my software like Slurm, pdsh and MPI installed which I then copy over the /usr/local on the first instance and NFS export to all other instances. This way I have persistent home directories and a very simple first-login script that configures the virtual cluster for me.

### User Management

[**How can PAM be used to control a user\'s limits on or access to compute nodes?**]{#pam}\
To control a user\'s limits on a compute node:

First, enable Slurm\'s use of PAM by setting *UsePAM=1* in *slurm.conf*.

Second, establish PAM configuration file(s) for Slurm in */etc/pam.conf* or the appropriate files in the */etc/pam.d* directory (e.g. */etc/pam.d/sshd* by adding the line \"account required pam_slurm.so\". A basic configuration you might use is:

    account  required  pam_unix.so
    account  required  pam_slurm.so
    auth     required  pam_localuser.so
    session  required  pam_limits.so

Third, set the desired limits in */etc/security/limits.conf*. For example, to set the locked memory limit to unlimited for all users:

    *   hard   memlock   unlimited
    *   soft   memlock   unlimited

Finally, you need to disable Slurm\'s forwarding of the limits from the session from which the *srun* initiating the job ran. By default all resource limits are propagated from that session. For example, adding the following line to *slurm.conf* will prevent the locked memory limit from being propagated:*PropagateResourceLimitsExcept=MEMLOCK*.

To control a user\'s access to a compute node:

The pam_slurm_adopt and pam_slurm modules prevent users from logging into nodes that they have not been allocated (except for user root, which can always login). They are both included with the Slurm distribution.

The pam_slurm_adopt module is highly recommended for most installations, and is documented in its [own guide](pam_slurm_adopt.md).

pam_slurm is older and less functional. These modules are built by default for RPM packages, but can be disabled using the .rpmmacros option \"%\_without_pam 1\" or by entering the command line option \"\--without pam\" when the configure program is executed. Their source code is in the \"contribs/pam\" and \"contribs/pam_slurm_adopt\" directories respectively.

The use of either pam_slurm_adopt or pam_slurm does not require *UsePAM* being set. The two uses of PAM are independent.

[**How can I exclude some users from pam_slurm?**]{#pam_exclude}\
**CAUTION:** Please test this on a test machine/VM before you actually do this on your Slurm computers.

**Step 1.** Make sure pam_listfile.so exists on your system. The following command is an example on Redhat 6:

    ls -la /lib64/security/pam_listfile.so

**Step 2.** Create user list (e.g. /etc/ssh/allowed_users):

    # /etc/ssh/allowed_users
    root
    myadmin

And, change file mode to keep it secret from regular users(Optional):

    chmod 600 /etc/ssh/allowed_users

**NOTE**: root is not necessarily listed on the allowed_users, but I feel somewhat safe if it\'s on the list.

**Step 3.** On /etc/pam.d/sshd, add pam_listfile.so with sufficient flag before pam_slurm.so (e.g. my /etc/pam.d/sshd looks like this):

    #%PAM-1.0
    auth       required     pam_sepermit.so
    auth       include      password-auth
    account    sufficient   pam_listfile.so item=user sense=allow file=/etc/ssh/allowed_users onerr=fail
    account    required     pam_slurm.so
    account    required     pam_nologin.so
    account    include      password-auth
    password   include      password-auth
    # pam_selinux.so close should be the first session rule
    session    required     pam_selinux.so close
    session    required     pam_loginuid.so
    # pam_selinux.so open should only be followed by sessions to be executed in the user context
    session    required     pam_selinux.so open env_params
    session    optional     pam_keyinit.so force revoke
    session    include      password-auth

(Information courtesy of Koji Tanaka, Indiana University)

[**Can a user\'s account be changed in the database?**]{#user_account}\
A user\'s account can not be changed directly. A new association needs to be created for the user with the new account. Then the association with the old account can be deleted.

    # Assume user "adam" is initially in account "physics"
    sacctmgr create user name=adam cluster=tux account=physics
    sacctmgr delete user name=adam cluster=tux account=chemistry

[**I had to change a user\'s UID and now they cannot submit jobs. How do I get the new UID to take effect?**]{#changed_uid}\
When changing UIDs, you will also need to restart the slurmctld for the changes to take effect. Normally, when adding a new user to the system, the UID is filled in automatically and immediately. If the user isn\'t known on the system yet, there is a thread that runs every hour that fills in those UIDs when they become known, but it doesn\'t recognize UID changes of preexisting users. But you can simply restart the slurmctld for those changes to be recognized.

[**How can I get SSSD to work with Slurm?**]{#sssd}\
SSSD or System Security Services Daemon does not allow enumeration of group members by default. Note that enabling enumeration in large environments might not be feasible. However, Slurm does not need enumeration except for some specific quirky configurations (multiple groups with the same GID), so it\'s probably safe to leave enumeration disabled. SSSD is also case sensitive by default for some configurations, which could possibly raise other issues. Add the following lines to */etc/sssd/sssd.conf* on your head node to address these issues:

    enumerate = True
    case_sensitive = False

### Jobs

[**How is job suspend/resume useful?**]{#suspend}\
Job suspend/resume is most useful to get particularly large jobs initiated in a timely fashion with minimal overhead. Say you want to get a full-system job initiated. Normally you would need to either cancel all running jobs or wait for them to terminate. Canceling jobs results in the loss of their work to that point from their beginning. Waiting for the jobs to terminate can take hours, depending upon your system configuration. A more attractive alternative is to suspend the running jobs, run the full-system job, then resume the suspended jobs. This can easily be accomplished by configuring a special queue for full-system jobs and using a script to control the process. The script would stop the other partitions, suspend running jobs in those partitions, and start the full-system partition. The process can be reversed when desired. One can effectively gang schedule (time-slice) multiple jobs using this mechanism, although the algorithms to do so can get quite complex. Suspending and resuming a job makes use of the SIGSTOP and SIGCONT signals respectively, so swap and disk space should be sufficient to accommodate all jobs allocated to a node, either running or suspended.

[**How can I suspend, resume, hold or release all of the jobs belonging to a specific user, partition, etc?**]{#squeue_script}\
There isn\'t any filtering by user, partition, etc. available in the scontrol command; however the squeue command can be used to perform the filtering and build a script which you can then execute. For example:

    $ squeue -u adam -h -o "scontrol hold %i" >hold_script

[**After manually setting a job priority value, how can its priority value be returned to being managed by the priority/multifactor plugin?**]{#restore_priority}\
Hold and then release the job as shown below.

    $ scontrol hold <jobid>
    $ scontrol release <jobid>

[**Can I update multiple jobs with a single *scontrol* command?**]{#scontrol_multi_jobs}\
No, but you can probably use *squeue* to build the script taking advantage of its filtering and formatting options. For example:

    $ squeue -tpd -h -o "scontrol update jobid=%i priority=1000" >my.script

[**How could I automatically print a job\'s Slurm job ID to its standard output?**]{#task_prolog}\
The configured *TaskProlog* is the only thing that can write to the job\'s standard output or set extra environment variables for a job or job step. To write to the job\'s standard output, precede the message with \"print \". To export environment variables, output a line of this form \"export name=value\". The example below will print a job\'s Slurm job ID and allocated hosts for a batch job only.

    #!/bin/sh
    #
    # Sample TaskProlog script that will print a batch job's
    # job ID and node list to the job's stdout
    #

    if [ X"$SLURM_STEP_ID" = "X" -a X"$SLURM_PROCID" = "X"0 ]
    then
      echo "print =========================================="
      echo "print SLURM_JOB_ID = $SLURM_JOB_ID"
      echo "print SLURM_JOB_NODELIST = $SLURM_JOB_NODELIST"
      echo "print =========================================="
    fi

[**Is it possible to write to user stdout?**]{#write_to_job_stdout}\
The way user I/O is handled by Slurm makes it impossible to write to the user process as an admin after the user process is executed (execve is called). This happens right after the call to [TaskProlog](prolog_epilog.md), which is the last moment we can write to the stdout of the user process. Slurm assumes that this file descriptor is only owned by the user process while running. The file descriptor is opened as specified and passed to the task so it makes use of the file descriptor directly. Slumstepd is able to log error messages to the error file by duplicating the standard error of the process.

It is possible to write to standard error from SPANK plugins, but this can\'t be used to append a job summary, since the file descriptors are opened with a close-on-exec flag and are closed by the operating system right after the user process completes. In theory, a central place that could be used to prepare some kind of job summary is EpilogSlurmctld. However, using it to write to a file where user output is stored may be problematic. The script is running as SlurmUser, so intensive validation of the file name may be required (e.g. to prevent users from specifying something like /etc/passwd as the output file). It\'s also possible that a job could have multiple output files (see [filename pattern](srun.html#OPT_filename-pattern) in the srun man page).

[**Why are user processes and *srun* running even though the job is supposed to be completed?**]{#orphan_procs}\
Slurm relies upon a configurable process tracking plugin to determine when all of the processes associated with a job or job step have completed. Those plugins relying upon a kernel patch can reliably identify every process. Those plugins dependent upon process group IDs or parent process IDs are not reliable. See the *ProctrackType* description in the *slurm.conf* man page for details. We rely upon the cgroup plugin for most systems.

[**How can a job which has exited with a specific exit code be requeued?**]{#reqspec}\
Slurm supports requeue in hold with a **SPECIAL_EXIT** state using the command:

    scontrol requeuehold State=SpecialExit job_id

This is useful when users want to requeue and flag a job which has exited with a specific error case. See man scontrol(1) for more details.

    $ scontrol requeuehold State=SpecialExit 10
    $ squeue
       JOBID PARTITION  NAME     USER  ST       TIME  NODES NODELIST(REASON)
        10      mira    zoppo    david SE       0:00      1 (JobHeldUser)

The job can be later released and run again.

The requeuing of jobs which exit with a specific exit code can be automated using an **EpilogSlurmctld**, see man(5) slurm.conf. This is an example of a script which exit code depends on the existence of a file.

    $ cat exitme
    #!/bin/sh
    #
    echo "hi! `date`"
    if [ ! -e "/tmp/myfile" ]; then
      echo "going out with 8"
      exit 8
    fi
    rm /tmp/myfile
    echo "going out with 0"
    exit 0

This is an example of an EpilogSlurmctld that checks the job exit value looking at the **SLURM_JOB_EXIT2** environment variable and requeues a job if it exited with value 8. The SLURM_JOB_EXIT2 has the format \"exit:sig\", the first number is the exit code, typically as set by the exit() function. The second number of the signal that caused the process to terminate if it was terminated by a signal.

    $ cat slurmctldepilog
    #!/bin/sh

    export PATH=/bin:/home/slurm/linux/bin
    LOG=/home/slurm/linux/log/logslurmepilog

    echo "Start `date`" >> $LOG 2>&1
    echo "Job $SLURM_JOB_ID exitcode $SLURM_JOB_EXIT_CODE2" >> $LOG 2>&1
    exitcode=`echo $SLURM_JOB_EXIT_CODE2|awk '{split($0, a, ":"); print a[1]}'` >> $LOG 2>&1
    if [ "$exitcode" == "8" ]; then
       echo "Found REQUEUE_EXIT_CODE: $REQUEUE_EXIT_CODE" >> $LOG 2>&1
       scontrol requeuehold state=SpecialExit $SLURM_JOB_ID >> $LOG 2>&1
       echo $? >> $LOG 2>&1
    else
       echo "Job $SLURM_JOB_ID exit all right" >> $LOG 2>&1
    fi
    echo "Done `date`" >> $LOG 2>&1

    exit 0

Using the exitme script as an example, we have it exit with a value of 8 on the first run, then when it gets requeued in hold with SpecialExit state we touch the file /tmp/myfile, then release the job which will finish in a COMPLETE state.

[**Why is Slurm unable to set the CPU frequency for jobs?**]{#cpu_freq}\
First check that Slurm is configured to bind jobs to specific CPUs by making sure that TaskPlugin is configured to either affinity or cgroup. Next check that your processor is configured to permit frequency control by examining the values in the file */sys/devices/system/cpu/cpu0/cpufreq* where \"cpu0\" represents a CPU ID 0. Of particular interest is the file *scaling_available_governors*, which identifies the CPU governors available. If \"userspace\" is not an available CPU governor, this may well be due to the *intel_pstate* driver being installed. Information about disabling the *intel_pstate* driver is available from\
https://bugzilla.kernel.org/show_bug.cgi?id=57141 and\
http://unix.stackexchange.com/questions/121410/setting-cpu-governor-to-on-demand-or-conservative.

[**Can the salloc command be configured to launch a shell on a node in the job\'s allocation?**]{#salloc_default_command}\
Yes, just set \"use_interactive_step\" as part of the LaunchParameters configuration option in slurm.conf.

[**How can I set up a private /tmp and /dev/shm for jobs on my machine?**]{#tmpfs_jobcontainer}\
Tmpfs job container plugin can be used by including *JobContainerType=job_container/tmpfs* in your slurm.conf file. It additionally requires a [job_container.conf](job_container.conf.md) file to be set up which is further described in the man page. Tmpfs plugin creates a private mount namespace inside of which it mounts a private /tmp to a location that is configured in job_container.conf. The basepath is used to construct the mount path, by creating a job specific directory inside it and mounting /tmp to it. Since all the mounts are created inside of a mount namespace which is private, they are only visible inside the job. Hence this proves to be a useful solution for jobs that are on shared nodes, since each job can only view mounts created in their own mount namespace. A private /dev/shm is also mounted to isolate it between different jobs.

Mount namespace construction also happens before job\'s spank environment is set up. Hence all spank related job steps will view only private /tmp the plugin creates. The plugin also provides an optional initialization script that is invoked before the job\'s namespace is constructed. This can be useful for any site specific customization that may be necessary.

    parallels@linux_vb:~$ echo $SLURM_JOB_ID
    7
    parallels@linux_vb:~$ findmnt -o+PROPAGATION | grep /tmp
    ââ/tmp  /dev/sda1[/storage/7/.7] ext4  rw,relatime,errors=remount-ro,data=ordered   private

In the example above, *BasePath* points to /storage and a slurm job with job id 7 is set up to mount /tmp on /storage/7/.7. When user from inside a job tries to look up mounts, they can see that their /tmp is mounted. However they are prevented from mistakenly accessing the backing directory directly.

    parallels@linux_vb:~$ cd /storage/7/
    bash: cd: /storage/7/: Permission denied

They are allowed to access (read/write) /tmp only.

Additionally pam_slurm_adopt has also been extended to support this functionality. If a user starts an ssh session which is managed by pam_slurm_adopt, then the user\'s process joins the namespace that is constructed by tmpfs plugin. Hence in ssh sessions, user has the same view of /tmp and /dev/shm as their job. This functionality is enabled by default in pam_slurm_adopt but can be disabled explicitly by appending *join_container=false* as shown:

    account sufficient  pam_slurm_adopt.so join_container=false

[**How do I configure Slurm to work with System V IPC enabled applications?**]{#sysv_memory}\
Slurm is generally agnostic to http://man7.org/linux/man-pages/man2/ipc.2.html (a.k.a. \"sysv ipc\" in the Linux kernel). Memory accounting of processes using sysv ipc changes depending on the value of https://www.kernel.org/doc/Documentation/sysctl/kernel.txt (added in Linux kernel 3.1):

- shm_rmid_forced = 1\
  Forces all shared memory usage of processes to be accounted and reported by the kernel to Slurm. This breaks the separate namespace of sysv ipc and may cause unexpected application issues without careful planning. Processes that share the same sysv ipc namespaces across jobs may end up getting OOM killed when another job ends and their allocation percentage increases.
- shm_rmid_forced = 0 (default in most Linux distributions)\
  System V memory usage will not be reported by Slurm for jobs. It is generally suggested to configure the https://www.kernel.org/doc/Documentation/sysctl/kernel.txt parameter. The value of kernel.shmmax times the maximum number of job processes should be deducted from each node\'s configured RealMemory in your slurm.conf. Most Linux distributions set the default to what is effectively unlimited, which can cause the OOM killer to activate for unrelated new jobs or even for the slurmd process. If any processes use sysv memory mechanisms, the Linux kernel OOM killer will never be able to free the used memory. A Slurm job epilog script will be needed to free any of the user memory. Setting kernel.shmmax=0 will disable sysv ipc memory allocations but may cause application issues.

### General Troubleshooting

[**If a Slurm daemon core dumps, where can I find the core file?**]{#core_dump}\
If *slurmctld* is started with the -D option, then the core file will be written to the current working directory. If *SlurmctldLogFile* is an absolute path, the core file will be written to this directory. Otherwise the core file will be written to the *StateSaveLocation*, or \"/var/tmp/\" as a last resort.\
SlurmUser must have write permission on the directories. If none of the above directories have write permission for SlurmUser, no core file will be produced.

If *slurmd* is started with the -D option, then the core file will also be written to the current working directory. If *SlurmdLogFile* is an absolute path, the core file will be written to the this directory. Otherwise the core file will be written to the *SlurmdSpoolDir*, or \"/var/tmp/\" as a last resort.\
If none of the above directories can be written, no core file will be produced.

For *slurmstepd*, the core file will depend upon when the failure occurs. If it is running in a privileged phase, it will be in the same location as that described above for the slurmd daemon. If it is running in an unprivileged phase, it will be in the spawned job\'s working directory.

Nevertheless, in some operating systems this can vary, for example:

- In RHEL the event may be captured by the abrt daemon and generated in the configured dump location (e.g., /var/spool/abrt).
- In Ubuntu the event may be captured by the apport daemon and generated in the configured dump location (e.g., /var/lib/apport).

Normally, distributions need some more tweaking in order to allow the core files to be generated correctly.

slurmstepd uses the setuid() (set user ID) function to escalate privileges. It is possible that in certain systems and for security policies, this causes the core files not to be generated.\
To allow the generation in such systems you usually must enable the suid_dumpable kernel parameter:

Set:\
/proc/sys/fs/suid_dumpable to 2\
or\
sysctl fs.suid_dumpable=2\
\
or set it permanently in sysctl.conf\
fs.suid_dumpable = 2\
\

The value of 2, \"suidsafe\", makes any binary which normally not be dumped is dumped readable by root only.\
This allows the end user to remove such a dump but not access it directly. For security reasons core dumps in this mode will not overwrite one another or other files.\
This mode is appropriate when administrators are attempting to debug problems in a normal environment.

Then you must also set the core pattern to an absolute pathname:

    sysctl kernel.core_pattern=/tmp/core.%e.%p

We recommend reading your distribution\'s documentation about the configuration of these parameters.

It is also usually needed to configure the system core limits, since it can be set to 0.

    $ grep core /etc/security/limits.conf
    #        - core - limits the core file size (KB)
    *               hard    core            unlimited
    *               soft    core            unlimited

In some systems it is not enough to set a hard limit, you must set also a soft limit.

Also, for generating the limits in userspace, the *PropagateResourceLimits=CORE* parameter in slurm.conf could be needed.

Be also sure to give SlurmUser the appropriate permissions to write in the core location directories.

**NOTE**: On a diskless node depending on the core_pattern or if /var/spool/abrt is pointing to an in-memory filespace like tmpfs, if the job caused an OOM, then the generation of the core may fill up your machine\'s memory and hang it. It is encouraged then to make coredumps go to a persistent storage. Be careful of multiple nodes writing a core dump to a shared filesystem since it may significantly impact it.

**Other exceptions:**

On Centos 6, also set \"ProcessUnpackaged = yes\" in the file /etc/abrt/abrt-action-save-package-data.conf.

On RHEL6, also set \"DAEMON_COREFILE_LIMIT=unlimited\" in the file rc.d/init.d/functions.

On a SELinux enabled system, or on a distribution with similar security system, get sure it is allowing to dump cores:

    $ getsebool allow_daemons_dump_core

coredumpctl can also give valuable information:

    $ coredumpctl info

[**How can I get a backtrace from a core file?**]{#backtrace}\
If you do have a crash that generates a core file, you will want to get a backtrace of that crash to send to SchedMD for evaluation.

**NOTE**: Core files must be analyzed by the same binary that was used when they were generated. Compile time differences make it almost impossible for SchedMD to use a core file from a different system. You should always send a backtrace rather than a core file when submitting a support request.

In order to generate a backtrace you must use *gdb*, specify the path to the *slurm\** binary that generated the crash, and specify the path to the core file. Below is an example of how to get a backtrace of a core file generated by *slurmctld*:

    gdb -ex 't a a bt full' -batch /path/to/slurmctld <core_file>

You can also use *gdb* to generate a backtrace without a core file. This can be useful if you are experiencing a crash on startup and aren\'t getting a core file for some reason. You would want to start the binary from inside of *gdb*, wait for it to crash, and generate the backtrace. Below is an example, using *slurmctld* as the example binary:

    (gdb) /path/to/slurmctld
    (gdb) set print pretty
    (gdb) r -d
    (gdb) t a a bt full

You may also need to get a backtrace of a running daemon if it is stuck or hung. To do this you would point *gdb* at the running binary and have it generate the backtrace. Below is an example, again using *slurmctld* as the example:

    gdb -ex 't a a bt' -batch -p $(pidof slurmctld)

### Error Messages

[**\"Cannot resolve X plugin operations\" on daemon startup**]{#inc_plugin}\
This means that symbols expected in the plugin were not found by the daemon. This typically happens when the plugin was built or installed improperly or the configuration file is telling the plugin to use an old plugin (say from the previous version of Slurm). Restart the daemon in verbose mode for more information (e.g. \"slurmctld -Dvvvvv\").

[**\"Credential replayed\" in *SlurmdLogFile***]{#credential_replayed}\
This error is indicative of the *slurmd* daemon not being able to respond to job initiation requests from the *srun* command in a timely fashion (a few seconds). *Srun* responds by resending the job initiation request. When the *slurmd* daemon finally starts to respond, it processes both requests. The second request is rejected and the event is logged with the \"credential replayed\" error. If you check the *SlurmdLogFile* and *SlurmctldLogFile*, you should see signs of the *slurmd* daemon\'s non-responsiveness. A variety of factors can be responsible for this problem including

- Diskless nodes encountering network problems
- Very slow Network Information Service (NIS)
- The *Prolog* script taking a long time to complete

Configure *MessageTimeout* in slurm.conf to a value higher than the default 10 seconds.

[**\"Invalid job credential\"**]{#cred_invalid}\
This error is indicative of Slurm\'s job credential files being inconsistent across the cluster. All nodes in the cluster must have the matching public and private keys as defined by **JobCredPrivateKey** and **JobCredPublicKey** in the Slurm configuration file **slurm.conf**.

[**\"Task launch failed on node \... Job credential replayed\"**]{#cred_replay}\
This error indicates that a job credential generated by the slurmctld daemon corresponds to a job that the slurmd daemon has already revoked. The slurmctld daemon selects job ID values based upon the configured value of **FirstJobId** (the default value is 1) and each job gets a value one larger than the previous job. On job termination, the slurmctld daemon notifies the slurmd on each allocated node that all processes associated with that job should be terminated. The slurmd daemon maintains a list of the jobs which have already been terminated to avoid replay of task launch requests. If the slurmctld daemon is cold-started (with the \"-c\" option or \"/etc/init.d/slurm startclean\"), it starts job ID values over based upon **FirstJobId**. If the slurmd is not also cold-started, it will reject job launch requests for jobs that it considers terminated. This solution to this problem is to cold-start all slurmd daemons whenever the slurmctld daemon is cold-started.

[**\"Unable to accept new connection: Too many open files\"**]{#file_limit}\
The srun command automatically increases its open file limit to the hard limit in order to process all of the standard input and output connections to the launched tasks. It is recommended that you set the open file hard limit to 8192 across the cluster.

[***SlurmdDebug* fails to log job step information at the appropriate level**]{#slurmd_log}\
There are two programs involved here. One is **slurmd**, which is a persistent daemon running at the desired debug level. The second program is **slurmstepd**, which executes the user job and its debug level is controlled by the user. Submitting the job with an option of *\--debug=#* will result in the desired level of detail being logged in the *SlurmdLogFile* plus the output of the program.

[**\"Batch JobId=# missing from batch node \<node\> (not found BatchStartTime after startup)\"**]{#batch_lost}\
A shell is launched on node zero of a job\'s allocation to execute the submitted program. The *slurmd* daemon executing on each compute node will periodically report to the *slurmctld* what programs it is executing. If a batch program is expected to be running on some node (i.e. node zero of the job\'s allocation) and is not found, the message above will be logged and the job canceled. This typically is associated with exhausting memory on the node or some other critical failure that cannot be recovered from.

[**Multi-Instance GPU not working with Slurm and PMIx; GPUs are \"In use by another client\"**]{#opencl_pmix}\
PMIx uses the **hwloc API** for different purposes, including *OS device* features like querying sysfs folders (such as */sys/class/net* and */sys/class/infiniband*) to get the names of Infiniband HCAs. With the above mentioned features, hwloc defaults to querying the OpenCL devices, which creates handles on */dev/nvidia\** files. These handles are kept by slurmstepd and will result in the following error inside a job:

    $ nvidia-smi mig --id 1 --create-gpu-instance FOO,FOO --default-compute-instance
    Unable to create a GPU instance on GPU 1 using profile FOO: In use by another client

In order to use Multi-Instance GPUs with Slurm and PMIx you can instruct hwloc to not query OpenCL devices by setting the [HWLOC_COMPONENTS=-opencl]{.commandline} environment variable for slurmd, i.e. setting this variable in systemd unit file for slurmd.

[**\"srun: error: Unable to accept connection: Resources temporarily unavailable\"**]{#accept_again}\
This has been reported on some larger clusters running SUSE Linux when a user\'s resource limits are reached. You may need to increase limits for locked memory and stack size to resolve this problem.

[**\"Warning: Note very large processing time\" in *SlurmctldLogFile***]{#large_time}\
This error is indicative of some operation taking an unexpectedly long time to complete, over one second to be specific. Setting the value of the *SlurmctldDebug* configuration parameter to *debug2* or higher should identify which operation(s) are experiencing long delays. This message typically indicates long delays in file system access (writing state information or getting user information). Another possibility is that the node on which the slurmctld daemon executes has exhausted memory and is paging. Try running the program *top* to check for this possibility.

[**\"Duplicate entry\" causes slurmdbd to fail**]{#mysql_duplicate}\
This problem has been rarely observed with MySQL, but not MariaDB. The root cause of the failure seems to be reaching the upper limit on the auto increment field. Upgrading to MariaDB is recommended. If that is not possible then: backup the database, remove the duplicate record(s), and restart the slurmdbd daemon as shown below.

    $ slurmdbd -Dvv
    ...
    slurmdbd: debug:  Table "cray_job_table" has changed.  Updating...
    slurmdbd: error: mysql_query failed: 1062 Duplicate entry '2711-1478734628' for key 'id_job'
    ...

    $ mysqldump --single-transaction -u<user> -p<user> slurm_acct_db >/tmp/slurm_db_backup.sql

    $ mysql
    mysql> use slurm_acct_db;
    mysql> delete from cray_job_table where id_job='2711-1478734628';
    mysql> quit;
    Bye

If necessary, you can edit the database dump and recreate the database as shown below.

    $ mysql
    mysql> drop database slurm_acct_db;
    mysql> create database slurm_acct_db;
    mysql> quit;
    Bye

    $ mysql -u<user> -p<user> </tmp/slurm_db_backup.sql

[**\"Unable to find plugin: serializer/json\"**]{#json_serializer}\
Several parts of Slurm have swapped to using our centralized serializer code. JSON or YAML plugins are only required if one of the functions that require it is executed. If one of the functions is executed it will fail to create the JSON/YAML output and the linker will fail with the following error:

    slurmctld: fatal: Unable to find plugin: serializer/json

In most cases, these are required for new functionality added after Slurm-20.02. However, with each release, we have been adding more places that use the serializer plugins. Because the list is evolving we do not plan on listing all the commands that require the plugins but will instead provide the error (shown above). To correct the issue, please make sure that Slurm is configured, compiled and installed with the relevant JSON or YAML library (or preferably both). Configure can be made to explicitly request these libraries:

    ./configure --with-json=PATH --with-yaml=PATH $@

Most distributions include packages to make installation relatively easy. Please make sure to install the \'dev\' or \'devel\' packages along with the library packages. We also provide explicit instructions on how to install from source: [libyaml](related_software.md#yaml) and [libjwt](related_software.md#jwt).

### Third Party Integrations

[**Can Slurm be used with Globus?**]{#globus}\
Yes. Build and install Slurm\'s Torque/PBS command wrappers along with the Perl APIs from Slurm\'s *contribs* directory and configure http://www-unix.globus.org/ to use those PBS commands. Note there are RPMs available for both of these packages, named *torque* and *perlapi* respectively.

[**How can TotalView be configured to operate with Slurm?**]{#totalview}\
The following lines should also be added to the global *.tvdrc* file for TotalView to operate with Slurm:

    # Enable debug server bulk launch: Checked
    dset -set_as_default TV::bulk_launch_enabled true

    # Command:
    # Beginning with TV 7X.1, TV supports Slurm and %J.
    # Specify --mem-per-cpu=0 in case Slurm configured with default memory
    # value and we want TotalView to share the job's memory limit without
    # consuming any of the job's memory so as to block other job steps.
    dset -set_as_default TV::bulk_launch_string {srun --mem-per-cpu=0 -N%N -n%N -w`awk -F. 'BEGIN {ORS=","} {if (NR==%N) ORS=""; print $1}' %t1` -l --input=none %B/tvdsvr%K -callback_host %H -callback_ports %L -set_pws %P -verbosity %V -working_directory %D %F}

    # Temp File 1 Prototype:
    # Host Lines:
    # Slurm NodeNames need to be unadorned hostnames. In case %R returns
    # fully qualified hostnames, list the hostnames in %t1 here, and use
    # awk in the launch string above to strip away domain name suffixes.
    dset -set_as_default TV::bulk_launch_tmpfile1_host_lines {%R}
