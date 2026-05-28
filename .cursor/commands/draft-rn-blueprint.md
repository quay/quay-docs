# Draft release notes blueprint for the next y-stream

Rotate Red Hat Quay release notes on the **current branch** for the **next y-stream** (for example, 3.17 → 3.18). Follow the same pattern as [PR #1464](https://github.com/quay/quay-docs/pull/1464) (3.16 blueprint) and [PR #1558](https://github.com/quay/quay-docs/pull/1558) (3.17 release notes).

## Inputs

Ask the user for the target version if it is not obvious from context:

- **New y-stream:** `NEW` (example: `3.18`)
- **Previous y-stream:** `OLD` (example: `3.17`)
- **New z-stream initial:** `NEW_Z` (example: `3.18.0` / `v3.18.0`)

Derive module suffixes: `318` from `3.18`, `317` from `3.17`.

## 1. Update version attributes

Edit **both** attribute files (they must stay in sync):

- `_attributes/attributes.adoc`
- `release_notes/_attributes/attributes.adoc`

In each `ifeval` block (Project Quay and Red Hat Quay):

| Attribute | New value |
|-----------|-----------|
| `:producty:` | `NEW` |
| `:producty-n1:` | `OLD` (downstream block only) |
| `:productmin:` | `NEW_Z` without `v` (downstream) |
| `:productminv:` | `v` + `NEW_Z` |

## 2. Update `release_notes/master.adoc`

- **Remove** all `include::` lines for the previous y-stream z-stream RNs (`rn-OLD-*`, for example `rn-3-17-0.adoc`, `rn-3-17-1.adoc`).
- **Replace** previous y-stream detail module includes (`*-OLDsuffix`, for example `*-317`) with new `*-NEWSUFFIX` modules.
- **Keep** only one initial y-stream RN: `include::modules/rn-NEW-0.adoc[leveloffset=+2]` (stub until errata is published).
- Preserve commented optional includes if they existed for the previous release (`new-features-and-enhancements-quay-ocp`, `notable-technical-changes`, `deprecations`).

Example assembly tail for 3.18:

```asciidoc
include::modules/rn_overview.adoc[leveloffset=+1]
include::modules/rn-3-18-0.adoc[leveloffset=+2]
include::modules/new-features-and-enhancements-318.adoc[leveloffset=+3]
//include::modules/new-features-and-enhancements-quay-ocp-318.adoc[leveloffset=+3]
include::modules/new-quay-config-fields-318.adoc[leveloffset=+3]
include::modules/new-api-endpoints-318.adoc[leveloffset=+3]
//include::modules/notable-technical-changes-318.adoc[leveloffset=+3]
//include::modules/deprecations-318.adoc[leveloffset=+3]
include::modules/known-issues-and-limitations-318.adoc[leveloffset=+3]
include::modules/bug-fixes-318.adoc[leveloffset=+3]
include::modules/quay-feature-tracker.adoc[leveloffset=+3]
```

## 3. Delete previous y-stream release note modules

Delete from `modules/` (do not leave orphaned files):

- `rn-OLD-0.adoc`, `rn-OLD-1.adoc`, … (all z-stream RN modules for the retired y-stream)
- `bug-fixes-OLDSUFFIX.adoc`
- `known-issues-and-limitations-OLDSUFFIX.adoc`
- `new-features-and-enhancements-OLDSUFFIX.adoc`
- `new-features-and-enhancements-quay-ocp-OLDSUFFIX.adoc`
- `new-quay-config-fields-OLDSUFFIX.adoc`
- `new-api-endpoints-OLDSUFFIX.adoc`
- `notable-technical-changes-OLDSUFFIX.adoc`
- `deprecations-OLDSUFFIX.adoc`

## 4. Create new y-stream blueprint modules

Create stub modules under `modules/` with updated `[id]` and version text. Use these templates:

**`rn_overview.adoc`** — set `[id="release-notes-NEWSUFFIX"]`.

**`rn-NEW-0.adoc`** — errata stub (`RHBA-TBD`, issued TBD, link to errata TBD).

**`bug-fixes-NEWSUFFIX.adoc`** — one placeholder bullet: `PROJQUAY-[*PROJQUAY-*]. Previously,`

**`known-issues-and-limitations-NEWSUFFIX.adoc`** — `== Example` empty section.

**`new-features-and-enhancements-NEWSUFFIX.adoc`** — title + “The following updates have been made to {productname}.”

**`new-quay-config-fields-NEWSUFFIX.adoc`**, **`new-api-endpoints-NEWSUFFIX.adoc`** — title + one-line intro for NEW.

**`new-features-and-enhancements-quay-ocp-NEWSUFFIX.adoc`** — `== Example one` stub.

**`notable-technical-changes-NEWSUFFIX.adoc`**, **`deprecations-NEWSUFFIX.adoc`** — minimal stubs (often commented out in `master.adoc` until filled in).

## 5. Update upgrade documentation

**`modules/accessing-images.adoc`**

- Add a new top section `[id="upgrade-to-producty-from-OLD_underscore_z"]` for upgrade from previous y-stream (example `3_17_z`).
- Shift existing upgrade sections down one version; **remove** the oldest section (keep three supported prior versions).
- Fix any stray characters at end of file.

**`modules/proc_upgrade_standalone.adoc`**

- Supported paths: drop oldest minor, add previous y-stream → `{productmin}` (example `3.17.z -> {productmin}`).
- Update upgrade doc links to `#upgrade_to_NEW_z_from_OLD_z` pattern and display text.

**`modules/upgrading-red-hat-quay.adoc`**

- Operator channel: `stable-NEW` (example `stable-3.18`).

**`modules/upgrading-quay-operator.adoc`**

- Extend sequential upgrade example chain with previous y-stream step if needed.
- Update N-2/N-3 supported direct paths list to match `proc_upgrade_standalone`.

## 6. Update `modules/quay-feature-tracker.adoc`

- Table header: three latest y-streams (`Quay NEW`, `Quay OLD`, `Quay OLD-1`).
- Shift feature status columns: features that reached GA in OLD move to the OLD column; leave NEW column empty (`-`) for new blueprint rows.

## 7. Verify

Run from repo root:

```bash
# No orphaned OLD suffix modules
ls modules/*OLDSUFFIX* 2>/dev/null && echo "FAIL: old modules remain" || echo "OK"

# master.adoc includes only NEW modules
grep -E '317|3\.17|rn-3-17' release_notes/master.adoc modules/rn_overview.adoc && echo "FAIL" || echo "OK"

# Attributes consistent
diff <(grep -E '^:producty|^:producty-n1|^:productmin' _attributes/attributes.adoc) \
     <(grep -E '^:producty|^:producty-n1|^:productmin' release_notes/_attributes/attributes.adoc) || echo "WARN: attribute files differ"
```

Report a short summary: files deleted, files created, attributes set to NEW/OLD, and any manual follow-ups (fill errata in `rn-NEW-0`, populate feature modules, uncomment optional includes when ready).
