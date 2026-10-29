# Compatibility verification — v1.3.4

Verified using the uploaded binary files:
- `gunsandtargets-1.0.6.jar` compared against `gunsandtargets-1.0.5.1`.
- `tacz_turrets-forge-4.1.0-1.20.1.jar` compared against `tacz_turrets-forge-3.0.0-1.20.1`.
- The previous Custom TACZ Automation v1.3.3 JAR.

## Confirmed from the files

- Guns and Targets 1.0.6: 41 gun-smith recipe entries (31 previously included + 10 new). All 31 previous Custom TACZ Automation GunId/AttachmentId outputs still have a matching GAT index. The new automation version includes all 41 indexed outputs.
- **HK416C bug in external addon:** `addon/gunsandtargets/data/gat/recipes/guns/hk416c.json` has `result.id = "gat:hk416d"`; GAT also defines a separate `gat:hk416c` index. The new Create automation recipe uses `GunId:"gat:hk416c"`.
- TACZ Turrets 4.1.0: The old `tacz_turrets:turret` result has been replaced with a range of turret variants. The new automation version removes that obsolete recipe and adds 30 mechanical recipes for 10 turrets, 19 camos, and a turret workbench.
- Crafting recipes are conditional on the appropriate addon; certain variant recipes additionally require Mekanism or Immersive Engineering.
- All 536 unchanged recipe JSON files match the v1.3.3 JAR byte-for-byte. All original compiled PRMA classes and the Extra Gauges Mixin class are byte-for-byte unchanged.
- The build script reproduces identical file bytes from the included source and original PRMA compiled JAR.
- All 576 JSON recipe files can be parsed and the resulting JAR passes ZIP integrity checks.

## Limits

The offline validation cannot confirm Forge has successfully loaded every recipe, or that Minecraft gameplay, item interactions, Factory Gauges and TaCZ turret behavior work in a world. Test startup on client and server and inspect JEI recipes for added weapons/turrets before publishing as fully verified.

This release does not migrate old TACZ Turrets 3.0.0 inventory items into 4.1.0 items or fix the upstream HK416C smith-table recipe inside Guns and Targets.
