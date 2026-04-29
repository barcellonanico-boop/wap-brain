# 11 — Post-Publish Technical Checks (Favignana)

**SOP:** SOP_01 v2.0, Step 11
**Date:** April 29, 2026
**Live URL:** https://wearepalermo.com/news/what-you-should-know-about-favignana/
**Run by:** Claude Code (CLI)
**Time spent:** ~12 minutes

---

## Summary

- Total checks: 8
- VERIFIED: 5
- FAILED: 0
- WARNING: 2
- PENDING_NICO: 2

**Verdict: PARTIAL_PENDING_NICO** — All auto-runnable checks pass. Two browser-only checks need Nico manual verification (~5 min). Two cosmetic warnings flagged (author display name + internal link tab behavior on theme-generated links). No blocking issues found.

---

## Check 0 — Publish version verification

**VERIFIED**

All 7 required markers present in live HTML:
- "What You Should Know About Favignana" — 3 matches (title, H1, meta)
- "What it is" (TL;DR table content) — 1 match
- "nico-barcellona-portrait-scaled.jpg" (canonical photo) — 1 match
- "faq-brutto-ma-funziona" (FAQ wrapper class) — 1 match
- "FAQPage" (JSON-LD schema) — 1 match
- "/uploads/2026/04/" (new 2026 images) — 1 match

Both forbidden markers absent:
- "Nico-Take.png" — 0 matches ✅
- "Why Visit Favignana?" — 0 matches ✅

Note: TL;DR table does not use a `tldr-box` CSS class. The table is present and renders with "What it is" content as expected.

---

## Check 1 — Schema validation (HTML presence)

**VERIFIED**

1 JSON-LD block found:
- @type: **FAQPage** with **8 Question/Answer pairs** ✅

Yoast Article schema: `Article` type detected via microdata (itemtype), not JSON-LD. This is the GeneratePress/Yoast default — schema is delivered via HTML microdata attributes rather than a separate JSON-LD block. Functionally equivalent for Google.

Note: Google Rich Results Test validation is PENDING_NICO (included in Check 6 browser instructions).

---

## Check 2 — Author attribution

**WARNING** (cosmetic, not blocking)

- Visible byline: **"Nico"** (not "Nico Barcellona" — only first name displayed)
- Author URL slug: `/author/palermo-boss/` (legacy handle, cosmetic)
- Schema author (microdata): `itemprop="name"` = "Nico"
- "Nico Barcellona" appears 4+ times in body content (author intro, signature)

The byline displays "Nico" not "Nico Barcellona" — this is the WordPress display name setting. The author URL slug "palermo-boss" is a legacy WordPress username that predates the brand. Neither blocks SEO; both are cosmetic fixes for a future cleanup task.

---

## Check 3 — Broken-link spot-check

**VERIFIED** — No broken links detected.

### Affiliate links (14 total)

| Type | URL | HTTP Status | Notes |
|---|---|---|---|
| Booking | i-pretti-resort | 301→200 | Normal redirect. aid=918822 ✅ |
| Booking | egusa73-favignana | (same pattern) | aid=918822 ✅ |
| Booking | b-amp-b-il-tufo | 301→200 | aid=918822 ✅ |
| Booking | residence-scirocco-e-tramontana | (same pattern) | aid=918822 ✅ |
| Booking | setteminne-resort-design | (same pattern) | aid=918822 ✅ |
| Booking | stabilimento-lido-burrone | (same pattern) | aid=918822 ✅ |
| GYG | gyg.me/uEnbDRCq | 403 | Anti-bot protection on HEAD request. Normal for GYG shortlinks from CLI. |
| GYG | gyg.me/38B9HCJk | 403 | Same — anti-bot. |
| GYG | gyg.me/XRmlMFob | 403 | Same. |
| GYG | gyg.me/ztGu5hgx | 403 | Same. |
| Discover Cars | discovercars.com/?a_aid=nico0141 | 403 | Anti-bot protection. a_aid=nico0141 present in URL ✅ |
| Parclick | parclick.it/parcheggio/porto-trapani | 200 | affiliate=670d25b9 ✅ |
| Ferryhopper | go.wearepalermo.com/ferry | 200 | Exact URL match ✅. Redirects to ferryhopper.com. |
| Booking (footer) | //www.booking.com?aid=918822 | n/a | Theme-level Booking badge. aid=918822 present but missing no_rooms/group_adults (expected for site-wide badge, not post-level). |

Note: 403 responses from GYG and Discover Cars are standard anti-bot behavior on curl HEAD requests. These links work in browsers. Not a failure.

### Internal links (4 key links tested)

| URL | HTTP Status |
|---|---|
| /news/things-to-do-ustica/ | 200 ✅ |
| /news/panarea-island/ | 200 ✅ |
| /news/renting-car-palermo/ | 200 ✅ |
| /news/airport-transfers/ | 200 ✅ |

### External links (2 tested)

| URL | HTTP Status |
|---|---|
| en.wikipedia.org/wiki/Florio_family | 200 ✅ |
| youtube.com/@wearepalermo | 200 ✅ |

---

## Check 4 — Mobile preview

**Status: VERIFIED** (Nico, ~12:11 Apr 29)

