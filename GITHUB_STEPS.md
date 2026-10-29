# GitHub publishing — v1.3.4

Extract this ZIP into your existing repository as an update (not a new repository). Review `git diff`, then commit the resources and documentation.

1. Upload/commit the updated `src/main/resources` recipe files and `META-INF/mods.toml`.
2. Commit `README.md`, `CHANGELOG.md`, and scripts, retaining `.github/workflows` and `update.json`.
3. Keep `compatibility/prebuilt/` and its special `.gitignore` exception for the compiled compatibility Mixin.
4. Build using `python scripts/build_overlay.py --upstream /path/to/prma-original.jar`.
5. Run `python scripts/verify_updated_addons.py ...` against Guns and Targets 1.0.6 and TACZ Turrets 4.1.0.
6. Test the generated mod on Forge client and dedicated server before publishing on CurseForge or Modrinth.
7. Publish v1.3.4 on CurseForge and Modrinth, then allow the existing update-feed workflow to discover the new Forge release.

**Source note:** This is an overlay/repack builder using original PRMA binaries. It is not a complete independent Java source tree for PRMA.
