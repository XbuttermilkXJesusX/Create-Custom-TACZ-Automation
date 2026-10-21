# Create: Custom TACZ Automation — v1.2.1

Minecraft **1.20.1** · Forge · internal mod ID `prma`

## What this repository contains

This is the **editable recipe, asset and metadata source** extracted from the v1.2.1 mod JAR, plus a script that can repackage the mod using the compiled classes from the original PRMA 0.4.4 JAR.

- `src/main/resources/data/` — Create recipes, tags and other datapack resources.
- `src/main/resources/assets/` — textures, models, language files and other assets.
- `src/main/resources/META-INF/mods.toml` — editable Forge metadata including mod name and dependency requirements.
- `scripts/build_overlay.py` — builds a working replacement JAR using existing original PRMA compiled classes and all resources from this repository.

**Important:** This is **not the original Java source code**. The published mod JAR contains 64 compiled `.class` entries, not `.java` source. These 64 classes are unchanged from the original PRMA JAR. Building directly from Java source requires the upstream PRMA source repository or a separate decompilation/reimplementation effort. Don't label this GitHub project as a full source-code port.

## Build a mod JAR

Install Python 3 and supply the original PRMA JAR locally (it is deliberately not embedded in this repository):

```bash
python scripts/build_overlay.py --upstream "path/to/prma-1.20.1-0.4.4-cr6.0-SIMPLE-beta-all.jar"
```

The output is `build/libs/Create-Custom-TACZ-Automation-1.2.1.jar`. This is an **overlay/repackaging** build, not a Gradle Java compile. Add the result to client and dedicated server; remove the original PRMA JAR, because both use the `prma` mod ID.

## Edit recipes

Modify JSON files under `src/main/resources/data/`, then rerun the command above. Forge metadata lives at `src/main/resources/META-INF/mods.toml`.

## Dependencies

The JAR declares required versions for Create, Create: Arms Race, and TaCZ. Consult `mods.toml` for exact version ranges. Existing PRMA Java behavior remains unchanged.

## Licensing and credits

The JAR's Forge metadata states `MIT` and credits **Type-32** as an author. This repository was reconstructed from compiled artifacts. Confirm the original project's license and any separately licensed third-party textures/assets before publicly redistributing them, and preserve upstream notices and attribution. No claim is made that the upstream Java classes were independently authored here.

## Verification

The included resources were extracted from the current v1.2.1 JAR, while its 64 class files match the original PRMA JAR byte-for-byte. The overlay can be structurally verified, but this does not replace Minecraft client/server gameplay tests.
