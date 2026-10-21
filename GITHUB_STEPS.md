# Publishing on GitHub

Run `python tools/prepare_github.py` first, to obtain the original PRMA Java
source and overlay the exact v1.2.2 custom recipes and assets.

Then:

1. On GitHub click **New repository** and name it e.g.
   `Create-Custom-TACZ-Automation`.
2. Open the generated `Create-Custom-TACZ-Automation-Source` folder.
3. Keep `LICENSE`, upstream attribution and README information.
4. From this folder, upload the source files through GitHub's **Add file → Upload files**
   (or use the Git commands below).

```sh
cd Create-Custom-TACZ-Automation-Source
git remote rename origin upstream
git remote add origin https://github.com/YOUR_USERNAME/Create-Custom-TACZ-Automation.git
git add -A
git commit -m "Customize PRMA as Create: Custom TACZ Automation v1.2.2"
git push -u origin HEAD:main
```

If your new repository already has commits, coordinate the branch before pushing.
For easier attribution, consider forking the original PRMA repository instead
of creating a new one.

**Note:** `git push` may request GitHub authentication. Replace `YOUR_USERNAME`.

Before publishing a release or binary, confirm that your Java 17 Forge build
works, that it doesn't conflict with an existing `prma` JAR, and that all
third-party artwork licensing is correctly attributed.
