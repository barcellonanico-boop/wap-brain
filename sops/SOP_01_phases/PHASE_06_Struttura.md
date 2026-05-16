# PHASE 6 — Struttura

**Last updated:** May 16, 2026 (v2.3.3)
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

### Step 1.5 — Scaffold rule (CRITICAL)

For article REFRESH (not new article from scratch), the existing article is the STRUCTURAL SCAFFOLD. The Architect MUST start from Phase 3 KEEP and UPDATE sections as the H2 backbone, then:

- ADD new H2 only for Phase 3 MISSING gaps or Phase 3 EXTRANEOUS-CONVERT promotions
- REMOVE H2 only for Phase 3 KILL sections
- REORDER H2 only if Phase 4 persona psychology explicitly justifies it (documented in Step 3 order rationale)

The Brain Dump is NEVER the structural source. The Brain Dump is enrichment material that gets distributed across H2 sections (per Step 4 four-source mapping).

If Phase 3 audit lists, for example, 7 KEEP/UPDATE sections + 2 MISSING gaps + 1 EXTRANEOUS-CONVERT promotion, the final H2 count is ~10 (7 + 2 + 1). NOT a fresh list generated from Brain Dump topics.

**Hard-fail trigger:** if the H2 list cannot be traced back to Phase 3 audit verdicts (KEEP / UPDATE / MISSING / EXTRANEOUS-CONVERT), REGENERATE. The H2 list must show its work: each H2 explicitly mapped to a Phase 3 verdict in Step 4.

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

### Step 4.5 — Promotion rule: H2 vs H3 vs callout (CRITICAL)

For every macro-topic and Brain Dump material, decide H2 vs H3 vs callout by CONTENT VOLUME, not by emotional importance:

