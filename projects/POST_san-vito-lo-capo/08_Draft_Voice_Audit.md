# 08 Draft Voice — Audit Trail

Companion to `08_Draft_Voice.md`. This file documents the Phase 8 checklist results, trait verbatim evidence, failure mode audit, banned-phrase fixes, em-dash conversions, and final test run output. It is NOT part of the published article body.

**Article URL:** https://wearepalermo.com/news/comprehensive-guide-visiting-san-vito-lo-capo/
**Date:** 2026-05-17
**Pair file:** `08_Draft_Voice.md`
**Reference:** WAP_05c_VOICE_DNA.md, WAP_05d_VOICE_CHECKLIST.md v2.0, tools/test_voice_checklist.py v2.0

---

## Trait Verbatim Evidence (WAP_05d Section 2)

Required: ≥5 of 11 traits with verbatim quote. Achieved: 11/11.

Trait 1, The Anti-Romantic Pragmatist: Y.
Verbatim: "Those crystal-water postcard photos every guide shoves down your throat? They're shot when nobody's there."
H2 source: Is San Vito Lo Capo worth visiting? The honest answer

Trait 2, Exaggerated Biological Threat: Y.
Verbatim: "The sun in this part of Sicily, in summer, will cook your brain."
H2 source: Riserva dello Zingaro

Trait 3, Dialogic Strawman: Y.
Verbatim: "So when readers tell me, *\"But my company holiday is in August\"*, fair enough."
H2 source: Is San Vito Lo Capo worth visiting? The honest answer

Trait 4, Reluctant Educator: Y.
Verbatim: "Don't over-plan it. Wander. Eat. Sit."
H2 source: What the village actually feels like

Trait 5, Scam Radar Disclosure: Y.
Verbatim: "the local police make their entire year's income in three peak months by ticketing tourists who park wrong."
H2 source: How to get to San Vito Lo Capo from Palermo

Trait 6, Staccato Absolutes: Y.
Verbatim: "Pick the week: late May, June, September, early October."
H2 source: Bottom Line

Trait 7, Class/Culture Knife: Y.
Verbatim: "If you're coming from Manhattan, you'll think it's a steal. If you're coming from Sofia, you'll have a small heart attack at the first menu."
H2 source: How much does it cost in peak season (2026)

Trait 8, Setup-Pause-Snap: Y.
Verbatim: "Half of Italy is there. Not half of Sicily, half of *Italy*."
H2 source: Is San Vito Lo Capo worth visiting? The honest answer

Trait 9, The Italian Roast: Y.
Verbatim: "the local police make their entire year's income in three peak months by ticketing tourists who park wrong."
H2 source: How to get to San Vito Lo Capo from Palermo

