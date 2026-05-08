# WAP_05d Voice Checklist — Test 1 (Backwards Validation)

## Test setup
- **Date:** May 8, 2026
- **Article tested:** tools/test_articles/where-to-stay-palermo.html
- **Test type:** Backwards — checklist applied to known Nico-approved article. Expected: should PASS most/all sections.
- **Purpose:** Validate that current WAP_05d thresholds correctly recognize Nico voice as good.

## Methodology
- Parsed HTML with BeautifulSoup/lxml
- Extracted entry-content div only
- Stripped: hotel cards (box-shadow), FAQ details blocks, TL;DR blue box, callout divs, affiliate disclosure, divTable Pros/Cons/Advice blocks, Continue Planning grey box
- Split at H2 boundaries into 9 sections
- Applied all WAP_05d Section 1 mechanical checks
- H2 #8 (FAQ) correctly shows 0 words because all content was inside excluded `<details>` tags

## Results per H2

### H2 #1: The 3 Areas of Palermo (Pick Yours in 30 Seconds) — 366 words — FAIL (4 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 20 | ≥2 | PASS |
| Single-sentence paragraphs | 1/13 (8%) | ≥40% | **FAIL** |
| Italics | 5 | ≥3 | PASS |
| Ellipsis | 0 | ≥2 | **FAIL** |
| Rhetorical questions | 3 | ≥1 | PASS |
| Banned phrases | 0 | 0 | PASS |
| Max sentences/paragraph | 10 (4 paras over) | max 3 | **FAIL** |
| Bullet ratio | 0/13 (0%) | ≤30% | PASS |
| Avg sentence length | 7.3 words | 9-12 | **FAIL** |
| Compound sentences | 1 | max 2 | PASS |
| Contractions density | 82% | ≥80% | PASS |

### H2 #2: Centro Storico, the Real, Raw Heart — 588 words — FAIL (5 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 29 | ≥3 | PASS |
| Single-sentence paragraphs | 15/43 (35%) | ≥40% | **FAIL** |
| Italics | 11 | ≥3 | PASS |
| Ellipsis | 0 | ≥2 | **FAIL** |
| Rhetorical questions | 4 | ≥1 | PASS |
| Banned phrases | 1 ("charming") | 0 | **HARD-FAIL** |
| Max sentences/paragraph | 7 (7 paras over) | max 3 | **FAIL** |
| Bullet ratio | 0/43 (0%) | ≤30% | PASS |
| Avg sentence length | 6.8 words | 9-12 | **FAIL** |
| Compound sentences | 2 | max 2 | PASS |
| Contractions density | 92% | ≥80% | PASS |

### H2 #3: Politeama-Libertà, the Polished Zone — 222 words — FAIL (3 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 21 | ≥2 | PASS |
| Single-sentence paragraphs | 4/17 (24%) | ≥40% | **FAIL** |
| Italics | 2 | ≥1 | PASS |
| Ellipsis | 0 | N/A (≤300w) | PASS |
| Rhetorical questions | 3 | ≥1 | PASS |
| Banned phrases | 0 | 0 | PASS |
| Max sentences/paragraph | 12 (4 paras over) | max 3 | **FAIL** |
| Bullet ratio | 0/17 (0%) | ≤30% | PASS |
| Avg sentence length | 5.7 words | 9-12 | **FAIL** |
| Compound sentences | 2 | max 2 | PASS |
| Contractions density | 100% | ≥80% | PASS |

### H2 #4: Mondello, the Seaside Escape — 534 words — FAIL (5 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 25 | ≥3 | PASS |
| Single-sentence paragraphs | 13/43 (30%) | ≥40% | **FAIL** |
| Italics | 11 | ≥3 | PASS |
| Ellipsis | 0 | ≥2 | **FAIL** |
| Rhetorical questions | 6 | ≥1 | PASS |
| Banned phrases | 0 | 0 | PASS |
| Max sentences/paragraph | 5 (4 paras over) | max 3 | **FAIL** |
| Bullet ratio | 0/43 (0%) | ≤30% | PASS |
| Avg sentence length | 6.8 words | 9-12 | **FAIL** |
| Compound sentences | 5 | max 2 | **FAIL** |
| Contractions density | 91% | ≥80% | PASS |

