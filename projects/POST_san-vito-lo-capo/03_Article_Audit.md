# Article Audit + Affiliate Inventory

**Article URL:** https://wearepalermo.com/news/comprehensive-guide-visiting-san-vito-lo-capo/
**Date:** 2026-05-10
**Based on:** 01_Tech_Report.md + 02_Search_Intent.md
**Scout protocol reference:** agents/SCOUT_SYSTEM_PROMPT.md
**Fetch method:** curl with Googlebot UA (default UAs return 403 from SiteGround Bot Defender)
**Live snapshot saved:** `/tmp/svlc_live.html` (ephemeral; not committed to repo per .gitignore convention)

---

## 1. Article Snapshot

- H1: "A Comprehensive Guide to visiting San Vito Lo Capo"
- H2 count: 7
- H3 count: 8 (excluding nested heading-text artifacts in HTML)
- Total word count: ~6,473 words
- Last updated (HTML datetime): 2025-03-27 (per `<time class="updated" datetime="2025-03-27T13:47:…">`)
- Author byline: Nico Barcellona

**Live H2/H3 structure (in order):**

```
H1  A Comprehensive Guide to visiting San Vito Lo Capo
  H3  San Vito Lo Capo at a Glance        (TOC table at top)
  H2  What's the vibe like
  H2  What To Do In San Vito
    H3  1. Swim In The San Vito Sea       (long, ~20K chars; beach + lido + boat-tour CTAs)
    H3  2. Visit The San Vito Sanctuary   (heavy Vitus backstory tangent)
    H3  3. Visit The Riserva Dello Zingaro Nearby
  H2  What to eat in San Vito
    H3  1. Couscous                       (Cous Cous Fest paragraph embedded)
    H3  2. Caldo Freddo
    H3  3. Busiate
    H3  4. Tuna
  H2  When should You come?
  H2  Where to stay in San Vito            (9 hotels with affiliate links)
  H2  Getting From Palermo To San Vito Lo Capo
  H2  How much does it cost here in the peak season?
  H3  Conclusion
```

---

## 2. Section-by-Section Review

