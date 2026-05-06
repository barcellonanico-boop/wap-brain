# 02_Execution_Backlog.md — WAP Content Machine

**Last updated:** May 4, 2026

## Phase 1 — Build v2.3 MVP (current focus)

- [x] 1.1a Conceptual audit checklist v0.1 written (43 mechanical checks across A/B/C/D categories). Saved to tools/audit_checklist_v0.1.md. [PM + Nico] [Est: 60 min | Actual: 60 min — May 3 evening session]
- [x] 1.1b Implement Category A (15 checks) as `tools/audit_post.sh` v0.1. First run against /where-to-stay-palermo/ test fixture. 6 PASS / 7 FAIL. [PM + Claude Code] [Est: 3-4 hr | Actual: ~90 min — May 3 evening]
- [x] 1.1c Fix 5 bugs from v0.1 first run → v0.2. Body extraction, &amp; URL decoding, curl timeout 15s, WP system URL filter, A12 accepts 202. Score: 10 PASS / 3 FAIL / 2 WARN. [PM + Claude Code] [Actual: ~30 min — May 4 morning]
- [x] 1.1d Article-container extraction → v0.3. Isolate to entry-content div only (excludes sidebar, user comments, footer). Fixes A3 false positive on em-dash in user comment. Clean run: 13 PASS / 0 FAIL / 2 WARN. [PM + Claude Code] [Actual: ~20 min — May 4 evening]
- [x] 1.1e audit_post.sh v0.4-v0.6 — Category B (15 structural checks via BeautifulSoup). v0.4 first run 12 PASS / 3 FAIL. v0.5 thresholds revised (B11 bold 5→12 words, B14 FAQ 30-100→15-150 words). v0.6 B7 exemptions formalized (hotel cards, bold data lists). Final result on /where-to-stay-palermo/: 13/2/0. 2 FAIL legitimate (B7 prose paragraphs + B11 bold list) — Nico will fix when article is rewritten. CATEGORY B COMPLETE. [PM + Claude Code] [Est: 3-4 hr | Actual: ~75 min — May 4 evening]
- [x] 1.1f audit_post.sh v0.7 — Category C (5 affiliate + facts checks via tools/audit_category_c.py). C1 hotel URL = WAP_12 verbatim diff. C2 Affiliate Opportunity Check (manual gate). C3 00_Live_HTML.md exists (manual gate). C4 0 named restaurants from WAP_09 blacklist (43 entries). C5 Scout file exists (manual gate). First run flagged 4 missing hotels in WAP_12 (Villa Igiea + 3 Cefalù), added with full descriptions extracted from /where-to-stay-palermo/ HTML. After fix: C1 PASS. [Architect + PM] [Est: 45 min | Actual: ~30 min] (May 5)
- [x] 1.1g audit_post.sh v0.8 — Category D (4 voice + reader-flow checks via tools/audit_category_d.py). D1 technical concept explainers (ZTL, Via dei Tesori, bidet, AMAT) in same H2 as first mention. D2 0 generic travel-blog phrases (13-entry blacklist: vibrant, hidden gem, must-see, bucket list, breathtaking, stunning, etc). D3 0 reflective listening phrases (6-entry blacklist: I hear you, I understand, etc). D4 fake enthusiasm threshold (absolutely/definitely each ≤3, warn). All 4 PASS on /where-to-stay-palermo/. AUDIT SCRIPT 100% COMPLETE: A(15)+B(15)+C(5)+D(4) = 39 checks. [Architect + PM] [Est: 30 min | Actual: ~20 min] (May 5)

**MILESTONE: Audit script complete (May 5, 2026). 39 mechanical checks across 4 categories. Final result on /where-to-stay-palermo/: 32 PASS / 2 FAIL / 5 WARN. The 2 FAIL are legitimate (B7 prose, B11 bold) preserved for next article rewrite. WARNs are manual-gate skips (test fixture not in project folder).**

Phase 1 MVP remaining tasks:
- [x] 1.2 WAP_15_PERSONAS.md — DONE May 5 evening. 3 personas locked: A Anglo Couple Planner, B Italo-American Heritage Seeker 50+, C Returning Italy Traveler. Each persona has full schede (demographics, psychographics, search/buying behavior, voice match, knowledge gaps, channel, revenue %, top article mapping). Comparison table + Fase 2 workflow integration. Source: 9-dataset analysis + Ubersuggest top 30 organic pages. [PM + Nico] [Est: 2-3 hr | Actual: ~75 min]
- [x] 1.3 WAP_06c_CANONICAL_SNIPPETS.md — DONE. 7 verbatim HTML patterns extracted from /where-to-stay-palermo/ live HTML: TL;DR blue-box, affiliate disclosure, 3 callout variants (Pick/Take/Warning), hotel card, Pros/Cons/Advice block, FAQ details+JSON-LD, Continue Planning grey-box. WAP_06 affiliate disclosure CSS synced (0.75em→0.85em). WAP_00_INDEX updated. [PM + Claude Code] [Est: 1-2 hr | Actual: ~40 min] (May 5)

## Phase 2 — Fix procedure gaps BEFORE further article tests (May 6 refocus)

