# PHASE 08 — Voice Pass

**Last updated:** May 17, 2026 (v2.4.0)
**Owner agent:** Copywriter (Cowork)
**Pairs with:** brain/voice_corpus/phase_08_translation_prompt.md (operational prompt), brain/voice_corpus/nico_canon_01-04 (gold standard references), tools/test_voice_checklist.py v2.0 (post-check geometric detector)

---

## Purpose

Translate the Phase 7 information draft (07_Draft_Info.md) into Nico Barcellona's voice. Output is 08_Draft_Voice.md in the same project folder.

This phase is a TRANSLATION operation, not a voice-engineering operation. The voice is defined by four canon reference texts hand-written by Nico. The Copywriter agent receives the canon, applies eight operational moves, follows rhythm rules, and produces a Nico-grade output.

The mechanical detector tools/test_voice_checklist.py runs at the end as a geometric post-check (em-dashes, banned phrases, paragraph length, all-caps, rhetorical questions). It validates the shell, not the soul. The soul is in the prompt.

---

## Inputs

- projects/POST_<slug>/07_Draft_Info.md (the information draft from Phase 7)
- brain/voice_corpus/phase_08_translation_prompt.md (the operational prompt)
- brain/voice_corpus/nico_canon_01_intro_san_vito.md (loaded inline in the prompt)
- brain/voice_corpus/nico_canon_02_worth_visiting.md (loaded inline in the prompt)
- brain/voice_corpus/nico_canon_03_base_or_daytrip.md (loaded inline in the prompt)
- brain/voice_corpus/nico_canon_04_getting_there.md (loaded inline in the prompt)

---

## Procedure

### Step 1 — Load operational prompt

Open brain/voice_corpus/phase_08_translation_prompt.md. Copy the entire prompt block (from "You are a copywriter" through "Now translate."). The four canon references are inlined in the prompt; no separate file loads are required.

### Step 2 — Insert Phase 7 draft into the prompt

In the prompt, locate the placeholder `[INSERT TEXT HERE]` under "THE NEUTRAL TEXT:". Replace it with the full content of 07_Draft_Info.md from the active project folder.

### Step 3 — Execute the translation

Open a fresh Cowork chat with the Copywriter agent. Paste the complete filled prompt as a single message. Do not attach any knowledge folder or external files. The prompt is self-contained.

### Step 4 — Capture output

The Copywriter agent returns the translated text directly in the chat. Save the output verbatim as projects/POST_<slug>/08_Draft_Voice.md.

### Step 5 — Run geometric post-check

Execute:

python3 tools/test_voice_checklist.py projects/POST_<slug>/08_Draft_Voice.md

Expected results on a properly translated draft:
- Em-dashes: 0 (HARD-FAIL if > 0)
- Banned phrases (stunning, embark on, don't miss, hidden gem, must-see): 0 (HARD-FAIL if > 0)
- All-caps phrases: at least 1 (verdict words)
- Rhetorical questions: at least 1 (reader engagement)
- Per-section sentence-length and compound-sentence metrics: PASS on at least 80% of H2 sections

### Step 6 — Iterate if geometric fail

If em-dashes > 0 or banned phrases > 0, re-run Step 3 with a brief instruction prepended: "The previous output contained N em-dashes and N banned phrases. Re-translate the source, ensuring zero em-dashes and zero banned phrases in the output." Then re-save and re-test.

Other geometric soft-fails (sentence length, compound sentences) typically resolve naturally with the canon-driven translation. If they persist after one re-run, the draft is still acceptable; geometric metrics validate the shell, the canon validates the soul.

### Step 7 — Final acceptance

The draft is accepted when:
- Geometric post-check PASS on em-dashes and banned phrases (HARD)
- Subjective comparison to canon: a reader who knows the canon would not feel a tone drop-off
- All facts, prices, and named entities from 07_Draft_Info.md preserved in 08_Draft_Voice.md

---

## Output

projects/POST_<slug>/08_Draft_Voice.md — voice-translated draft, ready for Phase 9 (HTML conversion).

---

## Checklist (10 items)

| # | Check | Y/N |
|---|---|---|
| 1 | The full prompt from phase_08_translation_prompt.md was loaded, including all four canon references. | |
| 2 | The Phase 7 draft 07_Draft_Info.md was inserted verbatim at the `[INSERT TEXT HERE]` placeholder. | |
| 3 | Translation executed in a fresh Cowork chat with the Copywriter agent. | |
| 4 | Output saved verbatim as 08_Draft_Voice.md in the project folder. | |
| 5 | test_voice_checklist.py executed on the output. | |
| 6 | Em-dashes in output: 0. | |
| 7 | Banned phrases (stunning, embark on, don't miss, hidden gem, must-see): 0. | |
| 8 | At least 80% of H2 sections PASS the script's per-section metrics. | |
| 9 | All facts, prices, and named entities from 07_Draft_Info.md preserved in 08_Draft_Voice.md. | |
| 10 | Subjective canon comparison: output reads consistently with nico_canon_01-04 in tone, rhythm, and density of named characters. | |

**Pass criteria:** items 1-7 and 9 are HARD. Items 8 and 10 are SOFT (recommended but not blocking).

---

## Hard-fail triggers

- Em-dashes > 0 in 08_Draft_Voice.md → re-translate
- Banned phrase ("stunning", "embark on", "don't miss", "hidden gem", "must-see") present in 08_Draft_Voice.md → re-translate
- Phase 7 facts altered (prices changed, places renamed, claims invented) → re-translate with explicit instruction to preserve facts
- Output empty or truncated → re-execute Step 3

---

## Changelog

- v2.4.0 — May 17, 2026 — Major architectural rewrite. Replaced WAP_05c trait-descriptive approach with operational translation prompt (brain/voice_corpus/phase_08_translation_prompt.md) using 4 hand-written canon references (nico_canon_01-04) and 8 operational moves. Validated on 4 test runs (Cefalù food x2, NYE Palermo, Solo Female Travel Safety). Previous v2.3.6 wrapper around test_voice_checklist.py preserved as PHASE_08_Voice_Pass_v2.3.6_backup.md. test_voice_checklist.py now serves as geometric post-check only, not as primary voice validator. Checklist reduced from 21 voice-DNA items to 10 procedural items focused on translation workflow.
- v2.3.6 — May 16, 2026 — test_voice_checklist.py upgraded to v2.0 multi-format. Script now accepts Markdown (.md) natively in addition to HTML (.html). Step 7 simplified — direct run on draft.md without HTML conversion.
- v2.3 — May 10, 2026 — Initial wrapper around WAP_05c/05d + test_voice_checklist.py.
