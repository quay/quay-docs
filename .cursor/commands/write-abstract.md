## ⭐ **Updated Prompt (with “To…” as the preferred WHY-first pattern)**

**Instructions:** Scan the file. If it is a module file, for example, :PROCEDURE, :REFERENCE, or :CONCEPT, scan the ASSEMBLY that it is included in. Then, write an exceptional short description for Red Hat product documentation. Follow these strict guidelines and match the writing style shown in the example.

**Style Guidance:**
Write in a clear, calm, explanatory style that uses two concise sentences when possible. Prefer to start with a *purpose-first* structure using **“To…”** when describing why the user performs the task. Use “You can…” when the content is more action-focused or when “To…” is not natural for the module type. Keep the tone confident, direct, and user-focused, without sounding abrupt or overly technical.

1. **Format the Output:** Begin with `[role="_abstract"]` followed by a new line. Do not use bulleted lists or admonitions.

2. **Analyze the Content Type:** Determine whether the content is a Procedure (Task), Concept, or Reference module.

3. **Apply Module-Specific Structure:**

   * **If Procedure:**
     *Prioritize a WHY-first structure beginning with “To…”*
     Use patterns like:
     **“To *achieve the goal that this procedure accomplishes* you can *perform action*.”**
     Include the purpose or benefit up front. This information might be included in the ASSEMBLY file that uses the module.

   * **If Concept:**
     Define the concept in the first sentence, then state why it matters or how it helps the user. Use “To…” only if the concept revolves around a clear purpose.

   * **If Reference:**
     Describe what the item does or what it is used for. Generally avoid “To…” unless the reference itself directly enables a user goal.

4. **Length Constraints:** 50–300 characters (roughly 40–75 words).

5. **Readability:** Use plain English and simple sentences. Target FK Grade 12 or lower.

6. **Voice and Tense:** Active voice, present tense, second person (“You”).

7. **Forbidden Phrasing:**

   * No “This topic covers…”, “This section describes…”, or similar phrasing.
   * Do not use “deployment configurations”; use **deployment** instead.
   * Do not repeat the module title.
   * Do not use admonitions.
   * Avoid feature-forward phrasing like “This product allows you to…”.
   * Avoid anthropomorphism, or the assignment of human characteristics to non-human entities. For example, "The Placement service allows you to. . . ."
   * Avoid phrases like ". . . helps you. . ."; use direct user-action framing instead: ". . . you can . . ."
   * Try not to start with "In {product-title}, and instead use it later in the sentence when possible.

8. **Search Optimization:**
   If the product name does not appear in the title, include **{product-title}** in the **first sentence**.

9. **IBM Style Validation (REQUIRED):**
   **After generating the abstract, automatically validate it against the IBM Style Guide** by running:
   ```bash
   python3 /home/stevsmit/ibm-style-guide/check-ibm-style.py
   ```
   (The script reads from stdin, so pipe the generated abstract text to it, or save to a temp file first)
   
   The validation script dynamically extracts rules from `/home/stevsmit/ibm-style-guide/IBMQuickStyle.pdf` (no hardcoded rules) and checks for violations including:
   - Anthropomorphism (attributing human characteristics to objects)
   - Future tense usage (will, shall, going to)
   - Passive voice patterns
   - Incomplete sentences
   - Sentences starting with "It"
   - Phrasal verbs that could be replaced with one-word alternatives
   
   **If violations are found, revise the abstract to fix them and re-validate until no violations remain.** Only finalize the abstract after it passes IBM Style validation.

---

## ⭐ **Updated Target Style Example (WHY first with “To…”)**

[role="_abstract"]
**To keep your image streams clean and maintain organized image references in {product-title}, you can remove unused or outdated image stream tags. Remove tags by using the `oc delete istag` or `oc tag -d` commands.**