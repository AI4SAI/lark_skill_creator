# MPI Users Guide

MPI use depends upon the type of MPI being used. There are three fundamentally different modes of operation used by these various MPI implementations.

1.  Slurm directly launches the tasks and performs initialization of communications through the PMI-1, PMI-2 or PMIx APIs. (Supported by most modern MPI implementations.)
2.  Slurm creates a resource allocation for the job and then mpirun launches tasks using Slurm\'s infrastructure (srun).
3.  Slurm creates a resource allocation for the job and then mpirun launches tasks using some mechanism other than Slurm, such as SSH or RSH. These tasks are initiated outside of Slurm\'s monitoring or control and require access to the nodes from the batch node (e.g. SSH). Slurm\'s epilog should be configured to purge these tasks when the job\'s allocation is relinquished. The use of pam_slurm_adopt is strongly recommended.

**NOTE**: Slurm is not directly launching the user application in case 3, which may prevent the desired behavior of binding tasks to CPUs and/or accounting and is not a recommended way.

Two Slurm parameters control which PMI (Process Management Interface) implementation will be supported. Proper configuration is essential for Slurm to establish the proper environment for the MPI job, such as setting the appropriate environment variables. The *MpiDefault* configuration parameter in *slurm.conf* establishes the system\'s default PMI to be used. The *srun* option *\--mpi=* (or the equivalent environment variable *SLURM_MPI_TYPE*) can be used to specify when a different PMI implementation is to be used for an individual job.

There are parameters that can be set in the [mpi.conf](mpi.conf.md) file that allow you to modify the behavior of the PMI plugins.

**NOTE**: Use of an MPI implementation without the appropriate Slurm plugin may result in application failure. If multiple MPI implementations are used on a system then some users may be required to explicitly specify a suitable Slurm MPI plugin.

**NOTE**: If installing Slurm with RPMs, the *slurm-libpmi* package will conflict with the *pmix-libpmi* package if it is installed. If policies at your site allow you to install from source, this will allow you to install these packages to different locations, so you can choose which libraries to use.

**NOTE**: If you build any MPI stack component with hwloc, note that versions 2.5.0 through 2.7.0 (inclusive) of hwloc have a bug that pushes an untouchable value into the environ array, causing a segfault when accessing it. It is advisable to build with hwloc version 2.7.1 or later.

Links to instructions for using several varieties of MPI/PMI with Slurm are provided below.

- PMIx
- Open MPI
- Intel-MPI
- MPICH
- MVAPICH2
- HPE Cray PMI Support

------------------------------------------------------------------------

## https://openpmix.github.io/ {#pmix}

### Building PMIx {#pmix_build}

Before building PMIx, it is advisable to read these https://openpmix.github.io/support/how-to/. They provide some details on https://openpmix.github.io/code/getting-the-reference-implementation as well as some relevant notes with regards to https://openpmix.github.io/support/how-to/slurm-support.

This section is intended to complement the PMIx FAQ with some notes on how to prepare Slurm and PMIx to work together. PMIx can be obtained from the official https://github.com/openpmix/openpmix repository, either by cloning the repository or by downloading a packaged release.

Slurm support for PMIx was first included in Slurm 16.05 based on the PMIx v1.2 release. It has since been updated to support up to version 5.x of the PMIx series, as per the following table:

- Slurm 20.11+ supports PMIx v1.2+, v2.x and v3.x.
- Slurm 22.05+ supports PMIx v2.x, v3.x., v4.x. and v5.x.

If running PMIx v1, it is recommended to run at least 1.2.5 since older versions may have some compatibility issues with support of pmi and pmi2 APIs. Note also that Intel MPI doesn\'t officially support PMIx. It may work since PMIx offers some compatibility with PMI-2, but there is no guarantee that it will.

### Building Slurm with PMIx support {#slurm_pmix}

At configure time, Slurm won\'t build with PMIx unless **\--with-pmix** is set. Then it will look by default for a PMIx installation under:

    /usr
    /usr/local

If PMIx isn\'t installed in any of the previous locations, the Slurm configure script can be requested to point to the non default location. Here\'s an example assuming the installation dir is */home/user/pmix/v4.1.2/*:

    user@testbox:~/slurm/22.05/build$ ../src/configure \
    > --prefix=/home/user/slurm/22.05/inst \
    > --with-pmix=/home/user/pmix/4.1.2

