# Changelog

## 1.3.4 — Guns and Targets 1.0.6 and TACZ Turrets 4.1.0 compatibility

### Guns and Targets 1.0.6
- Checked 1.0.6 against the previously supported 1.0.5.1 JAR: the existing 31 outputs remain available.
- Added 10 Mechanical Crafting recipes: 8 guns (AR-15, C7A2, HK416C, HK MP5SD, MKE MPT55, MKE MPT55A1, MPT55K1A1, MPT55K2A1) and 2 attachments (C7A2 stock, MPT55A1 stock).
- Set output `GunId` for each new gun and included PRMA-compatible TaCZ item NBT.
- Worked around the addon's gun-smith HK416C recipe pointing at HK416D by giving the Create HK416C recipe its intended `gat:hk416c` output.

### TACZ Turrets 4.1.0
- Removed the outdated 3.0.0-era `tacz_turrets:turret` recipe.
- Added 10 turret production recipes, 19 camouflage recipes, and one turret workbench recipe for the new item IDs.
- Mechanical recipes are conditionally loaded with TACZ Turrets installed; Mekanism/Immersive Engineering-dependent recipes are separately conditioned on their mod being present.
- Did not add `*_identical` alternative outputs that share identical ingredients and would cause recipe conflicts.

### Preserved
- All 536 other existing recipe files are unchanged (old obsolete turret recipe replaced, new recipe count 576).
- Original PRMA content, 55 ZeroContact ammo Deploying recipes, TaCZ `GunId` Factory Gauge patch, and Forge update feed remain intact.
- Requires both client and server install. Static validation completed, but Minecraft gameplay testing remains necessary.

## 1.3.3
- Added Forge update-checking metadata, GitHub version feed and optional CurseForge sync automation.

## 1.3.2
- Improved the integrated Extra Gauges `GunId` mechanical recipe selector.

## 1.3.1
- Converted 55 ZeroContact ammo recipes to Deployer-based assembly.

## 1.3.0
- Major version number update with integrated Extra Gauges fix retained.

## 1.2.3
- Integrated the separate Extra Gauges × TaCZ compatibility addon.

## 1.2.2
- Expanded ZeroContact recipes to establish 537 total recipes.
