# Sync `redhat-3.17` with `master` (upstream)

In the **quay-docs** repository, run these commands in order from a shell. If any step fails, stop and report the error.

This matches the workflow where **`redhat-3.17` is reset to match `master`** after `master` is rebased onto `upstream/master`, then all three remotes are updated.

1. Update `master` from `upstream/master`.
2. Point `redhat-3.17` at the same commit as `master`.
3. Force-push to `origin`, `upstream`, and `downstream`.

```bash
git fetch upstream
git checkout master
git rebase upstream/master
git checkout redhat-3.17
git reset --hard master
git push origin redhat-3.17 --force
git push upstream redhat-3.17 --force
git push downstream redhat-3.17 --force
```

**Notes**

- These operations rewrite the remote branch history (`--force`). Only run when that is intentional.
- If `git push downstream` fails (for example DNS or VPN), fix network access and rerun only the failed push.
