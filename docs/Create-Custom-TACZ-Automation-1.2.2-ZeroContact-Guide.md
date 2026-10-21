# Create: Custom TACZ Automation v1.2.2 — ZeroContact integration

**Minecraft 1.20.1 / Forge / Create 6.0.8+**

Adds **121 Create Mechanical Crafting recipes** from the ZeroContact 1.1.6 built-in gear workbench, on top of the prior **3 standard ZeroContact recipes** already converted in v1.2.1. All former v1.2.1 PRMA classes, textures, models, and recipe files are preserved byte-for-byte.

## New recipes

| ZeroContact content | Count |
|---|---:|
| Ammunition | 55 |
| Armor and protective equipment | 42 |
| Loadout rigs and backpacks | 10 |
| Modules and electronics | 14 |
| **Total new** | **121** |

Every recipe is a Create `mechanical_crafting` layout with a distinct arrangement and a mod-loaded condition. Most costs are identical to the ZeroContact workbench costs; see CSV for each layout and all ingredients.

### Source-data issues handled

- **NVG T7** requires 99 raw ingredients, more than Create's 9×9 maximum. The recipe substitutes **5 iron blocks + 3 iron ingots for 48 iron ingots**, and **8 glowstone blocks for 32 glowstone dust**, which preserves the required resource amounts. Minecraft crafts both blocks using those items.
- The ZeroContact workbench source uses `zerocontact:sop_mr_desert`, but the pack's registered item is `zerocontact:rigs_sop_mr_desert`. The Create output uses the registered ID.
- Where multiple pieces of equipment share identical ingredient quantities, the recipes have distinct crafting shapes rather than arbitrary added costs.

### Dependencies and installation

Keep these mods installed in the same versions as before:
- Create: Arms Race 1.2.0+
- Create 6.0.8+ (Minecraft 1.20.1)
- TaCZ 1.1.8-hotfix2+
- ZeroContact 1.1.6 (optional for loading Custom TACZ Automation, required for these new recipes)

1. Remove `Create-Custom-TACZ-Automation-1.2.1-Dependencies-Forge-1.20.1.jar` from your client and server.
2. Install `Create-Custom-TACZ-Automation-1.2.2-ZeroContact-Forge-1.20.1.jar` on both client and server.
3. Keep the actual ZeroContact JAR installed as well: this is **not** a replacement for ZeroContact.
4. Do not install original PRMA at the same time as Custom TACZ Automation (both use the internal `prma` mod ID).

## Validation

- Confirmed source item definitions and generated outputs for all 121 recipes.
- Validated every Create recipe's JSON, size (max 9×9), referenced ingredients, and shape uniqueness.
- Preserved the original mod files, except the version/dependency metadata.
- Verified JAR integrity and Forge TOML parsing.

**Not tested inside Minecraft:** all generated recipes require client/server testing, especially zero-contact's runtime item registration and the mechanical crafter selection when another mod adds the same layout. Existing Factory Gauge recipe filters may need to be set to the correct new item.

The recipe catalog CSV contains the exact Create input count and pattern for every new piece of equipment.
