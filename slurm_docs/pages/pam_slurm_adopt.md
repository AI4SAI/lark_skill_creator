# pam_slurm_adopt

The purpose of this module is to prevent users from sshing into nodes that they do not have a running job on, and to track the ssh connection and any other spawned processes for accounting and to ensure complete job cleanup when the job is completed. This module does this by determining the job which originated the ssh connection. The user\'s connection is \"adopted\" into the \"external\" step of the job. When access is denied, the user will receive a relevant error message.

## Contents

- Installation
- Slurm Configuration
- SSH Configuration
- PAM Configuration
- Administrative Access Configuration
- pam_slurm_adopt Module Options
- Firewalls, IP Addresses, etc.
- SELinux
- Limitations

## Installation {#INSTALLATION}

### Source:

In your Slurm source directory, navigate to ./contribs/pam_slurm_adopt/ and run the following as **root**:

    make && make install

This will place pam_slurm_adopt.a, pam_slurm_adopt.la, and pam_slurm_adopt.so in /lib/security/ (on Debian systems) or /lib64/security/ (on RedHat/SUSE systems). This install location is not affected by configure\'s \--prefix flag; use \--with-pam_dir=PATH to modify the install location if desired.

### RPM:

The included slurm.spec will build a slurm-pam_slurm RPM which will install pam_slurm_adopt. Refer to the [Quick Start Administrator Guide](quickstart_admin.md) for instructions on managing an RPM-based install.

### DEB:

The included debian packaging scripts will build the slurm-smd-libpam-slurm-adopt package which will install pam_slurm_adopt. [Quick Start Administrator Guide](quickstart_admin.md) for instructions on managing an DEB-based install.

## Slurm Configuration {#SLURM_CONFIG}

**PrologFlags=contain** must be set in the slurm.conf. This sets up the \"extern\" step into which ssh-launched processes will be adopted. You must also enable the task/cgroup plugin in slurm.conf. See the [Slurm cgroups guide.](cgroups.md) **CAUTION** This option must be in place *before* using this module. The module bases its checks on local steps that have already been launched. Jobs launched without this option do not have an extern step, so pam_slurm_adopt will not have access to those jobs.

**LaunchParameters=ulimit_pam_adopt** will set RLIMIT_RSS in processes adopted by the external step, similar to tasks running in regular steps.

The **UsePAM** option in slurm.conf is not related to pam_slurm_adopt.

## SSH Configuration {#ssh_config}

Verify that **UsePAM** is set to **On** in /etc/ssh/sshd_config (it should be on by default).

Ensure that only supported **AuthenticationMethods** are enabled in sshd_config (on the compute nodes). At this time, only **publickey** and **password** are supported. In particular **keyboard-interactive** is explicitly unsupported and must be removed from **AuthenticationMethods**. If this step is not observed process adoption will be broken and SSH sessions will persist even after the job ends. See Limitations for more information.

## PAM Configuration {#PAM_CONFIG}

