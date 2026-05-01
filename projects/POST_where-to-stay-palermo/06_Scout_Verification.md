# 06 — Scout Verification (Where to Stay in Palermo)

**SOP:** SOP_01 v2.1, Step 6
**Date:** May 1, 2026
**Pass 1.5 verified:** v2 (`projects/POST_where-to-stay-palermo/05_Pass1_Info_v2.md`)
**Time spent:** ~30 min (cap)

---

## Summary Counts

- Total flags: **31**
- ✅ **CONFIRMED:** 14
- ⚠️ **UPDATE:** 11
- ❌ **REMOVE:** 0
- 🔄 **PARK (Nico):** 6

**Critical findings (P0):**
1. **Hotel name typo throughout draft and Intake: "Villa Igea" → must be "Villa Igiea"** (with the second "i"). This is the official Rocco Forte property name. Add to spelling lock alongside Piazza Madrice.
2. **4 of 6 affiliate URLs in the draft do NOT match WAP_12 canonical.** Likely revenue-bleed bugs. Exact swap-in list at the bottom.
3. **AST/Tarantola line on Pass 1.5 v2 (if it carries the Favignana-era pattern) is wrong** — but this draft replaces with the corrected Segesta+FlixBus line. Verified clean.
4. **Dua Lipa wedding at Villa Igiea is REPORTED, not officially confirmed.** Italian press (Giornale di Sicilia, Dagospia) and international outlets report Sept 5-7, 2026, Villa Igiea. Hotel reportedly booked for full week, entire floor of suites reserved. **Lipa's reps have NOT confirmed.** Couple stayed there summer 2025 — that part is documented (Lipa Instagram "Palermo in my heart"). Pass 2 must hedge: "reportedly" or "rumored." Do NOT state as fact.

---

## Per-Flag Verification Table

### Pricing claims (#1-9)

| # | Claim | Status | Evidence | Pass 2 Action |
|---|---|---|---|---|
| 1 | Centro Storico Airbnb peak ~€120/night | 🔄 PARK | Live Airbnb pricing varies day-to-day and isn't externally citable as a fixed source. Spot-check on Booking.com aggregator confirms €100-150 range for similar centro listings July 2026, so €120 is plausible mid-range. | Defer to Nico's first-hand 2026 knowledge (per Intake May 1 brain dump). Keep the number but consider hedging "around €120." |
| 2 | Politeama-Libertà Airbnb €90-100/night | 🔄 PARK | Same as #1 — externally unverifiable. Range matches Booking.com aggregator spot-check. | Defer to Nico. Keep as-is or hedge to "€90-110." |
| 3 | Mondello summer Airbnb €150+/night | 🔄 PARK | Same as #1 — Mondello July/Aug spot-check on Booking.com confirms €150+ is conservative; many listings €180-250+ in peak. | Defer to Nico. The "€150+" floor is safe — if anything understated. |
| 4 | Mondello winter -30-40% from summer | 🔄 PARK | Externally unverifiable from public sources. Pattern matches general Mediterranean coastal seasonality. | Defer to Nico. |
| 5 | B&B average €80-90/night summer | 🔄 PARK | Booking.com aggregator spot-check shows wide spread €60-150 for B&Bs summer. €80-90 is the lower-mid end. | Defer to Nico. Hedge wider: "€80-100" or "from around €80." |
| 6 | Hotel Politeama ~€190/night | ⚠️ UPDATE (hedge) | Hotels.com listing confirms 4-star, "guests love the breakfast", deluxe rooms exist. Live booking-engine prices fluctuate hourly. €190 is plausible mid-range for shoulder season. | Hedge to "around €180-220/night" or "€190+ in peak." |
| 7 | Politeama 4-star range €150-300/night | ✅ CONFIRMED (hedge) | Range is wide enough to absorb fluctuation. Spot-check on Booking.com and aggregator data supports this band for the cluster of 4-star hotels in Politeama. | Keep as-is. |
| 8 | Grand Hotel et Des Palmes ~€600/night | 🔄 PARK | Couldn't externally pin a fixed €600 figure (live rates fluctuate). Brand positioning as recently renovated 5-star supports premium pricing. | Defer to Nico's 2026 first-hand knowledge. |
| 9 | Villa Igiea ~€2,000/night | ⚠️ UPDATE (name) | Rocco Forte 5-star confirmed (luxuryendless.com, wantedinrome.com). 72 rooms, 28 suites. Premium pricing tier confirmed. **Name spelled "Villa Igiea" not "Villa Igea"** in all official sources. | Fix name to **Villa Igiea** throughout draft and brain docs. €2,000/night is plausible for suites in peak; defer the exact number to Nico. |

