# SOPS_INDEX.md — Master SOP Directory

**Purpose:** Single lookup table for every SOP in the WAP system.

**Used by:** Agents (especially WAP Copywriter) to find the right SOP for a given task.

**Updated:** Every time a SOP is added, removed, or its scope changes.

---

## How To Use This Index

Agents and PM scan the table below to find the SOP matching the current task. Each row tells you:
- Which SOP file to open
- What the SOP does
- When to use it
- Required inputs

If no SOP matches the task, escalate to PM/Nico. Do not invent a workflow.

---

## SOP Directory

| SOP File | Purpose | When To Use | Status |
|---|---|---|---|
| sops/SOP_01_Update_Existing_Post.md | Rewrite an existing wearepalermo.com blog post that's losing traffic. 8 steps. Brain-dump-first Pass 2. Pass 1 = SKELETON. Step 5 = Brain Dump session. Pass 2 = ASSEMBLY from brain dump verbatim. Hard 2-cycle stop. Replaces v2.1. | When a post is rotting per WAP_13 (lost clicks YoY), or has structural issues, or needs full freshness pass. NOT for minor edits. | v2.2 — Active |
| sops/SOP_02_Create_New_Post.md | Create a NEW blog post from a keyword/topic input. Different workflow from SOP_01 (no live HTML to start from). | When publishing a new post that doesn't exist yet on wearepalermo.com. | v1.x — Pending Phase 3 review |
| sops/SOP_03_Add_Story_To_Bank.md | Take a raw story dump from Nico, craft into 250-350 word bit, file into WAP_08 Story Bank with proper tags. | When Nico tells a new story (voice memo, chat, email) worth archiving. NOT for one-liners or near-duplicates. | v1.0 — Untested |

---

## When A New SOP Is Added

1. Create the SOP file in `sops/` folder using the SOP_XX_Description.md naming convention
2. Add a row to this index
3. Update brain/WAP_00_INDEX.md SOP Map section to mirror this index
4. Commit and push

---

## When A SOP Is Removed Or Replaced

1. Mark the row "DEPRECATED" in this index (don't delete the row)
2. Move the old SOP file to `sops/_archived/` if fully replaced
3. Update WAP_00_INDEX SOP Map
4. Commit and push

---

## Pending SOPs (Not Yet Created)

These are known gaps. Add when the work surfaces.

- SOP_04 — Newsletter / ConvertKit broadcast (when first newsletter is written)
- SOP_05 — Verify Affiliate Links (monthly maintenance check)
- SOP_06 — YouTube video description / SEO setup
- SOP_07 — Premium guide content update (Sicilian Way, Restaurant Guide)
- SOP_08 — Social post (Instagram, Facebook, X)

When any of these are created, follow "When A New SOP Is Added" above.

---

## Cross-Reference

This index is mirrored in brain/WAP_00_INDEX.md (SOP Map section). When this file changes, WAP_00_INDEX must be updated too.

The SOPs themselves live in `sops/` (not in `brain/`). Brain docs are reference material. SOPs are workflows.

---

## Changelog

- **v1.0** — April 27, 2026 — Initial creation. Indexed SOP_01 (v2.0), SOP_02, SOP_03. Listed pending SOPs (SOP_04 through SOP_08).
- **v1.1** — April 29, 2026 — Updated SOP_01 row to reflect v2.1 (12 steps across 3 phases). Pass 4 + Step 11 + Step 12 now in canonical pipeline.