For initial testing (see **warning** below), add the following line to the appropriate file in /etc/pam.d, such as system-auth or sshd (you may use either the \"required\" or \"sufficient\" PAM control flag):

    account    required      pam_slurm_adopt.so

The order of plugins is very important. pam_slurm_adopt.so should be the last PAM module in the account stack. Included files such as common-account should normally be included before pam_slurm_adopt. You might have the following account stack in sshd:

    account    required      pam_nologin.so
    account    include       password-auth
    ...
    -account    required      pam_slurm_adopt.so

Note the \"-\" before the account entry for pam_slurm_adopt. It allows PAM to fail gracefully if the pam_slurm_adopt.so file is not found. If Slurm is on a shared filesystem, such as NFS, then this is suggested to avoid being locked out of a node while the shared filesystem is mounting or down.

pam_slurm_adopt must be used with the task/cgroup task plugin and the proctrack/cgroup proctrack plugin. The pam_systemd module will conflict with pam_slurm_adopt, so you need to disable it in all files that are included in sshd or system-auth (e.g. password-auth, common-session, etc.).

**WARNING**: The default configuration for pam_slurm_adopt is meant to ensure an admin is not locked out of a node during testing. Production environments should consider setting both action_adopt_failure and action_generic_failure to **deny** after successful testing; otherwise, plugin failures may allow users to log in unconfined. Future examples on this page will include these flags.

If you need the user management features from pam_systemd, such as handling user runtime directory /run/user/\$UID, you can have the prolog script run \'loginctl enable-linger \$SLURM_JOB_USER\' and the epilog script disable it again (after making sure there are no other jobs from this user on the node) by running \'loginctl disable-linger \$SLURM_JOB_USER\'. You will also need to export the XDG\_\* environment variables if your software requires them. You can see an example of prolog and epilog scripts here:

Prolog:

    loginctl enable-linger $SLURM_JOB_USER
    exit 0

TaskProlog:

    echo "export XDG_RUNTIME_DIR=/run/user/$SLURM_JOB_UID"
    echo "export XDG_SESSION_ID=$(</proc/self/sessionid)"
    echo "export XDG_SESSION_TYPE=tty"
    echo "export XDG_SESSION_CLASS=user"

Epilog:

    #Only disable linger if this is the last job running for this user.
    O_P=0
    for pid in $(scontrol listpids | awk -v jid=$SLURM_JOB_ID 'NR!=1 { if ($2 != jid && $1 != "-1"){print $1} }'); do
            ps --noheader -o euser p $pid | grep -q $SLURM_JOB_USER && O_P=1
    done
    if [ $O_P -eq 0 ]; then
            loginctl disable-linger $SLURM_JOB_USER
    fi
    exit 0

You must also make sure a different PAM module isn\'t short-circuiting the account stack before it gets to pam_slurm_adopt.so. From the example above, the following two lines have been commented out in the included password-auth file:

    #account    sufficient    pam_localuser.so
    #-session   optional      pam_systemd.so

Note: This may involve editing a file that is auto-generated. Do not run the config script that generates the file or your changes will be erased.

## Administrative Access Configuration {#admin_access}

pam_slurm_adopt will always allow the root user access, and will do so even before checking for slurm configuration. If you wish to also allow other admins to the system with their own user accounts, this can be accomplished by stacking other modules along with pam_slurm_adopt.

Stacking pam_access with pam_slurm_adopt is one way to permit administrative access, with two possible implementations with subtle differences in behavior. Both will require editing the pam_access configuration file (/etc/security/access.conf). In the following example, the access.conf file will allow members of the group \"wheel\" to log in.

    +:(wheel):ALL
    -:ALL:ALL

Then you will need to stack the modules in the /etc/pam.d/sshd file. The order here matters, and each ordering has different implications. In the example below, pam_slurm adopt is listed first as \"sufficient\", followed by pam_access. In this configuration when the admin has a job running, their ssh session will be adopted into the job. If they do not, access will be permitted by pam_access, but note that pam_slurm_adopt will still emit the \"access denied\" message.

    account    sufficient    pam_slurm_adopt.so action_adopt_failure=deny action_generic_failure=deny
    account    required      pam_access.so

Flipping this order, with pam_access(sufficient) before pam_slurm_adopt(required), members of the administrative group will bypass pam_slurm_adopt entirely.

    account    sufficient    pam_access.so
    account    required      pam_slurm_adopt.so action_adopt_failure=deny action_generic_failure=deny

The pam_listfile module is another module that can be stacked with pam_slurm_adopt and achieve similar results. In the following example, it will allow all users in the specified file to log in, skipping the pam_slurm_adopt module. This can also be flipped similar to pam_access, with the same implications.

    account    sufficient    pam_listfile.so item=user sense=allow onerr=fail file=/path/to/allowed_users_file
    account    required      pam_slurm_adopt.so action_adopt_failure=deny action_generic_failure=deny

The pam_listfile module can also be configured to look for membership of a group. In this example, instead of checking the user, the plugin checks that the user belongs to one of the groups specified in the \'groupfile\'. If pam_systemd is needed for those users, you can link it to the pam_listfile.so module in the session phase, as shown below. If the pam_listfile module succeeds, the evaluation continues (success=ignore). Otherwise, the next module (pam_systemd) is ignored (default=1 skips the next module). The pam_systemd module will only be used for admin users in this example.

    account    sufficient                    pam_listfile.so item=group sense=allow onerr=fail file=/path/to/allowed_users_file
    -account   required                      pam_slurm_adopt.so action_adopt_failure=deny action_generic_failure=deny

    session    [default=1 success=ignore]    pam_listfile.so item=group sense=allow onerr=fail file=/etc/groupfile
    -session   optional                      pam_systemd.so

More information about the capabilities and configuration options for pam_access and pam_listfile can be found in their respective man pages.

## pam_slurm_adopt Module Options {#OPTIONS}

This module is configurable. Add these options to the end of the pam_slurm_adopt line in the appropriate file in /etc/pam.d/ (e.g., sshd or system-auth):

    account sufficient pam_slurm_adopt.so optionname=optionvalue

This module has the following options:

**action_no_jobs**
:   The action to perform if the user has no jobs on the node. Configurable values are:

    :   

        **ignore**
        :   Do nothing. Fall through to the next pam module.

        **deny** (default)
        :   Deny the connection.

**action_unknown**
:   The action to perform when the user has multiple jobs on the node **and** the RPC does not locate the source job. If the RPC mechanism works properly in your environment, this option will likely be relevant **only** when connecting from a login node. Configurable values are:

    :   

        **newest** (default)
        :   On systems with *cgroup/v1* pick the newest job on the node. The \"newest\" job is chosen based on the mtime of the job\'s step_extern cgroup; asking Slurm would require an RPC to the controller. Thus, the memory cgroup must be in use so that the code can check mtimes of cgroup directories. The user can ssh in but may be adopted into a job that exits earlier than the job they intended to check on. The ssh connection will at least be subject to appropriate limits and the user can be informed of better ways to accomplish their objectives if this becomes a problem. **NOTE**: If the module fails to retrieve the cgroup mtime, then the picked job may not be the newest one. On systems with *cgroup/v2* the newest is just the job with the greatest id, and thus this does not ensure that it is really the newest job.

        **allow**
        :   Let the connection through without adoption.

        **deny**
        :   Deny the connection.

**action_adopt_failure**
:   The action to perform if the process is unable to be adopted into any job for whatever reason. If the process cannot be adopted into the job identified by the callerid RPC, it will fall through to the action_unknown code and try to adopt there. A failure at that point or if there is only one job will result in this action being taken. Configurable values are:

    :   

        **allow** (default)
        :   Let the connection through without adoption.\
            **WARNING**: This value allows connections that were not able to be adopted into a job, which could allow users complete access to a node, not just to their allocated resources. This value is recommended for testing purposes only, we recommend using \"deny\" in production systems.

        **deny**
        :   Deny the connection.

**action_generic_failure**
:   The action to perform if there are certain failures such as the inability to talk to the local *slurmd* or if the kernel doesn\'t offer the correct facilities. Configurable values are:

    :   

        **ignore** (default)
        :   Do nothing. Fall through to the next PAM module, even if this module is set as \"required\" or \"requisite\".\
            **WARNING**: This value does not deny connections pam_slurm_adopt was unable to handle normally, which could allow users complete access to a node, not just to their allocated resources. This value is recommended for testing purposes only, we recommend using \"deny\" in production systems.

        **allow**
        :   Let the connection through without adoption.\
            **WARNING**: This value explicitly allows connections pam_slurm_adopt was unable to handle normally, which could allow users complete access to a node, not just to their allocated resources. This value is recommended for testing purposes only, we recommend using \"deny\" in production systems.

        **deny**
        :   Deny the connection.

**disable_x11**
:   Turn off Slurm built-in X11 forwarding support. Configurable values are:

    :   

        **0** (default)
        :   If the job the connection is adopted into has Slurm\'s X11 forwarding enabled, the DISPLAY variable will be overwritten with the X11 tunnel endpoint details.

        **1**
        :   Do not check for Slurm\'s X11 forwarding support, and do not alter the DISPLAY variable.

**join_container**
:   Control the interaction with the namespace plugins. Configurable values are:

    :   

        **true** (default)
        :   Attempt to join a namespace created by the namespace plugins.

        **false**
        :   Do not attempt to join a namespace.

**log_level**
:   See [SlurmdDebug](slurm.conf.md#OPT_SlurmdDebug) in slurm.conf for available options. The default log_level is **info**.

**nodename**
:   If the NodeName defined in **slurm.conf** is different than this node\'s hostname (as reported by **hostname -s**), then this must be set to the NodeName in **slurm.conf** that this host operates as.

**service**
:   The pam service name for which this module should run. By default it only runs for sshd for which it was designed for. A different service name can be specified like \"login\" or \"\*\" to allow the module to in any service context. For local pam logins this module could cause unexpected behavior or even security issues. Therefore if the service name does not match then this module will not perform the adoption logic and returns PAM_IGNORE immediately.

### Firewalls, IP Addresses, etc. {#firewall}

*slurmd* should be accessible on any IP address from which a user might launch ssh. The RPC to determine the source job must be able to reach the *slurmd* port on that particular IP address. If there is no *slurmd* on the source node, such as on a [login node](quickstart_admin.md#login), it is better to have the RPC be rejected rather than silently dropped. This will allow better responsiveness to the RPC initiator.

### SELinux

SELinux may conflict with pam_slurm_adopt, but it is generally possible for them to work side by side. This is an example type enforcement file that was used on a fairly stock Debian system. It is provided to give some direction and to show what is required to get this working but may require additional modification.

    module pam_slurm_adopt 1.0;

    require {
        type sshd_t;
        type var_spool_t;
        type unconfined_t;
        type initrc_var_run_t;
        class sock_file write;
        class dir { read search };
        class unix_stream_socket connectto;
    }

    #============= sshd_t ==============
    allow sshd_t initrc_var_run_t:dir search;
    allow sshd_t initrc_var_run_t:sock_file write;
    allow sshd_t unconfined_t:unix_stream_socket connectto;
    allow sshd_t var_spool_t:dir read;
    allow sshd_t var_spool_t:sock_file write;

It is possible for some plugins to require more permissions than this. Notably, namespace/tmpfs will require something more like this:

    module pam_slurm_adopt 1.0;

    require {
        type nsfs_t;
        type var_spool_t;
        type initrc_var_run_t;
        type unconfined_t;
        type sshd_t;
        class sock_file write;
        class dir { read search };
        class unix_stream_socket connectto;
        class fd use;
        class file read;
        class capability sys_admin;
    }

    #============= sshd_t ==============
    allow sshd_t initrc_var_run_t:dir search;
    allow sshd_t initrc_var_run_t:sock_file write;
    allow sshd_t nsfs_t:file read;
    allow sshd_t unconfined_t:fd use;
    allow sshd_t unconfined_t:unix_stream_socket connectto;
    allow sshd_t var_spool_t:dir read;
    allow sshd_t var_spool_t:sock_file write;
    allow sshd_t self:capability sys_admin;

## Limitations {#LIMITATIONS}

Internally, some AuthenticationMethods cause sshd to fork an extra process during the login flow, which sshd partially offloads the authentication dialogue to. This can confuse PAM modules, and may break process adoption with pam_slurm_adopt.

When using SELinux support in Slurm, the session started via pam_slurm_adopt won\'t necessarily be in the same context as the job it is associated with.

When using namespace/linux and the user namespace is configured, the pam_limits module may not be able to set memlock, sigpending, msgqueue, nice, or rtprio.
