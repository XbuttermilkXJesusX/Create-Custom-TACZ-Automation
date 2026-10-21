# ZeroContact Ammunition — v1.3.1

55 ZeroContact ammunition recipes now use **Create Deploying**, replacing the mechanically crafted bulk-ingot layouts.

## Processing flow

1. Use PRMA's existing cutting/casing, gunpowder and cartridge processing recipes to produce the cartridge or shell listed for each round.
2. Run that cartridge/shell along a Create belt. Place the listed bullet/component material in a Deployer.
3. The Deployer produces **one ZeroContact ammunition item**.

**Important:** These are **Deploying** recipes, not 55 additional Sequenced Assembly recipes. This avoids ambiguous sequenced-assembly selection when multiple ZeroContact ammunition variants share an identical PRMA cartridge. It still uses the normal PRMA ammunition supply chain. The component requirements have been redesigned, rather than preserving the full metal-ingot costs from ZeroContact workbench crafting.

Requirements: PRMA's original cartridge production, Create, and the ZeroContact addon. ZeroContact recipes only load when the addon is installed.

## Recipes

| Output | Input 1 | Input 2 |
|---|---|---|
| `zerocontact:12g_ap` | `prma:shotgun_shell_base` | `prma:medium_iron_head` |
| `zerocontact:12g_db` | `prma:shotgun_shell_base` | `prma:shotgun_shell` |
| `zerocontact:12g_flechette` | `prma:shotgun_shell_base` | `prma:small_iron_head` |
| `zerocontact:308_m62` | `prma:long_iron_high_gunpowder_cartridge` | `minecraft:glowstone_dust` |
| `zerocontact:308_m80` | `prma:long_iron_high_gunpowder_cartridge` | `prma:308_head` |
| `zerocontact:308_m80a1` | `prma:long_iron_high_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:308_m993` | `prma:long_iron_high_gunpowder_cartridge` | `prma:medium_iron_head` |
| `zerocontact:308_sp` | `prma:long_iron_high_gunpowder_cartridge` | `prma:small_copper_head` |
| `zerocontact:308_un` | `prma:long_iron_high_gunpowder_cartridge` | `prma:small_brass_head` |
| `zerocontact:338_ap` | `prma:long_brass_high_gunpowder_cartridge` | `prma:medium_iron_head` |
| `zerocontact:338_fmj` | `prma:long_brass_high_gunpowder_cartridge` | `prma:338_head` |
| `zerocontact:338_tacx` | `prma:long_brass_high_gunpowder_cartridge` | `prma:small_copper_head` |
| `zerocontact:338_ucw` | `prma:long_brass_high_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:40mm_incendiary` | `prma:40mm_casing` | `minecraft:blaze_powder` |
| `zerocontact:40mm_smoke` | `prma:40mm_casing` | `minecraft:gunpowder` |
| `zerocontact:45acp_ap` | `prma:small_brass_medium_gunpowder_cartridge` | `prma:medium_iron_head` |
| `zerocontact:45acp_fmj` | `prma:small_brass_medium_gunpowder_cartridge` | `prma:45acp_head` |
| `zerocontact:45acp_hs` | `prma:small_brass_medium_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:45acp_rip` | `prma:small_brass_medium_gunpowder_cartridge` | `prma:small_copper_head` |
| `zerocontact:50bmg_api_t` | `prma:long_iron_high_gunpowder_cartridge` | `prma:long_iron_head` |
| `zerocontact:545x39bp` | `prma:medium_copper_medium_gunpowder_cartridge` | `prma:medium_iron_head` |
| `zerocontact:545x39bs` | `prma:medium_copper_medium_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:545x39bt` | `prma:medium_copper_medium_gunpowder_cartridge` | `minecraft:glowstone_dust` |
| `zerocontact:545x39pp` | `prma:medium_copper_medium_gunpowder_cartridge` | `prma:small_copper_head` |
| `zerocontact:545x39ps` | `prma:medium_copper_medium_gunpowder_cartridge` | `prma:small_brass_head` |
| `zerocontact:545x39t` | `prma:medium_copper_medium_gunpowder_cartridge` | `minecraft:redstone` |
| `zerocontact:556x45ap` | `prma:medium_brass_medium_gunpowder_cartridge` | `prma:medium_iron_head` |
| `zerocontact:556x45hp` | `prma:medium_brass_medium_gunpowder_cartridge` | `prma:small_copper_head` |
| `zerocontact:556x45m855` | `prma:medium_brass_medium_gunpowder_cartridge` | `prma:556x45_head` |
| `zerocontact:556x45m855a1` | `prma:medium_brass_medium_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:556x45m856` | `prma:medium_brass_medium_gunpowder_cartridge` | `minecraft:glowstone_dust` |
| `zerocontact:556x45m856a1` | `prma:medium_brass_medium_gunpowder_cartridge` | `minecraft:redstone` |
| `zerocontact:556x45m995` | `prma:medium_brass_medium_gunpowder_cartridge` | `prma:long_iron_head` |
| `zerocontact:57x28l191` | `prma:medium_brass_low_gunpowder_cartridge` | `minecraft:glowstone_dust` |
| `zerocontact:57x28sb193` | `prma:medium_brass_low_gunpowder_cartridge` | `prma:57x28_head` |
| `zerocontact:57x28ss190` | `prma:medium_brass_low_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:58x42dbp191` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:medium_iron_head` |
| `zerocontact:58x42dbx95` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:58x42_head` |
| `zerocontact:58x42dvc12` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:762x39ap` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:long_iron_head` |
| `zerocontact:762x39bp` | `prma:medium_iron_medium_gunpowder_cartridge` | `minecraft:iron_nugget` |
| `zerocontact:762x39hp` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:small_copper_head` |
| `zerocontact:762x39pp` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:762x39_head` |
| `zerocontact:762x39ps` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:small_brass_head` |
| `zerocontact:762x39sp` | `prma:medium_iron_medium_gunpowder_cartridge` | `prma:medium_copper_head` |
| `zerocontact:762x54bt` | `prma:medium_iron_high_gunpowder_cartridge` | `minecraft:glowstone_dust` |
| `zerocontact:762x54fmj` | `prma:medium_iron_high_gunpowder_cartridge` | `prma:762x54_head` |
| `zerocontact:762x54hp` | `prma:medium_iron_high_gunpowder_cartridge` | `prma:small_copper_head` |
| `zerocontact:762x54lps` | `prma:medium_iron_high_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:762x54snb` | `prma:medium_iron_high_gunpowder_cartridge` | `prma:small_brass_head` |
| `zerocontact:9x19ap` | `prma:small_brass_low_gunpowder_cartridge` | `prma:medium_iron_head` |
| `zerocontact:9x19luger_cci` | `prma:small_brass_low_gunpowder_cartridge` | `prma:9mm_head` |
| `zerocontact:9x19pbp` | `prma:small_brass_low_gunpowder_cartridge` | `prma:small_iron_head` |
| `zerocontact:9x19pst` | `prma:small_brass_low_gunpowder_cartridge` | `minecraft:glowstone_dust` |
| `zerocontact:9x19rip` | `prma:small_brass_low_gunpowder_cartridge` | `prma:small_copper_head` |
