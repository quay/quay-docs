# align-content-type-with-template

Verify that `.adoc` modules and assemblies match their declared **modular documentation content type** using Red Hat templates. Use this command on its own or as part of **`/fix-dita-assembly`**.

## Invocation

The user supplies one or more file paths (required), for example:

- `@modules/arch-intro.adoc`
- An assembly and its included modules

If no path is given, ask which file(s) to process.

## Templates

| Type | Template |
| --- | --- |
| ASSEMBLY | `/home/stevsmit/cqa-cursor/TEMPLATE_ASSEMBLY_a-collection-of-modules.adoc` |
| CONCEPT | `/home/stevsmit/cqa-cursor/TEMPLATE_CONCEPT_concept-explanation.adoc` |
| PROCEDURE | `/home/stevsmit/cqa-cursor/TEMPLATE_PROCEDURE_doing-one-procedure.adoc` |
| REFERENCE | `/home/stevsmit/cqa-cursor/TEMPLATE_REFERENCE_reference-material.adoc` |

Read the template that matches each file’s `:_mod-docs-content-type:` value before editing.

## Checks (apply to every file)

- Correct `:_mod-docs-content-type:` attribute
- `[id="..."]` before `=` title (modules and assemblies)
- Blank line after `=` title before abstract or body
- `[role="_abstract"]` short description where required
- No forbidden structures for that type (for example, no `===` in concepts if avoidable; procedures have `.Procedure` and step lists)
- **Assembly only:** after the first `include::`, only more includes and an optional `[role="_additional-resources"]` / `== Additional resources` section

Fix structural mismatches in the same edit pass. Do **not** commit unless the user asks.

## Report

Summarize for the user:

- Files changed (with brief note per file)
- Files that already matched the template
- Structural issues that need human review (for example, nested sections that require new modules)
