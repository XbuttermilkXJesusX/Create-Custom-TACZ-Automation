# Enable update notifications — Create: Custom TACZ Automation v1.3.4

The mod now points Forge's built-in update checker at this public URL:

`https://raw.githubusercontent.com/XbuttermilkXJesusX/Create-Custom-TACZ-Automation/main/update.json`

Forge reads that JSON file when checking updates, compares its `1.20.1-latest` and `1.20.1-recommended` entries against the installed `prma` version, and sends outdated users to the CurseForge project page. The notification appears through Forge's Mods screen; it does **not** auto-download files.

## Required once: Publish the feed

1. Upload the contents of the v1.3.4 source ZIP (including hidden `.github` directory) to the GitHub repository **https://github.com/XbuttermilkXJesusX/Create-Custom-TACZ-Automation**, on its **main** branch.
2. Verify that `https://raw.githubusercontent.com/XbuttermilkXJesusX/Create-Custom-TACZ-Automation/main/update.json` opens and displays JSON (not a 404 page).
3. Upload `Create-Custom-TACZ-Automation-1.3.4-Updated-Addons-Forge-1.20.1.jar` as a new **Forge / 1.20.1** file on **https://www.curseforge.com/minecraft/mc-mods/create-custom-tacz-automation**.

The initial JSON has version `1.2.2` as the latest CurseForge file **observed when this package was made**. That is deliberate: do not advertise unreleased builds. After v1.3.4 is published, update the feed using either automatic or manual steps below.

## Option A: Automatic CurseForge release synchronization (recommended)

1. Obtain a CurseForge Core API key through the official CurseForge API access process. Keep it private; don't commit it to the repository.
2. In GitHub open **Settings → Secrets and variables → Actions → New repository secret**. Set its name to `CURSEFORGE_API_KEY` and value to your key.
3. Under **Settings → Actions → General**, permit GitHub Actions to have **Read and write permissions** for the repository `GITHUB_TOKEN`, if this isn't already enabled. The workflow explicitly asks for `contents: write`.
4. Open the **Actions** tab, enable workflows if prompted, and run **Update Forge version notices from CurseForge → Run workflow** once. The workflow otherwise checks once per hour (GitHub may delay scheduled runs).
5. Check the newest Actions run and open `update.json` on `main`. It should now list the latest published version in `promos`.

The workflow runs `python scripts/sync_curseforge_updates.py`, using CurseForge project ID **1758542** and 1.20.1 filter. It only considers available matching Forge releases; it updates the feed when CurseForge reports a newer published file. It leaves `update.json` unchanged if the API is unavailable or your secret is not set.

Note: An API key is **only used in GitHub Actions**, never placed inside the Minecraft JAR or public update JSON.

## Option B: Manual updates without an API key

After each new release becomes publicly downloadable on CurseForge:

1. Edit the repository-root `update.json` in GitHub.
2. Under `"1.20.1"`, add an entry for the exact new mod version, e.g. `"1.3.4": "Your short changelog"`.
3. Change both `"1.20.1-latest"` and `"1.20.1-recommended"` to the new stable release version (for beta, you may change only `latest`).
4. Commit the JSON file on the `main` branch. No new mod JAR is required just to change the update notice.

```json
{
  "homepage": "https://www.curseforge.com/minecraft/mc-mods/create-custom-tacz-automation",
  "1.20.1": {
    "1.3.4": "Compatibility with Guns and Targets 1.0.6 and TACZ Turrets 4.1.0",
    "1.3.4": "New features and fixes"
  },
  "promos": {
    "1.20.1-latest": "1.3.4",
    "1.20.1-recommended": "1.3.4"
  }
}
```

The JSON above is an **example for a future 1.3.4 release**, not a claim that 1.3.4 already exists.

## Testing

- Start Forge 1.20.1 with v1.3.4 after you publish the JSON; check Minecraft's **Mods** menu.
- Before a newer CurseForge release exists, **you should not get an outdated warning** for 1.3.4.
- When a newer version is released and its version number appears in `update.json`, Forge should show an update indicator and link to the CurseForge project.
- You can run `python scripts/sync_curseforge_updates.py --fixture some-api-response.json --output /tmp/test-feed.json` for offline tests without an API key.

**Important:** Installing the v1.3.4 JAR alone does not create the public JSON file or enable your repository's GitHub Actions. Complete the GitHub setup above to make notifications function.
