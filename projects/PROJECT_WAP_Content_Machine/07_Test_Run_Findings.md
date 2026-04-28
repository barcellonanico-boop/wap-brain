# 07 — Test Run Findings

**Purpose:** Living log of every issue, gap, mistake, missing rule, and improvement opportunity discovered during the SOP_01 Phase 3 test run on /where-to-stay-palermo/. Findings captured as they emerged. At end of test, distilled lessons get promoted to Brain doc updates and SOP_01 v2.0 patches.

**Started:** April 27, 2026
**Test target:** /where-to-stay-palermo/ (P1 Tier A, -2,012 clicks YoY)
**Status:** Test STOPPED at Step 6 v2 review (Apr 27, 15:12). Output quality unacceptable. Decision: stop test, redesign SOP_01 from the ground up.

---

## Findings Log

| # | When Found | Step | Severity | Finding | Fix Path |
|---|---|---|---|---|---|
| 1 | Apr 26 | Pre-Step-1 | High | SOP_01 v1.1 has no formal Structural Audit step. Some posts need restructuring before voice rewriting. | Patch SOP_01 with formal Step 2.5 Structural Audit between Prep and Rewrite. |
| 2 | Apr 27, Step 2 | Step 2 | Medium | Free walking tour internal links rejected by Nico (conflict with Sicilian Way premium guide). | Add "Free vs Paid Content Conflict" rule to WAP_03 or WAP_06. Update Architect agent prompt. |
| 3 | Apr 27, Step 2 | Step 2 | Medium | WAP_04 says /where-to-stay-palermo/ status RANKING; WAP_13 says ROTTING. Two docs conflict. | Reconcile: WAP_04 references WAP_13 as canonical for status. |
| 4 | Apr 27, Step 2 | Step 2 | Medium | Live post SEO title vs H1 mismatch ("3 Top Areas... 2025" vs "Where to Stay... Trip"). Year-stamped title hurts freshness in 2026. | Add SEO/H1 sync rule to WAP_06. |
| 5 | Apr 27, Step 2 | Step 2 | Medium | Architect couldn't verify schema via web_fetch (strips JSON-LD) or bash curl (domain not allowlisted). | Allowlist wearepalermo.com for bash, OR add Step 2 sub-task: PM runs Google Rich Results Test before Step 3. |
| 6 | Apr 27, Step 2.5 | Step 2.5 | Low | Centro Storico = unified single area is Nico's local truth, not 4 sub-neighborhoods. | Add to WAP_05 as permanent local-truth rule. |
| 7 | Apr 27, Step 2.5 | Step 2.5 | Low | Vucciria fact lock: NOT a working morning fish market. It's restaurant/nightlife. Capo and Ballarò are working markets. | Add Vucciria fact to WAP_10 entry. Add to WAP_05 as fact lock. |
| 8 | Apr 27, Step 3 | Step 3 | High | Copywriting produced markdown, post needs HTML for WordPress. Output format unspecified. | Update SOP_01 Step 3 prompt template: HTML mandatory for SOP_01 (existing post rewrites). |
| 9 | Apr 27, Step 5 | Step 5 | High | v1 used generic Pro Tip blocks instead of WAP_06 Local's Take/Pick/Warning templates. Required min 1 box per H2 / 1 per ~300 words. v1 had 2 in 3,470 words. | Patch Copywriting agent system prompt: enforce WAP_06 text box compliance (Variants 1/2/3 only, frequency rule, mix variants). |
| 10 | Apr 27, Step 5 | Step 5 | High | v1 jumped from affiliate disclosure to TL;DR with no Nico intro. Cold readers don't know who's writing. | Update WAP_06 post structure rule: Nico intro MUST precede TL;DR. Order: Italic lead → Featured image → Nico intro (~80 words) → Affiliate disclosure → TL;DR. |
| 11 | Apr 27, Step 5 | Step 5 | High | Single-pass writing (info + structure + voice + format + HTML in one go) produces flat tone of voice. Voice attention split. | Patch SOP_01 to v2.0 with 3-pass writing model: Step 3a (Info & Structure, markdown), Step 3b (Trimming & Voice, markdown), Step 3c (Format & HTML). Each pass = separate Copywriting handoff. PM gates each pass. |
| 12 | Apr 27, Step 5 | Step 5 | Medium | v1 missed reader-need answers per area: walking size, cleanliness, airport connection, supermarket availability, restaurant coverage. | Add to WAP_06 "Cold Reader Reality Check" checklist for area/where-to-stay posts. Update SOP_01 Step 2.5 to include checklist. |
| 13 | Apr 27, Step 5 | Step 5 | Medium | Wall-of-text paragraphs survived. WAP_06 max is 2 sentences or 45 words. | Reinforce in WAP_06: rule mandatory not aspirational. Step 3c (Format) explicitly breaks long paragraphs as final cleanup. |
| 14 | Apr 27, Step 4 | Step 4 | Medium | Scout caught 4 disputed facts: ZTL fine €164 not €160, Unico Boutique 4-star not 5, B&B Mondello stars conflict, Villa Gabriella 300 sqm unverified. | No Scout patch needed. Add to Copywriting prompt: when stating star ratings, verify against hotel's own official site, not aggregators. |
| 15 | Apr 27, Step 5 | Step 5 | Medium | Star rating convention inconsistent: government Giata stars mixed with editorial stars on apartments/vacation rentals. | Add to WAP_06: stars only on officially classified hotels. Apartments/B&Bs/rentals: descriptive tagline only, no stars. |
| 16 | Apr 27, Step 5 | Step 5 | Low | "Continue Your Palermo Planning" block required by WAP_06 at end. v1 had social CTAs instead. | Reinforce in Copywriting agent prompt and SOP_01 Step 3c. Continue Planning block mandatory. Social CTAs separate. |
| 17 | Apr 27, Step 5 | Step 5 | Low | v1 affiliate disclosure was generic. WAP_06 requires Nico-voiced version. | Reinforce Nico-voiced affiliate disclosure rule. Provide canonical example in agent prompt. |
| 18 | Apr 27, Step 5 | Step 5 | Low | FAQPage schema must be added at publish (Step 8). Easy to forget. | Add explicit reminder to SOP_01 Step 8. Architect agent prompt enforces. |
| 19 | Apr 27, Step 5 | Step 5 | Low | Live post had internal copy error: "5 best places" but only 3 listed in main + 2 in luxury sub-section. | Architect Step 2 should flag internal numerical inconsistencies. |
| 20 | Apr 27, Step 5 | Step 5 | Low | Live post used em-dashes despite WAP_06 ban. | Reinforce in Copywriting agent prompt: em-dash purge mandatory final step. |
| 21 | Apr 27, Step 5 | Step 5 | Medium | Nico's YouTube scripts are content assets needing folder structure. | Create `brain/youtube-scripts/` folder + INDEX.md + this script as first entry. Add row to WAP_00_INDEX. |
| 22 | Apr 27, Step 6 v2 | Step 6 | Medium | Affiliate disclosure in v2 is full font size and bold. Should be smaller font, light green color, less visually prominent. | Add to WAP_06 affiliate disclosure spec: small font, light green box, low visual weight. Specify CSS. |
| 23 | Apr 27, Step 6 v2 | Step 6 | High | TL;DR / "Quick answer, no fluff" block design fails. Doesn't connect to article opening. Feels disconnected. Reads like robot summary. | Redesign TL;DR as proper HTML callout box with light color, "in a rush?" framing that invites scroll. Add design spec to WAP_06. |
| 24 | Apr 27, Step 6 v2 | Step 6 | High | "And why should you listen to me?" as H2 is structurally wrong. Author intro is not a major content section. | Add to WAP_06: author intro is flowing prose, NEVER an H2. H2s reserved for major content sections only. |
| 25 | Apr 27, Step 6 v2 | Step 6 | High | Author intro doesn't say "I'm Nico Barcellona." Reader doesn't learn the name. | Add to Copywriting agent prompt: author intro MUST include name "Nico Barcellona" within first sentence. |
| 26 | Apr 27, Step 6 v2 | Step 6 | High | Author intro fails its real job: convincing the reader to KEEP READING. Currently just credentials. No sales hook. | Add to WAP_06 author intro spec: must contain (1) name, (2) credibility hook, (3) reason to keep reading (sales hook / promise of value). Three jobs in one paragraph. Update agent prompt. |
| 27 | Apr 27, Step 6 v2 | Step 6 | High | Bold logic broken: bolding entire sentences. Should bold 2-3 word phrases that carry meaning. | Add to WAP_06 emphasis rules: bold = 2-4 word phrases only. Never bold full sentences. Bold for emphasis, not visual weight. Update Copywriting agent prompt. |
| 28 | Apr 27, Step 6 v2 | Step 6 | High | "SEO" / "search engine optimization" appeared in reader-facing body copy. Industry-insider talk breaks fourth wall. | Add to WAP_05 banned-words list: "SEO", "search engine optimization", "AIO", "AI Overview", "ranking", "keywords" (in body copy context). These are meta-talk, not reader content. |
| 29 | Apr 27, Step 6 v2 | Step 6 | Medium | Wall-of-text paragraphs survived again despite being in revision prompt. | Step 3c (Format) MUST break paragraphs as final cleanup. Enforce in agent prompt with explicit max-2-sentence rule. |
| 30 | Apr 27, Step 6 v2 | Step 6 | Medium | Copywriting agent itself was vulgar in commentary, not just in Nico-voice. Distinction needed. | Add to Copywriting agent prompt: agent prose (commentary, structure, deliverable headers) is NEVER vulgar. Only Nico-voice content can curse. |
| 31 | Apr 27, Step 6 v2 | Step 6 | High | Overall design quality is poor. Generic. No visual hierarchy. No design DNA matching the live blog. | Add to WAP_06: visual design specs for every callout, hotel card, table, header, list. Provide canonical CSS templates. Copywriting must use exact templates, not invent variants. |
| 32 | Apr 27, Pass 1 | Step 6 | Medium | Copywriting agent invented "5-job author intro" rule (current WAP_06 v2 specifies 3 jobs: name + credibility + sales hook). Agent added "problem" and "bullet overview" without authorization. | Park decision until post-Favignana. Evaluate after publish whether to ratify as WAP_06 v2.1 or revert to 3-job rule. |
| 33 | Apr 27, Pass 1 | Step 6 | Medium | Copywriting agent invented "TL;DR mentions monetization signals" rule. No current WAP_06 rule for this. | Park decision until post-Favignana. Evaluate after publish. |
| 34 | Apr 27, Pass 1 | Step 6 | Medium | Pass 1 v2.1 word count 4,875 vs target 2,800-3,200. ~52% over target. Pass 2 expected to "trim" but Pass 2 is voice work, not bloat-rescue. | Patch SOP_01: add explicit Pass 1 word-count gate. If Pass 1 exceeds target by >25%, mandatory revision before Scout. |
| 35 | Apr 27, Pass 1 | Step 6 | Low | Copywriting agent gave PM procedural instructions ("tell PM to do X, here's how to manage scope"). Agents deliver work, PM manages workflow. | Reinforce in Copywriter agent prompt v2.1: agents do not direct PM workflow. Flag observations, do not prescribe procedure. |
| 36 | Apr 27, Pass 1 | Step 6 | Low | 3 new Nico stories captured during Pass 1 review (dinghy gas scam, bike-closed-for-lunch, Nordic friend lobster). Used in draft. Need formal SOP_03 intake to Story Bank post-publish. | Schedule SOP_03 batch run post-Favignana publish. Candidates S008, S009, S010. |
| 37 | Apr 27, Pass 1 | Step 6 | Low | WAP_10 prices stale (bike rental, scooter rental, hotel peak season pricing). Nico provided 2026 numbers Apr 27 but WAP_10 not updated. | Schedule WAP_10 price update batch post-Favignana publish. Include: Favignana bike €10/day, scooter €50-80/day, peak hotels €150-180/night. |
| 38 | Apr 28 | Step 6 | Low | Process flag: structural divergences from 04_Structural_Audit during Pass 1 (10→11 H2s, sections moved). Nico approved via direct feedback Apr 27 evening. Process valid this run, but flag: 04_Structural_Audit needs to be the controlling doc; mid-pass changes should update it OR be logged as authorized deviations. | Patch SOP_01 Step 5: Structural Audit doc updates require an explicit "amended Apr DD" entry when changes happen mid-pass. Don't ship divergence silently. |

