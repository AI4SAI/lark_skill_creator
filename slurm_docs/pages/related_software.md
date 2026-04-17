# Related Software

Slurm source can be downloaded from https://www.schedmd.com/download-slurm/.

Note that the following related software is not written or maintained by SchedMD. Some of the software is required for certain functionality (e.g. MySQL or MariaDB are required to use slurmdbd) while other software was written to provide additional functionality for users or administrators.

- **Authentication** plugins identifies the user originating a message.
  - **MUNGE** (recommended)\
    In order to compile the \"auth/munge\" authentication plugin for Slurm, you will need to build and install MUNGE, available from https://dun.github.io/munge/ and http://packages.debian.org/src:munge and http://fedoraproject.org/ and http://packages.ubuntu.com/src:munge.

- **Authentication** tools for users that work with Slurm.
  - https://github.com/hautreux/auks\
    AUKS is an utility designed to ease Kerberos V credential support addition to non-interactive applications, like batch systems (Slurm, LSF, Torque, etc.). It includes a plugin for the Slurm workload manager. AUKS is not used as an authentication plugin by the Slurm code itself, but provides a mechanism for the application to manage Kerberos V credentials.

- **Databases** can be used to store accounting information. See our [Accounting](accounting.md) web page for more information.
  - http://www.mysql.com/
  - https://mariadb.org/

  \

- **DRMAA (Distributed Resource Management Application API)**\
  https://github.com/psnc-apps/slurm-drmaa for Slurm is an implementation of http://www.gridforum.org/ http://www.drmaa.org/ (Distributed Resource Management Application API) http://www.ogf.org/documents/GFD.133.pdf for submission and control of jobs to [Slurm](index.md). Using DRMAA, grid applications builders, portal developers and ISVs can use the same high-level API to link their software with different cluster/resource management systems.\
  \
  There is a variant of PSNC DRMAA providing support for Slurm\'s \--cluster option available from https://github.com/natefoo/slurm-drmaa.\
  \
  Perl 6 DRMAA bindings are available from https://github.com/scovit/Scheduler-DRMAA.
  \

- **Hardware topology**
  - http://www.open-mpi.org/projects/hwloc/
  - **NOTE**: If you build Slurm or any MPI stack component with hwloc, note that versions 2.5.0 through 2.7.0 (inclusive) of hwloc have a bug that pushes an untouchable value into the environ array, causing a segfault when accessing it. It is advisable to build with hwloc version 2.7.1 or later.
  - Used by slurmd and PMIx client to get hardware topology information.

