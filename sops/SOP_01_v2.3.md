# SOP_01 v2.3 — Article Refresh Workflow

**Version:** 2.3
**Last updated:** May 10, 2026
**Status:** Production-ready (pending agent prompt updates + San Vito end-to-end validation)
**Owner:** Nico Barcellona
**Orchestration:** Claude Cowork (autonomous), with Nico intervention only at Phase 5 Brain Dump and Phase 11 Sign-off

---

## Purpose

Standard Operating Procedure for refreshing existing articles on wearepalermo.com. Designed for ~80% autonomous execution by AI agents, preserving Nico's authentic voice through structured Voice DNA application and explicit human checkpoints only where strategically necessary.

This master document unifies the 11 individual phase documents in `sops/SOP_01_phases/`. Each phase has its own document with detailed procedure + checklist + canonical output. This master provides:
- The complete workflow flow (entry/exit per phase)
- Cross-references between phases
- Agent assignments
- Human intervention points
- File outputs by phase
- Failure handling and loop-back logic

---

## Workflow Overview

```
START
  ↓
Phase 1 — Tech Recon                     [Architect] → 01_Tech_Report.md
  ↓
Phase 2 — Search Intent Analysis         [Architect] → 02_Search_Intent.md
  ↓
Phase 3 — Article Audit + Affiliate Inv. [Scout]     → 03_Article_Audit.md
  ↓
Phase 4 — Persona Match                  [Architect] → 04_Persona_Match.md
  ↓
Phase 5 — Brain Dump + Question Set      [Architect + NICO] → 05_Brain_Dump.md
  ↓                                       (HUMAN INTERVENTION 1/2)
Phase 6 — Struttura                      [Architect] → 06_Structure.md
  ↓
Phase 7 — Bozza Informativa              [Copywriter] → 07_Draft_Info.md
  ↓
Phase 8 — Voice Pass                     [Copywriter] → 08_Draft_Voice.md
  ↓
Phase 9 — HTML                           [Copywriter] → 09_Final.html
  ↓
Phase 10 — Audit Mechanical              [audit_post.sh] → 10_Audit_Log.txt
  ↓
Phase 11 — Review + Publish              [Architect + NICO] → 11_Publish_Report.md + LIVE ARTICLE
                                          (HUMAN INTERVENTION 2/2)
END
```

**Total phases:** 11
**Autonomous phases:** 9 (Phases 1-4, 6-10)
**Human intervention phases:** 2 (Phase 5 Brain Dump, Phase 11 Sign-off)

---

## Phase Index

| # | Phase | Document | Agent | Output File | Human Input |
|---|-------|----------|-------|-------------|-------------|
| 1 | Tech Recon | [PHASE_01_Tech_Recon.md](SOP_01_phases/PHASE_01_Tech_Recon.md) | Architect | 01_Tech_Report.md | GSC CSV exports (manual download) |
| 2 | Search Intent Analysis | [PHASE_02_Search_Intent.md](SOP_01_phases/PHASE_02_Search_Intent.md) | Architect | 02_Search_Intent.md | None |
| 3 | Article Audit + Affiliate Inventory | [PHASE_03_Article_Audit.md](SOP_01_phases/PHASE_03_Article_Audit.md) | Scout | 03_Article_Audit.md | None |
| 4 | Persona Match | [PHASE_04_Persona_Match.md](SOP_01_phases/PHASE_04_Persona_Match.md) | Architect | 04_Persona_Match.md | None |
| 5 | Brain Dump + Question Set | [PHASE_05_Brain_Dump.md](SOP_01_phases/PHASE_05_Brain_Dump.md) | Architect + Nico | 05_Brain_Dump.md | **Yes — voice/text dictation via MacWhisper** |
| 6 | Struttura | [PHASE_06_Struttura.md](SOP_01_phases/PHASE_06_Struttura.md) | Architect | 06_Structure.md | None |
| 7 | Bozza Informativa | [PHASE_07_Bozza_Info.md](SOP_01_phases/PHASE_07_Bozza_Info.md) | Copywriter | 07_Draft_Info.md | None |
| 8 | Voice Pass | [PHASE_08_Voice_Pass.md](SOP_01_phases/PHASE_08_Voice_Pass.md) | Copywriter | 08_Draft_Voice.md | None |
| 9 | HTML | [PHASE_09_HTML.md](SOP_01_phases/PHASE_09_HTML.md) | Copywriter | 09_Final.html | None |
| 10 | Audit Mechanical | [PHASE_10_Audit_Mechanical.md](SOP_01_phases/PHASE_10_Audit_Mechanical.md) | Script | 10_Audit_Log.txt | None |
| 11 | Review + Publish | [PHASE_11_Review_Publish.md](SOP_01_phases/PHASE_11_Review_Publish.md) | Architect + Nico | 11_Publish_Report.md | **Yes — sign-off APPROVE/REJECT/DEFER + WordPress paste oversight** |

