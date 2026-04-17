# JSON Web Tokens (JWT) Authentication

Slurm provides a https://datatracker.ietf.org/doc/html/rfc7519 compliant implementation of https://jwt.io/. This authentication can be used as an **AuthAltType**, usually alongside **auth/munge** as the **AuthType**. The only supported communication direction is from a client connecting to **slurmctld** and **slurmdbd**. This means that certain scenarios (specifically interactive jobs using **srun**) are currently not supported for clients with auth/jwt enabled (or that have SLURM_JWT in their environment).

## Prerequisites

JWT requires [libjwt](related_software.md#jwt). Both the library and the development headers must be available when Slurm is compiled.

## Full root trust in JWT creation {#trust_jwt_create}

The power to create JWTs is the power of root on a cluster. This is a per-site decision on what/who/when/how to trust. If a given authentication system can not be fully trusted with the powers of root for the entire cluster, then an authenticating proxy will need to be used to divide up the trust and implement the site\'s specific policies before the requests reach Slurm (specifically slurmrestd). While possibly inefficient, there is no technical reason that tiers of authenticating proxies can not be used if there is a lack of trust but a desire to allow creation of lesser auth tokens. Each site will need to weight the risks and benefits of which JWTs to trust before implementing any system. Once a job has been queued, the proxied authentication system will no longer be involved and the job will run with that user\'s permissions and access per Linux/POSIX\'s ACLs and trusts.

## Models of trust {#models_trust}

There are several ways to handle controlling JWT authentication and access. Slurm JWT plugin implementation is purposefully simple and will not be able to support most models of trust needed by sites. There already exists a plethora of authentication systems, and the expectation is that any site that wants more complexity than the default offering will use one of those systems instead.

- External JWT generation

  We provide an example python script for generating new JWTs but they are a standard and most languages have existing tooling for them. This is usually the easiest route for sites but does require each site to implement the tooling for their users directly.

- Authenticating proxy

  This is the most versatile option, as any authentication system can be placed in front of slurmrestd. It requires creating a slurmuser/root token that can then be used to proxy for any user. There are existing solutions for this with Nginx and Apache, and probably every other non-trivial proxy. We suggest choosing the preferred proxy and finding an existing setup guide for authenticating via that proxy. The proxy will need to have the **X-SLURM-USER-TOKEN** and **X-SLURM-USER-NAME** headers defined.

  There is no requirement that an authenticating proxy implement JWT for clients. This is the primary benefit of authenticating proxies; they can use any authentication method since they are the trusted point that tells Slurm which user the request is from. These authentication tokens are only used by the proxy and are not passed to the job. This is generally not an issue as once the job is in Slurm, it runs as the Posix user with all of the inherent trust of that user and it then uses `auth/munge` or `auth/slurm` for everything after that.

- JWKS

  This is like an authentication proxy, as another system is used to create the tokens, but it skips having the authentication system in front of Slurm by using signed public keys. This tends to be the preferred solution for sites using cloud authentication systems, such as:

  - https://aws.amazon.com/blogs/hpc/using-the-slurm-rest-api-to-integrate-with-distributed-architectures-on-aws/
  - https://www.keycloak.org/ - Using keycloak is an option which doesn\'t require a cloud auth solution.

## Setup for Standalone Use {#setup}

1.  [Configure and build Slurm with JWT support](related_software.md#jwt)

2.  Add the same JWT key to both the controller and slurmdbd (if used). For the controller only, it is recommended to put the JWT key in the StateSaveLocation. For example, using /var/spool/slurm/statesave/:

        dd if=/dev/random of=/var/spool/slurm/statesave/jwt_hs256.key bs=32 count=1
        chown slurm:slurm /var/spool/slurm/statesave/jwt_hs256.key
        chmod 0600 /var/spool/slurm/statesave/jwt_hs256.key
        chown slurm:slurm /var/spool/slurm/statesave
        chmod 0755 /var/spool/slurm/statesave

    The key does not have to be in the StateSaveLocation, but that is a convenient location if you have multiple controllers since it is shared between them. The key should not be placed in a directory where non-admin users might be able to access it. The key file should be owned by **SlurmUser** or **root**, with recommended permissions of 0400. The file must not be accessible by \'other\'.

3.  In both slurm.conf and slurmdbd.conf, add JWT as an alternative authentication type:

        AuthAltTypes=auth/jwt
        AuthAltParameters=jwt_key=/var/spool/slurm/statesave/jwt_hs256.key

4.  Restart slurmctld

5.  Create tokens for users as desired:

        scontrol token username=$USER

    An optional **lifespan=\$LIFESPAN** option can be used to change the token lifespan from the default 1800 seconds. The root account, or **SlurmUser** account can be used to generate tokens for any user. Alternatively, a user may use the command to generate tokens for themselves by simply calling

        scontrol token

    Note that administrators can prevent users from generating tokens by setting the following parameter in slurm.conf:

        AuthAltParameters=disable_token_creation

    This functionality is provided to allow sites to control when and how users are provided tokens along with controlling the token lifespans.

6.  Export the **SLURM_JWT** environment variable before calling any Slurm command.

7.  Export the **SLURM_JWT=daemon** environment variable before starting the slurmrestd daemon to activate *AuthAltTypes=auth/jwt* as the primary authentication mechanism.

## External Authentication Integration with JWKS and RS256 Tokens {#external_auth}

Starting with the 21.08 release, Slurm can support RS256 tokens such as those generated by https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html, https://azure.github.io/azure-workload-identity/docs/installation/self-managed-clusters/oidc-issuer/jwks.html, or https://www.keycloak.org/docs/latest/securing_apps/#\_client_authentication_adapter.

To enable Slurm\'s RS256 token support, an appropriate JWKS file must be downloaded and configured as such:

    AuthAltTypes=auth/jwt
    AuthAltParameters=jwks=/var/spool/slurm/statesave/jwks.json

The jwks file should be owned by **SlurmUser** or **root**, must be readable by **SlurmUser**, with recommended permissions of 0400. The file must not be writable by \'other\'.

Note that, by default, the built-in ability to generate HS256 tokens will be disabled when JWKS support is enabled. It can be re-enabled by explicitly configuring the **jwt_key=** option alongside **jwks=**.

Note: Slurm ignores the **x5c** and **x5t** fields and does not attempt to verify the certificate chain if presented in the JWKS file. JWTs are only verified against RSA 256 bit keys provided via **e** and **n** fields.

JWKS has signing keys that receive trust by being placed in the jwks.json. Those trusted keys can then create new tokens (which are JWTs) for any user by signing them. JWKS does not support adding keys for individual users but only for adding trusted signing keys.

JWT and JWKS can coexist in Slurm. Slurm will auto-disable JWT when JWKS is configured as a safety mechanism, to avoid accidentally having both enabled at the same time.

### Keycloak

https://www.keycloak.org/ can be used to manage authentication tokens through JWT or JWKS. Certain items should be customized when using it with Slurm. Refer to the https://www.keycloak.org/getting-started/getting-started-docker for initial setup. Or, if you need to automate the initial setup, you can implement the following customizations:

1.  `startup.sh` (replace `secret` with a randomly generated client secret):

        #!/bin/bash
        export SECRET=secret
        /opt/keycloak/bin/kc.sh bootstrap-admin service --client-id test --client-secret:env=SECRET
        exec /opt/keycloak/bin/kc.sh start-dev --log=console --log-console-level=debug --http-enabled true

2.  Dockerfile:

        FROM keycloak/keycloak
        COPY startup.sh /startup.sh
        ENTRYPOINT [ "/startup.sh" ]

3.  Environment variables (replace with actual username and password):

        KC_BOOTSTRAP_ADMIN_USERNAME=admin
        KC_BOOTSTRAP_ADMIN_PASSWORD=password

Once you have a running KeyCloak instance, log into the admin console and create a new Realm, User, and Client as documented in their https://www.keycloak.org/getting-started/getting-started-docker. When creating the client, ensure that **Direct access grants** is checked. You can then set up a mechanism to use to integrate this authentication method into Slurm.

For example, using **JWKS**:

1.  Create a JSON file with valid RS256 keys:

        curl "http://10.11.1.23:8080/realms/master/protocol/openid-connect/certs" > /etc/slurm/jwks.json

2.  Point Slurm to that file for authentication:

        AuthAltTypes=auth/jwt
        AuthAltParameters=jwks=/etc/slurm/jwks.json,userclaimfield=preferred_username

Alternately, using **JWT**:

1.  Create script to generate JWT from KeyCloak:

        #!/bin/bash
        [ -z "$1" -o -z "$2" ] && echo "USAGE:\n$0 {user_name} {user_password}" && exit 1

        curl -s \
        Â Â -d "client_id=test" \
        Â Â -d "client_secret=secret" \
        Â Â -d "username=$1" \
        Â Â -d "password=$2" \
        Â Â -d "grant_type=password" \
        Â Â -d "scope=openid" \
        Â Â "http://10.11.1.23:8080/realms/master/protocol/openid-connect/token" | \
        Â Â jq -r '.id_token'

2.  You can then use that script to set the JWT variable for Slurm commands or REST API requests:

        env SLURM_JWT=$(get_keycloak_jwt.sh username password) \
        sbatch -o none -e none --wrap 'unset SLURM_JWT; srun uptime'

### User Mapping {#user_mapping}

Depending on the service used to generate tokens, you may run into issues mapping the token to a username. Slurm defaults to using the `sun` (Slurm UserName) field. If the service uses a different field, you will need to correct this for it to work with Slurm.

**Option 1**: Change Slurm to use a different field. This can be customized using [AuthAltParameters=userclaimfield](slurm.conf.md#OPT_userclaimfield=). For example, using the default field for https://www.keycloak.org/:

    AuthAltParameters=jwks=/local/path/to/jwks.json,userclaimfield=preferred_username

**Option 2**: Change the identity service to use a different field. In KeyCloak 25.0, for example, you should find this option under **Clients -\> Client details -\> Dedicated scopes -\> Mapper details**. Change the username mapping to use the `sun` field.

## Compatibility

Slurm uses libjwt to view and verify https://datatracker.ietf.org/doc/html/rfc7519 JWT tokens. Compliant tokens generated by another solution can be used as long as the following requirements are met:

1.  Required tokens for Slurm are present:
    - iat: Unix timestamp of creation date.
    - exp: Unix timestamp of expiration date.
    - sun or username: Slurm UserName ( https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_437).
2.  Tokens are signed with HS256 algorithm compliant to RFC7518. RS256 is also supported to verify tokens, although Slurm cannot create them directly.
3.  Signing key is provided to slurmctld and slurmdbd to allow decryption of the tokens. Slurm currently only supports a single signing key.

The following scripts require the installation of the JWT Python module. This script can serve as an example of what you might do to generate a jwt key for use with Slurm.

    #!/usr/bin/env python3
    import sys
    import os
    import pprint
    import json
    import time
    from datetime import datetime, timedelta, timezone

    from jwt import JWT
    from jwt.jwa import HS256
    from jwt.jwk import jwk_from_dict
    from jwt.utils import b64decode,b64encode

    if len(sys.argv) != 3:
        sys.exit("gen_jwt.py [user name] [expiration time (seconds)]");

    with open("/var/spool/slurm/statesave/jwt.key", "rb") as f:
        priv_key = f.read()

    signing_key = jwk_from_dict({
        'kty': 'oct',
        'k': b64encode(priv_key)
    })

    message = {
        "exp": int(time.time() + int(sys.argv[2])),
        "iat": int(time.time()),
        "sun": sys.argv[1]
    }

    a = JWT()
    compact_jws = a.encode(message, signing_key, alg='HS256')
    print("SLURM_JWT={}".format(compact_jws))

Similarly, the following script can be used as an example of how you might verify that a jwt key is valid for use with Slurm.

    #!/usr/bin/env python3
    import sys
    import os
    import pprint
    import json
    import time
    from datetime import datetime, timedelta, timezone

    from jwt import JWT
    from jwt.jwa import HS256
    from jwt.jwk import jwk_from_dict
    from jwt.utils import b64decode,b64encode

    if len(sys.argv) != 2:
        sys.exit("verify_jwt.py [JWT Token]");

    with open("/var/spool/slurm/statesave/jwt.key", "rb") as f:
        priv_key = f.read()

    signing_key = jwk_from_dict({
        'kty': 'oct',
        'k': b64encode(priv_key)
    })

    a = JWT()
    b = a.decode(sys.argv[1], signing_key, algorithms=["HS256"])
    print(b)
