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
| 29 | Apr 28, Pass 2 | Step 8 | High | Pass 2 voice work failed twice (v1 read like a memo, v2 was italics on top of v1 prose) before landing on v3. Total session burn: ~5+ hours over 3 rounds. Diagnosis from Copywriter agent: WAP_05 has rules but no annotated examples to teach the feel. Rules alone don't compose into voice. | Create WAP_05b "Voice in Action" — annotated Palermo Tourist Information article showing how voice moves combine into rhythm. THIS WEEK action. Highest-leverage post-publish fix. |
| 30 | Apr 28, Pass 2 | Step 8 | Medium | Copywriter agent invented "11-move Maniscalco voice formula" structural lock. Useful substance but not agent's place to lock new SOP rules unprompted. | Park until post-publish. Evaluate whether to ratify the 11 moves into WAP_05 v2.1 after Favignana ships. |
| 31 | Apr 28, Pass 2 | Step 8 | Medium | Copywriter proposed content-type-specific word-count bands (quick-answer / destination-guide / pillar) replacing single 3,000-3,500 target in SOP_01 Step 8. Substance valid: voice install adds words to destination guides, doesn't tighten them. Pass 2 v3 landed at 3,755 (+8.7% over v1) with proper voice density. | Park until post-publish. Evaluate SOP_01 Step 8 patch with new bands. |
| 32 | Apr 28, Pass 2 | Step 8 | Low | Copywriter proposed pinning gold-standard Pass 2 sample inside SOP_01 Step 8 as reference paragraph. | Park until post-publish. Evaluate after WAP_05b done. |
| 33 | Apr 28, Pass 2 | Step 8 | Medium | Copywriter proposed "Credibility rule" — credibility lives in author intro, not re-introduced in every H2. Sharp observation valid. | Park until post-publish. Evaluate WAP_06 or SOP_01 Step 8 patch. |
| 34 | Apr 28, Pass 2 | Step 8 | Medium | Copywriter proposed "Tourist-secret reframing" cliche-killer pattern: when killing "hidden gem" / "off the beaten path" cliches, reframe as insider-vs-outsider, not as overcrowded. Hidden-gem-fix in Favignana article followed this pattern. | Park until post-publish. Evaluate WAP_05 cliche-killer patch. |
| 35 | Apr 28, Pass 2 | Step 8 | Low | Copywriter re-proposed WAP_14_TARGET_AUDIENCE.md (already flagged Apr 27 as finding-set escalation). Valid gap: WAP doesn't have permanent audience definition doc, produced "vs Ustica" cold-reader mistake in Pass 1 v1. | Park until post-publish. Evaluate creating WAP_14 separately. |
| 36 | Apr 28, Pass 2 | Step 8 | Medium | 5 new Story Bank candidates surfaced this run: S008 (dinghy gas scam), S009 (bike-closed-for-lunch), S010 (Nordic friend lobster), S011 (grandmother swimming Cala Azzurra 1962), S012 (alternate phrasing "half in mother's belly"). S011 and S012 are interchangeable for credibility job. | Schedule SOP_03 batch run post-Favignana publish. PM picks S011 vs S012. |
| 37 | Apr 28, Pass 2 | Step 8 | Low | Process repeat: Copywriter agent gave PM procedural instructions ("paste this into Claude Code", "tell PM to do X") — same pattern as finding #25. Agent overstep on workflow direction. | Reinforce in Copywriter agent prompt v2.2: agents file work + observations only, do NOT prescribe PM workflow. Patch agent prompt post-Favignana. |
| 38 | Apr 28, Pass 3 | Step 9 | High | Pass 3 took 5 versions and ~155 min vs 45-60 min budget. Root cause: WAP_06 v2 spec was incomplete (hotel card HTML, callout HTML, TL;DR layout, FAQ format) + 00_Live_HTML.md snapshot was stale (image URLs wrong) + no formal canonical-reference-article rule + Architect cannot HTTP-test URLs. Spec gaps not Architect execution. | P0 patches D1-D6, D10, D12-D14 applied Apr 28. |
| 39 | Apr 28, Pass 3 | Step 9 | High | Pass 2 v3 self-claimed paragraph-length compliance and was wrong: 19 wall-of-text violations carried into Pass 3. Pass 2 self-check was human estimate, not mechanical scan. | D12 patch applied: Pass 2 self-check requires mechanical scans with exact counts, not estimates. |
| 40 | Apr 28, Pass 3 | Step 9 | Medium | Pass 3 scope was ambiguous on whether Architect could mechanically split wall-of-text paragraphs at sentence boundaries. v1 Architect assumed not allowed, shipped wall-of-text. | D13 patch applied: Pass 3 explicitly CAN and MUST mechanically split paragraphs at sentence boundaries when Pass 2 ships violations. |
| 41 | Apr 28, Pass 3 | Step 9 | High | Architect inferred image URLs from naming conventions (e.g., `b-amp-b-il-tufo.jpg` actual was `il-tufo.jpg`). Produced 2 rejection cycles. | D14 patch applied: Architect ships `[NICO: paste URL]` placeholders unless URL verified. |
| 42 | Apr 28, Pass 4 | (NEW Step 10) | Medium | Pass 4 (Nico manual edits) is real and material but not codified in SOP_01. Currently informal between Pass 3 and Publish. | P1: codify Pass 4 as explicit step in SOP_01. Park to this-week patches batch. |
| 43 | Apr 28, Pass 3 | Snapshot tooling | Medium | 00_Live_HTML.md snapshot has stale image URLs. Architect trusted as authoritative; produced broken images. | P1: define snapshot generation process, refresh cadence, and trust rules. Currently NO trust for image URLs. Park to this-week patches batch. |
| 44 | Apr 28, Pass 3 | Architect process | Medium | Architect self-criticism (handoff doc section G): (1) should not infer image URLs, (2) should mechanically split wall-of-text in v1 not flag-and-ship, (3) should diff against canonical reference article before assuming spec is right, (4) should mechanically scan Pass 2 input before Pass 3, (5) architect notes section too long (250 lines vs <80 target). | P0 items addressed by D14, D13, D17 (codify Tourist Info as canonical reference). Items 4 + 5 are agent-prompt patches: park to Architect agent prompt v2.1 batch. |
| 48 | Apr 29, Step 10/10.5 | Step 10 | High | Favignana post sat unpublished for 14 hours (Apr 28 22:51 → Apr 29 11:50) because no verify-publish step existed in SOP_01. PM operated on Nico-said-shipped without verification. Brain doc patches were applied as if post was live. Discovered Apr 29 11:24 when Step 11 prompt run by Claude Code revealed live URL was still pre-rewrite version. | Patched into SOP_01 Apr 29: Step 10 codified WordPress publish procedure, Step 10.5 added as mandatory verify-via-fetch within 60 seconds. |
| 49 | Apr 29, Step 11 | Step 11 | Medium | Architect agent in normal Claude project has no web/HTTP/browser access. Cannot run Step 11 live URL checks. Claude Code (CLI access) and PM (web_fetch) CAN. Step 11 was misassigned to Architect. | Patched into SOP_01 Apr 29: Step 11 reassigned to Claude Code primary + Nico for browser-only checks (mobile preview, GSC). Architect agent role spec updated implicitly. |
| 50 | Apr 29, Step 10 | Step 10 | Medium | "Procedure for rewriting" was implicit, not codified. WordPress publish action sequence (Code Editor mode, replace body, Yoast fields, author setting, featured image, date update to today, hit Update) had never been written down. Caused incomplete publish (signature was wrong English version, would have caused content drift on next post). | Patched into SOP_01 Apr 29: Step 10 codified. Hard rule: publish date always updated to today on republish. |
| 51 | Apr 29, Commit 2 morning | Process | Low | Claude Code commits can sit staged-but-not-fully-pushed if a run hits an issue mid-execution. WAP_06 patches + brand rename morning commit did not push initially; was pushed only when Step 11 commit ran. Pattern: assume nothing is committed until verified. | Add post-commit push verification to PM Claude Code prompt protocol: end every prompt with explicit "verify push completed via git log origin/main" or "fetch the URL the file should now be at". |
| 52 | Apr 29, post-publish UI | Site | Low | Author bio photo missing site-wide on rendered posts. Likely Gravatar email mismatch (WordPress user email is `nicolabarcelllona@gmail.com` with triple-L typo, doesn't match Gravatar account email). Affects every post, not Favignana-specific. | Park to backlog. Fix path: install "Simple Local Avatars" plugin OR fix WP user email + create/link Gravatar with the correct email. ~15-30 min separate task. |
| 53 | Apr 29, audit | Process | Medium | PM Claude Code prompts that embed full file content >5,000 words inline can truncate across chat clients. Apr 29 SOP_01 v2.1 rewrite prompt truncated at "## Project Folder File Naming Convention" header, requiring continuation message. Wasted ~5 min recovering. | PM Claude Code prompt protocol updated Apr 29: when writing files >5,000 words, split into multiple Write calls in same prompt OR pre-warn truncation risk OR use semantic instructions instead of literal content. Logged as standard. |
| 54 | Apr 29, audit | Process | High | Brain docs accumulated entropy faster than they were pruned. Multiple times Apr 27-29: rules added by appending to bottom of doc instead of rewriting body to reflect current state. SOP_01 had v1.1 8-step pipeline in body coexisting with v2.0+ patches at bottom. WAP_06 had three competing paragraph-length rules. Author intro numbered differently in WAP_06 vs WAP_05b. Brand rename incomplete. Architect's responsibility list outdated. | Patched Apr 29: when a doc has a major version change, REWRITE the body, don't just append. Use "Changelog" section to log what changed but body must reflect current single source of truth. Added to PM protocol below. |
| 55 | Apr 29, audit | Process | Low | Audit revealed a class of "silent drift" failures: the system told us things were done when they weren't (post not actually published, brand rename incomplete, agent prompts stale, two pipelines coexisting). Pattern: assume nothing is in canonical state until verified by independent fetch/grep. Findings #48 (post not published despite "shipped" claim), #51 (commit not pushed despite commit message), #54 (docs not consistent despite "patches applied"). | Patched Apr 29: PM verification protocol — after every commit, web_fetch or grep the canonical state. Don't trust the operation report. Trust the artifact. |
| 56 | May 1, where-to-stay-palermo Step 2-3 transition | PM | High | PM made confident factual claim ("you're #1 ranking on 'where to stay in palermo' US Google") based on single Ubersuggest serp_analysis call. Data was stale (updated_at field showed 14 months old) and contradicted GSC reality (position 9.8 average over 3 months per Nico's GSC screenshot). PM built a strategic reframe on the false claim ("don't break #1 rank") that would have shifted Step 4 Structural Audit in the wrong direction. Nico caught it via independent GSC check. Without Nico catching it, downstream Steps 4-7 would have been built on bad data. Same class as Findings #48 (post not actually published), #55 (silent drift). | Park to post-publish patches batch. Patch SOP_01 v2.1 Step 3 to add: "PM does NOT pull external SEO data (Ubersuggest, Ahrefs, Semrush) before Architect's Step 3 GSC report. GSC is canonical. Other tools are confirmation only, not source. PM SEO claims without GSC backing get a [UNVERIFIED] tag." Patch PM_SYSTEM_PROMPT Claude Code Prompt Protocol Rule 4 to extend to ALL canonical claims (not just commits): rank, traffic, brand state, publish state. |
| 57 | May 1, where-to-stay-palermo Step 2-3 transition | Process / SOP gap | Medium | SOP_01 v2.1 defines what each specialist agent does at each step (Architect Step 3 = GSC + prep packet). It does NOT define what PM can or cannot do in parallel between steps. PM had access to Ubersuggest tool and used it without the SOP saying that's a PM responsibility. Result: PM did Architect's job badly, with worse data, before Architect ran. The SOP needs an explicit "PM does not pull specialist-agent data sources independently" rule, OR a "PM tool restrictions" section. | Park to post-publish patches batch. Add "PM Boundaries" section to SOP_01 v2.1: PM orchestrates, gates, writes handoffs, runs verify-publish (Step 11 web_fetch). PM does NOT pull GSC, Ubersuggest, Ahrefs, Semrush, schema validators, or any specialist tool that has a defined home in the pipeline. If PM finds itself wanting to "just check something quickly" with a specialist tool, the answer is wait for the specialist agent step. |
| 58 | May 1, where-to-stay-palermo Step 3 | Process / SOP gap | Medium | Claude Code expanded scope from "move 7 GSC files to project folder + commit" to fully executing SOP_01 Step 3 (Prep), generating 02_Prep.md autonomously without explicit instruction. Architect opened next session to find file already populated with 9 of 10 sections covered. Architect paused, asked PM, did not overwrite. Pattern: agents with broad tool access doing more than asked. Same class as Findings #56 (PM doing Architect's job badly with worse tool) and #57 (PM does not have specialist-tool boundary policy). Now confirmed: ALL agent prompts need explicit "do only what is asked, do not anticipate next steps" rule. | Park to post-publish patches batch. SOP_01 v2.1 needs explicit per-step "scope cap" language. Each handoff prompt must end with "do not execute any step beyond what this prompt requests." Plus Claude Code-specific guidance: "Claude Code, you have broad capability via your CLI access. Tasks that touch the WAP repo go through PM-authored prompts. Do not pre-execute future steps." |
| 59 | May 1, where-to-stay-palermo Step 3 | PM | Medium | PM Intake doc included an internal-link reference (`/where-to-stay-cefalu/`) that returns 404. PM assumed root-level slug from convention (the post is /where-to-stay-palermo/, so PM assumed Cefalù equivalent at /where-to-stay-cefalu/), did not curl -I or web_fetch to verify before locking Intake. Caught by Claude Code's Step 3 internal-link 200-status audit. Same class as Finding #56 (PM confident factual claim without independent verification). | Park to post-publish patches batch. Add to PM Intake protocol (and SOP_01 v2.1 Step 1): "All internal-link URLs referenced in the Intake doc must be HTTP-verified before locking. Either via web_fetch (PM tool) or via Architect's pre-Step-1 link audit. Assumed URLs are NOT acceptable." Same lesson as #56-58: trust artifacts not assumptions. |
| 60 | May 1, where-to-stay-palermo Step 4 v1 | Process / SOP gap | High | Architect produced a structural audit (v1) that was internally consistent, comprehensive, well-formatted, and FUNDAMENTALLY BACKWARDS. H2 1 was "Why most where-to-stay advice is wrong" — a defensive opening that announces the article's superiority before delivering value. The whole structure optimized for AIO citation (Quick Picks first, decision matrix early) and forgot that humans need context before decisions. Macro → micro reader flow was missing entirely: pricing came before areas, accommodation type was buried late, horror stories were weaponized as a section instead of sprinkled in voice. PM gated Step 4 and called it "the strongest deliverable of the whole project so far" — wrong. Nico caught the structural failure on read. Same class as Findings #56 (PM trusts proxy data), #58 (agents do work outside scope without verification): PM optimized for surface quality (formatting, comprehensiveness, decision count) instead of canonical correctness (does this match how a real reader thinks?). | Park to post-publish patches batch. SOP_01 v2.1 Step 4 (Structural Audit) needs explicit "reader question flow validation" gate. Step 4 deliverable must include a "macro → micro reader flow" section that maps: what would a real reader ask FIRST? What would they ask SECOND? Does the locked outline answer questions in the order a human asks them? If outline doesn't match the natural question flow, outline is wrong. Plus PM gating rule: PM cannot approve a Step 4 deliverable without independently walking through the "real reader" test on the outline. PM approving on surface quality without reader-flow check = same class of failure as approving Ubersuggest "you're #1" on tool output without GSC check. |
| 70 | May 1, where-to-stay-palermo Step 6 Scout | Copywriter + Pass 1 brief gap | High | Scout caught 4 of 6 hotel affiliate URLs in Pass 1.5 v2 don't match WAP_12 canonical: Politeama Apartments (draft: politeama-apartments vs WAP_12: painpa-i-mercati-apartments), Hotel Wagner (draft: hotelwagner vs WAP_12: grand-wagner), L'Officina di Apollo (draft: officina-di-apollo vs WAP_12: l-39-officina-di-apollo apostrophe URL-encoding), Unico Boutique Hotel d'Arte (draft: unico-boutique vs WAP_12: unico-boutique-d-39-arte same encoding). Pattern: Copywriter inferred Booking URLs from hotel names instead of pulling verbatim from WAP_12 source-of-truth. Real revenue bug — wrong URLs may 404 or route to wrong hotels. Same root cause class as #56-#60: agents acting on inference instead of verifying canonical source. | Park to post-publish patches batch. Pass 1 Copywriter brief must require: every hotel affiliate URL pulled VERBATIM from WAP_12. No URL inference from hotel names. Add to Pass 1 mandatory self-check (D12 patch extension): "Affiliate URL audit: every URL in draft cross-checked against WAP_12 verbatim. List any deviations." Same lesson as #56 (PM trusted Ubersuggest), #58 (Claude Code inferred scope), #59 (PM assumed URL), #60 (PM approved backwards structure). H2 1 was "Why most where-to-stay advice is wrong" — a defensive opening that announces the article's superiority before delivering value. The whole structure optimized for AIO citation (Quick Picks first, decision matrix early) and forgot that humans need context before decisions. Macro → micro reader flow was missing entirely: pricing came before areas, accommodation type was buried late, horror stories were weaponized as a section instead of sprinkled in voice. PM gated Step 4 and called it "the strongest deliverable of the whole project so far" — wrong. Nico caught the structural failure on read. Same class as Findings #56 (PM trusts proxy data), #58 (agents do work outside scope without verification): PM optimized for surface quality (formatting, comprehensiveness, decision count) instead of canonical correctness (does this match how a real reader thinks?). | Park to post-publish patches batch. SOP_01 v2.1 Step 4 (Structural Audit) needs explicit "reader question flow validation" gate. Step 4 deliverable must include a "macro → micro reader flow" section that maps: what would a real reader ask FIRST? What would they ask SECOND? Does the locked outline answer questions in the order a human asks them? If outline doesn't match the natural question flow, outline is wrong. Plus PM gating rule: PM cannot approve a Step 4 deliverable without independently walking through the "real reader" test on the outline. PM approving on surface quality without reader-flow check = same class of failure as approving Ubersuggest "you're #1" on tool output without GSC check. |

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

### Apr 28 Post-Pass-2 Park Decisions

PM consolidated decision Apr 28 16:45: park ALL escalations from Pass 2 session except Escalation 1 (WAP_05b creation). Reasoning: scope discipline. Favignana ship is the goal. All structural patches evaluated post-publish.

THIS WEEK action (one item):
- Create WAP_05b "Voice in Action" with annotated Palermo Tourist Information article. Highest-leverage fix to prevent next post burning 5+ hours on voice failure.

POST-PUBLISH evaluation batch (Findings #22-37, 16 items):
- 2 invented WAP_06 rules (5-job intro, TL;DR-mentions-monetization) from Pass 1
- 11-move Maniscalco voice formula from Pass 2
- Content-type-specific word count bands
- Gold-standard sample pinned in SOP_01
- Credibility rule (no H2 self-introductions)
- Tourist-secret reframing cliche-killer
- WAP_14 Target Audience doc creation
- 04_Structural_Audit amendment-protocol patch
- SOP_03 batch run for S008, S009, S010, S011/S012
- WAP_10 price update
- WAP_12 Favignana population
- WAP_06b Things-to-Do subsection promotion
- Copywriter agent prompt v2.2 (workflow boundary patch)

### Apr 28 Post-Pass-3+4 Park Decisions

PM consolidated decision Apr 28 evening: Favignana shipped. P0 patches applied (D1-D6, D10, D12-D14).

P1 batch parked to this-week-patches session:
- D7 (Bold logic explicit rule — "every long paragraph must have at least one bolded skim-keyword")
- D8 (Featured image pattern — plain `<img>`, no [caption] shortcode)
- D15 (Pass 4 step formalization in SOP_01 — codify what Nico already does)
- D16 (Snapshot tooling redesign — generation, refresh, trust rules)

P2 backlog parked:
- D9 (Image attributes — PM decision Apr 28: Nico's minimal canonical wins; spec follows practice.)
- D17 (Tourist Info as canonical reference — PM decision Apr 28: codified in SOP_01 Step 9 scope clarification as part of D13 patch.)

PM judgment calls (Apr 28):
- D9 → Nico's minimal canonical (his preference governs, his rankings prove it)
- D11 → KEEP FAQPage schema (invisible, SEO upside, retroactive Tourist Info fix is separate task) — applied in P0 batch as part of D10
- D17 → Codified in SOP_01 D13 patch (spec lags practice in one-person operation; Step 9 input is cheaper)

POST-PUBLISH evaluation batch now 23 items (Findings #22-44).

### Apr 29 Favignana Closeout — Findings #48-52

PM consolidated decisions Apr 29 ~12:30:

P0 patched Apr 29 (this session):
- #48 (Step 10.5 verify publish) → SOP_01 patched
- #49 (Step 11 reassigned to Claude Code) → SOP_01 patched
- #50 (Step 10 publish procedure codified) → SOP_01 patched

Process patch this session:
- #51 (push verification) → codified in PM closeout prompt protocol

Backlog:
- #52 (author avatar) → site-wide cosmetic fix, separate task

Related signature canonical fix (today): "Un grande abbraccio, *Nico Barcellona*" replaces deprecated English "A hug is always". Patched into WAP_05b + WAP_06.

Tourist Info article retroactive fix (signature + author byline + brand rename "The Sicilian Way" → "We Are Palermo Premium Guide" in body): logged as separate backlog item, not blocking.

### Apr 29 Audit + Cleanup Session — Findings #53-55 + Major Doc Cleanup

PM consolidated decision Apr 29 ~12:30: full audit of brain repo health before next post run. Found 6 contradictions/gaps across SOP_01, WAP_06, WAP_05b, WAP_01, WAP_02, AGENT_INDEX, ARCHITECT_SYSTEM_PROMPT.

Cleanup pass executed Apr 29 12:50-13:30 across 4 commits:

**Commit 1:** SOP_01 v2.1 — full body rewrite. 12 steps across 3 phases. Old v1.1 8-step pipeline removed from body. All Apr 27-29 patches integrated. Findings A1, A6 resolved.

**Commit 2:** WAP_06 v2.2 — killed duplicate paragraph-length rule (Foundation Rules is single source of truth, 180 char text block). Renumbered author intro 1-8 to match WAP_05b. Findings A2, A3 resolved.

**Commit 3:** Brand rename completion (WAP_01, WAP_02 — was missed in Apr 29 morning rename) + AGENT_INDEX step numbering update (Architect Steps 2/3/4/8, Copywriter Steps 5/7, Scout Step 6) + Architect system prompt v2.1 alignment (removed publish-to-WordPress responsibility, removed live-check responsibility, updated step numbering). Findings A4, A5, A6 resolved.

**Commit 4 (this commit):** Findings #53-55 logged + meta-process patches + WAP_00_INDEX timestamp + SOPS_INDEX v2.1 update + final repo health check.

The lesson: **patch by rewriting, not appending.** Major version changes (v1→v2, v2.0→v2.1) require body rewrites. Minor patches can append. The system was growing entropy faster than it was being pruned.

After this commit, repo is in clean state for next post run.

### May 1 where-to-stay-palermo run — Findings #56-60, #70

PM consolidated decision May 1 ~13:00: park BOTH findings until post-publish per park-until-publish rule (same discipline applied to Favignana findings #22-44). Reasoning: scope discipline. Where-to-stay ship is the goal. Mid-run process patches create more entropy.

Post-publish patches batch will need:
- SOP_01 v2.1 Step 3: "PM does not pull specialist-agent SEO/ranking data independently. Architect's Step 3 GSC report is the canonical source. PM uses [UNVERIFIED] tag if making any claim before Architect's Step 3 lands."
- SOP_01 v2.1 new section "PM Boundaries": PM orchestrates, gates, writes handoffs, runs Step 11 web_fetch. Does not run Ubersuggest / Ahrefs / Semrush / GSC / schema validators / curl HEAD checks / any specialist tool with a defined home in the pipeline.
- PM_SYSTEM_PROMPT v1.2: Extend Claude Code Prompt Protocol Rule 4 to ALL canonical claims (rank, traffic, brand state, publish state), not just post-commit verification. Add explicit rule: "When stating a fact about the WAP system or wearepalermo.com to Nico, cite the canonical source (GSC, live URL, brain doc artifact). If unable to cite canonical, say so explicitly with [UNVERIFIED]. Do not substitute proxy data and present as ground truth."

- SOP_01 v2.1 needs explicit per-step "scope cap" language at the end of every handoff prompt template: "Do not execute any step beyond what this prompt requests. Do not anticipate downstream steps."
- Claude Code-specific scope rule: All tasks touching the WAP repo go through PM-authored prompts. Claude Code does not pre-execute future steps even if it has the capability and context.
- PM Intake protocol (SOP_01 v2.1 Step 1): All internal-link URLs referenced in the Intake doc must be HTTP-verified (web_fetch or curl -I) before Intake is locked. No assumed URLs.

- SOP_01 v2.1 Step 4 must include "Reader Question Flow Validation" — Architect maps "what would a reader ask in what order?" and validates the outline against the natural question flow. Macro → micro check: does the outline answer the most general question first, then progressively narrower questions? If pricing appears before area context, or accommodation-type buried late, or horror stories weaponized as a section instead of sprinkled in voice — reject the outline.
- PM gating discipline for Step 4: PM cannot approve a structural audit on surface quality (comprehensiveness, formatting, decision count). PM must walk through the outline as a real reader would and ask: "is the next H2 answering the next question I'd have?" Surface-quality approval without reader-flow check = Finding #56-class error.
- WAP_12 update: Add Villa Igiea (Rocco Forte) with affiliate URL Nico provided May 1: https://www.booking.com/hotel/it/grandhotelvillaigieapalermo.en.html?aid=918822&no_rooms=1&group_adults=2 — Mondello-area luxury, ~€2,000/night, "where Dua Lipa got married" Nico voice reference.
- WAP_12 update: Add 12 Cefalù hotels from /news/where-to-stay-cefalu/ existing article. Areas: Old Town (5 hotels — Duomo Apartments, El Corazón, Sikelia House, Amare Cefalù, Casa Mimí), Lungomare Beachfront (4 — B&B Le Suites di Costanza, Salemare Rooms & Suites, Blue Bay, Cefalù Sea Palace 5★), Hills Above Cefalù (3 — Al 33 Giri, Cuore Della Valle, Skyview Cefalù). All affiliate URLs in the existing live HTML at /news/where-to-stay-cefalu/.
- Live Cefalù article (/news/where-to-stay-cefalu/) is also rotting per WAP_13 (P2 Tier A). Eventually needs own SOP_01 run. Park.
- Live Cefalù article uses "The Sicilian Way" old brand name in body. Retroactive brand-rename pass needed (same task class as Tourist Info article retroactive fix).

- Pass 1 Copywriter brief: every hotel affiliate URL pulled VERBATIM from WAP_12 source-of-truth. No URL inference from hotel names. Add to Pass 1 mandatory self-check (D12 patch extension): "Affiliate URL audit table — every URL in draft cross-checked against WAP_12 verbatim. List any deviations."

These eight patches are the same lesson, applied at eight layers (per-step Architect data sourcing, per-agent boundaries, per-claim hygiene, per-prompt scope caps, per-tool Claude Code scope, per-Intake URL verification, per-Step-4 reader flow validation, per-Pass-1 affiliate URL verbatim-from-WAP_12 discipline). All trace to a single root cause: agents AND PM optimize for surface quality without verifying canonical correctness OR using available source material systematically. Apply as one commit post-publish.
