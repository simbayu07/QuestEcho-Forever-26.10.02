#!/usr/bin/env python3
"""Apply a narrow, backed-up local fix to the audited QuestEcho 1.9.4 release.

Default is read-only. Does not ship upstream source or touch audio/settings.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil


PATCHES = {
    "QuestEcho.toc": (
        "5a39c43e6999d80477d698571aad6be7020b1c958a8fdbb73d2ce45498e51066",
        (("Minimap.lua\r\nBindings.xml\r\n", "Minimap.lua\r\n"),),
    ),
    "QuestEcho112.lua": (
        "57186cfe69c9daf4022a0f31ce7b9c3abdaa35d1f70823a50edc2701426b311c",
        (("local IS_112 = (INTERFACE < 20000)",
          'local IS_112 = (INTERFACE < 20000) and type(WOW_PROJECT_ID) ~= "number"'),),
    ),
    "Core.lua": (
        "2808eb9e20cc34b74b4e383753093d9ea9f2e8a19db806e932ea3c728fdd03b4",
        (("local IS_MODERN_API = (TOC_VERSION >= 90000)",
          'local IS_MODERN_API = (TOC_VERSION >= 90000) or ((WOW_PROJECT_ID == 1 or WOW_PROJECT_ID == 18) and TOC_VERSION >= 16000 and TOC_VERSION < 17000)'),
         ("local IS_VANILLA_ERA = (TOC_VERSION < 20000)",
          'local IS_VANILLA_ERA = (TOC_VERSION < 20000) and type(WOW_PROJECT_ID) ~= "number"'),
         ("local MUSIC_CHANNEL_PLAYBACK = (not IS_VANILLA_ERA)",
          'local MUSIC_CHANNEL_PLAYBACK = (not IS_VANILLA_ERA) and type(WOW_PROJECT_ID) ~= "number"')),
    ),
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def transform(name, data):
    """Accept only the audited original bytes or our exact patched result."""
    expected, replacements = PATCHES[name]
    original = data
    # Recognize the exact first hotfix, then normalize it to the current one.
    if name == "Core.lua" and digest(data) == "9c2f4c2d28e9a2080d9de63a2a7c192f1e2e8b22377e19a2054d23477275265c":
        original = data.replace(
            b"(WOW_PROJECT_ID == 1 and TOC_VERSION >= 16000 and TOC_VERSION < 17000)",
            b"((WOW_PROJECT_ID == 1 or WOW_PROJECT_ID == 18) and TOC_VERSION >= 16000 and TOC_VERSION < 17000)", 1)
    if digest(original) != expected:
        for before, after in replacements:
            if original.count(after.encode()) != 1:
                raise ValueError(f"{name}: unrecognized source; no files changed")
            original = original.replace(after.encode(), before.encode(), 1)
        if digest(original) != expected:
            raise ValueError(f"{name}: unrecognized source; no files changed")
    result = original
    for before, after in replacements:
        if result.count(before.encode()) != 1:
            raise ValueError(f"{name}: patch context is not unique")
        result = result.replace(before.encode(), after.encode(), 1)
    return result


def prepare(addon_dir):
    toc = (addon_dir / "QuestEcho.toc").read_text(encoding="utf-8-sig")
    if not re.search(r"^## Version:\s*1\.9\.4\s*$", toc, re.MULTILINE):
        raise ValueError("Only the audited QuestEcho 1.9.4 release is supported")
    changes = {}
    for name in PATCHES:
        original = (addon_dir / name).read_bytes()
        updated = transform(name, original)
        if original != updated:
            changes[name] = (original, updated)
    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("addon_dir", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--backup-dir", type=Path)
    args = parser.parse_args()
    changes = prepare(args.addon_dir)
    report = {"addon_dir": str(args.addon_dir), "mode": "apply" if args.apply else "check",
              "files": {name: {"before": digest(old), "after": digest(new)}
                        for name, (old, new) in changes.items()}}
    if args.apply and changes:
        if args.backup_dir is None:
            parser.error("--apply requires a new --backup-dir outside the addon directory")
        backup = args.backup_dir.resolve()
        if backup == args.addon_dir.resolve() or args.addon_dir.resolve() in backup.parents:
            parser.error("backup must be outside the addon directory")
        backup.mkdir(parents=True, exist_ok=False)
        for name in changes:
            shutil.copy2(args.addon_dir / name, backup / name)
        (backup / "manifest.json").write_text(json.dumps(report, indent=2) + "\n")
        # Reject concurrent edits before entering a block that may restore bytes.
        for name, (old, _) in changes.items():
            if (args.addon_dir / name).read_bytes() != old:
                raise ValueError(f"{name}: changed during patching; stop and inspect")
        attempted = []
        try:
            for name, (_, new) in changes.items():
                # Include a failing write because it may have written only part.
                attempted.append(name)
                (args.addon_dir / name).write_bytes(new)
            for name, (_, new) in changes.items():
                if (args.addon_dir / name).read_bytes() != new:
                    raise OSError(f"{name}: verification failed")
        except Exception:
            for name in reversed(attempted):
                (args.addon_dir / name).write_bytes(changes[name][0])
            raise
        report["backup_dir"] = str(backup)
    report["status"] = "patched" if args.apply and changes else "needs_patch" if changes else "already_patched"
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
