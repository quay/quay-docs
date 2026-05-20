# fix-dita-assembly

Prepare an **assembly and every module it includes** for DITA migration: run AsciiDocDITA Vale checks, fix reported issues, align modules with Red Hat modular-docs templates, then validate IBM Style Guide compliance.

## Invocation

The user supplies an **assembly** path (required), for example:

- `@master.adoc`
- `/home/stevsmit/gg/quay-docs/architecture/master.adoc`

If no path is given, ask which assembly to process.

## Scope: discover all files

1. Read the assembly `.adoc` file.
2. Collect **every file to process**:
   - The assembly itself
   - Each active (non-commented) `include::path.adoc[...]` under the assembly directory (resolve relative paths from the assembly’s directory)
   - Ignore lines whose `include::` is commented out (`//include::`)
3. Process files in this order: **assembly first**, then included modules in **include order** (top to bottom in the assembly).

## Step 1: Run `ditavaleocp` on each file

For each file in scope, run:

```bash
vale --config=/home/stevsmit/vale/.vale.ini --output=line "<path>"
```

(`ditavaleocp` is the shell alias for the same command.)

Record every **error** and **warning** with: file path, line, rule name (e.g. `AsciiDocDITA.ShortDescription`), and message.

## Step 2: Fix Vale issues (per rule)

Use the action for each rule. Primary reference:

- **OSDOCS PDF:** `/home/stevsmit/cqa-cursor/OSDOCS-Content updates in preparation for migrating to DITA-190526-144719.pdf` (use `pdftotext` on this file when you need rule-specific “Action to take” detail)
- **AsciiDocDITA rules:** https://github.com/jhradilek/asciidoctor-dita-vale?tab=readme-ov-file#available-rules

### Rule-specific handlers

| Vale rule | Action |
| --- | --- |
| **AsciiDocDITA.ShortDescription** | Run the **`/write-abstract`** command for that file. If the file is a module, read the parent assembly for context before writing the abstract. Validate abstract text with `python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py` (stdin). Place `[role="_abstract"]` on its own line immediately after the level-1 title, with a blank line before the abstract paragraph. |
| **AsciiDocDITA.CalloutList** | Remove callout markers (`<1>`, `<2>`, …) from code blocks and replace the trailing callout list with prose. Use patterns from https://github.com/openshift/openshift-docs/pull/102276/changes : **unordered list** for multiple distinct callouts, **one lead-in sentence** for a single callout, or **description list** when labels map cleanly to values. Do not leave numbered callout lists. |
| **AsciiDocDITA.AuthorLine** | Add a blank line between the `=` title and the following line (assembly or module). For assemblies, confirm TOC is not broken. |
| **AsciiDocDITA.BlockTitle** | Remove floating block titles (`.Title`) or convert per OSDOCS PDF: lead-in sentence, `==` heading, or leave only on allowed blocks (table, figure, example, code). Image captions like `image:file.png[Caption]` are allowed. |
| **AsciiDocDITA.NestedSection** | Split `===` (and deeper) sections into separate module files, or flatten to `==` only within a single topic per modular-docs guidance. |
| **AsciiDocDITA.AssemblyContents** | Move any prose between/after `include::` directives into a module; assembly may only have title, abstract, includes, and `[role="_additional-resources"]` / `== Additional resources`. |
| **AsciiDocDITA.DocumentId** | Ensure `[id="..."]` immediately precedes the `=` title. |
| **AsciiDocDITA.ContentType** | Set `:_mod-docs-content-type:` to `ASSEMBLY`, `CONCEPT`, `PROCEDURE`, or `REFERENCE` at top of file. |
| **AsciiDocDITA.DiscreteHeading** | Replace `[discrete]` headings with description lists, `==` sections, or a new module. |
| **AsciiDocDITA.LineBreak** | Replace ` +` line breaks with separate paragraphs or table `a` operator as appropriate. |
| **AsciiDocDITA.TaskContents** / **TaskTitle** / **TaskStep** / **TaskDuplicate** | Align procedure modules with `/home/stevsmit/cqa-cursor/TEMPLATE_PROCEDURE_doing-one-procedure.adoc` (`.Procedure` block title, single step list, allowed block titles only). |
| **AsciiDocDITA.AdmonitionTitle** | Remove titles on `[NOTE]`/`[IMPORTANT]`/etc. blocks. |
| **AsciiDocDITA.ConceptLink** | Move in-body xrefs/links to `== Additional resources` where practical. |
| Other rules | Follow OSDOCS PDF “Action to take” for that rule; if guidance is “no action required” or “tiger team”, note it and skip. |

Do **not** change content for rules marked incomplete in the OSDOCS PDF unless the user asks.

## Step 3: Align content type with templates

After Vale fixes, verify each file matches its declared type using these templates:

| Type | Template |
| --- | --- |
| ASSEMBLY | `/home/stevsmit/cqa-cursor/TEMPLATE_ASSEMBLY_a-collection-of-modules.adoc` |
| CONCEPT | `/home/stevsmit/cqa-cursor/TEMPLATE_CONCEPT_concept-explanation.adoc` |
| PROCEDURE | `/home/stevsmit/cqa-cursor/TEMPLATE_PROCEDURE_doing-one-procedure.adoc` |
| REFERENCE | `/home/stevsmit/cqa-cursor/TEMPLATE_REFERENCE_reference-material.adoc` |

Check at minimum:

- Correct `:_mod-docs-content-type:` attribute
- `[id="..."]` before `=` title (modules and assemblies)
- Blank line after `=` title before abstract or body
- `[role="_abstract"]` short description where required
- No forbidden structures for that type (e.g. no `===` in concepts if avoidable; procedures have `.Procedure` and step lists)
- Assembly: only includes + optional Additional resources after modules begin

Fix structural mismatches in the same edit pass.

## Step 4: IBM Style Guide check (required)

After **all** edits to a file, run:

```bash
python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py --no-spell "<path>"
```

Follow **`/check-ibm-sg`** guidance: fix reported issues (anthropomorphism, future tense, passive voice, expletives, self-referential phrasing, OCP structural hits). Re-run until the file is clean or only acceptable false positives remain (document any you skip).

## Step 5: Re-run Vale and report

1. Re-run `ditavaleocp` on each file in scope.
2. Summarize for the user:
   - Files changed (with brief note per file)
   - Remaining Vale errors/warnings that need human review
   - Any rules skipped per OSDOCS “wait for instruction”
3. Do **not** commit unless the user asks.

## Execution notes

- Work through the full assembly in one session when possible; batch independent Vale runs.
- Prefer minimal, correct diffs; do not rewrite unrelated prose.
- Preserve attribute names (`{productname}`, `{ocp}`, etc.) and existing IDs unless a rule requires a change.
- For large assemblies, you may process in batches but must report overall status when done.

## Example workflow

```bash
# List includes (agent parses assembly)
grep -E '^(//)?include::' architecture/master.adoc

# Vale one file
vale --config=/home/stevsmit/vale/.vale.ini --output=line architecture/master.adoc

# IBM SG one file
python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py --no-spell architecture/master.adoc
```
