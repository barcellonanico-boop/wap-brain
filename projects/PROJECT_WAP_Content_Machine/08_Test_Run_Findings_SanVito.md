# 08 — Test Run Findings — San Vito Lo Capo (Cowork Agent v1.0 end-to-end)

**Started:** May 12, 2026
**Test target:** /news/comprehensive-guide-visiting-san-vito-lo-capo/
**Test type:** First end-to-end run of Cowork Article Refresh Agent v1.0 on SOP_01 v2.3 (Phases 3-10 autonomous, Phase 5 with Nico Brain Dump)
**Status:** Phases 1-10 completed by agent. Phase 11 (publish) NOT reached. Output file 09_Final.html audited against SOP procedures and brain docs.
**Verdict:** WORKFLOW HARD-FAIL. Article unpublishable as-is. Procedure gaps identified.

---

## Executive summary

The Cowork agent executed all 11 phases without halting. Output 09_Final.html violates Hard-Fail triggers of Phase 6 (structure based on Brain Dump not existing article), Phase 7 (cultural adaptation), Phase 8 (voice geometry not applied), Phase 9 (hotel card images missing). Mechanical Audit Phase 10 did not catch the failures.

ROOT CAUSE: NOT procedure absence. Procedures are documented and detailed. ROOT CAUSE is enforcement absence: Cowork agent reads phase docs, produces output violating them, no automated gate stops advancement.

PRIMARY ERROR (per Nico debrief): Phase 6 Struttura structured the Brain Dump instead of refreshing the existing article. The existing article was the scaffold to preserve; the Brain Dump was enrichment. The Cowork agent inverted this. Phase 7 then executed the bad structure faithfully. Phase 8 Voice Pass did not apply the Maniscalco-style transformation per WAP_05c, only preserved Brain Dump tone. Phase 9 HTML cascaded the failures.

---

## Phase-by-phase verdict (Nico debrief May 12)

| Phase | Status | Note |
|---|---|---|
| 1 Tech Recon | PASS | GSC + Ubersuggest analysis solid |
| 2 Search Intent | PASS | Macro-topics + A→B mapping correct |
| 3 Article Audit | PASS | KEEP/UPDATE/KILL verdicts reasonable |
| 4 Persona Match | PASS with minor fix | Knowledge gaps section took template literally: returned "ZTL BD AMAT Italian neighborhood granularity" instead of actual cultural gaps an Anglo wouldn't get (e.g. "toccarsi i coglioni" superstition, "caldofreddo" gelato variety, etc). Fix in Phase 4 template. |
| 5 Brain Dump | PASS with concern | Question Set generation good. Brain Dump dictation captured. Note: some Brain Dump content (August warning in particular) may have been too strongly framed — Nico self-flagged this as a "may have been exaggerated" item for future calibration. Not procedure bug. |
| 6 Struttura | CRITICAL FAIL | Structured the Brain Dump, not the article refresh. Should have started from existing article (Phase 3 KEEP sections) as scaffold + Brain Dump as enrichment. Inverted the four-source integration model. |
| 7 Bozza Info | CASCADE FAIL | Executed the bad Phase 6 structure faithfully. Cultural adaptation HARD-FAIL: "color of my nonno's morning pee" + "children peeing in water" copied verbatim from Brain Dump for Anglo Couple persona. |
| 8 Voice Pass | FAIL | Did not apply Maniscalco-style transformation. Brain Dump tone preserved verbatim. No DNA trait amplification. WAP_05d checklist likely not run or run with insufficient enforcement. |
| 9 HTML | FAIL | Hotel cards missing required `<img>` per WAP_06c template. 9 hotel cards, 0 images, 0 placeholders. Artemide/il-vecchio-mulino URL anomaly not resolved despite Phase 5 question. No Continue Planning block. FAQ placed after Bottom Line (wrong order). |
| 10 Audit Mechanical | FAIL or SKIPPED | Either audit_post.sh ran and missed all above, or was skipped. Audit log to be inspected to determine which. |
| 11 Review + Publish | NOT REACHED | Workflow caught at Phase 10. Output unpublishable. |

---

## Root cause analysis

### Architectural finding

Cowork single-agent v1.0 has no enforcement between phases. The agent self-reports "Phase X complete" and advances. Critical-severity failures (Phase 6 structural inversion, Phase 7 cultural adaptation, Phase 8 voice geometry, Phase 9 hotel images) were all self-approved with no gate stopping advancement.

The procedures themselves are detailed and (where followed) correct. The agent reads them but does not enforce its own checklists.

### Specific procedural gaps identified

1. PHASE_04_Persona_Match.md template for "Knowledge gaps" produces generic Italian-bureaucratic acronyms (ZTL/AMAT) instead of cultural-translation gaps an Anglo reader genuinely wouldn't decode. Template guidance needs replacement with concrete examples: superstitions, food terms with no English equivalent, family-cast references, dialectal expressions, etc.

2. PHASE_06_Struttura.md does not explicitly mandate "existing article is the scaffold; Brain Dump enriches and updates; never structure the Brain Dump alone." The 4-source mapping is present but priority/scaffold-role of existing article is not enforced.

3. PHASE_07_Bozza_Info.md cultural adaptation Step 3 has examples but no enforcement mechanism. Checklist item #7 "Cultural adaptation applied" passes on a Y/N self-report. Needs evidence requirement: "list every Brain Dump item containing Italian idiom or bodily-fluid imagery, with before/after adaptation."

4. PHASE_08_Voice_Pass.md is a wrapper. The Voice Pass execution lives in WAP_05d operational checklist + test_voice_checklist.py script. If the test script PASSED on this draft, thresholds are too lax. If it didn't run, the wrapper enforcement failed.

5. PHASE_09_HTML.md checklist item #4 "Hotel cards use WAP_06c snippet" passes on a Y/N for the outer template. Does not separately check inner elements including `<img>`. Image placeholder rule from WAP_06 (Image Inference Ban) not surfaced in the checklist.

---

## Path forward (Nico decision May 12)

CHOSEN: Manual fase-by-fase re-test starting from Phase 6. Specialist agents (Architect for Phases 1-6, Copywriter for Phases 7-9). PM gates each handoff. Each phase output reviewed, calibrated, and procedure updated.

Failed-run outputs (06-10) preserved in `projects/POST_san-vito-lo-capo/failed_run_v1/` for reference.

Phase 1-5 outputs retained at canonical paths as inputs for the manual re-test.

Outcome of manual re-test: SOP_01 v2.4 with calibration fixes derived from each phase's manual execution.

NOT pursued (rejected): Path A rollback to pre-Cowork architecture (Nico verdict: not useful, "una cazzata").

---

## Appendix — Procedures referenced

- sops/SOP_01_phases/PHASE_04_Persona_Match.md
- sops/SOP_01_phases/PHASE_06_Struttura.md
- sops/SOP_01_phases/PHASE_07_Bozza_Info.md
- sops/SOP_01_phases/PHASE_08_Voice_Pass.md
- sops/SOP_01_phases/PHASE_09_HTML.md
- sops/SOP_01_phases/PHASE_10_Audit_Mechanical.md
- brain/WAP_05c_VOICE_DNA.md
- brain/WAP_05d_VOICE_CHECKLIST.md v2.0
- brain/WAP_06_CONTENT_FORMAT.md
- brain/WAP_06c_CANONICAL_SNIPPETS.md
- agents/COWORK_ARTICLE_REFRESH_AGENT.md
