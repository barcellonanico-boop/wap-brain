# WAP_05d — Voice Checklist (Mechanical)

**Last updated:** May 8, 2026
**Status:** v1.0 — initial mechanical engineering
**Pairs with:** WAP_05c (Voice DNA — descriptive source of truth)
**Used by:** Voice Pass (Phase 6) of SOP_01 v2.3 workflow

---

## Purpose

This document is the operational tool the Voice Pass agent applies to a draft. It is NOT descriptive. For descriptions of voice traits, devices, lexical profile, and failure modes, read WAP_05c.

This tool answers ONE question: does this draft pass voice check or fail voice check?

The checklist is mechanical. Numbers, counts, verbatim quotes. No subjective scoring.

---

## How To Use

### Inputs
1. Pass 5 draft (assembled bozza from brain dump)
2. brain/WAP_05c_VOICE_DNA.md (read first for trait definitions)
3. Brain dump source (for verbatim cross-check)

### Output
A `06_Voice_Pass.md` file in the article's POST folder containing:
- Filled checklist (every Y/N, every count, every verbatim quote)
- Per-H2 pass/fail status
- Article-level pass/fail status
- List of flags for Nico if any H2 fails

### Procedure
1. Run mechanical checks (Section 1 below) on each H2 + paragraph + sentence
2. Run trait verbatim evidence check (Section 2 below) on the article
3. Compute pass/fail per H2 + globally (Section 3 below)
4. If any H2 fails OR article fails: produce Nico flag (Section 4)
5. Hard stop: max 2 cycles of agent flag → Nico fix → re-check

The agent NEVER regenerates voice itself. It flags, Nico fixes.

---

## SECTION 1 — MECHANICAL COUNTS

For each H2 section, count and report:

### 1A. H2-level counts (per section)

| Metric | Threshold | Rule |
|---|---|---|
| Sentences ≤3 words | minimum 1 every 200 words of section | PASS if count ≥ ceil(section_words / 200) |
| Single-sentence paragraphs | minimum 40% of paragraphs in section | PASS if (single-sentence paragraphs / total paragraphs) ≥ 0.40 |
| Italics instances | minimum 3 if section >300 words; minimum 1 if section ≤300 words | PASS if count meets threshold for the section size |
| Ellipsis "…" instances | minimum 2 if section >300 words; not required if section ≤300 | PASS if count meets threshold |
| Rhetorical questions | minimum 1 per H2 | PASS if count ≥1 |
| Banned phrases | 0 | HARD-FAIL if count ≥1 — section must regenerate |

Banned phrases list (scan literal substrings, case-insensitive):
stunning, breathtaking, magical, charming, picturesque, vibrant, bustling, hidden gem, wanderlust, delightful, lovely, quaint, whether you're looking for, there's something for everyone, get ready to explore, a feast for the senses, embark on, immerse yourself, experience the magic of, it's worth noting, additionally, furthermore, moreover, in conclusion, to sum up, don't miss, be sure to, ultimate guide, complete guide, locals love, truly, genuinely, incredibly, nestled in, off the beaten path, must-see, must-visit

### 1B. Article-level counts (per article, not per H2)

| Metric | Threshold | Rule |
|---|---|---|
| All-caps words/phrases | minimum 1 per article | PASS if count ≥1 article-wide |
| Em-dashes ("—") | 0 (zero) | HARD-FAIL if count ≥1 — article must regenerate the offending paragraphs |

### 1C. Paragraph-level checks (per paragraph in each H2)

| Metric | Threshold | Rule |
|---|---|---|
| Sentences per paragraph | maximum 3 (hard cap) | FAIL if any paragraph has ≥4 sentences |
| Bullet usage | maximum 30% of paragraphs in section | FAIL if (bulleted blocks / total paragraphs in section) > 0.30 |

### 1D. Sentence-level checks (per H2)

| Metric | Threshold | Rule |
|---|---|---|
| Average sentence length per H2 | 9-12 words target; 13-15 words acceptable only if compensated | PASS if avg ≤12, OR if avg 13-15 AND H2 contains ≥3 sentences ≤3 words within the 30 sentences before/after |
| Compound sentences with "and"/"because"/"however"/"although" connecting 2 independent clauses | maximum 2 per H2 | FAIL if count >2 in a single H2 |
| Contractions density | minimum 80% (count contractions / count of expandable verb forms) | PASS if ≥80%; expandable forms include "do not", "you will", "it is", "we are", "I am", "they are", "would not", "could not", "should not", "is not", "was not", "were not", "have not", "has not", "had not", "will not" |

---

## SECTION 2 — TRAIT VERBATIM EVIDENCE CHECK

For each of the 11 voice elements below, the agent answers Y or N. To answer Y, the agent MUST quote verbatim from the draft the text demonstrating the trait. If the agent cannot produce a verbatim quote, the answer is N. No exceptions. No subjective interpretation.

**Format the agent must use:**
```
Trait #X — [Trait Name]: Y / N
Verbatim evidence: "[exact text from draft]"
H2 source: [section name where the quote appears]
```

If N:
```
Trait #X — [Trait Name]: N
Reason: not present in any H2.
```

