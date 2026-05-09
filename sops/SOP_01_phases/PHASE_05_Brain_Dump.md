# PHASE 5 — Brain Dump + Question Set

**Last updated:** May 9, 2026
**Position in workflow:** Fifth phase of SOP_01 v2.3
**Agent:** Architect (Question Set generation + Brain Dump transcription)
**Human input:** Nico (this is the ONLY phase requiring human intervention)
**Pairs with:** PHASE_01 (emerging clusters), PHASE_02 (macro-topics, A→B), PHASE_03 (UPDATE/MISSING/affiliate gaps), PHASE_04 (persona-specific angles), brain/WAP_05c_VOICE_DNA.md (voice triggers), brain/WAP_12_AFFILIATE_LINKS.md (gap targets)

---

## Purpose

Capture Nico's verbatim knowledge, voice, and on-the-ground reality for the article being refreshed. This is the ONLY phase where Nico intervenes directly. Everything before this is automated analysis. Everything after this is automated execution.

The Brain Dump is the source material from which all subsequent phases (Struttura, Bozza, Voice Pass) draw. Without rich, verbatim Brain Dump material, downstream phases produce generic AI prose.

The Question Set is the bridge: Architect agent uses outputs of Phases 1-4 to formulate questions that elicit exactly what's needed. Nico responds. Architect captures verbatim.

---

## Procedure

### PART A — Question Set generation (automated, before Nico)

#### Step 1 — Inputs

The Architect agent must collect:
- `01_Tech_Report.md` — emerging clusters, keyword gaps
- `02_Search_Intent.md` — Point A→B, reader thought flow, macro-topics
- `03_Article_Audit.md` — UPDATE sections, MISSING macro-topics, affiliate gaps
- `04_Persona_Match.md` — persona-specific angles + DNA traits emphasis
- `brain/WAP_05c_VOICE_DNA.md` — voice trigger inventory (family cast, pop culture references)
- `brain/WAP_12_AFFILIATE_LINKS.md` — current affiliate inventory

#### Step 2 — Identify question categories

Generate questions across 6 categories:

**A. UPDATE QUESTIONS** (info already in article, needs refresh)
- For each section marked UPDATE in Phase 3
- Format: "L'articolo dice [X]. Aggiornamento al 2026?"
- Purpose: refresh outdated specifics (prices, dates, rules, contacts)

**B. MISSING QUESTIONS** (Phase 2 macro-topics not covered)
- For each MISSING macro-topic from Phase 3 structure review
- Format: "Macro-topic [X]: che brain dump hai?"
- Purpose: fill content gaps to align with Search Intent

**C. EMERGING CLUSTER QUESTIONS** (Phase 1 rising queries)
- For each emerging cluster not already addressed by UPDATE/MISSING
- Format: "Le query [X, Y, Z] stanno crescendo. Cosa hai da dire?"
- Purpose: capture rising opportunities

**D. AFFILIATE GAP QUESTIONS** (Phase 3 affiliate inventory gaps)
- One question per critical affiliate gap (hotel/tour/car missing in WAP_12 for this topic)
- Format: "Manca [X hotel/tour] in WAP_12 per questo articolo. Suggerimenti?"
- Purpose: populate WAP_12 with Nico-approved affiliate items

**E. PERSONA-SPECIFIC QUESTIONS** (Phase 4 strategic implications)
- Angles from Phase 4 strategic implications for Brain Dump
- Format: "[Specific angle for primary persona]"
- Purpose: ensure Brain Dump material lands with the right reader

