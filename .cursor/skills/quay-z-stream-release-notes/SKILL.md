---
name: quay-z-stream-release-notes
description: Creates Red Hat Quay z-stream release notes from a release-build pull request URL (for example quay-konflux-configs). Creates branch rn-3-y-z, adds AsciiDoc module, updates attributes and master includes, commits and pushes. Use when the user passes a GitHub PR URL for a Quay release-notes build, asks to draft z-stream release notes from konflux, or says to run the Quay RN workflow for a version 3.9+ z-stream.
---

# Quay z-stream release notes from a release PR

Use this workflow when the user supplies **one primary URL**: typically a **GitHub pull request** on `quay/quay-konflux-configs` (or similar) that lists fixed issues and version metadata for a **Red Hat Quay z-stream** (patch) release. **Applies to {productname} 3.9 and later.**

If the PR is private or unreachable, ask the user to paste the PR body (or the **Fixed Issues** table), the target **Quay version** (for example `3.17.2`), **RHSA/RHBA** advisory ID and link, **issue date**, and **Clair** version if it changes.

## Inputs to confirm

1. **Full z-stream version** (for example `3.17.2`) — from the PR title/body or file diff if not obvious.
2. **Advisory**: errata type and ID (`RHSA-YYYY:nnnn` or `RHBA-YYYY:nnnn`), correct **access.redhat.com** link, and **issued date**.
3. **Clair** version (`clairproductminv`) if the PR or build metadata changes it; otherwise keep the value already in `_attributes/attributes.adoc`.

## 1. Git branch

- Base the branch name on **x.y.z** using **hyphens**, matching existing modules (for example `rn-3-17-2` for version 3.17.2). Do **not** use dots in the branch name.
- From the repo default branch (or the branch the user specifies), create and checkout:

```bash
git fetch origin
git checkout origin/main   # or master; use the repo’s default
git checkout -b rn-3-<y>-<z>
```

Replace `<y>-<z>` with the minor and patch as separate segments (for example `17-2` for 3.17.2).

## 2. New release module

- Add `release_notes/modules/rn-3-<y>-<z>.adoc` (for example `rn-3-17-2.adoc`).
- **Structure**: Follow **`release_notes/modules/rn-3-17-1.adoc`** for z-streams (short module: title, issued line, abstract, single **Bug fixes** section). Do **not** keep empty “new features” or “known issues” sections — omit those subsections entirely for a typical z-stream (same as `rn-3-17-1.adoc`).
- **Title line**: Use the real advisory id in the form `= RHSA-2026:0518 - {productname} 3.17.1 release` (match errata type and numbering from the advisory).
- **Abstract**: Same pattern as `rn-3-17-1.adoc`: state the concrete version (for example `3.17.2`), `Clair {clairproductminv}`, and link the correct advisory URL and anchor text.
- **Section anchor**: Use the repository’s established id pattern for z-stream bug fixes, for example `[id="bug-fixes-317-2"]` and `== {productname} 3.17.2 bug fixes` (digits only in the id: **no** dots in `317-2`).
- **Module root id**: `[id="rn-3-17-2"]` matching the filename.

Reference template with placeholders (replace all `y`, `z`, advisory, and dates):

- `_mod-docs-content-type: REFERENCE`
- `[id="rn-3-y-z"]` → actual id `rn-3-<y>-<z>`
- Title, issued date, abstract with real RHSA/RHBA link
- One `==` section for bug fixes only when following the minimal z-stream layout

## 3. Which issues to document (Fixed Issues)

- In the PR body, find the **Fixed Issues** (or similarly named) section.
- **Do not** document **CVE** items: skip rows whose summary, title, or ticket text is CVE-centric (for example contains `CVE-`, “Common Vulnerabilities and Exposures”, or is clearly only a security advisory with no product bug narrative). When in doubt, skip CVE-only rows.
- Document **PROJQUAY-***** (or equivalent product bugs) that remain after excluding CVEs. If the list is huge, prefer the same **curated** set the release notes usually call out (the user or PR may imply only specific bugs; if ambiguous, list non-CVE **PROJQUAY-** tickets from the fixed list and ask whether to trim).

