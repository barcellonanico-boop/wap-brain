# WAP Audience Analysis — May 5, 2026

Compiled from 9 datasets analyzed during May 5 session. Source data preserved on Nico's local machine + GA4 + Stripe + Booking + GYG + YouTube + Gemini AI on YouTube.

---

## Executive Summary

WAP has 3 distinct audiences across 3 channels. Site = 60% revenue (Booking + GYG + Stripe). YouTube = brand amplifier with separate audience, near-zero direct revenue. Meta Ads = tertiary, untracked attribution.

Total tracked annual revenue: ~€28,400.
- Booking.com: ~€15,500 (56%)
- GetYourGuide: €7,458 (27%)
- Sicilian Way (Stripe): €4,669 (17%)
- YouTube AdSense: ~€780 (3%)

Site is mobile-first read (67%), desktop-finalized purchase. Anglo couple traveler is dominant revenue driver.

---

## Dataset 1 — GA4 Site Demographics (12 months)

- 218,188 active users / 218,630 new users (low return rate, no newsletter)
- 187,530 engaged sessions / 55.1% engagement rate / 2m54s avg time
- Female 60.1% / Male 39.9%
- Top countries: UK 20%, USA 20%, Italy 18%, Germany 5%, Canada 4%, Australia 4%
- Top cities: London 18K, Palermo 14K (locals reading EN content), Rome 6.6K, NY 4.2K
- Top age: 25-34 + 45-54 (two cluster generations)
- Engagement time highest: Canada 3m19s, Australia 3m26s, USA 3m03s. Italy lowest 2m26s.

## Dataset 2 — GA4 Tech (12 months)

- Mobile 67% / Desktop 31% / Tablet 1.9%
- iOS 104K (dominant), Android 48K, Windows 35K, macOS 31K
- Browser: Safari ~110K, Chrome ~95K
- Screen res top: 390x844 (iPhone 14/15 Pro), 393x852, 1920x1080

## Dataset 3 — Booking.com Booker Insights

- Country (who books): USA dominant peak Aug, Australia constant 2nd, UK 3rd, Canada 4th
- Traveler type: Couple dominant ~70% of volume, picco August
- Travel purpose: Leisure 95%+, Work near zero
- Trip type: International overwhelming, Domestic near zero
- Device: Desktop dominant for checkout (~50/45 split desktop/mobile)
- Language: English dominant, German + Swedish minimal

## Dataset 4 — Booking.com Commission (10 invoices Feb 2025–Jan 2026)

| Month | Bookings | Commission | €/booking |
|---|---|---|---|
| Feb 2025 | 8 | €97 | €12 |
| Apr 2025 | 51 | €837 | €16 |
| May 2025 | 67 | €1,486 | €22 |
| Jun 2025 | 65 | €1,910 | €29 |
| Jul 2025 | 72 | €2,319 | €32 |
| Aug 2025 | 43 | €1,402 | €33 |
| Sep 2025 | 114 | €2,695 | €24 |
| Oct 2025 | 82 | €1,515 | €18 |
| Nov 2025 | 23 | €452 | €20 |
| Jan 2026 | 11 | €181 | €16 |
| TOTAL | 536 | €12,895 | €24 |

10-month total €12,895 → annualized estimate ~€15,500.

Pattern: high season Jun-Sep = 30% higher €/booking (couples on premium summer hotels). Low season Dec-Feb = drop ~93% from Sep peak. Sep peak in stayed bookings.

## Dataset 5 — Stripe Sicilian Way (Premium Guide)

