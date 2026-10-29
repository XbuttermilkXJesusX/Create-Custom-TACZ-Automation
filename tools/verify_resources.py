#!/usr/bin/env python3
"""Check that v1.3.4 source resources match the binary from which extracted."""
from pathlib import Path
import hashlib, json, sys
r=Path(__file__).resolve().parents[1]
manifest=json.loads((r/'manifest.sha256.json').read_text(encoding='utf-8'))['resources']
bad=[]
for p,expected in manifest.items():
    f=r/'src/main/resources'/p
    if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=expected:
        bad.append(p)
print(f'Validated {len(manifest)-len(bad)}/{len(manifest)} resources.')
if bad:
    print('Missing or changed resources:', '\n'.join(bad[:30]))
    sys.exit(1)