- [ ] 2.0a Build Voice Pass standalone documentation — qualitative voice checklist beyond Categoria D mechanical checks. Codify bestemmie, italianità, Maniscalco-mode, anti-vlogger framing, insider voice, brutal honesty calibration. Define Phase 6 input → steps → output. Canonical voice-fail vs voice-win examples. NOT another article test before this is done. [Copywriter + Nico] [Est: 2-3 hr | Actual: __]
- [ ] 2.0b Audit accumulated findings (07_Test_Run_Findings #1-84 + Parking Lot #1-4) and group by SOP_01 v2.3 phase — output: master gap list per phase (Phase 1, 2, 3, 4, 5, 7, 8, 9). Voice Pass already covered in 2.0a. [PM + Nico] [Est: 60-90 min | Actual: __]
- [ ] 2.0c Write SOP_01 v2.3 operational document covering all 9 phases with inputs / steps / outputs / checks. Based on 2.0a (Voice Pass) + 2.0b (other phase gaps). [PM + Nico] [Est: 3-4 hr | Actual: __]
- [ ] 2.0d Update agent system prompts (Architect + Copywriter + Scout) for v2.3 roles. [PM + Nico] [Est: 60-90 min | Actual: __]
- [ ] 2.0e Re-validate full SOP_01 v2.3 on San Vito Lo Capo (resume from Phase 3 Brain Dump using preserved Tech Report + Persona Match in projects/POST_san-vito-lo-capo/). [Nico + agents] [Est: 4-6 hr | Actual: __]

## Phase 2 — Test MVP on 1 article (AFTER procedure gaps fixed)

- [ ] 2.1 Pick test article from WAP_13 P1/P2 list. Criteria: medium difficulty, not flagship, can absorb hand-finishing if needed. Candidates: /palermo-street-food/, /best-beaches-near-palermo/, /palermo-airport-transfers/. [Nico] [Est: 5 min | Actual: __]
- [ ] 2.2 Run Fase 1 (Tech recon) manually with current Architect tools. Validate: GSC story + SERP top 5 real-time + Scout parallel. Save: 01_Tech_Report.md. [Architect + PM] [Est: 30 min | Actual: __]
- [ ] 2.3 Run Fase 2 (Persona match). Pull persona scheda from WAP_15. Customize for this article. Save: 02_Persona.md. [PM] [Est: 20 min | Actual: __]
- [ ] 2.4 Run Fase 3 (Brain dump). Nico raw dump given the 2 reports above. Save: 03_Brain_Dump.md. [Nico + PM] [Est: 30-45 min | Actual: __]
- [ ] 2.5 Run Fase 4 (Structure). Agent autonomous. Output: H2/H3 ossatura with placeholder markers for callouts/Pros/Cons/FAQ. Cite brain dump where stories go. Save: 04_Struttura.md. [Agent autonomous + PM gate] [Est: 30 min | Actual: __]
- [ ] 2.6 Run Fase 5 (First draft). Agent autonomous. Fills sections from brain dump + old article (non-obsolete parts). No tone of voice yet. Markdown only. Save: 05_Bozza.md. [Agent autonomous] [Est: 45 min | Actual: __]
- [ ] 2.7 Run Fase 6 (Tone of voice). Agent autonomous. Rewrites with Nico voice. Pulls from Story Bank + Experience bank. Sets geometry (no walls, paragraph length, callout limits). Markdown still. Save: 06_Voice.md. [Agent autonomous] [Est: 45 min | Actual: __]
- [ ] 2.8 Run Fase 7 (HTML conversion). Agent autonomous. Converts 06 to HTML using WAP_06c snippets verbatim. No new decisions. Save: 07_Article.html. [Agent autonomous] [Est: 30 min | Actual: __]
- [ ] 2.9 Run Fase 8 (Mechanical auditor). Run audit_post.sh on 07. Output PASS or FAIL list. If FAIL: return to relevant fase ONCE. If FAIL again: escalate to Nico. [Auditor script] [Est: 5 min | Actual: __]
- [ ] 2.10 Run Fase 9 (Nico final review + publish). One read. Publish via WordPress UI. [Nico] [Est: 30-45 min | Actual: __]
- [ ] 2.11 Post-test debrief. What broke. What worked. What to fix in audit checklist or workflow. Document findings. [PM + Nico] [Est: 30 min | Actual: __]

## Phase 3 — Write SOP_01 v2.3 (after MVP works)

- [ ] 3.1 Write SOP_01 v2.3 based on what worked in Phase 2. 9 fasi documented with clear inputs/outputs. Replace v2.2.
- [ ] 3.2 Update agent system prompts (PM, Architect, Copywriter, Scout) for v2.3 roles.
- [ ] 3.3 Update WAP_00_INDEX.md and SOPS_INDEX.md.

## Phase 4 — Validate v2.3 on 2-3 more articles

- [ ] 4.1 Test article 2 (different post type than article 1).
- [ ] 4.2 Test article 3 (different post type again).
- [ ] 4.3 Refine v2.3 based on test results.

## Phase 5 — Production rollout

- [ ] 5.1 Run v2.3 on remaining P1 posts from WAP_13.

## Parking (deferred — see 03_Parking_Lot.md)

Items deferred until v2.3 is stable:
- Findings #56-76 patches (most landed in v2.2; remaining go in v2.3)
- Findings #77-84 patches (May 2 Pass 3 disaster — most landed in WAP_06 patches May 3)
- SOP_02 v2.3-aligned redesign
- Newsletter / YouTube / Social workflows
- Scout Perplexity Sonar upgrade
- Firecrawl integration
