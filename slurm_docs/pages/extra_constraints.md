# Extra Constraints

## Contents

Overview

Configuration

Node Extra Data

Job Submission

- Syntax
- Warnings
- Valid and Invalid Requests

Examples

## Overview {#Overview}

Extra data may be added to a node, and jobs may request extra constraints to filter nodes based on their extra data. This is disabled by default, but may be enabled in slurm.conf. **Warning**: Slurm\'s backfill scheduler cannot accurately plan nodes for jobs whose request extra constraints are not immediately satisfied. This means that the more often extra data for nodes is changed, the less accurate the backfill scheduler will be.

## Configuration {#Configuration}

- In slurm.conf, configure `SchedulerParameters=extra_constraints`

## Node Extra Data {#Node_Extra_Data}

A node\'s extra data is a json formatted string. It may be initialized on slurmd startup with the \--extra flag for slurmd. For example:

    slurmd --extra '{ "a": 1.23, "b": true, "c": 0, "foo": "bar", "zed": 23 }'

Or, it may be updated with scontrol. For example:

    scontrol update nodename=node123 extra='{ "a": 1.23, "b": true, "c": 0, "foo": "bar", "zed": 23 }'

This defines the features that may be requested by the \--extra option in salloc, sbatch, and srun. Values may be any string, number, or boolean value.

## Job Submission {#Job_Submission}

### Syntax {#Syntax}

The salloc, sbatch, or srun \--extra field is an arbitrary string enclosed in single or double quotes if using spaces or some special characters.

If **SchedulerParameters=extra_constraints** is enabled, this string is used for node filtering based on the *Extra* field in each node.

The most basic request is structured like this:

    <key><comparison_operator><value>

Key and value are arbitrary, non-empty strings that cannot contain any characters that are part of operators and cannot contain parentheses. Thus, the following characters are not allowed in a key or value:

    ,&|<>=!()

The following comparison operators are allowed:

- `= (equal to)`
- `!= (not equal to)`
- `> (greater than)`
- `>= (greater than or equal to)`
- `< (less than)`
- `<= (less than or equal to)`

Two numbers are equal if their difference is less than 0.00001. Numerical suffixes (such as kb or mb) are not supported. If letters are interspersed with numbers, then the key or value is considered a string.

Requests can be joined together with boolean operators.

    <request><boolean_operator><request>

The following boolean operators are allowed:

    &   (AND)
    ,   (AND)
    |   (OR)

Any number of parentheses may be used to group requests together. All boolean operators at any given level of parentheses must be identical. Boolean operators at different levels of parentheses may be different. For example, this is not allowed:

    a=1&b=2|c=foobar

But this is allowed:

    (a=1&b=2)|c=foobar

### Warnings {#Warnings}

Whitespace characters are not treated specially. Any whitespace characters will be considered part of a key or value. This means that the following is invalid:

    --extra " (a=b)"

The space at he beginning is parsed as a key of a request. Then the opening parenthesis character is recognized as an invalid character for either a key or a comparison operator. This request would result in the job being rejected. However, this is valid:

    --extra "( a=b)"

This has a single request. The key is \" a\", the comparison operator is \"=\", and the value is \"b\".

This same warning applies to single and double quotes. These are not considered special characters, and thus are part of a string. Thus, bar and \"bar\" are not equal.

### Valid and Invalid Requests {#Valid}

Here are some examples of **valid** requests:

    a=1.23
    a=   b
    a!=1.24
    a!=1.23|foo!=blah
    b=200
    b=true
    foo<baz
    (c<=0.0001&a=1.25)|zed=23.0
    ((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=false|c>=0.00000001)
    ((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=true|c>=0.1)

Here are some examples of **invalid** requests:

Invalid comparison operator:

    a,<=6

Trailing operator:

    a<=6<=

Multiple boolean operators in a row:

    a=5&&&b=5
    a=5|||b=5

Multiple comparison operators in a row:

    a====5
    b<=<=5

Parentheses without anything inside:

    a=5&()

Different boolean operators at a single level of parentheses:

    a=5&b=5|c=5
    (a=1)&(b=2)|(c=3)

No boolean operator between individual requests:

    a=1(b=2)
    (a=1)(b=2)
    (((a=1)b=2))

## Examples {#Examples}

Given a node with the following extra data:

    Extra={ "a": 1.23, "b": true, "c": 0, "foo": "bar", "zed": 23 }

The following \--extra requests are fulfilled by this node:

    a=1.23
    a!=1.24
    a!=1.23|foo!=blah
    b=200
    b=true
    foo<baz
    (c<=0.0001&a=1.25)|zed=23.0
    ((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=false|c>=0.00000001)
    ((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=true|c>=0.1)

The following \--extra requests are not fulfilled by this node:

    a!=1.23
    b=0
    b=false
    foo>baz
    ((c<=0.0001&a=1.25)|zed=23.0)&(a<1|b=false|c>=0.00001)

Reminder: in order for two numbers to be considered equal, their difference must be less than 0.0001. This is why 0.0001 is not considered equal to 0 and thus the request `c>=0.0001` is not fulfilled, but 0.00000001 is considered equal to 0 and thus the request `c>=0.00000001` is fulfilled.

A practical example might be to have a script that looks at the load average of each node and updates the extra attribute for each node with the current value. This would allow users to restrict their jobs to nodes whose load average is below a certain threshold.

In this simple example, the three nodes in a cluster are being monitored and the extra attribute is being populated with their load average.

    $ scontrol show nodes node[01-03] | grep -E 'NodeName|Extra'
    NodeName=node01 Arch=x86_64 CoresPerSocket=6
       Extra={ "load": 0.99 }
    NodeName=node02 Arch=x86_64 CoresPerSocket=6
       Extra={ "load": 0.75 }
    NodeName=node03 Arch=x86_64 CoresPerSocket=6
       Extra={ "load": 0.45 }

A job can request to run on a machine with less than half of the CPU time being utilized.

    $ sbatch -n12 --extra "load<0.5" --wrap='srun sleep 10'
    Submitted batch job 11206

    $ squeue
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                 11206     debug     wrap      ben  R       0:03      1 node03

A job can also request to run on a node between a range of acceptable load values.

    $ sbatch -n12 --extra "(load<0.9&load>0.5)" --wrap='srun sleep 10'
    Submitted batch job 11207

    $ squeue
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                 11207     debug     wrap      ben  R       0:01      1 node02
