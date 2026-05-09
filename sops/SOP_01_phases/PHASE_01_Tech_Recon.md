# PHASE 1 — Tech Recon

**Last updated:** May 9, 2026
**Position in workflow:** First phase of SOP_01 v2.3
**Agent:** Architect
**Manual input required from Nico:** GSC export CSVs (YoY + QoQ) — Google does not offer free GSC API
**Pairs with:** WAP_13 (GSC audit reference doc), Ubersuggest API tools

---

## Purpose

Establish empirical SEO baseline for the article being refreshed. Identify trend (recovering/declining/stable), emerging keyword opportunities, cannibalized clusters (likely lost to Google AI Overviews), and competitive SERP landscape. Output is the technical foundation for all subsequent phases.

---

## Procedure (5 steps)

### Step 1 — Inputs required

The agent must collect:
- **Article URL** to be refreshed
- **Main target keyword** for the article (from existing meta title or top GSC query)
- **GSC YoY export CSV** — Last 3 months vs same period previous year (compare period in GSC dashboard)
- **GSC QoQ export CSV** — Last 3 months vs previous 3 months
- **Topic context** — what the article is about (1 sentence)

If any required input is missing, agent flags Nico immediately. Do not proceed.

### Step 2 — GSC analysis (both YoY and QoQ)

For each comparison period, calculate and report:
- Total clicks: current vs comparison + variation %
- Total impressions: current vs comparison + variation %
- CTR: current vs comparison + variation in absolute %
- Average position: current vs comparison + delta

Then identify top 10 queries per period, ranked by current clicks.

### Step 3 — Keyword cluster identification

Group queries from both YoY and QoQ data into clusters:

- **Emerging clusters:** queries that rose >20% in QoQ clicks OR impressions. These are growth opportunities to prioritize.
- **Cannibalized clusters:** queries that dropped >40% YoY. Likely lost to Google AI Overviews or SGE. These topics may need to be abandoned or reframed.
- **Stable clusters:** queries with -20% to +20% variation in both YoY and QoQ. Maintain.

Group queries by topic similarity, not exact match. E.g. "best time visit San Vito", "san vito weather", "san vito in september" → cluster "Best Time".

### Step 4 — Ubersuggest SERP analysis

For the main target keyword, fetch via Ubersuggest API:
- Search volume (monthly)
- SEO difficulty score
- CPC
- Top 10 organic SERP competitors with URL + position + estimated traffic
- SERP features present (5 boolean flags: featured snippet, Google AI Overview, video carousel, People Also Ask, image pack)

### Step 5 — Generate output report

Compile findings into `01_Tech_Report.md` using the canonical structure (see below). Save to `projects/POST_[article-slug]/01_Tech_Report.md`.

---

## Output Canonical Structure

File: `projects/POST_[article-slug]/01_Tech_Report.md`

```markdown
# Tech Recon Report

**Article URL:** [url]
**Main keyword:** [keyword]
**Date:** [YYYY-MM-DD]
**Topic context:** [1 sentence]

## 1. GSC YoY (Last 3 months vs same period previous year)

| Metric | Current | Year ago | Variation |
|---|---|---|---|
| Clicks | X | Y | ±N% |
| Impressions | X | Y | ±N% |
| CTR | X% | Y% | ±N pp |
| Avg position | X | Y | ±N |

### Top 10 queries YoY
| Query | Clicks now | Clicks year ago | Variation | Position now |
|---|---|---|---|---|

## 2. GSC QoQ (Last 3 months vs previous 3 months)

| Metric | Current | Previous | Variation |
|---|---|---|---|
| Clicks | X | Y | ±N% |
| Impressions | X | Y | ±N% |
| CTR | X% | Y% | ±N pp |
| Avg position | X | Y | ±N |

### Top 10 queries QoQ
| Query | Clicks current | Clicks previous | Variation |
|---|---|---|---|

## 3. Keyword Clusters

### Emerging clusters (>20% rising QoQ)
- **[Cluster name]:** queries [list], total clicks change: ±N%
- ...

### Cannibalized clusters (>40% YoY decline, likely AIO loss)
- **[Cluster name]:** queries [list], total clicks decline: -N%
- (Or: "None identified")

### Stable clusters (-20% to +20% variation)
- **[Cluster name]:** queries [list]

## 4. SERP Analysis (Ubersuggest)

**Main keyword:** [keyword]
- Search volume: N/month
- SEO difficulty: N/100
- CPC: $X

### Top 10 SERP competitors
| Position | URL | Domain | Est. traffic |
|---|---|---|---|

### SERP features present
- Featured snippet: Y/N
- Google AI Overview: Y/N
- Video carousel: Y/N
- People Also Ask: Y/N
- Image pack: Y/N

## 5. Strategic Implications

[3-5 sentences. Format:]

**Trend overall:** ↑ recovering / ↓ declining / → stable
**Priority topics for refresh** (based on emerging clusters): [list]
**Topics to abandon** (based on cannibalized clusters): [list, or "none"]
**SERP gap vs competitors:** [observations on what competitors cover that we don't]
**Refresh urgency:** HIGH / MEDIUM / LOW
```

