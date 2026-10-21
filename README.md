# Create: Custom TACZ Automation — v1.2.2 source overlay

**Minecraft 1.20.1 • Forge 47.x • Create 6.0.8+ • TaCZ 1.1.8-hotfix2+ • Create: Arms Race 1.2.0+**

This archive contains **all editable resource files extracted from the user's exact
v1.2.2 mod JAR** (Create processing and mechanical crafting JSON, models, textures,
translations, mixin configuration, and Forge metadata). It is intended to be
applied **on top of the original PRMA Java source repository**, which is MIT-licensed.

## Important: this ZIP is a source **overlay**, not a complete standalone Java project

The finished v1.2.2 mod was produced by adding and changing resources inside a
**compiled PRMA JAR**. A compiled JAR contains `.class` bytecode rather than the
original editable Java files. To avoid presenting decompiled or invented Java as
the original source, this archive supplies your **exact resource files** and
an automated method of combining them with PRMA's **public original Java source**.

Original upstream project:
https://github.com/CTRL-Neo-Studios/PreciseManufacturing

Recommended branch: `1.20.1-simple-create0.6`.

## Create the GitHub repository (Windows / macOS / Linux)

1. Install Git, Python 3, and Java **17**.
2. Extract this archive somewhere convenient.
3. In a terminal opened inside the extracted folder, run:

   ```shell
   python tools/prepare_github.py
   ```

   This clones the public PRMA source under `Create-Custom-TACZ-Automation-Source/`
   and overlays all v1.2.2 resources. The script updates `gradle.properties` with
   the new display name/version and Create dependency (the documented
   Create 6.0.8-289 development artifact).
4. Open `Create-Custom-TACZ-Automation-Source/` and review the changes.
5. You can now create a **new GitHub repository**, upload the contents of that
   source directory, or push it via Git (see `GITHUB_STEPS.md`).
6. To try building it, from inside the source directory run:
   - Windows: `gradlew.bat build`
   - macOS/Linux: `./gradlew build`

> **Build warning:** Gradle compilation was **not verified** here. The original
> upstream source branch may not exactly correspond to the compiled PRMA 0.4.4
> release used to make the working v1.2.2 JAR. If Gradle reports API version,
> mapping, or library problems, resolve those in the upstream `build.gradle`
> before treating its output as equivalent to v1.2.2. The included JSON/resources
> were verified against the working JAR, not tested in a new compiled build.

## Original code and licensing

PRMA Java classes, Forge project scripts, and build wrapper are published in the
upstream project by Type-32 / CTRL-Neo-Studios. Keep the upstream MIT license,
author credit, and license notices. PRMA's README says some ammo/cartridge
textures are derived from TaCZ with **CC BY-NC-SA 4.0** attribution, which is
separate from the MIT license on the code; review those terms before public
redistribution.

The internal mod ID remains `prma` to preserve existing saves and PRMA items.
Do **not** install the original PRMA JAR alongside this modified version.

## Resource layout

- `src/main/resources/data/prma/recipes/` — actual Create recipes
- `src/main/resources/assets/prma/` — images, models, translations, sounds
- `src/main/resources/META-INF/mods.toml` — v1.2.2 dependency requirements
- `src/main/resources/prma.mixins.json` — PRMA mixin registration
- `tools/prepare_github.py` — download Java source / apply overlay
- `tools/verify_resources.py` — verify overlay checksums
- `manifest.sha256.json` — list of all extracted resource files

**Not included:** compiled Java bytecode, bundled third-party JARs, Gradle caches,
or source files fetched from GitHub. These belong in their respective original
projects or are downloaded by the setup script.

## ZeroContact recipes added in v1.2.2

Added 121 Create Mechanical Crafting recipes based on the original ZeroContact gear-workbench data. These are under `src/main/resources/data/prma/recipes/automation/zerocontact_gear/`. The mod contains conditional `forge:mod_loaded` checks and an optional ZeroContact dependency.

ZeroContact 1.1.6 or later must be installed to craft these items. All previous v1.2.1 recipes and original PRMA code are preserved.

The matching recipe list and notes are in `docs/`. Rebuilding the Java code still requires PRMA's original upstream sources as explained above.
