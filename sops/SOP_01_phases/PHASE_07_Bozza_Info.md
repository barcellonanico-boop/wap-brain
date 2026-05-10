# PHASE 7 — Bozza Informativa

**Last updated:** May 10, 2026
**Position in workflow:** Seventh phase of SOP_01 v2.3
**Agent:** Copywriter
**Pairs with:** PHASE_06_Struttura (blueprint), all source phase outputs

---

## Purpose

Build the article's first complete draft as a Markdown file. This draft has full content (info + voice signals + ironies adapted to persona) but is NOT yet polished for voice geometry (paragraph length, italics density, ellipsis pattern, etc.) and is NOT yet HTML.

This phase integrates FOUR sources to produce the draft. The Brain Dump is one source, not the only source.

---

## The four-source integration model

The Copywriter integrates content from:

1. **Existing article** (from Phase 3 KEEP and UPDATE sections) — informational scaffold. Reuse what's already good. Refresh outdated specifics.

2. **Brain Dump** (from Phase 5) — voice signals, updates, ironies, opinions, family references, affiliate suggestions. Brain Dump is unstructured raw material in Italian/English/mixed. Copywriter parses meaning, doesn't copy verbatim.

3. **AI knowledge** — facts the Copywriter knows from general knowledge. Examples: history of Teatro Politeama, dates of buildings, generic context. Used to fill gaps where Brain Dump and existing article don't have content but the H2 needs to be substantive.

4. **Search Intent** (from Phase 2) — what the reader needs to learn. The Copywriter ensures every H2 actually answers the reader's question, even if neither Brain Dump nor existing article fully addressed it.

### Cultural adaptation per persona (critical)

The Copywriter MUST adapt cultural references to the primary persona (Phase 4). Examples:

- **Italian-language joke from Brain Dump:** "Prenderei i tassisti a bastonate sulle gengive" (literally "I'd club the taxi drivers on the gums").
  - **Persona A (Anglo Couple) adaptation:** "Palermo taxi drivers and I have an understanding: they overcharge me, I curse their grandmothers in Sicilian. It works."
  - The literal translation doesn't land in English. The Copywriter translates the **sentiment** (frustration + Sicilian directness + dark humor) into culturally legible expression.

- **Pop culture reference Brain Dump:** "Tipo Maniscalco quando parla di sua zia" — works for Persona B (heritage Italians know Sebastian Maniscalco) but lands flat for Persona A.
  - **Persona A adaptation:** drop the reference, keep the structural humor (anecdotal storytelling)
  - **Persona B keep:** Maniscalco reference lands

- **Family reference Brain Dump:** "Mia nonna Nunzia diceva sempre…"
  - **Persona A:** translate to "My grandmother used to say…" — keep the warmth, lose untranslatable details
  - **Persona B:** keep "Nonna Nunzia" untranslated — the Italian word adds heritage resonance
  - **Persona C:** depends on context, often translate but with Italian word in italics

The cultural adaptation is the Copywriter's main craft in this phase. Verbatim copy of Italian ironies into an English article for Anglo readers fails.

---

## Procedure

### Step 1 — Inputs

The Copywriter collects:
- `06_Structure.md` — blueprint with per-H2 4-source mapping
- `05_Brain_Dump.md` — Nico's voice signals
- `03_Article_Audit.md` — KEEP/UPDATE specifics
- `02_Search_Intent.md` — A→B bridge, Reader Thought Flow
- `04_Persona_Match.md` — persona framing, DNA traits emphasis
- The existing live article (URL from Phase 1) — for KEEP material extraction

### Step 2 — TL;DR generation

Build the TL;DR box (100-200 words) at top of article using:
- Brain Dump summary if available
- Otherwise, condense Bottom Line of full article

### Step 3 — Per-H2 drafting

For each H2 from Phase 6 Structure, integrate the 4 sources:

**Step 3a — Start with existing article material (if Phase 3 marked KEEP)**

