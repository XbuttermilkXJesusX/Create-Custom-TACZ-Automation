#!/usr/bin/env python3
"""Repackage Create: Custom TACZ Automation v1.2.2 from PRMA compiled code
and this source overlay's recipes and assets. Not a Java compile.
"""
from pathlib import Path
import argparse
import zipfile
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--upstream', required=True, type=Path,
                    help='Original prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar')
parser.add_argument('--output', type=Path, default=root / 'build/libs/Create-Custom-TACZ-Automation-1.2.2.jar')
args = parser.parse_args()
resources = root / 'src/main/resources'
if not args.upstream.is_file():
    sys.exit(f'Original PRMA JAR not found: {args.upstream}')
if not resources.is_dir():
    sys.exit(f'Source resources not found: {resources}')
resource_files = {p.relative_to(resources).as_posix(): p for p in resources.rglob('*') if p.is_file()}
args.output.parent.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(args.upstream, 'r') as upstream, zipfile.ZipFile(args.output, 'w', zipfile.ZIP_DEFLATED) as output:
    seen = set()
    for info in upstream.infolist():
        if info.is_dir():
            continue
        name = info.filename
        # Preserve original executable classes and binary packaging metadata.
        # Recipes/assets come ONLY from the overlay, not the old JAR.
        if (name.endswith('.class') or name == 'mixin.refmap.json' or
                name.startswith('.cache/') or
                (name.startswith('META-INF/') and name != 'META-INF/mods.toml')):
            if name not in resource_files and name not in seen:
                output.writestr(name, upstream.read(name))
                seen.add(name)
    for name, path in sorted(resource_files.items()):
        if name in seen:
            continue
        output.write(path, name)
        seen.add(name)
with zipfile.ZipFile(args.output) as built:
    failure = built.testzip()
    if failure:
        sys.exit(f'JAR integrity check failed: {failure}')
    print(f'Created {args.output} with {len(built.namelist())} files')