### The 11 elements

1. **Anti-Romantic Pragmatist** — actively mocks or dismantles romanticized travel views in favor of brutal logistics
2. **Exaggerated Biological Threat** — absurd, fatalistic hyperbole about consequences of minor mistakes
3. **Dialogic Strawman** — invents whiny/naive tourist quote, then shuts it down
4. **Reluctant Educator** — frames info delivery as exhausting chore made necessary by tourist incompetence
5. **Scam Radar Disclosure** — explicitly points out how institutions/locals/guides are lying or screwing the reader
6. **Class/Culture Knife** — casual, unbothered observations about people, regions, types — no apology
7. **Setup-Pause-Snap** — 3-beat: setup expectation → pause (…/italics/short fragment) → flat verdict
8. **Italian Roast** — self-deprecating Sicilian/Italian targeting (his own people, region, institutions)
9. **Hyperbolic Origin Story** — uses Nonna Nunzia, father, grandfather, etc. as comic authority
10. **Pop Culture Hook** — US/Italian-American references (Mafia movies, Joe Rogan, Sinatra, etc.) used ironically
11. **Direct Reader Targeting** — "you/your" addressing reader's mistakes/assumptions in scene

(Two additional supporting devices — Cultural Code-Switching and Absurdist Metaphor for the Mundane — are tracked but NOT counted toward the 11. They are mechanical devices captured in Section 1.)

---

## SECTION 3 — PASS/FAIL COMPUTATION

### Per-H2 pass criteria

An H2 PASSES if and only if ALL of the following are true:
- All Section 1A H2-level counts meet thresholds
- All Section 1C paragraph-level checks pass
- All Section 1D sentence-level checks pass
- Zero banned phrases (Section 1A hard-fail)

If ANY of the above fails: H2 FAILS and goes to Nico flag.

### Per-article pass criteria

An article PASSES if and only if ALL of the following are true:
- Every H2 individually passes (per above)
- Section 1B article-level counts pass (1 all-caps minimum, 0 em-dashes)
- Section 2 verbatim evidence: ≥5 of 11 traits present with verbatim quote
- Zero banned phrases anywhere in the article

If ANY of the above fails: article FAILS and goes to Nico revision.

### Hard stops

After 2 cycles of agent flag → Nico fix → re-check, if the article still fails, escalate to PM. Do not run a 3rd cycle.

---

## SECTION 4 — NICO FLAG FORMAT

When an H2 or the article fails, the agent produces a flag for Nico. Format:

```
## Voice Pass — H2 #N: [section title] — FAILED

Failed checks:
- [Item from Section 1A/1B/1C/1D, with current count vs threshold]
- [Item from Section 2, missing trait]
- [Banned phrase found: quote it verbatim]

Specific guidance for fix:
- [What needs to be added — e.g. "Section needs 1 more sentence ≤3 words. Currently 0, threshold 1."]
- [What needs to be removed — e.g. "Section contains banned phrase 'hidden gem' on line 14. Remove or rephrase."]

Verbatim quotes from current draft demonstrating the failure:
[Quote relevant text]
```

Nico reads the flag, edits the H2 manually, returns updated H2 to agent. Agent re-runs checklist on the updated H2 only (not the whole article — efficient).

---

## SECTION 5 — WORKFLOW INTEGRATION

### Position in SOP_01 v2.3

```
Phase 1: Tech Recon (GSC primary, Ubersuggest secondary)
Phase 1.5: Affiliate Inventory Check (against WAP_12)
Phase 2: Persona Match (against WAP_15)
Phase 3: Brain Dump (Nico voice memos verbatim)
Phase 4: Struttura
Phase 5: Bozza (assemble brain dump verbatim)
Phase 6: Voice Pass ← THIS DOC drives this phase
Phase 7: HTML (canonical snippets from WAP_06c)
Phase 8: Audit (audit_post.sh v0.8 — 39 mechanical checks)
Phase 9: Review
```

### Voice Pass execution sequence

1. Agent opens Pass 5 draft
2. Agent opens WAP_05c (read trait definitions for context)
3. Agent opens this doc (WAP_05d) and applies the checklist
4. Agent produces 06_Voice_Pass.md with full checklist filled
5. Pass: advance to Phase 7 HTML
6. Fail: produce Nico flag, wait for Nico fix
7. Re-check after fix
8. Hard stop at 2 cycles → escalate to PM

### Hard rule — agent does NOT generate voice from rules

If H2 fails, the agent does NOT regenerate the H2 itself. Voice cannot be generated from rules + examples. The agent flags. Nico fixes manually.

This rule exists because:
- 4 consecutive Pass 2 cycles failed on /where-to-stay-palermo/ rebuild
- 3 consecutive Pass 2 cycles failed on /favignana/ rebuild
- Every locked version of every published article traces back to a Nico brain dump verbatim, lightly assembled

The procedure stops fighting this reality.

---

## CHANGELOG

- v1.0 — May 8, 2026 — Initial mechanical engineering. Separated from WAP_05c (which retains descriptive voice DNA only). Pair WAP_05c + WAP_05d cover Voice Pass: WAP_05c describes the voice, WAP_05d enforces it.