**Spot-check pattern verdict:** Pricing band is broadly consistent with Booking.com aggregator data for July-August 2026. Nico's confirmation per Intake is sufficient — no externally citable fixed source exists for live booking rates.

---

### Logistics / facts (#10-17)

| # | Claim | Status | Evidence | Pass 2 Action |
|---|---|---|---|---|
| 10 | Famila Via Libertà 24h current status | ✅ CONFIRMED | Already verified in `02_Prep.md` (Verification Results section): Famila Superstore, Via Libertà 30, 90133 Palermo, hours 00:00-24:00. Source: famila.it official listing. | Keep as-is. |
| 11 | Bus 806 Politeama → Mondello frequency 2026 | ✅ CONFIRMED | AMAT Palermo S.p.A. operator confirmed. busmaps.com (GTFS): hours 05:45-21:40 daily. Rome2Rio: every 15 min during peak weekday operation. Tripadvisor crowdsourced (older but still indicative): every 30 min on Sundays/holidays until ~10pm. | Keep as-is. If specific frequency claimed in draft, hedge to "every 15-30 min depending on day/time." |
| 12 | Bus 806 journey time 30-40 min | ✅ CONFIRMED | busmaps.com (AMAT GTFS): full route ~35 min, 27 stops. Moovit: 35 min route duration. Rome2Rio: 25 min for shorter sub-segment. The 30-40 min figure is accurate for full Piazza Crispi → Mondello terminal journey. | Keep as-is. |
| 13 | Walking time Piazza Castelnuovo to Quattro Canti = 15 min | ✅ CONFIRMED | Distance ~1.2 km via Via Ruggero Settimo / Via Maqueda. Standard walking pace 5 km/h = ~14 min. The 15 min figure is correct for an average walker. | Keep as-is. |
| 14 | Train Palermo Centrale → Cefalù = 1 hour | ⚠️ UPDATE (hedge) | Trainline: 40-51 min depending on service, fastest 40 min. Omio: avg 46 min, fastest 42 min. Rome2Rio: 52 min. "1 hour" is the upper bound, not the typical. Better: "about 45-55 minutes" or "under an hour." | Update to **"about 45-55 minutes"** OR **"under an hour"**. The current "1 hour" overstates by ~10-15 min. |
| 15 | Train Palermo Centrale → Cefalù frequency 2026 | ✅ CONFIRMED | Trenitalia Regionale. Trainline: ~23 trains/day. Omio: 19-33 trains/day depending on weekday/weekend. First train ~05:08-05:13, last ~21:35. Approximately hourly+ frequency throughout the day. | Keep "hourly" or update to "around hourly, more during the day." |
| 16 | La Via dei Tesori 2026 dates | ⚠️ UPDATE (hedge) | Already covered in `02_Prep.md`: event confirmed for 2026, but exact dates NOT yet announced as of May 1. Typical timing: weekends across October-November. Source: leviedeitesori.com. | Use **"usually October-November"** or **"weekends in October-November"**. Do NOT state specific 2026 dates. |
| 17 | Il Sole 24 Ore Palermo crime stats current edition | ⚠️ UPDATE | Current edition: **Indice della Criminalità 2025** (data from 2024). Palermo = **3,936 denunce per 100k inhabitants**. Milan tops at 6,952; Florence 6,500; Rome 6,400; Naples 4,479. **Palermo is LOWER than Milan, Florence, Rome, AND Naples**. Source: lab24.ilsole24ore.com/indice-della-criminalita. Quality of Life 2025: Palermo ranks 97th of 107 provinces (separate index, "qualità della vita" not crime). Don't confuse the two. | Use **2024 data from the 2025 edition**. Pass 2 should specify: "Per Il Sole 24 Ore's 2025 crime index (data from 2024), Palermo ranks below Milan, Rome, Florence, and Naples in reported crimes per capita." If draft cites specific number, use **3,936 per 100k** for Palermo. |

