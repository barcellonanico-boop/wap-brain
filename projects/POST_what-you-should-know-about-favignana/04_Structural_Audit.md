# 04 — Structural Audit

**SOP:** SOP_01 v2.0, Step 5 (Structural Audit)
**Target URL:** https://wearepalermo.com/news/what-you-should-know-about-favignana/
**Decision session:** April 27, 2026, ~21:25-21:50 (PM + Nico, collaborative)

---

## Structural Decision

**FULL REWRITE** per Architect Section I (02_Prep.md). Bones survive (18 H2s in coherent flow, voice survived in places, 6 hotel cards with correct affiliate IDs). Structural problems exceed polish: misplaced author intro, missing TL;DR callout, three competing box styles, hotel card violations, missing Continue Planning + Sicilian Way + affiliate disclosure, FAQs need expansion + schema.

3-pass model applies. Pass 1 markdown information. Pass 2 voice + brain-dump fragments installed verbatim. Pass 3 HTML + WAP_06 v2 templates.

---

## Reader Intent

**Who's searching "favignana":** US tourists planning a Sicily trip, considering an island day-trip or short stay. Volume 4,400/mo (peak July 9,900), informational + light commercial. Most are at the "should I add this island to my itinerary" stage.

**What they actually want:**
- A reason to pick Favignana over the next island in their list
- Concrete logistics (how to get there, how long to stay)
- Real talk on crowds, prices, season
- Where to sleep, what to eat, what to do
- A trustworthy local voice (not another Top 10 listicle)

**What they fear:**
- Booking the wrong island
- Showing up without a bike/scooter and being stranded
- Paying tourist prices
- Going in August and hating it
- Wasting a day with bad weather + bad info

**Cold reader test:** US 35-year-old planning a 10-day Sicily trip. Has 1-2 days to spare. Hears "Favignana" from someone, Googles it, lands on WAP. They need answers in 90 seconds OR they bounce to TripAdvisor.

---

## Search Goal Classification

Informational + light commercial. AI Overview is heavily activated on this query (KG + PAA at SERP positions 1, 2, 4 per Architect SERP scan). Wikipedia at #5 = AIO factual entity grounding pulls from there.

**WAP's competitive lane:** authentic local voice + monetization depth + real-talk on crowds/prices that competitors can't write.

**AIO extractability target:** the TL;DR callout must contain the direct answer in <100 words, structured for verbatim citation.

---

## Live Post Section-by-Section Audit

