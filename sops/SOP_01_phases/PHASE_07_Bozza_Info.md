# PHASE 7 — Bozza Informativa

**Last updated:** May 16, 2026 (v2.3.5)
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

### Cultural adaptation evidence requirement

The Copywriter MUST produce a Cultural Adaptation Log as part of the Phase 7 output. The log lists every Brain Dump segment containing one of the following, and documents the adaptation chosen:

- Italian idiom or proverb
- Bodily-fluid imagery (piscio, sputo, etc.)
- Family-cast reference (nonna, papà, zio, bisnonno, etc.)
- Sicilian dialect expression (futtitinni, allora, minchia, camurria, etc.)
- Untranslated food term (caldofreddo, sfincione, panelle, etc.)
- Superstition reference (toccarsi i coglioni, malocchio, corno, etc.)
- Pop culture reference specific to Italian audience (Maniscalco, Italian TV, etc.)
- Hyperbolic/scatological imagery that may not land for Persona A
- Untranslated Italian or Sicilian term not globally known (any noun, place-type, civic acronym, or cultural concept that an Anglo reader from Manchester or Chicago would NOT recognize). NON-EXAMPLES (globally known, no gloss needed): pizza, pasta, espresso, cappuccino, gelato, panini. EXAMPLES (require gloss): pane cunzato, ZTL, passeggiata, nonno/nonna, sfincione, panelle, pareo, lungomare, tonnaroto, mattanza, lido, agriturismo, baglio.

Format per row:

| Brain Dump segment (verbatim Italian) | Adapted output (English, primary persona) | Adaptation type |
|---|---|---|
| "[verbatim quote]" | "[adapted English]" | drop / translate-sentiment / keep-italics / cultural-equivalent |

If a Brain Dump segment is left verbatim in the draft (zero adaptation), the log must document WHY (e.g., "Maniscalco kept for Persona B — verbatim acceptable") OR the draft is non-compliant.

**Italian/Sicilian term gloss rule:** the first occurrence of any term in category 9 (untranslated Italian/Sicilian term not globally known) MUST be immediately followed by either (a) an inline English gloss in parentheses, e.g. "nonno (grandfather)", "ZTL (the restricted-traffic zone in Italian city centres)", "pane cunzato (a topped Sicilian flatbread)"; OR (b) a self-explanatory surrounding sentence that makes the meaning unambiguous within the same paragraph. Proper-noun dish names (e.g. caldo freddo, busiate, pesto alla Trapanese) treated as named items are exempt from inline gloss IF the surrounding sentence describes the dish. Second and subsequent occurrences of the same term do NOT require gloss.

**Hard-fail trigger:** Cultural Adaptation Log missing → REGENERATE. Brain Dump segments matching categories 1-8 present in the draft without a corresponding log entry → REGENERATE. Category-9 term present in the draft without inline gloss or self-explanatory surrounding sentence at first occurrence → REGENERATE.

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
- Convert dictation rhythm to writing rhythm: Brain Dump is dictated speech. Speech has run-on cadence, repetitions, fillers, and rhythm that reads as transcript when written verbatim. The Copywriter reshapes each Brain Dump excerpt into prose rhythm: tighter sentences, sentence-length variation per WAP_05c, no transcript artifacts. Read the rewritten passage aloud — if it sounds like dictation, rewrite.
- Log every adaptation in the Cultural Adaptation Log (see "Cultural adaptation evidence requirement" above)

**Step 3b-bis — Affiliate CTA cross-reference rule**

When the draft mentions an affiliated product or service that was already CTA-placed in an earlier H2 ("the boat tour above," "the rental I mentioned," "the hotel I recommended," "see the operator above"), the Copywriter MUST re-place the affiliate placeholder (`[GYG_CARD: ...]`, `[DC_CALLOUT]`, `[HOTEL_CARD: slug]`, etc.) inline at the new mention, even if it appears redundant with the earlier placement. NEVER use a text-only cross-reference ("above," "earlier," "as I mentioned") to point the reader back to an affiliate item without re-placing the placeholder.

Rationale:
- Monetisation: the reader clicks on a CTA they see, not on a text instruction to scroll back.
- UX: forcing the reader to scroll up to find a previously placed item breaks reading flow and degrades the article.

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
| 7 | Cultural Adaptation Log present and complete: every Brain Dump segment matching the 8 categories (Italian idiom, bodily-fluid imagery, family-cast reference, Sicilian dialect, untranslated food term, superstition, Italian-audience pop culture, hyperbolic/scatological imagery) has a log entry with verbatim Italian + adapted English + adaptation type. | |
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
| 21 | Dictation rhythm converted to writing rhythm: no transcript-style run-on passages from Brain Dump. Sentence-length variation per WAP_05c applied. | |
| 22 | If any Brain Dump segment in the 8 categories is kept verbatim, the Cultural Adaptation Log documents WHY (persona match justifying verbatim retention). | |
| 23 | Category-9 Italian/Sicilian terms requiring gloss: every first occurrence has either an inline English gloss in parentheses or a self-explanatory surrounding sentence. | |
| 24 | Affiliate CTA cross-reference rule: no text-only "above" / "earlier" / "I mentioned" references to an affiliate item without the corresponding placeholder re-placed inline at the new mention. | |

**Pass criteria:** 24/24 Y. All required.

### Hard-fail triggers

- H2 missing from Phase 6 → REGENERATE
- Cultural adaptation absent: Italian ironies copied verbatim into English for Anglo persona → REGENERATE
- HTML markup present → REGENERATE (Phase 9 territory)
- Phase 3 KILL sections included → REGENERATE
- Cultural Adaptation Log missing → REGENERATE
- Brain Dump segments in the 8 categories present in draft without corresponding log entry → REGENERATE
- Category-9 Italian/Sicilian term present in draft without inline gloss or self-explanatory surrounding sentence at first occurrence → REGENERATE
- Text-only cross-reference to a previously placed affiliate item ("above," "earlier," "I mentioned") without the placeholder re-placed inline at the new mention → REGENERATE

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

- v2.3.5 — May 16, 2026 — Added Cultural Adaptation Log category 9 (untranslated Italian/Sicilian term not globally known) with non-example and example lists. Added Italian/Sicilian term gloss rule: first occurrence of any category-9 term requires inline English gloss in parentheses or self-explanatory surrounding sentence. Added Step 3b-bis Affiliate CTA cross-reference rule: text-only "above" / "earlier" references to a previously CTA-placed affiliate item forbidden — placeholder must be re-placed inline at every mention. Checklist items #23 #24 added (Pass criteria 24/24). Two new hard-fail triggers added.
- v2.3.4 — May 16, 2026 — Added Cultural Adaptation Log requirement: every Brain Dump segment matching 8 categories (Italian idiom, bodily-fluid imagery, family-cast, Sicilian dialect, untranslated food term, superstition, Italian-audience pop culture, hyperbolic/scatological imagery) must have a log entry with verbatim Italian + adapted English + adaptation type. Added Step 3b dictation-to-writing rhythm conversion. Checklist item #7 rewritten; items #21 #22 added (Pass criteria 22/22). Two new hard-fail triggers added.
- v1.0 — May 10, 2026 — Initial creation. Four-source integration phase with mandatory cultural adaptation per primary persona. 20-item checklist. Hard-fail on missing H2, literal translation, HTML markup leak.
