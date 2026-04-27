# 07 — Test Run Findings

**Purpose:** Living log of every issue, gap, mistake, missing rule, and improvement opportunity discovered during the SOP_01 Phase 3 test run on /where-to-stay-palermo/. Findings are captured as they emerge during the test. At end of test, distilled lessons get promoted to Brain doc updates and SOP_01 v2.0 patches.

**Started:** April 27, 2026
**Test target:** /where-to-stay-palermo/ (P1 Tier A, -2,012 clicks YoY)
**Status:** In progress (Step 5/6 active)

---

## How To Use This Doc

**During the test run:**
- PM logs every issue discovered as a new row in the Findings Log below
- Severity: High (breaks workflow or output quality), Medium (nice-to-have improvement), Low (minor polish)
- Each finding has a Fix Path describing where the lesson eventually gets codified

**At end of test run:**
- Review entire Findings Log
- Group findings by Fix Path (Brain doc updates, SOP patches, agent prompt updates)
- Generate batch of Claude Code prompts that apply each fix
- Move this doc to "completed test" status, archive findings into permanent Brain doc updates

**For future SOP test runs:**
- Use this doc as a template
- Each test run gets its own findings log
- Pattern: project-local raw findings → distilled rules promoted to Brain after test

---

## Findings Log

| # | When Found | Step | Severity | Finding | Fix Path |
|---|---|---|---|---|---|
| 1 | Apr 26 | Pre-Step-1 | High | SOP_01 v1.1 has no formal Structural Audit step. Some posts need restructuring (new sections added, sections cut, complete redesign) before voice rewriting. v1.1 implicitly assumes existing structure is fine. | Patch SOP_01 to v1.2 with formal Step 2.5 Structural Audit between Prep (Step 2) and Rewrite (Step 3). PM + Architect produce structural decision before Copywriting writes. |
| 2 | Apr 27, Step 2 | Step 2 (Prep) | Medium | Architect prep packet flagged 4 free walking tour internal link candidates. These were rejected by Nico because they conflict with Sicilian Way premium guide monetization (free walking tour articles undermine paid product). | Add "Free vs Paid Content Conflict" rule to WAP_03 (Monetization) or WAP_06 (Content Format): "Posts that funnel toward Sicilian Way premium guide must NOT link to free walking-tour or itinerary articles. Itineraries are paid product." Update Architect agent system prompt with the rule. |
| 3 | Apr 27, Step 2 | Step 2 (Prep) | Medium | WAP_04_CONTENT_INVENTORY.md row 019 lists /where-to-stay-palermo/ as Status RANKING. WAP_13_GSC_AUDIT_LATEST.md lists same URL as P1 ROTTING -77% YoY. Two docs have conflicting status fields. | Decide which doc is canonical for status. Either remove status from WAP_04 (defer to WAP_13) or have WAP_04 reference WAP_13 as source of truth. Same conflict will exist for every P1/P2/P3 row in WAP_04. |
| 4 | Apr 27, Step 2 | Step 2 (Prep) | Medium | Live post has SEO title vs H1 mismatch: SEO title is "The 3 Top Areas and Accommodations for Your Palermo Stay 2025" (numbered, year-stamped). H1 is "Where to Stay in Palermo to Get the Most of Your Trip" (un-numbered). Should be unified. The "2025" year stamp also hurts freshness signals in 2026. | Add to WAP_06: rule that SEO title and H1 should match (or have intentional documented differentiation). Audit existing posts for similar mismatches. |
| 5 | Apr 27, Step 2 | Step 2 (Prep) | Medium | Architect could not verify schema markup via web_fetch (markdown extraction strips JSON-LD) or bash curl (wearepalermo.com not allowlisted). Schema audit blocked. | Add tool capability: either allowlist wearepalermo.com for bash curl, or add a dedicated schema-checking method that pulls raw HTML. Alternatively, build a Step 2 sub-task: "PM runs Google Rich Results Test on URL before Step 3" so schema state is known. |
| 6 | Apr 27, Step 2.5 | Step 2.5 (Structural Audit) | Low | "Centro Storico = unified single area" framing is Nico's local truth (locals don't think of Kalsa/Vucciria/Capo/Albergheria as separate stay options). Tourist guides treat them as separate areas. This is a competitive differentiator and SEO opportunity. | Add to WAP_05 (Voice and Persona) as a permanent local-truth rule. Future posts about Palermo accommodation should reflect this framing. |
| 7 | Apr 27, Step 2.5 | Step 2.5 | Low | Vucciria fact lock established: NOT a working morning fish market. It is currently a restaurant/nightlife area, touristy. Capo and Ballarò are the working morning markets. PM had hallucinated the Vucciria-as-fish-market claim earlier in session. | Add Vucciria fact to WAP_10 entry. Add to WAP_05 as a Palermo fact lock that all agents should respect. PM and other agents should never claim Vucciria is a working morning market. |
| 8 | Apr 27, Step 3 | Step 3 (Rewrite) | High | Copywriting produced markdown output, but post needs WordPress-ready HTML for direct paste. Step 3 prompt didn't specify output format clearly. | Update SOP_01 Step 3 prompt template to specify HTML output mandatory for SOP_01 (rewrites of existing posts that go to WordPress). Markdown OK for SOP_02 if reviewed before HTML conversion. |
| 9 | Apr 27, Step 5 | Step 5 (Nico Review) | High | Copywriting v1 used generic Pro Tip boxes (custom HTML) instead of WAP_06 Local's Take (Variant 1, orange), Local's Pick (Variant 2, green), or Local's Warning (Variant 3, red) templates. Each WAP_06 template requires a specific Nico photo URL and specific color. v1 had only 2 generic boxes total in 3,470 words. WAP_06 mandates "one box per H2 section, one per ~300 words." | Patch Copywriting agent system prompt: enforce WAP_06 text box compliance. Variants 1/2/3 only. No generic Pro Tip blocks. Mix variants across post. Frequency rule baked in. |
| 10 | Apr 27, Step 5 | Step 5 | High | Copywriting v1 jumped from affiliate disclosure straight to TL;DR with no Nico intro. Cold readers (US tourist who never heard of WAP) don't know who's talking before being asked to trust recommendations. The "I'm Sicilian, born here" credibility hook was at section 3, buried. | Update WAP_06 post structure rule: Nico self-introduction MUST precede the TL;DR / direct-answer block. Order: Italic lead → Featured image → Nico intro (~80 words) → Affiliate disclosure → TL;DR. Update SOP_01 Step 3 prompt template with explicit ordering. |
| 11 | Apr 27, Step 5 | Step 5 | High | Single-pass writing (Copywriting handles information + structure + voice + format + HTML in one go) produces flat tone of voice. Voice attention gets split across too many concerns. v1 reads as competent reformat of Nico's YouTube script, NOT as a fresh Sebastian-Maniscalco rhythm pass. | Patch SOP_01 to v2.0 with 3-pass writing model. Step 3a (Information & Structure, markdown OK), Step 3b (Trimming & Voice, markdown), Step 3c (Format & HTML). Each pass = separate Copywriting handoff. Each pass = different attention focus. PM gates each pass. |
| 12 | Apr 27, Step 5 | Step 5 | Medium | v1 missing several reader-need answers per area: walking size of area, cleanliness reality, airport connection, supermarket availability, restaurant/food coverage in Politeama and Mondello. Cold readers want to know "is this my area, can I live here, what's nearby." | Add to WAP_06 (Content Format) as "Cold Reader Reality Check" — list of standard reader-need items every "where to stay" or area-comparison post must cover. Update SOP_01 Step 2.5 Structural Audit to include this checklist. |
| 13 | Apr 27, Step 5 | Step 5 | Medium | v1 had several wall-of-text paragraphs exceeding WAP_06 max (2 sentences or 45 words per paragraph for mobile). Pass 3 should always include a paragraph-length scrub. | Reinforce in WAP_06 that paragraph-length rule is mandatory, not aspirational. Add explicit instruction to Step 3c (Format) to break long paragraphs as final cleanup. |
| 14 | Apr 27, Step 4 | Step 4 (Scout) | Medium | Scout caught 4 disputed facts: ZTL fine €164 (not €160), Unico Boutique 4-star (not 5), B&B Mondello Design star rating conflict (drop stars), Villa Gabriella 300 sqm (unverified). All actionable in Step 6. | No SOP patch needed — Scout did its job correctly. But add to WAP_05 / Copywriting prompt: when stating star ratings, verify against hotel's own official site, not aggregator sites. |
| 15 | Apr 27, Step 5 | Step 5 | Medium | Star rating convention inconsistent in v1: official Giata/government tourism stars (Hotel Wagner 5★) mixed with editorial stars on properties not officially classified (apartments, vacation rentals). Misleading to readers — implies authority that doesn't exist. | Add to WAP_06: rule on star rating conventions. Use ★ stars only on officially classified hotels. For apartments, B&Bs without official rating, vacation rentals: drop stars and use descriptive tagline only ("My top pick for Mondello" without stars). |
| 16 | Apr 27, Step 5 | Step 5 | Low | "Continue Your Palermo Planning" block (gray box with 3 internal links to related post + premium guide + YouTube) is required by WAP_06 at end of every post. v1 had social CTAs (Instagram + YouTube + Facebook group) instead. | Reinforce in Copywriting agent prompt and SOP_01 Step 3c (Format): Continue Your Palermo Planning block is mandatory. Social CTAs are separate and optional. |
| 17 | Apr 27, Step 5 | Step 5 | Low | v1 affiliate disclosure was generic. WAP_06 requires Nico-voiced disclosure (e.g., "Heads up: some links are affiliate links. I get a small cut so I can keep the circus running, pay the people who help me, and avoid having to go beg my cousin for a real job."). | Reinforce Nico-voiced affiliate disclosure rule in Copywriting agent prompt. Provide canonical example. |
| 18 | Apr 27, Step 5 | Step 5 | Low | FAQPage schema must be added at publish (Step 8). Easy to forget — not in v1. | Add explicit reminder to SOP_01 Step 8 (Architect Publish): FAQPage schema generated from FAQ section, added as Custom HTML block in WordPress directly below visible FAQ. Architect agent prompt should enforce. |
| 19 | Apr 27, Step 5 | Step 5 | Low | Existing live post had internal copy error: "I've handpicked 5 of the best places to stay" but only 3 hotels listed in main Politeama section (other 2 in separate "Luxury Options" sub-section). Math error inherited if v1 doesn't fix. | Not a SOP issue — fix in Step 6 of this run. But adds to: when Architect inventories the live post in Step 2, flag any internal numerical inconsistencies for Step 3 to correct. |
| 20 | Apr 27, Step 5 | Step 5 | Low | Existing live post used em-dashes despite WAP_06 ban. Voice signatures ("park your butt on silk sheets") survived from old voice but em-dashes did too. Copywriting must purge in Pass 3 (Format). | Reinforce in Copywriting agent prompt: em-dash purge is mandatory final step. No exceptions. |
| 21 | Apr 27, Step 5 | Step 5 | Medium | Nico's YouTube scripts are valuable content assets that get repurposed across formats (video → blog → newsletter). Currently no folder structure for them. | Create `brain/youtube-scripts/` folder. Add `INDEX.md` listing all scripts (topic, date, URL, primary-source-for-which-blogs). Save where-to-stay-palermo YouTube script as first entry. Add row to WAP_00_INDEX. |

