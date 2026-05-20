# Sync `redhat-3.13` with upstream

In the **quay-docs** repository, run these commands in order from a shell. If any step fails, stop and report the error.

1. Fetch and rebase the release branch onto its upstream tracking branch.
2. Force-push the updated branch to `origin`, `upstream`, and `downstream`.

```bash
git fetch upstream
git checkout redhat-3.13
git rebase upstream/redhat-3.13
git push origin redhat-3.13 --force
git push upstream redhat-3.13 --force
git push downstream redhat-3.13 --force
```

**Notes**

- These operations rewrite the remote branch history (`--force`). Only run when that is intentional.
- If `git push downstream` fails (for example DNS or VPN), fix network access and rerun only the failed push.