- **Hostlist**\
  A Python program used for manipulation of Slurm hostlists including functions such as intersection and difference. Download the code from:\
  http://www.nsc.liu.se/\~kent/python-hostlist\
  \
  Lua bindings for hostlist functions are also available here:\
  https://github.com/grondo/lua-hostlist\
  **NOTE**: The Lua hostlist functions do not support the bracketed numeric ranges anywhere except at the end of the name (i.e. \"tux\[0001-0100\]\" and \"rack\[0-3\]\_blade\[0-63\]\" are not supported).
  \

- **MPI** versions supported
  - https://software.intel.com/en-us/intel-mpi-library
  - https://www.mpich.org/
  - http://mvapich.cse.ohio-state.edu/
  - https://www.open-mpi.org/

- **Command wrappers**\
  There is a wrapper for Maui/Moab\'s showq command https://github.com/pedmon/slurm_showq.
  \

- **Scripting interfaces**
  - A **Perl** interface is included in the Slurm distribution in the *contribs/perlapi* directory and packaged in the *perlapi* RPM.
  - https://github.com/pyslurm/ is a Python/Cython module to interface with Slurm. There is also a Python module to expand and collect hostlist expressions available http://www.nsc.liu.se/\~kent/python-hostlist/.

  \

- **SPANK Plugins**\
  SPANK provides a very generic interface for stackable plug-ins which may be used to dynamically modify the job launch code in Slurm. SPANK plugins may be built without access to Slurm source code. They need only be compiled against Slurm's spank.h header file, added to the SPANK config file plugstack.conf, and they will be loaded at runtime during the next job launch. Thus, the SPANK infrastructure provides administrators and other developers a low cost, low effort ability to dynamically modify the runtime behavior of Slurm job launch. Additional documentation can be found [here](spank.md).
  \

- **Node Health Check**\
  Probably the most comprehensive and lightweight health check tool out there is https://github.com/mej/nhc. It has integration with Slurm as well as Torque resource managers.
  \

- **Accounting Tools**
  - **UBMoD** is a web based tool for displaying accounting data from various resource managers. It aggregates the accounting data from sacct into a MySQL data warehouse and provide a front end web interface for browsing the data. For more information, see the http://ubmod.sourceforge.net/resource-manager-slurm.html and https://github.com/ubccr/ubmod.\
  - http://xdmod.sourceforge.net/ (XD Metrics on Demand) is an NSF-funded open source tool designed to audit and facilitate the utilization of the XSEDE cyberinfrastructure by providing a wide range of metrics on XSEDE resources, including resource utilization, resource performance, and impact on scholarship and research.

  \

- **STUBL (Slurm Tools and UBiLities)**\
  STUBL is a collection of supplemental tools and utility scripts for Slurm.\
  https://github.com/ubccr/stubl.
  \

- **pestat**\
  Prints a consolidated compute node status line, with one line per node including a list of jobs.\
  https://github.com/OleHolmNielsen/Slurm_tools/tree/master/pestat
  \

- **Graphical Sdiag**\
  The sdiag utility is a diagnostic tool that maintains statistics on Slurm\'s scheduling performance. You can run sdiag periodically or as you modify Slurm\'s configuration. However if you want a historical view of these statistics, you could save them in a time-series database and graph them over time as performed with this tool:
  - https://github.com/fasrc/slurm-diamond-collector
  - https://github.com/collectd/collectd/pull/1198 (for use with https://github.com/edf-hpc/jobmetrics)

  \

- https://github.com/json-c/json-c/wiki

  Some Slurm plugins ([slurmrestd](rest.md), [burst_buffer/datawarp](burst_buffer.md), [burst_buffer/lua](burst_buffer.md), [jobcomp/elasticsearch](elasticsearch.md), and [jobcomp/kafka](jobcomp_kafka.md)) parse and/or serialize JSON format data. These plugins and slurmrestd are designed to make use of the **JSON-C library (\>= v0.15)** for this purpose. Instructions for the build are as follows:

      git clone --depth 1 --single-branch -b json-c-0.15-20200726 https://github.com/json-c/json-c.git json-c
      mkdir json-c-build
      cd json-c-build
      cmake ../json-c
      make
      sudo make install

  Declare the package configuration path before compiling Slurm (example provided for /bin/sh):

      export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/:$PKG_CONFIG_PATH

  \

- https://github.com/nodejs/http-parser

  [slurmrestd](rest.md) requires **libhttp_parser (\>= v2.6.0)**. Instructions for the build are as follows:

      git clone --depth 1 --single-branch -b v2.9.4 https://github.com/nodejs/http-parser.git http_parser
      cd http_parser
      make
      sudo make install

  Add the following argument when running *configure* for Slurm:

      --with-http-parser=/usr/local/

  \

- https://github.com/yaml/libyaml

  [slurmrestd](rest.md) and commands that recognize a `--yaml` flag will be able to parse YAML if **libyaml (\>= v0.2.5)** is present. Instructions for the build are as follows:

      git clone --depth 1 --single-branch -b 0.2.5 https://github.com/yaml/libyaml libyaml
      cd libyaml
      ./bootstrap
      ./configure
      make
      sudo make install

  Add the following argument when running *configure* for Slurm:

      --with-yaml=/usr/local/

  \

- https://github.com/benmcollins/libjwt

  [JWT authentication](jwt.md) requires **libjwt (\>= v1.10.0 and \< v2)**. Instructions for the build are as follows:

      git clone --depth 1 --single-branch -b v1.12.0 https://github.com/benmcollins/libjwt.git libjwt
      cd libjwt
      autoreconf --force --install
      ./configure --prefix=/usr/local
      make -j
      sudo make install

  Add the following argument when running *configure* for Slurm:

      --with-jwt=/usr/local/

  \
