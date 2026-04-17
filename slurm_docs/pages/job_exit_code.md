# Job Exit Codes

A job\'s exit code (aka exit status, return code and completion code) is captured by Slurm and saved as part of the job record. For sbatch jobs, the exit code that is captured is the output of the batch script. For salloc jobs, the exit code will be the return value of the exit call that terminates the salloc session. For srun, the exit code will be the return value of the command that srun executes.

Any non-zero exit code will be assumed to be a job failure and will result in a Job State of FAILED with a Reason of \"NonZeroExitCode\".

The exit code is an 8 bit unsigned number ranging between 0 and 255. While it is possible for a job to return a negative exit code, Slurm will display it as an unsigned value in the 0 - 255 range.

## Job Step Exit Codes {#exitcodes}

When a job contains multiple job steps, the exit code of each executable invoked by srun is saved individually to the job step record.

## Signaled Jobs {#signaled}

When a job or step is sent a signal that causes its termination, Slurm also captures the signal number and saves it to the job or step record.

## Displaying Exit Codes and Signals {#displayed}

Slurm displays a job\'s exit code in the output of the **scontrol show job** and the **sview** utility. Slurm displays job step exit codes in the output of the **scontrol show step** and the **sview** utility.

When a signal was responsible for a job or step\'s termination, the signal number will be displayed after the exit code, delineated by a colon(:).

## Database Job/Step Records {#db}

The Slurm control daemon sends job and step records to the Slurm database when the Slurm accounting_storage plugin is installed. Job and step records sent to the Slurm db can be viewed using the **sacct** command. The default **sacct** output contains an ExitCode field whose format mirrors the output of **scontrol** and **sview** described above.

# Derived Exit Code and Comment String {#derived}

After reading the above description of a job\'s exit code, one can imagine a scenario where a central task of a batch job fails but the script returns an exit code of zero, indicating success. In many cases, a user may not be able to ascertain the success or failure of a job until after they have examined the job\'s output files.

The job includes a \"derived exit code\" field. It is initially set to the value of the highest exit code returned by all of the job\'s steps (srun invocations). The job\'s derived exit code is determined by the Slurm control daemon and sent to the database when the accounting_storage plugin is enabled.

In addition to the derived exit code, the job record in the Slurm database contains a comment string. This is initialized to the job\'s comment string (when AccountingStoreFlags parameter in the slurm.conf contains \'job_comment\') and can only be changed by the user.

A new option has been added to the **sacctmgr** command to provide the user the means to modify these two fields of the job record. No other modification to the job record is allowed. For those who prefer a simpler command specifically designed to view and modify the derived exit code and comment string, the **sjobexitmod** wrapper has been created (see below).

The user now has the means to annotate a job\'s exit code after it completes and provide a description of what failed. This includes the ability to annotate a successful completion to jobs that appear to have failed but actually succeeded.

## The sjobexitmod command {#sjobexitmod}

The sjobexitmod command is available to display and update the two derived exit fields of the Slurm db\'s job record. **sjobexitmod** can first be used to display the existing exit code / string for a job:

    > sjobexitmod -l 123
    JobID Account NNodes NodeList     State ExitCode DerivedExitCode Comment
    ----- ------- ------ -------- --------- -------- --------------- -------
    123        lc      1     tux0 COMPLETED      0:0             0:0

If a change is desired, **sjobexitmod** can modify the derived fields:

    > sjobexitmod -e 49 -r "out of memory" 123

     Modification of job 123 was successful.

    > sjobexitmod -l 123
    JobID Account NNodes NodeList     State ExitCode DerivedExitCode Comment
    ----- ------- ------ -------- --------- -------- --------------- -------
    123        lc      1     tux0 COMPLETED      0:0            49:0 out of memory

The existing **sacct** command also supports the two new derived exit fields:

    > sacct -X -j 123 -o JobID,NNodes,State,ExitCode,DerivedExitcode,Comment
    JobID   NNodes      State ExitCode DerivedExitCode        Comment
    ------ ------- ---------- -------- --------------- --------------
    123          1  COMPLETED      0:0            49:0  out of memory
