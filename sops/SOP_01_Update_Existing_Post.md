# SOP_01 — Update an Existing Post

**SOP ID:** SOP_01
**Category:** Content — Rescue Track
**Owner:** WAP PM
**Last updated:** April 24, 2026
**Status:** v2.0 (P0 patches Apr 28: D12 mechanical self-check, D13 Pass 3 scope, D14 image placeholders)

---

## Purpose

Take an existing wearepalermo.com post that is losing traffic (P1, P2, or P3 per the latest GSC audit) and republish it with:
- Current Nico voice installed (not just preserved — most old posts predate WAP_05)
- WAP_06 format compliance
- AI Overview-resistant structure (first 540 words contain extractable answer)
- Verified and working affiliate links
- Fact-checked claims
- Schema markup where applicable
- Images appropriate to the content

This SOP is the core rescue workflow. Not for creating new content (use SOP_02).

---

## When To Use

Run SOP_01 when any of these are true:
- Post is flagged P1/P2/P3 in the latest GSC audit (see WAP_13)
- Post has dropped 30%+ YoY clicks
- Post references outdated prices, names, hours, or facts
- Post violates current WAP_06 format rules
- Post predates current WAP_05 voice guide

Do NOT run SOP_01 when:
- Post is ranking well (Status: RANKING or EVERGREEN)
- Post is seasonal and currently out-of-season
- Post is flagged NO_DATA (those need a delete-or-rewrite decision, not an update)

---

## Prerequisites

Before starting, confirm the following are accessible:

- **All current Brain docs** (WAP_00 is the index — use it to confirm which docs are relevant)
- **Key Brain docs always used by SOP_01:**
  - WAP_05 — Voice and Persona (source of truth for voice rules)
  - WAP_06 — Content Format (source of truth for post structure, first-540, schema, length tiers)
  - WAP_08_STORY_BANK_INDEX.md + brain/stories/ folder (story raw material)
  - WAP_10 — Places, Experiences, Monuments, Rituals (all raw material for what to mention)
  - WAP_12 — Affiliate Links Registry (canonical affiliate URLs)
  - WAP_13 — Latest GSC Audit (source of priority and status for target post)
- **WordPress access:** admin credentials, Rank Math or Yoast plugin confirmed installed
- **GSC access:** current performance data for the target URL
- **Target post live URL:** open in a tab

Brain docs listed above are the MINIMUM. SOP_01 never hardcodes a Brain doc range. WAP_00_INDEX always reflects what currently exists.

---

## Inputs

For every SOP_01 run, gather:

