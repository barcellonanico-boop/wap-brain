# PHASE 8 — Voice Pass

**Last updated:** May 17, 2026 (v2.3.6)
**Position in workflow:** Eighth phase of SOP_01 v2.3
**Agent:** Copywriter
**Status:** Implementation complete. Voice DNA + checklist validated on Nico corpus (3/3 PASS).
**Pairs with:** brain/WAP_05c_VOICE_DNA.md (descriptive DNA), brain/WAP_05d_VOICE_CHECKLIST.md (operational checklist v2.0), tools/test_voice_checklist.py v2.0 (multi-format: Markdown + HTML)

---

## Purpose

Take Phase 7 Bozza Informativa Markdown draft and apply voice geometry + DNA trait amplification. Output is `08_Draft_Voice.md`. This phase has TWO existing artifacts that ARE the operational documentation:
- **WAP_05c_VOICE_DNA.md** — descriptive: 11 traits, family cast, lexical profile, transformation examples, failure modes
- **WAP_05d_VOICE_CHECKLIST.md v2.0** — operational: 21 detectors, banned phrases (10 AI-generic composite phrases HARD-FAIL), em-dash HARD-FAIL, scare-quote exemption

This PHASE_08 document is a wrapper that points to the canonical sources.

---

## Procedure

### Step 1 — Inputs
- `07_Draft_Info.md`, `04_Persona_Match.md`, WAP_05c, WAP_05d

### Step 2 — DNA trait amplification per persona (Phase 4 lands-hardest list)

### Step 3 — Voice geometry (WAP_05d sections 1A-1D)

### Step 4 — Banned phrases enforcement (10 composite phrases, Option B)

### Step 5 — Trait verbatim evidence (11/12 traits minimum)

### Step 6 — Failure mode detection (6 modes per WAP_05d)

### Step 7 — Run `python3 tools/test_voice_checklist.py <draft>` on draft (.md or .html accepted)

### Step 8 — Iterate if FAIL

### Step 9 — Output `08_Draft_Voice.md`

See WAP_05d_VOICE_CHECKLIST.md for full operational details on each step.

---

## Checklist

The operational checklist IS `WAP_05d_VOICE_CHECKLIST.md v2.0`. Mechanical run: `python3 tools/test_voice_checklist.py [draft.md]`

**Pass criteria:** ≥80% H2 sections PASS, 0 banned composite phrases, 0 em-dashes, ≥11/12 traits with verbatim evidence, 0 failure modes.

---

## Validation history

Validated May 9, 2026: where-to-stay 9/9 PASS, tourist-information 21/22 PASS, favignana 16/17 PASS. Non-Nico stress test FAILS clearly.

---

## Workflow integration

**Input:** `07_Draft_Info.md` + `04_Persona_Match.md` + WAP_05c + WAP_05d
**Output:** `08_Draft_Voice.md`
**Next phase:** Phase 9 — HTML

---

## Changelog

- v2.3.6 — May 17, 2026 — tools/test_voice_checklist.py upgraded from v1.1 (HTML-only) to v2.0 (multi-format). Markdown path added: `##` → H2 splits, `**` → `<strong>`, `*` → `<em>`, blank lines → `<p>`, list items → `<ul><li>`. Affiliate placeholders and table rows stripped before analysis. Extension auto-detection: `.md` → Markdown path, any other extension → existing HTML path. Step 7 updated to note both formats accepted. All 21 detectors, FAQ exemption, banned phrases, em-dash HARD-FAIL unchanged. Backup of v1.1 preserved at tools/test_voice_checklist_v1.1_backup.py.
- v1.0 — May 10, 2026 — Wrapper. Implementation in WAP_05c (May 6) + WAP_05d v2.0 (May 9) + test_voice_checklist.py.
