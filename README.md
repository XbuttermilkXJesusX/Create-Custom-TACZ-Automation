# Create: Custom TACZ Automation

**Bring your TaCZ workshop into a Create-powered factory.**

Create: Custom TACZ Automation expands **Create: Precise Manufacturing (PRMA)** with automated crafting recipes for weapons, attachments, ammunition, tactical equipment, and more. Instead of producing everything by hand, you can build production lines using Create's Mechanical Crafters and PRMA's processing machines.

This project is a customized continuation of PRMA's **simplified automation** version. It retains the original PRMA content and adds recipes inspired by Create: Arms Race and other TaCZ-related addons.

> **Current version: 1.3.3** · Minecraft **1.20.1** · **Minecraft Forge 47.x** · Works on **client and dedicated server**
>
> **Important:** The internal mod ID is still `prma` for compatibility. **This replaces the original PRMA mod; do not install both JARs.**


## Version 1.3.3 — CurseForge update notifications

This release enables **Minecraft Forge's built-in update checker** for `prma` (the existing internal mod ID). If a newer version of **Create: Custom TACZ Automation** is announced through the published version feed, Forge can display an update indicator in the Mods menu, show release notes and link players to [the official CurseForge page](https://www.curseforge.com/minecraft/mc-mods/create-custom-tacz-automation). It does **not** download or install updates automatically.

