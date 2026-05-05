# 02 — Persona Match — /news/comprehensive-guide-visiting-san-vito-lo-capo/

**Date:** May 5, 2026 (22:16)
**Phase:** v2.3 Workflow Phase 2 — Persona Match
**Status:** COMPLETE
**Input:** 01_Tech_Report.md + brain/WAP_15_PERSONAS.md

---

## Decision

**Primary Persona:** A — Anglo Couple Planner
**Secondary Persona:** none

---

## Justification

### Signals from GSC queries
All top-volume queries are beach/leisure/decision-driven, no heritage or off-path framing:
- "san vito lo capo" 1,474 clicks (intent: navigational + transactional)
- "san vito lo capo beach" 83 clicks (intent: beach-focused)
- "palermo to san vito lo capo" 66 clicks (intent: logistical)
- "things to do in san vito lo capo" 54 clicks (intent: activity)
- "is san vito lo capo worth visiting" 17 clicks (intent: decision)
- "san vito lo capo restaurants" 12 clicks (intent: practical)

Zero queries containing "roots," "ancestry," "Corleone," "Sicilian heritage," "off the beaten path," "real Sicily." → Persona B and C signals absent.

### Signals from Ubersuggest demographic clickstream ("san vito lo capo")
- Age 35-44: 45% (dominant) → matches Persona A exactly
- Female 55% / Male 20% → Persona A female-led couple planning
- Desktop 71% → planner research mode (Persona A reads on phone, books on desktop)

### Signals from GSC geography
- Top markets: UK 782 + USA 741 + Canada 269 + Italy 169 + Australia 152 = 2,113 clicks (57% of total)
- UK + USA + AU + CA = anglo core of Persona A (50% match WAP_15 attribute)

### Signals from GSC device
- Mobile 43% / Desktop 30% / Tablet 1% → consistent with Persona A "mobile read, desktop book" pattern

### Why no Secondary Persona
- Heritage angle: no signal in queries, no Sicilian-American emotional intent. Persona B not relevant.
- Off-path angle: query intent is mainstream beach holiday, not Persona C "I've done Tuscany" sophisticated traveler. Persona C not relevant.

This article is **pure Persona A**. Anti-pattern from WAP_15 explicitly warns against multi-persona articles unless data supports it. Data here points to one.

---

## Persona A attributes that matter MOST for this article

From WAP_15 schede, the attributes most relevant to San Vito Lo Capo rewrite:

### Decision style
3-4 month planning horizon. Reads 5-10 articles before booking. Comparison-heavy. → Article must be comprehensive enough to be the LAST thing she reads, not the first.

### Knowledge gaps
- ZTL → not relevant for San Vito (no ZTL there). DROP this WAP_15-default callout for this article.
- Bidet → not relevant for this article.
- AMAT → not relevant (no urban transport in San Vito). DROP.
- Italian neighborhood granularity → not relevant.

### NEW knowledge gaps specific to San Vito (not in WAP_15)
- Riserva dello Zingaro (national park concept, walking-only access)
- Beach club pricing reality 2026 (€20-40 lido per day)
- Couscous Festival September (date + worth-it answer)
- "Day-trip from Palermo vs base in San Vito?" — the critical decision
- August reality (prices doubled, parking gridlock, beach overcrowded)
- Egadi day-trip option from San Vito (or separate stay)
- Common typos: San Vito Capo, San Vito del Capo, San Vito de Capo

### Fears (Persona A) relevant here
- Wasting vacation days → "is it worth visiting?" intent
- Tourist traps → restaurant blacklist + lido vs free beach trade-off
- Booking the wrong week (August) → seasonality brutality required
- Getting lost / parking → from-Palermo logistics + parking 2026 prices

### Voice calibration for this article (per WAP_15)
- **Maniscalco brutality on August**: "Don't go in August. Or go and don't blame me."
- **Specific 2026 numbers**: room €150-300 August vs €70-120 May/September; lido €25-40/day; parking €10-15/day; Zingaro entrance fee
- **Insider framing**: "Where I send my friends from Palermo"
- **Anti-vlogger**: "The guides will tell you August is paradise. They're lying."
- **Heritage callout**: NOT for this article. Persona A is not Italo-American.

---

## Article structure implications (preview for Phase 4)

Sections that MUST be in the rewrite (driven by GSC emergent clusters + Persona A gaps):

1. Coming from Palermo (NEW emphasis, +120-140% QoQ cluster)
2. The town centre / what the village is like (NEW, +133-200% QoQ cluster)
3. Worth visiting? Direct answer (recovery cluster +55% QoQ)
4. When to go / when to skip (Persona A August fear)
5. Beaches: free vs lido pricing 2026
6. Riserva dello Zingaro (Persona A gap)
7. Restaurants: 3-5 specific names + 2026 prices (NEW emphasis, +33% QoQ)
8. Where to stay: 3-5 hotels (BLOCKED by WAP_12 gap, see Tech Report)
9. Couscous Festival (September decision)
10. Day-trip vs base decision (the critical question)
11. Egadi day-trip option

Sections to DE-EMPHASIZE (cannibalized by Google AIO):
- "Things to do" framed as listicle. Pivot to narrative experiential.

---

## Hand-off to Phase 3 (Brain Dump)

When Nico is ready, the agent runs Phase 3 with the 13 brain-dump questions in 01_Tech_Report.md. The Persona A focus narrows those questions: ask only what serves a couple-traveler beach holiday, not heritage angles.