- 148 customers / 12 months / €4,669 total revenue
- Avg €31.55 / median €31.61
- Tier distribution: 48.6% pay €40-50 (full price $47), 37.2% pay €20-30 (downsell $31), 12.2% pay <€20
- Monthly distribution: peak Sep (20), Jul (17), May (15), Aug (14), Jan (14). Dec lowest (3).
- Pattern: customers buy 2-3 months BEFORE travel, not during
- Email TLD: 85.8% .com (Gmail/Yahoo dominant — provider doesn't reveal country)
- Names sample: mix anglo + Italian heritage (Asaro, Tellini, Pittari, Conti, Ferrara) + few European (Pollak, Engin, Wallmansson)

## Dataset 6 — GetYourGuide Tour Bookings

- 793 bookings / 159 tours actually booked (out of 500 listed)
- €7,458 total commission / 54,695 visitors via WAP links / 1.45% avg conversion
- Top 5 by bookings: Street Food Walking (110/€854), NO Mafia Walking (68/€386), Bar Crawl (61/€136), Wine Tasting (52/€416), San Vito Boat (43/€452)
- Top by commission: Street Food €854, Vintage Fiat 500 €536 (only 16 bk), San Vito Boat €452
- Categories: Walking Tours top volume (223 bk), Day Trips top €/tour (€1,496 across 34 tours)
- Cities: Palermo 73% of total bookings, San Vito Lo Capo 8%, Taormina 3%

## Dataset 7 — Meta Ads Cheat Sheet (lead gen, 3 years total)

- 230 leads / €374 spent / €1.63 CPL
- Demographics: Women 76% (175), Men 23% (53)
- Age: 65+ DOMINANT (~150 leads of 230)
- Costo per result Women €1.57, Men €1.73
- Ad creative: "Don't visit Palermo without this" + PDF mockup + Cathedral
- Audience NOT overlapping with site audience — different channel, different demographic
- ROI on Sicilian Way unknown (not tracked)

## Dataset 8 — YouTube Channel (12 months — YouTube Studio)

- 162,606 views / 9.9K hours watched / 7,585 subscribers (-15% vs prior year)
- $857 AdSense revenue (~€780, 3% of total)
- Demographics: Male 67.3% / Female 32.8% (OPPOSITE of site)
- Age: 35-44 (25.2%), 25-34 (24.1%), 45-54 (21.6%), 55-64 (18.8%), 65+ (10.2%)
- Geo: USA 25.9%, UK 9.8%, Italy 5.9% (much lower than site 18%), Canada 4.5%, Germany 4.4%
- Device: TV 40.8%, Phone 26.8%, Computer 25.4%, Tablet 6.8%
- Audience behavior: 86.6% NEW viewers, 13.2% occasional, 0.2% habitual = high churn
- Traffic source: YouTube search 37.6%, External 20.1%, Suggested 17.2%
- Language: English 89%, others negligible
- Top video by retention: "Don't Make 5 Mistakes" 61.2%, "3 Beaches" 54.1%, "Dressing for Sicily" 43.2%
- Pattern: short list-style brutal videos > long complete guides

## Dataset 9 — Gemini AI Insights from YouTube Comments (90 days, hidden data)

NOTE: 90-day data shows audience aging vs 12-month YouTube Studio data. The recent skew is older.

- Age (90d): 45-54 (51%), 65+ (30%), other 19%. Audience aging vs 12-month dataset.
- Geo: USA dominant (Florida, California, NY specific), Canada strong, Iceland niche, Australia, UK (London), Sweden, Finland, Belgium, Germany
- Psychographics from comments:
  1. "Heritage seekers" — children/grandchildren of Sicilian immigrants returning to find roots. Mention specific small towns (Villafrati, San Cataldo, Sferracavallo).
  2. "Anxiety about scams" — fear rental car scams, taxi scams, tourist traps. Want a "local brother" to protect them.
  3. "Edutainment" — watch for entertainment as much as info. Many watch even without planning a trip.
  4. Long stays — many plan 20-30 day trips, not weekends.
- Stated growth opportunities: ancestry guide content, silver travelers (60+) content, "living in Palermo for a month" content

---

## Three Personas (concept — full draft in WAP_15)

### Persona A — "The Anglo Couple Planner"
- 35-55, USA/UK/AU/CA, female lead planner for couple trip
- Mobile-first reading, desktop checkout
- 3-4 month planning horizon
- Buys Sicilian Way 2-3 months pre-trip
- Books Booking.com hotels (mid-luxury €100-300/night)
- Books GYG walking + food + bar crawl tours
- Voice match: Maniscalco-flavored authenticity + safety reassurance
- ~50-60% of audience, ~60-70% of revenue
- Channel: Site dominant, no YouTube

### Persona B — "The Italo-American Heritage Seeker (50+)"
- 45-65+, USA dominant (FL/CA/NY), 2nd-3rd gen Sicilian
- Family origin in small towns (Villafrati, San Cataldo, Sferracavallo)
- Long stays 20-30 days
- High disposable time + budget, premium tour buyer (Vintage Fiat 500, Corleone Mafia private)
- Buys Sicilian Way (cognomi italiani in Stripe data)
- Watches YouTube on smart TV
- Voice match: "Born in Palermo, 39 years here, 100% Sicilian" identity recognition + brutal honesty about flaws
- ~25-35% of audience, ~25-35% of revenue (high LTV)
- Channel: YouTube + Site

### Persona C — "The Returning Italy Traveler"
- 30-50, has done Tuscany/Rome/Amalfi, now seeking the South
- Values anti-tourist-vlogger positioning ("not the umpteenth John from Manchester")
- More skeptical, slower converter
- Lower buyer rate but high engagement
- Voice match: Nico's anti-tourist-vlogger + cultural authenticity
- ~10-15% of audience, ~5-10% of revenue
- Channel: Site

---

## Key Strategic Findings

1. Site = 83% of revenue (Booking + GYG + Stripe). YouTube + Meta Ads = brand awareness, not direct revenue.
2. Mobile reads, desktop pays. CTAs must work on iPhone 14/15 Pro screen sizes (390x844).
3. YouTube audience is DIFFERENT from site audience (M67/F33 vs F60/M40). Two channels, two pubblici.
4. Booking commission averages €24/booking. Each working hotel link = real money. WAP_12 + audit C1 critical.
5. Customers buy 2-3 months pre-trip. Content needs Google indexing 3+ months before travel season.
6. Italian site traffic (18%) is mostly expats + tourists already in Italy searching, not target buyers.
7. Heritage seekers (Persona B) is high-LTV + Persona B exists across both channels (YouTube discovery → site purchase).
8. Newsletter not yet implemented — would mainly serve Persona B (Italian heritage continuity content) as future product.

---

## Open Questions for Future Sessions

- Top 10 organic landing pages (need GSC + GA4 Top Pages export)
- Meta Ads → Sicilian Way attribution (overlap of 230 leads with 148 buyers)
- Top buyer profile — which articles converted them
- Repeat customer rate — currently no tracking
- Discover Cars affiliate revenue (not analyzed)