- Version feed URL: [`update.json`](https://raw.githubusercontent.com/XbuttermilkXJesusX/Create-Custom-TACZ-Automation/main/update.json) (must be published at the GitHub repository root on the `main` branch).
- Publishing destination: [CurseForge](https://www.curseforge.com/minecraft/mc-mods/create-custom-tacz-automation) (project ID **1758542**).
- **Optional automatic synchronization:** the included [GitHub Actions workflow](.github/workflows/sync-curseforge-updates.yml) runs hourly and queries the official CurseForge API for released Forge 1.20.1 files. Configure its `CURSEFORGE_API_KEY` repository secret first. Until configured, manually update `update.json` when you publish a new version.
- The initial version feed lists **1.2.2**, the latest file visible on CurseForge as this release package was prepared. This avoids claiming that **1.3.3** is downloadable from CurseForge before you actually publish it. The workflow will promote 1.3.3 once the CurseForge file is released and recognized.
- Player checks need an internet connection to retrieve the GitHub-hosted JSON. Failures should not prevent Minecraft from starting.

See [UPDATE_CHECK_SETUP.md](UPDATE_CHECK_SETUP.md) for the required one-time GitHub setup and manual fallback.

**No recipe or compatibility changes in 1.3.3:** The 537 recipes, including 55 ZeroContact Deployer ammo operations, original PRMA classes and integrated Extra Gauges/TaCZ `GunId` patch are unchanged from 1.3.2.

## Version 1.3.2 — ZeroContact ammo production update

All **55 ZeroContact ammunition variants** now use Create's **Deployer** for the final ammunition assembly instead of large, randomly arranged Mechanical Crafter layouts. Each starts from a PRMA casing or filled cartridge and consumes a caliber-/variant-specific bullet component or modifier. This makes the ZeroContact rounds part of PRMA's normal ammunition-material production chain.

This update preserves the other **66 ZeroContact gear-workbench** automation recipes and the three earlier ZeroContact conversions. It leaves PRMA's 45 original Sequenced Assembly recipes, all items/code, and the integrated Extra Gauges patch unchanged. Read [the complete new ammunition recipe table](docs/ZeroContact-Ammo-Production-v1.3.2.md) and [CSV](docs/ZeroContact-Ammo-Production-v1.3.2.csv).

**Not a replacement for PRMA Sequenced Assembly:** the final ZeroContact-ammo step is Create Deploying, not a new multistep recipe for each variant. This avoids recipe-selection conflicts between variants sharing the same underlying cartridge. ZeroContact's original bulk-workbench material costs were intentionally adapted for PRMA cartridge-and-Deployer production.

## Version 1.3.0

Version **1.3.0** is a release/version update of v1.2.3. **All 537 Create recipes, the original PRMA compiled functionality, and the integrated TaCZ `GunId` Factory Gauge patch are preserved.** It does not add new recipes or change crafting costs.

**Source transparency:** The ZIP linked with this release contains editable recipe/asset sources and the readable Java source for the **Extra Gauges compatibility Mixin**. PRMA's original 64 compiled Java classes are *not* supplied as independent `.java` files in this archive. For a full editable Gradle project, run the upstream source preparation script and verify compilation yourself. The release JAR is reproducible through the overlay builder with a separately obtained PRMA 0.4.4 JAR.

## What changed in v1.3.2

The integrated Extra Gauges compatibility hook now chooses the exact TaCZ gun recipe **before** Extra Gauges runs its item-only lookup. It uses the output `GunId` and configured ingredients and cancels the original search for TaCZ gun requests only. This is intended to fix RPK, SKS and SCAR-H cross-selection. It is not yet verified in a full Minecraft session.

## Features

- **Industrial gun production:** Create Mechanical Crafting recipes for TaCZ weapons, using Arms Race patterns where applicable and plate-and-mechanism style recipes for other supported guns.
- **Attachments and accessories:** Automate compatible sights, grips, magazines, and other gun accessories.
- **Ammunition production:** Keep PRMA's original ammunition-processing recipes, including multi-step **Sequenced Assembly**.
- **Create processing:** Includes PRMA's original cutting, mixing, crushing, and milling recipes, plus its items, assets, and processing functionality.
- **Tactical equipment:** Adds mechanical crafting for targets, turrets, and equipment from supported addons.
- **ZeroContact integration:** Adds 55 Deployer ammunition recipes and 69 Mechanical Crafting recipes for armor, loadouts, equipment, and the earlier ZeroContact conversions when ZeroContact is installed.
- **Factory-friendly recipes:** Designed for Create logistics, automation, and larger Mechanical Crafter setups.
- **Built-in Extra Gauges × TaCZ support (v1.2.3):** Adds `GunId`-aware mechanical recipe selection when the original Create: Extra Gauges 2.0.7 is installed; the standalone compatibility addon is no longer required.

### What's in v1.3.2?

The packaged v1.3.2 JAR contains **537 Create recipe JSON files**:

| Recipe type | Count |
| --- | ---: |
| Mechanical Crafting | 397 |
| Deploying (ZeroContact ammunition) | 55 |
| Sequenced Assembly | 45 |
| Mechanical Cutting | 31 |
| Mixing | 5 |
| Crushing | 3 |
| Milling | 1 |
| **Total** | **537** |

All 85 original PRMA recipes are retained unchanged. The added ZeroContact integration accounts for **66** of the Mechanical Crafting recipes and **55** Deploying recipes. Not every supported addon supplies recipes, and not every advanced gun modification can be represented as a simple fixed-output Create recipe.

## Supported mods — recipe coverage

**These are the mods that this release actually adds Create automation recipes for.** The numbers below were checked against the recipe files packaged in **v1.3.2** (not estimated from each mod's total item count). Each addon retains its own items: install that mod to craft its items.

| Mod / content source | New Create recipes | Notes |
| --- | ---: | --- |
| **Timeless and Classics Zero (TaCZ)** | **165** | Core TaCZ items, guns and equipment |
| **ZeroContact** | **69** Mechanical Crafting + **55** Deploying | 55 Deployer ammo recipes, 66 remaining gear-workbench recipes, and 3 earlier crafting conversions |
| **GucciVuitton** | **48** | TaCZ addon recipes |
| **LRADD** | **46** | TaCZ addon recipes |
| **Guns and Targets** | **31** | Targets and related crafting |
| **LRTactical** | **20** | Tactical items and equipment |
| **Turret TaCZ** (`turrettacz`) | **8** | Turret-related recipes |
| **Hardened Targets** | **5** | Target recipes |
| **Apocalyptic Arsenal** | **4** | Related addon recipes |
| **TaCZ Turrets** (`tacz_turrets`) | **1** | Turret recipe |
| **Total new automation recipes** | **452** | 397 Mechanical Crafting + 55 Deploying |

In addition to **397 Mechanical Crafting** and **55 ZeroContact Deploying** recipes, the mod retains all **85 original PRMA processing recipes** (45 Sequenced Assembly, 31 Cutting, 5 Mixing, 3 Crushing, and 1 Milling), bringing the total to **537 Create recipes**.

**Create: Arms Race 1.2.0+** is a **required dependency and a source of the gun-crafting style/patterns**; its existing recipes are not counted as a separate addon group above. The TaCZ gun recipes in this mod use Arms Race layouts where applicable.

### Other TaCZ addons reviewed but not converted

**TaCZ Guns Lights Addon**, **TaCZ Tweaks**, **TaCZ Presence**, and **TaCZ Addon** have **no converted Create recipes in this release**. In particular, the two TaCZ Addon gun-upgrade operations that modify an existing weapon were left out because a fixed-output crafting recipe could lose the original gun's data. Their absence from the table does **not** mean the mods are incompatible with Minecraft or TaCZ.

> **Dependency note:** Only the three mods in the Required section below are mandatory for the automation mod itself. For optional addons in this table, install the matching mod to use its corresponding recipes. Some combinations still need in-game verification.

## Requirements

### Required

| Dependency | Minimum version |
| --- | --- |
| Minecraft | 1.20.1 |
| Forge | 47.x |
| [Create](https://modrinth.com/mod/create) | **6.0.8+**, compatible with Minecraft 1.20.1 |
| Create: Arms Race | **1.2.0+** |
| [Timeless and Classics Zero (TaCZ)](https://modrinth.com/mod/timeless-and-classics-zero) | **1.1.8-hotfix2+** |

### Optional integrations

**Create: Extra Gauges 2.0.7** optionally enables the built-in TaCZ Factory Gauge compatibility patch. **Do not install the standalone Extra Gauges × TaCZ compatibility addon at the same time.**

**ZeroContact** enables its 124 addon recipes (69 Mechanical Crafting, 55 Deploying); the other optional supported packs are listed in the **Supported mods — recipe coverage** table above. Their recipes reference items provided by those addons, so install whichever packs you want to automate. Check compatibility with Minecraft 1.20.1; do not treat the recipe table as a mandatory dependency list.

> Minimum versions are based on the Forge dependency metadata included in v1.3.2. A higher version still needs to be compatible with Minecraft 1.20.1 and the rest of your modpack.

## Installation

1. Install Minecraft **1.20.1 Forge** and the three required mods above.
2. Download the latest **Create: Custom TACZ Automation** release JAR.
3. Remove the original **PRMA / Create: Precise Manufacturing** JAR, if installed. Both mods use the same `prma` ID.
4. Place this mod's JAR in the `mods` folder **on both the client and the server**.
5. For NBT-aware Factory Gauge recipe selection, install the **unmodified Create: Extra Gauges 2.0.7 JAR** and remove any standalone Extra Gauges × TaCZ compatibility addon.
6. Add any optional TaCZ addons whose recipes you want to use.
7. Start Minecraft and the server, then look up recipes in your recipe viewer or test them in a Mechanical Crafter.

**Updating:** Replace the previous Custom TACZ Automation JAR; do not leave multiple versions installed. Back up your world before updating a large modpack.

## How to use it

Build a Create processing line, supply the listed ingredients, and route its output into your factory's storage. Different products use different Create machines:

- **Mechanical Crafters** for guns, attachments, and equipment (some patterns are larger than 3×3).
- **Sequenced Assembly** for PRMA's multi-stage ammunition manufacturing.
- **Deployers** for the 55 ZeroContact ammunition finishing recipes (PRMA-prepared cartridges plus a variant-specific component).
- **Mixers, Mechanical Saws, Crushing Wheels, and Millstones** for PRMA materials and intermediate processing.

TaCZ gun variants share the item `tacz:modern_kinetic_gun`. With **original Extra Gauges 2.0.7**, the included optional client-side compatibility Mixin makes Factory Gauge mechanical recipe selection distinguish `GunId` values. This is the proven standalone v1.0.3 compatibility code merged into the automation JAR, without altering the Extra Gauges JAR. In-game testing of the merged packaging is still pending; Stock Link internals are not modified.

## Building from source

This repository's downloadable **source overlay** contains the editable recipes, textures, models, language files, Forge metadata, and setup scripts for v1.3.2. **It is not a standalone Java source project by itself.** The Java implementation originally comes from [Create: Precise Manufacturing](https://github.com/CTRL-Neo-Studios/PreciseManufacturing) (PRMA), by Type-32 / CTRL-Neo-Studios.

There are two build workflows. Choose the one that fits your goal.

### Option A — Build the complete project with Gradle (development)

**Prerequisites:** Java **17 JDK**, Python **3.9+**, Git, and internet access to download Gradle dependencies.

1. Download/extract the v1.3.2 GitHub source overlay ZIP.
2. Open a terminal in that extracted folder.
3. Run:

   ```bash
   python tools/prepare_github.py
   ```

   The script clones the original PRMA Java source (branch `1.20.1-simple-create0.6`), applies this mod's resources and `mods.toml`, and creates `Create-Custom-TACZ-Automation-Source/`.

4. Enter the generated source folder:

   ```bash
   cd Create-Custom-TACZ-Automation-Source
   ```

5. Build with the included Gradle wrapper:

   **Windows (PowerShell / Command Prompt)**
   ```bat
   gradlew.bat build
   ```

   **Linux / macOS**
   ```bash
   ./gradlew build
   ```

6. If successful, the resulting JAR will be in `build/libs/`.

> **Build status:** This is the source-development route, but **a clean Gradle compilation of v1.3.2 has not been verified**. The available PRMA source branch may differ from the exact PRMA 0.4.4 binary used for the released mod, and Create/TaCZ development dependencies may require adjustment. Do not assume that a newly compiled JAR is identical to the distributed release until it has been tested.

### Option B — Repackage recipes with the existing PRMA JAR (no Java compilation)

This is useful if you only want to edit recipes, assets, or Forge metadata while keeping PRMA's compiled Java code unchanged.

**Prerequisites:** Python **3.9+** and a local copy of the original `prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar`.

From the extracted source overlay folder, run:

```bash
python scripts/build_overlay.py --upstream "path/to/prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar"
```

The script combines the original PRMA compiled classes with this repository's resources and the prebuilt Extra Gauges compatibility Mixin. The matching editable Java source is included in `compatibility/src/main/java/`. It writes:

```text
build/libs/Create-Custom-TACZ-Automation-1.3.2.jar
```

**This is a binary/resource overlay, not a Java compilation.** It does not let you change PRMA's Java behavior. To change the compatibility Mixin itself, edit its Java source and compile with the full Minecraft/Forge/Create toolchain, then replace its prebuilt class. You must supply the upstream JAR yourself; do not commit someone else's binary to this repository without checking permission.

### Editing or adding recipes

The main recipe folder is:

```text
src/main/resources/data/prma/recipes/
```

Useful locations include:

```text
src/main/resources/
├── META-INF/mods.toml             # Mod name, version, dependency ranges
├── assets/prma/                   # Textures, models, translations
├── data/prma/recipes/             # Create processing and crafting recipes
├── data/prma/recipes/automation/  # Addon automation recipes
└── prma.png                       # Mod icon
```

After changing recipe JSON, use either build workflow above. For an unchanged overlay, you can check the packaged resources against its manifest with:

```bash
python tools/verify_resources.py
```

This checksum check **will report differences after intentional edits**. It is not a JSON validity checker or a Minecraft gameplay test.

## Repository and release notes

- `README.md` — project overview, installation, build instructions.
- `src/main/resources/` — editable data and asset overlay.
- `tools/prepare_github.py` — prepares a Gradle project using upstream PRMA source.
- `scripts/build_overlay.py` — packages the resource overlay with a local PRMA JAR.
- `docs/` — current ZeroContact ammunition recipe guide and CSV; also includes the historical v1.2.2 catalog.
- `manifest.sha256.json` — reference hashes for the unmodified source overlay.

**v1.3.0:** Version update with the same recipes and integrated compatibility patch as v1.2.3; no crafting balance changes. **v1.2.3:** Integrates the working Extra Gauges × TaCZ compatibility Mixin directly into the automation mod. **v1.2.2:** Adds 121 ZeroContact equipment recipes on top of the previous TaCZ/Arms Race-style automation and PRMA processing. See the ZeroContact recipe catalog in `docs/` for patterns, ingredients, and item IDs.

## Known limitations

- Large Mechanical Crafting layouts are limited by Create's recipe dimensions (maximum 9×9 for the included recipes).
- Some original high-cost recipes were adapted to fit Create's grid; consult the corresponding recipe documentation rather than assuming all ingredient totals match their source crafting station.
- Fixed-output Create recipes cannot faithfully reproduce every gun-upgrade operation that modifies an existing weapon's NBT.
- Runtime gameplay and all client/server combinations have **not been exhaustively tested**. Report the recipe ID, mod versions, logs, and screenshots when something fails.

## Credits and licensing

**Based on [Create: Precise Manufacturing](https://github.com/CTRL-Neo-Studios/PreciseManufacturing)** by **Type-32 / CTRL-Neo-Studios**. This project retains PRMA code, assets, and the internal `prma` mod ID. The upstream project publishes an **MIT** license for its software; preserve its original credits and license notices.

PRMA also attributes some bullet/cartridge textures to **Timeless and Classics Zero**, with **CC BY-NC-SA 4.0** licensing. **Those assets may have different redistribution requirements from the code.** Check the original notices and rights for any third-party content before distributing a public source repository or release JAR.

This is a community customization and is **not an official TaCZ or Create release**.


### Embedded Extra Gauges compatibility (introduced in v1.2.3)

Version 1.3.2 continues to include the same GunId-aware Factory Gauge Mixin as the standalone compatibility addon v1.0.3. It is **not** a modified Extra Gauges JAR. Install original `extra_gauges-2.0.7.jar` to use its features, and **remove the separate `create-extra-gauges-tacz-compat-*.jar`** to avoid loading the Mixin twice. The internal mod ID remains `prma`; no second mod ID is registered by the embedded patch. The patch is client-side and has no direct effect on dedicated servers.

The ZIP contains `compatibility/src/main/java` (readable source) and `compatibility/prebuilt` (the bytecode used for a deterministic no-compile overlay build). The Gradle workflow has not yet been tested with this additional Mixin.