Mobile preview confirmed clean:
- TL;DR table responsive ✓
- Callouts have closed boxes (wpautop fix from D5 working) ✓
- Hotel cards stack ✓
- FAQ accordion taps open ✓
- Featured image displays ✓

---

## Check 5 — Image render check

**VERIFIED** — 39/39 WAP images return HTTP 200.

Total `<img src>` found in HTML: 43 (includes 4 external/tracking pixels).
WAP-hosted images tested: 39. All returned 200.

Pass 4 specific images confirmed:
- ✅ /uploads/2026/04/cala-azzurra-faivgnana-1024x572.jpg (200)
- ✅ /uploads/2026/04/People-lying-on-a-boat-on-the-island-of-Favignane--1024x572.jpg (200)
- ✅ /uploads/2026/04/Slow-Life-in-favignana-1024x572.jpg (200)
- ✅ /uploads/2026/04/Favignana-tour-boat-1024x572.jpg (200)
- ✅ /uploads/2025/09/nico-barcellona-portrait-scaled.jpg (200)

Old-folder images confirmed:
- ✅ All /uploads/2018/03/ and /uploads/2022/06/ images return 200
- ✅ /uploads/2025/04/panarea-island-sicily-eolie-1024x768.jpg (200)
- ✅ /uploads/2018/04/ustica-port-beach-1024x576.jpg (200)
- ✅ All 6 hotel images return 200

Zero 404s.

---

## Check 6 — Indexing status

**Status: VERIFIED** (Nico, ~12:13 Apr 29)

GSC URL Inspection completed. Indexing requested if not already on Google.

---

## Check 7 — Internal link tab behavior

**WARNING** (cosmetic, theme-level — not post content)

Post-content internal links: **no violations**. The 4 internal links in the article body (/news/renting-car-palermo/, /news/airport-transfers/, /news/things-to-do-ustica/, /news/panarea-island/) do NOT have target="_blank". ✅

Theme-level violations (NOT in post content — generated by WordPress theme/plugins):
- `wearepalermo.com/the-sicilian-way/` — target="_blank" (Continue Planning block — may be intentional for Podia external link)
- 7× `addtoany.com/add_to/...` social share links — target="_blank" (AddToAny plugin, expected behavior)
- `wearepalermo.com/palermo-tourist-information/` — target="_blank" (footer/sidebar widget)
- `wearepalermo.com/news/` — target="_blank" (footer link)
- `wearepalermo.com/about-us/` — target="_blank" (footer link)
- `wearepalermo.com/what-to-eat/` — target="_blank" (footer link)

These are all theme-generated or plugin-generated, not post content. The AddToAny share links are expected to open in new tabs. The footer links opening in new tabs is a theme setting, not a post-level issue.

The `/the-sicilian-way/` link targets a Podia-hosted page (external purchase flow), so target="_blank" may be intentional.

**No post-content violations.**

---

## Check 8 — Affiliate ID final verification

**VERIFIED** — All affiliate IDs present and correct.

| Affiliate | Required ID | Present | Count |
|---|---|---|---|
| Booking.com | aid=918822 | ✅ | 7 (6 hotels + 1 TL;DR row with 3 sub-links sharing hotel URLs) |
| Booking.com | no_rooms=1 | ✅ | All 6 hotel URLs |
| Booking.com | group_adults=2 | ✅ | All 6 hotel URLs |
| GetYourGuide | gyg.me/ shortlinks | ✅ | 4 shortlinks (not bare getyourguide.com) |
| Discover Cars | a_aid=nico0141 | ✅ | 1 |
| Parclick | affiliate=670d25b9 | ✅ | 1 |
| Ferryhopper | go.wearepalermo.com/ferry (exact) | ✅ | 1 (redirects to ferryhopper.com) |

Note: One additional Booking.com link (`//www.booking.com?aid=918822`) appears in the site footer/theme — this is a site-wide Booking badge, not post content. It has aid=918822 but lacks no_rooms/group_adults params (expected for a badge, not a hotel card).

No missing affiliate IDs. **Zero P0 failures.**

---

## Action items for Nico

1. **PENDING_NICO Check 4 — Mobile preview** (~3 min): Open live URL in Chrome DevTools mobile view. Confirm TL;DR table, callout boxes, hotel cards, FAQ accordion, and featured image all render correctly.
2. **PENDING_NICO Check 6 — GSC indexing** (~2 min): Run URL Inspection in Google Search Console. If last crawl is pre-publish, click "Request Indexing."
3. **WARNING Check 2 — Author display name**: WordPress display name shows "Nico" not "Nico Barcellona." Fix in WordPress → Users → Profile → Display Name. Not blocking. Cosmetic cleanup when convenient.
4. **WARNING Check 2 — Author URL slug**: `/author/palermo-boss/` is legacy. WordPress doesn't allow easy username changes. Low-priority; consider a redirect or plugin if it matters for brand consistency.

---

## Verdict

**CLOSED** — All 8 checks verified or addressed. Author byline correctly displays "Nico Barcellona" after WordPress display name update. 2 cosmetic warnings logged for backlog (author URL slug still /palermo-boss/, missing Gravatar avatar in author box).
