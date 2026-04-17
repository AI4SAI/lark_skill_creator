# [TLS Certificate Manager]{#top}

## Overview {#Overview}

The `certmgr` plugin interface can be used alongside the `tls` plugin interface to dynamically create and renew signed certificates for slurmd/sackd nodes.

Signed certificates and accompanying private keys generated with certmgr are saved in slurmd\'s spool directory when they are retrieved from slurmctld, and loaded when slurmd starts up.

## certmgr/script {#script}

The `certmgr/script` plugin allows scripts to be used to perform the necessary operations needed to validate node identity and generate signed certificates.

### OpenSSL Example {#script_examples}

This is an example using the openssl cli to generate certificate signing requests and to sign such requests to create signed certificates. This example is not meant to be used in production, and is only mean to show the intended responsibilities of each script.

In this example, there are a list of things that need to be preloaded on each machine before Slurm can do its certificate management. Note that any instructions for slurmd also apply to sackd nodes.

slurmctld will need access to the CA certificate, and the CA certificate/key pair must be owned by `SlurmUser` (this is NOT recommended in a production setting). See the [TLS](tls.md#s2n_openssl_example) page for more info on how to generate this certificate/key pair.

The following scripts need to be created and configured. See [CertmgrParameters](slurm.conf.md#OPT_CertmgrParameters) for more details on each script.

- `get_node_token_script`
- `generate_csr_script`
- `validate_node_script`
- `sign_csr_script`

slurmctld needs to be able to validate slurmd\'s certificate signing request. This is done via unique tokens that are retrieved on slurmd nodes using `get_node_token_script`, and validated on the slurmctld host using `validate_node_script`.

A unique token will to be generated for each slurmd. Each token will be stored on its respective slurmd host, as well as in a comprehensive list that contains all node tokens on the slurmctld host. This token will be sent from slurmd to slurmctld along with the certificate signing request that slurmd will generate at runtime, and be validated by slurmctld before slurmctld creates a signed certificate. Note that slurmd will not begin to process any RPCs until a signed certificate is loaded.

This is a simple example of how these tokens can be generated and stored:

    # generate base64 32 character random token
    base64 /dev/urandom | head -c 32 > ${NODENAME}_token.txt

    # add token to token list
    echo "`cat ${NODENAME}_token.txt`" >> node_token_list.txt

Node **n1** needs to boot up with `n1_token.txt` and/or have it securely transferred to it. **slurmctld** needs to have secure access to `node_token_list.txt` in order to validate node tokens with the `validate_node_script`.

The `get_node_token_script`, `generate_csr_script`, and `get_node_cert_key_script` paths need to point to scripts that exist and are executable on slurmd nodes.

#### get_node_token_script example: {#get_node_token_script_example}

Print token to stdout. Return zero exit code for success, and non-zero exit code for error.

    #!/bin/bash

    # Slurm node name is passed in as arg $1
    TOKEN_PATH=/etc/slurm/certmgr/$1_token.txt

    # Check if token file exists
    if [ ! -f $TOKEN_PATH ]
    then
        echo "$BASH_SOURCE: Failed to resolve token path '$TOKEN_PATH'"
        exit 1
    fi

    # Print token to stdout
    cat $TOKEN_PATH

    # Exit with exit code 0 to indicate success
    exit 0

#### generate_csr_script example: {#generate_csr_script_example}

Print certificate signing request to stdout. Return zero exit code for success, and non-zero exit code for error.

    #!/bin/bash

    # Slurm node name is passed in as arg $1
    NODE_PRIVATE_KEY=/etc/slurm/certmgr/$1_private_key.pem

    # Check if node private key file exists
    if [ ! -f $NODE_PRIVATE_KEY ]
    then
        echo "$BASH_SOURCE: Failed to resolve node private key path '$NODE_PRIVATE_KEY'"
        exit 1
    fi

    # Generate CSR using node private key and print CSR to stdout
    openssl req -new -key $NODE_PRIVATE_KEY \
        -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=$1"

    # Check exit code from openssl
    if [ $? -ne 0 ]
    then
        echo "$BASH_SOURCE: Failed to generate CSR"
        exit 1
    fi

    # Exit with exit code 0 to indicate success
    exit 0

#### get_node_cert_key_script example: {#get_node_cert_key_script}

Print private key used to generate CSR to stdout. Return zero exit code for success, and non-zero exit code for error.

    #!/bin/bash

    # Slurm node name is passed in as arg $1
    NODE_PRIVATE_KEY=/etc/slurm/certmgr/$1_cert_key.pem

    # Check if node private key file exists
    if [ ! -f $NODE_PRIVATE_KEY ]
    then
        echo "$BASH_SOURCE: Failed to resolve node private key path '$NODE_PRIVATE_KEY'"
        exit 1
    fi

    cat $NODE_PRIVATE_KEY

    # Exit with exit code 0 to indicate success
    exit 0

The `validate_node_script` and `sign_csr_script` paths need to point to scripts that exist and are executable on **slurmctld**.

#### validate_node_script example: {#validate_node_script_example}

Return zero exit code for valid node tokens, and non-zero exit code for invalid node tokens or other errors.

    #!/bin/bash

    # Node's unique token is passed in as arg $1
    NODE_TOKEN=$1
    NODE_TOKEN_LIST_FILE=/etc/slurm/certmgr/node_token_list.txt

    # Check if node token list file exists
    if [ ! -f $NODE_TOKEN_LIST ]
    then
        echo "$BASH_SOURCE: Failed to resolve node token list path '$NODE_TOKEN_LIST'"
        exit 1
    fi

    # Check if unique node token is in token list file
    grep $1 $NODE_TOKEN_LIST_FILE

    # Check exit code from grep to see if token was found
    if [ $? -ne 0 ]
    then
        echo "$BASH_SOURCE: Failed to validate token '$NODE_TOKEN'"
        exit 1
    fi

    # Exit with exit code 0 to indicate success (node token is valid)
    exit 0

#### sign_csr_script example: {#sign_csr_script_example}

Print signed certificate to stdout. Return zero exit code for success, and non-zero exit code for error.

    #!/bin/bash

    # Certificate signing request is passed in as arg $1
    CSR=$1
    CA_CERT=/etc/slurm/certmgr/root_cert.pem
    CA_KEY=/etc/slurm/certmgr/root_key.pem

    # Check if CA certificate file exists
    if [ ! -f $CA_CERT ]
    then
        echo "$BASH_SOURCE: Failed to resolve CA certificate path '$CA_CERT'"
        exit 1
    fi

    # Check CA private key permissions
    if [ `stat -c "%a" $CA_KEY` -ne $KEY_PERMISSIONS ]
    then
        echo "$BASH_SOURCE: Bad permissions for CA private key at '$CA_KEY'. Permissions should be $KEY_PERMISSIONS"
        exit 1
    fi

    # Sign CSR using CA certificate and CA private key and print signed cert to stdout
    openssl x509 -req -CA $CA_CERT -CAkey $CA_KEY 2>/dev/null <<< $CSR

    # Check exit code from openssl
    if [ $? -ne 0 ]
    then
        echo "$BASH_SOURCE: Failed to generate signed certificate"
        exit 1
    fi

    # Exit with exit code 0 to indicate success
    exit 0

If everything is configured correctly, the following lines should appear in the slurmd and slurmctld logs with the [DebugFlags=TLS](slurm.conf.md#OPT_TLS) setting.

slurmd:

    slurmd: certmgr/script: certmgr_p_get_node_token: TLS: Successfully retrieved unique node token
    slurmd: certmgr/script: certmgr_p_generate_csr: TLS: Successfully generated csr:
    -----BEGIN CERTIFICATE REQUEST-----
    . . .
    -----END CERTIFICATE REQUEST-----

slurmctld:

    slurmctld: certmgr/script: certmgr_p_sign_csr: TLS: Successfully validated node token
    slurmctld: certmgr/script: certmgr_p_sign_csr: TLS: Successfully generated signed certificate:
    -----BEGIN CERTIFICATE-----
    . . .
    -----END CERTIFICATE-----

slurmd:

    slurmd: TLS: Successfully got signed certificate from slurmctld:
    -----BEGIN CERTIFICATE-----
    . . .
    -----END CERTIFICATE-----

[DebugFlags=AuditTLS](slurm.conf.md#OPT_AuditTLS) can also be used to show less verbose logs of certificate renewal.
