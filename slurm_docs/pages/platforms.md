# Platforms

## Operating Systems {#os}

- **FreeBSD** --- Limited support, not actively tested.
- **Linux** --- Slurm has been thoroughly tested on most popular Linux distributions using arm64 (aarch64), ppc64, and x86_64 architectures. Some features are limited to recent releases and newer Linux kernel versions. Currently supported distributions include:
  - Debian 11 (Bullseye)
  - Debian 12 (Bookworm)
  - Debian 13 (Trixie)
  - RedHat Enterprise Linux 8 (RHEL8) and RHEL8 derivatives
  - RedHat Enterprise Linux 9 (RHEL9) and RHEL9 derivatives
  - RedHat Enterprise Linux 10 (RHEL10) and RHEL10 derivatives
  - SUSE Linux Enterprise Server (SLES) 12
  - SUSE Linux Enterprise Server (SLES) 15
  - Ubuntu 20.04
  - Ubuntu 22.04
  - Ubuntu 24.04
- **NetBSD** --- Limited support, not actively tested.
- **macOS** --- Slurm has run on macOS in the past, but does not currently. It should be possible to fix this with some adjustments to linker and compiler flags, and any patches would be appreciated.

## Databases {#database}

Slurm will be built with support for MySQL if it finds supported development libraries at build time. Although it is possible to build Slurm against older versions of MySQL, it is not recommended. SchedMD recommends you use a currently supported version of MySQL or MariaDB.

Further reading:

- [Quick Start Administrator Guide](quickstart_admin.md)
- [Accounting and Resource Limits](accounting.md)
- [Upgrade Guide](upgrades.md)

## Accelerators {#accel}

Slurm has optional support for managing a variety of accelerator cards. Specific plugins have been developed for:

- **gres/gpu** --- several autodetection plugins are available for different vendors:
  - **AutoDetect=nvml** enables autodetection of NVIDIA GPUs through their proprietary NVML library.
  - **AutoDetect=nvidia** also enables autodetection of NVIDIA GPUs, but through generic Linux interfaces rather than their proprietary library. This plugin doesn\'t detect MIGs or NVlinks.
  - **AutoDetect=rsmi** enables autodetection of AMD GPUs through their proprietary RSMI library (tested on x86_64 and arm64).
  - **AutoDetect=oneapi** enables autodetection of Intel GPUs through their proprietary oneAPI library.
  - **AutoDetect=nrt** enables autodetection of AWS Trainium/Inferentia devices.
- **gres/mps** --- NVIDIA CUDA Multi-Process Service provides ways to share GPUs between multiple compute processes
- **gres/shard** --- Generic mechanism that provides a way to share GPUs between multiple compute processes
