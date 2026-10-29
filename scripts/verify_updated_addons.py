#!/usr/bin/env python3
"""Verify recipe outputs against Guns and Targets 1.0.6 and TACZ Turrets 4.1.0.
Usage: python scripts/verify_updated_addons.py <automation-jar> <gunsandtargets-jar> <tacz-turrets-jar>
Offline static validation only. Does not verify Minecraft runtime behavior.
"""
import json, pathlib, sys, zipfile, re
if len(sys.argv)!=4: raise SystemExit(__doc__)
with zipfile.ZipFile(sys.argv[1]) as mod,zipfile.ZipFile(sys.argv[2]) as gat,zipfile.ZipFile(sys.argv[3]) as tur:
  recipes={n:json.loads(mod.read(n)) for n in mod.namelist() if n.startswith('data/prma/recipes/') and n.endswith('.json')}
  gat_indexes=set()
  for path in gat.namelist():
    m=re.fullmatch(r'addon/gunsandtargets/data/gat/index/(guns|attachments)/(.+)\.json',path)
    if m: gat_indexes.add(('GunId' if m.group(1)=='guns' else 'AttachmentId','gat:'+m.group(2)))
  missing=[]
  for name,r in recipes.items():
    if '/gunsandtargets/' in name:
      nbt=r['result'].get('nbt','')
      m=re.search(r'(GunId|AttachmentId):"([^"]+)"',nbt)
      if not m or (m.group(1),m.group(2)) not in gat_indexes:missing.append((name,nbt))
  assert not missing, f'GAT recipe outputs missing from index: {missing}'
  tur_outputs=set(re.findall(rb'tacz_turrets:[a-z0-9_]+',b' '.join(tur.read(x) for x in tur.namelist() if x.startswith('data/tacz_turrets/recipes/') and x.endswith('.json'))))
  for name,r in recipes.items():
    if '/tacz_turrets/' in name and r['result']['item'].startswith('tacz_turrets:'):
      assert r['result']['item'].encode() in tur_outputs,(name,r['result'])
  assert not any('/tacz_turrets/turret.json' in x for x in recipes)
  print(f'Static compatibility check passed: {len(recipes)} recipes, GAT IDs and turret outputs present')
