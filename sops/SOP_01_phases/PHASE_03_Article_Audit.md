# PHASE 3 — Article Audit + Affiliate Inventory

**Last updated:** May 9, 2026
**Position in workflow:** Third phase of SOP_01 v2.3
**Agent:** Scout
**Pairs with:** PHASE_01_Tech_Recon (input), PHASE_02_Search_Intent (input), WAP_12 affiliate database, agents/SCOUT_SYSTEM_PROMPT.md (veridicità protocol)

---

## Purpose

Verify the existing article against the Search Intent (Phase 2) and inventory all affiliate links against WAP_12. The two are combined because they share the same fundamental question: what already exists, and is it good?

This phase determines:
- What sections of the current article to KEEP, UPDATE, KILL, or convert/remove (EXTRANEOUS)
- What macro-topics from Phase 2 are MISSING and need to be added in the refresh
- What internal/external links need attention
- What affiliate links work, what's broken, and what gaps exist in WAP_12 that Phase 5 Brain Dump must fill

---

## Procedure

### PART A — Article Audit

#### Step 1 — Inputs

The Scout agent must collect:
- Article URL (live)
- `01_Tech_Report.md` (Phase 1)
- `02_Search_Intent.md` (Phase 2 — provides macro-topics + reader thought flow + A→B framework)
- WAP_12 entries relevant to the article topic
- Reference: `agents/SCOUT_SYSTEM_PROMPT.md` for fact-verification protocol

#### Step 2 — Fetch and parse article body

Fetch live HTML via curl. Strip:
- `<head>` and meta
- Header navigation
- Footer
- Sidebar
- Comments section (`ol.commentlist` or equivalent)
- Scripts and tracking tags

