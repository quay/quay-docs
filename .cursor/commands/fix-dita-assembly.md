# fix-dita-assembly

**Master command:** prepare an **assembly and every module it includes** for DITA migration by running three sub-commands in order, then reporting final Vale status.

## Invocation

The user supplies an **assembly** path (required), for example:

- `@master.adoc`
- `/home/stevsmit/gg/quay-docs/architecture/master.adoc`

If no path is given, ask which assembly to process.

## Scope: discover all files

1. Read the assembly `.adoc` file.
2. Collect **every file to process**:
   - The assembly itself
   - Each active (non-commented) `include::path.adoc[...]` (resolve relative paths from the assembly’s directory)
   - Ignore lines whose `include::` is commented out (`//include::`)
3. Process files in this order: **assembly first**, then included modules in **include order** (top to bottom in the assembly).

Pass the full file list to each sub-command below.

## Workflow (run in order)

### 1. `/asciidoctor-dita-vale-resolution`

Run **`/asciidoctor-dita-vale-resolution`** on every file in scope. That command runs `ditavaleocp`, fixes AsciiDocDITA Vale hits per rule (including `/write-abstract` for `ShortDescription`), and re-runs Vale on each file.

### 2. `/align-content-type-with-template`

Run **`/align-content-type-with-template`** on every file in scope. That command checks structure against the ASSEMBLY, CONCEPT, PROCEDURE, and REFERENCE templates.

### 3. `/check-ibm-sg`

Run **`/check-ibm-sg`** on every file in scope. Follow that command’s guidance: fix reported issues (anthropomorphism, future tense, passive voice, expletives, self-referential phrasing, OCP structural hits). Re-run until each file is clean or only acceptable false positives remain (document any you skip).

## Final step: re-run Vale and report

1. Re-run `ditavaleocp` on each file in scope:

   ```bash
   vale --config=/home/stevsmit/vale/.vale.ini --output=line "<path>"
   ```

2. Summarize for the user:
   - Files changed across all steps (with brief note per file)
   - Remaining Vale errors/warnings that need human review
   - Remaining IBM Style Guide issues (if any)
   - Any rules skipped per OSDOCS “wait for instruction”
3. Do **not** commit unless the user asks.

## Execution notes

- Work through the full assembly in one session when possible; batch independent Vale and IBM checks.
- Prefer minimal, correct diffs; do not rewrite unrelated prose.
- Preserve attribute names (`{productname}`, `{ocp}`, etc.) and existing IDs unless a rule requires a change.
- For large assemblies, you may process in batches but must report overall status when done.

## Example: discover includes

```bash
grep -E '^(//)?include::' architecture/master.adoc
```

## Sub-commands (also usable standalone)

| Command | Purpose |
| --- | --- |
| `/asciidoctor-dita-vale-resolution` | Run Vale and fix AsciiDocDITA rule violations |
| `/align-content-type-with-template` | Align modules with modular-docs templates |
| `/check-ibm-sg` | IBM Style Guide and OCP structural checks |
