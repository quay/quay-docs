# check-ibm-sg

Validate AsciiDoc (and plain text) against a **reference corpus** in `/home/stevsmit/ibm-style-guide/`, using heuristic checks aligned with those guides plus optional spelling.

## Reference sources (all beside `check-ibm-style.py`)

| File | Role |
| --- | --- |
| `ibm-style-documentation.pdf` | IBM Style (full) — corpus load + IBM-aligned prose checks |
| `IBMQuickStyle.pdf` | IBM Style (quick reference) — corpus load |
| `red-hat-supplementary-style-guide.pdf` | Red Hat supplementary style — corpus load + RH-aligned prose checks |
| `ocp-documentation-guidelines.md` | OpenShift docs / modular-docs rules — corpus load + `.adoc` structural checks |

On each run, the script prints **stderr** lines such as `✓ <filename> (N chars)` or `— missing <filename>` so you can confirm every source was read.

**How this relates to “rules”:** The PDFs and Markdown are **read and verified at startup**. The checks themselves are **pattern-based heuristics** (and Hunspell) **aligned with** IBM Style, the supplementary guide, and the OCP guidelines—they do **not** parse every rule on every page of the PDFs.

## What gets checked

**IBM-aligned (prose):**

- **Anthropomorphism**: Inanimate subjects described with human-like agency or “allows you” patterns
- **Future tense**: `will`, `shall`, `going to` (use present tense where appropriate)
- **Passive voice**: Narrow pattern such as `…ed by` / `…ed with`
- **Expletive constructions**: `It is`, `There is`, `There are` (subject hidden)
- **Phrasal verbs**: Suggest one-word alternatives where listed
- **First person**: `I`, `we`, `us`, `our` (use with caution in product docs)
- **Gender-specific pronouns**: Prefer inclusive wording

**Red Hat supplementary–aligned (prose):**

- Self-referential phrasing (e.g. “This topic covers…”, “Use this procedure to…”)
- Feature-focused phrasing (e.g. “This product allows you to…”)

**OpenShift guidelines–aligned (`.adoc` only):**

- Heading titled **Overview**
- **Optional:** prefix on assembly/module titles
- **`===` or deeper** headings (H3+)
- **Backticks** in `=` / assembly or module titles

**Spelling (optional):**

- **Hunspell** (`en_US`) on prose lines, with AsciiDoc stripped and a tech-word personal dictionary  
- Disable with `--no-spell` if you only want style/structure checks

## How to use

**Stdin (one blob of text):**

```bash
echo "Your text here" | python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py
```

**One or more files or directories** (recurses for `*.adoc`; skips `.git`, `_preview`, etc.):

```bash
python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py /path/to/module.adoc
python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py /home/stevsmit/pp/openshift-docs
```

**Default when no args and stdin is a TTY:** if `/home/stevsmit/pp/openshift-docs` exists, that tree is scanned.

**Useful flags:**

- `--no-spell` — skip Hunspell
- `--max-files N` — stop after *N* files when scanning a tree

**In Cursor:** run `/check-ibm-sg` with a file path or selection as you already do; the agent runs the same script.

## Report format

Issues include **file path** (or `<stdin>`), **line number**, rule name, short description, optional suggestion, and a text snippet.

## Exit codes

- `0`: No issues reported
- `1`: One or more issues reported
- `2`: Usage error (e.g. no stdin, no paths, and no default docs tree)

## Examples

**Violations (stdin):**

```bash
echo "It is important to set up the system. The system will be configured by the administrator." | python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py
```

**Clean sample:**

```bash
echo "To configure your deployment, you can use the oc command. This enables you to manage your cluster resources effectively." | python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py
```

## Dependencies

- **pdftotext** (poppler-utils) — PDF text extraction for corpus verification
- **hunspell** + **en_US** dictionary — spelling (skipped with a warning if missing)

## Notes

- Treat output as **advisory**; technical terms and product names can still trigger spelling noise—extend the script’s tech word list or use `--no-spell` when appropriate.
- Keep all four reference files in `/home/stevsmit/ibm-style-guide/` next to `check-ibm-style.py` for a full corpus load.
