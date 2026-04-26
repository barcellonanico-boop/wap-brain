# WAP_13_GSC_AUDIT_LATEST.md — Latest GSC Audit

**Last audit:** April 21, 2026
**Source data:** Google Search Console export, April 21, 2026
**Comparison periods:** Last 3 months vs. Previous 3 months (QoQ), and Last 3 months vs. Same period last year (YoY)

---

## What This Doc Is

The current Google Search Console audit for wearepalermo.com. Living source of truth for SOP_01 and SOP_02. Always reflects the most recent audit.

When a new audit is run, this file is overwritten with the new data. The previous version is moved to `archive/gsc-audits/` named with the audit date (e.g. `2026-04-21_GSC_Audit.md`) for historical reference.

This doc tells agents:
- Which posts are P1, P2, P3, P4 (priority for rewrites)
- Each post's revenue tier (A, B, C)
- Each post's current GSC status
- The latest sitewide trend
- Which patterns to watch for in future audits

---

## How Agents Use This Doc

### SOP_01 Step 1 (Intake)
1. Open this doc
2. Pick the highest-priority post not yet rewritten (P1 first, then P2, then P3)
3. Note its status, revenue tier, current clicks, position
4. Use those as inputs into SOP_01 Step 2 (Prep)

### SOP_02 Step 1 (Topic Selection)
1. Reference this doc to ensure new content fills a gap, not duplicates existing healthy posts
2. Cross-check against the Healthy section before greenlighting a new post on a topic that's already ranking

### Architect (audit refresh, ~every 60 days during Phase 3, then quarterly)
1. Run new GSC export
2. Re-classify all pages using the methodology below
3. Archive current WAP_13 to `archive/gsc-audits/[date]_GSC_Audit.md`
4. Overwrite WAP_13 with new analysis

---

## Cadence

- **Phase 3 test period (Apr-Jun 2026):** every 60 days
- **Ongoing:** quarterly (4x per year)
- Trigger an off-cycle audit if site-wide clicks drop 20%+ month-over-month

---

## Executive Summary — Latest Audit

Site-wide clicks, last 3 months vs. comparison periods:

| Metric | Current (3mo) | QoQ Prev | QoQ Change | YoY Prev | YoY Change |
|---|---|---|---|---|---|
| Total clicks | 54,472 | 47,032 | +7,440 (+16%) | 65,314 | **-10,842 (-17%)** |

**Headline:** QoQ says the site is growing. YoY says the site has lost 17% of its traffic. The QoQ growth is optical — it only exists because we're comparing against an even deeper trough. The real trend is decline.

**Root cause (likely):** Google's core updates through 2024-2025, helpful content classifier integration, and AI Overview cannibalization. Travel queries saw 381% AI Overview growth (per Task 1.8 research). Tripadvisor publicly acknowledged AI Overviews broke their traffic model. WAP shows the same fingerprint: most bleeding posts still rank top 10, losing clicks at stable positions. That's AI Overview theft, not ranking demotion.

**Content in decline:** 44 posts bleeding traffic (40% of catalogued content). 12 are urgent (Priority 1).

---

## Priority Breakdown

| Priority | Count | What It Means | Action |
|---|---|---|---|
| **P1** | 12 | High decline + revenue-critical | SOP_01 first wave |
| **P2** | 6 | High decline + conversion-adjacent | SOP_01 second wave |
| **P3** | 18 | Medium decline OR low-revenue brand posts | SOP_01 third wave |
| **P4** | 30 | Low-priority fixes or dead posts | Address as capacity allows |
| **HEALTHY** | 43 | Healthy — ranking or growing | Leave alone, monitor |

---

## Methodology (Reference)

### Status Classifications

- `LOSING_BOTH` — Declining in QoQ AND YoY. Urgent.
- `LOSING_Q` — Declining in QoQ only. Recent hit.
- `ROTTING` — Flat QoQ but losing 30%+ YoY. Slow bleed.
- `RANKING` — Top 10 position, stable or growing clicks. Healthy.
- `RANKING_SOFT` — Top 10 but drifting down in clicks.
- `UNDERPERFORMING` — Page 2-3 (position 11-30), has impressions but not clicks. Opportunity.
- `NEW_WINNER` — Newer post, no YoY data, >50 current clicks.
- `NEW_POST` — Newer post, any current clicks.
- `NEW_INVISIBLE` — New post, zero traction.
- `EVERGREEN_SEASONAL` — Seasonal post doing well in its season.
- `SEASONAL_OFF` — Seasonal post off-season.
- `NO_DATA` — Invisible to Google. Rewrite or delete.
- `LOW_VISIBILITY` — Low impressions, low position. Forgotten.
- `OTHER` — Doesn't fit cleanly. Manual review.