---

## Patches Pending (Generated At End Of Test)

This section will be populated at end of test run with the actual Claude Code prompts that apply each fix.

**Brain doc updates needed:**
- WAP_03 (Monetization): Free vs Paid Content Conflict rule (Finding #2)
- WAP_04 ↔ WAP_13 status reconciliation (Finding #3)
- WAP_05 (Voice and Persona): Centro Storico unified-area local truth (Finding #6), Vucciria fact lock (Finding #7)
- WAP_06 (Content Format): Multiple updates — SEO title/H1 sync rule (Finding #4), post structure ordering (Finding #10), Cold Reader Reality Check checklist (Finding #12), star rating conventions (Finding #15)
- WAP_10 (Places/Experiences): Vucciria entry fact correction (Finding #7)
- WAP_00_INDEX: New `brain/youtube-scripts/` folder row (Finding #21)
- New folder + index: `brain/youtube-scripts/` (Finding #21)

**SOP updates needed:**
- SOP_01 v2.0: Add formal Step 2.5 Structural Audit (Finding #1), split Step 3 into 3a/3b/3c (Finding #11), add HTML-output rule to Step 3c (Finding #8), add Step 8 FAQPage schema reminder (Finding #18)

**Agent prompt updates needed:**
- Copywriting agent: WAP_06 text box enforcement (Finding #9), Nico intro before TL;DR (Finding #10), star rating sourcing (Finding #14), em-dash purge mandatory (Finding #20), Continue Planning block mandatory (Finding #16), Nico-voiced affiliate disclosure (Finding #17)
- Architect agent: Free vs Paid linking rule (Finding #2), copy-error flagging in prep (Finding #19), FAQPage schema enforcement (Finding #18)
- Scout agent: No changes needed — performed correctly (Finding #14)

**Tool/capability updates needed:**
- Schema audit method that bypasses web_fetch markdown stripping (Finding #5)

---

## Severity Summary

- **High severity (8 findings):** 1, 8, 9, 10, 11
- **Medium severity (8 findings):** 2, 3, 4, 5, 12, 13, 14, 15, 21
- **Low severity (8 findings):** 6, 7, 16, 17, 18, 19, 20

---

## Next Steps

1. Continue test run from current point (Step 6 Revision pending PM decision on 3-pass restructure)
2. Append new findings to log as they emerge
3. At end of test, generate batch of Claude Code prompts to apply patches
4. Archive this findings log alongside test completion artifacts
