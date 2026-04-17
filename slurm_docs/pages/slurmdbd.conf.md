# slurmdbd.conf

Section: Slurm Configuration File (5)\
Updated: Slurm Configuration File\
Index

[ ]{#lbAB}

## NAME

slurmdbd.conf - Slurm Database Daemon (SlurmDBD) configuration file

[ ]{#lbAC}

## DESCRIPTION

**slurmdbd.conf** is an ASCII file which describes Slurm Database Daemon (SlurmDBD) configuration information. The file will always be located in the same directory as the **slurm.conf**.

The contents of the file are case insensitive except for the names of nodes and files. Any text following a \"#\" in the configuration file is treated as a comment through the end of that line. Changes to the configuration file take effect upon restart of SlurmDBD or daemon receipt of the SIGHUP signal unless otherwise noted.

This file should be only on the machine where SlurmDBD executes, owned by the SlurmUser or root, and have permissions set to 600 or 640. If the slurmdbd daemon is started as user root and changes to another user ID, the configuration file will initially be read as user root, but will be read as the other user ID in response to a SIGHUP signal. This file should be protected from unauthorized access since it contains a database password. The overall configuration parameters available include:

**AllowNoDefAcct**
:   Remove requirement for users to have a default account. Boolean, yes to turn on, no (default) to enforce default accounts.

:   

**AllResourcesAbsolute**
:   When adding a resource (license) treat allocated/allowed counts as absolute numbers instead of percentage numbers. Boolean, yes to turn on, no (default) to use the numbers as percentages instead.

:   

**ArchiveDir**
:   If ArchiveScript is not set the slurmdbd will generate a file that can be read in anytime with sacctmgr load filename. This directory is where the file will be placed after a purge event has happened and archive for that element is set to true. Default is /tmp. The format for this files name is \$ArchiveDir/\$ClusterName\_\$ArchiveObject_archive\_\$BeginTimeStamp\_\$endTimeStamp We limit archive files to **MaxPurgeLimit** records per file. If more records exist during that time period, they will be written to a new file. Subsequent archive files during the same time period will have \".\<number\>\" appended to the file, for example .2, with the number increasing by one for each file in the same time period.

:   

**ArchiveEvents**
:   When purging events also archive them. Boolean, yes to archive event data, no otherwise. Default is no.

:   

**ArchiveJobs**
:   When purging jobs also archive them. Boolean, yes to archive job data, no otherwise. Default is no.

:   

**ArchiveResvs**
:   When purging reservations also archive them. Boolean, yes to archive reservation data, no otherwise. Default is no.

:   

**ArchiveScript**
:   This script can be executed every time a rollup happens (every hour, day and month), depending on the Purge\*After options. This script is used to transfer accounting records out of the database into an archive. It is used in place of the internal process used to archive objects. The script is executed with no arguments, and the following environment variables are set.

:   

    :   

        **SLURM_ARCHIVE_EVENTS**
        :   1 for archive events 0 otherwise.

        :   

        **SLURM_ARCHIVE_LAST_EVENT**
        :   Time of last event start to archive.

        :   

        **SLURM_ARCHIVE_JOBS**
        :   1 for archive jobs 0 otherwise.

        :   

        **SLURM_ARCHIVE_LAST_JOB**
        :   Time of last job submit to archive.

        :   

        **SLURM_ARCHIVE_STEPS**
        :   1 for archive steps 0 otherwise.

        :   

        **SLURM_ARCHIVE_LAST_STEP**
        :   Time of last step start to archive.

        :   

        **SLURM_ARCHIVE_SUSPEND**
        :   1 for archive suspend data 0 otherwise.

        :   

        **SLURM_ARCHIVE_TXN**
        :   1 for archive transaction data 0 otherwise.

        :   

        **SLURM_ARCHIVE_USAGE**
        :   1 for archive usage data 0 otherwise.

        :   

        **SLURM_ARCHIVE_LAST_SUSPEND**
        :   Time of last suspend start to archive.

:   

**ArchiveSteps**
:   When purging steps also archive them. Boolean, yes to archive step data, no otherwise. Default is no.

:   

**ArchiveSuspend**
:   When purging suspend data also archive it. Boolean, yes to archive suspend data, no otherwise. Default is no.

:   

**ArchiveTXN**
:   When purging transaction data also archive it. Boolean, yes to archive transaction data, no otherwise. Default is no.

:   

**ArchiveUsage**
:   When purging usage data (Cluster, Association and WCKey) also archive it. Boolean, yes to archive transaction data, no otherwise. Default is no.

:   

**AuthAltTypes**
:   Comma-separated list of alternative authentication plugins that the slurmdbd will permit for communication. Acceptable values at present include **auth/jwt**.
    **NOTE**: The path to the required jwt_hs256.key must be specified with **AuthAltParameters**. The jwt_hs256.key should only be visible to the SlurmUser and root. It is not suggested to place the jwt_hs256.key on any nodes other than the machine running **slurmctld** and the machine running **slurmdbd**. **auth/jwt** can be activated by the presence of the *SLURM_JWT* environment variable. When activated, it will override the default

:   

**AuthAltParameters**
:   Used to define alternative authentication plugins options. Multiple options may be comma separated.

:   

    :   

        **jwks**=
        :   Absolute path to JWKS file. Key should be owned by SlurmUser or root, must be readable by SlurmUser, with suggested permissions of 0400. It must not be writable by \'other\'. Only RS256 keys are supported, although other key types may be listed in the file. If set, no HS256 key will be loaded by default (and token generation is disabled), although the jwt_key setting may be used to explicitly re-enable HS256 key use (and token generation).

        :   

        **jwt_key**=
        :   Absolute path to JWT key file. Key must be HS256. Key should be owned by SlurmUser or root, must be readable by SlurmUser, with suggested permissions of 0400. It must not be accessible by \'other\'.

:   

**AuthInfo**
:   Additional information to be used for authentication of communications with the Slurm control daemon (slurmctld) on each cluster. The interpretation of this option is specific to the configured **AuthType**. Multiple options may be specified in a comma-delimited list. If not specified, the default authentication information will be used.

:   

    :   

        **socket**
        :   Path name to a MUNGE daemon socket to use (e.g. \"socket=/var/run/munge/munge.socket.2\"). The default value is \"/var/run/munge/munge.socket.2\". Used by *auth/munge* and *cred/munge*.

        :   

        **ttl**
        :   Credential lifetime, in seconds (e.g. \"ttl=300\"). The default value is dependent upon the MUNGE installation, but is typically 300 seconds.

        :   

        **use_client_ids**
        :   Allow the *auth/slurm* plugin to authenticate users without relying on the user information from LDAP or the operating system.

:   

**AuthType**
:   Define the authentication method for communications between Slurm components. SlurmDBD must be terminated prior to changing the value of **AuthType** and later restarted. This should match the **AuthType** used in slurm.conf. Acceptable values at present:

    :   

        **auth/munge**
        :   Indicates that MUNGE is to be used (default). (See \"https://dun.github.io/munge/\" for more information).

        :   

        **auth/slurm**
        :   Use Slurm\'s internal authentication plugin.

:   

**CommitDelay**
:   How many seconds between commits on a connection from a Slurmctld. This speeds up inserts into the database dramatically. If you are running a very high throughput of jobs you should consider setting this. In testing, 1 second improves the slurmdbd performance dramatically and reduces overhead. There is a small probability of data loss though since this creates a window in which if the slurmdbd exits abnormally for any reason the data not committed could be lost. While this situation should be very rare, it does present an extremely small risk, but may be the only way to run in extremely heavy environments. In all honesty, the risk is quite low, but still present.

:   

**CommunicationParameters**
:   Comma separated options identifying communication options.

:   

    :   

        **DisableIPv4**
        :   Disable IPv4 only operation for the slurmdbd. This should also be set in your **slurm.conf** file.

        :   

        **EnableIPv6**
        :   Enable using IPv6 addresses for the slurmdbd. When using both IPv4 and IPv6, address family preferences will be based on your /etc/gai.conf file. This should also be set in your **slurm.conf** file.

        :   

        **keepaliveinterval**=#
        :   Specifies the interval, in seconds, between keepalive probes on idle connections. This affects most outgoing connections from the slurmdbd (e.g. between the primary and backup, or from the slurmdbd to the slurmctld). The default value is 30 seconds.

        :   

        **keepaliveprobes**=#
        :   Specifies the number of unacknowledged keepalive probes sent before considering a connection broken. This affects most outgoing connections from the slurmdbd (e.g. between the primary and backup, or from the slurmdbd to the slurmctld). The default value is 3.

        :   

        **keepalivetime**=#
        :   Specifies how long, in seconds, a connection must be idle before starting to send keepalive probes as well as how long to delay closing a connection to process messages still in the queue. This affects most outgoing connections from the slurmdbd (e.g. between the primary and backup, or from the slurmdbd to the slurmctld). The default value is 30 seconds.

:   

**DbdAddr**
:   Name that **DbdHost** should be referred to in establishing a communications path. This name will be used as an argument to the getaddrinfo() function for identification. For example, \"elx0000\" might be used to designate the Ethernet address for node \"lx0000\". By default the **DbdAddr** will be identical in value to **DbdHost**.

:   

**DbdBackupHost**
:   The short, or long, name of the machine where the backup Slurm Database Daemon is executed (i.e. the name returned by the command \"hostname -s\"). This host must have access to the same underlying database specified by the \'Storage\' options mentioned below.

:   

**DbdHost**
:   The short, or long, name of the machine where the Slurm Database Daemon is executed (i.e. the name returned by the command \"hostname -s\"). This value must be specified.

:   

**DbdPort**
:   The port number that the Slurm Database Daemon (slurmdbd) listens to for work. The default value is SLURMDBD_PORT as established at system build time. If no value is explicitly specified, it will be set to 6819. This value must be equal to the **AccountingStoragePort** parameter in the slurm.conf file.

:   

**DebugFlags**
:   Defines specific subsystems which should provide more detailed event logging. Multiple subsystems can be specified with comma separators. Most DebugFlags will result in additional logging messages for the identified subsystems if **DebugLevel** is at \'verbose\' or higher. More logging may impact performance. Valid subsystems available today (with more to come) include:

:   

    :   

        **AuditRPCs**
        :   For all inbound RPCs to slurmdbd, print the originating address, authenticated user, and RPC type before the connection is processed.

        :   

        **DB_ARCHIVE**
        :   SQL statements/queries when dealing with archiving and purging the database.

        :   

        **DB_ASSOC**
        :   SQL statements/queries when dealing with associations in the database.

        :   

        **DB_EVENT**
        :   SQL statements/queries when dealing with (node) events in the database.

        :   

        **DB_JOB**
        :   SQL statements/queries when dealing with jobs in the database.

        :   

        **DB_QOS**
        :   SQL statements/queries when dealing with QOS in the database.

        :   

        **DB_QUERY**
        :   SQL statements/queries when dealing with transactions and such in the database.

        :   

        **DB_RESERVATION**
        :   SQL statements/queries when dealing with reservations in the database.

        :   

        **DB_RESOURCE**
        :   SQL statements/queries when dealing with resources like licenses in the database.

        :   

        **DB_STEP**
        :   SQL statements/queries when dealing with steps in the database.

        :   

        **DB_TRES**
        :   SQL statements/queries when dealing with trackable resources in the database.

        :   

        **DB_USAGE**
        :   SQL statements/queries when dealing with usage queries and inserts in the database.

        :   

        **DB_WCKEY**
        :   SQL statements/queries when dealing with wckeys in the database.

        :   

        **FEDERATION**
        :   SQL statements/queries when dealing with federations in the database.

        :   

        **Network**
        :   Network details.

        :   

        **NetworkRaw**
        :   Dump raw hex values of key Network communications.

        :   

        **TLS**
        :   TLS plugin

:   

**DebugLevel**
:   The level of detail to provide the Slurm Database Daemon\'s logs. The default value is **info**.

:   

    :   

        **quiet**
        :   Log nothing

        :   

        **fatal**
        :   Log only fatal errors

        :   

        **error**
        :   Log only errors

        :   

        **info**
        :   Log errors and general informational messages

        :   

        **verbose**
        :   Log errors and verbose informational messages

        :   

        **debug**
        :   Log errors and verbose informational messages and debugging messages

        :   

        **debug2**
        :   Log errors and verbose informational messages and more debugging messages

        :   

        **debug3**
        :   Log errors and verbose informational messages and even more debugging messages

        :   

        **debug4**
        :   Log errors and verbose informational messages and even more debugging messages

        :   

        **debug5**
        :   Log errors and verbose informational messages and even more debugging messages

:   

**DebugLevelSyslog**
:   The slurmdbd daemon will log events to the syslog file at the specified level of detail. If not set, the slurmdbd daemon will log to syslog at level **fatal**, unless there is no **LogFile** and it is running in the background, in which case it will log to syslog at the level specified by **DebugLevel** (at **fatal** in the case that **DebugLevel** is set to **quiet**) or it is run in the foreground, when it will be set to quiet.

:   

    :   

        **quiet**
        :   Log nothing

        :   

        **fatal**
        :   Log only fatal errors

        :   

        **error**
        :   Log only errors

        :   

        **info**
        :   Log errors and general informational messages

        :   

        **verbose**
        :   Log errors and verbose informational messages

        :   

        **debug**
        :   Log errors and verbose informational messages and debugging messages

        :   

        **debug2**
        :   Log errors and verbose informational messages and more debugging messages

        :   

        **debug3**
        :   Log errors and verbose informational messages and even more debugging messages

        :   

        **debug4**
        :   Log errors and verbose informational messages and even more debugging messages

        :   

        **debug5**
        :   Log errors and verbose informational messages and even more debugging messages

:   **NOTE**: By default, Slurm\'s systemd service file starts the slurmdbd daemon in the foreground with the -D option. This means that systemd will capture stdout/stderr output and print that to syslog, independent of Slurm printing to syslog directly. To prevent systemd from doing this, add \"StandardOutput=null\" and \"StandardError=null\" to the respective service files or override files.

:   

**DefaultQOS**
:   When adding a new cluster this will be used as the qos for the cluster unless something is explicitly set by the admin with the create.

:   

**DisableArchiveCommands**
:   Disable the ability to run sacctmgr archive commands.

:   

**DisableCoordDBD**

:   Disable the coordinator status in all slurmdbd interactions.

    When this is set, a coordinator may not do the following in slurmdbd as they relate to the account(s) they coordinate:

    Add accounts\
    Add/Modify/Remove associations\
    Add/Remove coordinators\
    Add/Modify/Remove users

    Boolean, yes to turn on, no (default) to recognize coordinator status in all slurmdbd interactions.

:   

**HashPlugin**
:   Identifies the type of hash plugin to use for network communication. Acceptable values include:

:   

    :   

        **hash/k12**
        :   Hashes are generated by the KangorooTwelve cryptographic hash function. This is the default.

        :   

        **hash/sha3**
        :   Hashes are generated by the SHA-3 cryptographic hash function.

:   **NOTE**: Make sure that HashPlugin has the same value both in slurm.conf and in slurmdbd.conf.

**LogFile**
:   Fully qualified pathname of a file into which the Slurm Database Daemon\'s logs are written. The default value is none (performs logging via syslog).\
    See the section **LOGGING** in the slurm.conf man page if a pathname is specified.

:   

**LogTimeFormat**
:   Format of the timestamp in slurmdbd log files. Accepted format values include \"iso8601\", \"iso8601_ms\", \"rfc5424\", \"rfc5424_ms\", \"rfc3339\", \"clock\", \"short\" and \"thread_id\". The values ending in \"\_ms\" differ from the ones without in that fractional seconds with millisecond precision are printed. The default value is \"iso8601_ms\". The \"rfc5424\" formats are the same as the \"iso8601\" formats except that the timezone value is also shown. The \"clock\" format shows a timestamp in microseconds retrieved with the C standard clock() function. The \"short\" format is a short date and time format. The \"thread_id\" format shows the timestamp in the C standard ctime() function form without the year but including the microseconds, the daemon\'s process ID and the current thread name and ID.

:   

**MaxPurgeLimit**
:   When archiving and purging records, limit each individual operation to this many rows. The operations will then repeat until all targeted rows are processed. This limit ensures that locks will periodically be released, allowing other database operations to occur. A lower limit will release locks more frequently, which may improve system responsiveness while purging records from large tables. However, a lower limit will also increase the total amount of time required to complete the purge. In most cases it is not recommended to set a higher limit than default. Default value is 50000.

:   

**MaxQueryTimeRange**
:   Return an error if a query is against too large of a time span, to prevent ill-formed queries from causing performance problems within SlurmDBD. Default value is INFINITE which allows any queries to proceed. Accepted time formats are the same as the MaxTime option in slurm.conf. Operator and higher privileged users are exempt from this restriction. Note that queries which attempt to return over 3GB of data will still fail to complete with ESLURM_RESULT_TOO_LARGE.

:   

**MessageTimeout**
:   Time permitted for a round-trip communication to complete in seconds. Default value is 10 seconds.

:   

**Parameters**
:   Contains arbitrary comma separated parameters used to alter the behavior of the slurmdbd.

:   

    :   

        **PreserveCaseUser**
        :   When defining users do not force lower case which is the default behavior.

:   

**PidFile**
:   Fully qualified pathname of a file into which the Slurm Database Daemon may write its process ID. This may be used for automated signal processing. The default value is \"/var/run/slurmdbd.pid\".

:   

**PluginDir**
:   Identifies the places in which to look for Slurm plugins. This is a colon-separated list of directories, like the PATH environment variable. The default value is the prefix given at configure time + \"/lib/slurm\".

:   

**PrivateData**
:   This controls what type of information is hidden from regular users. By default, all information is visible to all users. User **SlurmUser**, **root**, and users with AdminLevel=Admin can always view all information. Multiple values may be specified with a comma separator. Acceptable values include:

:   

    :   

        **accounts**
        :   prevents users from viewing any account definitions unless they are coordinators of them.

        :   

        **events**
        :   prevents users from viewing event information unless they have operator status or above.

        :   

        **jobs**
        :   prevents users from viewing job records belonging to other users unless they are coordinators of the account running the job when using sacct.

        :   

        **reservations**
        :   restricts getting reservation information to users with operator status and above.

        :   

        **usage**
        :   prevents users from viewing usage of any other user. This applies to sreport.

        :   

        **users**
        :   prevents users from viewing information of any user other than themselves, this also makes it so users can only see associations they deal with. Coordinators can see associations of all users in the account they are coordinator of, but can only see themselves when listing users.

:   

**PurgeEventAfter**
:   Events are purged from the database after this amount of time has passed since they ended. This includes node down times and such. The time is a numeric value and is a number of months. If you want to purge more often you can include \"hours\", or \"days\" behind the numeric value to get those more frequent purges (i.e. a value of \"12hours\" would purge everything older than 12 hours). The purge takes place at the start of the each purge interval. For example, if the purge time is 2 months, the purge would happen at the beginning of each month. If not set (default), then event records are never purged.

:   

**PurgeJobAfter**
:   Individual job records are purged from the database after this amount of time has passed since they ended. Aggregated information will be preserved to \"PurgeUsageAfter\". The time is a numeric value and is a number of months. If you want to purge more often you can include \"hours\", or \"days\" behind the numeric value to get those more frequent purges (i.e. a value of \"12hours\" would purge everything older than 12 hours). The purge takes place at the start of the each purge interval. For example, if the purge time is 2 months, the purge would happen at the beginning of each month. If not set (default), then job records are never purged.

:   

**PurgeResvAfter**
:   Individual reservation records are purged from the database after this amount of time has passed since they ended. Aggregated information will be preserved to \"PurgeUsageAfter\". The time is a numeric value and is a number of months. If you want to purge more often you can include \"hours\", or \"days\" behind the numeric value to get those more frequent purges (i.e. a value of \"12hours\" would purge everything older than 12 hours). The purge takes place at the start of the each purge interval. For example, if the purge time is 2 months, the purge would happen at the beginning of each month. If not set (default), then reservation records are never purged.

:   

**PurgeStepAfter**
:   Individual job step records are purged from the database after this amount of time has passed since they ended. Aggregated information will be preserved to \"PurgeUsageAfter\". The time is a numeric value and is a number of months. If you want to purge more often you can include \"hours\", or \"days\" behind the numeric value to get those more frequent purges (i.e. a value of \"12hours\" would purge everything older than 12 hours). The purge takes place at the start of the each purge interval. For example, if the purge time is 2 months, the purge would happen at the beginning of each month. If not set (default), then job step records are never purged.

:   

**PurgeSuspendAfter**
:   Individual job suspend records are purged from the database after this amount of time has passed since they ended. Aggregated information will be preserved to \"PurgeUsageAfter\". The time is a numeric value and is a number of months. If you want to purge more often you can include \"hours\", or \"days\" behind the numeric value to get those more frequent purges (i.e. a value of \"12hours\" would purge everything older than 12 hours). The purge takes place at the start of the each purge interval. For example, if the purge time is 2 months, the purge would happen at the beginning of each month. If not set (default), then suspend records are never purged.

:   

**PurgeTXNAfter**
:   Individual transaction records are purged from the database after this amount of time has passed since they occurred. The time is a numeric value and is a number of months. If you want to purge more often you can include \"hours\", or \"days\" behind the numeric value to get those more frequent purges (i.e. a value of \"12hours\" would purge everything older than 12 hours). The purge takes place at the start of the each purge interval. For example, if the purge time is 2 months, the purge would happen at the beginning of each month. If not set (default), then transaction records are never purged.

:   

**PurgeUsageAfter**
:   Usage records (Cluster, Association, QOS and WCKey) are purged from the database after this amount of time has passed since they were created or last modified. These tables are the source for reports generated by the [sreport](sreport.md)(1) command. The time is a numeric value and is a number of months. If you want to purge more often you can include \"hours\", or \"days\" behind the numeric value to get those more frequent purges (i.e. a value of \"12hours\" would purge everything older than 12 hours). The purge takes place at the start of the each purge interval. For example, if the purge time is 2 months, the purge would happen at the beginning of each month. If not set (default), then usage records are never purged.

:   

**SlurmUser**
:   The name of the user that the **slurmdbd** daemon executes as. This user should match the SlurmUser used for all instances of slurmctld that report to slurmdbd. It must exist on the machine executing the Slurm Database Daemon and have the same UID as the hosts on which **slurmctld** executes. For security purposes, a user other than \"root\" is recommended. The default value is \"root\".
    **NOTE**: If the SlurmUser for slurmctld is root you can still use a non-root SlurmUser for slurmdbd (in any other case, both SlurmUsers should match) by explicitly setting the user\'s AdminLevel to Admin. After adding a user in this way, you must restart slurmctld.

:   

**StorageBackupHost**
:   Define the name of the backup host the database is running where we are going to store the data. This can be viewed as a backup solution when the StorageHost is not responding. It is up to the backup solution to enforce the coherency of the accounting information between the two hosts. With clustered database solutions (active/passive HA), you would not need to use this feature. Default is none.

:   

**StorageHost**
:   Define the name of the host the database is running where we are going to store the data. This can be the host on which slurmdbd executes, but for larger systems, we recommend keeping the database on a separate machine.

:   

**StorageLoc**
:   Specify the name of the database as the location where accounting records are written. Defaults to \"slurm_acct_db\".

:   

**StorageParameters**
:   Comma separated list of key-value pair parameters.

:   

    :   

        **SSL_CERT**
        :   The path name of the client public key certificate file.

        :   

        **SSL_CA**
        :   The path name of the Certificate Authority (CA) certificate file.

        :   

        **SSL_CAPATH**
        :   The path name of the directory that contains trusted SSL CA certificate files.

        :   

        **SSL_KEY**
        :   The path name of the client private key file.

        :   

        **SSL_CIPHER**
        :   The list of permissible ciphers for SSL encryption.

        :   

        **token_duration**
        :   Duration in seconds to cache generated database passwords before requesting a new one from the StoragePassScript. Typically the token should refresh prior to actual expiration; upon token generation failure the cached token will continue to be used to avoid transient generation failures from causing connection failures. Default value is 300 seconds (5 minutes).

:   

**StoragePass**
:   Define the password used to gain access to the database to store the job accounting data. The \'#\' character is not permitted in a password.

:   

**StoragePassScript**
:   Absolute path to an executable script that generates ephemeral authentication tokens for database connections which are used instead of **StoragePass**. The script must output the password/token to stdout and exit with status 0 on success. This allows dynamic password generation, instead of storing static credentials in configuration files. The script must be owned and executable by SlurmUser.

:   Environment variables provided to the script:

    :   

        **SLURM_STORAGE_HOSTNAME**
        :   Database hostname

        **SLURM_STORAGE_PORT**
        :   Database port number

        **SLURM_STORAGE_USER**
        :   Database username

:   Expected output format:\
    **TOKEN=***\<authentication_token\>*

:   The script must exit with status 0 on success, non-zero on failure. Any output to stderr will be logged as an error. If there is a backup host specified, the script will still be provided the main hostname and the same token is used for both hosts.

:   

**StoragePort**
:   The port number that the Slurm Database Daemon (slurmdbd) communicates with the database. Default is 3306.

:   

**StorageType**
:   Define the accounting storage mechanism type. Acceptable values at present include \"accounting_storage/mysql\". The value \"accounting_storage/mysql\" indicates that accounting records should be written to a MySQL or MariaDB database specified by the **StorageLoc** parameter. This value must be specified.

:   

**StorageUser**
:   Define the name of the user we are going to connect to the database with to store the job accounting data. If no value is specified, the user that started the slurmdbd will be used.

:   

**TCPTimeout**
:   Time permitted for TCP connection to be established. Default value is 2 seconds.

:   

**TLSParameters**
:   Comma-separated options identifying TLS options. Supported values include:

:   

    :   

        **ca_cert_file=**
        :   Path of certificate authority (CA) certificate. Must exist on all hosts and be accessible by all Slurm components. File permissions must be 644, and owned by SlurmUser/root.
            Default path is \"ca_cert.pem\" in the Slurm configuration directory

        :   

        **dbd_cert_file=**
        :   Path of certificate used by slurmdbd. Must chain to **ca_cert_file**. Should only exist on host running slurmdbd. File permissions must be 600, and owned by SlurmUser.
            Default path is \"dbd_cert.pem\" in the Slurm configuration directory

        :   

        **dbd_cert_key_file=**
        :   Path of private key that accompanies **dbd_cert_file**. Should only exist on host running slurmdbd. File permissions must be 600, and owned by SlurmUser.
            Default path is \"dbd_cert_key.pem\" in the Slurm configuration directory

        :   

        **load_system_certificates**
        :   Load certificates found in default system locations (e.g. /etc/ssl) into trust store.
            Default is to not load system certificates, and to rely solely on **ca_cert_file** to establish trust.

        :   

        **security_policy_version=**
        :   Security policy version used by s2n. See s2n documentation for more details. Default security policy is \"20230317\", which is FIPS compliant and includes TLS 1.3.

:   

**TLSType**
:   Specify the TLS implementation that will be used. Acceptable values at present:

:   

    :   

        **tls/s2n**
        :   Use the s2n TLS plugin.

:   

**TrackSlurmctldDown**
:   Boolean yes or no. If set the slurmdbd will mark all idle resources on the cluster as down when a slurmctld disconnects or is no longer reachable. The default is no.

:   

**TrackWCKey**
:   Boolean yes or no. Used to set display and track of the Workload Characterization Key. Must be set to track wckey usage. This must be set to generate rolled up usage tables from WCKeys. **NOTE**: If TrackWCKey is set here and not in your various slurm.conf files all jobs will be attributed to their default WCKey.

:   

[ ]{#lbAD}

## EXAMPLE

    #
    # Sample /etc/slurmdbd.conf
    #
    ArchiveEvents=yes
    ArchiveJobs=yes
    ArchiveResvs=yes
    ArchiveSteps=no
    ArchiveSuspend=no
    ArchiveTXN=no
    ArchiveUsage=no
    #ArchiveScript=/usr/sbin/slurm.dbd.archive
    AuthInfo=/var/run/munge/munge.socket.2
    AuthType=auth/munge
    DbdHost=db_host
    DebugLevel=info
    PurgeEventAfter=1month
    PurgeJobAfter=12month
    PurgeResvAfter=1month
    PurgeStepAfter=1month
    PurgeSuspendAfter=1month
    PurgeTXNAfter=12month
    PurgeUsageAfter=24month
    LogFile=/var/log/slurmdbd.log
    PidFile=/var/run/slurmdbd.pid
    SlurmUser=slurm_mgr
    StoragePass=password_to_database
    StorageType=accounting_storage/mysql
    StorageUser=database_mgr

[ ]{#lbAE}

## COPYING

Copyright (C) 2008-2010 Lawrence Livermore National Security. Produced at Lawrence Livermore National Laboratory (cf, DISCLAIMER).\
Copyright (C) 2010-2022 SchedMD LLC.

This file is part of Slurm, a resource management program. For details, see \<[https://slurm.schedmd.com/](index.md)\>.

Slurm is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Slurm is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[ ]{#lbAF}

## FILES

/etc/slurmdbd.conf

[ ]{#lbAG}

## SEE ALSO

**[slurm.conf](slurm.conf.md)**(5), **[slurmctld](slurmctld.md)**(8), **[slurmdbd](slurmdbd.md)**(8) **syslog** (2)

------------------------------------------------------------------------

[ ]{#index}

## Index

NAME

:   

DESCRIPTION

:   

EXAMPLE

:   

COPYING

:   

FILES

:   

SEE ALSO

:   

------------------------------------------------------------------------

This document was created by *man2html* using the manual pages.\
Time: 20:41:14 GMT, March 12, 2026
