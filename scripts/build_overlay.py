#!/usr/bin/env python3
"""Create v1.3.2 from a local original PRMA binary and editable resources.

This is not a Java source compilation; the patch's Java source is in
compatibility/src/main/java and verified working bytecode in compatibility/prebuilt.
"""
from pathlib import Path
import argparse, zipfile, sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--upstream', required=True, type=Path,
                    help='Original prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar')
parser.add_argument('--output', type=Path,
                    default=root / 'build/libs/Create-Custom-TACZ-Automation-1.3.2.jar')
args = parser.parse_args()
resources = root / 'src/main/resources'
patch = root / 'compatibility/prebuilt/dev/customtacz/compat/mixin/FactoryPanelScreenTaCZMixin.class'
if not args.upstream.is_file():
    sys.exit(f'Original PRMA JAR not found: {args.upstream}')
if not patch.is_file():
    sys.exit(f'Compiled compatibility patch missing: {patch}')
resource_files = {p.relative_to(resources).as_posix(): p
                  for p in resources.rglob('*') if p.is_file()}
args.output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(args.upstream,'r') as upstream, zipfile.ZipFile(args.output,'w',zipfile.ZIP_DEFLATED) as output:
    seen = set()
    for info in upstream.infolist():
        if info.is_dir():
            continue
        name = info.filename
        if (name.endswith('.class') or name == 'mixin.refmap.json' or
            name.startswith('.cache/') or
            (name.startswith('META-INF/') and name != 'META-INF/mods.toml')):
            if name == 'META-INF/MANIFEST.MF':
                original = upstream.read(name).decode('utf-8')
                if 'MixinConfigs:' in original:
                    sys.exit('Unexpected upstream MixinConfigs; requires manual merge')
                modified = (original.rstrip('\r\n') +
                    '\r\nMixinConfigs: extra_gauges_tacz_compat.mixins.json\r\n\r\n')
                output.writestr(name,modified.encode('utf-8'))
            else:
                output.writestr(name,upstream.read(name))
            seen.add(name)
    for name,path in sorted(resource_files.items()):
        if name in seen:
            continue
        output.write(path,name)
        seen.add(name)
    mixin_class='dev/customtacz/compat/mixin/FactoryPanelScreenTaCZMixin.class'
    if mixin_class in seen:
        sys.exit('Unexpected matching class in upstream PRMA')
    output.write(patch,mixin_class)
with zipfile.ZipFile(args.output) as built:
    failure=built.testzip()
    if failure:
        sys.exit(f'JAR integrity failure: {failure}')
    print(f'Built {args.output} with {len(built.namelist())} entries')