Or the analogous with RPM based building:

    user@testbox:~/slurm_rpm$ rpmbuild \
    > --define '_prefix /home/user/slurm/22.05/inst' \
    > --define '_slurm_sysconfdir /home/user/slurm/22.05/inst/etc' \
    > --define '_with_pmix --with-pmix=/home/user/pmix/4.1.2' \
    > -ta slurm-22.05.2.1.tar.bz2

**NOTE**: It is also possible to build against multiple PMIx versions with a \':\' separator. For instance to build against 3.2 and 4.1:

    ...
    > --with-pmix=/path/to/pmix/3.2.3:/path/to/pmix/4.1.2 \
    ...

Then, when submitting a job, the desired version can then be selected using any of the available from \--mpi=list. The default for pmix will be the highest version of the library:

    $ srun --mpi=list
    MPI plugin types are...
        cray_shasta
        none
        pmi2
        pmix
    specific pmix plugin versions available: pmix_v3,pmix_v4

Continuing with the configuration, if Slurm is unable to locate the PMIx installation and/or finds it but considers it not usable, the configure output should log something like this:

    checking for pmix installation...
    configure: WARNING: unable to locate pmix installation

Inspecting the generated config.log in the Slurm build directory might provide more detail for troubleshooting purposes. After configuration, we can proceed to install Slurm (using make or rpm accordingly):

    user@testbox:~/slurm/22.05/build$ make -j install
    user@testbox:~/slurm/22.05/build$ cd /home/user/slurm/22.05/inst/lib/slurm/
    user@testbox:~/slurm/22.05/inst/lib/slurm$ ls -l *pmix*
    lrwxrwxrwx 1 user user      16 jul  6 17:17 mpi_pmix.so -> ./mpi_pmix_v4.so
    -rw-r--r-- 1 user user 9387254 jul  6 17:17 mpi_pmix_v3.a
    -rwxr-xr-x 1 user user    1065 jul  6 17:17 mpi_pmix_v3.la
    -rwxr-xr-x 1 user user 1265840 jul  6 17:17 mpi_pmix_v3.so
    -rw-r--r-- 1 user user 9935358 jul  6 17:17 mpi_pmix_v4.a
    -rwxr-xr-x 1 user user    1059 jul  6 17:17 mpi_pmix_v4.la
    -rwxr-xr-x 1 user user 1286936 jul  6 17:17 mpi_pmix_v4.so