---

## Entry Criteria (Workflow Start)

To start the SOP_01 v2.3 workflow on an article, Nico provides:

1. **Article URL** — the live wearepalermo.com URL to refresh
2. **Topic context** — 1 sentence describing what the article covers
3. **GSC export YoY** — CSV of last 3 months vs same period previous year (manual download from GSC dashboard, no free API)
4. **GSC export QoQ** — CSV of last 3 months vs previous 3 months
5. **Project folder created** — `projects/POST_[article-slug]/` with the two CSVs in `raw/` subfolder

Cowork verifies these inputs before starting Phase 1. If any missing, workflow does not start.

---

## Exit Criteria (Workflow End)

Workflow completes when Phase 11 produces:

1. Live article on wearepalermo.com responding 200
2. FAQPage JSON-LD schema rendering correctly
3. All affiliate links clickable on live page
4. GA4 tracking confirmed working
5. `11_Publish_Report.md` saved with full audit trail

---

## Phase Transition Rules

Each phase has its own checklist (in respective PHASE_NN.md document). The workflow advances ONLY when:
- Current phase checklist passes (all items Y per that phase's pass criteria)
- No hard-fail trigger fired
- Soft warnings logged but acceptable

If hard-fail trigger fires:
- Workflow halts at that phase
- Cowork notifies Nico with specific failure details
- Resolution required before advancing

If soft warning only:
- Workflow advances
- Warning logged in phase output for awareness

---

## Failure Handling and Loop-Back

When a phase fails or is rejected, the workflow loops back according to the failure type:

| Failure at phase | Cause | Loop-back to |
|---|---|---|
| Phase 1 | Missing GSC exports | Wait for Nico (BLOCKER) |
| Phase 1 | Missing Ubersuggest data | Retry API or wait |
| Phase 2 | Empty Point A or B | Re-run Phase 2 with deeper analysis |
| Phase 3 | Article fetch failed | Verify URL with Nico |
| Phase 3 | ≥3 broken affiliates | Fix WAP_12 entries (BLOCKER) |
| Phase 4 | <40% persona match | Escalate to PM, possibly revisit Phase 2 |
| Phase 5 | Brain Dump paraphrased | Re-process Nico raw input verbatim |
| Phase 5 | Affiliate gaps not 100% addressed | Request additional Brain Dump from Nico (BLOCKER) |
| Phase 6 | <90% Phase 2 macro-topic coverage | Re-run Phase 6 with full coverage |
| Phase 7 | Cultural adaptation absent | Re-run Phase 7 with persona-aware adaptation |
| Phase 7 | HTML markup leak | Re-run Phase 7 (Markdown only) |
| Phase 8 | Em-dash or banned phrase | Re-run Phase 8 with strict checklist |
| Phase 8 | <11/12 trait coverage | Re-run Phase 7 to preserve more voice signals, then Phase 8 |
| Phase 9 | Hotel URL not matching WAP_12 (Finding #77) | Re-run Phase 9 verbatim from WAP_12 (BLOCKER) |
| Phase 9 | Malformed JSON-LD | Re-run Phase 9 schema generation |
| Phase 10 Cat A FAIL | Markup/schema issue | Loop to Phase 9 fix |
| Phase 10 Cat B FAIL | Prose geometry | Loop to Phase 8 fix |
| Phase 10 Cat C FAIL | Affiliate URL mismatch | Loop to Phase 9 fix (BLOCKER) |
| Phase 10 Cat D FAIL | Voice safety net | Loop to Phase 8 fix |
| Phase 11 | Schema validation FAIL | Loop to Phase 9 |
| Phase 11 | Nico REJECT | Loop to phase Nico specifies |
| Phase 11 | Live URL non-200 post-publish | Investigate WordPress, possibly undo |
| Phase 11 | Broken affiliate on live page | BLOCKER (revenue at risk), fix and re-publish |

---

## Agent Roles

### Architect (5 phases: 1, 2, 4, 5, 6, 11 technical portion)

Strategic phases. SEO analysis, search intent reasoning, persona verification, structure design, technical pre-publish checks, WordPress execution.

System prompt: `agents/ARCHITECT_SYSTEM_PROMPT.md` (currently v2.1, requires update to v2.3)

### Scout (1 phase: 3)

Verification phase. Article audit + affiliate inventory + link validation. Cross-references SCOUT_SYSTEM_PROMPT for fact-verification protocol.

System prompt: `agents/SCOUT_SYSTEM_PROMPT.md` (currently v1.0, requires update to v2.3)

### Copywriter (3 phases: 7, 8, 9)

Execution phases. Draft assembly with cultural adaptation, voice DNA application, HTML conversion via canonical snippets.

System prompt: `agents/COPYWRITER_SYSTEM_PROMPT.md` (currently v2.1, requires update to v2.3)

### Script (1 phase: 10)

Mechanical audit via `tools/audit_post.sh v0.8`. 39 checks across 4 categories.

### Nico (2 phases: 5, 11)

Human intervention points:
- Phase 5: dictate Brain Dump via MacWhisper (~30-45 min text input, Italian/English/mixed)
- Phase 11: visual review + sign-off APPROVE/REJECT/DEFER (~10-15 min)

---

## Cross-Phase Dependencies

Phase outputs feed into subsequent phases. The dependency map:

```
Phase 1 → Phase 2 (GSC clusters)
Phase 1 → Phase 4 (broader GSC sample for verbatim evidence)

Phase 2 → Phase 3 (macro-topics for COVERED/MISSING analysis)
Phase 2 → Phase 4 (Point A→B profile for persona alignment)
Phase 2 → Phase 5 (macro-topics for Question Set MISSING category)
Phase 2 → Phase 6 (macro-topics + reader thought flow)
Phase 2 → Phase 7 (Search Intent angle per H2)

Phase 3 → Phase 5 (UPDATE/MISSING/affiliate gaps for Question Set)
Phase 3 → Phase 6 (KEEP material + EXTRANEOUS-CONVERT macro-topics)
Phase 3 → Phase 7 (existing article scaffold)
Phase 3 → Phase 9 (KEEP internal links list)

Phase 4 → Phase 5 (persona-specific question angles)
Phase 4 → Phase 6 (H2 ordering psychology)
Phase 4 → Phase 7 (cultural adaptation rules per persona)
Phase 4 → Phase 8 (DNA traits emphasis: lands-hardest list)

Phase 5 → Phase 6 (Brain Dump material assignment per H2)
Phase 5 → Phase 7 (one of 4 sources for draft assembly)

Phase 6 → Phase 7 (blueprint with per-H2 4-source mapping)

Phase 7 → Phase 8 (draft to apply voice geometry)

Phase 8 → Phase 9 (voice-applied Markdown to convert)

Phase 9 → Phase 10 (HTML to audit)

Phase 10 → Phase 11 (audit log gate to publish)
```

---

## Cross-Brain-Doc References

The SOP draws on multiple Brain documents. These are referenced explicitly in phase documents:

- `brain/WAP_05c_VOICE_DNA.md` — Voice DNA descriptive (referenced in Phase 8)
- `brain/WAP_05d_VOICE_CHECKLIST.md` v2.0 — Voice operational checklist (Phase 8)
- `brain/WAP_06c_CANONICAL_SNIPPETS.md` — HTML snippets (Phase 9)
- `brain/WAP_12_AFFILIATE_LINKS.md` — Verbatim affiliate URLs (Phase 3, 9, 10)
- `brain/WAP_15_PERSONAS.md` — Persona definitions A/B/C (Phase 4)
- `tools/audit_post.sh` — Mechanical audit script (Phase 10)
- `tools/test_voice_checklist.py` — Voice checklist runner (Phase 8)

---

## File Output Map (per article)

When the workflow runs on an article, the following files are produced in order:

```
projects/POST_[article-slug]/
├── raw/
│   ├── gsc_yoy.csv               (Nico-provided, before Phase 1)
│   └── gsc_qoq.csv               (Nico-provided, before Phase 1)
├── 01_Tech_Report.md             (Phase 1 output)
├── 02_Search_Intent.md           (Phase 2)
├── 03_Article_Audit.md           (Phase 3)
├── 04_Persona_Match.md           (Phase 4)
├── 05a_Question_Set.md           (Phase 5 Part A — intermediate)
├── 05b_Nico_Raw.md               (Phase 5 Part B — Nico's MacWhisper dictation)
├── 05_Brain_Dump.md              (Phase 5 Part C — final consolidated)
├── 06_Structure.md               (Phase 6)
├── 07_Draft_Info.md              (Phase 7)
├── 08_Draft_Voice.md             (Phase 8)
├── 09_Final.html                 (Phase 9)
├── 10_Audit_Log.txt              (Phase 10)
├── 11_Schema_Validation.txt      (Phase 11 intermediate)
├── 11_Preview_Snapshot.png       (Phase 11 intermediate)
└── 11_Publish_Report.md          (Phase 11 final)
```

---

## Cowork Orchestration Pattern

Cowork is the orchestrator for autonomous execution. The pattern:

1. **Workflow trigger:** Nico places article in queue (provides URL + topic + GSC CSVs)
2. **Cowork verifies entry criteria** — files in expected locations
3. **Cowork executes Phase 1-4 autonomously** — each phase produces output, runs checklist, advances on PASS, halts on FAIL
4. **At Phase 5 Part A:** Cowork generates Question Set, notifies Nico with file path + estimated time
5. **Workflow pauses** until Nico delivers `05b_Nico_Raw.md` (MacWhisper dictation)
6. **Cowork resumes:** Phase 5 Parts B+C (light cleanup, organization, output)
7. **Cowork executes Phase 6-10 autonomously**
8. **At Phase 11:** Cowork generates preview snapshot, notifies Nico for sign-off
9. **Workflow pauses** until Nico decides APPROVE/REJECT/DEFER
10. **If APPROVED:** Cowork executes WordPress publish + post-publish verification
11. **If REJECTED:** Cowork loops back to specified phase with Nico's feedback
12. **If DEFERRED:** Cowork holds at Phase 11, can resume later

The notification + pause mechanism at Phase 5 and Phase 11 is what makes the SOP fit autonomous orchestration despite requiring 2 human intervention points.

---

## Performance Targets

These are aspirational targets to validate after end-to-end testing on San Vito and subsequent articles:

- **Total wall-clock time per article:** 4-8 hours from queue start to publish (most of it autonomous)
- **Nico's active time per article:** 45-60 minutes total (30-45 min Phase 5 Brain Dump + 10-15 min Phase 11 sign-off)
- **Failure rate (any hard-fail trigger):** <20% on first run, decreasing as agents calibrate
- **Voice DNA validation rate:** ≥80% H2 sections PASS WAP_05d v2.0 on first Phase 8 run

---

## Calibration and Evolution

This SOP is v2.3. Previous iterations (v1.0, v2.0, v2.1, v2.2) failed at specific points documented in:
- `projects/PROJECT_WAP_Content_Machine/07_Test_Run_Findings.md` (84+ findings from rebuild cycles May 1-9)
- `projects/PROJECT_WAP_Content_Machine/03_Parking_Lot.md`

Key v2.3 evolutions over v2.2:
- 11 phases (was 9, with proper separation of Search Intent + Persona Match + Brain Dump + Bozza Info)
- Per-phase standalone documents in `sops/SOP_01_phases/` (was monolithic)
- Voice Pass operationalized via WAP_05d v2.0 (DNA-mirror checklist, May 9)
- Brain Dump corrected as ONE source of FOUR (existing article + Brain Dump + AI knowledge + Search Intent)
- Cultural adaptation per persona explicit in Phase 7 (Italian ironies adapted, Maniscalco refs persona-specific)
- Banned phrases reduced to 10 AI-generic composite phrases (Option B, May 9 evening)

When the workflow runs on real articles and produces findings, calibration updates go into the relevant PHASE_NN.md and reference back to this master document.

---

## Status as of May 10, 2026

- All 11 phase documents written ✅
- Master document (this file) written ✅
- Voice Pass operational (WAP_05c + WAP_05d v2.0) ✅
- Audit Mechanical operational (audit_post.sh v0.8) ✅
- Agent system prompts updated to v2.3 ❌ (NEXT TASK)
- End-to-end validation on San Vito ❌ (Phase 1+2 already saved May 5, resume from Phase 3 after agent prompt updates)
- Cowork orchestration setup ❌ (after validation succeeds)

---

## Changelog

- v2.3 — May 10, 2026 — Master document created. Unifies 11 phase documents in `sops/SOP_01_phases/`. Documents complete workflow flow with entry/exit criteria, agent assignments, human intervention points, file output map, cross-phase dependencies, failure handling and loop-back logic, Cowork orchestration pattern with pause-resume mechanism at human intervention points. Status snapshot: phase docs complete, agent prompt updates and validation pending.
- v2.2 — May 8, 2026 — Pre-rebuild iteration with 9 phases (deprecated by v2.3 11-phase structure)
- v2.1 — May 5, 2026 — Initial structured iteration after Where-to-stay rebuild post-mortem