---

## Checklist (Y/N)

The Architect agent applies this checklist before delivering. Self-verification.

| # | Check | Y/N |
|---|---|---|
| 1 | Article URL + main keyword documented | |
| 2 | Topic context (1 sentence) documented | |
| 3 | GSC YoY: all 4 metrics reported (clicks, impressions, CTR, avg position) with variations | |
| 4 | GSC YoY: top 10 queries listed with current vs comparison clicks + variation + position | |
| 5 | GSC QoQ: all 4 metrics reported with variations | |
| 6 | GSC QoQ: top 10 queries listed with current vs previous clicks + variation | |
| 7 | At least 1 emerging cluster identified with queries listed | |
| 8 | Cannibalized clusters documented (specific list OR explicit "none identified") | |
| 9 | Stable clusters documented with queries | |
| 10 | Ubersuggest main keyword data complete (volume + difficulty + CPC) | |
| 11 | SERP top 10 competitors listed with URL + position + est. traffic | |
| 12 | All 5 SERP features flags answered Y/N | |
| 13 | Strategic Implications section: trend overall identified | |
| 14 | Strategic Implications section: priority topics for refresh listed | |
| 15 | Strategic Implications section: topics to abandon listed (or "none") | |
| 16 | Strategic Implications section: SERP gap observations documented | |
| 17 | Strategic Implications section: refresh urgency classified | |

**Pass criteria:** 17/17 Y. All required.

### Hard-fail triggers

- Missing GSC YoY export → BLOCKER. Article cannot proceed. Agent flags Nico to provide CSV.
- Missing GSC QoQ export → BLOCKER. Same as above.
- Missing Ubersuggest data → BLOCKER. Agent retries API or flags Nico.
- Strategic Implications section empty or generic → REGENERATE.

---

## Threshold definitions

- **Emerging cluster:** >20% increase in QoQ clicks OR impressions (whichever is higher)
- **Cannibalized cluster:** >40% YoY decline in clicks
- **Stable:** -20% to +20% variation in both YoY and QoQ
- **Refresh urgency HIGH:** YoY decline >30% OR QoQ decline >20%
- **Refresh urgency MEDIUM:** YoY decline 10-30% OR stable but emerging clusters present
- **Refresh urgency LOW:** stable or recovering trend, no major emerging clusters

---

## Workflow integration

**Input:** Article URL + GSC YoY CSV + GSC QoQ CSV + topic context (provided by Nico manually)

**Output:** `projects/POST_[article-slug]/01_Tech_Report.md`

**Next phase:** Phase 2 — Search Intent Analysis (uses this report's clusters and queries as input)

---

## Notes for Cowork orchestration

When this phase runs autonomously via Cowork:
1. Cowork checks for GSC CSVs in expected location (e.g., `projects/POST_[slug]/raw/gsc_yoy.csv` and `gsc_qoq.csv`)
2. If missing, Cowork notifies Nico and waits
3. Once CSVs present, Cowork runs the Architect agent on this PHASE_01 procedure
4. Architect produces `01_Tech_Report.md` + applies checklist
5. If 17/17 PASS → advance to Phase 2
6. If FAIL → report which checks failed, do not advance

---

## Changelog

- v1.0 — May 9, 2026 — Initial creation. First phase of SOP_01 v2.3 documented as standalone PHASE doc with procedure + checklist + canonical output structure.