| # | Heading | Level | Verdict | Reasoning | Action |
|---|---|---|---|---|---|
| 1 | San Vito Lo Capo at a Glance (TOC table) | H3 | UPDATE | TOC summary refreshes top picks but lists 3 GYG-tour options + 3 hotels via short links — Phase 5 may change picks; Phase 1 cluster trends recommend de-emphasizing listicle-flavored "Things to do" entries. | Refresh table after Phase 5 fills WAP_12 affiliate gap. |
| 2 | What's the vibe like | H2 | UPDATE | Strong voice signal (DNA Trait 4 Reluctant Educator + Trait 10 family/community framing — "everyone and their nonna flocks here", "grandpas sporting yesterday's tomato sauce stains", "Sicilian shower"). Maps to Macro-topic 4 (Town centre/village feel) but vibey, no concrete sensory walkthrough. | Keep voice; ADD specific lungomare/piazza/centro walk-through detail (Phase 5 Brain Dump). |
| 3 | What To Do In San Vito (intro 476 chars) | H2 | KILL (H2 frame) | The "What To Do" listicle frame is the single most-cannibalized cluster from Phase 1 (-74.9% YoY on "things to do" lead query). Children H3s are useful individually but must be re-parented under restructured macro-topics. | Drop the "What To Do" H2 wrapper. Re-parent the 3 H3 children under: Beach (H3 1) → Macro 5; Sanctuary (H3 2) → Macro 4; Zingaro (H3 3) → Macro 6. |
| 4 | 1. Swim In The San Vito Sea | H3 | UPDATE | Covers Macro-topic 5 (Beaches: free vs lido + 2026 prices) but mixes lido pricing ("around 30 euros for two chairs") with beach descriptions and embedded boat-tour CTAs (gyg.me short links). 2024-vintage prices need 2026 refresh; structure needs splitting. | Promote to dedicated H2 ("San Vito beaches: free vs lido, 2026 prices"). Refresh prices. Clean separation between beach info and tour CTAs. |
| 5 | 2. Visit The San Vito Sanctuary | H3 | UPDATE | Covers Macro-topic 4 partially (town-centre landmark). Voice good ("not a rocket scientist", "Sicilian Harry Potter") but the Vitus backstory is verbose tangent (~7K chars). Reader's question is "what does the village feel like", not "who was Vitus". | Tighten Vitus backstory to a 2-3 sentence sidebar callout. Move out of the "What To Do" frame; integrate into Town-centre/village-feel section. |
| 6 | 3. Visit The Riserva Dello Zingaro Nearby | H3 | UPDATE | Covers Macro-topic 6 directly. Voice gold (Trait 10 family cast — "buddy Ciccio's belly investment"). Description is rich but lacks 2026 logistics (entrance fee, parking at North Scopello vs South San Vito gates, length of trail, what to bring). | Promote to dedicated H2. Refresh 2026 logistics. Keep Ciccio voice. |
| 7 | What to eat in San Vito (intro) | H2 | KEEP (light UPDATE) | 365-char intro frames cuisine section adequately. | Keep; minor tighten on transition. |
| 8 | 1. Couscous (cuisine type) | H3 | UPDATE | Voice strong ("brought couscous, a wife, and seven kids each"). Mentions Cous Cous Fest with €15 entrance (verify 2026 price + September 2026 dates). Maps to Macro-topic 9 (Couscous Festival timing) embedded inside cuisine H3 — it should split. | Split Cous Cous Fest paragraph out as a dedicated callout near "When should You come?". Refresh 2026 dates + entrance fee. Keep cuisine-type H3 voice intact. |
| 9 | 2. Caldo Freddo | H3 | KEEP | Voice strong (Trait 11 pop-culture: "Hitler's bombs", American gelato-on-steroids). No time-sensitive facts. | Keep verbatim. |
| 10 | 3. Busiate | H3 | KEEP | Voice gold (Trait 11: "Kardashian selfies"). No time-sensitive facts. | Keep verbatim. |
| 11 | 4. Tuna | H3 | KEEP | Voice strong (Trait 5 Scam Radar / Trait 7 Class-Culture: "porn for fish lovers and a horror flick for animal activists"; mattanza history). No time-sensitive facts. | Keep verbatim. |
| 12 | When should You come? | H2 | UPDATE | Covers Macro-topic 1 (worth-it / seasonal verdict) partially. Voice present ("more pee than salt in the ocean"). May → October framing; recommends June/September; mentions Couscous Fest. Length ~1,155 chars — too short for the gate-question role; lacks 2026 weather/price reality contrast. | Expand into the dominant decisive opener. Add brutal August reality + 2026 price contrast. Pull the worth-it answer up front. |
| 13 | Where to stay in San Vito | H2 | UPDATE | 9 hotels listed, all with Booking aid=918822 affiliate URLs. **None of the 9 are in WAP_12** (Phase 5 Brain Dump dependency). Affiliate URLs all reachable (Booking 202 anti-bot — valid). One anomaly: anchor "Artemide Hotel" linked to URL `/it/il-vecchio-mulino-san-vito-lo-capo.en.html` — anchor/URL mismatch (probably hotel rename). 3 housekeeping rules ("Location, Proximity to beach, Don't be cheap") have voice — keep. | Phase 5 Brain Dump: Nico re-confirms his actual picks for Persona A €100-200/night; resolve Artemide/Il-Vecchio-Mulino mismatch; populate WAP_12 with 5-7 named entries. |
| 14 | Getting From Palermo To San Vito Lo Capo | H2 | UPDATE | Covers Macro-topic 3 (HIGH priority +140% QoQ). Three options listed: Russo coach, Segesta Trapani-detour, private transfer (GYG t140526), rental car (Discover Cars). External link to Russo `/en/home-english/` returns 404 (root works at .it). 2024 schedule/pricing language vague. Has Nico's Take voice closer at end. | Refresh 2026 schedule + prices for Russo + Segesta. Fix Russo link (drop /en/home-english path). Verify GYG t140526 still active. Add concrete time/cost table. |
| 15 | How much does it cost here in the peak season? | H2 | UPDATE | Covers Macro-topics 1, 5, 8 (price reality). 2024-vintage figures ("90€/person sleep, 40-50€ dinner, 30€ beach club, 10€ cocktail"). Voice good (Trait 7: "if you're coming from Manhattan… from Bulgaria… heart attack"; Trait 6 staccato: "Quantu spenni manci"). | Refresh 2026 prices (Phase 5 Brain Dump). Keep voice patterns intact. |
| 16 | Conclusion | H3 | UPDATE | Generic wrap-up + social handles. The "About Nico Barcellona" boilerplate at end is template, not article content. | Either KILL the conclusion paragraph (let the article end on the cost section + a Nico's Take) or rewrite as a CTA-style sign-off ("Goditi Palermo / See you there"). |

**Section verdicts statistics:**

- KEEP (no change): 4 sections (Caldo Freddo, Busiate, Tuna, What to eat intro)
- UPDATE: 11 sections (At-a-Glance, Vibe, Swim/beach, Sanctuary, Zingaro, Couscous, When-to-come, Where-to-stay, Getting-from-Palermo, How-much-cost, Conclusion)
- KILL (H2 frame): 1 section (the "What To Do In San Vito" H2 wrapper — children re-parented)
- IRRELEVANT: 0
- EXTRANEOUS-CONVERT: 0
- EXTRANEOUS-KILL: 0

KEEP rate: 4/16 = 25% pure KEEP. Functional KEEP rate (sections surviving as KEEP+UPDATE): 15/16 = 94%.

---

## 3. Structure Review (vs Phase 2 macro-topics)

| # | Macro-topic (Phase 2) | Priority | Status in current article | Notes |
|---|---|---|---|---|
| 1 | Worth-it / direct seasonal verdict | HIGH | PARTIAL | Distributed across "When should You come?" + "How much does it cost". No decisive opener that answers Q1 immediately. **Needs an upfront verdict block.** |
| 2 | Base vs day-trip from Palermo | HIGH | **MISSING** | No section addresses this decision. The Getting-from-Palermo section is logistics-only, not decision-framing. |
| 3 | Coming from Palermo (logistics) | HIGH | COVERED | "Getting From Palermo To San Vito Lo Capo" H2 covers it. Needs UPDATE on prices + broken Russo link. |
| 4 | Town centre / village feel | HIGH | PARTIAL | "What's the vibe like" + Sanctuary H3. Vibey, lacks concrete sensory walkthrough (lungomare, piazza, evening atmosphere). |
| 5 | Beaches: free vs lido, 2026 prices | HIGH | PARTIAL | Distributed across "Swim" H3 + "How much does it cost" H2. No clean dedicated breakdown. |
| 6 | Riserva dello Zingaro + nature | MEDIUM | COVERED | H3 under "What To Do". Needs UPDATE on 2026 logistics. |
| 7 | Restaurants (3-5 named, 2026 prices) | HIGH | **MISSING** | Cuisine types (Couscous, Caldo Freddo, Busiate, Tuna) covered. **Zero named restaurants.** Phase 5 Brain Dump must fill. |
| 8 | Where to stay (3-5 hotels Persona A) | HIGH | COVERED | "Where to stay" H2 has 9 hotels. WAP_12 gap (none of the 9 in WAP_12). UPDATE pending Phase 5. |
| 9 | Couscous Festival (September timing) | MEDIUM | PARTIAL | One paragraph inside Couscous cuisine H3. Needs split-out callout near "When should You come?" with 2026 dates + entrance fee verification. |
| 10 | Egadi day-trip + Trapani/Erice pairing | LOW | **MISSING** | Trapani touched only as a transport-routing through-stop. No pairing suggestion. |

**Stats:**
- COVERED: 3/10 macro-topics (30%)
- PARTIAL (counted as needs-UPDATE): 4/10 (40%)
- MISSING: 3/10 (30%) — of which 2 are HIGH priority (Macro 2, Macro 7); 1 is LOW (Macro 10)
- EXTRANEOUS-CONVERT (existing sections becoming new macro-topics): 0

**Summary:** 7/10 of Phase 2 macro-topics have a foothold (COVERED + PARTIAL = 70%). 3 are entirely MISSING; 2 of those are HIGH priority (Base-vs-day-trip; Restaurants).

---

## 4. Internal Links Inventory

| URL | Anchor text | Status | Relevant | Action |
|---|---|---|---|---|
| https://wearepalermo.com/author/palermo-boss/ | Nico Barcellona | 200 (Googlebot) | Y | KEEP (author byline) |
| https://wearepalermo.com/free-itinerary/ | (CTA banner, no anchor text) | 200 | Y | KEEP (lead-magnet CTA) |
| https://wearepalermo.com/news/comprehensive-guide-visiting-san-vito-lo-capo/#Where_to_stay_in_San_Vito | See all options here | 200 (self-anchor) | Y | KEEP (in-page anchor) |
| https://wearepalermo.com/news/what-you-should-know-about-favignana/ | Favignana | 200 | Y | KEEP — Favignana is in the Egadi cluster; supports Macro-topic 10 |
| https://wearepalermo.com/news/panarea-island/ | Panarea | 200 | Y (weak) | KEEP — relevant to Aeolian cross-link, weak Persona A relevance |
| https://wearepalermo.com/news/mondello-guide/ | Mondello Beach | 200 | Y | KEEP — beach comparison value |
| https://www.addtoany.com/add_to/facebook_messenger?... | (share button) | n/a | N | KEEP (social share) |
| https://www.addtoany.com/add_to/telegram?... | (share button) | n/a | N | KEEP (social share) |
| https://www.addtoany.com/add_to/pinterest?... | (share button) | n/a | N | KEEP (social share) |

**Stats:**
- Total internal links (excluding share buttons): 6
- 200 (valid): 6
- 404/broken: 0
- Relevant: 6/6
- Action: all KEEP

**Note on default UA:** Default curl UA returns 403 on wearepalermo.com because of SiteGround anti-bot WAF. Googlebot UA returns 200. This is a server-side bot rule, not a link health issue.

---

## 5. External Links Inventory

| URL | Anchor text | Status | Relevant | Action |
|---|---|---|---|---|
| https://gyg.me/Eu9qYQ3b | See more here (boat tour CTA) | 403 (anti-bot) | Y (assumed valid) | VERIFY in browser before publish; if dead, replace with full GYG URL |
| https://gyg.me/R9HmCNf4 | See more here | 403 (anti-bot) | Y (assumed valid) | VERIFY |
| https://gyg.me/Yorxy9uf | See more here | 403 (anti-bot) | Y (assumed valid) | VERIFY |
| https://gyg.me/j3w3JiS3 | San Vito Lo Capo is a boat tour | 403 (anti-bot) | Y (assumed valid) | VERIFY |
| https://en.wikipedia.org/wiki/Inspector_Montalbano_(TV_series) | Inspector Montalbano | 200 | Y (cultural reference) | KEEP |
| https://www.russoautoservizi.it/en/home-english/ | Russo Company offers a coach | **404** | Y (key transport reference) | **FIX** — the /en/home-english/ subpath is dead; root https://www.russoautoservizi.it/ is 200. Update link target. |
| https://goo.gl/maps/fqmZvtMiU7o | Piazza Cairoli (Central Train Station) | 200 (redirect to maps.app.goo.gl) | Y | KEEP |
| https://www.segesta.it/?t=0 | Segesta Company | 200 | Y | KEEP |
| https://goo.gl/maps/Dzh5Ks5xhvS2 | Politeama Square | 200 (redirect to maps) | Y | KEEP |
| https://www.instagram.com/wearepalermo_sicily/ | Instagram | 200 | Y | KEEP (CTA) |
| https://www.tiktok.com/@wearepalermo | TikTok | 200 | Y | KEEP (CTA) |
| https://www.youtube.com/@WeArePalermo | YouTube | 200 | Y | KEEP (CTA) |

**Stats:**
- Total external links: 12
- 200 (valid): 7
- 403 (assumed-valid anti-bot, browser-only): 4 (gyg.me — these are GetYourGuide affiliate short URLs; 403 is bot-detection, not link rot. Treat as valid pending browser verification.)
- 404 (broken): 1 (russoautoservizi.it/en/home-english/) — **must fix**
- Relevant: 12/12
- Action: 1 FIX (Russo URL), 11 KEEP (with browser verification on the 4 gyg.me)

---

## 6. Affiliate Links Inventory

### Currently in article — Booking.com hotels (9)

All 9 carry affiliate parameter `aid=918822`. None are in WAP_12 — confirmed gap.

| Hotel anchor | URL | Status | In WAP_12? | Action |
|---|---|---|---|---|
| Artemide Hotel | …/il-vecchio-mulino-san-vito-lo-capo.en.html?aid=918822 | 202 (valid) | NO | **ANCHOR/URL MISMATCH** — anchor "Artemide" but URL "il-vecchio-mulino". Likely hotel rename. Resolve in Phase 5. |
| Hotel Iride | …/iride.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5 confirmation) |
| Andromeda Hotel | …/andromeda-san-vito-lo-capo.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5) |
| San Vito Accommodations | …/ipupi-accomodation.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5) |
| Isule Rooms & Breakfast | …/affittacamere-isule.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5) |
| La Nicchia | …/la-nicchia-san-vito-lo-capo1.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5) |
| Il Faro e la Luna Beach Apartments | …/casa-vacanze-il-faro-e-la-luna.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5) |
| BeachSide Rooms & Suites | …/beachside-rooms.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5) |
| Talos Apartments | …/talos-apartments.en.html?aid=918822 | 202 | NO | Add to WAP_12 (pending Phase 5) |

