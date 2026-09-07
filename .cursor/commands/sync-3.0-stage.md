# Sync `3.0-stage` from `redhat-3.18` (via `master`)

In the **quay-docs** repository, run these commands in order from a shell. If any step fails, stop and report the error.

This sync is different from `sync-redhat-3.18`: `3.0-stage` is reset to `redhat-3.18`, and `redhat-3.18` is first reset to `master`. After the reset, set `:producty:` to `3` so the publishing toolchain can build successfully.

1. Fetch remotes and rebase local `master` onto `upstream/master`.
2. Reset `redhat-3.18` to match `master`, then force-push it.
3. Reset `3.0-stage` to match `redhat-3.18`.
4. Set `:producty: 3` in both attribute files (both `ifeval` blocks).
5. Commit the attribute change if needed, then force-push `3.0-stage`.

```bash
git fetch upstream
git checkout master
git rebase upstream/master

git checkout redhat-3.18
git reset --hard master
git push origin redhat-3.18 --force
git push upstream redhat-3.18 --force
git push downstream redhat-3.18 --force

git checkout 3.0-stage
git reset --hard redhat-3.18

# Publishing toolchain expects producty=3 on 3.0-stage (not 3.18).
# Update both ifeval blocks in both attribute files.
sed -i 's/^:producty: 3\.18$/:producty: 3/' _attributes/attributes.adoc
sed -i 's/^:producty: 3\.18$/:producty: 3/' release_notes/_attributes/attributes.adoc

git add _attributes/attributes.adoc release_notes/_attributes/attributes.adoc
git diff --cached --quiet || git commit -m "Update producty attr to 3"

git push origin 3.0-stage --force
git push upstream 3.0-stage --force
git push downstream 3.0-stage --force
```

**Notes**

- Chain of truth: `upstream/master` → local `master` → `redhat-3.18` → `3.0-stage`.
- On `3.0-stage` only, `:producty:` must be `3` (see `_attributes/attributes.adoc`). Leave `:producty-n1:`, `:productmin:`, and `:productminv:` unchanged.
- These operations rewrite remote branch history (`--force`). Only run when that is intentional.
- If `git push downstream` fails (for example DNS or VPN), fix network access and rerun only the failed push.
- Confirm working tree is clean before starting (`git status`). Stash or commit local changes first.
- The attribute commit is skipped when `producty` is already `3` (`git diff --cached --quiet`).