### Revenue Tiering

- **Tier A (Revenue-critical):** Where to stay, accommodation, car rental, tours, safety, parking, transport, neighborhoods, Mondello/Cefalù/Taormina/Favignana guides, wineries. Booking.com, Discover Cars, GetYourGuide, Parclick commission streams.
- **Tier B (Conversion-adjacent):** Itineraries, "how many days," first-timer guides, what-to-see, places-to-visit hubs. Not direct commission drivers but they funnel traffic into Tier A pages.
- **Tier C (Brand/traffic):** History, Mafia, culture, food-specific posts, folklore, legends. Drive authority and brand, no direct commission.

### Priority Formula

- **P1** = HIGH decline severity + Tier A revenue impact, plus the 3 biggest Tier B bleeders (any Tier B post losing 1,000+ clicks YoY)
- **P2** = HIGH decline + Tier B (most Tier B bleeders) OR MEDIUM decline + Tier A
- **P3** = HIGH decline + Tier C, OR MEDIUM decline + Tier B, OR LOW decline + Tier A
- **P4** = Everything else declining, plus NO_DATA (rewrite/delete)

### Notes on Exceptions in Latest Audit

- `/what-to-see/` (Tier B) upgraded to P1: lost -3,685 clicks YoY, biggest single-page bleed on site.
- `/places-to-visit-near-here/` (Tier B) upgraded to P1: -1,354 YoY loss.
- `/news/comprehensive-guide-visiting-san-vito-lo-capo/` (Tier B) upgraded to P1: -2,893 YoY loss (second biggest bleed).

---

## P1 — Urgent (12 posts)

The emergency room. High decline severity + revenue impact. Fix first via SOP_01.

Sorted by absolute YoY click loss (biggest wounds first):

| # | URL | Status | Tier | Current Clicks | YoY Prev | YoY Δ | YoY % | Position | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `/what-to-see/` | ROTTING | B | 1,786 | 5,471 | **-3,685** | -67% | 6.5 | Biggest single-page bleed on site. Top of funnel hub. Still ranks top 10. AI Overview suspect. |
| 2 | `/news/comprehensive-guide-visiting-san-vito-lo-capo/` | ROTTING | B | 3,587 | 6,480 | **-2,893** | -45% | 7.5 | Second biggest bleed. Still ranks top 10. |
| 3 | `/where-to-stay-palermo/` | ROTTING | A | 594 | 2,606 | **-2,012** | -77% | 9.9 | Biggest revenue page loss. Booking.com commission bleeding. |
| 4 | `/places-to-visit-near-here/` | ROTTING | B | 1,046 | 2,400 | **-1,354** | -56% | 6.6 | Day-trip hub. Feeds tour affiliate traffic. |
| 5 | `/news/what-you-should-know-about-favignana/` | ROTTING | A | 2,153 | 3,340 | **-1,187** | -36% | 6.5 | Ferry + accommodation commission. |
| 6 | `/news/vehicle-parking-palermo/` | ROTTING | A | 2,256 | 3,245 | **-989** | -30% | 5.7 | Parclick commission. Position 5.7 still strong. |
| 7 | `/news/taormina-guide/` | LOSING_BOTH | A | 445 | 1,308 | **-863** | -66% | 13.0 | Position dropped out of top 10. Full rewrite needed. |
| 8 | `/districts/` | ROTTING | A | 152 | 757 | **-605** | -80% | 6.3 | Neighborhood hub feeds where-to-stay. |
| 9 | `/news/renting-car-palermo/` | ROTTING | A | 607 | 1,123 | **-516** | -46% | 13.3 | Discover Cars commission. Dropped to page 2. |
| 10 | `/news/palermo-safe-place-visit/` | LOSING_BOTH | A | 23 | 242 | **-219** | -90% | 10.3 | Trust-building page. -90% brutal. |
| 11 | `/news/best-wineries-and-vineyards-in-sicily/` | LOSING_Q | A | 60 | 13 | +47 | — | 22.0 | QoQ crashed -61% after big YoY growth. Recent hit. Position slipped to page 2. |
| 12 | `/news/cefalu-travel-guide/` | LOSING_Q | A | 75 | 14 | +61 | — | 17.2 | Same pattern. QoQ -57% after YoY growth. Page 2. |

