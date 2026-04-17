# [Slurm APIs]{#top}

### Overview

All of the Slurm commands utilize a collection of Application Programming Interfaces (APIs) exposed through the \"slurm.h\" and \"slurmdb.h\" headers. Slurm\'s APIs are fixed within each major release. They do change --- significantly --- between each major release.

Developers are encouraged to target Slurm\'s [REST API](rest_api.md) which provides for broader cross-version compatibility.
