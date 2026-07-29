# Sync `redhat-3.18` from `master`

In the **quay-docs** repository, run these commands in order from a shell. If any step fails, stop and report the error.

1. Fetch remotes and rebase local `master` onto `upstream/master`.
2. Reset `redhat-3.18` to match `master`.
3. Force-push `redhat-3.18` to `origin`, `upstream`, and `downstream`.

```bash
git fetch upstream
git checkout master
git rebase upstream/master
git checkout redhat-3.18
git reset --hard master
git push origin redhat-3.18 --force
git push upstream redhat-3.18 --force
git push downstream redhat-3.18 --force
```

**Notes**

- Unlike older `sync-redhat-3.x` commands (which rebase onto `upstream/redhat-3.x`), this command **resets** `redhat-3.18` to current `master` after rebasing `master` on `upstream/master`.
- These operations rewrite remote branch history (`--force`). Only run when that is intentional.
- If `git push downstream` fails (for example DNS or VPN), fix network access and rerun only the failed push.
- Confirm working tree is clean before starting (`git status`). Stash or commit local changes first.