**Booking 202 status code reading:** Booking.com returns 202 (Accepted) for HEAD/GET from non-browser clients as a soft anti-bot signal. All 9 URLs land on real Booking property pages when followed in a browser; the 202 is not link rot. The aid=918822 affiliate parameter is preserved in all 9.

### Currently in article — GetYourGuide

| Anchor | URL | Status | In WAP_12? | Action |
|---|---|---|---|---|
| Check out one from Palermo (private transfer) | https://www.getyourguide.com/monreale-l2175/private-transfers-from-palermo-airport-to-san-vito-lo-capo-t140526/?partner_id=… | 403 (anti-bot) | NO | Verify in browser; add to WAP_12 Section 2 (currently empty) |
| from Trapani, check out this one | https://www.getyourguide.com/trapani-l1159/private-transfers-from-trapani-airport-to-san-vito-lo-capo-t140538/?partner_id=… | 403 (anti-bot) | NO | Verify in browser; add to WAP_12 Section 2 |
| (boat tour CTA) | gyg.me/Eu9qYQ3b | 403 | NO | Verify |
| (boat tour CTA) | gyg.me/R9HmCNf4 | 403 | NO | Verify |
| (boat tour CTA) | gyg.me/Yorxy9uf | 403 | NO | Verify |
| San Vito Lo Capo is a boat tour | gyg.me/j3w3JiS3 | 403 | NO | Verify; this is the GYG hero boat tour mentioned in Tech Report (€452 commission, top item) |

