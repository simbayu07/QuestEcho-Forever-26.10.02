# QuestEcho 1.9.4 compatibility fixes

## Source and scope

This snapshot was copied from the user's installed QuestEcho 1.9.4 on 2026-10-02 after the three fixes below. The repository previously contained 1.7.0 addon files despite having a 1.9.4 Git tag. The existing Git history, screenshot and original README are retained. The new snapshot has all 15 files from the addon directory, including its own icon and 60-byte silence resource. External voice packs and SavedVariables are excluded.

Upstream: https://github.com/LeySure/QuestEcho-Forever. Author: Leysure. Upstream copyright notices are unchanged. No new license is applied to upstream code.

## Local changes relative to the audited 1.9.4 release

1. `QuestEcho112.lua`: require the absence of a numeric `WOW_PROJECT_ID` before enabling the original 1.12 compatibility layer. Modern Forever 16001 and Era 11509 otherwise incorrectly matched the old `INTERFACE < 20000` condition. That layer replaced global frame creation and discarded native callback arguments, causing `elapsed=nil` and other cross-addon errors.
2. `Core.lua`: classify projects 1 and 18 with Interface 16000–16999 as modern Forever. Exclude modern clients from the old vanilla and music-channel fallback paths, keeping normal sound handles and `StopSound`. The modern classification also avoids the legacy chat-frame override. Existing Retail handling and clients without a modern project identifier retain their original paths.
3. `QuestEcho.toc`: remove the explicit `Bindings.xml` entry. The file remains in the addon root with all three bindings; the client loads it through its dedicated binding mechanism instead of the ordinary UI XML parser.

The other 12 installed files are unchanged from the local 1.9.4 release. No change to voice data, queue content or saved user settings is required. A client reload is needed for newly loaded globals and callbacks to take effect.

## Provenance and checksums

Original release files accepted by the patch tool:

| File | Original SHA-256 |
| --- | --- |
| `Core.lua` | `2808eb9e20cc34b74b4e383753093d9ea9f2e8a19db806e932ea3c728fdd03b4` |
| `QuestEcho112.lua` | `57186cfe69c9daf4022a0f31ce7b9c3abdaa35d1f70823a50edc2701426b311c` |
| `QuestEcho.toc` | `5a39c43e6999d80477d698571aad6be7020b1c958a8fdbb73d2ce45498e51066` |

Local backup stages were named `QuestEcho-1.9.4-20261002-compat`, `QuestEcho-1.9.4-20261002-bindings` and `QuestEcho-1.9.4-20261002-project18`. Backups stay outside the repository and game addon folder. [installed-snapshot.json](installed-snapshot.json) records current file hashes without machine-specific paths.

The original two-file compatibility hotfix had Core SHA-256 `9c2f4c2d28e9a2080d9de63a2a7c192f1e2e8b22377e19a2054d23477275265c`; the tool can migrate exactly that prior revision to the project-18 fix.

## Reapply to a separately installed audited 1.9.4 release

The checked-in addon already contains the fixes. The standalone Python 3 tool is retained to validate or reapply them after replacing an installation with the exact audited release:

```sh
python3 tools/patch_questecho_194.py '/path/to/Interface/AddOns/QuestEcho'
python3 tools/patch_questecho_194.py '/path/to/Interface/AddOns/QuestEcho' \
  --apply --backup-dir '/path/to/backups/QuestEcho-1.9.4-local-fix'
```

The default operation only checks. Applying requires a new backup directory outside the addon folder. The tool checks the version and complete file hashes, rejects unknown edits before writing, and is idempotent. A partial write failure restores only the files it attempted to change. Do not bypass these checks for newer QuestEcho versions.

## Validation

The snapshot is byte-for-byte identical to the 15 files in the installed fixed addon. The patcher's read-only check reports `already_patched`. All Lua source files are syntax-checked with Lua 5.1; TOC references and the binding XML are checked for completeness.

The Dialogue UI integration regression suite reads this local snapshot and covers native callback arguments on projects 1, 18 and 2, sound handles, playback/stop, queue isolation, legacy classification, patch idempotence, unknown-source refusal and safe handling of concurrent/partial writes. These use real QuestEcho source with simulated game APIs. They do not substitute for in-game validation on every client.
