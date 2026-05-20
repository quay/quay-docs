# Jira ticket attachments vs ROSA reuse CSV

**When you run this command:** Type or paste the Jira **URL** or **issue key** in the same chat input (for example `https://redhat.atlassian.net/browse/OSDOCS-17113` or `OSDOCS-17113`). The agent reads it from that message; nothing in this file selects the ticket for you.

**Instructions:** The user provides a Red Hat Jira issue URL or key (for example `https://redhat.atlassian.net/browse/OSDOCS-17112` or `OSDOCS-17112`). Complete the workflow below in order. Do not ask the user to run steps you can run yourself.

---

## 1. Resolve the issue key

- Parse the ticket key from the URL (path segment after `/browse/`) or accept a bare key like `OSDOCS-17112`.
- Folder name for outputs: **`{KEY}-attachments`** (example: `OSDOCS-17112-attachments`), created under the **workspace root** (`rosa-crossover`).

---

## 2. Fetch the Jira issue and attachment metadata

- Use the **Atlassian MCP** (or equivalent authenticated Jira access):
  - Call `getAccessibleAtlassianResources` if needed to obtain `cloudId` for `redhat.atlassian.net`.
  - Call `getJiraIssue` with `cloudId` and `issueIdOrKey` set to the ticket key. Use `expand` as needed so **attachments** are present in the response.
- Summarize briefly: ticket **summary**, **status**, and list of **attachment** filenames.

---

## 3. Download attachments into `{KEY}-attachments/`

- Create the directory `{KEY}-attachments` in the workspace if it does not exist.
- For **each** attachment whose filename ends in **`.txt`**:
  - Prefer downloading the file bytes into that folder **preserving the original filename**.
  - If direct download returns **403** or fails (no token in the environment), use a **documented fallback** only when appropriate: for example, reconstruct module-list `.txt` content from **openshift-docs** on GitHub by resolving assemblies and `include::modules/...` lines, matching the “Module Extraction Results” style used in this repo. If you use a fallback, state that clearly in the output.
- If the issue has **no** `.txt` attachments, report that and stop after listing other attachment types.

---

## 4. Scan all `.txt` files in `{KEY}-attachments/`

- Read every `*.txt` file in that folder.
- Extract every **Asciidoc path** referenced (typically paths inside **single quotes** ending in `.adoc`, including **assembly** and **module** paths).
- Build a **normalized** set of paths for comparison:
  - Strip a leading `openshift-docs/` prefix if present.
  - Paths should match the CSV convention (e.g. `modules/foo.adoc`, `microshift_networking/.../bar.adoc`).

---

## 5. Compare to the ROSA reuse spreadsheet

- Load the CSV file at the workspace path:

  **`ROSA reuse of OCP content - ROSA (HCP + CLASSIC).csv`**

- Parse **every** line that contains an `.adoc` path. Treat the path as the **first CSV field** (text before the first comma) when that field ends with `.adoc` (same rule as used when comparing `OSDOCS-17112-attachments` to this file).
- Compute the **set intersection**: paths that appear in **both** the attachment-derived set and the CSV set.

---

## 6. Report results

- List **duplicate `.adoc` files** (the intersection), sorted alphabetically, one path per line.
- If the intersection is **empty**, say so explicitly.
- Optionally include short counts: number of unique `.adoc` refs from attachments, number of rows in the CSV, size of the intersection.

---

## 7. Technical notes (for the agent)

- Do not skip steps after a single failure; if Jira download fails, try MCP-only content, authenticated `curl` if `ATLASSIAN_API_TOKEN` (or similar) is available, or the openshift-docs reconstruction fallback.
- Keep the diff focused: do not edit unrelated project files unless the user asks.
- When citing local files in the final message, use normal workspace-relative paths (for example `OSDOCS-17112-attachments/…` and `ROSA reuse of OCP content - ROSA (HCP + CLASSIC).csv`).

---

**User input:** The user’s message supplies the Jira URL or issue key (and may @-mention the CSV for context; still use the filename above as the canonical path in this repo).
