# PHASE 6 — Struttura

**Last updated:** May 10, 2026
**Position in workflow:** Sixth phase of SOP_01 v2.3
**Agent:** Architect
**Pairs with:** All previous phase outputs (1-5)

---

## Purpose

Build the final article structure. Map every macro-topic + Brain Dump material + persona framing into ordered H2/H3 sections with word count targets, affiliate placements, and internal links. This is the blueprint for Phase 7 Bozza Informativa.

---

## Procedure

### Step 1 — Inputs

The Architect agent collects:
- `01_Tech_Report.md` — emerging clusters, target keyword
- `02_Search_Intent.md` — macro-topics, Reader Thought Flow, A→B bridge
- `03_Article_Audit.md` — KEEP/UPDATE sections, MISSING gaps, EXTRANEOUS-CONVERT, refresh scope
- `04_Persona_Match.md` — primary persona, persona framing per macro-topic, DNA traits emphasis
- `05_Brain_Dump.md` — Nico's voice signals, updates, ironies, affiliate suggestions

### Step 2 — H2 list generation

Each FINAL macro-topic becomes an H2 candidate. Sources for the macro-topic list:
- Phase 2 macro-topics
- Phase 3 EXTRANEOUS-CONVERT sections (now elevated to new H2)
- Phase 3 MISSING gaps (need to be added)

### Step 3 — H2 ordering (persona-psychology driven)

Order is AI-reasoned per article based on Phase 4 strategic implications. Not template-driven.

Examples (illustrative, not prescriptive):
- Persona A (Anglo Couple Planner): safety/scams early to defuse anxiety, then logistics, then experience
- Persona B (Italo-Heritage Seeker): heritage-emotional content first (resonance), then practical
- Persona C (Returning Italy Traveler): comparison/decision support first, then deep dives

Document the order rationale in 1-2 sentences.

### Step 4 — Per-H2 mapping

For each H2 in the order, document:

- **Title** (final H2 wording)
- **Macro-topic origin:** Phase 2 / Phase 3 EXTRANEOUS-CONVERT / Phase 3 MISSING
- **GSC cluster:** from Phase 1 (which queries this H2 targets)
- **Reader question covered:** from Phase 2 thought flow
- **Word count target:** 200-800 words (AI-reasoned per topic complexity)
- **Persona framing:** tone + concerns + cultural refs + A→B contribution (from Phase 4)
- **Sources to integrate (for Phase 7 Bozza):**
  - Existing article material: which Phase 3 KEEP/UPDATE sections feed this H2
  - Brain Dump material: which Phase 5 segments feed this H2 (or "none — covered by other sources")
  - AI knowledge needed: gaps where Copywriter must use general knowledge
  - Search Intent angle: what reader question this answers
- **Affiliate placements:** hotel cards / GYG tours / Discover Cars / Sicilian Way callouts (from Phase 3 inventory)
- **Internal links:** from Phase 3 KEEP list relevant to this H2
- **H3 sub-sections (if needed):** each H3 same mapping pattern

### Step 5 — Article framework

Beyond H2 list, define:

- **Total word count target:** 1500-5000 words (AI-reasoned per topic complexity and Phase 3 refresh scope)
- **TL;DR box:** 100-200 words at top of article (Phase 5 Brain Dump material if available, or summary of Bottom Line)
- **FAQ section:** 4-8 Q&A at bottom (sourced from Phase 2 Reader Thought Flow questions not fully covered in main H2 sections)
- **Featured image:** placeholder reference (Phase 11 publish handles actual image)

### Step 6 — Sanity checks

Before delivering Struttura:
- Phase 2 macro-topics coverage: ≥90%
- Phase 3 KEEP sections referenced in source mapping: tracked
- Phase 3 MISSING gaps: 100% addressed by H2 mapping
- Brain Dump material distribution: most H2 reference Brain Dump (but not required for every H2)
- Word count totals: sum of H2 + TL;DR + FAQ ≈ total target ±15%

### Step 7 — Generate output

Save `06_Structure.md` to `projects/POST_[article-slug]/`.

---

## Checklist (Y/N)

| # | Check | Y/N |
|---|---|---|
| 1 | Total word count target documented (range 1500-5000) | |
| 2 | Refresh scope from Phase 3 documented | |
| 3 | Primary persona from Phase 4 documented | |
| 4 | H2 order rationale written (1-2 sentences tied to persona psychology) | |
| 5 | Every H2 has final title | |
| 6 | Every H2 has macro-topic origin classified | |
| 7 | Every H2 has GSC cluster mapped from Phase 1 | |
| 8 | Every H2 has reader question from Phase 2 thought flow | |
| 9 | Every H2 has word count target | |
| 10 | Every H2 has persona framing (tone + concerns + refs + A→B) | |
| 11 | Every H2 has sources-to-integrate with all 4 source slots filled (existing/brain dump/AI/intent) | |
| 12 | Every H2 has affiliate placements documented (specific items or "none" explicit) | |
| 13 | Every H2 has internal links assigned (or "none") | |
| 14 | H3 sub-sections defined where needed with same mapping pattern | |
| 15 | TL;DR box defined with source + format | |
| 16 | FAQ section: 4-8 questions listed with source per question | |
| 17 | Phase 2 macro-topic coverage ≥90% | |
| 18 | Phase 3 MISSING gaps: 100% addressed by H2 mapping | |
| 19 | Brain Dump material distributed across H2 (not all on one H2, not absent everywhere) | |
| 20 | Word count totals add up: sum H2 + TL;DR + FAQ ≈ target ±15% | |

**Pass criteria:** 20/20 Y. All required.

### Hard-fail triggers

- <90% Phase 2 macro-topic coverage → REGENERATE (article won't serve Search Intent)
- Phase 3 MISSING gaps not 100% addressed → REGENERATE (gaps remain)
- H2 without persona framing → REGENERATE (Phase 8 Voice Pass needs this)
- H2 without sources-to-integrate (all 4 slots empty) → REGENERATE (Phase 7 has nothing to work with)
- Word count totals diverging >15% from target → REGENERATE (math doesn't add up)

---

## Workflow integration

**Input:** Phases 1+2+3+4+5 outputs
**Output:** `06_Structure.md`
**Next phase:** Phase 7 — Bozza Informativa (uses this structure as blueprint, integrates 4 sources per H2)

---

## Changelog

- v1.0 — May 10, 2026 — Initial creation. 7-step procedure with H2 ordering rationale (AI-reasoned per persona psychology), per-H2 mapping with 4-source integration framework (existing article + Brain Dump + AI knowledge + Search Intent), word count targets, affiliate placements, internal links, H3 sub-sections, TL;DR + FAQ definition, coverage stats. 20-item checklist with hard-fail on coverage gaps and missing source assignments.
