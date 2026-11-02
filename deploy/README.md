# Skill runtime delivery

The release maintainer remains the content owner. One native systemd timer
per consuming host downloads the stable GitHub Release, verifies its checksum,
complete file manifest and public-document index, and atomically replaces
`/var/lib/sai-skills/current`. Consumers read fixed local version directories.
An unavailable source, invalid package, modified local tree, conflicting
version or downgrade leaves the previous version selected. There is no model
call, question-path download or new service process.

```mermaid
flowchart LR
  Release[Approved GitHub Release] --> Timer[Hourly systemd task]
  Timer --> Store[Verified version directory]
  Store --> Current[Atomic current link]
  Current --> Bot[Bot local index]
  Current --> Pilot[Pilot native Skill provider]
  Pilot -->|User clicks Install| Home[User-owned native Agent directory]
```

Build the reproducible, standard-library-only runtime with Python 3.10 or later:

```sh
python3 skill_package.py runtime --output dist/sai-skill-package.pyz
```

Deploy that exact artifact at
`/usr/local/lib/sai-skills/sai-skill-package.pyz` (root-owned, mode 0644),
alongside these two unit files in `/etc/systemd/system`. The consuming host
needs Python 3.10+, a system CA bundle and outbound HTTPS to GitHub
and its release assets. Version discovery uses GitHub's native stable-release
redirect, without API credentials or anonymous API quota. No exporter
dependencies or credentials are required.
The service's only writable persistent directory is its native StateDirectory.

Before the first migration, compare the candidate public document IDs against
the existing consumer manifest and review every removal. This is a release
preflight; do not maintain another permanent corpus list. Then run the service
once, read back the package and consumer behavior, and enable the timer:

```sh
systemctl daemon-reload
systemctl start sai-skills-update.service
python3 /usr/local/lib/sai-skills/sai-skill-package.pyz current --store /var/lib/sai-skills --require-index
systemctl enable --now sai-skills-update.timer
```

Enable both consumers only with the same qualified content release. The Bot
points its existing knowledge plugin at
`/var/lib/sai-skills/current/sai-user-guide/references`; Pilot's native provider
uses the fixed path returned by `current`. Their existing reload mechanisms
verify new content before publishing it to a request. The old 0.2.3 package
has no public-document index and is intentionally refused by `--require-index`.

`current` returns the installed version, fixed path, release URL, archive
SHA-256 and latest update attempt. Failures are visible in `status.json`, the
command's nonzero JSON result and `journalctl -u sai-skills-update.service`.
The timer checks once an hour, with up to five minutes of jitter, including
missed runs after reboot. A failed check is retried at the next timer event.

Pilot's one-click action calls `install-user --store /var/lib/sai-skills
--agent codex|opencode|claude`; `--dry-run` returns the exact target first.
The tool rejects root and obtains the real effective UID's home from NSS,
not browser input or `$HOME`. Codex and OpenCode use `~/.agents/skills`;
Claude Code uses `~/.claude/skills`. This installs a personal copy, with no
background writer. Repeating the action updates an unchanged managed copy;
local modifications are preserved and reported as `LOCAL_MODIFIED`. A native
file lock serializes concurrent installs. Backups retain original inodes at
`~/.local/share/sai-skill-backups`, outside discovery directories.
Earlier unchanged packages in `~/.codex/skills` and
`~/.config/opencode/skills` are moved into that same backup during installation,
so the new shared copy does not leave stale duplicates in native discovery.
Personal or unrecognized old copies are preserved and reported with their path.
SIGTERM enters normal rollback; after a hard process or host failure, inspect the
target and retained backup before retrying. Requests that lose their reply
must read back before being reported as completed.

To stop automatic updates, disable `sai-skills-update.timer`. Existing local
packages remain readable. To roll back content, stop the timer, verify the
chosen retained version with `check`, and atomically replace `current` using
the host's native symlink/rename commands. Read back both consumers; preserve
the old release directories until that readback passes. A same-version asset
replacement is rejected, so publish a new version for a content correction.
Personal copies belong to their users and are not rolled back by this action.

Validation in this repository covers local package transitions, failures,
ownership checks and CLI serialization. It does not establish a production
deployment or an authenticated Pilot browser installation.