**Step 3b — Integrate Brain Dump material**
- Find Brain Dump segments that touch this topic
- Parse meaning, voice signals, ironies, references
- Adapt culturally for primary persona

**Step 3c — Fill gaps with AI knowledge**
- Maintain voice (write AI-knowledge content in Nico's voice, not Wikipedia voice)

**Step 3d — Verify Search Intent answered**

**Step 3e — Hit word count target (±15%)**

### Step 4 — Affiliate placements

Place affiliate items per Phase 6 mapping as Markdown placeholders:
- `[HOTEL_CARD: hotel-name]`
- `[GYG_CARD: tour-id]`
- `[DC_CALLOUT]`
- `[SW_CALLOUT]`

DO NOT include actual HTML — that's Phase 9 territory.

### Step 5 — Internal links (Markdown format)

### Step 6 — FAQ section (4-8 Q&A, 50-150 words each, Markdown format)

### Step 7 — Sanity checks

Before delivering:
- Every H2 from Phase 6 present
- Every H2 has content from at least 1 source (usually 2-3 combined)
- Cultural adaptation applied where Brain Dump had Italian/idiomatic content
- Word counts within ±15%
- NO HTML markup (Markdown only)
- Voice signals present (ironies, asides, family refs adapted)

### Step 8 — Output

Save `07_Draft_Info.md` to `projects/POST_[article-slug]/`.

---

## Checklist (Y/N)

| # | Check | Y/N |
|---|---|---|
| 1 | Every H2 from Phase 6 Structure present | |
| 2 | H2 order matches Phase 6 | |
| 3 | TL;DR present at top (100-200 words) | |
| 4 | TL;DR sources documented | |
| 5 | Every H2 has content from at least 1 of the 4 sources | |
| 6 | H2 sources tracking: most use 2-3 sources combined | |
| 7 | Cultural adaptation applied: Italian ironies/idioms adapted for primary persona | |
| 8 | Voice signals present: at least 3 ironies/asides/family refs across the article | |
| 9 | Each H2 word count within ±15% of Phase 6 target | |
| 10 | Total article word count within ±10% of Phase 6 target | |
| 11 | Affiliate placements as Markdown placeholders | |
| 12 | Internal links applied per Phase 6 mapping | |
| 13 | FAQ section: 4-8 Q&A pairs | |
| 14 | Each FAQ answer 50-150 words | |
| 15 | NO HTML markup (Markdown only) | |
| 16 | NO inline CSS or HTML class names | |
| 17 | NO actual hotel URLs (only placeholders) | |
| 18 | Search Intent verification: each H2 answers its assigned reader question | |
| 19 | Phase 3 UPDATE specifics actually refreshed | |
| 20 | Phase 3 KILL sections NOT included | |

**Pass criteria:** 20/20 Y. All required.

### Hard-fail triggers

- H2 missing from Phase 6 → REGENERATE
- Cultural adaptation absent: Italian ironies copied verbatim into English for Anglo persona → REGENERATE
- HTML markup present → REGENERATE (Phase 9 territory)
- Phase 3 KILL sections included → REGENERATE

---

## Why this phase is NOT a Brain Dump verbatim assembly

Earlier WAP iterations treated Phase 7 as "ASSEMBLE Brain Dump verbatim, target 80% word overlap." This was wrong. The Brain Dump is unstructured dictated text — it doesn't have all the article's content, doesn't follow article structure, contains tangents and ironies that need cultural adaptation for non-Italian readers.

The corrected Phase 7 integrates four sources, with cultural adaptation as the Copywriter's main craft.

---

## Workflow integration

**Input:** Phase 6 Structure + all upstream phase outputs + existing live article
**Output:** `07_Draft_Info.md` (Markdown)
**Next phase:** Phase 8 — Voice Pass

---

## Changelog

- v1.0 — May 10, 2026 — Initial creation. Four-source integration phase with mandatory cultural adaptation per primary persona. 20-item checklist. Hard-fail on missing H2, literal translation, HTML markup leak.
