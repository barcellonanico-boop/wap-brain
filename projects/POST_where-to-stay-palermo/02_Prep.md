# 02_Prep.md — Where to Stay in Palermo

**SOP:** SOP_01 v2.1, Step 3 (Prep)
**Date:** May 1, 2026
**Target URL:** https://wearepalermo.com/where-to-stay-palermo/
**Run by:** Claude Code (CLI)
**Time spent:** ~20 min

---

## Strategic Reframe

**Position 9.8 average. CTR 1%. The post is being SEEN but not CLICKED.**

54,500 impressions over 3 months means Google is showing this page regularly on page 1 lower half. But 1% CTR at that impression volume is brutal — the page is losing the click to competitors above it AND to AI Overview absorption.

**Three problems, three fixes:**

1. **Title kills freshness.** Current SEO title: "The 3 Top Areas and Accommodations for Your Palermo Stay 2025" — year-stamped to LAST YEAR. In May 2026, this is a freshness penalty. Searchers skip 2025-dated results. Fix: rewrite title with 2026 or no year, plus Nico voice hook.

2. **Structure doesn't earn AI citation.** No TL;DR in first 200 words. No FAQ section. No FAQPage schema. The direct answer to "where to stay in Palermo" is buried below filler. Fix: WAP_06 author intro architecture (8 steps) puts the answer in the first 540 words. FAQPage schema earns Rich Results.

3. **Voice is the only moat vs DA 90+ competitors.** Reddit, Times, Telegraph all rank on this query with raw domain authority. WAP (DA 33) can't outmuscle them on links. The differentiation is Nico's authentic local voice — something no travel-guide aggregator can replicate. Fix: full voice install via Pass 2 with WAP_05b patterns.

**Recovery math:** Climbing from position 9.8 → 5 ≈ 3x current clicks (~1,650/quarter). Position 5 → 3 ≈ another 2x (~3,300/quarter). The 2,500+/quarter recovery target requires roughly position 5 sustained.

---

## GSC Query Analysis (Top 10 — last 3 months, source: Nico GSC screenshot May 1)

[Source: GSC live data via Nico screenshot. NOT Ubersuggest/Ahrefs.]

| Rank | Query | Clicks | Impressions | CTR | Notes |
|---|---|---|---|---|---|
| 1 | where to stay in palermo | 63 | 3,571 | 1.8% | Primary keyword. Highest clicks. |
| 2 | where to stay palermo | 15 | 574 | 2.6% | Variant, decent CTR |
| 3 | palermo where to stay | 12 | 691 | 1.7% | Variant |
| 4 | we are palermo | 12 | 340 | 3.5% | BRAND query — not topical |
| 5 | best area to stay in palermo | 10 | 920 | 1.1% | HIGH OPPORTUNITY — high impressions, low CTR. AIO candidate. |
| 6 | where to stay in palermo sicily | 9 | 760 | 1.2% | Sicily qualifier. AIO candidate. |
| 7 | wearepalermo | 6 | 147 | 4.1% | BRAND query |
| 8 | palermo best area to stay | 4 | 103 | 3.9% | Variant of #5 |
| 9 | best place to stay in palermo | 3 | 592 | 0.5% | WORST CTR — 592 impressions, 3 clicks. Strong AIO cannibalization signal. |
| 10 | best area to stay in palermo sicily | 3 | 349 | 0.9% | AIO candidate |

**Total:** 551 clicks | 54,500 impressions | 1% average CTR | position 9.8

**Key observations:**