### H2 #5: Cefalù, the Smarter Alternative — 508 words — FAIL (4 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 37 | ≥3 | PASS |
| Single-sentence paragraphs | 10/34 (29%) | ≥40% | **FAIL** |
| Italics | 7 | ≥3 | PASS |
| Ellipsis | 0 | ≥2 | **FAIL** |
| Rhetorical questions | 6 | ≥1 | PASS |
| Banned phrases | 0 | 0 | PASS |
| Max sentences/paragraph | 6 (7 paras over) | max 3 | **FAIL** |
| Bullet ratio | 2/36 (6%) | ≤30% | PASS |
| Avg sentence length | 6.4 words | 9-12 | **FAIL** |
| Compound sentences | 1 | max 2 | PASS |
| Contractions density | 85% | ≥80% | PASS |

### H2 #6: Apartment, B&B, Hotel, or Villa? — 531 words — FAIL (6 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 20 | ≥3 | PASS |
| Single-sentence paragraphs | 12/40 (30%) | ≥40% | **FAIL** |
| Italics | 9 | ≥3 | PASS |
| Ellipsis | 0 | ≥2 | **FAIL** |
| Rhetorical questions | 10 | ≥1 | PASS |
| Banned phrases | 1 ("charming") | 0 | **HARD-FAIL** |
| Max sentences/paragraph | 6 (4 paras over) | max 3 | **FAIL** |
| Bullet ratio | 0/40 (0%) | ≤30% | PASS |
| Avg sentence length | 7.1 words | 9-12 | **FAIL** |
| Compound sentences | 4 | max 2 | **FAIL** |
| Contractions density | 95% | ≥80% | PASS |

### H2 #7: Pricing Reality 2026 — 365 words — FAIL (5 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 14 | ≥2 | PASS |
| Single-sentence paragraphs | 10/28 (36%) | ≥40% | **FAIL** |
| Italics | 10 | ≥3 | PASS |
| Ellipsis | 0 | ≥2 | **FAIL** |
| Rhetorical questions | 3 | ≥1 | PASS |
| Banned phrases | 0 | 0 | PASS |
| Max sentences/paragraph | 5 (4 paras over) | max 3 | **FAIL** |
| Bullet ratio | 0/28 (0%) | ≤30% | PASS |
| Avg sentence length | 7.3 words | 9-12 | **FAIL** |
| Compound sentences | 5 | max 2 | **FAIL** |
| Contractions density | 92% | ≥80% | PASS |

### H2 #8: FAQ — 0 words — FAIL (5 checks, expected — all content excluded)
All content correctly excluded (inside `<details>` tags). Section is an empty shell. This section should be SKIPPED by the checklist, not counted.

### H2 #9: Bottom Line — 237 words — FAIL (3 checks)
| Check | Value | Threshold | Result |
|---|---|---|---|
| Sentences ≤3 words | 18 | ≥2 | PASS |
| Single-sentence paragraphs | 4/11 (36%) | ≥40% | **FAIL** |
| Italics | 8 | ≥1 | PASS |
| Ellipsis | 0 | N/A (≤300w) | PASS |
| Rhetorical questions | 7 | ≥1 | PASS |
| Banned phrases | 0 | 0 | PASS |
| Max sentences/paragraph | 4 (1 para over) | max 3 | **FAIL** |
| Bullet ratio | 1/12 (8%) | ≤30% | PASS |
| Avg sentence length | 4.9 words | 9-12 | **FAIL** |
| Compound sentences | 0 | max 2 | PASS |
| Contractions density | 100% | ≥80% | PASS |

