# SOP_01_Update_Existing_Post.md — Update Existing Post

Last updated: May 2, 2026 (v2.2 — brain-dump-first Pass 2 redesign. 12 steps consolidated to 8. Hard stop on Pass 2 cycles. Voice memos drive voice; agent assembles. Replaces v2.1.)

---

## What This SOP Does

Rewrite an existing wearepalermo.com blog post that's losing traffic per WAP_13. 8 steps. Pass 2 is built around Nico's brain dump per section, not around an agent generating voice from rules.

This SOP is for **rewriting**, not creating. For new posts, see SOP_02.

---

## When To Use

- Post is rotting per WAP_13 (lost clicks YoY)
- Post has structural issues (broken H2 hierarchy, missing voice, outdated facts)
- Post needs full freshness pass (older than 18 months + still ranking)
- NOT for minor edits (typo fixes, single-line changes)

---

## The Core Principle

**Nico's brain dump is the voice source. The Copywriter assembles around it. The Copywriter does NOT generate voice from rules.**

This was learned the hard way across Favignana (Apr 28, 3 cycles) and where-to-stay-palermo (May 1-2, 4 cycles + PM-direct rebuild). Both runs proved that even with WAP_05 + WAP_05b in place, the agent transcribes voice memos rather than restructuring them, and produces memo-shaped prose when asked to "install voice" on a Pass 1 information draft. SOP_01 v2.2 stops fighting this.

---

## Inputs Required