If support for PMI-1 or PMI-2 version is also needed, it can also be installed from the contribs directory:

    user@testbox:~/slurm/22.05/build/$ cd contribs/pmi1
    user@testbox:~/slurm/22.05/build/contribs/pmi1$ make -j install

    user@testbox:~/slurm/22.05/build/$ cd contribs/pmi2
    user@testbox:~/slurm/22.05/build/contribs/pmi2$ make -j install

    user@testbox:~/$ ls -l /home/user/slurm/22.05/inst/lib/*pmi*
    -rw-r--r-- 1 user user 493024 jul  6 17:27 libpmi2.a
    -rwxr-xr-x 1 user user    987 jul  6 17:27 libpmi2.la
    lrwxrwxrwx 1 user user     16 jul  6 17:27 libpmi2.so -> libpmi2.so.0.0.0
    lrwxrwxrwx 1 user user     16 jul  6 17:27 libpmi2.so.0 -> libpmi2.so.0.0.0
    -rwxr-xr-x 1 user user 219712 jul  6 17:27 libpmi2.so.0.0.0
    -rw-r--r-- 1 user user 427768 jul  6 17:27 libpmi.a
    -rwxr-xr-x 1 user user   1039 jul  6 17:27 libpmi.la
    lrwxrwxrwx 1 user user     15 jul  6 17:27 libpmi.so -> libpmi.so.0.0.0
    lrwxrwxrwx 1 user user     15 jul  6 17:27 libpmi.so.0 -> libpmi.so.0.0.0
    -rwxr-xr-x 1 user user 241640 jul  6 17:27 libpmi.so.0.0.0

**NOTE**: Since Slurm and PMIx lower than 4.x both provide libpmi\[2\].so libraries, we recommend you install both pieces of software in different locations. Otherwise, these same libraries might end up being installed under standard locations like /usr/lib64 and the package manager would error out, reporting the conflict.

**NOTE**: Any application compiled against PMIx should use the same PMIx or at least a PMIx with the same security domain than the one Slurm is using, otherwise there could be authentication issues. E.g. one PMIx compiled \--with-munge while another compiled \--without-munge (the default since PMIx 4.2.4). A workaround which might work is to specify the desired security method adding \"\--mca psec native\" to the cli or exporting PMIX_MCA_psec=native environment variable.

**NOTE**: If you are setting up a test environment using multiple-slurmd, the TmpFS option in your slurm.conf needs to be specified and the number of directory paths created needs to equal the number of nodes. These directories are used by the Slurm PMIx plugin to create temporal files and/or UNIX sockets. Here is an example setup for two nodes named compute\[1-2\]:

    slurm.conf:
    TmpFS=/home/user/slurm/22.05/inst/tmp/slurmd-tmpfs-%n

    $ mkdir /home/user/slurm/22.05/inst/tmp/slurmd-tmpfs-compute1
    $ mkdir /home/user/slurm/22.05/inst/tmp/slurmd-tmpfs-compute2

### Testing Slurm and PMIx {#pmix_testing}

It is possible to directly test Slurm and PMIx without needing to have an MPI implementation installed. Here is an example demonstrating that both components work properly:

    $ srun --mpi=list
    MPI plugin types are...
        cray_shasta
        none
        pmi2
        pmix
    specific pmix plugin versions available: pmix_v3,pmix_v4

    $ srun --mpi=pmix_v4 -n2 -N2 \
    > /home/user/git/pmix/test/pmix_client -n 2 --job-fence -c
    ==141756== OK
    ==141774== OK

## https://open-mpi.org/ {#open_mpi}

The current versions of Slurm and Open MPI support task launch using the [srun]{.commandline} command.

If OpenMPI is configured with *\--with-pmi=* pointing to either Slurm\'s PMI-1 libpmi.so or PMI-2 libpmi2.so libraries, the OMPI jobs can then be launched directly using the srun command. This is the preferred mode of operation since accounting features and affinity done by Slurm will become available. If pmi2 support is enabled, the option \'\--mpi=pmi2\' must be specified on the srun command line. Alternately configure \'MpiDefault=pmi\' or \'MpiDefault=pmi2\' in slurm.conf.

Starting with Open MPI version 3.1, PMIx is natively supported. To launch Open MPI applications using PMIx the \'\--mpi=pmix\' option must be specified on the srun command line or \'MpiDefault=pmix\' must be configured in slurm.conf.

It is also possible to build OpenMPI using an external PMIx installation. Refer to the OpenMPI documentation for a detailed procedure but it basically consists of specifying **\--with-pmix=PATH** when configuring OpenMPI. Note that if building OpenMPI using an external PMIx installation, both OpenMPI and PMIx need to be built against the same libevent/hwloc installations. OpenMPI configure script provides the options **\--with-libevent=PATH** and/or **\--with-hwloc=PATH** to make OpenMPI match what PMIx was built against.

A set of parameters are available to control the behavior of the Slurm PMIx plugin, read [mpi.conf](mpi.conf.md) for more information.

**NOTE**: OpenMPI has a limitation that does not support calls to *MPI_Comm_spawn()* from within a Slurm allocation. If you need to use the *MPI_Comm_spawn()* function you will need to use another MPI implementation combined with PMI-2 since PMIx doesn\'t support it either.

**NOTE**: Some kernels and system configurations have resulted in a locked memory too small for proper OpenMPI functionality, resulting in application failure with a segmentation fault. This may be fixed by configuring the slurmd daemon to execute with a larger limit. For example, add \"LimitMEMLOCK=infinity\" to your slurmd.service file.

------------------------------------------------------------------------

## **Intel MPI** {#intel_mpi}

Intel® MPI Library for Linux OS supports the following methods of launching the MPI jobs under the control of the Slurm job manager:

The *mpirun* command over the Hydra PM

The *srun* command (Slurm, recommended)

This description provides detailed information on these two methods.

### The mpirun Command over the Hydra Process Manager {#intel_mpirun_hydra}

Slurm is supported by the *mpirun* command of the Intel® MPI Library through the Hydra Process Manager by default. When launched within an allocation the *mpirun* command will automatically read the environment variables set by Slurm such as nodes, cpus, tasks, etc, in order to start the required hydra daemons on every node. These daemons will be started using srun and will subsequently start the user application. Since Intel® MPI supports only PMI-1 and PMI-2 (not PMIx), it is highly recommended to configure this mpi implementation to use Slurm\'s PMI-2, which offers better scalability than PMI-1. PMI-1 is not recommended and should be deprecated soon.

Below is an example of how a user app can be launched within an exclusive allocation of 10 nodes using Slurm\'s PMI-2 library installed from contribs:

    $ salloc -N10 --exclusive
    $ export I_MPI_PMI_LIBRARY=/path/to/slurm/lib/libpmi2.so
    $ mpirun -np <num_procs> user_app.bin

Note that by default Slurm will inject two environment variables to ensure mpirun or mpiexec will use the Slurm bootstrap mechanism (srun) to launch Hydra. With these, Hydra will also pass the argument \'\--external-launcher\' to srun in order to not consider these hydra processes as regular steps. This automatic variable injection mechanism can be disabled by setting \"MpiParams=disable_slurm_hydra_bootstrap\" in slurm.conf, with the exception of the cases where \"slurm\" is already explicitly set as a bootstrap.

It is possible to run Intel MPI using a different bootstrap mechanism. To do so, explicitly set the following environment variable prior to submitting the job with sbatch or salloc:

    $ export I_MPI_HYDRA_BOOTSTRAP=ssh
    $ salloc -N10
    $ mpirun -np <num_procs> user_app.bin

### The srun Command (Slurm, recommended) {#intel_srun}

This method is also supported by the Intel® MPI Library. This method is the best integrated with Slurm and supports process tracking, accounting, task affinity, suspend/resume and other features. As in the previous case, we show an example of how a user app can be launched within an exclusive allocation of 10 nodes using Slurm\'s PMI-2 library installed from contribs, allowing it to take advantage of of all the Slurm features. This can be done with *sbatch* or *salloc* commands:

    $ salloc -N10 --exclusive
    $ export I_MPI_PMI_LIBRARY=/path/to/slurm/lib/libpmi2.so
    $ srun user_app.bin

**NOTE**: The reason we\'re pointing manually to Slurm\'s PMI-1 or PMI-2 library is for licensing reasons. IMPI doesn\'t link directly to any external PMI implementations so, unlike other stacks (OMPI, MPICH, MVAPICH\...), Intel is not built against Slurm libs. Pointing to this library will cause Intel to dlopen and use this PMI library.

**NOTE**: There is no official support provided by Intel against PMIx libraries. Since IMPI is based on MPICH, using PMIx with Intel may work due to PMIx maintaining compatibility with pmi2 (which are the libraries used in MPICH) but it is not guaranteed to run in all cases and PMIx could break this compatibility in future versions.

For more information see: https://software.intel.com/en-us/intel-mpi-library.

## https://www.mpich.org/ {#mpich}

MPICH was formerly known as MPICH2.

MPICH jobs can be launched using **srun** or **mpiexec**. Both modes of operation are described below. The MPICH implementation supports PMI-1, PMI-2 and PMIx (starting with MPICH v4).

Note that by default Slurm will inject two environment variables to ensure mpirun or mpiexec will use the Slurm bootstrap mechanism (srun) to launch Hydra. With these, Hydra will also pass the argument \'\--external-launcher\' to srun in order to not consider these hydra processes as regular steps. This automatic variable injection mechanism can be disabled by setting \"MpiParams=disable_slurm_hydra_bootstrap\" in slurm.conf, with the exception of the cases where \"slurm\" is already explicitly set as a bootstrap.

It is possible to run MPICH using a different bootstrap mechanism. To do so, explicitly set the following environment variable prior to submitting the job with sbatch or salloc:

    $ export HYDRA_BOOTSTRAP=ssh
    $ salloc -N10
    $ mpirun -np <num_procs> user_app.bin

### MPICH with srun and linked with Slurm\'s PMI-1 or PMI-2 libs {#mpich_pmi_slurm}

MPICH can be built specifically for use with Slurm and its PMI-1 or PMI-2 libraries using a configure line similar to that shown below. Building this way will force the use of this library on every execution. Note that the LD_LIBRARY_PATH may not be necessary depending on your Slurm installation path:

For PMI-2:

    user@testbox:~/mpich-4.0.2/build$ LD_LIBRARY_PATH=~/slurm/22.05/inst/lib/ \
    > ../configure --prefix=/home/user/bin/mpich/ --with-pmilib=slurm \
    > --with-pmi=pmi2 --with-slurm=/home/lipi/slurm/master/inst

or for PMI-1:

    user@testbox:~/mpich-4.0.2/build$ LD_LIBRARY_PATH=~/slurm/22.05/inst/lib/ \
    > ../configure --prefix=/home/user/bin/mpich/ --with-pmilib=slurm \
    > --with-slurm=/home/user/slurm/22.05/inst

These configure lines will detect the Slurm\'s installed PMI libraries and link against them, but **will not install** the mpiexec commands. Since PMI-1 is already old and doesn\'t scale well we don\'t recommend you link against it. It is preferable to use PMI-2. You can follow this example to run a job with PMI-2:

    $ mpicc -o hello_world hello_world.c
    $ srun --mpi=pmi2 ./hello_world

A Slurm upgrade will not affect this MPICH installation. There is only one unlikely scenario where a recompile of the MPI stack would be needed after an upgrade, which is when we forcibly link against Slurm\'s PMI-1 and/or PMI-2 libraries and if their APIs ever changed. These should not change often but if it were to happen, it would be noted in Slurm\'s RELEASE_NOTES file.

### MPICH with PMIx and integrated with Slurm {#mpich_slurm_pmix}

You can also build MPICH using an external PMIx library which should be the same one used when building Slurm:

    $ LD_LIBRARY_PATH=~/slurm/22.05/inst/lib/ ../configure \
    > --prefix=/home/user/bin/mpich/ \
    > --with-pmix=/home/user/bin/pmix_4.1.2/ \
    > --with-pmi=pmix \
    > --with-slurm=/home/user/slurm/master/inst

After building this way, any execution must be made with Slurm (srun) since the Hydra process manager is not installed, as it was in previous examples. Compile and run a process with:

    $ mpicc -o hello_world hello_world.c
    $ srun --mpi=pmix ./hello_world

### MPICH with its internal PMI and integrated with Slurm {#mpich_slurm_hydra}

Another option is to just compile MPICH but not set **\--with-pmilib**, **\--with-pmix** or **\--with-pmi**, and only keep **\--with-slurm**. In that case, MPICH will not forcibly link against any PMI libraries and it will install the mpiexec.hydra command by default. This will cause it to use its internal PMI implementation (based on PMI-1) and Slurm API functions to detect the job environment and launch processes accordingly:

    user@testbox:~/mpich-4.0.2/build$ ../configure \
    > --prefix=/home/user/bin/mpich/ \
    > --with-slurm=/home/user/slurm/22.05/inst

Then the app can be run with srun or mpiexec:

    $ mpicc -o hello_world hello_world.c
    $ srun ./hello_world

or

    $ mpiexec.hydra ./hello_world

mpiexec.hydra will spawn its daemons using Slurm steps launched with srun and will use its internal PMI implementation.

**NOTE**: In this case, compiling with the **\--with-slurm** option created the Hydra bootstrap commands (mpiexec.hydra and others) and linked them against the versioned Slurm\'s main public API (libslurm.so.X.0.0). That is because these commands use some Slurm functions to detect the job environment. Be aware then that upgrading Slurm would need a recompile of the MPICH stack. It is usually enough to symlink the name of the linked library to the new one, but this is not guaranteed to work.

### MPICH without Slurm integration {#mpich_hydra}

Finally, it is possible to compile MPICH without integrating it with Slurm. In that case it will not identify the job and will just run the processes as if it were on a local machine. We recommend reading MPICH documentation and the configure scripts for more information on the existing possibilities.

------------------------------------------------------------------------

## https://mvapich.cse.ohio-state.edu/ {#mvapich2}

MVAPICH2 has support for Slurm. To enable it you need to build MVAPICH2 with a command similar to this:

    $ ./configure --prefix=/home/user/bin/mvapich2 \
    > --with-slurm=/home/user/slurm/22.05/inst/

**NOTE**:In certain MVAPICH2 versions and when building with GCC \> 10.x, it is possible that these flags must be prepended to the configure line:

    FFLAGS="-std=legacy" FCFLAGS="-std=legacy" ./configure ...

When MVAPICH2 is built with Slurm support it will detect that it is within a Slurm allocation, and will use the \'srun\' command to spawn its hydra daemons. It does not link to the Slurm API, which means that during an upgrade of Slurm there is no need to recompile MVAPICH2. By default it will use the internal PMI implementation.

Note that by default Slurm will inject two environment variables to ensure mpirun or mpiexec will use the Slurm bootstrap mechanism (srun) to launch Hydra. With these, Hydra will also pass the argument \'\--external-launcher\' to srun in order to not consider these hydra processes as regular steps. This automatic variable injection mechanism can be disabled by setting \"MpiParams=disable_slurm_hydra_bootstrap\" in slurm.conf, with the exception of the cases where \"slurm\" is already explicitly set as a bootstrap.

It is possible to run MVAPICH2 using a different bootstrap mechanism. To do so, explicitly set the following environment variable prior to submitting the job with sbatch or salloc:

    $ export HYDRA_BOOTSTRAP=ssh
    $ salloc -N10
    $ mpirun -np <num_procs> user_app.bin

### MVAPICH2 with srun and linked with Slurm\'s PMI-1 or PMI-2 libs {#mvapich_pmi_slurm}

It is possible to force MVAPICH2 to use one of the Slurm\'s PMI-1 (libpmi.so.0.0.0)or PMI-2 (libpmi2.so.0.0.0) libraries. Building with this mode will cause all the executions to use Slurm and its PMI libraries. The Hydra process manager binaries (mpiexec) won\'t be installed. In fact the mpiexec command will exist as a symbolic link to Slurm\'s srun command. It is recommended not to use PMI-1, but to use at least PMI-2 libs. See below for an example of how to configure and usage:

    For PMI-2:

    ./configure --prefix=/home/user/bin/mvapich2 \
    > --with-slurm=/home/user/slurm/master/inst/  \
    > --with-pm=slurm --with-pmi=pmi2

    and for PMI-1:

    ./configure --prefix=/home/user/bin/mvapich2 \
    > --with-slurm=/home/user/slurm/master/inst/ \
    > --with-pm=slurm --with-pmi=pmi1

To compile and run a user application in Slurm:

    $ mpicc -o hello_world hello_world.c
    $ srun --mpi=pmi2 ./hello_world

For more information, please see the MVAPICH2 documentation on their https://mvapich.cse.ohio-state.edu/

### MVAPICH2 with Slurm support and linked with external PMIx {#mvapich_pmix_slurm}

It is possible to use PMIx within MVAPICH2 and integrated with Slurm. This way no Hydra Process Manager will be installed and the user apps will need to run with srun, assuming Slurm has been compiled against the same or a compatible PMIx version as the one used when building MVAPICH2.

To build MVAPICH2 to use PMIx and integrated with Slurm, a configuration line similar to this is needed:

    ./configure --prefix=/home/user/bin/mvapich2 \
    > --with-slurm=/home/user/slurm/master/inst/ \
    > --with-pm=slurm \
    > --with-pmix=/home/user/bin/pmix_4.1.2/ \
    > --with-pmi=pmix

Running a job looks similar to previous examples:

    $ mpicc -o hello_world hello_world.c
    $ srun --mpi=pmix ./hello_world

**NOTE**: In the MVAPICH2 case, compiling with integration with Slurm (**\--with-slurm**) doesn\'t add any dependency to commands or libraries, so upgrading Slurm should be safe without any need to recompile MVAPICH2. There is only one unlikely scenario where a recompile of the MPI stack would be needed after an upgrade, which is when we forcibly link against Slurm\'s PMI-1 and/or PMI-2 libraries and if their APIs ever changed. These should not change often but if it were to happen, it would be noted in Slurm\'s RELEASE_NOTES file.

## **HPE Cray PMI support** {#hpe_cray_pmi}

Slurm comes by default with a Cray PMI vendor-specific plugin which provides compatibility with the HPE Cray Programming Environment\'s PMI. It is intended to be used in applications built with this environment on HPE Cray machines.

The plugin is named *cray_shasta* (Shasta was the first Cray architecture this plugin supported) and built by default in all Slurm installations. Its availability is shown by running the following command:

    $ srun --mpi=list
    MPI plugin types are...
        cray_shasta
        none

The Cray PMI plugin will use some reserved ports for its communication. These ports are configurable by using *\--resv-ports* option on the command line with **srun**, or by setting *MpiParams=ports*=\[*port_range*\] in your slurm.conf. The first port listed in this option will be used as the PMI control port, defined by Cray as the **PMI_CONTROL_PORT** environment variable. There cannot be more than one application launched in the same node using the same **PMI_CONTROL_PORT**.

This plugin does not support MPMD/heterogeneous jobs and it requires *libpals \>= 0.2.8*.
