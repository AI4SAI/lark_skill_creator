# [Job Launch Design Guide]{#top}

## Overview

This guide describes at a high level the processes which occur in order to initiate a job including the daemons and plugins involved in the process. It describes the process of job allocation, step allocation, task launch and job termination. The functionality of tens of thousands of lines of code has been distilled here to a couple of pages of text, so much detail is missing.

## Job Allocation {#job_allocation}

The first step of the process is to create a job allocation, which is a claim on compute resources. A job allocation can be created using the **salloc**, **sbatch** or **srun** command. The **salloc** and **sbatch** commands create resource allocations while the **srun** command will create a resource allocation (if not already running within one) plus launch tasks. Each of these commands will fill in a data structure identifying the specifications of the job allocation requirement (e.g. node count, task count, etc.) based upon command line options and environment variables and send the RPC to the **slurmctld** daemon. The UID and GID of the user launching the job will be included in a credential which will be used later to restrict access to the job, so further steps run in the allocation will need to be launched using the same UID and GID as the one used to create the allocation. If the new job request is the highest priority, the **slurmctld** daemon will attempt to select resources for it immediately, otherwise it will validate that the job request can be satisfied at some time and queue the request. In either case the request will receive a response almost immediately containing one of the following:

- A job ID and the resource allocation specification (nodes, cpus, etc.)
- A job ID and notification of the job being in a queued state OR
- An error code

The process of selecting resources for a job request involves multiple steps, some of which involve plugins. The process is as follows:

1.  Call **job_submit** plugins to modify the request as appropriate
2.  Validate that the options are valid for this user (e.g. valid partition name, valid limits, etc.)
3.  Determine if this job is the highest priority runnable job, if so then really try to allocate resources for it now, otherwise only validate that it could run if no other jobs existed
4.  Determine which nodes could be used for the job. If the feature specification uses an exclusive OR option, then multiple iterations of the selection process below will be required with disjoint sets of nodes
5.  Call the **select** plugin to select the best resources for the request
6.  The **select** plugin will consider network topology and the topology within a node (e.g. sockets, cores, and threads) to select the best resources for the job
7.  If the job can not be initiated using available resources and preemption support is configured, the **select** plugin will also determine if the job can be initiated after preempting lower priority jobs. If so then initiate preemption as needed to start the job

## Step Allocation {#step_allocation}

The **srun** command is always used for job step creation. It fills in a job step request RPC using information from the command line and environment variables then sends that request to the **slurmctld** daemon. It is important to note that many of the **srun** options are intended for job allocation and are not supported by the job step request RPC (for example the socket, core and thread information is not supported). If a job step uses all of the resources allocated to the job then the lack of support for some options is not important. If one wants to execute multiple job steps using various subsets of resources allocated to the job, this shortcoming could prove problematic. It is also worth noting that the logic used to select resources for a job step is relatively simple and entirely contained within the **slurmctld** daemon code (the **select** plugin is not used for job steps). If the request can not be immediately satisfied due to a request for exclusive access to resources, the appropriate error message will be sent and the **srun** command will retry the request on a periodic basis. (**NOTE**: It would be desirable to queue the job step requests to support job step dependencies and better performance in the initiation of job steps, but that is not currently supported.) If the request can be satisfied, the response contains a digitally signed credential (by the **cred** plugin) identifying the resources to be used.

## Task Launch {#task_launch}

The **srun** command builds a task launch request data structure including the credential, executable name, file names, etc. and sends it to the **slurmd** daemon on node zero of the job step allocation. The **slurmd** daemon validates the signature and forwards the request to the **slurmd** daemons on other nodes to launch tasks for that job step. The degree of fanout in this message forwarding is configurable using the **TreeWidth** parameter. Each **slurmd** daemon tests that the job has not been cancelled since the credential was issued (due to a possible race condition) and spawns a **slurmstepd** program to manage the job step. Note that the **slurmctld** daemon is not directly involved in task launch in order to minimize the overhead on this critical resource.

Each **slurmstepd** program executes a single job step. Besides the functions listed below, the **slurmstepd** program also executes several SPANK plugin functions at various times.

1.  Performs MPI setup (using the appropriate plugin)
2.  Calls the **switch** plugin to perform any needed network configuration
3.  Creates a container for the job step using a **proctrack** plugin
4.  Change user ID to that of the user
5.  Configures I/O for the tasks (either using files or a socket connection back to the **srun** command
6.  Sets up environment variables for the tasks including many task-specific environment variables
7.  Fork/exec the tasks

## Job Step Termination {#step_termination}

There are several ways in which a job step or job can terminate, each with slight variation in the logic executed. The simplest case is if the tasks run to completion. The **srun** will note the termination of output from the tasks and notify the **slurmctld** daemon that the job step has completed. **slurmctld** will simply log the job step termination. The job step can also be explicitly cancelled by a user, reach the end of its time limit, etc. and those follow a sequence of steps very similar to that for job termination, which is described below.

## Job Termination {#job_termination}

Job termination can either be user initiated (e.g. **scancel** command) or system initiated (e.g. time limit reached). The termination ultimately requires the **slurmctld** daemon to notify the **slurmd** daemons on allocated nodes that the job is to be ended. The **slurmd** daemon does the following:

1.  Send a SIGCONT and SIGTERM signal to any user tasks
2.  Wait **KillWait** seconds if there are any user tasks
3.  Send a SIGKILL signal to any user tasks
4.  Wait for all tasks to complete
5.  Execute any **Epilog** program
6.  Send an epilog_complete RPC to the **slurmctld** daemon

## Job Accounting Records {#job_record}

When Slurm is configured to use SlurmDBD to store job records (i.e. *AccountingStorageType=accounting_storage=slurmdbd*), there are multiple records that get stored for each job. There is a record for the job as a whole as well as entries for the following types of job steps:

- **extern step** --- A step created for each job as long as you have *PrologFlags=contain* in your slurm.conf. Each node in the job will have a slurmstepd process created for the extern step. [pam_slurm_adopt](pam_slurm_adopt.html) uses this step to contain external connections.
- **batch step** --- A step created for jobs that were submitted with sbatch. The batch host, or the primary node for the job, will run an instance of slurmstepd for the batch step, which is used to run the script provided to sbatch.
- **interactive step** --- A step created for jobs that were submitted with salloc when *LaunchParameters=use_interactive_step* is configured in your slurm.conf. The node on which you have the interactive shell will run an instance of slurmstepd to run the shell or the command provided to salloc.
- **normal step** --- A job can have multiple normal steps, which will appear in sacct as \<**job_id**\>.\<**step_id**\>. These steps are created when srun is called from inside the job and the slurmstepd created will run the command passed to srun. Each step will have one instance of slurmstepd created per node in the step and each instance of slurmstepd can run multiple tasks in the same step.
