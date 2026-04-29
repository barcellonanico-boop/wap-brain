# SOP_01_Update_Existing_Post.md — Update Existing Post

Last updated: April 29, 2026 (v2.1 — full body rewrite. Integrates all Apr 27-29 patches into a single 12-step pipeline. Replaces old v1.1 single-pass workflow.)

---

## What This SOP Does

Rewrite an existing wearepalermo.com blog post that's losing traffic per WAP_13. 12 steps across 3 phases. 3-pass writing model + Nico final + post-publish verification.

This SOP is for **rewriting**, not creating. For new posts, see SOP_02.

---

## When To Use

- Post is rotting per WAP_13 (lost clicks YoY)
- Post has structural issues (broken H2 hierarchy, missing voice, outdated facts)
- Post needs full freshness pass (older than 18 months + still ranking)
- NOT for minor edits (typo fixes, single-line changes)

---

## Inputs Required

- Target URL (single post)
- WAP_13 GSC audit data: clicks, impressions, position, top queries
- Target status (P1 / P2 / P3 from WAP_13)
- Revenue tier (A / B / C from WAP_13)
- Known quality issues (audit notes + Nico's observations)

---

## Outputs

Every SOP_01 run produces:

1. Republished post live on wearepalermo.com (verified via fetch within 60 seconds of publish)
2. Project folder `projects/POST_[slug]/` with all 10 deliverable files
3. Revision log entry in `projects/PROJECT_WAP_Content_Machine/04_Change_Log.md`
4. Baseline metrics snapshot for 6-week comparison
5. Any new stories captured → SOP_03
6. Any new experiences/places captured → queue for WAP_10 update
7. Any affiliate link issues → queue for WAP_12 update
8. Findings logged to `projects/PROJECT_WAP_Content_Machine/07_Test_Run_Findings.md`

---

## Agents & Responsibilities (v2.1 — REVISED Apr 29)

| Agent | Role in SOP_01 v2.1 |
|---|---|
| **WAP PM** | Orchestrates workflow. Writes handoff prompts. Tracks time. Updates docs after every step. Schedules 6-week monitoring. Runs Step 11 (Verify Publish) via web_fetch. |
| **WAP Architect** | Steps 2, 3, 4, 8. Live HTML snapshot. GSC data + prep packet. Structural audit. Pass 3 HTML conversion + schema. **Architect does NOT publish to WordPress.** Architect does NOT run post-publish live checks (no browser/HTTP access in normal Claude project sessions). |
| **WAP Copywriter** | Steps 5, 7. Pass 1 Information Draft (markdown, structure first, voice rough). Pass 2 Voice + Trim + Corrections (markdown, voice locked, mechanical self-check mandatory). |
| **WAP Scout** | Step 6. Fact verification. Returns VERIFIED / DISPUTED / UNVERIFIABLE per claim with sources. |
| **Nico** | Step 9 (Pass 4 manual edits). Step 10 (publish via WordPress UI). 2 browser-only checks in Step 12 (mobile preview, GSC URL Inspection). Reviews and approves at every PM gate. |
| **Claude Code** | Step 11 (Verify Publish via web_fetch). Step 12 (6 of 8 post-publish mechanical checks via curl). Final commit verification. |

---

## The 12-Step Workflow

### Phase A — SETUP

#### Step 1 — Intake (PM, ~5 min)

1. Open WAP_13 (latest GSC audit)
2. Select highest-priority post not yet updated
3. Confirm post still matches its audit classification
4. Create project folder: `projects/POST_[slug]/`
5. Create Execution Backlog entry in PROJECT_WAP_Content_Machine
6. Announce to Nico: "Starting SOP_01 on [URL]. Expected total: ~3-5 hours of focused work."

**Deliverable:** `projects/POST_[slug]/01_Intake.md` containing target URL, audit data, Nico's brain dump on the post.

---

#### Step 2 — Live HTML Snapshot (Architect, ~5 min)

Architect captures the current live state of the post BEFORE any work begins. Critical for diff and rollback.

1. Fetch the live URL via web_fetch
2. Save the rendered HTML to `00_Live_HTML.md`
3. Note: image URLs in this snapshot are NOT trustworthy as canonical (per D14). They reflect what's currently live but may be stale or wrong.

**Deliverable:** `00_Live_HTML.md` with full HTML, header noting "snapshot only, image URLs not canonical."

---

#### Step 3 — Prep (Architect, ~15 min)

1. Pull GSC performance snapshot (6 months: top 10 queries, position, clicks, CTR)
2. Inventory all outbound links from the live HTML (affiliate / internal / external)
3. Cross-check each affiliate link against WAP_12; flag broken or missing
4. Pull 5+ internal link candidates from current WAP post inventory
5. Check current schema markup (FAQPage? Article? Missing?)
6. Note technical issues (broken images, broken links, mobile breaks)
7. Identify SERP competitors via Ubersuggest if relevant
8. Build prep packet

**Deliverable:** `02_Prep.md` containing prep packet: GSC data, affiliate audit, internal link candidates, outbound link inventory, schema state, technical issues, SERP competitor analysis.

---

#### Step 4 — Structural Audit (Architect, ~20 min)

Architect reviews the live post + prep packet and decides: full rewrite or surgical edit.

1. Apply Cold Reader Reality Check (relevant items per post type)
2. Identify structural gaps (missing H2s, broken hierarchy, missing FAQ, no TL;DR)
3. Decide: FULL REWRITE or SURGICAL EDIT
4. If FULL REWRITE: produce new H2 outline with target word counts per section
5. Lock voice notes for downstream agents (signature moves expected, mode A/B, story slots)
6. Lock special instructions for Pass 1, Pass 2, Pass 3 (post-type rules, NO-GO list, etc.)

**Amendment protocol:** If Pass 1 (Step 5) produces structural divergences from the audit (extra H2, sections moved), Pass 1 MUST update `04_Structural_Audit.md` with an explicit "Amended Apr DD" entry. Don't ship divergence silently.

**Deliverable:** `04_Structural_Audit.md` with verdict, outline, voice notes, special instructions.

---

### Phase B — WRITE (3 passes + Nico final)

Each pass is a separate Copywriter or Architect handoff. PM gates between passes. No blending.

#### Step 5 — Pass 1: Information Draft (Copywriter, ~45-60 min)

PM writes handoff to Copywriter with:
- `04_Structural_Audit.md` outline (every H2 in the outline MUST be in the draft)
- Prep packet from Step 3
- Reference: WAP_05 (voice rules), WAP_05b (voice in action), WAP_06 (format), WAP_06b (post-type), WAP_08 (story bank), WAP_10 (places), WAP_12 (affiliate links)
- Target word count per WAP_06 length tiers
- Specific instructions for this post (NO-GO list, post-type rules)

Copywriter produces draft markdown:
- Full post body in markdown
- Every H2 from the outline present
- Voice ROUGH is OK at this stage; Pass 2 polishes
- Brain-dump fragments installed (rough wording fine — Pass 2 polishes cadence)
- ENFORCE 180-character text block limit FROM THE START (Foundation Rule 1, WAP_06)
- ENFORCE 300-400 word section limit FROM THE START (Foundation Rule 2, WAP_06)
- All factual claims wrapped in [VERIFY: X] flags for Scout
- FAQ section drafted (6-8 questions)
- Suggested meta title (50-60 chars), meta description (140-155 chars), URL slug (DO NOT change unless explicit)
- Internal link suggestions (3-5)
- Image placement suggestions

**Self-check before submitting (mechanical):**
- Every text block ≤180 chars? Report count of violations.
- Every section ≤400 words? Report any over.
- All [VERIFY:] flags listed and counted
- Word count total
- Em-dash count (must be 0 — em-dashes are a Fireable Offense per WAP_05)

**Deliverable:** `05_Pass1_Info.md` with Pass 1 markdown draft + self-check table.

---

#### Step 6 — Scout Fact Check (Scout, ~15-20 min)

PM writes handoff to Scout. Input: `05_Pass1_Info.md`.

Scout extracts every [VERIFY:] flag and every other factual claim and returns per-claim:
- VERIFIED + source URL
- DISPUTED + explanation + source URL + recommended correction
- UNVERIFIABLE (personal anecdote, opinion, taste call)

**Scope Scout checks:**
- Statistics, numbers, prices, hours, dates
- Historical facts
- Place names and addresses
- Names of people (historical, chefs, authors)
- Hotel star ratings (against hotel's OWN site, not aggregators — per WAP_06b)
- Claims phrased as fact ("oldest", "only", "biggest")

**Scope Scout does NOT check:**
- Nico's first-hand observations
- Opinions, comedic framing, voice choices
- Invented dialogue, mocking quotes

PM reviews Scout's report. Nico decides on DISPUTED claims (correct, hedge, or remove). Decisions logged for Pass 2.

**Deliverable:** `06_FactCheck.md` with verdict + source per claim + Nico decisions on DISPUTED.

---

#### Step 7 — Pass 2: Voice + Trim + Corrections (Copywriter, ~30-45 min)

PM writes handoff to Copywriter with:
- `05_Pass1_Info.md`
- `06_FactCheck.md` corrections
- Reference: WAP_05 + WAP_05b (voice teaching doc)
- Word-count target per content type (destination guides ±10% of Pass 1, quick-answer tighten 10-15%, pillars +15-20%)

Copywriter rewrites paragraph-by-paragraph:
- Install Maniscalco voice (every text block has at least one signature move)
- Apply alternation rhythm (long → short → long → very short, no 4-in-a-row stretches per WAP_06 Foundation Rule 3)
- Apply Scout corrections exactly
- Keep all approved brain-dump fragments
- Em-dash purge (must end at 0)
- Banned-words purge ("SEO", "AI Overview", "ranking", "keywords", "schema markup", etc.)
- 180-character text block limit ENFORCED
- Bold logic: 2-4 word skim-keywords, never full sentences
- First-person stories (long narrative + habitual practice both valid per WAP_05b Pattern D)

**MANDATORY MECHANICAL SELF-CHECK before submitting (D12 patch — NOT a human estimate):**

Pass 2 deliverable MUST include a self-check table with EXACT COUNTS, not "compliant ✅" estimates. Required scans:

1. **Text block length scan:** every prose block, count chars. Flag any >180. Report exact count of violations.
2. **Em-dash regex:** count of `—` (em-dash unicode). MUST be 0. Report exact count.
3. **Banned-words regex:** count of "SEO", "AI Overview", "ranking", "keywords", "schema markup". MUST be 0 in body. Report exact count per term.
4. **[VERIFY:] tag scan:** count of `[VERIFY:`. MUST be 0. Report count.
5. **Word count grep:** total body word count. Report number.
6. **Bold full-sentence scan:** count of `<strong>` content with 50+ chars or 8+ words. Report count.
7. **Post-specific scans:** any post-specific typos to enforce (e.g., "Piazza Madrice" not "Matrice"). Report count of violations.

Lesson from Apr 28 Favignana: Pass 2 v3 self-claimed paragraph-length compliance via human estimate; mechanical scan in Pass 3 found 19 wall-of-text violations. Human estimates are unreliable on length compliance. Mechanical only.

**Deliverable:** `07_Pass2_Voice.md` with Pass 2 markdown + self-check table with exact counts.

---

#### Step 8 — Pass 3: Format & HTML (Architect, ~45-60 min)

PM writes handoff to Architect with:
- `07_Pass2_Voice.md`
- WAP_06 templates (TL;DR, callout, hotel card, FAQ — all canonical HTML in WAP_06)
- WAP_06b post-type rules
- Tourist Info article URL (canonical reference per D17)

Architect converts markdown to publish-ready HTML.

**Pass 3 IS:**
- Mechanical format application (HTML conversion, callout boxes per D5 wpautop pattern, hotel cards per D3, TL;DR table per D4, Continue Planning block, FAQPage JSON-LD schema per D11)
- Image placement (use `[NICO: paste URL]` placeholder for any unverified URL — D14)
- Mechanical paragraph splits at sentence boundaries if Pass 2 missed any wall-of-text violations (D13). NOT a voice rewrite.
- Final mechanical scans: em-dash purge, banned-words, text-block length, bold logic
- 8-step author intro architecture per WAP_06 (italic lead → featured image → disarming opener → name+credibility+hook → 3 bullets → time-vs-benefit sentence → TL;DR table → affiliate disclosure)
- Section architecture per WAP_06 (image after H2, body prose, closing callout(s) — all sections except Conclusion + FAQ)

**Pass 3 IS NOT:**
- Voice rewrite (locked in Pass 2)
- Structural changes (locked in Step 4 + Step 5)
- Fact corrections (locked in Step 7 with Scout corrections)
- New content additions

**Image URL rules (D14 — placeholder default):**

Architect cannot HTTP-test image URLs. Therefore:
1. If Pass 2 includes verified image URLs → use as-is
2. If `00_Live_HTML.md` snapshot has URLs → DO NOT TRUST without verification
3. If Tourist Info article uses an image (e.g., Nico portrait) → use that URL as canonical
4. Otherwise → ship as `[NICO: paste URL]` placeholder for Nico to fill in Pass 4

DO NOT infer URLs from naming conventions. Examples that broke this Apr 28: inferred `b-amp-b-il-tufo.jpg`, actual was `il-tufo.jpg`. Inferred `i-pretti-favignana.jpg`, actual was `i-pretty.jpg`. Always placeholder when unverified.

**Canonical reference rule (D17 — PM decision Apr 28):** When in doubt about callout / FAQ / intro patterns, the most recent published WAP article (currently: Tourist Info, https://wearepalermo.com/palermo-tourist-information/) is canonical, NOT the spec. The spec lags actual practice in a one-person operation. Architect should diff against Tourist Info before assuming spec is right.

**Architect notes constraint:** Pass 3 deliverable architect notes section MUST be ≤80 lines. Deeper analysis goes into a separate handoff doc, not buried in the Pass 3 file (Finding #44 lesson).

**Deliverable:** `08_Pass3_HTML.md` with publish-ready HTML body + concise architect notes (<80 lines) + list of `[NICO: paste URL]` placeholders for Pass 4.

---

#### Step 9 — Pass 4: Nico Manual Edits (Nico, ~15-30 min)

Nico opens `08_Pass3_HTML.md` and produces the actually-shipped version.

Nico:
1. Fills every `[NICO: paste URL]` placeholder with actual image URL (from media library or new upload)
2. Uploads any new images needed to `/uploads/YYYY/MM/`
3. Applies any final voice or format tweaks Pass 3 didn't catch
4. Confirms canonical patterns from latest published article (vs. older live posts)
5. Saves as `09_Pass4_Nico_Final.md`

**Critical:** the Pass 4 file is THE SHIPPED VERSION. If Nico makes structural changes here that diverge from Pass 3 (e.g., adds new image slots, moves sections, removes elements), those changes get logged as deltas in a reconciliation doc for brain doc patching post-publish.

**Deliverable:** `09_Pass4_Nico_Final.md` with the actually-shipped HTML.

---

### Phase C — PUBLISH & VERIFY

#### Step 10 — Publish (Nico, ~10-15 min)

WordPress publish procedure (codified Apr 29):

1. Open WordPress admin for the target post URL
2. **Switch editor to Code Editor / Text mode** (NOT Visual mode — Visual mangles HTML, callout structure, JSON-LD schema)
3. **Replace post body**: delete current content, paste full HTML from `09_Pass4_Nico_Final.md`
4. **Update post title (H1)** to match Pass 4 spec
5. **Update Yoast SEO panel:**
   - Focus keyphrase (typically primary keyword)
   - SEO title (50-60 chars, includes keyphrase)
   - **Slug — DO NOT CHANGE** (URL preservation for SEO juice. Changing slug = losing all GSC ranking history.)
   - Meta description (140-155 chars, includes keyphrase, in Nico voice)
6. **Set author** to "Nico Barcellona" (NOT "palermo-boss" or any legacy handle). If display name shows wrong: Users → Profile → Display name publicly as → Nico Barcellona → Update.
7. **Set featured image** per Pass 4 spec (alt text per Pass 4)
8. **Update publish date to TODAY** — HARD RULE. Always today's date on republish. Never keep the original publish date.
9. **Set/preserve categories and tags**
10. **Hit Update**

**Deliverable:** post live at the existing URL.

---

#### Step 11 — Verify Publish (Claude Code or PM web_fetch, ~2 min)

MANDATORY. Cannot skip. Within 60 seconds of Step 10 hitting Update.

1. **Fetch the live URL** via web_fetch (PM) or curl (Claude Code)
2. **Verify presence** of Pass 4 markers:
   - New post title in `<title>` and `<h1>`
   - New H2 #1 wording
   - TL;DR table visible (search HTML for `tldr-box` class or first row content)
   - Featured image is the new one (search for new image filename)
   - Author byline is "Nico Barcellona"
   - FAQPage JSON-LD schema present
3. **Verify absence** of old markers:
   - Old title
   - Old H2 wording
   - Old callout photo filename (if it changed)
4. **If any marker is wrong:** publish failed. Possible causes: silent save, draft saved instead of update, cache issue, wrong post edited. DO NOT proceed to Step 12. Return to Step 10 and re-publish. Verify again.

**Lesson from Apr 28-29 Favignana run:** the post sat unpublished for 14 hours (Apr 28 22:51 → Apr 29 11:50) because no verify-publish step existed. SOP operated on assumption "publish happened" without proof. This step is non-negotiable.

**Deliverable:** confirmation in chat / change log entry that publish verified.

---

#### Step 12 — Post-Publish Technical Checks (Claude Code + Nico, ~30-45 min)

Reassigned April 29: Step 12 is executed by **Claude Code** (CLI access via curl/web_fetch) plus **Nico** (browser-only checks). NOT the Architect agent (no browser/HTTP access in normal Claude project sessions).

**Hybrid execution:**

Claude Code runs 6 of 8 checks mechanically:
1. Schema validation (JSON-LD HTML presence: Article + FAQPage)
2. Author attribution (Article schema author = Nico Barcellona, not legacy handle)
3. Broken-link spot-check (curl -I every link, status codes)
4. Image render check (HEAD requests on every image URL)
5. Internal link tab behavior (target="_blank" audit per WAP_06 — internal NO target="_blank", external + affiliate YES)
6. Affiliate ID final verification (parse query strings, confirm aid=918822, gyg.me shortlinks, a_aid=nico0141, affiliate=670d25b9, go.wearepalermo.com/ferry)

Nico runs 2 browser-only checks:
7. Mobile preview (Chrome DevTools or phone — confirm callouts have closed boxes per D5 wpautop, TL;DR responsive, hotel cards stack, FAQ accordion works)
8. GSC URL Inspection (URL is on Google or Request Indexing, no manual actions)

**Deliverable:** `11_PostPublish_Checks.md` with all 8 checks resolved (VERIFIED / FAILED / WARNING / PENDING_NICO → updated to VERIFIED after Nico runs browser checks).

When all 8 are VERIFIED or addressed, mark post CLOSED in change log. Schedule 6-week monitoring trigger.

---

## Project Folder File Naming Convention

| File | Step | Content |
|---|---|---|
| `00_Live_HTML.md` | Step 2 | Pre-rewrite live HTML snapshot |
| `01_Intake.md` | Step 1 | Target URL, audit data, Nico brain dump |
| `02_Prep.md` | Step 3 | Prep packet (GSC, links, schema, competitors) |
| `04_Structural_Audit.md` | Step 4 | Outline, voice notes, special instructions |
| `05_Pass1_Info.md` | Step 5 | Pass 1 markdown draft + self-check |
| `06_FactCheck.md` | Step 6 | Scout report + Nico decisions on DISPUTED |
| `07_Pass2_Voice.md` | Step 7 | Pass 2 markdown draft + mechanical self-check |
| `08_Pass3_HTML.md` | Step 8 | Publish-ready HTML + architect notes |
| `09_Pass4_Nico_Final.md` | Step 9 | Actually-shipped HTML (Nico's version) |
| `11_PostPublish_Checks.md` | Step 12 | 8-check report |
| `12_Monitoring_6week.md` | Post-publish | 6-week click recovery data |
| `PM_VOICE_ESCALATION.md` | Ad hoc | Voice failure analysis (if needed) |
| `10_PM_Handoff_*.md` | Ad hoc | Reconciliation docs for brain doc patching |

Note: `03_*.md` and `10_*.md` slots are unused by convention. File numbers don't perfectly align with step numbers (legacy from earlier SOP versions). Naming kept for backward compatibility with existing project folders.

---

## Step Time Budget (v2.1)

| Step | Phase | Agent | Target | Notes |
|---|---|---|---|---|
| 1 Intake | A | PM | 5 min | |
| 2 Live HTML Snapshot | A | Architect | 5 min | |
| 3 Prep | A | Architect | 15 min | |
| 4 Structural Audit | A | Architect | 20 min | |
| 5 Pass 1 Information | B | Copywriter | 45-60 min | Word count varies by post type |
| 6 Scout Fact Check | B | Scout | 15-20 min | |
| 7 Pass 2 Voice | B | Copywriter | 30-45 min | Mechanical self-check mandatory |
| 8 Pass 3 HTML | B | Architect | 45-60 min | Notes ≤80 lines |
| 9 Pass 4 Nico Edits | B | Nico | 15-30 min | |
| 10 Publish | C | Nico | 10-15 min | WordPress UI work |
| 11 Verify Publish | C | Claude Code / PM | 2 min | Mandatory gate before Step 12 |
| 12 Post-Publish Checks | C | Claude Code + Nico | 30-45 min | 6 mechanical + 2 browser |
| **TOTAL** | | | **~4 hours focused work** | Excluding revision rounds |

If post requires multiple revision rounds (e.g., Pass 2 v1 → v2 → v3), add 30-45 min per extra round. Favignana (Apr 27-28) ran ~12 hours total with multiple revision rounds across Pass 1 + Pass 2 + Pass 3 (5 versions).

---

## Failure Modes & Recovery

| Problem | Fix |
|---|---|
| Copywriter produces AI-sounding output (voice violation) | Send back with specific WAP_05 + WAP_05b rule citation. If 2 rounds fail, prompt needs fixing — log as Finding. |
| Scout returns multiple DISPUTED claims | Pause. Nico decides per claim: correct, hedge, or remove. |
| Affiliate link in WAP_12 is broken | Architect flags. Triggers SOP_05 (Affiliate Link Verification — to be built as Task 2.9). Temporarily use next-best link. |
| Pass 1 produces structural divergences from Step 4 outline | Update `04_Structural_Audit.md` with "Amended Apr DD" entry. Don't ship divergence silently. |
| Pass 2 self-check claims compliant but Pass 3 mechanical scan finds violations | Pass 2 self-check failed. Send back to Copywriter to fix mechanically. Reinforce: scans are mandatory, estimates are unreliable. |
| Pass 3 cannot verify image URL | Use `[NICO: paste URL]` placeholder. Do not infer from naming conventions. |
| Pass 3 architect notes exceed 80 lines | Move deeper analysis to separate handoff doc. Keep Pass 3 file lean. |
| Step 11 verify finds wrong content | Publish failed. Return to Step 10. Common causes: WordPress saved as draft, cache, wrong post edited. |
| Step 12 finds missing affiliate ID | P0 — fix immediately. Lost revenue every day. |
| Image missing or broken at publish | Nico re-uploads to `/uploads/YYYY/MM/` and updates HTML. Re-run Step 11. |
| 6-week monitoring shows NO improvement | Trigger SOP_01b (revision revision) — to be defined. Park for now. |
| 6-week monitoring shows WORSE performance | Rollback via WordPress revision history. Investigate. Log in audit. |

---

## Post-Publish Monitoring

At the 6-week mark after republish:
- Clicks (last 14 days pre-republish vs last 14 days post + 4 weeks)
- Position for primary keyword
- CTR
- AI Overview citation presence (manual Google check)

Log to `projects/POST_[slug]/12_Monitoring_6week.md`:
- Pre-rewrite baseline
- 6-week post-rewrite snapshot
- Delta (absolute + %)
- Verdict: RECOVERED / PARTIAL / FAILED
- Notes

3 RECOVERED in a row = SOP_01 production-ready.
3 FAILED in a row = SOP_01 has a flaw. Revise.

---

## Handoff Prompt Templates

Templates live in a separate file: `sops/SOP_01_Handoff_Prompts.md` (to be created — Task 2.10).

Required templates:
- Template 1: Architect Live HTML Snapshot (Step 2)
- Template 2: Architect Prep Packet (Step 3)
- Template 3: Architect Structural Audit (Step 4)
- Template 4: Copywriter Pass 1 (Step 5)
- Template 5: Scout Fact Check (Step 6)
- Template 6: Copywriter Pass 2 (Step 7)
- Template 7: Architect Pass 3 (Step 8)
- Template 8: Claude Code Step 11 Verify Publish
- Template 9: Claude Code + Nico Step 12 Post-Publish Checks

Templates are parameterized — PM fills target URL, priority, audit data per run.

---

## Changelog

- **v1.0** — April 24, 2026 — Initial draft (8-step single-pass workflow)
- **v1.1** — April 24, 2026 — Nico review feedback: install voice (not preserve), reference Brain docs by pointer, Step 6.5 images, Task 2.7/2.8/2.9 logged
- **v2.0** — April 27-28, 2026 — Full pipeline redesign after `/where-to-stay-palermo/` test failure (31 findings). Single-pass writing replaced with 3-pass model (Information → Voice → HTML). Project folder pattern. Scout after Pass 1. Structural Audit added as Step 5. Plus P0 patches D1-D14 from Favignana Pass 3+4 (Apr 28).
- **v2.1** — April 29, 2026 — Full body rewrite to integrate all Apr 27-29 patches into a single coherent 12-step pipeline. Replaces old v1.1 8-step body description. Pass 4 (Nico Manual Edits) formalized as Step 9. Step 10 publish procedure codified (was implicit). Step 11 (Verify Publish) added as mandatory gate. Step 12 (Post-Publish Checks) reassigned from Architect to Claude Code + Nico (Architect has no browser/HTTP access). Findings #48-50 resolved. Brand reference updated: "We Are Palermo Premium Guide" (formerly "The Sicilian Way").