**Pattern observations:**
- 10 of 12 P1 posts still rank top 10 or just outside. The decline is NOT a ranking demotion. It's CTR collapse — almost certainly AI Overview cannibalization.
- 2 posts (Taormina, renting-car) dropped to page 2. These need deeper structural work.
- 2 posts (wineries, cefalù) GREW year-over-year then crashed this quarter. Something recent broke them — algorithm hit or competitor push. Investigate.

**SOP_01 implications for P1 posts still in top 10:**
- Direct-answer block in first 540 words is the lever
- These posts need the extractable TL;DR chunk that AI Overviews can lift verbatim
- Structural rewrite from WAP_06 format (italic lead → Nico intro → benefit → Local's Take → first 540 words MUST contain the full answer)
- Voice preservation matters — many of these posts pre-date the current voice doc

---

## P2 — High Priority (6 posts)

HIGH decline + Tier B, OR MEDIUM decline + Tier A. Second wave.

| URL | Status | Tier | YoY Δ | Position | Notes |
|---|---|---|---|---|---|
| `/news/palermo-taxi-services/` | ROTTING | A | -429 | 9.7 | Still top 10. Transport affiliate potential. |
| `/best-palermo-tours/` | ROTTING | A | -393 | 13.5 | GetYourGuide feed. Dropped to page 2. |
| `/news/precautions-female-travelers-in-sicily/` | ROTTING | A | -365 | 9.6 | Trust page for solo female travel segment. |
| `/news/travel-guide-first-timers/` | LOSING_BOTH | B | -71 | 10.2 | Small volume but trend is ugly (-86% YoY). |
| `/news/airport-transfers/` | UNDERPERFORMING | A | +50 | 12.1 | Page 2, needs push. |
| `/news/where-to-stay-cefalu/` | UNDERPERFORMING | A | +132 | 11.9 | Page 2, Booking.com upside. |

---

## P3 — Medium Priority (18 posts)

MEDIUM decline + Tier B/C, or LOW decline + Tier A, or HIGH decline + Tier C. Third wave.

| URL | Status | Tier | YoY Δ | Position |
|---|---|---|---|---|
| `/sicilian-people/` | ROTTING | C | -787 | 7.0 |
| `/news/godfather-sicilian-shooting-locations/` | ROTTING | C | -747 | 13.7 |
| `/news/salina-island/` | ROTTING | C | -553 | 10.9 |
| `/news/how-many-days-in-palermo/` | ROTTING | B | -441 | 6.9 |
| `/news/historic-palermo-street-markets/` | LOSING_BOTH | C | -393 | 13.4 |
| `/news/explore-palermo-in-one-day/` | ROTTING | B | -266 | 19.2 |
| `/news/plan-palermo-trip/` | ROTTING | B | -252 | 20.4 |
| `/news/top-things-see-corleone/` | LOSING_BOTH | C | -225 | 10.3 |
| `/news/quattro-canti-four-corners/` | ROTTING | B | -181 | 7.4 |
| `/news/feast-saint-rosalia/` | LOSING_BOTH | C | -129 | 11.2 |
| `/free-self-guided-walking-tours/` | UNDERPERFORMING | B | -103 | 12.3 |
| `/news/teatro-massimo/` | UNDERPERFORMING | B | -33 | 11.0 |
| `/audio-guides-palermo/` | UNDERPERFORMING | B | -33 | 16.0 |
| `/free-self-guided-walking-tours/discover-palermo-old-town/` | UNDERPERFORMING | B | -14 | 10.4 |
| `/news/reasons-visit-palermo-infographic/` | UNDERPERFORMING | B | 0 | 10.6 |
| `/free-itinerary/` | UNDERPERFORMING | B | +14 | 13.8 |
| `/news/sicily-itinerary/` | UNDERPERFORMING | B | +112 | 23.1 |
| `/things-to-do/` | UNDERPERFORMING | B | +306 | 10.4 |

---

## P4 and lower priorities

P4 (30 posts) and the remaining declining/dead posts are not enumerated here — they're addressed only as capacity allows after P1-P3 are cleared. For the full P4 list and NO_DATA delete-or-rewrite candidates, see the original snapshot in `archive/gsc-audits/2026-04-21_GSC_Audit.md`.

---

## Healthy Content (43 posts) — Reference Only

Don't touch these via SOP_01. They're ranking or growing. Three standout winners worth studying for pattern replication:

| URL | Status | Position | Why It Wins |
|---|---|---|---|
| `/what-pack-sicily/` | RANKING | 2.4 | +3,576 QoQ, +1,723 YoY. Monster page. Reverse-engineer this. |
| `/news/best-places-sicily/` | NEW_WINNER | 8.6 | +3,859 QoQ. New post, no YoY. |
| `/news/sicilian-street-food-specialities/` | RANKING | 6.7 | +705 QoQ. Stable winner. |

Full list of 43 healthy posts available in archived snapshot if needed for cross-reference.

---

## Key Findings From Latest Audit

### Finding 1: Revenue pages bleed the most
8 of 12 P1 posts are Tier A (direct commission). Total YoY click loss across Tier A P1 posts: **-6,404 clicks**. At WAP's conversion rate and Booking's ~4% commission, this is meaningful monthly revenue leaking out.

### Finding 2: Top 10 ranking doesn't mean healthy
10 of 12 P1 posts still rank top 10 or just below. This kills the old SEO intuition. Watching rankings won't save you. Watch **clicks at constant ranking** to catch AI Overview cannibalization.

### Finding 3: QoQ view alone is misleading
Without YoY, the picture looked like +16% growth. Reality is -17% YoY. Every future audit MUST compare both QoQ and YoY. Seasonal effects make QoQ unreliable as a sole signal.

### Finding 4: Winners exist — study them
The three big winners (`/what-pack-sicily/`, `/news/best-places-sicily/`, `/news/sicilian-street-food-specialities/`) are offsetting the bleed. Reverse-engineer what they're doing right and apply to P1 rescues.

### Finding 5: Seasonal posts need separate tracking
Christmas, New Year's, autumn-guide posts all show as "losing" in April but that's seasonal timing. Status `EVERGREEN_SEASONAL` flags these so they don't get SOP_01 treatment in the wrong season.

---

## Recommended SOP_01 Test Sequence

When SOP_01 runs Phase 3, test on these three P1 posts in this order:

1. **`/where-to-stay-palermo/`** — Highest revenue page loss on the site (-2,012 clicks YoY, Booking.com commission impact). Position 9.9, top of page 2 territory. Full SOP_01 rewrite needed: WAP_06 formatting, first-540-words direct answer block, FAQ schema, structural redesign across 5+ neighborhoods, proper affiliate disclosure. Higher complexity than typical SOP_01 run because it requires structural decisions on multiple sub-topics (which neighborhoods to feature, which accommodation types to cover, what booking guidance to include). Recommend testing SOP_01 on simpler content (e.g. /news/vehicle-parking-palermo/) BEFORE attempting where-to-stay-palermo.

2. **`/news/vehicle-parking-palermo/`** — Position 5.7 is very strong. Clicks bleeding but ranking intact. Perfect test case for "add TL;DR block + FAQ schema" AIO rescue playbook. Parclick commission upside.

3. **`/news/taormina-guide/`** — Dropped to position 13. Structural rewrite needed, not just optimization. Tests SOP_01 on the harder case.

If SOP_01 successfully rescues those three (measurable click recovery within 6-8 weeks), roll across the rest of P1, then P2.

---

## Open Questions From This Audit

These are tracked in the project parking lot for follow-up Architect tasks:

1. **Q-crash investigation:** `/news/best-wineries-and-vineyards-in-sicily/` and `/news/cefalu-travel-guide/` grew YoY then crashed this quarter. What changed in Q1 2026? Algorithm update, competitor publish, or page-specific issue?

2. **Winner reverse-engineering:** Deep-dive on `/what-pack-sicily/` (position 2.4, monster page). What's the structural pattern? Apply it to P1 rescues.

3. **Walking-tour consolidation:** Multiple `/free-self-guided-walking-tours/` URLs underperform. Is this a content cannibalization issue (multiple thin pages competing for same keywords)? Architect investigate.

---

## Audit Schedule

| Audit Date | Status | Snapshot Archived |
|---|---|---|
| April 21, 2026 | Current (this file) | archive/gsc-audits/2026-04-21_GSC_Audit.md |

When next audit runs:
- Move this file's content to `archive/gsc-audits/2026-MM-DD_GSC_Audit.md`
- Replace this file with new audit findings
- Update audit schedule table above

---

## Changelog

- v1.0 — April 26, 2026 — Initial migration of April 21 audit data from `projects/PROJECT_WAP_Content_Machine/06_GSC_Audit_Results.md` to permanent Brain doc. Established living-doc pattern: WAP_13_GSC_AUDIT_LATEST.md always reflects current state, historical snapshots archived to `archive/gsc-audits/[date]_GSC_Audit.md`. SOP_01 references this filename permanently.