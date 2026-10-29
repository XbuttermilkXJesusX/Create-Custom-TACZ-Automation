# Create: Custom TACZ Automation

**Automate modern weapons, ammunition, turrets, and attachments with Create for Minecraft Forge 1.20.1.**

> **Version 1.3.4** · Forge 47.x · Create 6.0.8+ · TaCZ 1.1.8-hotfix2+

Custom TACZ Automation expands **Create: Precise Manufacturing (PRMA)** with factory-friendly processing and Mechanical Crafting recipes. The internal mod ID remains `prma` so existing worlds and integrations retain compatibility. **This replaces the original PRMA JAR; never install both.**

## Downloads and project links

- **CurseForge:** https://www.curseforge.com/minecraft/mc-mods/create-custom-tacz-automation
- **Modrinth:** https://modrinth.com/mod/create-custom-tacz-automation
- **GitHub:** https://github.com/XbuttermilkXJesusX/Create-Custom-TACZ-Automation

## What's new in v1.3.4

- Validated against **Guns and Targets 1.0.6**. All 31 previously supported outputs are still present, and 10 new Create recipes cover eight new guns and two attachments.
- The HK416C has its own actual `gat:hk416c` index. The Guns and Targets **native** HK416C gun-smith recipe currently returns HK416D; our new Create recipe deliberately outputs the correct HK416C `GunId` instead.
- Updated for **TACZ Turrets 4.1.0**. Removed the obsolete `tacz_turrets:turret` recipe from 3.0.0 and added **30** mechanical recipes: 10 turret types, 19 camouflage items, and the turret workbench.
- Kept PRMA processing and all existing recipes for TaCZ, ZeroContact, and other addons. The Extra Gauges `GunId` selection Mixin is unchanged from v1.3.3.
- Preserved Forge update notifications linked to the GitHub-hosted `update.json` feed.

## Features

- **Mechanical Crafting:** Build automated production of TaCZ guns, accessories, and the expanded Guns and Targets items.
- **PRMA manufacturing:** Includes casings, cartridge components, original Sequenced Assembly, and material processing.
- **ZeroContact ammunition:** 55 Deployer recipes using prepared PRMA cartridges; existing ZeroContact equipment recipes remain intact.
- **Turrets and camouflage:** Craft items from TACZ Turrets 4.1.0, including basic/advanced/elite/ultimate, scrap, industrial, brass, modern, tactical, steel, and camouflage variants.
- **Create: Extra Gauges:** Built-in TaCZ `GunId`-aware recipe selection. Use the original Extra Gauges 2.0.7, not a separate compatibility addon.
- **Update alerts:** Forge checks for a newer published version using the GitHub version feed; players can follow the update link to CurseForge.

## Recipe coverage

| Addon / content | Automation recipes |
| --- | ---: |
| TaCZ core | 165 |
| ZeroContact — gear & earlier conversions | 69 |
| ZeroContact — Deployer ammunition | 55 |
| GucciVuitton | 48 |
| LRADD | 46 |
| Guns and Targets | 41 |
| LRTactical | 20 |
| Turret TaCZ (separate mod) | 8 |
| Hardened Targets | 5 |
| Apocalyptic Arsenal | 4 |
| TACZ Turrets | 30 |
| **New addon recipes** | **491** |
| **Original PRMA processing recipes** | **85** |
| **Total packaged recipes** | **576** |

Recipe types:

| Create recipe type | Count |
| --- | ---: |
| `create:crushing` | 3 |
| `create:cutting` | 31 |
| `create:deploying` | 55 |
| `create:mechanical_crafting` | 436 |
| `create:milling` | 1 |
| `create:mixing` | 5 |
| `create:sequenced_assembly` | 45 |
| **Total** | **576** |

Recipes for optional addons are active only when those addons are installed. The internal `prma` ID and PRMA content have not been renamed or removed.

## Requirements