## 4. Jira / Issues and CCFR-style bug write-ups

For **each** bug to document:

1. Open the ticket (for example `https://issues.redhat.com/browse/PROJQUAY-9948` or the **redhat.atlassian.net** URL if that is what the user provides). Use **fetch or browser tools** when available. If the tracker requires login and content is unavailable, ask the user for the **Summary** and **Description** (or paste).
2. Write the release-note bullet in **CCFR-aligned** prose per the Red Hat Supplementary Style Guide (Cause / Condition / Fix / Result). **Match the existing voice and layout in** `release_notes/modules/bug-fixes-317.adoc`:
   - Start with `* link:https://issues.redhat.com/browse/PROJQUAY-nnnn[*PROJQUAY-nnnn*].` (use **issues.redhat.com** for consistency with current release notes unless the repo standard changes).
   - First paragraph: **Previously,** … (condition / customer impact).
   - If the fix needs a second paragraph, use a line break with AsciiDoc continuation `+` on its own line, then **With this release,** / **This release** / **This update** … (fix and result).
3. Do **not** duplicate the same issue twice. Fix link targets: ticket id in the link must match the bold id in the text (avoid mismatches like in stale examples).

If there are **no** non-CVE bugs to document, use a single line: `There were no bug fixes for this release.` (as in `rn-3-17-1.adoc`).

## 5. New features / known issues sections

- For **z-stream** releases, **omit** “new features and enhancements” and “known issues and limitations” subsections from `rn-3-<y>-<z>.adoc` unless the user explicitly provides content for them.
- If the user **does** supply enhancements or known issues, add well-formed `==` sections with appropriate unique `[id="..."]` values; otherwise leave the module as **title + abstract + bug fixes only**.

## 6. Include in the release notes book

- Edit `release_notes/master.adoc`: add `include::modules/rn-3-<y>-<z>.adoc[leveloffset=+2]` **immediately after** `include::modules/rn_overview.adoc[leveloffset=+1]`, **before** older `rn-3-*` includes (newest release first).

## 7. Update `_attributes/attributes.adoc`

For a **z-stream** on the same **y** (for example 3.17.1 → 3.17.2):

- In the `ifeval::["{productname}" == "Red Hat Quay"]` block, set:
  - `:productmin:` to **3.y.z** (no `v` prefix).
  - `:productminv:` to **v3.y.z** (leading `v`).
- Update `:producty:` only if this release starts a **new minor** line (unusual for a pure z-stream workflow).
- In the `Project Quay` / upstream `ifeval` block, update `:producty:` and `:productminv:` to stay consistent with the downstream z-stream you are documenting (this repo already mirrors them in the template).
- Adjust `:clairproductminv:` only if the release PR or metadata requires it.

Do **not** change unrelated attributes.

## 8. Commit message and push

- Stage the new module, `master.adoc`, and `_attributes/attributes.adoc` (and any other intentional edits only).
- Commit with message:

```text
Adds 3.y.z release notes
```

Replace `3.y.z` with the **full version** (for example `Adds 3.17.2 release notes`).

- Push:

```bash
git push -u origin rn-3-<y>-<z>
```

Request **git_write** and **network** permissions when running these commands for the user.

## Quality checks

- No CVE-only bullets in the z-stream bug list unless the user explicitly overrides.
- AsciiDoc ids unique and consistent (`rn-3-*`, `bug-fixes-*`).
- Advisory link and id in the module match the real errata.
- Compare finished bug bullets to `bug-fixes-317.adoc` for formatting parity.

## Example invocation (for the user)

In Cursor chat, say something like: **“Run quay z-stream release notes for https://github.com/quay/quay-konflux-configs/pull/157”** and attach or paste the PR if the repository is private.