## Article-level summary

| Check | Value | Threshold | Result |
|---|---|---|---|
| All-caps words | 10 | ≥1 | PASS |
| Em-dashes | 0 | 0 | PASS |

**Sections: 0 PASS / 9 FAIL out of 9 total**
**Article-level: PASS**

## Fail Pattern Analysis

| Check | Sections failed | % | Classification |
|---|---|---|---|
| Single-sentence paragraphs | 9/9 | 100% | **THRESHOLD TOO HIGH** or **PARSER ISSUE** |
| Max sentences/paragraph | 8/9 | 89% | **PARSER ISSUE** (likely) |
| Avg sentence length | 8/9 | 89% | **PARSER ISSUE** (avg 4.9-7.3 vs target 9-12 — sentences over-split) |
| Ellipsis | 6/9 | 67% | **THRESHOLD MAYBE TOO HIGH** or Nico doesn't use ellipsis in this article |
| Compound sentences | 3/9 | 33% | **THRESHOLD TOO TIGHT** (max 2 per H2 too aggressive for 500+ word sections) |
| Banned phrases | 2/9 | 22% | **REAL FINDING** — "charming" appears twice in the Nico-approved article |
| Sentences ≤3 words | 1/9 | 11% | OK (only FAQ empty section) |
| Italics | 1/9 | 11% | OK (only FAQ empty section) |
| Rhetorical questions | 1/9 | 11% | OK (only FAQ empty section) |
| Bullet ratio | 0/9 | 0% | OK |
| Contractions density | 0/9 | 0% | OK |

## Diagnosis

**The checklist FAILS its own gold-standard article.** 0/9 sections pass. This means the thresholds are miscalibrated — they reject known-good Nico voice as bad.

### Root causes (3 categories):

#### 1. PARSER ISSUES (must fix in script, not thresholds)

**Avg sentence length 4.9-7.3 words (target 9-12):** The sentence splitter is over-splitting. HTML content has inline elements, abbreviations, numbers with periods, and hotel card data remnants that create false sentence boundaries. Real Nico sentences average 9-12 words as measured by Gemini on the Tourist Info script. The parser needs to be smarter about sentence boundaries (ignore periods inside abbreviations, numbers, etc.) or the threshold needs to accommodate HTML-specific deflation.

**Max sentences/paragraph 89% fail:** Same root cause. If sentences are over-split, paragraphs appear to have more sentences than they actually do. A paragraph with 2 real sentences might register as 5 if the splitter fragments on "Dr.", "€59.", "No. 1", etc.

**Single-sentence paragraphs 100% fail at 40%:** Partially parser (if paragraphs are counted incorrectly due to HTML structure) and partially threshold. The 40% target was calibrated against the Tourist Info VIDEO SCRIPT, which has more staccato rhythm than a formatted HTML article with hotel cards and structured data.

#### 2. THRESHOLD ISSUES (must recalibrate)