**F. VOICE TRIGGER QUESTIONS** (optional, opportunity for Nico's voice)
- 2-3 questions designed to surface Voice DNA traits
- Examples:
  - Family cast references: "Hai una storia di tuo padre/nonna con [topic]?"
  - Pop culture hook: "Maniscalco-style scenario su [topic]?"
  - Italian Roast triggers: "Cosa ti fa incazzare di [topic]?"
  - Anti-Romantic Pragmatist setup: "Cosa scrivono i travel blog su [topic] che non è vero?"
- Purpose: give Nico explicit prompts that surface DNA traits which downstream Voice Pass can amplify

#### Step 3 — Prioritize and balance questions

Target range: 10-15 questions total.

Distribution guidance:
- HIGH priority Phase 2 macro-topics: 1-2 questions each
- MEDIUM priority macro-topics: 0-1 question each
- LOW priority macro-topics: skip (no Brain Dump needed)
- Affiliate gaps: 1 question per critical gap
- Voice triggers: 2-3 questions opportunistic

If >15 questions, group related questions or cut MEDIUM/LOW priority.
If <10 questions, expand on HIGH priority macro-topics with sub-questions.

#### Step 4 — Format Question Set

Generate intermediate file: `projects/POST_[article-slug]/05a_Question_Set.md`

Structure:

```markdown
# Question Set for [Article Title]

**Date generated:** [YYYY-MM-DD]
**Estimated time for Nico:** ~30-45 min voice memo OR ~20-30 min text response
**Total questions:** N (range 10-15)

## Context for Nico (read first)

- **Persona primaria:** [A/B/C from Phase 4]
- **Persona reasoning:** [1 sentence why this persona]
- **A→B bridge:** [Phase 2 bridge sentence]
- **Refresh scope:** [Phase 3 scope: MINOR/MAJOR/FULL REWRITE]
- **Voice DNA emphasis:** [Phase 4 lands-hardest list — which traits matter most for this persona]

## Questions

### Category A — UPDATE (refresh existing info)

1. **[Question]**
   *Context:* [where in article + what specifically to refresh]

2. ...

### Category B — MISSING (new macro-topics to add)

1. **[Question]**
   *Context:* [macro-topic from Phase 2, A→B contribution]

### Category C — EMERGING CLUSTERS (rising queries from Phase 1)

1. **[Question]**
   *Context:* [cluster name + sample queries]

### Category D — AFFILIATE GAPS

1. **[Question]**
   *Context:* [WAP_12 missing item, persona match]

### Category E — PERSONA-SPECIFIC

1. **[Question]**
   *Context:* [Phase 4 angle, persona reasoning]

### Category F — VOICE TRIGGERS (optional, take if it lands)

1. **[Question]**
   *Context:* [DNA trait it triggers]

## Notes for Nico

- Speak naturally. Don't optimize. Filler is fine — we transcribe verbatim and edit later.
- If a question doesn't land, skip it and explain why.
- Bonus material outside questions is welcomed — captured in dedicated section.
- Voice triggers (Category F) are optional. Take them if a real story comes to mind, skip if forced.
```

### PART B — Brain Dump capture (Nico intervenes)

#### Step 5 — Deliver Question Set to Nico

Cowork notifies Nico: Question Set ready, X questions, estimated time Y minutes. Nico reads the Context section first to align with persona/A→B/voice emphasis.

#### Step 6 — Nico responds

Two formats accepted:
- **Voice memo:** Nico records audio responding to questions in order. File: `projects/POST_[article-slug]/05b_Nico_Raw.[mp3|m4a|wav]`
- **Text:** Nico writes responses directly. File: `projects/POST_[article-slug]/05b_Nico_Raw.md`

#### Step 7 — Transcribe verbatim and organize

Architect agent processes Nico's response:

If voice memo:
- Use transcription tool (Whisper or equivalent)
- Save verbatim including filler ("uhm", "ehm", repetitions, false starts) — DO NOT clean up
- Reason: voice DNA lives in the natural flow; cleanup destroys evidence

If text:
- Copy verbatim, no editing

Organize:
- Match each Question Set question with corresponding response
- If Nico skipped a question: mark "SKIPPED" with reason if provided
- Bonus material (off-topic stories, tangents): capture in dedicated "Bonus / Off-Topic" section

#### Step 8 — Generate output

Compile into `05_Brain_Dump.md` using canonical structure (see below). Save to `projects/POST_[article-slug]/05_Brain_Dump.md`.

The intermediate `05a_Question_Set.md` and `05b_Nico_Raw.md` files remain in the project folder for traceability.

---

## Output Canonical Structure

File: `projects/POST_[article-slug]/05_Brain_Dump.md`

```markdown
# Brain Dump

**Article URL:** [url]
**Date Question Set generated:** [YYYY-MM-DD]
**Date Brain Dump captured:** [YYYY-MM-DD]
**Capture format:** Voice memo / Text
**Based on:** Phases 1+2+3+4

## Context Summary

- **Persona primaria:** [A/B/C]
- **A→B bridge:** [from Phase 2]
- **Refresh scope:** [from Phase 3]
- **Voice DNA emphasis:** [from Phase 4 lands-hardest list]

## Brain Dump per Question

### Category A — UPDATE

**Q1:** [question verbatim from Question Set]
**Nico verbatim:** "..."

**Q2:** [question]
**Nico verbatim:** "..."

### Category B — MISSING

**Q[N]:** [question]
**Nico verbatim:** "..."

### Category C — EMERGING CLUSTERS

[same structure]

### Category D — AFFILIATE GAPS

**Q[N]:** [question]
**Nico verbatim:** "..."
**WAP_12 update needed:** YES — add [item details] / NO / DEFER (Nico will provide later)

### Category E — PERSONA-SPECIFIC

[same structure]

### Category F — VOICE TRIGGERS

[same structure, including SKIPPED if Nico passed]

## Bonus / Off-Topic Material

Things Nico said outside the Question Set scope — preserve verbatim, may be useful for downstream phases:

- "[verbatim]"
- "[verbatim]"

## WAP_12 Updates Required

Affiliate items Nico mentioned that need to be added to WAP_12:

| Item | Type | URL/ID | Persona match | Notes |
|---|---|---|---|---|

## Quality Notes

- **Voice DNA traits surfaced (verbatim evidence):**
  - Trait 1: [name] — quote: "..."
  - Trait 2: [name] — quote: "..."
  - ... (target ≥3 traits)
- **Phase 2 macro-topic coverage:** N/N COVERED (X%)
- **Phase 3 MISSING gaps coverage:** N/N filled (X%)
- **Phase 3 affiliate gaps coverage:** N/N addressed (X%)
- **Estimated downstream usability:** HIGH / MEDIUM / LOW (based on richness + verbatim quality)
```

---

## Checklist (Y/N)

The Architect agent applies this checklist before delivering. Two-stage: PART A applies before delivering Question Set to Nico, PART B+C apply after Nico response.

| # | Check | Y/N |
|---|---|---|

### PART A — Question Set quality (before delivery to Nico)

| 1 | Question Set has 10-15 questions total (range 8-15 acceptable) | |
| 2 | Category A UPDATE: covers all Phase 3 UPDATE-marked sections | |
| 3 | Category B MISSING: covers all Phase 2 macro-topics not yet in article | |
| 4 | Category C EMERGING CLUSTERS: includes Phase 1 rising clusters not covered by A or B | |
| 5 | Category D AFFILIATE GAPS: 1 question per critical Phase 3 affiliate gap | |
| 6 | Category E PERSONA-SPECIFIC: leverages Phase 4 strategic implications | |
| 7 | Category F VOICE TRIGGERS: 2-3 optional questions targeting DNA traits | |
| 8 | Each question has context line (purpose + reference to Phase output) | |
| 9 | Estimated time for Nico documented (voice or text) | |
| 10 | Persona/A→B/Voice emphasis context summary at top of Question Set | |

### PART B — Brain Dump capture quality (after Nico response)

| 11 | Nico response captured: voice memo transcribed verbatim OR text copied verbatim | |
| 12 | NO paraphrasing — verbatim only including filler/repetitions (Finding #74 critical) | |
| 13 | Each Question Set question has matched answer OR explicit "SKIPPED" with reason | |
| 14 | Bonus / off-topic material captured in dedicated section verbatim | |
| 15 | WAP_12 update list compiled with items Nico mentioned (URL/type/persona/notes) | |

### PART C — Coverage verification

| 16 | Phase 2 macro-topic coverage: ≥80% in Brain Dump material | |
| 17 | Phase 3 MISSING gaps: ≥90% addressed | |
| 18 | Phase 3 affiliate gaps: 100% addressed (skip explicit acceptable) | |
| 19 | Voice DNA traits surfaced: ≥3 traits with verbatim evidence | |
| 20 | Coverage stats documented in Quality Notes section | |

**Pass criteria:** 20/20 Y. All required.

### Hard-fail triggers

- Question Set <8 or >15 questions → REGENERATE (out of acceptable range)
- Question Set missing UPDATE / MISSING / AFFILIATE GAPS categories → REGENERATE (core coverage broken)
- Brain Dump paraphrased instead of verbatim → REGENERATE (Finding #74 critical — verbatim is the source of voice authenticity)
- Phase 3 affiliate gaps <100% addressed → BLOCKER (cannot proceed to Struttura without affiliate clarity; Nico must explicitly skip if no input)
- Phase 2 macro-topic coverage <80% → flag for follow-up Brain Dump session before advancing

### Soft warnings (do not block, document)

- Voice DNA traits surfaced <3: WARN (Brain Dump may be flat, downstream Voice Pass will struggle)
- Phase 2 macro-topic coverage 80-90%: WARN (acceptable but not ideal)

---

## Why this is the only Nico-intervention phase

Phases 1-4 are pure analysis: GSC data, Search Intent reasoning, article audit, persona verification. All can run autonomously by AI agents.

Phases 6-11 are execution: Struttura, Bozza, Voice Pass, HTML, Audit, Review. All run autonomously once Brain Dump is complete.

Phase 5 is the irreducible human input. Nico's voice, knowledge, lived experience, family stories, and on-the-ground reality cannot be generated by AI. They must be captured.

Once captured, every subsequent phase processes the Brain Dump material — Struttura organizes it, Bozza assembles it, Voice Pass amplifies the voice signals already present in it, HTML formats it, Audit verifies it, Review approves it.

If Brain Dump quality is low (paraphrased, generic, thin), every downstream phase suffers. Hence the strict checklist on verbatim + coverage + voice trait surfacing.

---

## Workflow integration

**Input:** Phases 1+2+3+4 outputs + WAP_05c voice triggers + WAP_12 inventory

**Output:** `05_Brain_Dump.md` saved in `projects/POST_[article-slug]/`. Intermediate files `05a_Question_Set.md` and `05b_Nico_Raw.[mp3|md]` retained for traceability.

**Next phase:** Phase 6 — Struttura (uses Brain Dump material organized by H2 to build final article structure)

---

## Notes for Cowork orchestration

When this phase runs autonomously via Cowork:
1. Cowork verifies Phases 1-4 outputs all exist and passed their checklists
2. Cowork runs Architect agent on PART A (Question Set generation)
3. Architect produces `05a_Question_Set.md` + applies PART A checklist (items 1-10)
4. Cowork notifies Nico: Question Set ready, expected time Y minutes
5. Cowork pauses workflow, waits for Nico response file (`05b_Nico_Raw.[mp3|md]`)
6. Once Nico response detected in project folder, Cowork resumes
7. Architect runs PART B (transcription + organization)
8. Architect runs PART C (coverage verification)
9. Architect produces `05_Brain_Dump.md` + completes full 20-item checklist
10. If 20/20 PASS → advance to Phase 6
11. If hard-fail trigger fires → flag Nico, do not advance
12. If soft warning only → advance with warning logged

The notification + pause mechanism is what makes this phase fit autonomous orchestration despite requiring human input.

---

## Changelog

- v1.0 — May 9, 2026 — Initial creation. Documents the only Nico-intervention phase with 8-step procedure split into PART A (automated Question Set generation, 6 categories: UPDATE/MISSING/EMERGING CLUSTERS/AFFILIATE GAPS/PERSONA-SPECIFIC/VOICE TRIGGERS), PART B (Nico responds via voice memo or text), PART C (verbatim transcription + organization). 20-item checklist split across PART A (10 items, Question Set quality), PART B (5 items, capture quality), PART C (5 items, coverage verification). Hard-fail triggers: Question Set out of range, missing core categories, paraphrased Brain Dump (Finding #74), affiliate gaps <100% addressed, macro-topic coverage <80%. Cowork orchestration includes notification + pause mechanism to fit autonomous workflow despite human input.
