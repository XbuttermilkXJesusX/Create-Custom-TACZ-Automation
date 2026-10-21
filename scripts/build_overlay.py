#!/usr/bin/env python3
"""Build the v1.2.1 Forge JAR by combining unchanged upstream compiled code
with this repository's editable assets/recipes/metadata. Requires PRMA 0.4.4
compiled JAR supplied locally by the user. This is NOT Java source compilation.
"""
from pathlib import Path
import argparse
import zipfile
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--upstream', required=True, type=Path,
                    help='Path to prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar')
parser.add_argument('--output', type=Path, default=Path('build/libs/Create-Custom-TACZ-Automation-1.2.1.jar'))
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
resources = root / 'src/main/resources'
if not args.upstream.is_file():
    sys.exit('Upstream PRMA JAR not found: ' + str(args.upstream))
args.output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(args.upstream, 'r') as upstream, zipfile.ZipFile(args.output, 'w', zipfile.ZIP_DEFLATED) as out:
    # Only code and class-related mixin mapping are borrowed from upstream.
    for info in upstream.infolist():
        if info.is_dir():
            continue
        name = info.filename
        if name.endswith('.class') or name == 'mixin.refmap.json':
            out.writestr(name, upstream.read(name))
    # All editable recipe/data/assets/Forge metadata come from repo.
    for path in sorted(resources.rglob('*')):
        if path.is_file():
            out.write(path, path.relative_to(resources).as_posix())
with zipfile.ZipFile(args.output) as check:
    if check.testzip() is not None:
        sys.exit('JAR integrity check failed')
    print(f'Created {args.output}: {len(check.namelist())} entries')