- **H2** — substantive content (≥200 words) AND has a dedicated query cluster in Phase 1 (even small)
- **H3** — sub-topic of a larger H2, content 50-200 words
- **Callout** (Local's Take / Pick / Warning) — atomic pill, <50 words, no body

**Common error:** mapping a Phase 2 macro-topic to a callout because it's an "event" or "side note" — but the callout cannot hold the actual content (dates, schedule, location, link), forcing a content overflow. If the macro-topic needs >50 words to convey its value, it is NOT a callout.

**Hard-fail trigger:** Phase 2 macro-topic mapped to callout when the mapped content exceeds 50 words → REGENERATE as H2 or H3.

### Step 4.6 — Affiliate CTA saturation rule (CRITICAL)

In any single H2 section, max 1 affiliate CTA hero + max 1 affiliate CTA supporting OF THE SAME TYPOLOGY (e.g. 2 boat tours from GetYourGuide in the same H2 = saturation).

Exception: affiliate CTAs of DIFFERENT typologies (e.g. 1 GYG boat tour + 1 Discover Cars rental + 1 Booking hotel) can coexist in the same H2 because they serve different purchase intents.

**Rationale:** stacking >2 same-typology CTAs in one H2 reduces click-through rate (decision fatigue) and signals low-quality affiliate spam to readers. One hero + one supporting is the proven format from /where-to-stay-palermo/ rebuild May 2026.

**Hard-fail trigger:** H2 with >2 affiliate CTAs of the same typology → REGENERATE with hero + supporting pick.

### Step 4.7 — Article opening sequence (CRITICAL)

Every article opens with the 8-step Author Intro Architecture from brain/WAP_06_CONTENT_FORMAT.md → "Author Intro Architecture (8 Steps — canonical Apr 29)". Phase 6 documents these 8 opening elements explicitly before the first content H2.

The 8 canonical opening steps in order:

1. **Italic lead** — promise/USP in <25 words, italic, above featured image. Specific and strong. NOT generic ("the only guide you need").
2. **Featured image** — plain `<img>`, no `[caption]` shortcode. Placeholder reference here, actual asset in Phase 11.
3. **Disarming opener block** — "I know, I know" or equivalent. Acknowledges reader skepticism BEFORE they voice it.
4. **Name + credibility + sales hook** — one paragraph ~80-100 words. Nico self-introduces with concrete sensory specifics. Bold on identity, italic on emphasis.
5. **Three bullet points: "what you'll learn"** — concrete and specific, proves article delivers on USP.
6. **One sentence: time-vs-benefit framing** — short, frames why reading beats the alternative.
7. **TL;DR table** — structured `<table>` per WAP_06c §1, 4-row default + optional 5th "Where to stay" row.
8. **Affiliate disclosure box** — small grey neutral, Nico-voiced, AFTER TL;DR per WAP_06.

Phase 6 deliverable for the opening: list all 8 elements with per-article content notes (italic lead angle, disarming opener angle, Nico self-intro tailored to persona, 3-bullet content, time-vs-benefit one-liner, TL;DR row content, affiliate disclosure text). Phase 7 Copywriter writes the prose; Phase 6 maps the architecture.

**Hard-fail trigger:** Article opening sequence missing any of the 8 elements → REGENERATE.

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

### Step 6.5 — End-of-article canonical order

The last sections of every article follow this fixed order:

1. Content H2 sections (substantive topics)
2. Bottom Line H2 (decision summary, 80-200 words)
3. FAQ section (4-8 Q&A, `<details>/<summary>` snippet)
4. Continue Planning block (3 internal links, grey box per WAP_06c)

Author bio is NOT an end-of-article H2 in the structure. WordPress renders the canonical author box widget automatically below every post. Author bio updates apply to the WordPress author profile, not to article content.

**Hard-fail trigger:** FAQ placed BEFORE Bottom Line → REGENERATE. Continue Planning missing → REGENERATE. "About author" / "Author bio" H2 present in end-of-article structure → REGENERATE (handled by WordPress widget, not article body).

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
| 21 | Every H2 mapped to Phase 3 audit verdict (KEEP / UPDATE / MISSING source / EXTRANEOUS-CONVERT source). NO H2 sourced only from Brain Dump. | |
| 22 | End-of-article order verified: Bottom Line → FAQ → Continue Planning → Author bio | |
| 23 | Every macro-topic mapped to H2 / H3 / callout by content volume rule (Step 4.5). NO macro-topic >50 words assigned to a callout. | |
| 24 | Affiliate CTA saturation rule: no H2 has >2 CTAs of the same typology. Cross-typology CTAs allowed. | |
| 25 | Article opening sequence documents all 8 elements per Step 4.7 (italic lead + featured image + disarming opener + Nico self-intro + 3 bullets + time-vs-benefit + TL;DR + affiliate disclosure). NOT only TL;DR. | |
| 26 | End-of-article structure has NO "About author" / "Author bio" H2 (WordPress widget handles author box automatically). | |

**Pass criteria:** 26/26 Y. All required.

### Hard-fail triggers

- <90% Phase 2 macro-topic coverage → REGENERATE (article won't serve Search Intent)
- Phase 3 MISSING gaps not 100% addressed → REGENERATE (gaps remain)
- H2 without persona framing → REGENERATE (Phase 8 Voice Pass needs this)
- H2 without sources-to-integrate (all 4 slots empty) → REGENERATE (Phase 7 has nothing to work with)
- Word count totals diverging >15% from target → REGENERATE (math doesn't add up)
- H2 sourced from Brain Dump only (no Phase 3 audit verdict trace) → REGENERATE (Brain Dump cannot generate structure, only enrich)
- FAQ placed before Bottom Line → REGENERATE
- Continue Planning block missing → REGENERATE
- Phase 2 macro-topic mapped to callout when content exceeds 50 words → REGENERATE
- H2 with >2 affiliate CTAs of the same typology → REGENERATE
- Article opening sequence missing any of the 8 canonical elements from WAP_06 Author Intro Architecture → REGENERATE
- "About author" / "Author bio" H2 present in end-of-article structure → REGENERATE (WordPress widget handles automatically)

---

## Workflow integration

**Input:** Phases 1+2+3+4+5 outputs
**Output:** `06_Structure.md`
**Next phase:** Phase 7 — Bozza Informativa (uses this structure as blueprint, integrates 4 sources per H2)

---

## Changelog

- v2.3.3 — May 16, 2026 — Added Step 4.7 Article opening sequence (mandatory 8-step Author Intro Architecture from WAP_06: italic lead + featured image + disarming opener + Nico self-intro + 3 bullets + time-vs-benefit + TL;DR + affiliate disclosure). Corrected Step 6.5 end-of-article order: removed Author bio as structural H2; WordPress widget handles author box automatically. Checklist items #25 #26 added. Two new hard-fail triggers added.
- v2.3.2 — May 16, 2026 — Step 6.5 end-of-article order corrected: Bottom Line → FAQ → Continue Planning → Author bio (Bottom Line first for emotional close, FAQ as safety net after, not before). Added Step 4.5 Promotion rule (H2 vs H3 vs callout by content volume, hard-fail on macro-topic >50 words mapped to callout). Added Step 4.6 Affiliate CTA saturation rule (max 2 same-typology CTAs per H2, hard-fail on more). Checklist items #23 #24 added. Two new hard-fail triggers added. Fix derived from May 16 Phase 6 v1 test on San Vito Lo Capo where Cous Cous Fest was erroneously mapped to a callout despite >50 words of content, and 4 GYG tours saturated H2 5 Beaches.
- v2.3.1 — May 16, 2026 — Added Step 1.5 Scaffold rule mandating existing article (Phase 3 KEEP/UPDATE/MISSING/EXTRANEOUS-CONVERT) as structural source for refreshes; Brain Dump explicitly forbidden as structural source. Added Step 6.5 End-of-article canonical order (FAQ → Bottom Line → Continue Planning → Author bio). Checklist items #21 #22 added. Two new hard-fail triggers added (H2 sourced only from Brain Dump, FAQ after Bottom Line, Continue Planning missing). Fix derived from May 12 Test Run Findings (San Vito Lo Capo) Phase 6 root-cause audit.
- v1.0 — May 10, 2026 — Initial creation. 7-step procedure with H2 ordering rationale (AI-reasoned per persona psychology), per-H2 mapping with 4-source integration framework (existing article + Brain Dump + AI knowledge + Search Intent), word count targets, affiliate placements, internal links, H3 sub-sections, TL;DR + FAQ definition, coverage stats. 20-item checklist with hard-fail on coverage gaps and missing source assignments.
