# Phase 8 Rhythm Fix Prompt (v1.0)

**Author:** Nico Barcellona + PM (May 17, 2026 voice calibration session)
**Status:** locked, validated on San Vito Lo Capo (23 paragraphs split, 23/23 clean)
**Purpose:** operational prompt for the rhythm-fix pass in Phase 8. Used AFTER the translation pass when rhythm_detector.py reports paragraph-level rule C violations. Splits long paragraphs into shorter ones with zero rewriting.

**How to use:**
1. Run rhythm_detector.py on the Phase 8 translation output with --json output mode.
2. Save the JSON to a file (e.g. rhythm_violations.json).
3. For each violation in the JSON, format the paragraph into the prompt below under "THE 23 PARAGRAPHS TO SPLIT" (or as many as you have).
4. Run in a fresh Cowork chat with Copywriter agent.
5. Save the output as rhythm_split_output.md.
6. Run rhythm_merger.py to merge the splits back into the source file.

The agent's job is mechanical: insert blank lines to split paragraphs. No rewriting, no word changes, no additions. The detector + merger handle everything around it deterministically.

---

## THE PROMPT

You are doing a RHYTHM FIX PASS on N paragraphs from a finished article. This is a mechanical splitting task, not a rewrite.

═══════════════════════════════════════════════════════════
WHAT YOU DO

For each paragraph below, split it into 2 or more shorter paragraphs separated by blank lines, so that NO resulting paragraph contains more than 3 sentences.

═══════════════════════════════════════════════════════════
WHAT YOU DO NOT DO

- Do not change any wording. Every word, every comma, every punctuation mark, every italic marker, every bold marker, every link, every placeholder (like [DC_CALLOUT] or [GYG_CARD: ...]), every Italian phrase: all preserved verbatim.
- Do not rewrite sentences. Do not improve sentences. Do not shorten sentences. Do not merge sentences.
- Do not add new sentences. Do not add transitions. Do not add commentary.
- Do not remove any sentence.

The ONLY operation you perform is inserting blank lines between sentences to break the paragraph into smaller paragraphs.

═══════════════════════════════════════════════════════════
SPLITTING RULES

- Default split: every 1 to 3 sentences becomes its own paragraph.
- A single-sentence paragraph is allowed and encouraged for verdicts, punchlines, or short standalone statements.
- A sentence with a strong rhetorical function (a verdict, a one-word reaction, a punchline closing a thought) should be on its own line.
- Read each paragraph and use judgment about WHERE to split, but the constraint is hard: no resulting paragraph contains more than 3 sentences.

═══════════════════════════════════════════════════════════
SPECIAL CASE — Sentences exceeding rule E

If a paragraph contains a sentence flagged as exceeding 30 words AND containing 3+ conjoined clauses (rule E violation), you ARE allowed to split THAT one sentence by replacing a conjunction with a period. Minimal edit. Example: "and bolted on" becomes ". They bolted on". Choose the cleanest split. Do not rewrite anything else in this paragraph beyond that one sentence split.

═══════════════════════════════════════════════════════════
OUTPUT FORMAT

For each of the N paragraphs, output:

### Paragraph N

<the split version, with blank lines between sub-paragraphs>

---

Use the exact heading "### Paragraph N" with the original index number. Use "---" as a separator between paragraphs. No other commentary.

After the last paragraph, write at the very end:
"All N paragraphs split. Done."

═══════════════════════════════════════════════════════════
THE PARAGRAPHS TO SPLIT

[INSERT VIOLATION BLOCKS HERE, FORMATTED AS "### Paragraph N\n<text>\n"]

═══════════════════════════════════════════════════════════

Begin.
