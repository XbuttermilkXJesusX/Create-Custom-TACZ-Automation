#!/usr/bin/env python3
"""Update Forge update.json from released CurseForge files.

Uses CurseForge Core API; set CURSEFORGE_API_KEY in the environment.
Run automatically by .github/workflows/sync-curseforge-updates.yml.
No dependencies outside Python's standard library.
"""
import argparse
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

MOD_ID = 1758542
GAME_VERSION = "1.20.1"
HOMEPAGE = "https://www.curseforge.com/minecraft/mc-mods/create-custom-tacz-automation"
API = f"https://api.curseforge.com/v1/mods/{MOD_ID}/files"
# The mod's release file naming convention; avoid confusing 1.20.1 with a mod version.
RELEASE_VERSION = re.compile(r"(?i)Create[-_ ]Custom[-_ ]TACZ[-_ ]Automation[-_ ]v?(\d+\.\d+\.\d+)(?=[-_. ]|$)")


def read_files(api_key):
    files = []
    for index in range(0, 2000, 50):
        args = urllib.parse.urlencode({"gameVersion": GAME_VERSION, "index": index, "pageSize": 50})
        request = urllib.request.Request(API+"?"+args,
             headers={"Accept": "application/json", "x-api-key": api_key, "User-Agent": "CustomTaczAutomationForgeUpdateFeed/1.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
        batch = result.get("data", [])
        if not isinstance(batch, list):
            raise ValueError("Unexpected response from CurseForge: data is not an array")
        files.extend(batch)
        pagination = result.get("pagination") or {}
        if len(batch) < 50 or ("totalCount" in pagination and index+len(batch) >= pagination["totalCount"]):
            break
    return files


def version_tuple(value):
    return tuple(int(x) for x in value.split("."))


def generate(files, old):
    candidates = []
    for file in files:
        if not file.get("isAvailable", True):
            continue
        game_versions = file.get("gameVersions") or []
        if GAME_VERSION not in game_versions:
            continue
        # Do not consider Fabric/NeoForge versions as Forge-compatible.
        lower = {str(v).lower() for v in game_versions}
        if "fabric" in lower or "neoforge" in lower or "quilt" in lower:
            continue
        filename = file.get("fileName") or ""
        match = RELEASE_VERSION.search(filename)
        if not match:
            continue
        version = match.group(1)
        release_type = int(file.get("releaseType", 1))
        candidates.append((version_tuple(version), version, release_type, file))
    if not candidates:
        raise ValueError("CurseForge returned no compatible 1.20.1 Forge release files. Feed unchanged.")
    candidates.sort(key=lambda c:(c[0],c[3].get("fileDate", "")))
    latest = candidates[-1][1]
    stable = [c for c in candidates if c[2] == 1]
    recommended = stable[-1][1] if stable else latest
    changelogs = dict(old.get(GAME_VERSION, {}))
    for _, version, _, file in candidates:
        changelogs[version] = f"CurseForge release: {file.get('fileName', version)}. View the project page for details."
    # Only public releases from this CurseForge project contribute to the promotions.
    sorted_versions = {k: changelogs[k] for k in sorted(changelogs,key=version_tuple)}
    return {
       "homepage": HOMEPAGE,
       GAME_VERSION: sorted_versions,
       "promos": {f"{GAME_VERSION}-latest": latest,
                  f"{GAME_VERSION}-recommended": recommended}
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parents[1]/"update.json")
    parser.add_argument("--fixture",type=Path,help="Offline test: use file list JSON instead of contacting CurseForge")
    args=parser.parse_args()
    if args.output.exists():
        old=json.loads(args.output.read_text(encoding="utf-8"))
    else:
        old={}
    if args.fixture:
        fixture=json.loads(args.fixture.read_text(encoding="utf-8"))
        files=fixture["data"] if isinstance(fixture,dict) else fixture
    else:
        key=os.environ.get("CURSEFORGE_API_KEY", "")
        if not key:
            sys.exit("CURSEFORGE_API_KEY is not set; update.json was NOT changed")
        try:
            files=read_files(key)
        except (urllib.error.URLError,ValueError) as e:
            sys.exit(f"CurseForge API lookup failed; update.json was NOT changed: {e}")
    updated=generate(files,old)
    new_text=json.dumps(updated,indent=2,ensure_ascii=False)+"\n"
    if args.output.exists() and args.output.read_text(encoding="utf-8")==new_text:
        print("No release changes")
        return
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(new_text,encoding="utf-8")
    print("Updated",args.output,"latest",updated["promos"]["1.20.1-latest"])

if __name__ == "__main__":
    main()