Extract:
- H1 title
- All H2 and H3 headings (in order)
- Body prose
- All internal links (wearepalermo.com/*) with anchor text
- All external links with anchor text
- All affiliate links (Booking, Discover Cars, GetYourGuide, Podia/Sicilian Way)
- Last-updated date (from HTML meta if present)
- Total word count

#### Step 3 — Section-by-section info-level review

For each H2/H3 section, classify with one verdict:

- **KEEP:** info still accurate, still relevant to Search Intent A→B bridge, voice is acceptable. Ready to copy into refreshed article as-is or with minimal touch-up.
- **UPDATE:** info concept correct but specifics outdated (prices from 2023, statistics outdated, rules changed, contact info changed). Keep the section, refresh the data points.
- **KILL:** info no longer valid (train cancelled, attraction closed, fact wrong, advice obsolete). Remove entirely.
- **IRRELEVANT:** info correct but doesn't serve Search Intent A→B (digression, off-topic). Default action: KILL.
- **EXTRANEOUS:** section doesn't map to any macro-topic from Phase 2 BUT might be valuable. Decision tree: if the section topic is genuinely useful and aligned with the reader's A→B journey, propose CONVERT TO NEW H2 (becomes a new macro-topic in Phase 6 Struttura). Otherwise: KILL.

For every classification: provide 1-sentence reasoning citing either Search Intent (Phase 2) or fact-check evidence (Scout protocol).

#### Step 4 — Structure review vs Phase 2 macro-topics

Cross-reference current article H2/H3 list against the macro-topics identified in Phase 2:

- **COVERED:** macro-topic from Phase 2 has a corresponding section in the article
- **MISSING:** macro-topic from Phase 2 has NO corresponding section (gap to add in refresh)
- **EXTRANEOUS:** existing section that doesn't map to any Phase 2 macro-topic (handled in Step 3)

Statistics:
- COVERED: N/N macro-topics from Phase 2
- MISSING: N macro-topics need to be added
- EXTRANEOUS: N sections (each with proposed action: CONVERT or KILL)

#### Step 5 — Link inventory

Internal links (wearepalermo.com/*):
- Status code check (curl HEAD or equivalent)
- Anchor text
- Target URL
- Relevance assessment (Y/N — does this link still make sense in the refreshed context?)
- Action: KEEP / FIX (update target) / REMOVE

External links:
- Same metadata as internal
- Status code check
- Relevance assessment
- Action: KEEP / FIX / REMOVE

### PART B — Affiliate Inventory

#### Step 6 — Affiliate links cross-reference vs WAP_12

For each affiliate link in the article (Booking, Discover Cars, GetYourGuide, Podia):

Classify:
- **PRESENT in WAP_12:** link exists in inventory database for this topic. Valid. Verify status code 200.
- **MISSING from WAP_12:** link is in article but not in WAP_12. Anomaly. Flag for Nico — either add to WAP_12 (legitimate hotel/tour Nico approves) or remove from article.
- **WAP_12 has it but article doesn't:** opportunity. WAP_12 entry exists for this topic but article doesn't use it. Suggest placement in refreshed structure.

For the article's topic (extracted from Tech Recon main keyword), list WAP_12 coverage:
- Hotels: N entries available
- Tours (GYG): N entries available
- Cars (Discover Cars): N entries available
- Sicilian Way callouts: N possible insertion points

Status code check for ALL affiliate links (even those in WAP_12). Affiliate URLs change (Booking parameter updates, GYG IDs deprecate). Critical to verify.

#### Step 7 — Generate output

Compile findings into `03_Article_Audit.md` using canonical structure (see below). Save to `projects/POST_[article-slug]/03_Article_Audit.md`.

---

## Output Canonical Structure

File: `projects/POST_[article-slug]/03_Article_Audit.md`

```markdown
# Article Audit + Affiliate Inventory

**Article URL:** [url]
**Date:** [YYYY-MM-DD]
**Based on:** 01_Tech_Report.md + 02_Search_Intent.md
**Scout protocol reference:** agents/SCOUT_SYSTEM_PROMPT.md

## 1. Article Snapshot

- H1: [title]
- H2 count: N
- H3 count: N
- Total word count: N
- Last updated (HTML meta): [date or "not present"]

## 2. Section-by-Section Review

| Heading | Level | Verdict | Reasoning | Action |
|---|---|---|---|---|
| [section title] | H2 / H3 | KEEP / UPDATE / KILL / IRRELEVANT / EXTRANEOUS | [1 sentence] | [keep / update specifics / remove / convert to new H2] |

Stats:
- KEEP: N sections
- UPDATE: N sections
- KILL: N sections
- IRRELEVANT: N sections
- EXTRANEOUS (CONVERT to new H2): N sections
- EXTRANEOUS (KILL): N sections

## 3. Structure Review (vs Phase 2 macro-topics)

| Macro-topic (Phase 2) | Status in current article | Notes |
|---|---|---|
| [macro-topic] | COVERED in section X / MISSING | [where it lives now or what's needed] |

Stats:
- COVERED: N/N macro-topics from Phase 2 (X%)
- MISSING: N macro-topics need to be added in refresh
- EXTRANEOUS-CONVERT: N sections becoming new macro-topics

## 4. Internal Links Inventory

| URL | Anchor text | Status | Relevant | Action |
|---|---|---|---|---|

Stats:
- Total internal links: N
- 200 (valid): N
- 404/broken: N
- 301 redirects: N
- Relevant: N
- Irrelevant (suggest remove): N

## 5. External Links Inventory

| URL | Anchor text | Status | Relevant | Action |
|---|---|---|---|---|

Stats:
- Total external links: N
- 200 (valid): N
- 404/broken: N
- Relevant: N
- Irrelevant: N

## 6. Affiliate Links Inventory

### Currently in article
| URL | Type | Status code | In WAP_12? | Action |
|---|---|---|---|---|

### WAP_12 entries available for this topic, NOT currently used in article
| WAP_12 entry | Type | Suggested placement |
|---|---|---|

### Anomalies and broken links
- Affiliate links in article NOT in WAP_12: [list with action: add to WAP_12 or remove]
- Broken affiliate links (non-200): [list — BLOCKER if ≥3]

Stats:
- Total affiliate links in article: N
- Working (200): N
- Broken: N (BLOCKER threshold ≥3)
- WAP_12 coverage: N% of article links match WAP_12
- WAP_12 inventory for topic: N hotels, N tours, N cars, N Sicilian Way placements

## 7. Strategic Implications for Refresh

### Sections
- **KEEP as-is:** [list section titles]
- **UPDATE:** [list with what specifics to update]
- **KILL:** [list with reasoning]
- **EXTRANEOUS → CONVERT to new H2:** [list with proposed new macro-topic name]
- **MISSING (add in refresh):** [list from Phase 2 macro-topics not yet covered]

### Links
- **Internal links to add/fix/remove:** [actionable list]
- **External links to fix/remove:** [actionable list]

### Affiliate
- **Affiliate gaps for Phase 5 Brain Dump:** [list of hotels/tours/cars Nico needs to provide]
- **Affiliate anomalies:** [list with action]

### Refresh scope classification
**Refresh scope:** MINOR / MAJOR / FULL REWRITE
- MINOR: ≥70% sections KEEP, no MISSING HIGH priority macro-topics
- MAJOR: 30-70% KEEP, 1-3 MISSING HIGH priority macro-topics
- FULL REWRITE: <30% KEEP OR ≥4 MISSING HIGH priority macro-topics

**Justification:** [1-2 sentences explaining why this scope]
```

---

## Checklist (Y/N)

The Scout agent applies this checklist before delivering.

| # | Check | Y/N |
|---|---|---|
| 1 | Article body fetched + parsed (H1, H2/H3, body, links, affiliate URLs extracted) | |
| 2 | Word count documented | |
| 3 | Last-updated date extracted (or marked "not present") | |
| 4 | Every H2/H3 section classified with one of 5 verdicts (KEEP/UPDATE/KILL/IRRELEVANT/EXTRANEOUS) | |
| 5 | Each classification has 1-sentence reasoning citing Search Intent or fact-check | |
| 6 | EXTRANEOUS sections each have decision: CONVERT to new H2 OR KILL | |
| 7 | Each Phase 2 macro-topic mapped: COVERED or MISSING | |
| 8 | EXTRANEOUS-CONVERT sections proposed as new macro-topics | |
| 9 | Internal links extracted with anchor text + status code | |
| 10 | Internal links relevance assessed (Y/N each) + action assigned | |
| 11 | External links extracted with status code | |
| 12 | External links relevance assessed + action assigned | |
| 13 | Broken links flagged (404, non-200) | |
| 14 | Each affiliate link in article: PRESENT-in-WAP_12 / MISSING / classified | |
| 15 | Status code 200 verified for ALL affiliate links | |
| 16 | WAP_12 entries for topic listed (even if not used in article) | |
| 17 | Affiliate gaps for Phase 5 Brain Dump documented | |
| 18 | Anomalies flagged (article links not in WAP_12) | |
| 19 | KEEP sections list compiled | |
| 20 | UPDATE sections list with specifics-to-update notes | |
| 21 | KILL sections list with reasoning | |
| 22 | EXTRANEOUS→CONVERT sections list with proposed new macro-topic names | |
| 23 | MISSING sections list (from Phase 2 macro-topics) | |
| 24 | Internal/external links action list compiled | |
| 25 | Affiliate gaps documented as Phase 5 input | |
| 26 | Refresh scope classified MINOR/MAJOR/FULL REWRITE with justification | |

**Pass criteria:** 26/26 Y. All required.

### Hard-fail triggers

- Article body fetch failed → BLOCKER, cannot proceed. Flag Nico to verify URL.
- ≥3 affiliate links broken (non-200) → BLOCKER. Affiliate revenue at risk. Fix WAP_12 entries before proceeding to Phase 4.
- Phase 2 macro-topics ALL MISSING (0% coverage) → escalate. Either Phase 2 framing wrong OR article needs FULL REWRITE without using current as base. PM decision required.
- Strategic Implications section empty or generic → REGENERATE.
- EXTRANEOUS sections without decision (no CONVERT or KILL specified) → REGENERATE.

### Soft warnings (do not block, document for awareness)

- 1-2 affiliate links broken: WARN, fix before publish (Phase 11)
- 1-2 internal links 404: WARN, fix in Phase 9 HTML
- ≥3 internal links 404: stronger signal article is outdated, factor into refresh scope decision

---

## Refresh scope thresholds

| Scope | KEEP % | MISSING HIGH priority | Implication for downstream phases |
|---|---|---|---|
| MINOR | ≥70% | 0 | Phase 7 Bozza will mostly assemble existing + minor brain dump additions |
| MAJOR | 30-70% | 1-3 | Phase 5 Brain Dump must fill significant gaps; Phase 6 Struttura needs reorganization |
| FULL REWRITE | <30% | ≥4 | Treat as new article; existing content provides minimal scaffolding |

---

## Workflow integration

**Input:** `01_Tech_Report.md` + `02_Search_Intent.md` + WAP_12 + article live URL

**Output:** `03_Article_Audit.md` saved in `projects/POST_[article-slug]/`

**Next phase:** Phase 4 — Persona Match (uses audit findings + Search Intent to confirm primary persona with verbatim evidence)

---

## Notes for Cowork orchestration

When this phase runs autonomously via Cowork:
1. Cowork verifies `01_Tech_Report.md` and `02_Search_Intent.md` exist and passed their checklists
2. Cowork runs Scout agent on this PHASE_03 procedure
3. Scout fetches live article HTML, runs full audit + affiliate verification
4. Scout produces `03_Article_Audit.md` + applies 26-item checklist
5. If 26/26 PASS → advance to Phase 4
6. If hard-fail trigger fires → flag Nico for resolution, do not advance
7. If soft warnings only → advance with warnings logged

---

## Why combining Article Audit + Affiliate Inventory makes sense

Both tasks share the fundamental question: what already exists, and is it good? Splitting them would:
- Duplicate the article-fetch step
- Create artificial sequencing (Article Audit before Affiliate Inventory or vice versa)
- Hide the connection between content sections and affiliate placements

Combined, the Scout agent can flag affiliate placements that exist in sections marked KILL (the affiliate becomes orphaned) or recommend new placements for MISSING macro-topics that need to be added.

---

## Changelog

- v1.0 — May 9, 2026 — Initial creation. Combines Article Audit + Affiliate Inventory under Scout agent. 7-step procedure (inputs, fetch+parse, section review with 5 verdicts including EXTRANEOUS, structure review vs Phase 2 macro-topics, link inventory, affiliate cross-ref WAP_12, output). 26-item checklist. EXTRANEOUS sections have decision branch: CONVERT to new H2 or KILL. Refresh scope thresholds documented. Hard-fail triggers: fetch fail, ≥3 broken affiliates, 0% Phase 2 macro-topic coverage.
