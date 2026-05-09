# PHASE 2 — Search Intent Analysis

**Last updated:** May 9, 2026
**Position in workflow:** Second phase of SOP_01 v2.3
**Agent:** Architect
**Pairs with:** PHASE_01_Tech_Recon (input), WAP_15 Personas (preliminary hypothesis)

---

## Purpose

This is the psychological phase. Get inside the reader's head. Understand:
- What they actually want when they search this topic
- The pain they're starting from (Point A) and the transformation they seek (Point B)
- The natural sequence of questions they'd ask if they could ask a human expert
- Which macro-topics the article must cover to bridge A→B

This phase determines the article's strategic direction. Article Audit (Phase 3) and Persona Match (Phase 4) build directly on this output.

---

## Procedure

### Step 1 — Intent classification

Read top 20 GSC queries from `01_Tech_Report.md`. Classify the dominant intent (>50% of queries):

- **PLANNING:** user is organizing a future trip (still at home, pre-trip research)
- **ON-PLACE:** user is already there or about to arrive
- **DECISION:** user is in active selection mode (almost ready to book/buy)
- **COMPARISON:** user is evaluating alternatives (X vs Y)
- **INFORMATION:** user is just informing themselves (curiosity, no specific intent)

Mark confidence HIGH/MEDIUM/LOW. Cite ≥3 verbatim GSC queries as evidence.

### Step 2 — User profiling: Point A → Point B

This is the most important step. Profile the reader with depth.

**Point A — Where the user is:**
- What problem are they trying to solve?
- What frustrations / pains / fears do they carry?
- What barriers or obstacles do they perceive?
- What do they NOT know that they should know?

**Point B — Where they want to arrive:**
- What is their final desire?
- What transformation do they seek?
- What concrete outcome do they want from this specific article?

**The Bridge:**
The article exists to bridge A→B. Articulate clearly: what specifically must this article do to serve that bridge?

This profiling is the foundation. Every macro-topic in the article must serve the bridge.

### Step 3 — Reader Thought Flow

Generate 10-12 questions (range 8-15 acceptable) that the reader would ask if they could ask a human expert. Order them in the NATURAL sequence the reader's mind would follow.

The natural sequence depends on the article topic and intent. Do not apply a rigid template. Reason case by case based on:
- The intent classification (Step 1)
- The user profile A→B (Step 2)
- The actual GSC queries

Example sequence for a destination guide with PLANNING intent (illustrative, not prescriptive):
"Is it worth going? → How do I get there? → When should I go? → Where do I stay? → What does it cost? → Is it safe? → What should I avoid? → Bonus insider tips"

For a different topic with different intent, the sequence will be different. The agent reasons about which order makes psychological sense for THIS article's reader.

For each question, document:
- Why it matters (1 line)
- What part of the A→B bridge it serves

### Step 4 — Pre-skeleton macro-topics

Group the questions into 5-10 macro-topics. Each macro-topic becomes a candidate H2 in the final article structure (Phase 6).

For each macro-topic:
- Reader question(s) it answers
- GSC cluster it maps to (from Phase 1)
- Priority HIGH / MEDIUM / LOW
  - HIGH: covers Phase 1 emerging cluster + serves dominant intent + critical for A→B bridge
  - MEDIUM: covers stable cluster, supports bridge
  - LOW: marginal, edge cases, optional
- A→B contribution (1 sentence: how this macro-topic helps bridge A→B)

### Step 5 — Persona hypothesis (preliminary)

Based on queries + intent + A→B profile, hypothesize the primary persona from WAP_15 (A / B / C).

This is preliminary. Phase 4 Persona Match confirms it.

### Step 6 — Strategic implications

Synthesize for downstream phases:
- Macro-topics the article MUST cover (HIGH priority)
- Optional macro-topics (MEDIUM)
- Topics to NOT cover (LOW + cannibalized clusters from Phase 1)
- Tone-of-voice fit suggested by persona hypothesis
- A→B bridge clarity (does the proposed structure clearly serve the bridge?)

---

## Output Canonical Structure

File: `projects/POST_[article-slug]/02_Search_Intent.md`