1. Target URL (single post)
2. GSC snapshot (last 6 months: clicks, impressions, position, top queries)
3. Current post content (full copy of live HTML or markdown)
4. Target status (P1 / P2 / P3 from WAP_13)
5. Revenue tier (A / B / C from WAP_13)
6. Known quality issues (from audit notes + Nico's observations)

---

## Outputs

Every SOP_01 run produces:

1. Republished post live on wearepalermo.com with images
2. Revision log entry in `projects/PROJECT_WAP_Content_Machine/04_Change_Log.md`
3. Baseline metrics snapshot (pre-rewrite clicks/position) for later comparison
4. Monitoring trigger set for 6-week check-in
5. Any new stories captured → SOP_03 (Add Story to Bank)
6. Any new experiences/monuments/rituals captured → queue for WAP_10 update
7. Any affiliate link issues discovered → queue for WAP_12 update

---

## Agents & Responsibilities

| Agent | Role in SOP_01 |
|---|---|
| **WAP PM** | Orchestrates workflow. Writes handoff prompts. Tracks time. Updates docs. Schedules 6-week monitoring. |
| **WAP Architect** | Pulls GSC data. Builds prep packet. Publishes to WordPress. Adds schema markup. Verifies affiliate links against WAP_12. Tags analytics. |
| **WAP Copywriting** | Produces rewrite draft per WAP_05 voice + WAP_06 format. Pulls from WAP_08 stories + WAP_10 experiences. Generates FAQs. Revises on surgical feedback. |
| **WAP Scout** | (to be built as Task 2.7 before Phase 3) Verifies factual claims. Returns VERIFIED / DISPUTED / UNVERIFIABLE per claim with sources. |
| **Nico** | Provides personal anecdotes when gaps need filling. Reviews drafts. Gives surgical feedback (School C). Approves final. Adds images (until Task 2.8 Image Agent exists). |

---

## The 8-Step Workflow

### STEP 1 — INTAKE (PM, est 5 min)

1. Open WAP_13 (latest GSC audit Brain doc)
2. Select highest-priority post not yet updated
3. Confirm post still matches its audit classification (quick GSC re-check)
4. Create Execution Backlog entry: `- [ ] Update [URL] via SOP_01 [Copywriting + Architect + Scout] [Est: 90 min | Actual: __]`
5. Announce to Nico: "Starting SOP_01 on [URL]. Expected total time: ~90 min."

**Deliverable:** target URL confirmed + backlog entry created.

---

### STEP 2 — PREP (Architect, est 15 min)

Architect builds the prep packet Copywriting needs.

1. Pull GSC performance snapshot (6 months: top 10 queries, position, clicks, CTR)
2. Copy current live post content to scratch doc
3. Inventory all outbound links (flag affiliate vs. internal vs. external)
4. Check each affiliate link in WAP_12; flag any that are broken or missing from WAP_12
5. Pull 5+ internal link candidates from WAP's current post list
6. Check current schema markup on target URL (FAQPage? Article? Missing?)
7. Note technical issues (broken images, broken links, mobile layout breaks)

**Deliverable:** Prep packet containing:
- Target URL
- Current content (full)
- Top 10 GSC queries
- Current clicks, position, CTR
- Affiliate link audit (working / broken / missing from WAP_12)
- Internal link candidates (5+)
- Outbound links inventory
- Schema state
- Technical issues

PM reviews. If packet is incomplete, Architect fixes only the missing pieces.

---

### STEP 3 — REWRITE DRAFT (Copywriting, est 25-40 min)

PM writes handoff prompt to Copywriting with:

- Prep packet (full)
- Target URL, topic, audit priority, revenue tier
- **Reference-by-pointer (NOT copy):**
  - Apply WAP_05 voice rules (full doc in Copywriting's context)
  - Apply WAP_06 format rules (full doc in Copywriting's context)
  - Pull relevant stories from WAP_08 (Copywriting scans index for tag matches, opens specific story files)
  - Pull relevant experiences/monuments from WAP_10 (same scan pattern)
  - Use affiliate links from WAP_12 (canonical URLs only — no invented links)
- Target word count per WAP_06 length tiers
- Specific instructions for this post:
  - First 540 words must contain the answer to the primary query
  - Install current Nico voice (this post may predate WAP_05)
  - Named business rule per WAP_08 (genericize in free content unless flagged otherwise)

Copywriting produces draft markdown doc:
- Full post body
- FAQ section (5-8 questions) if applicable
- Suggested meta title (under 60 chars)
- Suggested meta description (under 155 chars)
- Suggested URL slug (only if change needed)
- Internal link suggestions (5+)
- Image placement suggestions with caption drafts (for Nico's Step 6.5)
- Any [CLAIM NEEDS VERIFICATION] flags for Scout

**Note on voice:** Old posts do not have current Nico voice. The job is to INSTALL the voice, not preserve it. Copywriting rewrites sentences that sound generic, AI, or pre-WAP_05.

**Deliverable:** draft doc in markdown, ready for Scout.

---

### STEP 4 — FACT CHECK (Scout, est 10 min)

PM writes handoff prompt to Scout. Input: draft from Step 3.

Scout extracts every factual claim and returns per claim:
- **VERIFIED** + source URL
- **DISPUTED** + explanation + source URL
- **UNVERIFIABLE** (e.g., personal anecdotes, opinion, matters of taste)

**Scope Scout checks:**
- Statistics and numbers
- Historical facts
- Opening hours, prices, addresses (any named business)
- Place names and locations
- Names of people (historical figures, chefs, authors)
- Dates
- Claims phrased as fact ("oldest X in Y", "only place that does Z")

**Scope Scout does NOT check:**
- Nico's first-hand observations
- Opinions and subjective calls
- Jokes and comedic framing
- Voice choices

**Deliverable:** fact-check report with verdict + source per claim.

PM reviews. DISPUTED claims go back to Copywriting for that specific fix only.

---

### STEP 5 — NICO REVIEW + SURGICAL FEEDBACK (Nico, est 15 min)

PM delivers to Nico:
- Fact-checked draft (full)
- Scout's report
- Suggested meta title + description
- Image placement suggestions

Nico reads full draft. Provides **surgical feedback** (School C):
- "Line X: too AI. Cut it."
- "Change 'upset' to 'pissed'."
- "Add a line after Y about Z."
- "FAQ #3 is generic. Rewrite based on [specific angle]."

Nico does NOT rewrite paragraphs. Nico writes feedback, Copywriting revises.

If Nico mentions new observation, new place, or new experience worth archiving:
- Story → flag for SOP_03 intake
- Place/monument/experience → flag for WAP_10 update

**Deliverable:** Nico's feedback doc (bullet list of edits + approvals).

---

### STEP 6 — REVISION + FINAL APPROVAL (Copywriting → Nico, est 10 min)

PM passes Nico's feedback to Copywriting. Copywriting applies feedback exactly — no creative additions, no improvements beyond what Nico flagged.

Nico re-reads ONLY edited sections. Not the whole post.

Nico approves or gives one more round of surgical feedback. Max 2 revision rounds total. If a third round is needed, the draft is structurally wrong → return to Step 3.

**Deliverable:** Nico-approved final draft.

---

### STEP 6.5 — IMAGES (Nico, est 10 min — interim process)

**Interim process until Image Agent exists (Task 2.8):**

Nico:
1. Reviews image placement suggestions from Step 3
2. Sources images (personal library, AI-generated, Unsplash, stock)
3. Edits images if needed (remove objects, adjust, enhance)
4. Saves with proper filenames (descriptive-kebab-case.jpg)
5. Writes alt text for each image (accessibility + SEO)
6. Hands images + placements to Architect

**When Image Agent (Task 2.8) exists, this step becomes a handoff prompt to the agent, same shape as Scout.**

**Deliverable:** image set + alt text + placement map.

---

### STEP 7 — PUBLISH + TRACK (Architect, est 10 min)

PM writes handoff prompt to Architect with:
- Nico-approved draft
- Image set + alt text + placements from Step 6.5
- Affiliate links from WAP_12 (verified in Step 2)

Architect:
1. Opens WordPress editor for target URL
2. Replaces post content with approved draft
3. Inserts images at placement points with alt text
4. Updates meta title + meta description (Rank Math / Yoast)
5. Updates URL slug if changed (adds 301 redirect from old slug)
6. Adds/updates FAQPage schema markup if FAQ section present
7. Adds/updates Article schema markup with Nico as Author
8. Verifies all affiliate links live and correct per WAP_12
9. Adds 5+ internal links from Step 2 suggestions
10. Runs Rank Math / Yoast SEO check, fixes critical issues
11. Publishes
12. Submits updated URL to GSC for re-indexing
13. Logs pre-rewrite baseline metrics to `projects/PROJECT_WAP_Content_Machine/07_SOP01_Test_Log.md`
14. Sets 6-week monitoring reminder

**Deliverable:** post live with images, baseline logged, monitoring set.

---

## Step Time Budget Targets (for Phase 3 measurement)

| Step | Agent | Target | Stretch |
|---|---|---|---|
| 1 Intake | PM | 5 min | 10 min |
| 2 Prep | Architect | 15 min | 25 min |
| 3 Rewrite | Copywriting | 25 min | 40 min |
| 4 Fact Check | Scout | 10 min | 20 min |
| 5 Nico Review | Nico | 15 min | 30 min |
| 6 Revision | Copywriting + Nico | 10 min | 25 min |
| 6.5 Images | Nico (→ Agent later) | 10 min | 20 min |
| 7 Publish | Architect | 10 min | 20 min |
| **TOTAL** | | **100 min** | **190 min** |

Phase 3: run SOP_01 on `/where-to-stay-palermo/`. Measure actual time per step. If totals exceed 190 min, SOP_01 needs simplification before production use.

---

## Failure Modes & Recovery

| Problem | Fix |
|---|---|
| Copywriting produces AI-sounding output (voice violation) | Send back with specific WAP_05 rule citation. If 2 rounds fail, prompt needs fixing — log as Task. |
| Scout returns multiple DISPUTED claims | Pause. Nico decides: remove claims, or rewrite with verified alternatives. |
| Affiliate link in WAP_12 is broken | Architect flags. Triggers SOP_05 (Affiliate Link Verification — to be built as Task 2.9). Temporarily use next-best link. |
| Nico's surgical feedback exceeds 2 rounds | Structural problem with draft. Return to Step 3 with new guidance. Do not patch. |
| Architect publishes with broken affiliate link | Immediate hotfix. Log incident. Audit triggers WAP_12 update. |
| Image missing or broken at publish | Revert to draft status. Return to Step 6.5. |
| 6-week monitoring shows NO improvement | Trigger SOP_01b (revision revision) — to be defined. Park for now. |
| 6-week monitoring shows WORSE performance | Rollback via WordPress revision history. Investigate. Log in audit. |

---

## Post-Publish Monitoring

At the 6-week mark after republish:
- Clicks (last 14 days pre-republish vs. last 14 days post + 4 weeks)
- Position for primary keyword
- CTR
- AI Overview citation presence (manual Google check)

Log to `07_SOP01_Test_Log.md`:
- Pre-rewrite baseline
- 6-week post-rewrite snapshot
- Delta (absolute + %)
- Verdict: RECOVERED / PARTIAL / FAILED
- Notes

3 RECOVERED in a row = SOP_01 production-ready.
3 FAILED in a row = SOP_01 has a flaw. Revise.

---

## Handoff Prompt Templates

Templates live in a separate file: `sops/SOP_01_Handoff_Prompts.md` (to be created).
- Template 1: Architect Prep Packet
- Template 2: Copywriting Rewrite Draft
- Template 3: Scout Fact Check
- Template 4: Architect Publish

Templates are parameterized — PM fills target URL, priority, audit data per run.

---

---

## Pass 2 Self-Check (MECHANICAL, NOT ESTIMATE) — D12 Apr 28

Pass 2 self-check is a MECHANICAL scan, not a human estimate. Lesson from Apr 28 Favignana run: Pass 2 v3 self-claimed paragraph-length compliance via human estimate; mechanical scan in Pass 3 found 19 wall-of-text violations. Human estimates are unreliable on length compliance.

**Required scans (every Pass 2 submission must include):**

1. **Paragraph length scan:** Every `<p>` block, count words. Flag any >45 words. Flag any >180 chars. Report count of violations.
2. **Em-dash regex:** Find all `—` (em-dash unicode). MUST be zero. Report exact count.
3. **Banned-words regex:** Find all instances of "SEO", "AI Overview", "ranking", "keywords", "schema markup" in body. MUST be zero. Report exact count.
4. **[VERIFY:] tag scan:** Find all `[VERIFY:`. MUST be zero. Report count.
5. **Word count grep:** Total word count of body (excluding agent notes). Report number.
6. **Bold full-sentence scan:** Find any `<strong>` content with 50+ chars or 8+ words. Report count.
7. **"Piazza Madrice" scan:** Find any "Matrice" (typo). MUST be zero in body. Report count.

**Pass 2 deliverable must include a self-check table with exact counts for all 7 scans, not "compliant ✅" estimates.** If any count is non-zero where it should be zero, fix before submitting.

---

## Pass 3 Scope Clarification — D13 Apr 28

**Scope rules (Apr 28 clarification):**

Pass 3 IS:
- Mechanical format application (HTML conversion, template wrapping, callout boxes, hotel cards, TL;DR table, Continue Planning block, FAQPage schema)
- Image placement and URL filling (or `[NICO: paste URL]` placeholder if URL not verifiable)
- **Mechanical paragraph splits at sentence boundaries** if Pass 2 missed wall-of-text violations. This is allowed and expected. NOT a voice rewrite.
- Final mechanical scans (em-dash purge, banned-words, paragraph length, bold logic)

Pass 3 IS NOT:
- Voice rewrite (locked in Pass 2)
- Structural changes (locked in Structural Audit + Pass 1)
- Fact corrections (locked in Pass 2 with Scout corrections)
- New content additions

**The mechanical paragraph split rule:** if Pass 2 ships with paragraphs >45 words or >180 chars, Pass 3 splits them at the nearest sentence boundary without changing wording. This is MANDATORY mechanical work, not optional. Architect should challenge upstream (escalate to PM) if Pass 2 ships with >5 paragraph-length violations — that signals a Pass 2 self-check failure.

**Canonical reference article rule (PM decision Apr 28):** When in doubt about callout/FAQ/intro patterns, the most recent published WAP article is canonical, not the spec. Currently: Tourist Info article (April 2026). The spec will always lag actual practice in a one-person operation. "Diff against most recent published article" is a Step 9 input.

---

## Image URL Verification — D14 Apr 28 (Placeholder Default)

Architect cannot HTTP-test image URLs without browser access. Therefore the canonical rule is: **all images in Pass 3 ship as `[NICO: paste URL]` placeholders unless the URL has been verified by Nico in this session OR is in the canonical Tourist Info reference article.**

DO NOT infer image URLs from naming conventions. Apr 28 examples that broke this rule:
- Inferred `b-amp-b-il-tufo.jpg`, actual was `il-tufo.jpg`
- Inferred `i-pretti-favignana.jpg`, actual was `i-pretty.jpg` (English variant)
- Inferred `residence-scirocco-favignana.jpg`, actual was `scirocco-e-tramontana-faviganana.jpg` (typo "faviganana" preserved across years)

**Architect workflow:**
1. If Pass 2 includes verified image URLs → use as-is
2. If `00_Live_HTML.md` snapshot has image URLs → DO NOT TRUST without verification (snapshots may be stale)
3. If Tourist Info article uses an image (e.g. Nico portrait) → use that URL as canonical
4. If neither → ship as `[NICO: paste URL]` placeholder for Pass 4

**Result:** placeholders are not failures. They are the correct conservative default. Pass 4 (Nico manual edits) is the URL-fill step.

---

## Step 10 — Publish (REVISED Apr 29)

WordPress publish procedure (codified):

1. **Open WordPress admin** for the target post URL
2. **Switch editor to Code Editor / Text mode** (NOT Visual mode — Visual mode mangles HTML, callout structure, and JSON-LD schema)
3. **Replace post body**: delete current content, paste Pass 4 HTML from `09_Pass4_Nico_Final.md`
4. **Update post title (H1)** to match Pass 4 spec
5. **Update Yoast SEO panel:**
   - Focus keyphrase (typically primary keyword)
   - SEO title (50-60 chars, includes keyphrase)
   - Slug — DO NOT CHANGE (URL preservation for SEO juice)
   - Meta description (140-155 chars, includes keyphrase, in voice)
6. **Set author** to "Nico Barcellona" (NOT "palermo-boss" or any legacy handle). If display name shows wrong: Users → Profile → Display name publicly as → "Nico Barcellona" → Update.
7. **Set featured image** per Pass 4 spec (alt text per Pass 4)
8. **Update publish date to today** (HARD RULE — always today's date on republish, never keep original)
9. **Set/preserve categories and tags**
10. **Hit Update**

---

## Step 10.5 — Verify Publish (NEW Apr 29)

MANDATORY. Cannot skip. Within 60 seconds of hitting Update:

1. **Open the live URL in incognito** (or use curl/web_fetch from CLI)
2. **Verify presence** of these markers from Pass 4:
   - New post title in `<title>` and `<h1>`
   - New H2 #1 wording
   - TL;DR table visible (search HTML for `tldr-box` class or first row content)
   - Featured image is the new one (search for new image filename)
   - Author byline is "Nico Barcellona"
3. **Verify absence** of old markers:
   - Old title
   - Old H2 wording
   - Old callout photo filename (if changed)
4. **If any marker is wrong**: publish failed (silent save, draft saved instead, cache issue, or wrong post edited). DO NOT proceed to Step 11. Return to WordPress and re-publish. Verify again.

Lesson from Apr 28-29 Favignana run: the post sat unpublished for 14 hours because no verify-publish step existed. SOP operated on assumption "publish happened" without proof. This step is non-negotiable.

---

## Step 11 — Post-Publish Technical Checks (REVISED Apr 29)

**Reassigned**: Step 11 is now executed by **Claude Code** (CLI access via curl/web_fetch), NOT by the Architect agent (which has no browser/HTTP access in normal Claude project sessions).

**Hybrid execution**:
- Claude Code runs 6 of 8 checks mechanically (schema HTML presence, author attribution, broken-link spot-check, image render check, internal link tab behavior, affiliate ID verification)
- Nico runs 2 browser-only checks (mobile preview in Chrome DevTools or phone, GSC URL Inspection in Search Console)
- Claude Code outputs `11_PostPublish_Checks.md` with PENDING_NICO sections for the browser checks
- Nico fills the PENDING_NICO sections after running checks
- Final commit closes the post

The Architect agent is no longer the right specialist for Step 11. Architect handles upstream technical work (schema design, prep, structural audit), not live URL verification.

---

## Changelog

- v1.0 — April 24, 2026 — Initial draft.
- v1.1 — April 24, 2026 — Nico review feedback applied:
  - "Preserve voice" → "install voice" throughout
  - Hardcoded WAP_00-10 reference replaced with "all current Brain docs"
  - WAP_05/06 format rules referenced instead of duplicated in Step 3
  - WAP_12 Affiliate Links Registry added as source of truth (new doc to build)
  - WAP_13 Latest GSC Audit added as source of truth (new doc to build)
  - WAP_10 expanded scope noted (includes monuments, experiences, rituals)
  - New Step 6.5 — Images (Nico manual until Image Agent exists)
  - Task 2.7 (Scout), 2.8 (Image Agent), 2.9 (Affiliate Verification SOP) logged as follow-ups
  - Total time budget updated to 100/190 min with images step added
- v2.0 — April 28, 2026 — P0 patches from Favignana Pass 3+4 session:
  - D12: Pass 2 self-check requires mechanical scans with exact counts (not human estimates). 7 mandatory scans.
  - D13: Pass 3 scope explicitly allows mechanical paragraph splits at sentence boundaries. Canonical reference article rule codified.
  - D14: Image URL inference banned. Placeholder default `[NICO: paste URL]` for all unverified URLs.
- v2.1 — April 29, 2026 — Favignana closeout patches:
  - Step 10 codified: WordPress publish procedure (Code Editor mode, Yoast fields, author setting, featured image, hard rule publish date always today)
  - Step 10.5 added: mandatory verify-publish via fetch within 60 seconds (triggered by 14-hour unpublished gap on Favignana)
  - Step 11 reassigned: from Architect agent to Claude Code (CLI) primary + Nico browser checks. Architect has no HTTP access in normal sessions.