## v1.3.3 — Forge update checker

- Connected Forge `prma` update notifications to the GitHub-hosted version feed and official CurseForge project page.
- Included `update.json`, an opt-in GitHub Action, and a CurseForge API synchronization script.
- Kept all 537 recipes, PRMA code/assets, ZeroContact ammo and GunId Extra Gauges compatibility unchanged.
- Automatic release promotion requires setting the GitHub `CURSEFORGE_API_KEY` secret and enabling the workflow.

## v1.3.2

- Changed TaCZ GunId-aware Extra Gauges compatibility from a post-search correction to a pre-search, cancellable selector for TaCZ guns.
- Preserved all 537 original recipes, PRMA items, textures, and ZeroContact ammunition operations.
- Kept original Extra Gauges 2.0.7 JAR untouched.
- Runtime behavior requires testing; compile and JAR validations are not a Minecraft runtime test.

## v1.3.1 — ZeroContact ammunition overhaul

- Replaced 55 ZeroContact mechanical-crafting ammo patterns with 55 Create Deploying recipes using PRMA prepared casings and cartridges.
- All original PRMA manufacturing recipes, compiled implementation, and Extra Gauges compatibility preserved.
- Other 66 ZeroContact gear recipes and three prior ZeroContact conversions unchanged.
- Added a complete ZeroContact ammo input/output guide and CSV.
- No new items, Java classes, or required dependencies.

# Changelog

## 1.3.0 — Versioned integrated compatibility release

- Updated the Forge mod version from 1.2.3 to **1.3.0**.
- Preserved all 537 Create recipes and the original PRMA functionality.
- Retained the integrated Extra Gauges + TaCZ `GunId` lookup compatibility patch.
- Updated README, overlay build output name, and Gradle-preparation version metadata.
- Fixed `.gitignore` so the required prebuilt compatibility Mixin can be committed when using the overlay build workflow.
- No gameplay recipe balance changes.

## 1.2.3

- Integrated the standalone Extra Gauges/TaCZ compatibility Mixin into the automation mod.

## 1.2.2

- Added 121 ZeroContact workbench automation recipes.