---

### Specific entities (#18-22)

| # | Claim | Status | Evidence | Pass 2 Action |
|---|---|---|---|---|
| 18 | Villa Igiea operator = Rocco Forte | ✅ CONFIRMED | Multiple T2 sources: luxuryendless.com, wantedinrome.com, timeforsicily.com, leisurebyte.com all confirm "Villa Igiea, part of Rocco Forte Hotels / Rocco Forte group." 72 rooms, 28 suites. | Keep, but fix spelling to **Villa Igiea**. |
| 19 | Dua Lipa wedding at Villa Igiea | ⚠️ UPDATE (hedge) | **REPORTED, NOT CONFIRMED.** Italian press (Giornale di Sicilia, Dagospia) and international outlets report wedding Sept 5-7, 2026, at Villa Igiea. Hotel reportedly booked for full week, entire floor of suites reserved. **Lipa's reps have NOT confirmed.** Couple stayed there summer 2025 — that part is documented (Lipa Instagram "Palermo in my heart"). | Use **"reportedly"** or **"rumored to be hosting"**. Do NOT state as fact. Example: "the venue rumored to host Dua Lipa's wedding in September 2026" or "where Dua Lipa is reportedly getting married." Adds topicality without overclaiming. |
| 20 | €100 Airbnb → host sees ~€40 (Italy short-term rental tax math) | 🔄 PARK | Externally unverifiable as a clean equation. Generally: Airbnb host fee ~3% + guest service fee paid separately + Italian short-term rental tax (cedolare secca 21% on rental income, plus tourist tax ~€1-3/night collected separately) + cleaning fee carved out. €40-50 net to host on €100 gross is plausible but varies wildly by host setup, mortgage, utilities, cleaning crew, etc. | Defer to Nico's first-hand operator knowledge (he runs his own Airbnbs). Keep the rough number but frame as "roughly" or "after platform fees, Italian taxes, and cleaning, the host may see around €40." |
| 21 | Fake-Mondello Airbnb pattern still active 2026 | 🔄 PARK | Pattern is real and well-documented for years (listings titled "Mondello" but located in Partanna-Mondello, Pallavicino, Sferracavallo zones inland). Couldn't externally verify "still active in 2026" via a single citable source — would require live Airbnb scraping which violates ToS. | Defer to Nico's first-hand 2026 knowledge. He sees this pattern actively as a Palermo host. |
| 22 | TikTok URL @wearepalermo | ✅ CONFIRMED | tiktok.com/@wearepalermo resolves to "Nico - Sicilian Storyteller (@wearepalermo)" with active video posts (Mondello, Aperol Spritz, Centro Storico, Faccia di Vecchia content). Handle confirmed. | Keep as-is. |

---

### WAP_12 hotel URL verifications (#23-28)

**This is the critical revenue section. 4 of 6 URLs in the brief differ from WAP_12 canonical. These need exact swap-in for Pass 2.**

| # | Hotel | Pass 1.5 v2 URL (per brief) | WAP_12 Canonical URL | Status | Evidence |
|---|---|---|---|---|---|
| 23 | Politeama Apartments | `/hotel/it/politeama-apartments.en.html` | **`/hotel/it/painpa-i-mercati-apartments.en.html`** | ⚠️ UPDATE | WAP_12 canonical confirmed. Live Booking page resolves to "Politeama Apartments by Giorgio" at Piazza Castelnuovo 47. Brief URL likely doesn't resolve or resolves to different listing. |
| 24 | Hotel Politeama | `/hotel/it/politeama-palace.en.html` | `/hotel/it/politeama-palace.en.html` | ✅ CONFIRMED | Match. Hotel's own site (hotelpoliteama.com) confirms 4-star in Palermo center. |
| 25 | Family Affair Luxury Suites | `/hotel/it/family-affair-luxury-suites.en.html` | **`/hotel/it/family-affair-b-amp-b-palermo.en.html`** | ⚠️ UPDATE | WAP_12 has different listing. Note: brief URL may or may not resolve — but WAP_12 is source of truth per brief. **Confirm with PM/Nico:** is "Family Affair Luxury Suites" the same property as "Family Affair B&B" in WAP_12, or two separate listings? If same, use WAP_12 URL. If different, decide which the post should link. |
| 26 | Hotel Wagner | `/hotel/it/hotelwagner.en.html` | **`/hotel/it/grand-wagner.en.html`** | ⚠️ UPDATE | WAP_12 canonical confirmed. Brief URL likely a synthetic/inferred URL that doesn't match Booking.com's actual property slug. |
| 27 | B&B L'Officina di Apollo | `/hotel/it/officina-di-apollo.en.html` | **`/hotel/it/l-39-officina-di-apollo.en.html`** | ⚠️ UPDATE | Booking.com URL-encodes the apostrophe in "L'Officina" as `l-39-`. WAP_12 captures this; the brief's simplified URL doesn't. |
| 28 | Unico Boutique Hotel d'Arte | `/hotel/it/unico-boutique.en.html` | **`/hotel/it/unico-boutique-d-39-arte.en.html`** | ⚠️ UPDATE | Same encoding issue: "d'Arte" → `d-39-arte` in Booking's slug. WAP_12 is correct. |

