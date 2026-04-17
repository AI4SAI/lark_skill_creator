# acct_gather.conf

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

**acct_gather.conf** - Slurm configuration file for the acct_gather plugins

[ ]{#lbAC}

## DESCRIPTION

**acct_gather.conf** is a UTF8 formatted file which defines parameters used by Slurm\'s acct_gather related plugins. The file will always be located in the same directory as the **slurm.conf**.

Parameter names are case insensitive but parameter values are case sensitive. Any text following a \"#\" in the configuration file is treated as a comment through the end of that line. The size of each line in the file is limited to 1024 characters.

Changes to the configuration file take effect upon restart of the Slurm daemons.

The following **acct_gather.conf** parameters are defined to control the general behavior of various plugins in Slurm.

The **acct_gather.conf** file is different than other Slurm .conf files. Each plugin defines which options are available. Each plugin to be loaded must be specified in the **slurm.conf** under the following configuration entries:

• AcctGatherEnergyType (plugin type=*acct_gather_energy*)\
• AcctGatherInterconnectType (plugin type=*acct_gather_interconnect*)\
• AcctGatherFilesystemType (plugin type=*acct_gather_filesystem*)\
• AcctGatherProfileType (plugin type=*acct_gather_profile*)

If the respective plugin for an option is not loaded then that option will be unknown to Slurm, causing the daemon to fatal on initialization. If you decide to change plugin types in **slurm.conf**, also make sure to change the related options in **acct_gather.conf**.

[ ]{#lbAD}

## acct_gather_energy/gpu

Required entry in slurm.conf:

:   AcctGatherEnergyType=acct_gather_energy/gpu

This plugin doesn\'t read any options from **acct_gather.conf**.\
Dataset provided by the plugin is: Energy.

:   

[ ]{#lbAE}

## acct_gather_energy/IPMI

Required entry in slurm.conf:

:   AcctGatherEnergyType=acct_gather_energy/ipmi

Options used for acct_gather_energy/ipmi are as follows:

:   

    **EnergyIPMIFrequency**=\<number\>
    :   This parameter is the number of seconds between BMC access samples. Ideally it should be higher or equal to **JobAcctGatherFrequency**, otherwise the JobAcctGather plugin will get repeated values in successive polls.

    :   

    **EnergyIPMICalcAdjustment**=\<yes\|no\>
    :   If set to \"yes\", the consumption between the last BMC access sample and a step consumption update is approximated to get more accurate task consumption. The adjustment is made at the step start and each time the consumption is updated, including the step end. The approximations are not accumulated, only the first and last adjustments are used to calculated the consumption. The default is \"no\".

    :   

    **EnergyIPMIPowerSensors**=\<key=values\>

    :   Optionally specify the ids of the sensors to used. Multiple \<key=values\> can be set with \";\" separators. The key \"Node\" is mandatory and is used to know the consumed energy for nodes (scontrol show node) and jobs (sacct). Other keys are optional and are named by administrator. These keys are useful only when profile is activated for energy to store power (in watt) of each key. \<values\> are integers except when using DCMI. Multiple values can be set with \",\" separators. The sum of the listed sensors is used for each key. EnergyIPMIPowerSensors is optional, default value is \"Node=\<value\>\" where \"\<value\>\" is the id of the first power sensor returned by ipmi-sensors.\
        i.e.\
        EnergyIPMIPowerSensors=Node=16,19,23,26;Socket0=16,23;Socket1=19,26;SSUP=23,26;KNC=16,19\
        EnergyIPMIPowerSensors=Node=29,32;SSUP0=29;SSUP1=32\
        EnergyIPMIPowerSensors=Node=1280

        Data Center Manageability Interface - acct_gather_energy/ipmi supports gathering power data through DCMI IPMI extension commands. When configured, the ipmi plugin will query the DCMI using the \"System Power mode\" or the \"Enhanced System Power Statistics mode\" flags depending on the configuration.

        To configure one or the other, the special sensor values DCMI or DCMI_ENHANCED can be used, for example:\
        EnergyIPMIPowerSensors=Node=DCMI\
        EnergyIPMIPowerSensors=Node=DCMI_ENHANCED

    The following **acct_gather.conf** parameters are defined to control the IPMI config default values for libipmiconsole.

    **EnergyIPMIUsername**=*USERNAME*
    :   Specify BMC Username.

    :   

    **EnergyIPMIPassword**=*PASSWORD*
    :   Specify BMC Password.

Datasets provided by the plugin have name: \<IPMI_SENSOR_LABEL\>Power.

:   

[ ]{#lbAF}

### NOTES:

This plugin requires the freeipmi development files to be installed and linkable at configure time. The plugin will not build otherwise. When building the RPM, *rpmbuild \... \--with freeipmi* can be specified to explicitly check for these dependencies.

[ ]{#lbAG}

## acct_gather_energy/rapl

Required entry in slurm.conf:

:   AcctGatherEnergyType=acct_gather_energy/rapl

This plugin doesn\'t read any options from **acct_gather.conf**.\
Dataset provided by the plugin is: Power.

:   

[ ]{#lbAH}

## acct_gather_energy/XCC

Required entry in slurm.conf:

:   AcctGatherEnergyType=acct_gather_energy/xcc

Options used for acct_gather_energy/xcc include only in-band communications with XClarity Controller, thus a reduced set of configurations is supported:

:   

    **EnergyIPMIFrequency**=\<number\>
    :   This parameter is the number of seconds between XCC access samples. Default is 30 seconds.

    :   

    **EnergyIPMITimeout**=\<number\>
    :   Timeout, in seconds, for initializing the IPMI XCC context for a new gathering thread. Default is 10 seconds.

Datasets provided by the plugin are: Energy, CurrPower.

:   

[ ]{#lbAI}

## acct_gather_filesystem/lustre

Required entry in slurm.conf:

:   AcctGatherFilesystemType=acct_gather_filesystem/lustre

This plugin doesn\'t read any options from **acct_gather.conf**.\
Datasets provided by the plugin are: Reads, ReadMB, Writes, WriteMB.

:   

[ ]{#lbAJ}

## acct_gather_profile/HDF5

Required entry in slurm.conf:

:   AcctGatherProfileType=acct_gather_profile/hdf5

Options used for acct_gather_profile/hdf5 are as follows:

:   

    **ProfileHDF5Dir**=\<path\>
    :   This parameter is the path to the shared folder into which the acct_gather_profile plugin will write detailed data (usually as an HDF5 file). The directory is assumed to be on a file system shared by the controller and all compute nodes. This is a required parameter.

    :   

    **ProfileHDF5Default**
    :   A comma-delimited list of data types to be collected for each job submission. Allowed values are:

        :   

            **All**
            :   All data types are collected. (Cannot be combined with other values.)

            :   

            **None**
            :   No data types are collected. This is the default. (Cannot be combined with other values.)

            :   

            **Energy**
            :   Energy data is collected.

            :   

            **Filesystem**
            :   File system (Lustre) data is collected.

            :   

            **Network**
            :   Network (InfiniBand) data is collected.

            :   

            **Task**
            :   Task (I/O, Memory, \...) data is collected.

            :   

[ ]{#lbAK}

## acct_gather_profile/InfluxDB

Required entry in slurm.conf:

:   AcctGatherProfileType=acct_gather_profile/influxdb

The InfluxDB plugin provides the same information as the HDF5 plugin but will instead send information to the configured InfluxDB server.

The InfluxDB plugin is designed against 1.x protocol of InfluxDB. Any site running a v2.x InfluxDB server will need to configure a v1.x compatibility endpoint along with the correct user and password authorization. Token authentication is not currently supported. [ ]{#lbAL}

### Options:

**ProfileInfluxDBDatabase**
:   InfluxDB v1.x database name where profiling information is to be written. InfluxDB v2.x bucket name where profiling information is to be written.

:   

**ProfileInfluxDBDefault**
:   A comma-delimited list of data types to be collected for each job submission. Allowed values are:

:   

    :   

        **All**
        :   All data types are collected. Cannot be combined with other values.

        :   

        **None**
        :   No data types are collected. This is the default. Cannot be combined with other values.

        :   

        **Energy**
        :   Energy data is collected.

        :   

        **Filesystem**
        :   File system (Lustre) data is collected.

        :   

        **Network**
        :   Network (InfiniBand) data is collected.

        :   

        **Task**
        :   Task (I/O, Memory, \...) data is collected.

:   

**ProfileInfluxDBFrequency**=\<seconds\>
:   How often in seconds data should be sent to the InfluxDB server. Note that in practice, profile data will be sent no more often than every JobAcctGatherFrequency seconds. A value of 0 disables buffering in the plugin so that data is sent to the InfluxDB server as soon it is collected. In all cases, data is sent to InfluxDB whenever the plugin\'s internal buffer is full and at the end of each job step. Default is 30 seconds.

:   

**ProfileInfluxDBHost**=\<hostname\>:\<port\>

:   The hostname of the machine where the *InfluxDB* instance is executed and the port used by the HTTP API. The port used by the HTTP API is the one configured through the bind-address influxdb.conf option in the \[http\] section. Example:

        ProfileInfluxDBHost=myinfluxhost:8086

:   

**ProfileInfluxDBPass**
:   Password for username configured in ProfileInfluxDBUser. Required in v2.x and optional in v1.x InfluxDB.

:   

**ProfileInfluxDBRTPolicy**
:   The InfluxDB v1.x retention policy name for the database configured in ProfileInfluxDBDatabase option. The InfluxDB v2.x retention policy bucket name for the database configured in ProfileInfluxDBDatabase option.

:   

**ProfileInfluxDBUser**
:   InfluxDB username that should be used to gain access to the database configured in ProfileInfluxDBDatabase. Required in v2.x and optional in v1.x InfluxDB. This is only needed if InfluxDB v1.x is configured with authentication enabled in the \[http\] config section and a user has been granted at least WRITE access to the database. See also **ProfileInfluxDBPass**.

:   

**ProfileInfluxDBTimeout**=\<seconds\>
:   The maximum time in seconds that an HTTP query to the InfluxDB server can take. After this timeout the data is discarded. Be aware that a long timeout can drain your nodes if the InfluxDB server is unresponsive and, when terminating the job, the last dataset takes more than UnkillableStepTimeout to be sent. Internally, that option sets CURLOPT_TIMEOUT library option. Default is 10 seconds.

:   

[ ]{#lbAM}

### NOTES:

This plugin requires the libcurl development files to be installed and linkable at configure time. The plugin will not build otherwise.

Information on how to install and configure InfluxDB and manage databases, retention policies and such is available on the official webpage.

Collected information is written from every compute node where a job runs to the *InfluxDB* instance listening on the ProfileInfluxDBHost. In order to avoid overloading the *InfluxDB* instance with incoming connection requests, the plugin uses an internal buffer which is filled with samples. Once the buffer is full, a HTTP API write request is performed and the buffer is emptied to hold subsequent samples. A final request is also performed when a task ends even if the buffer isn\'t full.

Failed HTTP API write requests are silently discarded. This means that collected profile information in the plugin buffer is lost if it can\'t be written to the *InfluxDB* database for any reason.

Plugin messages are logged along with the slurmstepd logs to SlurmdLogFile. In order to troubleshoot any issues, it is recommended to temporarily increase the slurmd debug level to debug3 and add Profile to the debug flags. This can be accomplished by setting the slurm.conf SlurmdDebug and DebugFlags respectively or dynamically through scontrol setdebug and setdebugflags.

Grafana can be used to create charts based on the data held by InfluxDB. This kind of tool permits one to create dashboards, tables and other graphics using the stored time series.

[ ]{#lbAN}

## acct_gather_interconnect/OFED

Required entry in slurm.conf:

:   AcctGatherInterconnectType=acct_gather_interconnect/ofed

Options used for acct_gather_interconnect/ofed are as follows:

:   

    **InfinibandOFEDPort**=\<number\>
    :   This parameter represents the port number of the local Infiniband card that we are willing to monitor. The default port is 1.

Datasets provided by the plugin: PacketsIn, PacketsOut, InMB, OutMB

[ ]{#lbAO}

## acct_gather_interconnect/sysfs

Required entry in slurm.conf:

:   AcctGatherInterconnectType=acct_gather_interconnect/sysfs

Options used for acct_gather_interconnect/sysfs are as follows:

:   

    **SysfsInterfaces**=\<interfaces\>
    :   Comma-separated list of interface names to collect statistics from. Usage from all listed interfaces will be summed together, and is not broken down individually.

Datasets provided by the plugin: PacketsIn, PacketsOut, InMB, OutMB

[ ]{#lbAP}

## EXAMPLE

    ###
    # Slurm acct_gather configuration file
    ###
    # Parameters for acct_gather_energy/impi plugin
    EnergyIPMIFrequency=10
    EnergyIPMICalcAdjustment=yes
    #
    # Parameters for acct_gather_profile/hdf5 plugin
    ProfileHDF5Dir=/app/slurm/profile_data
    # Parameters for acct_gather_interconnect/ofed plugin
    InfinibandOFEDPort=1

[ ]{#lbAQ}

## COPYING

Copyright (C) 2012-2013 Bull. Copyright (C) 2012-2022 SchedMD LLC. Produced at Bull (cf, DISCLAIMER).

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAR}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

DESCRIPTION

:   

acct_gather_energy/gpu

:   

acct_gather_energy/IPMI

:   

    NOTES:

    :   

acct_gather_energy/rapl

:   

acct_gather_energy/XCC

:   

acct_gather_filesystem/lustre

:   

acct_gather_profile/HDF5

:   

acct_gather_profile/InfluxDB

:   

    Options:

    :   

    NOTES:

    :   

acct_gather_interconnect/OFED

:   

acct_gather_interconnect/sysfs

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