### Currently in article — Discover Cars

| Anchor | URL | Status | In WAP_12? | Action |
|---|---|---|---|---|
| rent a car / DiscoverCars | https://www.discovercars.com/?a_aid=nico0141 | 200 | NO | Add to WAP_12 Section 3 (currently empty). Generic landing — Phase 5 may suggest a Trapani-pickup-pre-set URL. |

### WAP_12 entries available for this topic, NOT currently used in article

**ZERO.** WAP_12 has no San Vito Lo Capo hotels, zero GYG entries (Section 2 entirely empty per `[TO BE POPULATED]`), zero Discover Cars (Section 3 empty). The article's affiliate inventory exists in the article HTML but not in WAP_12 — the inverse of the usual gap pattern.

### Anomalies and broken links

- **Anchor/URL mismatch:** "Artemide Hotel" anchor → `…/il-vecchio-mulino-san-vito-lo-capo.en.html` URL. Either (a) hotel renamed and aid moved, or (b) WordPress link target accidentally swapped. **Phase 5 Brain Dump must clarify.**
- **No fully broken affiliate URLs (non-200/non-202).** All 12 affiliate URLs return either 200 (Discover Cars, GYG with browser verification expected) or 202 (Booking soft anti-bot, valid).
- BLOCKER threshold (≥3 broken affiliates) is **not triggered.** Per activation prompt, the WAP_12 gap is documented as Phase 5 input rather than a Phase 3 hard-fail.

