# Provenance

**Original PRMA Java implementation:** 64 compiled Java classes in the upstream mod JAR. No `.java` sources are supplied here. You must obtain PRMA's original source separately for normal Gradle Java builds.

**Custom changes:** Recipe/data assets and Forge metadata in `src/main/resources` are directly editable. All custom automation recipes belong there.

**Build:** `scripts/build_overlay.py` combines your local upstream compiled classes with repository data/assets; it does not decompile, synthesize, or recompile upstream Java.