- Target URL (single post)
- WAP_13 GSC audit data: clicks, impressions, position, top queries
- Target status (P1 / P2 / P3 from WAP_13)
- Revenue tier (A / B / C from WAP_13)
- Known quality issues (audit notes + Nico's observations)
- **Nico's availability for a 30-60 min Brain Dump session** (Step 5)

---

## Outputs

Every SOP_01 run produces:

1. Republished post live on wearepalermo.com (verified via fetch within 60 seconds of publish)
2. Project folder `projects/POST_[slug]/` with deliverable files (8 files in v2.2)
3. Revision log entry in `projects/PROJECT_WAP_Content_Machine/04_Change_Log.md`
4. Baseline metrics snapshot for 6-week comparison
5. Any new stories captured → SOP_03
6. Any new experiences/places captured → queue for WAP_10 update
7. Any affiliate link issues → queue for WAP_12 update
8. Findings logged to `projects/PROJECT_WAP_Content_Machine/07_Test_Run_Findings.md`

---

## Agents & Responsibilities (v2.2)

| Agent | Role in SOP_01 v2.2 |
|---|---|
| **WAP PM** | Orchestrates workflow. Writes handoff prompts. Runs Brain Dump session with Nico (Step 5). Transcribes voice memos verbatim. Hard-stops Pass 2 after 2 Copywriter cycles. Updates docs after every step. |
| **WAP Architect** | Step 2 (snapshot + prep + audit consolidated). Step 7 (Pass 3 HTML + schema). Architect does NOT publish to WordPress. Architect does NOT run post-publish live checks. |
| **WAP Copywriter** | Step 3 (Pass 1 SKELETON, structure only, no prose flow). Step 6 (Pass 2 ASSEMBLY from brain dump verbatim, hard stop at 2 cycles). |
| **WAP Scout** | Step 4 (fact verification, runs in parallel with Pass 1). |
| **Nico** | Step 5 (Brain Dump session with PM). Step 8 (Pass 4 manual edits). Publishes via WordPress UI. Reviews and approves at every PM gate. |
| **Claude Code** | Verify Publish via web_fetch. Post-publish mechanical checks via curl. Final commit verification. |

---

## The 8-Step Workflow

### Phase A — SETUP

#### Step 1 — Intake (PM, ~15 min)

1. Open WAP_13 (latest GSC audit)
2. Select highest-priority post not yet updated
3. Confirm post still matches its audit classification
4. Create project folder: `projects/POST_[slug]/`
5. Verify all linked URLs in the post return 200 (per Finding #57)
6. Capture Nico's brain dump on the post (free-form, before any structural work)
7. Create Execution Backlog entry in PROJECT_WAP_Content_Machine
8. Announce to Nico: "Starting SOP_01 v2.2 on [URL]. Expected total: ~3-5 hours of focused work, including ~30-60 min Brain Dump session at Step 5."

**Deliverable:** `projects/POST_[slug]/01_Intake.md` containing target URL, audit data, Nico's brain dump on the post.

---

#### Step 2 — Architect Prep (Architect, ~30 min — consolidated)

Architect produces ONE consolidated deliverable covering snapshot + prep + audit. Sub-sections:

**A. Live HTML snapshot:**
- Fetch the live URL via web_fetch
- Save the rendered HTML
- Note: image URLs in this snapshot are NOT trustworthy as canonical (per D14)

**B. Prep packet:**
- Pull GSC performance snapshot (6 months: top 10 queries, position, clicks, CTR — Architect pulls, NOT PM, per Finding #56)
- Inventory all outbound links from live HTML (affiliate / internal / external)
- Cross-check each affiliate link against WAP_12; flag broken or missing
- Pull 5+ internal link candidates from current WAP post inventory
- Check current schema markup (FAQPage? Article? Missing?)
- Note technical issues
- Identify SERP competitors via Ubersuggest if relevant

**C. Structural audit:**
- Apply Cold Reader Reality Check (relevant items per post type)
- Identify structural gaps
- Decide: FULL REWRITE or SURGICAL EDIT
- If FULL REWRITE: produce new H2 outline with target word counts per section
- **Reader-flow validation (per Finding #68):** map "what would a real reader ask FIRST? SECOND? THIRD?" Does the outline answer questions in the order a human asks them? PM cannot approve Step 2 without independently walking through the reader-flow test.
- Lock voice notes for downstream agents (signature moves expected, mode A/B, story slots)
- Lock special instructions for Pass 1 SKELETON, Pass 2 ASSEMBLY, Pass 3 HTML

**Amendment protocol:** If later steps produce structural divergences from the audit, the divergence MUST update `02_Architect_Prep.md` with an explicit "Amended [date]" entry. Don't ship divergence silently.

**Deliverable:** `projects/POST_[slug]/02_Architect_Prep.md` containing all three sub-sections.

---

### Phase B — WRITE (3 passes + Brain Dump + Nico final)

#### Step 3 — Pass 1 SKELETON (Copywriter, ~30-45 min)

**This is NOT a full prose draft. This is structure only.**

PM writes handoff to Copywriter with:
- `02_Architect_Prep.md` outline (every H2 in the outline MUST be in the skeleton)
- Reference: WAP_06 (format), WAP_06b (post-type), WAP_12 (affiliate links)
- **Voice docs (WAP_05, WAP_05b) are NOT input for Pass 1.** Voice comes in at Step 6.
- Specific instructions for this post (NO-GO list, post-type rules)

Copywriter produces SKELETON markdown:

**WHAT IS IN A SKELETON:**
- All H2 and H3 headings exactly per outline
- TL;DR table structure (5 rows, empty cells with bracketed labels for what each cell will contain)
- Hotel cards: name + type + stars + Booking URL VERBATIM from WAP_12 + 1-line factual descriptor (NOT prose)
- FAQ section: 6-8 question headings + bracketed labels for what each answer will cover
- Callout placement markers: `[CALLOUT — Local's Take/Pick/Warning: TOPIC]` with 1-line bracketed description of what it covers
- Image slot placeholders (11 typical for destination guides)
- Internal link suggestions (3-5)
- Suggested meta title, meta description, URL slug
- All factual claims wrapped in [VERIFY: X] flags for Scout

**WHAT IS NOT IN A SKELETON:**
- No prose paragraphs
- No voice install
- No "rough" drafting of paragraph content
- No invented anecdotes, callouts, or rhythm
- No transitions between sections (those go in Step 6)

**Self-check before submitting (mechanical, bash output PASTED, per Finding #67):**
- All H2s from outline present? (bash count vs outline count)
- Every hotel URL VERBATIM from WAP_12? (cross-check table, every URL — per Finding #70)
- All [VERIFY:] flags listed and counted
- 0 prose paragraphs (this is a skeleton, not a draft)
- 0 em-dashes
- Word count total (skeleton word count target: ~30-40% of finished article)

**Deliverable:** `projects/POST_[slug]/03_Pass1_Skeleton.md`

---

#### Step 4 — Scout Fact Check (Scout, ~20-30 min, runs in parallel with Pass 1)

PM dispatches Scout in parallel with Step 3. Scout works on the live post + Architect Prep, not the skeleton. Scout's job: verify all factual claims, prices, hours, distances, URLs — return VERIFIED / UPDATE / REMOVE / PARK per claim.

**Deliverable:** `projects/POST_[slug]/04_Scout_Verification.md`

PM applies Scout corrections to the skeleton in Step 5 prep.

---

#### Step 5 — Brain Dump session (PM + Nico, ~30-60 min) ⭐ NEW IN v2.2

This is the highest-leverage step in the SOP. It replaces "Copywriter installs voice on Pass 1 prose" with "Nico generates voice in real time, PM transcribes verbatim."

**Procedure:**

1. PM and Nico open the Pass 1 SKELETON together.
2. PM walks Nico through the skeleton H2 by H2.
3. For each H2, Nico voice-memos for 5-8 minutes covering:
   - The opening hook for that section
   - The pros (in his own words, his own examples, his own slap lines)
   - The cons (same)
   - Any callouts marked in the skeleton (Local's Take/Pick/Warning)
   - The transition into the next section
4. PM transcribes Nico's voice memos VERBATIM. No editing. No "cleaning up." No "improving rhythm." If Nico says "you know, like" three times in a sentence, that's in the transcript. The Copywriter strips filler in Step 6, not PM in Step 5.
5. Each H2 gets its own subsection in the brain dump file, clearly labeled with the H2 title and any callout markers.

**Why verbatim:** the rhythm IS in Nico's spoken delivery. Setup-pause-payoff. Mocking dialogue. Hyperbolic specifics. Slap closers. Light editing destroys it. The Copywriter's job in Step 6 is to clean filler and add transitions, NOT to "improve" Nico's voice.

**Special callout types Nico voices in this step:**
- 7 Mistakes / Dos & Don'ts callouts (per post type)
- ZTL / La Via dei Tesori / WiFi / area-specific explainers (anything readers don't know what is)
- Stories from Story Bank (S001-S00X) where they fit
- "Where NOT to stay" subsection per area
- Local's Pick callouts (Nico's specific top recommendation)

**Self-check before submitting:**
- Every H2 in the skeleton has a brain dump subsection? (count match)
- Every callout marker in the skeleton has been voiced? (count match)
- No PM editing introduced into Nico's transcribed prose?

**Deliverable:** `projects/POST_[slug]/05_Brain_Dump.md`

---

#### Step 6 — Pass 2 ASSEMBLY (Copywriter, ~60-90 min, HARD STOP at 2 cycles)

PM writes handoff to Copywriter with:
- `03_Pass1_Skeleton.md` (the structural frame)
- `05_Brain_Dump.md` (the voice source — VERBATIM Nico)
- `04_Scout_Verification.md` (factual corrections to apply)
- WAP_05 (voice rules — for tightening filler ONLY)
- WAP_05b (voice in action — for reference, NOT generation)
- WAP_06 (format)
- WAP_06b (post-type rules)

**Copywriter's job in Step 6 = ASSEMBLY:**

1. For each H2 in the skeleton, paste the corresponding brain dump VERBATIM into the prose slots.
2. Strip Nico's spoken filler ("you know," "like," "I don't know," "basically," um/uh, repetitions).
3. Apply WAP_06 Foundation Rules: split text blocks at 180 chars, split sections at 400 words.
4. Apply WAP_05 mechanical fixes: 0 em-dashes (replace with three-dot pause or period), 0 banned words (SEO/AIO/ranking/keywords/schema markup).
5. Add transitions BETWEEN sections (not within). Transitions are 1-2 sentences max. Connect what just happened to what's coming. Don't invent voice.
6. Apply Scout corrections (URL fixes, factual updates, B&B star strips, etc.).
7. Run mechanical self-check (bash output PASTED, per Finding #67).

**Copywriter's job in Step 6 IS NOT:**

- Rewriting Nico's prose to "improve rhythm" — the rhythm is the rhythm
- Generating new callouts from voice memos — that's transcription-by-rewriting, the Favignana + where-to-stay failure mode
- Replacing Nico's specific images with "better" ones
- Inventing new sections, jokes, or content not in the skeleton or brain dump
- Treating voice memos as "raw material" to be reworked — they ARE the voice

**THE ASSEMBLER PRINCIPLE (locked):** If the Copywriter finds itself paraphrasing a brain-dump block to "make it flow better," STOP. The flow is in the source. Paraphrasing IS transcription-by-rewriting. Re-paste the brain dump verbatim. Strip filler only.

**Mandatory self-check (bash output PASTED, per Findings #67 + #70):**

```
=== Pass 2 ASSEMBLY mechanical scan ===

wc -w of body: [paste]
grep -c "—" (em-dashes): [paste, must be 0]
grep -cE "(SEO|AI Overview|ranking|keywords|schema markup)": [paste, must be 0]
grep -cE "(Castellamare|Albergaria|Villa Igea|Piazza Matrice|Familia|Daita'|Ruggero VII)": [paste, must be 0]
grep -c "\[VERIFY:" (must be 0 — all resolved by Scout in Step 4): [paste]

=== Brain dump preservation audit ===

For each H2 in skeleton, confirm brain dump prose appears in Pass 2 substantially verbatim (>80% word overlap):
H2 1: [overlap %]
H2 2: [overlap %]
... (one row per H2)

Any H2 below 80% overlap is a paraphrasing failure. Rebuild from brain dump.

=== Affiliate URL audit (per Finding #70) ===

Every hotel URL cross-checked against WAP_12 verbatim:
| Hotel | URL in draft | URL in WAP_12 | Match Y/N |
| ... |

Any N is a Pass 2 fail. Fix before submit.
```

**HARD STOP RULE (per Finding #73):**

If Pass 2 v2 fails Nico's review, PM does NOT dispatch v3 to Copywriter. PM has 2 options:

(a) **PM-direct rebuild from brain dump.** PM takes `05_Brain_Dump.md` and assembles Pass 2 directly in chat or by writing the file. ~30-45 min.

(b) **Nico writes Pass 2 himself.** Copywriter is bypassed entirely for Pass 2. Copywriter resumes at Step 7 (Pass 3 HTML) only.

Either path is acceptable. Burning 4+ Copywriter cycles is not.

**Deliverable:** `projects/POST_[slug]/06_Pass2_Voice.md` (committed to repo BEFORE proceeding to Step 7 — per Finding #75, no chat-only artifacts).

---

### Phase C — FINISH

#### Step 7.0 — Live HTML Snapshot Capture (PM/Architect, ~10 min) ⭐ NEW MAY 3, 2026

Before Pass 3 starts, capture live HTML snapshots of:
1. The target article URL (always)
2. Every internally-linked WAP article that contributes images or canonical patterns
3. The most recent published article using the same post-type pattern

Save as `projects/POST_[slug]/00_Live_HTML.md`. Pass 3 cannot start until this exists. Per Finding #82.

---

#### Step 7 — Pass 3 HTML conversion (Architect, ~60-90 min)

Architect converts the locked Pass 2 markdown to canonical WAP HTML per WAP_06 v2.2:
- Callout div wpautop pattern (D5)
- Hotel card template (D3)
- TL;DR table (D4)
- FAQ details/summary inside faq-brutto-ma-funziona div (D10)
- 8-step author intro architecture (D2)
- Article schema JSON-LD with author=Nico Barcellona (D8)
- FAQPage schema JSON-LD MANDATORY (D8)
- 11 image slots with [NICO: paste URL] tokens preserving old article images where instructed

NO content changes. NO voice rewrites. NO new sections. Pure structural conversion + schema injection.

**Deliverable:** `projects/POST_[slug]/07_Pass3_HTML.md`

---

#### Step 8 — Pass 4 + Publish + Verify (Nico + Claude Code, ~45 min)

Nico:
1. Fills image URLs from WordPress media library
2. Final read-through edits
3. Publishes via WordPress UI
4. Mobile preview check
5. GSC URL Inspection check

Claude Code:
1. web_fetch the live URL within 60 seconds of publish
2. Confirm canonical HTML matches Pass 3 output
3. Run 6 post-publish mechanical checks (schema validates, affiliate URLs return 200, internal links resolve, etc.)
4. Commit baseline metrics snapshot for 6-week comparison

**Deliverable:** Live post + `projects/POST_[slug]/08_Post_Publish_Verification.md`

---

## Project File Structure (v2.2 — 8 deliverables)

```
projects/POST_[slug]/
├── 01_Intake.md              (Step 1)
├── 02_Architect_Prep.md      (Step 2 — snapshot+prep+audit consolidated)
├── 03_Pass1_Skeleton.md      (Step 3)
├── 04_Scout_Verification.md  (Step 4, parallel)
├── 05_Brain_Dump.md          (Step 5 — NEW, Nico voice memos verbatim)
├── 06_Pass2_Voice.md         (Step 6 — assembly from brain dump)
├── 07_Pass3_HTML.md          (Step 7)
└── 08_Post_Publish_Verification.md (Step 8)
```

Replaces v2.1's 12-step / 10-deliverable structure.

---

## What Changed From v2.1 → v2.2 (May 2, 2026)

| Old (v2.1) | New (v2.2) | Why |
|---|---|---|
| 12 steps | 8 steps | Reduce handoff failures (15 dropped dependencies in one v2.1 run) |
| Architect Steps 2, 3, 4 separate | Consolidated to Step 2 (one deliverable) | Same coverage, fewer gates |
| Step 5 Pass 1 = full prose draft | Step 3 Pass 1 = SKELETON only | Voice generation moved out of Pass 1 |
| Step 7 Pass 2 = Copywriter installs voice on prose | Step 6 Pass 2 = Copywriter assembles brain dump verbatim | Stop asking agent to do what it can't |
| No explicit brain dump step | Step 5 Brain Dump session, Nico voice memos verbatim | Voice source moved upstream of Copywriter |
| Pass 2 loops indefinitely | Hard stop at 2 cycles | Prevent 9-hour disaster (where-to-stay May 1-2) |
| WAP_05/WAP_05b loaded in Pass 1 | WAP_05/WAP_05b loaded only in Pass 2 (for cleanup, not generation) | Match doc usage to actual job |

---

## Changelog

- **v2.2** — May 2, 2026 — Brain-dump-first redesign after where-to-stay-palermo Pass 2 disaster (4 Copywriter cycles + PM-direct rebuild, ~9 hours burned). 12 steps → 8. New Step 5 Brain Dump session. Pass 1 redefined as SKELETON. Pass 2 redefined as ASSEMBLY. Hard 2-cycle stop on Pass 2.
- **v2.1** — April 29, 2026 — Full body rewrite. 12 steps across 3 phases. Pass 4 + Step 11 + Step 12 in canonical pipeline.
- **v2.0** — April 27, 2026 — Original 3-pass model.