| Section | Live | Decision |
|---|---|---|
| Italic lead | Generic ("looks like paradise—but what the hell do you actually do") | REWRITE — sharper hook, <25 words |
| Featured image | Cala Rossa 1024x684 | KEEP |
| Opening prose paragraphs (5+) | Walls of intro before author intro | CUT to ~20 words bridge into Nico intro |
| Old "Be careful" box (quick-guide-box) | Style violates WAP_06 v2 | REPLACE with WAP_06 v2 Variant 3 (Local's Warning) |
| Author intro (mid-page) | "I'm Nico—100% Sicilian, raised on espresso and sarcasm" | RESTRUCTURE: move BEFORE TL;DR. Rewrite to hit 3 jobs (name + credibility + sales hook). ~80 words. |
| H2: Why Visit Favignana? | Brief, lacks Cold Reader items 10-11, no island comparison | EXPAND: add vs Levanzo + Marettimo + Ustica + Aeolians (1-line each, link out). Install brain-dump items 10 (price reality) + 11 (crowds nuance). |
| H2: What is There to Do — 6 H3s | Strong section, voice mostly on | KEEP structure. Distribute GYG affiliates inline per topic (Q2 decision: distributed not aggregated). Strip Sicilian Way + Restaurant Guide CTAs (those are Palermo-only — confirmed by Nico). |
| H3: Rent a Boat | Sea Taxi named, no GYG | KEEP Sea Taxi reference. ADD inline: GYG yacht tour from Trapani (gyg.me/38B9HCJk, NEW from Nico) framed as captained alternative. |
| H3: Scuba Diving | Egadi Scuba named | KEEP Egadi Scuba named. NO GYG (confirmed: Egadi Scuba not on GYG). |
| H3: Local Foods | Tuna, pane cunzato, etc. | KEEP. NO Sicilian Way / Restaurant Guide CTAs (Palermo-only). |
| H3: Santa Caterina Castle | Hike + view section | KEEP. |
| H3: Florio Tuna Factory | "Book ahead", named workers | KEEP. NO GYG (confirmed: not on GYG). Verify museum site for current hours/booking. |
| H3: Tuff Caves | "Off the tourist radar" framing | KEEP. |
| H2: Where to Stay | 6 hotel cards with old WAP_06 template | FIX: per WAP_06 v2 hotel card template. Strip stars on Egusa73 + Setteminne + Lido Burrone (Architect verified violations). Update type-labels: Setteminne → B&B, Lido Burrone → B&B. Keep all 6 (Nico Q4). |
| H2: How Long Should You Stay? | "2-3 nights sweet spot" verdict | KEEP — strong section. |
| H2: Moving Around | Bike vs scooter vs car, "microwave to a picnic" | KEEP — voice gold. Verify bike/scooter prices for 2026 (Scout). |
| H2: Nightlife | "This is NOT Ibiza" framing | KEEP. |
| H2: Best Beaches | Land + boat-only beach lists | KEEP. |
| H2: Reach From Palermo | Bus + car + Discover Cars + Parclick | CONSOLIDATE into single "Getting to Favignana" H2 with 3 H3s. |
| H2: Reach From Trapani | Ferryhopper + 3 GYG tours | CONSOLIDATE. **Anchor swap: "Liberty Lines" → "Ferryhopper"** (Architect found URL resolves to Ferryhopper, not Liberty Lines). ADD 4th GYG yacht tour. Distribute by use-case (premium yacht / private / day cruise / boat with lunch). |
| H2: Reaching Levanzo and Marettimo | Already short | CONSOLIDATE as H3 inside Getting To Favignana. |
| H2: FAQs (4 questions) | No FAQPage schema | EXPAND to 6-8 questions. ADD FAQPage schema (Step 11 Architect task). |
| H2: Conclusion | Generic; CTA links to /free-itinerary/ | REWRITE: Nico verdict closer. REMOVE /free-itinerary/ link (WAP_03 banned). |
| Continue Planning block | MISSING | ADD per WAP_06 v2 (related post + Sicilian Way framed for Palermo trip + YouTube). |
| Bottom italic disclosure | MISSING | ADD per WAP_06 v2. |
| Signature | MISSING | ADD. |

---

## New Article Outline (10 H2s)


[Italic lead, <25 words] [Featured image: Cala Rossa current] [Author intro, ~80 words, 3 jobs: name + credibility + sales hook, NEVER an H2] [Top affiliate disclosure: small grey neutral box] [TL;DR callout: light blue box, "in a hurry?" framing, <100 words]
H2 1: Why Visit Favignana?
Brief vibe (1 paragraph)
vs Levanzo + Marettimo (1 paragraph, link to wearepalermo egadi/levanzo if exists)
vs Ustica (1 paragraph, link to Nico's Ustica article)
vs Aeolian Islands (1 paragraph, link to Nico's Aeolian article)
Crowds reality (brain-dump item 11): foreign presence still low, locals + Trapani crowd, influencer-of-the-moment risk
Price reality (brain-dump item 10): "grandmas renting basically holes" at premium prices, prices climb every year
Local's Take or Local's Pick callout
Word target: ~500 words
H2 2: Best Things to Do in Favignana
H3: Rent a Boat and Circumnavigate the Island
Sea Taxi named (kept)
Inline: GYG yacht tour from Trapani as captained alternative (gyg.me/38B9HCJk)
Local's Take: Nico's Mario Kart line preserved
H3: Scuba Diving
Egadi Scuba named (kept, no GYG)
Beginner to advanced sites
H3: Try the Local Foods
Red tuna, pane cunzato, sea urchins, couscous di pesce
NO Sicilian Way / Restaurant Guide CTAs (Palermo-only)
Brief mention of price reality
H3: Visit Santa Caterina Castle
Hike, view, history
H3: Florio Tuna Factory Museum
History, former-workers tour
Verify hours (Scout)
H3: Tuff Cave Exploration
Off-radar gem
Word target: ~900 words
H2 3: Where to Stay in Favignana
Brief framing (stay near port)
6 hotel cards (per WAP_06 v2):
Residence Scirocco e Tramontana — STAR DECISION FROM NICO
B&B Il Tufo — keep ★★★
I Pretti Resort — keep ★★★★
Egusa73 Favignana (Apartments) — STRIP STARS
Setteminne (B&B, type-label fix) — STRIP STARS
Stabilimento Lido Burrone (B&B, type-label fix) — STRIP STARS
Local's Pick callout (favorite)
Word target: ~450 words
H2 4: How Long Should You Stay?
2-3 nights verdict
One-day-trip honest take
Word target: ~200 words
H2 5: Moving Around the Island
Bike vs scooter vs car verdict
"Microwave to a picnic" line preserved
Verify 2026 prices (Scout)
Word target: ~250 words
H2 6: Favignana's Best Beaches
6 land beaches list
5 boat-only beaches list
Local's Pick: Cala Rossa by boat
Word target: ~300 words
H2 7: Nightlife Reality Check
"Not Ibiza" framing
Word target: ~200 words
H2 8: Getting to Favignana
H3: From Palermo (bus, car + Discover Cars + Parclick)
H3: From Trapani (Ferryhopper for ferries — NOT "Liberty Lines"; 4 GYG tours distributed by use-case: premium yacht / private / day cruise / boat with lunch)
H3: Hopping to Levanzo or Marettimo (Ferryhopper, ~10/30 min, Nico's "Levanzo dream / Marettimo wild" framing)
Word target: ~450 words
H2 9: FAQs (6-8 questions, FAQPage schema in Pass 3)
Existing 4 + 2-4 new (price reality, August advice, what to skip, Lampedusa-not-Egadi clarification, etc.)
Each answer 40-75 words self-contained
Word target: ~500 words
H2 10: Bottom Line
Nico verdict closer (replace generic conclusion)
1 sentence per: choose Favignana if X / skip if Y
Word target: ~150 words
[Bottom italic disclosure] [Continue Planning block: 1 related post + Sicilian Way framed for Palermo half + YouTube channel] [Signature]

**Total target: 2,800-3,200 words** (Architect's recommendation, Nico Q7 confirm).

---

## Voice + Tone Notes for Pass 2

### Mode: A (bar comedian default)

This is a destination guide, not a heavy/historical post. Mode A all the way. Sebastian Maniscalco rhythm, sarcastic, direct, no Mode B required.

### Brain-dump fragments to install verbatim

These are Nico's specific Favignana truths that don't exist in the live post. Pass 2 must surface them:

1. **"Two rays of sun, people boom, they rush over there"** (re crowds — install in Why Visit, crowds paragraph)

2. **"Grandmas renting you basically holes, little dens, and they make you pay for them like they're worth their weight in gold"** (re prices — install in Why Visit, price reality paragraph)

3. **"Ustica is closer, but you shoot yourself in the balls because there are like two bars, two restaurants, you do a couple climb-and-descents and you're done"** (re Ustica comparison — install in Why Visit, vs Ustica paragraph)

4. **"Already really a mess with the locals"** (re foreign tourists still low — install in Why Visit, crowds paragraph)

5. **"What Ibiza is for Barcelona, Favignana is for Palermo... except instead of a flight you take a bus, a ferry"** (with caveat that comparison breaks because no nightlife — install in Why Visit, opening framing)

6. **"Sea, fun, biking, boat, restaurants, aperitivo spots — really a fucking chaos"** (re vibe — install in Why Visit, vibe paragraph)

7. **First-person specific observation:** Nico's been going almost every summer since childhood. Make it specific. Not "I've been many times." Better: a specific memory or detail that proves it. (Pass 2 to surface or Nico to provide.)

### Voice lines from live post to PRESERVE

These already work — keep them:
- "Mario Kart" line (boat steering)
- "Mykonos" line (re nightlife)
- "Microwave to a picnic" (re cars)
- "Like going to a wine tasting and only smelling the cork" (re day-tripping)
- "Cyclones at the Florio factory" mood
- "Sandals will blow off" (Santa Caterina view)

### WAP_05 self-check minimums

- ≥1 Reader Interrogation
- ≥1 first-person specific observation (the "every summer since childhood" anchor — make it specific)
- ≥3 of the 21 signature moves
- Em-dash purge: MANDATORY
- Banned-in-body words: NONE (none detected by Architect, keep clean)
- Mode A throughout
- Verdict closer in conclusion (no corporate-blog ending)

---

## Post-Type-Specific Reminders (WAP_06b)

WAP_06b currently has where-to-stay populated. Things-to-Do / Island-Guide subsection is empty. This run produces input for that subsection.

**Cold Reader Reality Check (13 items, Architect-refined):**
1. Why this island vs others — DONE in H2 1
2. When to visit — covered in TL;DR + Why Visit + FAQ
3. How to get there — DONE in H2 8
4. Where to stay — DONE in H2 3
5. How long — DONE in H2 4
6. What to do — DONE in H2 2
7. How to get around — DONE in H2 5
8. What to eat — DONE in H2 2 (food H3)
9. Nightlife expectations — DONE in H2 7
10. Price reality — DONE in H2 1 (brain-dump fragment)
11. Crowds nuance — DONE in H2 1 (brain-dump fragment)
12. What to avoid — distributed across post (not consolidated)
13. Audience fit — implicit in Why Visit

**Post-publish task:** promote this 13-item checklist into WAP_06b Things-to-Do subsection (Architect handoff).

---

## Special Instructions for Downstream Agents

### For Pass 1 (Copywriting Information Draft)

- Use this outline as the structural blueprint. Every H2 in this outline MUST be in the markdown draft.
- Pull facts from live post and Architect prep. Do NOT invent.
- Verify any specific number / price / time / hour — flag [VERIFY: X] if unsure.
- Word target 2,800-3,200 distributed roughly per H2 word targets above.
- ENFORCE 180-character paragraph max from the start. No walls of text in Pass 1.
- Voice rough is OK — Pass 2 polishes.
- Brain-dump fragments listed above must appear in Pass 1 (rough wording OK — Pass 2 polishes the cadence).
- NO Sicilian Way / Restaurant Guide CTAs in body (Palermo-only — confirmed).
- Sicilian Way appears ONLY in Continue Planning block, framed as "the Palermo half of your Sicily trip."
- Output: projects/POST_what-you-should-know-about-favignana/05_Pass1_Info.md

### For Step 7 (Scout Fact Check)

After Pass 1 lands, Scout verifies:
- Boat rental "around €150" — likely stale, current 2026 rate?
- Bike rental €5-10/day, scooter €30-70/day — verify
- Liberty Lines RT prices: Levanzo €8, Marettimo €12 — verify Ferryhopper current
- Florio Tuna Factory hours, entry fee — verify museum site
- Ferry duration Trapani→Favignana 30 min — verify
- All 6 hotel star ratings against hotel's OWN official site (per WAP_06b)
- New GYG yacht tour: 4.6 stars / 338 reviews / 8 hours / EGADI LINES SNC — confirm canonical URL

### For Pass 2 (Voice & Trim)

- Install all 6 brain-dump fragments listed above.
- Apply scout fact corrections.
- Em-dash purge — mandatory.
- Apply 180-char paragraph limit.
- Apply bold logic (2-4 word phrases, never full sentences). Skimmer test must pass.
- Mode A maintained throughout.
- Verdict closer in H2 10 (Bottom Line).
- Output: projects/POST_what-you-should-know-about-favignana/07_Pass2_Voice.md

### For Pass 3 (Format & HTML)

- Apply WAP_06 v2 mandatory skeleton ordering.
- Apply WAP_06 v2 affiliate disclosure (top: grey neutral box).
- Apply WAP_06 v2 TL;DR callout (light blue, "in a hurry?" framing).
- Apply WAP_06 v2 hotel card template to all 6 hotels.
- Apply WAP_06 v2 Local's Take/Pick/Warning text boxes (mix variants, min 1 per H2).
- Apply WAP_06 v2 Continue Planning block (related post + Sicilian Way for Palermo half + YouTube).
- Apply FAQPage schema script after FAQ section.
- Final em-dash + banned-words scan (catch-all).
- Final 180-char paragraph scan.
- Output: projects/POST_what-you-should-know-about-favignana/08_Pass3_HTML.md

---

## Post-Type Rules Specific to This Run

This is an Island-Guide / Day-Trip post. WAP_06b lacks formal rules for this type. Run-specific rules:

1. Sicilian Way + Restaurant Guide are PALERMO-ONLY. Not mentioned in Favignana body. Continue Planning block frames Sicilian Way as "the Palermo half of your Sicily trip" (Q2 Continue Planning Option B confirmed).

2. Star rating convention: same as WAP_06b where-to-stay rule — only on Giata-classified hotels (verified per hotel's own site, NOT aggregator). Apartments / vacation rentals / unclassified B&Bs get NO stars.

3. Cold Reader Reality Check (13 items) applied above.

4. GYG inline distribution preferred over aggregation (PM call: better CTR).

5. Anchor swap: "Liberty Lines" → "Ferryhopper" wherever the redirect link `go.wearepalermo.com/ferry` is used.

---

## Open Items Carried Forward

1. **Residence Scirocco e Tramontana ★★★ ambiguous classification** (Architect flagged "AMBIGUOUS"). Default per WAP_06b conservative reading: STRIP STARS unless Nico can confirm Giata classification first-hand. **Decision:** Strip pending Nico's call.

2. **Egadi Scuba Diving + Florio Tuna Factory** — kept named, no GYG affiliate available. Future Kaizen if these become bookable on GYG.

3. **Lampedusa mention** decided OUT (Q9 Nico confirmed Ustica + Aeolians only — keeps Favignana primacy).

4. **WAP_12 Brain doc Favignana population** = separate post-publish Architect handoff (Architect Section D flag).

5. **WAP_06b Things-to-Do subsection promotion** = separate post-publish Brain handoff (Cold Reader 13-item checklist).

---

## Status

✅ Step 5 complete. Structural decision: FULL REWRITE. Outline locked. Voice notes locked. Special instructions locked.
→ Next: Step 6 (Pass 1 — Information Draft) by Copywriting agent.