**Ellipsis 67% fail:** Nico uses ellipsis in video scripts but NOT in this HTML article. The where-to-stay article uses em-dashes (wait — that's banned!) and bold/italic for pauses instead. The ellipsis threshold should be relaxed: minimum 1 (not 2) for >300w sections, OR make ellipsis a WARN not FAIL.

**Compound sentences max 2 per H2:** Too tight for 500+ word sections. Sections 4, 6, 7 have 4-5 compound sentences each. For long sections (>400 words), the threshold should scale — suggest max ceil(section_words / 200) instead of flat 2.

**Single-sentence paragraphs 40%:** Too high for HTML articles. HTML has structural paragraphs (containing images, links, callouts) that aren't single-sentence prose. Suggest lowering to 25-30%.

#### 3. REAL FINDINGS (article issues, not threshold issues)

**"charming" banned phrase in sections 2 and 6:** This is a legitimate catch. The word "charming" appears in the Nico-approved article and IS on the banned list. Whether to remove it from the banned list (Nico uses it intentionally in context) or fix the article is Nico's call.

### Summary classification

| Issue type | Checks affected | Action |
|---|---|---|
| Parser over-splitting sentences | avg sentence length, max sentences/para, single-sentence % | Fix parser |
| Threshold too tight for HTML articles | ellipsis, compound sentences, single-sentence % | Recalibrate WAP_05d v1.1 |
| Real article finding | banned phrase "charming" | Nico decision |

## Calibration recommendations for WAP_05d v1.1

1. **Fix sentence splitter** — use NLTK or spaCy sentence tokenizer instead of naive regex on `.!?`. This alone would likely fix avg sentence length + max sentences/para.
2. **Ellipsis threshold** — change from "minimum 2 if >300w" to "minimum 1 if >300w" OR make it WARN not FAIL.
3. **Compound sentences** — change from "max 2 per H2" to "max ceil(section_words / 200)" (scales with section size).
4. **Single-sentence paragraphs** — lower from 40% to 25%.
5. **FAQ section** — add explicit skip rule: if H2 has 0 words after exclusions, skip it entirely (don't count as FAIL).
6. **"charming" on banned list** — review with Nico. May need context-dependent exception.

## Next step

Draft WAP_05d v1.1 with calibrated thresholds + improved parser. Then re-run Test 1 to confirm gold-standard article passes.

---

## Test 1 — Round 2 (post-calibration v1.1)

**Date:** May 8, 2026 (evening)

### Calibration applied
- Parser fixed (NLTK sent_tokenize replacing naive regex — fixes over-splitting on abbreviations/prices)
- Single-sentence paragraphs: 40% → 25%
- Paragraph length: hard cap 3 → soft cap (max 2 paragraphs may exceed 3 sentences per H2)
- Ellipsis if >300w: ≥2 → ≥1
- Italics: skip rule for sections ≤100 words
- Rhetorical questions: moved from per-H2 to article-level (≥1 article-wide)
- FAQ skip rule added (single-sentence% + paragraph cap exempt for Q&A sections)
- Banned: "charming" removed as standalone, added composite phrases ("charming little", "charming village", etc.)

### Results post-calibration

**Sections: 0 PASS / 8 FAIL out of 8 checked (1 skipped — FAQ correctly excluded)**

| H2 | Words | Fails | Failed checks |
|---|---|---|---|
| #1 The 3 Areas | 366 | 4 | single-sent 8%, ellipsis 0, max sent/para 4 over, avg 7.8w |
| #2 Centro Storico | 588 | 3 | ellipsis 0, max sent/para 5 over, avg 7.9w |
| #3 Politeama | 222 | 3 | single-sent 24%, max sent/para 4 over, avg 5.7w |
| #4 Mondello | 534 | 4 | ellipsis 0, max sent/para 4 over, avg 6.8w, compound 5 |
| #5 Cefalù | 508 | 3 | ellipsis 0, max sent/para 5 over, avg 7.0w |
| #6 Apartment/Hotel | 531 | 4 | ellipsis 0, max sent/para 4 over, avg 7.1w, compound 4 |
| #7 Pricing | 365 | 4 | ellipsis 0, max sent/para 4 over, avg 7.3w, compound 5 |
| #8 FAQ | 0 | — | Skipped (FAQ exempt) |
| #9 Bottom Line | 237 | 1 | avg 5.3w |

Article-level: PASS (all-caps 2, em-dashes 0, rhetorical questions 46)

### Fail pattern analysis post-calibration

| Check | Sections failed v1.0 | Sections failed v1.1 | Δ |
|---|---|---|---|
| Avg sentence length | 8/9 (89%) | 8/8 (100%) | **PERSISTENT — primary remaining issue** |
| Max sentences/paragraph | 8/9 (89%) | 7/8 (88%) | Marginal improvement (soft cap helped Bottom Line pass) |
| Ellipsis | 6/9 (67%) | 6/8 (75%) | Lowered threshold helped but 0 ellipsis in entire article |
| Compound sentences | 3/9 (33%) | 3/8 (38%) | No change |
| Single-sentence paragraphs | 9/9 (100%) | 2/8 (25%) | **FIXED** (40%→25% threshold + better NLTK counting) |
| Banned phrases | 2/9 (22%) | 0/8 (0%) | **FIXED** ("charming" standalone removed) |

### Improvements from v1.0 → v1.1

1. **Single-sentence paragraphs: 100% fail → 25% fail.** The 40%→25% threshold + NLTK fix was the right move. 6/8 sections now pass this check.
2. **Banned phrases: 22% fail → 0% fail.** "charming" standalone removed, composite phrases added. No false positives.
3. **FAQ section correctly skipped** instead of counting as FAIL.
4. **Rhetorical questions now article-level** — 46 found, easily passes.

### Remaining problems (3 checks still systematically failing)

**1. Average sentence length (100% fail):** avg 5.3-7.9 words across all sections. Target 9-12. NLTK improved from 4.9-7.3 to 5.3-7.9 but not enough. Root cause: HTML articles have many structural fragments (bold hotel names, price lines, standalone numbers) that NLTK correctly treats as sentences but that aren't "prose sentences." The 9-12 target was calibrated from Nico's VIDEO SCRIPTS which are continuous prose. HTML articles structurally have shorter average because they mix prose with data.

**Recommendation:** Lower target to 7-12 words for HTML articles. Or make avg sentence length a WARN not FAIL.

**2. Max sentences/paragraph (88% fail):** NLTK counts are better but HTML paragraphs with rich formatting (bold + italic + links) still register as multi-sentence. The soft cap (max 2 paras over 3 sentences) helped Bottom Line (#9) pass but larger sections still have 4-5 paragraphs over.

**Recommendation:** Raise soft cap to max 4 paragraphs exceeding 3 sentences per H2. Or make it proportional: max ceil(section_paragraphs * 0.15).

**3. Ellipsis (75% fail):** Nico simply does NOT use ellipsis in this article. Zero across the entire article. The threshold assumes ellipsis is a voice marker but in HTML articles, Nico uses other pause devices (bold, italics, short fragments).

**Recommendation:** Make ellipsis WARN not FAIL. Or remove from required checks entirely (track but don't enforce).

### Diagnosis post-calibration

**WAP_05d v1.1 is NOT ready for production.** 0/8 sections pass. The three remaining issues are all threshold/classification problems, not parser problems. Need one more calibration round (v1.2) targeting:
1. Avg sentence length: lower target or make WARN
2. Max sentences/paragraph: raise soft cap
3. Ellipsis: make WARN or remove

### Next step

v1.2 calibration round targeting the 3 remaining systematic failures. Expected: if all 3 are addressed, most sections should pass (Bottom Line already passes with only avg sentence length failing).

---

## Test 1 — Round 3 (post-calibration v1.2)

**Date:** May 8, 2026 (evening)

### Calibration applied (v1.2 over v1.1)
- Avg sentence length: lower bound 9 → 7 (PASS if 7-12, WARN 13-15, FAIL >15 or <7)
- Max paragraphs >3 sentences: 2 → 4 per H2 (or ≤50% threshold, whichever permissive)
- Ellipsis ≥1 if >300w: demoted from FAIL to WARN (informational only)
- Introduced WARN vs FAIL distinction (WARNs do not block pass)

### Results post-calibration v1.2

**Sections: 1 PASS / 7 FAIL out of 8 checked (1 FAQ skipped)**

| H2 | Words | Result | Fails | WARNs | Details |
|---|---|---|---|---|---|
| #1 The 3 Areas | 366 | FAIL (1) | single-sent 8% | ellipsis 0 | Only single-sent% still failing |
| #2 Centro Storico | 588 | **PASS** | 0 | ellipsis 0 | First PASS! All mechanical checks green |
| #3 Politeama | 222 | FAIL (2) | single-sent 24%, avg 5.7w | — | Short section, fragment-heavy |
| #4 Mondello | 534 | FAIL (2) | avg 6.8w, compound 5 | ellipsis 0 | Avg just below 7w floor |
| #5 Cefalù | 508 | FAIL (1) | avg 7.0w | ellipsis 0 | avg 7.0 rounds to exactly 7.0 — borderline FAIL at <7 |
| #6 Apartment/Hotel | 531 | FAIL (1) | compound 4 | ellipsis 0 | Only compound sentences exceeding max 2 |
| #7 Pricing | 365 | FAIL (1) | compound 5 | ellipsis 0 | Same: compound sentences only |
| #8 FAQ | 0 | Skipped | — | — | FAQ exempt |
| #9 Bottom Line | 237 | FAIL (1) | avg 5.3w | — | Short section, fragment-heavy |

Article-level: PASS (all-caps 2, em-dashes 0, rhetorical questions 46)

### Fail pattern analysis v1.2

| Check | v1.0 | v1.1 | v1.2 | Δ trend |
|---|---|---|---|---|
| Avg sentence length | 89% | 100% | **50%** | Major improvement (floor 9→7) |
| Max sentences/paragraph | 89% | 88% | **0%** | **FIXED** (cap 2→4 + 50%) |
| Ellipsis | 67% | 75% | **0%** | **FIXED** (FAIL→WARN) |
| Compound sentences | 33% | 38% | **38%** | Persistent — 3 sections still fail |
| Single-sentence paragraphs | 100% | 25% | **25%** | Stable since v1.1 |
| Banned phrases | 22% | 0% | **0%** | Fixed since v1.1 |

### Remaining problems (2 checks)

**1. Avg sentence length (50% fail):** 4/8 sections fail with avg 5.3-7.0 words. The 7.0 floor catches sections that are exactly at the boundary. Sections #3 (5.7w), #4 (6.8w), #5 (7.0w), #9 (5.3w) all fail. These are genuinely fragment-heavy sections (Politeama is 222 words of mostly hotel card context, Bottom Line is 237 words of sign-off).

**Root cause:** Short sections (≤300w) and sections with extensive hotel-card-adjacent content have structurally lower avg sentence length because the non-excluded prose around cards is fragmentary (names, prices, brief descriptions). This is a format issue, not a voice issue.

**2. Compound sentences (38% fail):** 3/8 sections have 4-5 compound sentences vs max 2. Sections #4 (Mondello 534w, 5 compounds), #6 (Apartment/Hotel 531w, 4 compounds), #7 (Pricing 365w, 5 compounds). These longer sections naturally contain more compound structures.

**Root cause:** The max-2 flat cap doesn't scale with section length. A 530-word section at 4 compounds is 1 compound per 133 words — not excessive. The flat cap was designed for 200-word sections.

### Diagnosis v1.2

**Significant progress.** From 0/9 PASS (v1.0) → 0/8 PASS (v1.1) → **1/8 PASS (v1.2)**. Centro Storico (the largest prose section at 588 words) passes cleanly, which is the strongest validation signal — the checklist correctly recognizes the meatiest Nico-voice section.

The remaining 7 FAILs are all 1-2 check failures, NOT 4-6 check failures like v1.0. The checklist is close to production-ready. Two more threshold adjustments would likely bring it to 5-6/8 PASS:

1. **Avg sentence length floor 7 → 5** (or remove lower bound entirely for sections ≤300w)
2. **Compound sentences max 2 → scale to ceil(section_words / 150)** (approximately 1 compound per 150 words)

### Next step

Decision for Nico: accept v1.2 as-is (1/8 PASS but Centro Storico validates core voice recognition), OR do v1.3 with avg-floor and compound-scaling adjustments (expected 5-6/8 PASS).
