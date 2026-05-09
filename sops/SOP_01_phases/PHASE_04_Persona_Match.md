# PHASE 4 — Persona Match

**Last updated:** May 9, 2026
**Position in workflow:** Fourth phase of SOP_01 v2.3
**Agent:** Architect
**Pairs with:** PHASE_01_Tech_Recon (GSC queries verbatim), PHASE_02_Search_Intent (preliminary hypothesis + Point A→B), PHASE_03_Article_Audit (existing structure + EXTRANEOUS-CONVERT macro-topics), brain/WAP_15_PERSONAS.md

---

## Purpose

Phase 2 produced a preliminary persona hypothesis based on intent + thought flow. Phase 4 is independent verification with rigorous evidence. Either CONFIRM the hypothesis with stronger data, REFINE it (add secondary or adjust framing), or REJECT and replace.

The output of this phase drives:
- Phase 5 Brain Dump (which persona-specific angles to ask Nico)
- Phase 6 Struttura (does persona suggest specific H2 ordering)
- Phase 8 Voice Pass (which DNA traits land hardest with this persona)

If Phase 4 gets the persona wrong, the entire downstream article speaks to the wrong reader.

---

## Procedure

### Step 1 — Inputs

The Architect agent must collect:
- `01_Tech_Report.md` — top 30-50 GSC queries verbatim (broader sample than Phase 2's top 20)
- `02_Search_Intent.md` — preliminary persona hypothesis + Point A→B profile
- `03_Article_Audit.md` — final macro-topic list (Phase 2 + EXTRANEOUS-CONVERT additions)
- `brain/WAP_15_PERSONAS.md` — Personas A/B/C definitions

### Step 2 — Verbatim GSC evidence per persona

For each of the 3 personas (A, B, C), scan top 30-50 GSC queries and classify which match that persona's psychographic profile.

**Persona A — Anglo Couple Planner (50-60% audience, 60-70% revenue):**
- Planning-oriented queries ("best time to visit", "how many days", "guide to")
- Comfort/safety focused ("is X safe", "scams to avoid", "best area to stay")
- 30-65 demographic signals (couple, family with kids, retiree)
- English-native phrasing without heritage cues

**Persona B — Italo-Heritage Seeker 50+ (25-35% audience, 25-35% revenue, HIGH LTV):**
- Italian surname searches ("Barcellona Sicily ancestors", "Sicilian surname meaning")
- Heritage-discovery queries ("where did my family come from", "ancestral hometown")
- Specific village/town searches in rural Sicily
- Multi-generational travel cues ("with my parents", "for my grandmother")
- Italian language fragments mixed with English

**Persona C — Returning Italy Traveler (10-15% audience):**
- Comparative queries ("Palermo vs Catania", "X better than Y")
- Multi-stop itinerary planning ("Sicily 7 days", "Palermo + Taormina")
- Efficiency-focused ("worth it", "skip or visit", "best 2-day itinerary")
- Already-knows-Italy phrasing (less defensive, more curious)

For each persona, count: N queries match / total analyzed. Cite 5-10 verbatim queries as evidence.

### Step 3 — Cross-check vs Point A→B profile (Phase 2)

Phase 2 documented user pains, fears, barriers, knowledge gaps. Score how well each persona's psychographic matches this Point A profile:

- **STRONG alignment:** ≥3 Point A pains map directly to persona's known concerns + Point B desire matches persona's transformation pattern
- **MODERATE alignment:** 1-2 Point A pains map + Point B partially aligned
- **WEAK alignment:** persona's profile doesn't match Point A pains, OR Point B contradicts persona's typical desire

Document specific citations from Phase 2 for each scoring.

### Step 4 — Hypothesis verdict

Compare Phase 2 hypothesis against the verbatim evidence (Step 2) and Point A→B alignment (Step 3). Declare verdict:

- **CONFIRMED:** Phase 2 hypothesis stands. Same primary persona, same confidence level. Match % ≥40% on GSC + STRONG/MODERATE Point A→B alignment.
- **REFINED:** Phase 2 primary persona stands, but adjustments needed:
  - Add secondary persona (significant portion of queries match a different persona)
  - Adjust framing per Point A→B nuances discovered in deeper analysis
- **REJECTED:** Phase 2 hypothesis was wrong. Replace with persona showing stronger evidence. Document what Phase 2 missed.

If REJECTED, the new primary persona must show stronger evidence than the rejected hypothesis (higher GSC match % + better Point A→B alignment).

### Step 5 — Persona-specific framing per macro-topic

Use the FINAL macro-topic list (Phase 2 macro-topics + Phase 3 EXTRANEOUS-CONVERT + Phase 3 MISSING from gap analysis).

For each macro-topic, define:
- **Tone:** how this section should feel for THIS persona
  - Persona A: protective, warning-focused, comfort-reassuring
  - Persona B: cultural-validating, heritage-resonant, intimate
  - Persona C: efficient, comparative, no-bullshit
- **Persona concerns to address:** specific pains/questions THIS persona has on this topic
- **Cultural references / examples:** touchpoints that resonate with THIS persona
  - Persona A: US/UK comfort references, scam warnings, comparison to Disneyland-grade safety
  - Persona B: family stories, dialect references, Nonna Nunzia parallels, generational continuity
  - Persona C: comparison to other Italian cities they may know, efficiency math
- **A→B contribution:** how this section helps THIS persona move from pain to transformation

### Step 6 — Strategic implications for downstream phases

Synthesize for Phases 5, 6, 8:

**Phase 5 Brain Dump — persona-specific angles to ask Nico:**
- Examples: For Persona B → "Tell me a story about your nonna and a Palermo neighborhood." For Persona A → "What scams did your sister encounter in Palermo last summer?"
- Direct quotes the agent should request based on persona

**Phase 6 Struttura — H2 ordering implications:**
- Persona B may benefit from heritage-emotional H2 first (resonance), then logistics
- Persona A may need safety/scam H2 early (defuse anxiety), then planning details
- Persona C may want comparison H2 first (decision support), then deep-dive

**Phase 8 Voice Pass — DNA traits emphasis:**
- Persona A: Scam Radar Disclosure, Anti-Romantic Pragmatist, Setup-Pause-Snap (lands as comedy timing)
- Persona B: Hyperbolic Origin Story (Nonna Nunzia hits home), Cultural Code-Switching, Italian Roast (insider intimacy)
- Persona C: Class/Culture Knife (no-bullshit), Direct Reader Targeting, Numerical Slap (efficiency signals)

### Step 7 — Generate output

Compile findings into `04_Persona_Match.md` using canonical structure (see below). Save to `projects/POST_[article-slug]/04_Persona_Match.md`.

---

## Output Canonical Structure

File: `projects/POST_[article-slug]/04_Persona_Match.md`

```markdown
# Persona Match

**Article URL:** [url]
**Date:** [YYYY-MM-DD]
**Based on:** 01_Tech_Report.md + 02_Search_Intent.md + 03_Article_Audit.md
**Reference:** brain/WAP_15_PERSONAS.md

## 1. GSC Verbatim Evidence per Persona

**Total queries analyzed:** N (top 30-50 from Tech Report)

### Persona A — Anglo Couple Planner
**Match count:** N / [total]
**Match %:** N%
**Verbatim evidence (5-10 queries):**
- "[query 1]"
- "[query 2]"
- ...

### Persona B — Italo-Heritage Seeker 50+
**Match count:** N / [total]
**Match %:** N%
**Verbatim evidence:**
- "[query 1]"
- ...
(Or: "0 match — no heritage-cue queries in top 30-50.")

### Persona C — Returning Italy Traveler
**Match count:** N / [total]
**Match %:** N%
**Verbatim evidence:**
- "[query 1]"
- ...

## 2. Point A → B Profile Alignment

### Persona A alignment
- **Score:** STRONG / MODERATE / WEAK
- **Point A pains matching:** [list with citations from Phase 2]
- **Point B desire matching:** [citation]
- **Reasoning:** [1-2 sentences]

### Persona B alignment
[same structure]

### Persona C alignment
[same structure]

## 3. Hypothesis Verdict

**Phase 2 hypothesis:** [persona]
**Phase 4 confirmed primary:** [persona]
**Verdict:** CONFIRMED / REFINED / REJECTED

**Reasoning (3-5 sentences):**
[Why this verdict, citing match % from Step 2 + Point A→B alignment from Step 3]

**Secondary persona:**
[Persona + justification, OR explicit "none — primary covers >70% of queries"]

## 4. Persona-Specific Framing per Macro-Topic

| Macro-topic | Tone | Persona concerns to address | Cultural refs / examples | A→B contribution |
|---|---|---|---|---|

For each macro-topic from Phase 2 + Phase 3 (including EXTRANEOUS-CONVERT and MISSING gaps).

## 5. Strategic Implications for Downstream Phases

### Phase 5 Brain Dump — persona-specific angles
- [Question angle 1 — what to ask Nico that's specific to this persona]
- [Question angle 2]
- ...

### Phase 6 Struttura — H2 ordering implications
- [Recommendation on H2 order based on persona psychology]
- [Specific H2 that should come early/late]

### Phase 8 Voice Pass — DNA traits emphasis
- **Lands hardest:** [list of WAP_05c trait names with reasoning]
- **Use sparingly with this persona:** [traits that may not resonate or could alienate]

### Affiliate placement reminders (from Phase 3)
- [Persona-specific hotel/tour preferences if relevant]
```

---

## Checklist (Y/N)

The Architect agent applies this checklist before delivering.

| # | Check | Y/N |
|---|---|---|
| 1 | ≥30 GSC queries from Phase 1 analyzed (broader than Phase 2's top 20) | |
| 2 | Persona A: match count + match % + 5-10 verbatim evidence listed | |
| 3 | Persona B: match count + match % + verbatim evidence (or "0 match" explicit) | |
| 4 | Persona C: match count + match % + verbatim evidence (or "0 match" explicit) | |
| 5 | Persona A: Point A→B alignment scored STRONG/MODERATE/WEAK with Phase 2 citations | |
| 6 | Persona B: Point A→B alignment scored with citations | |
| 7 | Persona C: Point A→B alignment scored with citations | |
| 8 | Hypothesis verdict declared CONFIRMED / REFINED / REJECTED | |
| 9 | Verdict reasoning 3-5 sentences citing match % + Point A→B alignment | |
| 10 | If REJECTED: new primary persona has stronger evidence than Phase 2 hypothesis (higher match % + better alignment) | |
| 11 | Secondary persona identified with justification, OR explicit "none — primary covers >70%" | |
| 12 | EVERY macro-topic from Phase 2 + Phase 3 EXTRANEOUS-CONVERT + Phase 3 MISSING has persona framing assigned | |
| 13 | For each macro-topic: tone defined for primary persona | |
| 14 | For each macro-topic: persona concerns identified | |
| 15 | For each macro-topic: cultural refs/examples specific to persona noted | |
| 16 | For each macro-topic: A→B contribution articulated for THIS persona | |
| 17 | Phase 5 Brain Dump direction: persona-specific question angles documented | |
| 18 | Phase 6 Struttura ordering implications noted | |
| 19 | Phase 8 Voice Pass DNA traits emphasis documented (lands-hardest list + use-sparingly list) | |
| 20 | Primary persona match % ≥40% on GSC queries (confidence threshold) | |

**Pass criteria:** 20/20 Y. All required.

### Hard-fail triggers

- Primary persona match <40% on GSC queries → REGENERATE. Low confidence persona match. Either Phase 2 hypothesis was unsupported, OR queries genuinely don't match any persona cleanly. Revisit Phase 2 or escalate to PM.
- ALL 3 personas score WEAK on Point A→B alignment → escalate to PM. Likely Phase 2 user profile is too generic to discriminate between personas. Phase 2 needs revision.
- Macro-topics without persona framing → REGENERATE. Phase 6+8+9 cannot proceed without persona-specific framing per topic.
- Phase 2 hypothesis simply repeated without Step 2-3 verification → REGENERATE. Phase 4 must independently verify with broader sample.

### Soft warnings (do not block, document)

- Primary persona match 40-50%: WARN. Acceptable but borderline. Consider whether secondary persona is needed.
- Phase 2 hypothesis REJECTED: not a fail per se, but log finding. Pattern of repeated rejections across articles signals Phase 2 framework needs improvement.

---

## Workflow integration

**Input:** `01_Tech_Report.md` + `02_Search_Intent.md` + `03_Article_Audit.md` + `brain/WAP_15_PERSONAS.md`

**Output:** `04_Persona_Match.md` saved in `projects/POST_[article-slug]/`

**Next phase:** Phase 5 — Brain Dump (uses persona-specific Question Set angles from this output to formulate questions for Nico)

---

## Notes for Cowork orchestration

When this phase runs autonomously via Cowork:
1. Cowork verifies `01_Tech_Report.md`, `02_Search_Intent.md`, `03_Article_Audit.md` all exist and passed their checklists
2. Cowork runs Architect agent on this PHASE_04 procedure
3. Architect produces `04_Persona_Match.md` + applies 20-item checklist
4. If 20/20 PASS → advance to Phase 5
5. If hard-fail trigger fires → flag PM for resolution, do not advance
6. If soft warning only → advance with warning logged

---

## Why this phase is independent from Phase 2

Phase 2 produces a preliminary hypothesis based on intent + thought flow with limited (top 20) sample. Phase 4 verifies with:
- Broader GSC sample (top 30-50)
- Cross-check against Point A→B profile (which Phase 2 produced AFTER the hypothesis)
- Decision branch CONFIRMED/REFINED/REJECTED forces independent thought

If Phase 4 simply rubber-stamped Phase 2, it would be redundant. The independent verification protects against early framing errors propagating downstream.

---

## Changelog

- v1.0 — May 9, 2026 — Initial creation. Documents Persona Match as independent verification of Phase 2 hypothesis with 7-step procedure (inputs, verbatim GSC evidence per persona, Point A→B alignment scoring, verdict CONFIRMED/REFINED/REJECTED, persona-specific framing per macro-topic, strategic implications for Phases 5/6/8, output). 20-item checklist with hard-fail on <40% match, all-weak alignment, missing macro-topic framing, or rubber-stamping Phase 2 without verification.