Trait 10, Hyperbolic Origin Story: Y.
Verbatim: "back when *papà* drove us up the coast. The water felt like a swimming pool then."
H2 source: Element 4 Nico self-intro + Is San Vito Lo Capo worth visiting (Local's Take)

Trait 11, Pop Culture Hook: Y.
Verbatim: "In Sicily we've got more types of pasta than a Kardashian has selfies."
H2 source: What to eat in San Vito Lo Capo (Busiate)

Coverage: 11/11. Threshold cleared (≥5/11 required).

---

## Failure Mode Audit (WAP_05c Section 8)

All 6 failure modes scanned. Status:

1. Grumpy but Warm cliché: NOT PRESENT. No softening pivots. The August warning ends on the warning. The Castellammare pivot redirects to a different decision, not a tone softening.
2. Emojification of tone: NOT PRESENT. Zero emoji used as voice signal. The single "I ♥ San Vito" reference is inside scare-quotes describing souvenir T-shirts.
3. Mamma mia Italian stereotype: NOT PRESENT. Italian words used (*papà*, *passeggiata*, *Santuario di San Vito*, *busiate alla Trapanese*, *pani cunzato*, *nonno*, *nonni*, *zio Nunzio*, *Sicilian shower*, *caldo freddo*, *cous cous di pesce*, *Profumi di Couscous*, *gambero rosso*, *mattanza*, *Quantu spenni, manci*, *buonissimo*, *tranquillità*, *paesano*, *nonna*, *Tonnara del Secco*, *Sicilia*, *bellissima*, *bellissime*, *Segesta*, *gelato*) are all functional or proper-noun. None are decorative seasoning.
4. Compound sentence drag: NOT PRESENT. Brain Dump dictation rhythm converted to writing rhythm. test_voice_checklist.py reports 0 compound-sentence violations across all 14 H2 sections.
5. Objective recommendation: NOT PRESENT. Every option is opinionated. August = "Avoid". Russo via Trapani = "pilgrimage route". Rental car = "the option I push hardest".
6. Bullet massacre: NOT PRESENT. Bullets used only for enumerable items (3 what-you'll-learn bullets in opener, 3 link cards in Continue Planning). All other sections are prose.

All 6 failure modes cleared.

---

## Banned Phrases Audit (WAP_05c Section 5 + WAP_05d Section 1A)

Pre-fix scan of `07_Draft_Info.md` found 3 banned-phrase hits:

1. "embark on" inside scare-quoted mock in Element 4 ("No 'embark on a journey.'")
2. "stunning" used to describe coves at H2-6 Zingaro trail expectations
3. "Don't miss it" closing line at H2-7 Couscous

All three are HARD-FAIL triggers under WAP_05d Section 1A literal substring scan, case-insensitive, no scare-quote exemption.

Fixes applied in `08_Draft_Voice.md`:

1. Element 4 Nico self-intro: "No 'embark on a journey.'" became "No fake-poetic openings."
2. H2-6 Zingaro trail: "The coves themselves are stunning but the bottoms are rocky" became "The coves themselves are *bellissime*, but the bottoms are rocky"
3. H2-7 Couscous closing: "Don't miss it." became "Eat it."

Final scan result: 0 banned phrases across all 14 H2 sections. Confirmed by test_voice_checklist.py run.

---

## Em-dash Audit (WAP_05c Section 3 + WAP_05d Section 1B)

The `07_Draft_Info.md` source contained 102 em-dashes. All converted to alternative punctuation in `08_Draft_Voice.md` per voice geometry rules.

Conversion patterns applied:

- Parenthetical em-dash pair became commas or parentheses
- Em-dash before list or clarifier became colon or period
- Em-dash for snap rhythm became period, creating staccato fragments
- Em-dash inside quoted dialog became comma or period

Final scan: 0 em-dashes in `08_Draft_Voice.md` body. Confirmed by test_voice_checklist.py run (article-level em-dash check: PASS).

---

## All-caps + Rhetorical Questions Audit (WAP_05d Section 1B)

All-caps phrases article-wide (threshold ≥1):

- "DO NOT drive inside San Vito itself." (H2-3 rental car warning)
- "Avoid." in H2-8 month table (August row verdict)

Plus the meta-header all-caps detected by the tool (URL, REFRESH, CONFIRMED, PR, TL, DR, PMO).

Rhetorical questions article-wide: 41 detected. Threshold (≥1) cleared by a wide margin. Sample:

- "Wrong call here?" (H2-2 base vs day-trip)
- "Why would you take this?" (H2-3 Segesta route)
- "Why?" (H2-7 Busiate, pesto colour)
- "Expensive or cheap?" (H2-10 cost)
- "Outside that?" (H2-8 when to come)
- "Arrive in August?" (H2-1 worth visiting)
- "August your only option?" (H2-1 worth visiting)
- "Want to compare lidos?" (H2-5 lido)
- "Landing late at Palermo airport?" (H2-3 private transfer)
- "Long-stay couple (5+ nights)?" (H2-9 where to stay)

Both article-level thresholds cleared.

---

## DNA Trait Amplification per Persona (Phase 4 lands-hardest list)

Phase 4 §5 confirmed Persona A lands hardest with Trait 1 (Anti-Romantic Pragmatist), Trait 5 (Scam Radar Disclosure), Trait 6 (Staccato Absolutes), Trait 8 (Setup-Pause-Snap), Device 6 (Numerical Slap). Amplification verification:

- Trait 1 amplified in H2-1 opener (August water, postcard photos), H2-3 rental warning, H2-8 when to come, Bottom Line.
- Trait 5 amplified in H2-3 (police ticket trap), H2-5 (lido pricing transparency), H2-9 (Don't be cheap rule), H2-10 (Pre-booking is the single biggest lever).
- Trait 6 amplified in H2-1 ("It depends."), H2-2 ("Don't base in San Vito."), H2-3 ("DO NOT drive inside San Vito itself."), H2-8 ("Late May. All of June. All of September. Early October."), Bottom Line ("Skip August unless you've no choice.").
- Trait 8 amplified in H2-1 ("Half of Italy is there. Not half of Sicily, half of *Italy*."), H2-4 ("That's the entire vibe. *Tranquillità*."), H2-5 ("That split is the entire negotiation."), H2-10 ("The elephant in the room.").
- Device 6 saturated article-wide: €120-150/night, lido €28-35/day, dinner ~€50, cocktail €10-12, gelato €3-4, espresso ~€1.50, parking €10-15/day, Russo €11-12, GYG transfer €100-130, Zingaro €5/€3, Couscous Fest €15, drive-times 1h15/45min/50min/30min, Cous Cous Fest dates 18-27 Sep 2026, etc.

Sparing-use traits per Phase 4:

- Trait 10 family cast: only Ciccio (H2-6) and *papà* (Element 4 + H2-1 Local's Take). Both article-native. No new family-cast seeded.
- Trait 11 deep Italian-American refs: Kardashian-selfies (H2-7 Busiate) and Hitler's bombs (H2-7 Caldo Freddo) preserved as Persona A-compatible. No Maniscalco-specific or deep Goodfellas references added.

Amplification compliant with Phase 4 framing.

---

## Voice Geometry Audit (WAP_05d Section 1, full result table)

Per-section result from test_voice_checklist.py v2.0 final run:

| H2 # | Section | Status |
|---|---|---|
| 1 | Opening Sequence | PASS |
| 2 | Is San Vito Lo Capo worth visiting? The honest answer | PASS |
| 3 | Should you base in San Vito or day-trip from Palermo? | PASS |
| 4 | How to get to San Vito Lo Capo from Palermo | PASS |
| 5 | What the village actually feels like | PASS |
| 6 | San Vito beaches: free vs lido, 2026 prices | PASS |
| 7 | Riserva dello Zingaro | PASS |
| 8 | What to eat in San Vito Lo Capo | PASS |
| 9 | When to come to San Vito Lo Capo | PASS |
| 10 | Where to stay in San Vito Lo Capo | PASS |
| 11 | How much does it cost in peak season (2026) | PASS |
| 12 | Bottom Line | PASS |
| 13 | FAQ | PASS |
| 14 | Continue Planning Your Sicily Trip | PASS |

Total: 14 PASS / 0 FAIL out of 14.

Article-level checks:

- All-caps phrases: 9 found, threshold ≥1, PASS.
- Em-dashes: 0 found, threshold 0, PASS.
- Rhetorical questions: 41 found, threshold ≥1, PASS.

Article-level: PASS.

---

## Cultural Adaptation Carry-over (from Phase 7)

The Cultural Adaptation Log from `07_Draft_Info.md` (22 rows covering Italian idioms, family-cast references, Sicilian dialect, untranslated food terms, and Italian-audience pop refs) is preserved by reference. All verbatim retentions survive intact in `08_Draft_Voice.md`:

- *papà* (Element 4, H2-1 Local's Take)
- *nonno*, *nonni* (H2-3 rental warning)
- Ciccio (H2-6 Zingaro)
- *Sicilian shower* (H2-4 village feel)
- Grandpas with tomato sauce stains (H2-4 village feel)
- *Quantu spenni, manci* (H2-10 cost)
- *caldo freddo* (H2-7)
- *busiate*, *pesto alla Trapanese* (H2-7)
- *mattanza* (H2-7 tuna callout)
- *cous cous di pesce*, *Profumi di Couscous* (H2-7)
- Kardashian-selfies pop ref (H2-7 Busiate)
- Hitler's bombs pop ref (H2-7 Caldo Freddo)
- *zio Nunzio* (H2-5 free beach access)
- *gambero rosso* (H2-10 cost)

No new family-cast references seeded. No new Italian-American pop refs added. Persona A cultural-adaptation discipline maintained per Phase 4 §5.

---

## Test Harness Result

Command: `python3 tools/test_voice_checklist.py projects/POST_san-vito-lo-capo/08_Draft_Voice.md`

Final run output:

```
=== WAP_05d Voice Checklist v2.0, Multi-format Voice DNA Compliance Detector ===
Article: 08_Draft_Voice.md [Markdown]
Total H2 sections: 14

[per-section detail in full run, all 14 sections PASS]

=== ARTICLE-LEVEL CHECKS ===
  All-caps: 9 found (threshold >= 1) -- PASS
  Em-dashes: 0 found (threshold 0) -- PASS
  Rhetorical questions (article-wide): 41 (threshold >= 1) -- PASS

=== SUMMARY ===
Sections: 14 PASS / 0 FAIL out of 14 checked (0 skipped)
Article-level: PASS
```

WAP_05d Section 3 pass criteria check:

- Every H2 individually passes: YES (14/14)
- Section 1B article-level counts pass: YES (≥1 all-caps, 0 em-dashes)
- Section 2 verbatim evidence ≥5/11 traits with quote: YES (11/11)
- Zero banned phrases anywhere in article: YES (0 found)

Result: Article PASSES Phase 8 Voice Pass.

---

## Iteration Log

Iteration 1: initial draft. Failed on em-dashes (29 in audit-meta H2 headers), 3 banned phrases (stunning, embark on, Don't miss), compound sentences widespread, single-sentence paragraph ratio below threshold in 12 sections.

Iteration 2: removed meta-audit H2 wrappers (moved to companion file `08_Draft_Voice_Audit.md`), fixed all banned phrases, converted em-dashes to commas/periods/colons. 1 section PASS, 13 FAIL. Compound sentences and paragraph-break issues remain.

Iteration 3: aggressive compound-sentence splits (removed "and"/"because" connectors in 15+ word sentences), broke long paragraphs into single-sentence punches. 4 sections PASS, 10 FAIL.

Iteration 4: continued paragraph breaks across H2-5/6/7/8/10/11/12. Added italics in H2-3, H2-7, H2-10 (*Segesta*, *gelato*, *Tonnara del Secco*, *bellissime*, *fancy*, *kitchen flexibility*). 9 sections PASS, 5 FAIL.

Iteration 5: balanced avg sentence length (combined some fragments back where avg fell below 7.0), added 1-sentence paragraph breaks where threshold missed. 13 sections PASS, 1 FAIL.

Iteration 6: final fix on H2-1 Opening Sequence single-sentence paragraph ratio (split "Half of that is true." into its own paragraph and "The other half? The part nobody writes." into a separate paragraph). 14 sections PASS, 0 FAIL. Article-level PASS.

Total iterations to PASS: 6.

---

## Next Phase

Output `08_Draft_Voice.md` is locked. Phase 9 (HTML) consumes `08_Draft_Voice.md` as input. WAP_06c snippets applied at Phase 9.