```markdown
# Search Intent Analysis

**Article URL:** [url]
**Date:** [YYYY-MM-DD]
**Based on:** 01_Tech_Report.md

## 1. Intent Classification

**Primary intent:** PLANNING / ON-PLACE / DECISION / COMPARISON / INFORMATION
**Confidence:** HIGH / MEDIUM / LOW
**Evidence:** [3-5 verbatim GSC queries]

**Secondary intent:** [intent + evidence, or "none"]

## 2. User Profiling — Point A to Point B

### Point A — Where the user is

**Problem they're trying to solve:**
[1-2 sentences]

**Frustrations / pains / fears:**
- [Pain 1]
- [Pain 2]
- [Pain 3]

**Perceived barriers:**
- [Barrier 1]
- [Barrier 2]

**Knowledge gaps:**
- [Gap 1]
- [Gap 2]

### Point B — Where they want to arrive

**Final desire:**
[1-2 sentences]

**Transformation sought:**
[1-2 sentences]

**Concrete outcome from this article:**
[1 sentence]

### The Bridge

**What this article must do to bridge A→B:**
[2-3 sentences]

## 3. Reader Thought Flow

10-12 questions in natural psychological order:

1. **[Q1]** — why it matters; A→B contribution
2. **[Q2]** — why it matters; A→B contribution
...

**Order rationale:** [1-2 sentences explaining why this specific order makes sense for this reader]

## 4. Pre-skeleton Macro-Topics

| Macro-topic | Reader question(s) | GSC cluster (Phase 1) | Priority | A→B contribution |
|---|---|---|---|---|

## 5. Persona Hypothesis (preliminary)

**Hypothesized primary persona:** A / B / C
**Reasoning:** [2-3 sentences combining queries + Point A profile + thought flow]
**To be confirmed in Phase 4 Persona Match.**

## 6. Strategic Implications for Article

- **Macro-topics MUST cover** (HIGH priority): [list]
- **Macro-topics OPTIONAL** (MEDIUM): [list]
- **Macro-topics to NOT cover** (LOW + cannibalized): [list]
- **Tone of voice fit:** [suggested framing]
- **A→B bridge clarity:** [1 sentence assessment]
```

---

## Checklist (Y/N)

The Architect agent applies this checklist before delivering.

| # | Check | Y/N |
|---|---|---|
| 1 | Primary intent classified (one of 5: PLANNING/ON-PLACE/DECISION/COMPARISON/INFORMATION) | |
| 2 | Primary intent supported by ≥3 GSC verbatim queries as evidence | |
| 3 | Confidence level marked HIGH/MEDIUM/LOW with reasoning | |
| 4 | Secondary intent identified or explicit "none" | |
| 5 | Point A: problem documented (1-2 sentences) | |
| 6 | Point A: ≥3 frustrations/pains/fears listed | |
| 7 | Point A: ≥2 perceived barriers listed | |
| 8 | Point A: ≥2 knowledge gaps listed | |
| 9 | Point B: final desire documented | |
| 10 | Point B: transformation sought documented | |
| 11 | Point B: concrete outcome from article documented | |
| 12 | Bridge: 2-3 sentences explaining article's specific role | |
| 13 | Reader Thought Flow: 8-15 questions (target 10-12) | |
| 14 | Each question has "why it matters" + "A→B contribution" | |
| 15 | Question order: rationale documented (1-2 sentences explaining the chosen sequence for this reader) | |
| 16 | Pre-skeleton: 5-10 macro-topics | |
| 17 | Each macro-topic mapped to ≥1 reader question | |
| 18 | Each macro-topic mapped to GSC cluster from Phase 1 | |
| 19 | Each macro-topic has priority HIGH/MEDIUM/LOW | |
| 20 | Each macro-topic has A→B contribution (1 sentence) | |
| 21 | Persona hypothesis (A/B/C) selected with reasoning combining queries + Point A profile | |
| 22 | Strategic Implications: HIGH priority topics listed | |
| 23 | Strategic Implications: NOT-cover topics listed | |
| 24 | Strategic Implications: A→B bridge clarity assessment | |

**Pass criteria:** 24/24 Y. All required.

### Hard-fail triggers

- Point A or Point B sections empty/generic → REGENERATE (foundation of the bridge)
- Reader Thought Flow <8 questions → REGENERATE (superficial)
- Reader Thought Flow >15 questions → REGENERATE (article would become encyclopedia, not focused refresh)
- No macro-topic mapped to Phase 1 emerging cluster → REGENERATE (priorities misaligned)
- Bridge section missing or generic → REGENERATE
- Question order without rationale → REGENERATE (order must be reasoned, not random)

---

## Workflow integration

**Input:** `01_Tech_Report.md` from Phase 1

**Output:** `02_Search_Intent.md` saved in `projects/POST_[article-slug]/`

**Next phase:** Phase 3 — Article Audit + Affiliate Inventory (uses Search Intent + Reader Thought Flow + macro-topics to evaluate what's KEEP/UPDATE/KILL/MISSING in the existing article)

---

## Notes for Cowork orchestration

When this phase runs autonomously via Cowork:
1. Cowork verifies `01_Tech_Report.md` exists and is complete (17/17 checklist passed)
2. Cowork runs Architect agent on this PHASE_02 procedure
3. Architect produces `02_Search_Intent.md` + applies 24-item checklist
4. If 24/24 PASS → advance to Phase 3
5. If FAIL → report which checks failed, do not advance

---

## Why this phase matters

Without Search Intent, the article risks:
- Covering topics that don't match what the reader actually needs (generic encyclopedia)
- Wrong order of information (reader gets lost)
- Missing the A→B transformation (article doesn't help the reader)
- Filler content that doesn't serve the bridge

This phase is psychological work. The agent must reason like the reader, not like an SEO checklist.

---

## Changelog

- v1.0 — May 9, 2026 — Initial creation. Documents Search Intent Analysis as standalone phase with 6-step procedure (intent classification, A→B user profiling, reader thought flow, macro-topics, persona hypothesis, strategic implications). 24-item checklist with hard-fail triggers. Question order is AI-reasoned per article, not template-driven.
