# PHASE 08 — Voice Pass

**Last updated:** May 17, 2026 (v2.4.1)
**Owner agent:** Copywriter (Cowork)
**Pairs with:**
- brain/voice_corpus/phase_08_translation_prompt.md (translation operational prompt)
- brain/voice_corpus/phase_08_rhythm_fix_prompt.md (rhythm-fix operational prompt)
- brain/voice_corpus/nico_canon_01-04 (gold standard references)
- tools/rhythm_detector.py v1.3 (paragraph-level rhythm validator)
- tools/rhythm_merger.py v1.0 (split-output merger)
- tools/test_voice_checklist.py v2.0 (legacy geometric post-check)

---

## Purpose

Translate the Phase 7 information draft (07_Draft_Info.md) into Nico Barcellona's voice and enforce paragraph-level rhythm. Output is 08_Draft_Voice.md.

Phase 8 is a two-step pipeline:
1. Translation pass (Cowork Copywriter agent applies canon).
2. Rhythm enforcement (deterministic detector + targeted fix-pass + automated merger).

The voice itself is defined by four canon reference texts hand-written by Nico. The rhythm is enforced mechanically by rhythm_detector.py because in-prompt self-audit on rhythm was empirically demonstrated to be unreliable on long inputs.

---

## Inputs

- projects/POST_<slug>/07_Draft_Info.md
- brain/voice_corpus/phase_08_translation_prompt.md
- brain/voice_corpus/phase_08_rhythm_fix_prompt.md
- brain/voice_corpus/nico_canon_01-04 (inlined in translation prompt)
- tools/rhythm_detector.py
- tools/rhythm_merger.py

---

## Procedure

### Step 1 — Translation pass

Open brain/voice_corpus/phase_08_translation_prompt.md. Copy the entire prompt block. Replace the [INSERT TEXT HERE] placeholder with the full content of 07_Draft_Info.md from the active project folder.

Open a fresh Cowork chat with Copywriter agent (Opus 4.7). Paste the complete filled prompt as a single message. No knowledge folder attached. No file uploads.

The agent returns the translated draft. Save it verbatim as projects/POST_<slug>/08_Draft_Voice.md.

### Step 2 — Run rhythm detector

Execute:

python3 tools/rhythm_detector.py projects/POST_<slug>/08_Draft_Voice.md

If the report shows "PASS: no rhythm violations detected", skip to Step 6.

Otherwise, save the violations as JSON:

python3 tools/rhythm_detector.py projects/POST_<slug>/08_Draft_Voice.md --json > projects/POST_<slug>/phase_08_attempts/rhythm_violations.json

### Step 3 — Build rhythm-fix prompt

Open brain/voice_corpus/phase_08_rhythm_fix_prompt.md. Copy the prompt block. For each violation in rhythm_violations.json, append a block formatted as:

### Paragraph N
<paragraph text>

where N is the violation index and the text is the violation's "text" field. Append all violation blocks under "THE PARAGRAPHS TO SPLIT".

### Step 4 — Execute rhythm-fix pass

Open a fresh Cowork chat with Copywriter agent (Opus 4.7). Paste the filled rhythm-fix prompt as a single message. No knowledge folder attached.

The agent returns split paragraphs. Save the output verbatim as projects/POST_<slug>/phase_08_attempts/rhythm_split_output.md.

### Step 5 — Merge splits into source

Execute:

python3 tools/rhythm_merger.py \
  projects/POST_<slug>/08_Draft_Voice.md \
  projects/POST_<slug>/phase_08_attempts/rhythm_violations.json \
  projects/POST_<slug>/phase_08_attempts/rhythm_split_output.md \
  projects/POST_<slug>/phase_08_attempts/08_Draft_Voice_rhythm_clean.md

Verify "Replaced: N paragraphs" matches the violation count. If any paragraphs are reported as missing or text-not-found, investigate before proceeding.

### Step 6 — Re-run detector as final check

Execute:

python3 tools/rhythm_detector.py projects/POST_<slug>/phase_08_attempts/08_Draft_Voice_rhythm_clean.md

Expected: "PASS: no rhythm violations detected."

If violations remain, return to Step 3 with the residual violations.

### Step 7 — Promote rhythm-clean to baseline

Backup the pre-rhythm draft:

cp projects/POST_<slug>/08_Draft_Voice.md projects/POST_<slug>/phase_08_attempts/08_Draft_Voice_pre_rhythm_pass.md

Promote the rhythm-clean version:

