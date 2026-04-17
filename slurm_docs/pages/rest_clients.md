# REST API Client Writing Guide

See also:

- [REST API Quick Start Guide](rest_quickstart.md)
  - [Common Issues](rest_quickstart.md#common_issues)
- [REST API Details](rest.md)
- [REST API Methods and Models](rest_api.md)
- [slurmrestd man page](slurmrestd.md)
- [OpenAPI Plugin Release Notes](openapi_release_notes.md)

## Contents

- OpenAPI Specification (OAS)
- OpenAPI Standard Compliance
- OpenAPI Specification (OAS) Documentation
- Client design
- OpenAPI Specification (OAS) changes
  - Data Parser Lifecycle
  - Handling Format Changes

## OpenAPI Specification (OAS) {#openapi}

Slurmrestd is compliant with https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md. The generated OAS can be viewed at the following URLs:

- /openapi.json
- /openapi.yaml
- /openapi/v3

The generated OAS can be generated directly via calling:\

- Generate OAS with only a compiled slurmrestd:\
  `env SLURM_CONF=/dev/null slurmrestd --generate-openapi-spec -s slurmctld,slurmdbd -d v0.0.40`
- Generate OAS with fully configured Slurm install:\
  `slurmrestd --generate-openapi-spec -s slurmctld,slurmdbd -d v0.0.40`

The OAS is designed to be the primary documentation for the request methods and responses including their contents. There are several third party tools that automatically generate documentation against the OAS output listed by https://openapi.tools/. An example of how to generate the docs is here.

The generated OpenAPI specification changes depending on the configuration of slurmrestd at run time. [slurmrestd](slurmrestd.md) is a framework, and the actual content is provided by plugins, which are optional at runtime. However, the specific plugin versions (as noted by the v0.0.XX in the paths) will be stable across Slurm versions, if the relevant plugin is still present. Plugin life cycles are described [here](upgrades.md#openapi_changes).

## OpenAPI Standard Compliance {#openapi-compliance}

Slurm attempts to strictly comply with the relevant https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md. For reasons of compatibility, Slurm\'s OAS is tested against publicly available OpenAPI client generators, but Slurm does not directly support any of them as they are outside the control of SchedMD and may change at any time. The goal is to comply with the standards, supporting as many clients as possible, without favoring any one client. Sites are always welcome to write their own clients that are OpenAPI compliant. As a rule, SchedMD will debug the HTTP sent to and received by slurmrestd but will not directly debug any client source code.

Tested compatibility by OpenAPI plugins:

- openapi/slurmctld:
  - https://github.com/OpenAPITools/openapi-generator
  - https://github.com/oapi-codegen/oapi-codegen
- openapi/slurmdbd:
  - https://github.com/OpenAPITools/openapi-generator
  - https://github.com/oapi-codegen/oapi-codegen

## OpenAPI Specification (OAS) Documentation {#generated-openapi-docs}

Slurm includes [example generated documentation](rest_api.md), provided with each release. Slurm\'s documentation only includes the latest plugins to encourage sites to develop against the latest plugins, as they will have the longest lifespan and, by extension, the new clients will continue to work for longer. Plugin life cycles are described [here](upgrades.md#openapi_changes). This documentation is generated via the following steps using https://github.com/OpenAPITools/openapi-generator HTML output:

1.  Generate OAS:\
    ` env SLURM_CONF=/dev/null slurmrestd --generate-openapi-spec -s slurmctld,slurmdbd -d v0.0.40 > openapi.json `
2.  Generate documentation:\
    ` openapi-generator-cli generate -i openapi.json -g html -o rest_api_docs `
3.  Point browser to `rest_api_docs/index.html`

Swagger provides a https://editor-next.swagger.io/ to view and interact with the generated OAS. It makes generating clients and documentation via https://swagger.io/tools/swagger-codegen/ relatively simple.

## Client Design

Clients should always be generated against or designed to work with specific versions of the tagged paths from [slurmrestd](slurmrestd.md). Client developers are strongly encouraged to not include functionality for versions of methods not intended for use.

Client developers need to plan how to gracefully handle changes between different Slurm versions if they plan to support multiple versions. Slurm\'s method of versioning is done explicitly to allow old code to continue to work with newer Slurm releases while that older version is still supported. For example, v0.0.38 methods were added in Slurm-22.05 but can be used until Slurm-24.05. While this works, these methods will not get any new features or functionality, but generally only security fixes. Slurm will get several new features every release, and those changes are then reflected by the changes in the new plugin version. A client wishing to use the new features will have to move to the newer version as new features will not be backported.

Using an OpenAPI schema generated for just one version is advised. Many of the OpenAPI client generators have a way to strip out the version tag from the struct names (i.e. `V0039AccountFlagsDELETED` -\> `AccountFlagsDELETED`). This could allow for a set of unversioned base code could be created and then adjusted for material changes in the outputted code with newer Slurm versions. Having a strongly typed language can help with this considerably. Generally, only parts of the schema change between different versions for specific endpoints, although looking at a diff of them can be intimidating even if using something like https://jsondiff.com/. Another option is having wrappers to account for version differences in the same fashion as many c libraries account for differences between Windows and Linux.

The generated OpenAPI schema can change, depending on which plugins are present, but the versioned paths and their schemas will not (with limited exceptions). As such, generating a schema limited to only `v0.0.40` and placing it in your repo should result in a schema that can be used in Slurm-23.11 to Slurm-25.05. In general, regenerating the client code and OpenAPI schema will be counter-productive, as even the OpenAPI generators themselves can generate different results for the same OpenAPI specification between their versions. The same driver code would likely not even compile even though nothing about the server has changed. An example of this specific type of issue can be found https://github.com/oapi-codegen/oapi-codegen/tree/main?tab=readme-ov-file#action-required-the-repository-for-this-project-has-changed.

Developers may want to consider having a somewhat static set of compiled client code in your client\'s code repository. That code will then only need to be updated for revisions inside of the tagged versions, which are generally quite rare. That will remove the need for end users to run the code generators and limit the chances of any change disrupting your workflow. It will also allow you to plan for upgrades at a convenient time rather than having to ensure compatibility of multiple permutations at all times.

Developers should be aware that older versions of the versioned plugins are removed from Slurm in a documented cadence as given [here](upgrades.md#openapi_changes). Clients will need to be upgraded once the relevant plugins versions are removed to continue to communicate with slurmrestd.

If slurmrestd compiles, then all of it will compile. Run time args to slurmrestd and slurm.conf will, however, change the output of OAS. For instance, if slurmdbd accounting is not configured then the `/slurmdb/` paths will automatically **not** be included as there is an invalid prerequisite for them. A client that queries them will get a 404 error. Slurmrestd can and should be told to load the minimal number of plugins too (via -d and -s) which will also change which paths are present and thus included in the OAS. To slurmrestd, the OAS is just a form of documentation and doesn\'t have any bearing to how it functions. A client could be generated with many paths that the current running slurmrestd does not have loaded. That client will just get 404 errors for those queries and should try to avoid them via internal logic. The client only needs to have a matching OAS for the paths/endpoints that client will actually query. Since all endpoints in slurmrestd are versioned, there is an automatic guarantee they will work (if present) as though the client is querying the original slurmrestd it used to generate the original OAS it was compiled against. If a path of the same version does not behave the same, then that is a bug, and we kindly ask that a https://support.schedmd.com/.

There are very limited situations where slurmrestd will generate an OAS with the same endpoint having different functionalities.

- If the specification is somehow fundamentally broken so that it violates the OpenAPI standard. Slurm has test units to try catch this but those tests are not perfect.
- A new field or path has been added. This should never break a client as clients should ignore unknown fields in JSON/YAML.

## OpenAPI Specification (OAS) changes {#openapi-changes}

Changes to the OAS are always listed with every release in the [OpenAPI Release Notes](openapi_release_notes.md).

A simple trick to see the differences between versions is to query both and then mask the newer one, to avoid having diff list out every version tag that changed:

    env SLURM_CONF=/dev/null slurmrestd -d v0.0.41 -s slurmdbd,slurmctld --generate-openapi-spec > /tmp/v41.json
    env SLURM_CONF=/dev/null slurmrestd -d v0.0.40 -s slurmdbd,slurmctld --generate-openapi-spec > /tmp/v40.json
    cat /tmp/v41.json | sed -e 's#v0.0.41#v0.0.40#g' > /tmp/v41_masked.json
    vimdiff /tmp/v40.json /tmp/v41_masked.json
    jsondiff /tmp/v40.json /tmp/v41_masked.json

Sometimes this trick still produces too much change in the diff output to be useful. In those cases, selecting a specific (sub)schema can be helpful:

    jq '.components.schemas."v0.0.40_job"' /tmp/v40.json > /tmp/v40_job.json
    jq '.components.schemas."v0.0.40_openapi_job_info_resp".properties.jobs.items' /tmp/v41_masked.json > /tmp/v41_masked_job.json
    vimdiff /tmp/v40_job.json /tmp/v41_masked_job.json

The generated OpenAPI schemas are very detailed and get more detailed every release as we add more enums, better expose possible values and increase documentation in comments. Even minor changes to tree structure can result in a large number of changes in the generated schema, which can be confusing while looking at diffs. The example above shows the inlining of `v0.0.40_job` into `v0.0.40_openapi_job_info_resp`. Depending on the generated client, that change may not change the resultant client code at all.

### Data Parser Lifecycle {#data_parser_lifecycle}

  ------------------------ --------------------------------------------------------- ------------------------
  **data_parser plugin**   **Added in Release**                                      **Removed in Release**
  v0.0.39                  23.02 ([release notes](openapi_release_notes.md#23020))   24.11
  v0.0.40                  23.11 ([release notes](openapi_release_notes.md#23110))   25.11
  v0.0.41                  24.05 ([release notes](openapi_release_notes.md#24050))   26.05
  v0.0.42                  24.11 ([release notes](openapi_release_notes.md#24110))   26.11
  v0.0.43                  25.05 ([release notes](openapi_release_notes.md#25050))   27.05
  v0.0.44                  25.11 ([release notes](openapi_release_notes.md#25110))   27.11
  ------------------------ --------------------------------------------------------- ------------------------

The data_parser plugins are explicitly versioned with scheduled release and removal dates in the above table. The data_parser plugins are purposefully kept the same between releases and instead a new incremented version is added for every major release. This new version will be the only version to receive any changes in any content, formatting, bug fixes, or any other behavior visible to clients. This allows developers to keep using the same client after a Slurm upgrade, as long as it was written for a data_parser plugin that still exists in the new Slurm version. The exception to this rule is that all plugins will always receive any security related fixes according to the https://www.schedmd.com/security-policy/ as with any part of Slurm. The data_parser plugins provided upstream with Slurm in any release are considered to have the same support as any other part of that release.

The OpenAPI plugins (openapi/slurmctld and openapi/slurmdbd) are unversioned and drive the data_parser plugins to generate content. The OpenAPI plugins have no expected removal date and will have bug fixes applied as they will not change the presentation of the data to clients.

Planned deprecation of plugins, endpoints, parameters, fields, and values is being documented via the https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md?plain=1#L861 of setting \"Deprecated: True\" in generated OpenAPI specification. Any plugin that is not marked as deprecated will continue to exist in the next major Slurm release pending any critical issues which will be announced separately. Any plugin marked for deprecation will be removed on the next major release. In general, the last three plugins have been retained in each major release with the oldest always getting marked as deprecated.

**NOTE**: Sites are always encouraged to use the latest stable plugin version available for code development. There is no guarantee of compatibility between different versions of the same plugin with clients. Clients should always make sure to validate their code when migrating to newer versions of plugins. Plugin versions will always be included in the path for every method provided by a given plugin to ensure no two plugins will provide the same path.

As the data_parser plugins utilize the Slurm API internally, compatibility is entirely based on the Slurm version. Refer to the general [compatibility window](upgrades.md#compatibility_window) explanation for details.

### Handling Format Changes {#format_changes}

Any scripts or clients making use of `--json` or `--yaml` arguments with any CLI commands may need to pass the data_parser version explicitly to avoid issues after an upgrade. The default data_parser used is the latest version which may not have a compatible format with the prior versions. Sites can use the specification generation mode to compare formatting differences.

    $CLI_COMMAND --json=v0.0.41+spec_only > /tmp/v41.json;
    $CLI_COMMAND --json=v0.0.40+spec_only > /tmp/v40.json;
    json_diff /tmp/v40.json /tmp/v41.json;

In the event of a format incompatibility, the preferred data_parser can be requested explicitly starting with the v0.0.40 plugins in any release before the plugin\'s removal.

    $CLI_COMMAND --json=v0.0.41 $OTHER_ARGS | $SITE_SCRIPT;
    $CLI_COMMAND --json=v0.0.40 $OTHER_ARGS | $SITE_SCRIPT;
    $CLI_COMMAND --yaml=v0.0.41 $OTHER_ARGS | $SITE_SCRIPT;
    $CLI_COMMAND --yaml=v0.0.40 $OTHER_ARGS | $SITE_SCRIPT;

Any `slurmrestd` web clients can determine the relevant plugin being used by looking at the URL being queried. Example URLs:

    http://$HOST/slurmdb/v0.0.40/jobs
    http://$HOST/slurm/v0.0.40/jobs

The relevant data_parser plugin in the example URLs is \"v0.0.40\" which matches the `data_parser/v0.0.40` plugin. Plugin naming follows the naming schema of `vX.X.XX` where each X is a number. The naming schema matches the internal naming schema for Slurm\'s packed binary RPC layer but is not directly related. The URLs for each given data_parser plugins will remain a valid query target until the plugin is removed as part of SchedMD\'s commitment to ensure release limited backwards compatibility. While it should be possible to continue using any client from a prior release while the plugins are still supported, sites should always **recompile** any generated OpenAPI clients and **test thoroughly** before upgrading.
