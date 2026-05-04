# 02_Execution_Backlog.md — WAP Content Machine

**Last updated:** May 4, 2026

## Phase 1 — Build v2.3 MVP (current focus)

- [x] 1.1a Conceptual audit checklist v0.1 written (43 mechanical checks across A/B/C/D categories). Saved to tools/audit_checklist_v0.1.md. [PM + Nico] [Est: 60 min | Actual: 60 min — May 3 evening session]
- [x] 1.1b Implement Category A (15 checks) as `tools/audit_post.sh` v0.1. First run against /where-to-stay-palermo/ test fixture. 6 PASS / 7 FAIL. [PM + Claude Code] [Est: 3-4 hr | Actual: ~90 min — May 3 evening]
- [x] 1.1c Fix 5 bugs from v0.1 first run → v0.2. Body extraction, &amp; URL decoding, curl timeout 15s, WP system URL filter, A12 accepts 202. Score: 10 PASS / 3 FAIL / 2 WARN. [PM + Claude Code] [Actual: ~30 min — May 4 morning]
- [x] 1.1d Article-container extraction → v0.3. Isolate to entry-content div only (excludes sidebar, user comments, footer). Fixes A3 false positive on em-dash in user comment. Clean run: 13 PASS / 0 FAIL / 2 WARN. [PM + Claude Code] [Actual: ~20 min — May 4 evening]
- [x] 1.1e audit_post.sh v0.4-v0.6 — Category B (15 structural checks via BeautifulSoup). v0.4 first run 12 PASS / 3 FAIL. v0.5 thresholds revised (B11 bold 5→12 words, B14 FAQ 30-100→15-150 words). v0.6 B7 exemptions formalized (hotel cards, bold data lists). Final result on /where-to-stay-palermo/: 13/2/0. 2 FAIL legitimate (B7 prose paragraphs + B11 bold list) — Nico will fix when article is rewritten. CATEGORY B COMPLETE. [PM + Claude Code] [Est: 3-4 hr | Actual: ~75 min — May 4 evening]
- [ ] 1.1f Implement Category C (5 affiliate + facts checks). Requires WAP_12 cross-reference. [PM + Claude Code] [Est: 1-2 hr | Actual: __]
- [ ] 1.1g Implement Category D (4 reader-flow + voice checks). [PM + Claude Code] [Est: 1 hr | Actual: __]
- [ ] 1.2 Build 2-3 reader personas (general WAP, not per-article). Sources: GA4 demographics, Facebook group, Nico sensations, common reader questions. Personas: First-Timer Foreigner (US/UK/Northern Europe), Returning-Visitor (been to Italy, knows basics), Italo-American Roots-Search. Each with: age, origin, what they know, what they don't, question order, fears, wants. Output: brain/WAP_15_PERSONAS.md. [Nico + PM] [Est: 2-3 hr | Actual: __]
- [ ] 1.3 Build canonical HTML snippets library. Extract verbatim from /where-to-stay-palermo/ live HTML (just published). Snippets: TL;DR blue-box, callout 3 variants (Take/Pick/Warning), hotel card, Pros/Cons/Advice block (D15), FAQ details/summary, Continue Planning grey-box, affiliate disclosure. Output: brain/WAP_06c_CANONICAL_SNIPPETS.md. [PM] [Est: 1-2 hr | Actual: __]

## Phase 2 — Test MVP on 1 article

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