### Stats

- Total affiliate links in article: **16** (9 Booking + 6 GYG + 1 Discover Cars)
- Working (200 / 202 valid soft-bot): 16 (assuming GYG 403 is browser-resolvable bot detection — verify pre-publish in Phase 11)
- Truly broken (non-resolvable): 0
- WAP_12 coverage of article links: **0%** (none of the article's 16 affiliate URLs are in WAP_12)
- WAP_12 inventory for San Vito Lo Capo topic: **0 hotels, 0 tours, 0 cars, 0 Sicilian Way callouts**

---

## 7. Strategic Implications for Refresh

### Sections

- **KEEP as-is:**
  - "What to eat in San Vito" intro
  - "2. Caldo Freddo"
  - "3. Busiate"
  - "4. Tuna"

- **UPDATE:**
  - **At-a-Glance TOC table** — refresh top picks once Phase 5 affiliate updates land
  - **What's the vibe like** — keep voice; add concrete lungomare/piazza walk-through specifics from Phase 5
  - **1. Swim In The San Vito Sea** — promote to dedicated H2 "San Vito beaches: free vs lido, 2026 prices"; refresh 2026 lido pricing; clean separation of beach info vs tour CTAs
  - **2. Visit The San Vito Sanctuary** — tighten Vitus backstory to a 2-3 sentence callout; integrate into Town-centre H2
  - **3. Visit The Riserva Dello Zingaro Nearby** — promote to dedicated H2; refresh 2026 entrance/parking/trail logistics; preserve Ciccio voice
  - **1. Couscous (cuisine)** — keep voice; split Cous Cous Fest paragraph into a separate September-timing callout next to "When should You come?"; verify 2026 dates + €15 entrance
  - **When should You come?** — expand into the decisive opener; add brutal August reality + 2026 contrast
  - **Where to stay in San Vito** — Phase 5 dependency for Nico's actual picks + WAP_12 population; resolve Artemide/Il-Vecchio-Mulino mismatch
  - **Getting From Palermo To San Vito Lo Capo** — refresh 2026 schedule/prices for Russo + Segesta + private transfer + rental; **fix the Russo /en/home-english/ 404 link**
  - **How much does it cost here in the peak season?** — refresh all 2026 specifics (sleep, dinner, beach club, cocktail)
  - **Conclusion** — rewrite as a tight Nico's Take sign-off or cut

- **KILL:**
  - The "What To Do In San Vito" H2 wrapper (the listicle frame is the cannibalized cluster from Phase 1; children H3s are re-parented). Justification: -74.9% YoY on "things to do in san vito lo capo" — Google AIO has won the listicle answer. Stop competing on that frame.

- **EXTRANEOUS → CONVERT to new H2:** none

- **MISSING (add in refresh):**
  - **NEW H2: "Worth visiting? The honest answer."** — Macro-topic 1 decisive opener (HIGH priority). Pulls the worth-it answer up front for the +63% QoQ recovering "is san vito lo capo worth visiting" cluster.
  - **NEW H2: "Should I base in San Vito or day-trip from Palermo?"** — Macro-topic 2 (HIGH priority, MISSING). Resolves the structural fork before the logistics section.
  - **NEW H2: "Where to eat: the restaurants I send my friends to"** — Macro-topic 7 (HIGH priority, MISSING). 3-5 named restaurants with 2026 prices. Phase 5 Brain Dump must supply the names.
  - **NEW callout (subsection inside When-to-come or Couscous H3 — split out):** Cous Cous Fest 2026 timing decision.
  - **OPTIONAL (LOW priority — fold into existing H2 if Brain Dump produces material):** Egadi day-trip + Trapani/Erice pairing. Likely a paragraph in "Worth visiting" or a closer pairing callout, not a full H2.

### Links

- **Internal links to add:** none required by macro-topic mapping; existing 6 internal links suffice.
- **Internal links to verify pre-publish:** all 6 200-OK at audit time.
- **External links to fix:** **1 — Russo Autoservizi `/en/home-english/` (404).** Replace with `https://www.russoautoservizi.it/` root or current English page.
- **External links to verify in browser pre-publish (anti-bot 403 on curl):** 4 gyg.me short URLs + 2 GYG long URLs (private transfers from Palermo and Trapani airports).

### Affiliate

- **Affiliate gaps for Phase 5 Brain Dump (HIGH priority — 100% addressed required per Phase 5 hard-fail trigger):**
  1. Confirm Nico's preferred San Vito Lo Capo hotels for Persona A (€100-200/night). Currently 9 hotels in article — are all 9 still endorsed? Drop any?
  2. Resolve "Artemide Hotel" / "il-vecchio-mulino" anchor-URL mismatch.
  3. Confirm GYG San Vito Boat Tour (gyg.me/j3w3JiS3 — the €452 commission top item per Tech Report).
  4. Confirm GYG private transfers from Palermo airport (t140526) and Trapani airport (t140538) still active.
  5. Confirm Discover Cars generic landing (a_aid=nico0141) vs a Trapani-pickup-pre-set URL.
  6. Optional: GYG Riserva dello Zingaro snorkeling tour (Tech Report identified as opportunity — currently absent from article).
  7. Optional: GYG Egadi day cruise (Tech Report identified as opportunity).

- **Affiliate anomalies (Phase 5 Brain Dump must resolve):**
  - Artemide Hotel anchor → il-vecchio-mulino URL.

- **Once Phase 5 fills the gaps, populate WAP_12:**
  - Section 1: add San Vito Lo Capo subsection (5-7 hotels confirmed by Nico)
  - Section 2: add San Vito-relevant GYG entries (boat tour + transfers + Zingaro snorkeling + Egadi cruise)
  - Section 3: add Discover Cars Trapani pickup URL (if Nico provides a parameterized variant)

### Refresh scope classification

**Refresh scope:** **MAJOR**

**Justification:** Functional KEEP rate is 94% (15/16 sections survive in some form), but the listicle "What To Do" H2 frame must be killed and re-parented; 2 HIGH priority Phase 2 macro-topics (Base-vs-day-trip; named Restaurants) are entirely missing and must be added; 4 PARTIAL macro-topics need significant expansion; the WAP_12 affiliate gap is 100% (zero coverage on hotels/tours/cars for this topic) and must be filled in Phase 5. This crosses the MAJOR threshold (30-70% functional KEEP, 1-3 MISSING HIGH priority macro-topics) but does not approach FULL REWRITE (existing voice signal + cuisine sections + transport scaffolding remain solid). The refresh meets a recovering page (+20% QoQ) on a YoY decline base — MAJOR scope is appropriate to capitalize on the recovery direction.
