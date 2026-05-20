# asciidoctor-dita-vale-resolution

Resolve **AsciiDocDITA Vale** errors and warnings on one or more `.adoc` files so content is ready for DITA migration. Use this command on its own or as part of **`/fix-dita-assembly`**.

## Invocation

The user supplies one or more file paths (required), for example:

- `@modules/arch-intro.adoc`
- A directory of `.adoc` files

If no path is given, ask which file(s) to process.

## Step 1: Run `ditavaleocp`

For each file, run:

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
| **AsciiDocDITA.LineBreak** | Replace ` +` hard line breaks with separate paragraphs or the table `a` operator as appropriate. **Also:** when a block title is immediately followed by a lone `+` on the next line (common before example output), remove that `+` line. Example — before: `.Example output:` then `+` on the next line; after: `.Example output:` with no `+` beneath it. |
| **AsciiDocDITA.TaskContents** / **TaskTitle** / **TaskStep** / **TaskDuplicate** | Align procedure modules with `/home/stevsmit/cqa-cursor/TEMPLATE_PROCEDURE_doing-one-procedure.adoc` (`.Procedure` block title, single step list, allowed block titles only). |
| **AsciiDocDITA.AdmonitionTitle** | Remove titles on `[NOTE]`/`[IMPORTANT]`/etc. blocks. |
| **AsciiDocDITA.ConceptLink** | Move in-body xrefs/links to `== Additional resources` where practical. |
| Other rules | Follow OSDOCS PDF “Action to take” for that rule; if guidance is “no action required” or “tiger team”, note it and skip. |

Do **not** change content for rules marked incomplete in the OSDOCS PDF unless the user asks.

## Step 3: Re-run Vale and report

1. Re-run `ditavaleocp` on each file processed.
2. Summarize for the user:
   - Files changed (with brief note per file)
   - Remaining Vale errors/warnings that need human review
   - Any rules skipped per OSDOCS “wait for instruction”
3. Do **not** commit unless the user asks.

## Execution notes

- Prefer minimal, correct diffs; do not rewrite unrelated prose.
- Preserve attribute names (`{productname}`, `{ocp}`, etc.) and existing IDs unless a rule requires a change.