---

## Severity Summary

- **High severity (12 findings):** 1, 8, 9, 10, 11, 23, 24, 25, 26, 27, 28, 31
- **Medium severity (11 findings):** 2, 3, 4, 5, 12, 13, 14, 15, 21, 22, 29, 30
- **Low severity (8 findings):** 6, 7, 16, 17, 18, 19, 20

---

## Decision: Test STOPPED Apr 27, 15:12

After v2 review showed unacceptable output quality across multiple dimensions (broken H2 hierarchy, missing author name, bad bold logic, walls of text, poor design, banned-word usage), Nico decided: stop the test. Redesign SOP_01 from the ground up using all 31 findings as input.

Next phase: SOP_01 v2.0 redesign session starting Apr 27, 15:12.

---

## Patches Pending (Generated In SOP_01 v2.0 Redesign)

This section will be populated as the redesign produces concrete patches.

### Park-Until-Post-Publish Decisions (April 28, 2026)

The following items came up during Pass 1 v2.1 review. Decision: park, do not action mid-run. Address as batch post-Favignana publish.

- Findings #32 + #33: Two invented WAP_06 rules (5-job intro, TL;DR-mentions-monetization). Decide whether to ratify as v2.1 or revert.
- Finding #36: SOP_03 batch run for S008, S009, S010 stories.
- Finding #37: WAP_10 price update batch.
- Finding #38: SOP_01 Step 5 amendment-protocol patch.
- 6 Brain doc escalations from Copywriter: parking ALL 6 per PM decision Apr 28. Re-evaluate post-publish.