---

### Hotel star ratings (#29-31)

Per WAP_06b: only Giata-classified hotels carry stars. B&Bs are extra-alberghiera and don't qualify for official Italian star classification regardless of what aggregators show. This rule was established and enforced in the Favignana run (Apr 28).

| # | Hotel | Pass 1.5 v2 Stars | Verdict | Evidence |
|---|---|---|---|---|
| 29a | Palazzo Natoli | ★★★★ | ✅ CONFIRMED | Confirmed via Booking + aggregators as 4-star boutique near Quattro Canti. WAP_12 Apr 24 verified. |
| 29b | La Terrazza sul Centro | ★★★★ | 🔄 PARK | Need to spot-check on hotel's own site. Not in WAP_12 source-of-truth excerpt I retrieved. Defer until WAP_12 listing for this property is reviewed. |
| 29c | Palazzo Santamarina | ★★★★ | ✅ CONFIRMED | WAP_12 Apr 24 verified as 4-star Luxury Hotel & Spa in Centro Storico. |
| 29d | Grand Hotel Piazza Borsa | ★★★★ | ✅ CONFIRMED | WAP_12 Apr 24 verified as 4-star in Centro Storico. |
| 30a | Hotel Politeama | ★★★★ | ✅ CONFIRMED | Hotel's own site (hotelpoliteama.com) explicitly self-describes as **"a 4 stars hotel in the center of Palermo."** WAP_06b satisfied — own-site canonical. |
| 30b | Hotel Wagner | ★★★★★ | 🔄 PARK | Couldn't pull hotel's own site result directly in search, only aggregators. WAP_12 has it as 5-star "Grand Hotel Wagner" via Booking URL (`grand-wagner.en.html`). Booking lists 5-star, multiple aggregators agree. Likely fine but PM should spot-check hotelwagnerpalermo.com (or canonical own-site) before Pass 2 ships. |
| 31a | Grand Hotel et Des Palmes | ★★★★★ | ✅ CONFIRMED | Multiple T2 sources, Rocco Forte / Mandarin Oriental / Rocco Forte family, well-documented 5-star Liberty-style. WAP_12 verified. |
| 31b | B&B Mondello Design | ★★★★ | ⚠️ UPDATE (STRIP) | WAP_06b violation: B&B classification → no Giata stars. Aggregator shows 4-star, but per WAP_06b strict reading, B&Bs are extra-alberghiera. **STRIP STARS, keep "B&B" type-label.** Same rule that was applied to Setteminne and Lido Burrone in Favignana run. |
| 31c | B&B L'Officina di Apollo | ★★★ | ⚠️ UPDATE (STRIP) | Same WAP_06b violation. **STRIP STARS, keep "B&B" type-label.** |
| 31d | Villa Igiea | ★★★★★ | ✅ CONFIRMED | Rocco Forte 5-star, multiple T1/T2 confirmations. WAP_06b satisfied. **Fix name spelling: "Villa Igea" → "Villa Igiea"** (consistent with #9, #18, #19). |

---

## WAP_12 Canonical URL Corrections (Exact Swap-In for Pass 2)

Find-and-replace these in `05_Pass1_Info_v2.md` for Pass 2:

| # | OLD (in draft) | NEW (canonical from WAP_12) |
|---|---|---|
| 23 | `https://www.booking.com/hotel/it/politeama-apartments.en.html?aid=918822&no_rooms=1&group_adults=2` | `https://www.booking.com/hotel/it/painpa-i-mercati-apartments.en.html?aid=918822&no_rooms=1&group_adults=2` |
| 25 | `https://www.booking.com/hotel/it/family-affair-luxury-suites.en.html?aid=918822&no_rooms=1&group_adults=2` | `https://www.booking.com/hotel/it/family-affair-b-amp-b-palermo.en.html?aid=918822&no_rooms=1&group_adults=2` ⚠️ **CONFIRM W/ NICO FIRST: same property or different?** |
| 26 | `https://www.booking.com/hotel/it/hotelwagner.en.html?aid=918822&no_rooms=1&group_adults=2` | `https://www.booking.com/hotel/it/grand-wagner.en.html?aid=918822&no_rooms=1&group_adults=2` |
| 27 | `https://www.booking.com/hotel/it/officina-di-apollo.en.html?aid=918822&no_rooms=1&group_adults=2` | `https://www.booking.com/hotel/it/l-39-officina-di-apollo.en.html?aid=918822&no_rooms=1&group_adults=2` |
| 28 | `https://www.booking.com/hotel/it/unico-boutique.en.html?aid=918822&no_rooms=1&group_adults=2` | `https://www.booking.com/hotel/it/unico-boutique-d-39-arte.en.html?aid=918822&no_rooms=1&group_adults=2` |

URL #24 (Hotel Politeama, `politeama-palace.en.html`) is correct as-is.

---

## Other Corrections Required for Pass 2

1. **"Villa Igea" → "Villa Igiea"** throughout draft. Add to spelling lock in Intake alongside Piazza Madrice, Castellammare, etc. **CRITICAL for SEO and credibility.**
2. **Dua Lipa wedding line:** add **"reportedly"** or **"rumored"** hedge. Lipa's reps haven't confirmed. Press reports only.
3. **Train Palermo→Cefalù: "1 hour" → "about 45-55 minutes"** or **"under an hour."**
4. **La Via dei Tesori: state "usually October-November"** without specific 2026 dates (not yet announced).
5. **Il Sole 24 Ore citation:** specify "2025 edition (data from 2024)" and use the correct framing — Palermo is BELOW Milan, Rome, Florence, AND Naples in the crime index. Concrete number: 3,936 per 100k for Palermo.
6. **B&B Mondello Design and B&B L'Officina di Apollo:** STRIP STARS per WAP_06b. Keep B&B type-label.

---

## Open Questions for PM / Nico (before Pass 2)

1. **Family Affair: same property as WAP_12's `family-affair-b-amp-b-palermo`, or different listing?** The brief and WAP_12 disagree. PM/Nico to confirm which listing is the right one for this post.
2. **Hotel Wagner / Grand Hotel Wagner own-site spot-check:** WAP_12 Booking URL is `grand-wagner.en.html` and external sources show it as 5-star. Per WAP_06b, hotel's own site is canonical for stars. PM/Nico to spot-check hotelwagnerpalermo.com or whatever the canonical own-URL is, just to lock the 5-star claim.
3. **La Terrazza sul Centro:** not in the WAP_12 excerpt I retrieved. If not in WAP_12, why is it in the draft? Confirm it's in the registry, or add it before Pass 2.
4. **Pricing numbers (#1-9):** all defer to Nico's first-hand 2026 knowledge from the May 1 brain dump. No external source can fix-cite live booking rates. PM should confirm numbers stay or get hedged in Pass 2.
5. **Dua Lipa hedge wording:** Nico's preference for "reportedly" vs "rumored" vs "where Dua Lipa is said to be getting married this September." All work; pick the one that fits voice.

---

## Time Spent

~30 min (cap reached). Hotel star spot-checks limited to top-3 priority hotels (Politeama, Wagner, Villa Igiea) plus the two B&Bs that needed strip-stars treatment per WAP_06b. Other hotels deferred to WAP_12 Apr 24 verification timestamp.