**Required:** Minecraft 1.20.1, Minecraft Forge 47.x, Create **6.0.8+**, Timeless and Classics Zero (TaCZ) **1.1.8-hotfix2+**, and Create: Arms Race **1.2.0+**.

**Optional for recipe groups:** Guns and Targets **1.0.6+**, TACZ Turrets **4.1.0+**, ZeroContact, and the other listed addons. Original Create: Extra Gauges **2.0.7** enables the built-in Gauge patch.

TACZ Turrets 4.1.0 declares **SmartBrainLib 1.15+** and **GeckoLib 4.8.3+** as dependencies; provide the required libraries if Forge reports them missing. Some turret variants additionally require **Mekanism** or **Immersive Engineering** ingredients. Recipes for these variants are conditionally registered when those mods are present. TACZ Turrets' own config may disable some turret types; follow the addon configuration.

**Note on ingredient costs:** The Create recipes for updated turrets follow the materials in TACZ Turrets' native gun-smith recipes where practical. Iron, copper, and gold blocks can represent nine ingots in recipes requiring more than an 8×8 Mechanical Crafter can hold. Some large patterns require an expanded Mechanical Crafter arrangement.

## Installation

1. Remove the previous Custom TACZ Automation JAR and any original PRMA mod JAR (do not run both).
2. Install **v1.3.4** in both client and server `/mods` folders.
3. Update **Guns and Targets to 1.0.6** and **TACZ Turrets to 4.1.0**, including the latter's required dependencies.
4. Keep Create 6.0.8+, TaCZ, Create: Arms Race, and any other addons you use.
5. Keep the **unmodified** `extra_gauges-2.0.7.jar` if using Factory Gauges; remove any separate Extra Gauges/TaCZ compatibility addon.
6. Restart client and server. Verify the new Guns and Targets weapons and 4.1.0 turret recipes with JEI and a test Mechanical Crafter.

## Known considerations

- The uploaded Guns and Targets 1.0.6 native gun-smith recipe `guns/hk416c.json` points to `gat:hk416d`, even though its index defines `gat:hk416c`. Our Create recipe uses the dedicated gun index instead; the native recipe itself remains unchanged.
- To avoid conflicting outputs, the various TACZ Turrets `*_identical` gun-smith recipes are **not** duplicated as Create recipes. Each supported turret has one distinct automation recipe based on its standard materials.
- The previous 3.0.0 item `tacz_turrets:turret` is not crafted by this version. Existing stored old turrets may need handling by TACZ Turrets itself; this mod does not migrate items.
- This update has passed static JAR/recipe/ID validation; **actual client/server startup and crafting still need in-game testing**. Do not treat static checks as a gameplay guarantee.

## Source and build

This GitHub source package contains **editable recipe JSON, assets, Markdown documentation, update checker files and the readable Java code for the Extra Gauges compatibility Mixin**, plus its prebuilt compiled class. The upstream PRMA implementation is included in compiled form **only in the release JAR**, not as complete editable Java source in this source ZIP.

To reproduce the release from this source package, obtain the original `prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar`, then run:

```bash
python scripts/build_overlay.py --upstream path/to/prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar --output build/libs/Create-Custom-TACZ-Automation-1.3.4.jar
```

To verify item IDs against the two updated mods:

```bash
python scripts/verify_updated_addons.py build/libs/Create-Custom-TACZ-Automation-1.3.4.jar gunsandtargets-1.0.6.jar tacz_turrets-forge-4.1.0-1.20.1.jar
```

**The two third-party addon JARs are not bundled here.** See `COMPATIBILITY_AUDIT.md`, `CHANGELOG.md`, `GITHUB_STEPS.md`, and `UPDATE_CHECK_SETUP.md` for release and update automation instructions.

## Credits

Based on **Create: Precise Manufacturing (PRMA)** by Type-32. Original Create, TaCZ, Guns and Targets, TACZ Turrets and other addons are the work of their respective authors. This project is an independent integration and is not an official release of those addons.
