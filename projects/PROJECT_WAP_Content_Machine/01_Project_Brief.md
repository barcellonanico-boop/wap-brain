# 01_Project_Brief.md — WAP Content Machine

**Started:** April 22, 2026
**Status:** Active — Pivot v2.3 (May 3, 2026)
**Owner:** Nico Barcellona

## Goal

Build an AI-assisted content machine for wearepalermo.com that updates rotting blog posts and creates new ones with minimal Nico friction. Target: 80% autopilot. Voice stays Nico (Italian-American comedian, brutally honest, never AI-sounding). Output: well-formatted, SEO-effective, persona-targeted articles published live.

## Strategy v2.3 (May 3, 2026 — pivot)

After May 1-2 disaster on /where-to-stay-palermo/ (~17 hours work, 8+ agent cycles, 5x SOP_01 v2.1 budget overrun, article ultimately hand-finished by Nico), the procedure is being redesigned.

**Old assumption (v2.1, v2.2):** agents write, Nico approves.
**Reality:** Nico writes (via brain dumps and voice memos), agents assemble. Every locked article version traces back to Nico raw input, lightly restructured.

**v2.3 design:**
- Nico provides: target article URL + 2 notes
- Agent does technical recon (GSC + SERP top 5 + Scout obsolete check)
- Agent matches persona scheda (which type of reader is this article for, what they know, what they don't, in what order they ask questions)
- Nico does brain dump (raw, unedited)
- Agent does autonomous chain: structure → first draft → tone of voice → HTML conversion
- Mechanical auditor verifies output against checklist (binary checks, not interpretation)
- Nico final read + publish

Workflow target: ~3-4 hours of Nico time per article (vs ~17 hours under v2.1). Agent autonomous from brain dump to HTML.

## Scope (What's IN)

- Update existing rotting posts via SOP_01 v2.3
- Create new posts via SOP_02 (future)
- Story Bank capture via SOP_03
- Affiliate registry maintenance (WAP_12)
- GSC audit cycles (WAP_13, quarterly)
- Persona schede (WAP_15, NEW in v2.3)
- Canonical HTML snippets library (WAP_06c, NEW in v2.3)
- Mechanical audit script (tools/audit_post.sh, NEW in v2.3)

## Out of Scope (What's NOT)

- New product launches (Sicilian Way redesign, etc.)
- Newsletter/ConvertKit broadcasts (deferred to SOP_04)
- YouTube content workflows (deferred to SOP_06)
- Social media automation (deferred to SOP_08)
- Italian-language site (no plans, English-only)

## Relevant Brain Docs

- WAP_00_INDEX.md (master directory)
- WAP_01_BUSINESS_OVERVIEW.md (the business)
- WAP_05_VOICE_AND_PERSONA.md (Nico voice rules)
- WAP_05b_VOICE_IN_ACTION.md (voice patterns + Voice Memo Rework Discipline)
- WAP_06_CONTENT_FORMAT.md (HTML format + Foundation Rules including 1.5 callout limit, 2 section balance)
- WAP_06b_POST_TYPE_GUIDES.md (per-post-type rules)
- WAP_06c_CANONICAL_SNIPPETS.md (NEW v2.3, HTML library)
- WAP_12_AFFILIATE_LINKS.md (affiliate registry)
- WAP_13_GSC_AUDIT_LATEST.md (which posts to update)
- WAP_15_PERSONAS.md (NEW v2.3, reader personas)

## Relevant SOPs

- SOP_01_Update_Existing_Post.md (currently v2.2, redesigning to v2.3)
- SOP_02_Create_New_Post.md (will inherit v2.3 design)
- SOP_03_Add_Story_To_Bank.md (independent)

## Key Decisions

- April 22, 2026: Project started. Goal: 80% autopilot content machine.
- April 27, 2026: SOP_01 v2.0 created (3-pass model).
- April 28, 2026: Favignana run. 3 Pass 2 voice cycles. WAP_05b created as fix.
- April 29, 2026: SOP_01 v2.1 (12 steps, formal Pass 4 + Verify + Post-publish steps).
- May 1-2, 2026: Where-to-stay-palermo run. 4 Pass 2 cycles + 5 Pass 3 cycles. Article ultimately hand-finished by Nico.
- May 2, 2026 (lunch): SOP_01 v2.2 committed. Brain-dump-first Pass 2. 12→8 steps. Hard 2-cycle stop. Did not prevent same-day Pass 3 disaster.
- May 2, 2026 (afternoon): Pass 3 disaster. Findings #77-84 logged.
- **May 3, 2026: PIVOT to v2.3.** Strategy changed from agent-writes-Nico-approves to Nico-writes-agent-assembles with mechanical auditor. Build minimal viable: 1 persona, 1 audit script, 1 snippet library. Test on 1 article. Iterate. SOP v2.3 written only after MVP works.

## Test Plan v2.3

**Phase 1 — Build MVP (current):**
- Build mechanical audit script first (working backwards from PASS criteria)
- Build 1 persona scheda (target: First-Timer Foreigner)
- Build canonical snippets library (where-to-stay snippets first)

**Phase 2 — Test on 1 article:**
- Pick medium-difficulty post (NOT Taormina, too important for first test)
- Run all 9 fases manually, log what breaks
- Fix what breaks before writing SOP v2.3

**Phase 3 — Write SOP_01 v2.3:**
- After MVP works on 1 article
- Document only what worked

**Phase 4 — Test on 2-3 more articles:**
- Validate SOP v2.3 holds across post types

**Phase 5 — Production:**
- Roll out to remaining rotting posts from WAP_13