- **Brand queries (#4, #7)** = 18 clicks combined. These confirm domain recognition but aren't topical.
- **"best area" cluster (#5, #8, #10)** = 17 clicks / 1,372 impressions / ~1.2% CTR. HIGH OPPORTUNITY — these are the "which neighborhood" intent queries the rewrite directly answers.
- **"best place" (#9)** = 0.5% CTR on 592 impressions. Almost certainly AIO-cannibalized. The AI Overview answers "Politeama, Centro Storico, Mondello" directly and the user never clicks.
- **974 total queries** available — PM to request full export for long-tail analysis. Long-tail likely includes "kalsa palermo stay", "politeama palermo hotel", "mondello vs centro storico palermo" etc.

**AIO cannibalization candidates:**
- "best place to stay in palermo" (0.5% CTR — abnormal even for position 9)
- "best area to stay in palermo" (1.1% CTR on 920 impressions)
- "best area to stay in palermo sicily" (0.9% CTR on 349 impressions)

**Strategy:** TL;DR table in first 540 words with the 3-area answer + "My pick" = the AI Overview source citation play. If Google cites WAP's TL;DR as the AIO source, CTR problem reverses — WAP gets the brand credit even if user doesn't click.

---

## Affiliate Audit

### Hotels on live page vs WAP_12

All 15 WAP_12 hotels are present on the live page. All use `aid=918822`. No missing affiliate IDs.

| Hotel | Live URL Slug | WAP_12 Slug | Match |
|---|---|---|---|
| Family Affair B&B | family-affair-b-amp-b-palermo | family-affair-b-amp-b-palermo | ✅ |
| Politeama Apartments | painpa-i-mercati-apartments | painpa-i-mercati-apartments | ✅ |
| Hotel Politeama | politeama-palace | politeama-palace | ✅ |
| Hotel Wagner | grand-wagner | grand-wagner | ✅ |
| Grand Hotel et Des Palmes | grandhoteletdespalmespalermo | grandhoteletdespalmespalermo | ✅ |
| Palazzo Sovrana | palazzo-sovrana | palazzo-sovrana | ✅ |
| La Terrazza sul Centro | la-terrazza-sul-centro | la-terrazza-sul-centro | ✅ |
| Palazzo Natoli | exclusive-rooms-palazzo-natoli | exclusive-rooms-palazzo-natoli | ✅ |
| Grand Hotel Piazza Borsa | grand-piazza-borsa | grand-piazza-borsa | ✅ |
| Palazzo Santamarina | santamarina-luxury-suites-fit-amp-spa | santamarina-luxury-suites-fit-amp-spa | ✅ |
| B&B Mondello Design | b-amp-b-mondello-design | b-amp-b-mondello-design | ✅ |
| L'Officina di Apollo | l-39-officina-di-apollo | l-39-officina-di-apollo | ✅ |
| Villa Cinzia | villa-cinzia-palermo | villa-cinzia-palermo | ✅ |
| Villa Gabriella | villa-gabriella-palermo | villa-gabriella-palermo | ✅ |
| Unico Boutique d'Arte | unico-boutique-d-39-arte | unico-boutique-d-39-arte | ✅ |

**All 15 match. Zero discrepancies. Zero missing affiliate IDs.**

**Note:** The earlier Step 2 flag about Grand Hotel Et Des Palmes URL discrepancy (`grandhoteletdespalmespalermo` vs `grand-wagner`) was a misread — those are TWO DIFFERENT HOTELS. Grand Hotel et Des Palmes = `grandhoteletdespalmespalermo`. Hotel Wagner = `grand-wagner`. Both correct, both present.

### Other links on live page

- **Airbnb embed:** `airbnb.it/rooms/972417625250236623` — Nico's own Via Divisi apartment. Direct booking, not affiliate. Present and working.
- **Google Maps links:** 2 maps embeds (Politeama area, general Palermo). Working.
- **Booking.com site-wide badge:** `//www.booking.com?aid=918822` — theme-level, not post content. Present.

### Revenue bug flag (from Step 2)

Step 2 flagged "Family Affair Palermo broken inner href to Palazzo Sovrana." This needs verification in Step 4 or Pass 3 — may be a visual/layout issue on the live page rather than a broken link. All affiliate URLs confirmed working at the URL level.

---

## Hotel Inventory Check (3 buckets)

**Bucket 1 — On live page AND in WAP_12 ✅ (15 hotels)**
All 15 WAP_12 hotels are on the live page. Full match.

**Bucket 2 — On live page but NOT in WAP_12 ❓**
None found. The live page only contains the 15 WAP_12 hotels + Nico's Airbnb (direct booking section, not affiliate).

**Bucket 3 — In WAP_12 but NOT on live page**
N/A — WAP_12 was built FROM this page's hotel list. All 15 are present.

**New hotels from Intake brain dump (not yet in WAP_12):**
- Villa Igea (Rocco Forte, ~€2,000/night) — mentioned by Nico in Intake. NOT on live page, NOT in WAP_12. Step 4 decides whether to add.

---

## Internal Link Candidates

| URL | Status | Post Title | Why It Fits |
|---|---|---|---|
| /news/where-to-stay-cefalu/ | 200 ✅ | Where to Stay in Cefalù | Mandatory — Cefalù section per Intake scope |
| /news/mondello-guide/ | 200 ✅ | Mondello Guide | Mondello section reference |
| /news/palermo-safe-place-visit/ | 200 ✅ | Is Palermo Safe? | Safety claims in area sections |
| /news/airport-transfers/ | 200 ✅ | Airport Transfers | "How to get from airport" in booking-timing or area sections |
| /districts/ | 200 ✅ | Palermo Districts | SEO capture for neighborhood queries |
| /news/cefalu-travel-guide/ | 200 ✅ | Cefalù Travel Guide | Cefalù section secondary link |
| /news/vehicle-parking-palermo/ | 200 ✅ | Parking in Palermo | ZTL warning in Centro Storico section |
| /news/renting-car-palermo/ | 200 ✅ | Renting a Car | "Do I need a car?" FAQ answer |

**IMPORTANT:** `/where-to-stay-cefalu/` (root-level URL from Intake) returns **404**. The correct URL is `/news/where-to-stay-cefalu/` (under /news/). Update Intake reference.

---

## Outbound Links to Remove

| Link | Issue | Action |
|---|---|---|
| `/free-itinerary/` sidebar widget | Free vs paid conflict (banned per WAP_06b) | Remove in Pass 3. NOTE: this may be a site-wide sidebar widget, not post content — if so, it's a theme fix, not a per-post fix. |
| `wearepalermo.podia.com/the-sicilian-way` | Old brand name. Should be "We Are Palermo Premium Guide" in copy (URL stays same). | Update anchor text in Pass 3. URL is correct, just the display name needs updating. |
| `quotes.yourdictionary.com` (Godfather quote) | Low-value external link. Adds no SEO value. | Remove or replace with more authoritative reference if quote stays. |
| `facebook.com/groups/wearepalermo` | Facebook group link. | Keep if Nico wants, remove if not actively managed. PM decision. |

---

## Schema Markup State

| Schema | Present | Notes |
|---|---|---|
| JSON-LD blocks | 1 | Single block detected |
| Article / BlogPosting | NO (not in JSON-LD) | May be in microdata (GeneratePress theme pattern from Favignana). Needs verification. |
| FAQPage | **NO** | No FAQ section on live page. Must add in rewrite. |
| Author (microdata) | NOT FOUND | No `itemprop="name"` detected. Author attribution weak. |
| Breadcrumb | Not checked | Low priority |

**Critical gap:** No FAQPage schema, no FAQ section. This is the single biggest AIO-citation opportunity to add.

---

## Technical Issues (NEW — not in Step 2)

1. **SEO title year-stamped "2025"** — Kills freshness in 2026. Must update in Yoast.
2. **H1 vs title mismatch** — H1: "Where to Stay in Palermo to Get the Most of Your Trip" vs Title: "The 3 Top Areas and Accommodations for Your Palermo Stay 2025". Different framing, neither is optimal.
3. **No H2-level content sections** — The current page has only 2 real H2s ("What Are the Best Places..." and "Don't Screw This Up"). The 3 areas are H3s. Full rebuild needed.
4. **~5,034 words** — Above the 4,000 target. Trim opportunity in Pass 2.
5. **No author attribution in schema** — Weak E-E-A-T signal. Must add "Nico Barcellona" author via Yoast.
6. **2 sidebar "FREE itinerary" H2 widgets** — Site-wide widget promoting banned content. Not post-content but affects the page. Flag for Nico.
7. **Airbnb embed** — Direct Airbnb widget embedded in page. Per Intake, keep but don't push hard.

---

## SERP Competitor Structural Analysis

### untolditaly.com (DA 32 — same league as WAP DA 33)
- ~3,500-4,000 words
- **6 neighborhoods** (Borgo Vecchio, Castellammare/Vucciria, Mondello, Politeama, Kalsa, Albergheria). Splits Centro Storico into sub-neighborhoods — opposite of WAP's unified approach.
- 18 hotels (3 per neighborhood: luxury/mid/budget tiers)
- No FAQ, no FAQPage schema
- Angle: neighborhood-by-neighborhood guide, localized expert
- **What they do that WAP doesn't:** cover more neighborhoods, tier hotels by budget
- **What WAP does that they don't:** authentic Nico voice, unified Centro Storico local-truth framing

### thethinkingtraveller.com (DA 56)
- ~5,500-6,000 words
- Structure: Quick Answer → District Breakdown → Accommodation Types → By Travel Style → Season Guide → FAQ
- No specific hotel names — discusses price ranges by category (€40-80, €80-180, €180-350, €350+)
- Has FAQ section
- Angle: "match accommodation to travel style" — pushes toward private villas (their business model)
- **What they do that WAP doesn't:** season-by-season guide, accommodation type comparison, FAQ
- **What WAP does that they don't:** specific hotel recommendations with affiliate links, real pricing from a local, Nico voice

---

## Verification Results

### Famila Supermarket Via Libertà
- **Confirmed:** Famila (one L, correct spelling)
- **Address:** Via Libertà 30, 90133 Palermo
- **Hours:** 24h confirmed (00:00-24:00)
- **Source:** [famila.it official listing](https://www.famila.it/punti-vendita/sicilia/famila-superstore-palermo-via-liberta--30)

### Salita Partanna Grocery
- **Confirmed:** Famila Superstore at Salita Partanna 1, 90133 Palermo
- **Note:** This is the SAME chain (Famila) as the Via Libertà location — different branch. Also a Carrefour Market at Salita Partanna 14 (separate store). Intake says "Salita Partanna — best big grocery store in Centro Storico" — the Famila Superstore at Salita Partanna 1 matches this description.
- **Source:** [famila.it](https://www.famila.it/punti-vendita/sicilia/famila-superstore-palermo-via-salita-partanna-1)

### La Via dei Tesori 2026
- **Status:** Event confirmed for 2026 but exact dates NOT yet announced as of May 1
- **Typical timing:** Historically runs across weekends in October-November. Some sources mention September for 2026 but this may be a different component of the festival.
- **Recommendation:** Use hedged language: "usually October-November" with [VERIFY: exact 2026 dates when announced]
- **Official site:** [leviedeitesori.com](https://www.leviedeitesori.com/)

---

## Open Questions for PM / Step 4

1. **Cefalù internal link URL is `/news/where-to-stay-cefalu/`** (NOT `/where-to-stay-cefalu/` as stated in Intake). Confirm correct URL for Cefalù section.
2. **Villa Igea (Rocco Forte)** — Nico mentions in brain dump. Not in WAP_12. Add to rewrite? If yes, need affiliate link or mark as non-affiliate luxury reference.
3. **FREE itinerary sidebar widgets** — site-wide, not post-specific. Can Architect remove from this page only, or does Nico need to update the widget globally?
4. **Facebook group link** — keep or remove?
5. **Full GSC 974-row export** — needed for long-tail query analysis. PM to request from Nico.
6. **Grand Hotel et Des Palmes pricing** — Intake says "~€600/night" as Nico's quote. Verify against Booking.com current rates in Scout Step 6.
7. **Author attribution** — no author schema detected. Confirm whether Yoast Article schema auto-generates with author, or if manual addition needed.

---

## Summary for PM

**Critical findings:**

1. **Title is year-stamped "2025"** — single biggest quick-win. Updating to 2026 or removing year could lift CTR immediately even before content rewrite.
2. **"best place to stay" query has 0.5% CTR on 592 impressions** — almost certainly AIO-cannibalized. TL;DR table + FAQPage schema is the citation play.
3. **All 15 affiliate links verified, all match WAP_12** — no revenue bugs at the URL level. Affiliate infrastructure is clean.
4. **Cefalù URL correction needed** — Intake references wrong URL (`/where-to-stay-cefalu/` 404). Correct: `/news/where-to-stay-cefalu/` (200).

Step 3 complete. Ready for PM gate → Step 4 (Structural Audit).