cp projects/POST_<slug>/phase_08_attempts/08_Draft_Voice_rhythm_clean.md projects/POST_<slug>/08_Draft_Voice.md

### Step 8 — Legacy geometric post-check

Execute test_voice_checklist.py as a final shell-level validator:

python3 tools/test_voice_checklist.py projects/POST_<slug>/08_Draft_Voice.md

Expected:
- Em-dashes: 0 (HARD-FAIL if > 0)
- Banned phrases (stunning, embark on, don't miss, hidden gem, must-see): 0 (HARD-FAIL if > 0)

This step validates surface-level cleanliness. The rhythm has already been validated by rhythm_detector.py.

---

## Output

projects/POST_<slug>/08_Draft_Voice.md — voice-translated, rhythm-clean draft, ready for Phase 9 (HTML conversion).

projects/POST_<slug>/phase_08_attempts/ — workspace folder containing intermediate artifacts:
- rhythm_violations.json (detector output)
- rhythm_split_output.md (rhythm-fix agent output)
- 08_Draft_Voice_pre_rhythm_pass.md (pre-merge baseline backup)
- 08_Draft_Voice_rhythm_clean.md (merged output)

---

## Checklist (12 items)

| # | Check | Y/N |
|---|---|---|
| 1 | The translation prompt from phase_08_translation_prompt.md was loaded with all four canon references. | |
| 2 | The Phase 7 draft was inserted verbatim at the [INSERT TEXT HERE] placeholder. | |
| 3 | Translation executed in a fresh Cowork chat with Copywriter agent on Opus 4.7. | |
| 4 | Translation output saved as 08_Draft_Voice.md. | |
| 5 | rhythm_detector.py executed on the translation output. | |
| 6 | If violations found: rhythm_violations.json saved, rhythm-fix prompt built, fix-pass executed in fresh Cowork chat. | |
| 7 | rhythm_merger.py executed; "Replaced: N paragraphs" matches violation count. | |
| 8 | rhythm_detector.py re-run on merged output reports zero violations. | |
| 9 | Pre-rhythm draft backed up as 08_Draft_Voice_pre_rhythm_pass.md. | |
| 10 | Rhythm-clean version promoted to 08_Draft_Voice.md. | |
| 11 | test_voice_checklist.py final post-check: em-dashes 0, banned phrases 0. | |
| 12 | All facts, prices, and named entities from 07_Draft_Info.md preserved in 08_Draft_Voice.md. | |

**Pass criteria:** items 1-5, 7-11 are HARD. Item 6 is conditional. Item 12 is verified by sampling 5-10 facts at random.

---

## Hard-fail triggers

- Em-dashes > 0 in 08_Draft_Voice.md → re-translate
- Banned phrase present in 08_Draft_Voice.md → re-translate
- rhythm_detector.py reports residual violations after merge → re-run rhythm-fix on residuals
- Phase 7 facts altered (prices, places, claims) → re-translate with explicit fact-preservation instruction
- rhythm_merger.py reports "original text not found in source" for any paragraph → investigate (source file modified between detector and merger?)

---

## Changelog

- v2.4.1 — May 17, 2026 — Added rhythm enforcement pipeline (detector + fix-pass + merger). Phase 8 is now a two-step pipeline: translation pass (agent) + rhythm enforcement (deterministic). Empirically validated on San Vito Lo Capo (5404-word article, 23 violations detected, 23 paragraphs split, zero violations after merge). Rationale: in-prompt rhythm self-audit was tested on 3 separate prompt designs (v2 standard, v2 with batching, v2 with sentence-by-sentence checklist) and consistently failed to enforce paragraph-level splitting on long inputs. Moving the rhythm enforcement outside the agent into a deterministic detector+fixer pipeline solves the problem. New assets: brain/voice_corpus/phase_08_rhythm_fix_prompt.md, tools/rhythm_detector.py v1.3, tools/rhythm_merger.py v1.0.
- v2.4.0 — May 17, 2026 — Major architectural rewrite. Replaced WAP_05c trait-descriptive approach with operational translation prompt (brain/voice_corpus/phase_08_translation_prompt.md) using 4 hand-written canon references (nico_canon_01-04) and 8 operational moves. Validated on 4 test runs (Cefalù food x2, NYE Palermo, Solo Female Travel Safety).
- v2.3.6 — May 16, 2026 — test_voice_checklist.py upgraded to v2.0 multi-format.
- v2.3 — May 10, 2026 — Initial wrapper around WAP_05c/05d + test_voice_checklist.py.
