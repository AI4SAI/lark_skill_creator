# Man Pages

**NOTE: This documentation is for Slurm version 25.11.\
Documentation for other versions of Slurm is distributed with the code**

Refer to [this page](slurm.md) for an overview of Slurm.

## Commands

  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------
  [sacct](sacct.md)         Displays accounting data for all jobs and job steps in the Slurm job accounting log or Slurm database.
  [sacctmgr](sacctmgr.md)   Used to view and modify Slurm account information.
  [salloc](salloc.md)       Obtain a Slurm job allocation (a set of nodes), execute a command, and then release the allocation when the command is finished.
  [sattach](sattach.md)     Attach to a Slurm job step.
  [sbatch](sbatch.md)       Submit a batch script to Slurm.
  [sbcast](sbcast.md)       Transmit a file to the nodes allocated to a Slurm job.
  [scancel](scancel.md)     Used to signal jobs or job steps that are under the control of Slurm.
  [scontrol](scontrol.md)   View or modify Slurm configuration and state.
  [scrontab](scrontab.md)   Manage Slurm crontab files.
  [scrun](scrun.md)         An OCI runtime proxy for slurm.
  [sdiag](sdiag.md)         Scheduling diagnostic tool.
  [sh5util](sh5util.md)     Merge utility for acct_gather_profile plugin.
  [sinfo](sinfo.md)         View information about Slurm nodes and partitions.
  [sprio](sprio.md)         View the factors that comprise a job\'s scheduling priority.
  [squeue](squeue.md)       View information about jobs located in the Slurm scheduling queue.
  [sreport](sreport.md)     Generate reports from the slurm accounting data.
  [srun](srun.md)           Run parallel jobs.
  [sshare](sshare.md)       Tool for listing the shares of associations to a cluster.
  [sstat](sstat.md)         Display the status information of a running job/step.
  [strigger](strigger.md)   Used to set, get or clear Slurm trigger information.
  [sview](sview.md)         Graphical user interface to view and modify Slurm state.
  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------

## Configuration Files {#configuration_files}

  -------------------------------------------------- --------------------------------------------------------------------------
  [acct_gather.conf](acct_gather.conf.md)            Slurm configuration file for the acct_gather plugins.
  [burst_buffer.conf](burst_buffer.conf.md)          Slurm burst buffer configuration.
  [cgroup.conf](cgroup.conf.md)                      Slurm configuration file for the cgroup support.
  [gres.conf](gres.conf.md)                          Slurm configuration file for generic resource management.
  [helpers.conf](helpers.conf.md)                    Slurm configuration file for the node_features/helpers plugin.
  [job_container.conf](job_container.conf.md)        Slurm configuration file for configuring the tmpfs job container plugin.
  [mpi.conf](mpi.conf.md)                            Slurm configuration file to allow the configuration of MPI plugins.
  [namespace.yaml](namespace.yaml.md)                Slurm configuration file for the namespace/linux plugin.
  [oci.conf](oci.conf.md)                            Slurm configuration file for OCI Containers.
  [plugstack.conf](spank.md#SECTION_CONFIGURATION)   Slurm configuration file for SPANK plug-in stack.
  [slurm.conf](slurm.conf.md)                        Slurm configuration file.
  [slurmdbd.conf](slurmdbd.conf.md)                  Slurm Database Daemon (SlurmDBD) configuration file.
  [topology.conf](topology.conf.md)                  Slurm configuration file for defining the network topology.
  [topology.yaml](topology.yaml.md)                  Slurm configuration file for defining multiple network topologies.
  -------------------------------------------------- --------------------------------------------------------------------------

## Daemons and Other {#daemons}

  ----------------------------- ---------------------------------------------------------
  [sackd](sackd.md)             Slurm Auth and Cred Kiosk Daemon.
  [slurmctld](slurmctld.md)     The central management daemon of Slurm.
  [slurmd](slurmd.md)           The compute node daemon for Slurm.
  [slurmdbd](slurmdbd.md)       Slurm Database Daemon.
  [slurmrestd](slurmrestd.md)   The Slurm REST API daemon.
  [slurmstepd](slurmstepd.md)   The job step manager for Slurm.
  [SPANK](spank.md)             Slurm Plug-in Architecture for Node and job (K)control.
  ----------------------------- ---------------------------------------------------------
