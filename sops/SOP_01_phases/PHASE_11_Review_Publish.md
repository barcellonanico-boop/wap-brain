# PHASE 11 — Review + Publish

**Last updated:** May 10, 2026
**Position in workflow:** Eleventh and final phase of SOP_01 v2.3
**Agent:** Architect (technical) + Nico (sign-off)
**Pairs with:** Google Rich Results Test, GA4, WordPress block editor

---

## Purpose

Final pre-publish verification, Nico sign-off, WordPress publish, post-publish verification. The only phase besides Phase 5 Brain Dump where Nico intervenes.

---

## Procedure

### Step 1 — Pre-publish technical checks

Architect agent runs:
- Phase 10 audit_post.sh status: verify 0 FAIL
- HTML browser render: check for rendering anomalies
- All affiliate links 200: curl verify
- All internal links 200: curl verify
- Schema validation: FAQPage JSON-LD renders correctly

If any FAIL → STOP, flag Nico.

### Step 2 — Schema validation

Google Rich Results Test on FAQPage JSON-LD. Save to `11_Schema_Validation.txt`.

### Step 3 — Cowork preview snapshot

Generate preview snapshot for Nico's visual review. File: `11_Preview_Snapshot.png` (or PDF).

### Step 4 — Nico sign-off

Nico reviews and decides:
- **APPROVE:** publish proceeds
- **REJECT:** workflow loops back with feedback
- **DEFER:** article paused

If APPROVED, Nico provides: featured image, categories, tags, slug confirmation, publish timing.

### Step 5 — WordPress publish

1. Open WordPress block editor
2. Switch to "Code editor" mode
3. Paste `09_Final.html` content
4. Switch back to "Visual editor", verify rendering
5. Set featured image, categories, tags
6. Verify slug
7. Update meta title + description (Yoast)
8. Click "Update" or "Publish"

### Step 6 — Post-publish verification

- Live URL responds 200
- Schema rendered on live page
- GSC URL Inspection: request indexing
- GA4 tracking verified (real-time pageview)
- Affiliate links clickable on live page
- Featured image displays correctly
- Mobile rendering verified

### Step 7 — Generate publish report

Save `11_Publish_Report.md` with full timestamps, URLs, sign-off record.

---

## Checklist (Y/N)

| # | Check | Y/N |
|---|---|---|
| 1 | Phase 10 Audit Log: 0 FAIL | |
| 2 | HTML renders correctly in browser | |
| 3 | All affiliate links 200 pre-publish | |
| 4 | All internal links 200 pre-publish | |
| 5 | FAQPage JSON-LD validated | |
| 6 | Meta tags complete (title, description, OG) | |
| 7 | Preview snapshot generated | |
| 8 | Nico sign-off received | |
| 9 | If REJECTED: feedback captured, loop to specified phase | |
| 10 | If APPROVED: featured image provided | |
| 11 | If APPROVED: categories + tags + slug confirmed | |
| 12 | WordPress: HTML pasted | |
| 13 | WordPress: featured image set | |
| 14 | WordPress: categories + tags applied | |
| 15 | WordPress: meta title + description set | |
| 16 | Publish executed (or scheduled) | |
| 17 | Live URL responds 200 | |
| 18 | Schema rendered on live page | |
| 19 | GSC URL Inspection submitted | |
| 20 | GA4 tracking verified | |
| 21 | Affiliate clickability tested on live page | |
| 22 | Mobile rendering verified | |
| 23 | 11_Publish_Report.md generated | |

**Pass criteria:** 23/23 Y for APPROVED path.

### Hard-fail triggers

- Phase 10 FAIL → STOP
- Schema validation fails → fix Phase 9
- Nico REJECT → loop back
- Live URL non-200 → BLOCKER
- Affiliate broken on live page → BLOCKER (revenue at risk)

---

## Workflow integration

**Input:** `09_Final.html` + `10_Audit_Log.txt` + Nico sign-off
**Output:** `11_Publish_Report.md` + live article
**Next phase:** None — workflow complete.

---

## Changelog

- v1.0 — May 10, 2026 — Initial creation. 7-step procedure: pre-publish checks, schema validation, preview snapshot, Nico sign-off, WordPress publish, post-publish verification, publish report. 23-item checklist.
