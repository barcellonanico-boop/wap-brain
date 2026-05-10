# PHASE 9 — HTML

**Last updated:** May 10, 2026
**Position in workflow:** Ninth phase of SOP_01 v2.3
**Agent:** Copywriter (assemblage role only)
**Pairs with:** brain/WAP_06c_CANONICAL_SNIPPETS.md (HTML patterns), brain/WAP_12_AFFILIATE_LINKS.md (verbatim hotel/tour URLs)

---

## Purpose

Convert Phase 8 voice-applied Markdown (`08_Draft_Voice.md`) into final HTML (`09_Final.html`) ready for WordPress paste. NO inventing HTML — the Copywriter only assembles using canonical snippets from WAP_06c.

Critical rule (Finding #77): hotel URLs MUST match WAP_12 verbatim. Inventing URLs is a HARD-FAIL BLOCKER.

---

## Procedure

### Step 1 — Inputs
- `08_Draft_Voice.md`, WAP_06c, WAP_12, `06_Structure.md`, `03_Article_Audit.md`

### Step 2 — Markdown to HTML conversion
- `# H1` → `<h1>`, `## H2` → `<h2>`, `### H3` → `<h3>`
- `*italic*` → `<em>`, `**bold**` → `<strong>`
- Lists → `<ul>/<ol>`, Links → `<a href>`

### Step 3 — WAP_06c snippet replacement
- `[HOTEL_CARD: slug]` → WAP_06c hotel card with WAP_12 VERBATIM URL
- `[GYG_CARD: id]` → WAP_06c GYG card with WAP_12 verbatim URL
- `[DC_CALLOUT]` → WAP_06c Discover Cars snippet
- `[SW_CALLOUT]` → WAP_06c Sicilian Way snippet
- TL;DR → WAP_06c TL;DR snippet
- Pros/Cons → WAP_06c Pros/Cons snippet
- FAQ → WAP_06c `<details>/<summary>` snippet

### Step 4 — FAQPage JSON-LD schema generation
- `<script type="application/ld+json">` with FAQPage schema from FAQ Q&A pairs
- Validate JSON parses correctly

### Step 5 — Internal links integration

### Step 6 — Cross-checks
- Every placeholder resolved
- All affiliate URLs match WAP_12 character-for-character
- JSON-LD valid and matches visible FAQ
- No invented inline styles or class names
- HTML validates

### Step 7 — Output `09_Final.html`

---

## Checklist (Y/N)

| # | Check | Y/N |
|---|---|---|
| 1 | All H2 from Phase 8 present in HTML | |
| 2 | TL;DR uses WAP_06c snippet | |
| 3 | Pros/Cons use WAP_06c snippet (if applicable) | |
| 4 | Hotel cards use WAP_06c snippet | |
| 5 | Hotel URLs match WAP_12 verbatim (Finding #77 BLOCKER) | |
| 6 | GYG cards use WAP_06c snippet (if applicable) | |
| 7 | GYG URLs match WAP_12 verbatim | |
| 8 | DC callout uses WAP_06c snippet (if applicable) | |
| 9 | SW callout uses WAP_06c snippet (if applicable) | |
| 10 | FAQ uses WAP_06c `<details>/<summary>` snippet | |
| 11 | FAQPage JSON-LD embedded | |
| 12 | JSON-LD parses correctly | |
| 13 | JSON-LD Q&A matches visible HTML FAQ | |
| 14 | Internal links placed per Phase 3 KEEP list | |
| 15 | NO inline `style="..."` invented | |
| 16 | NO HTML class names invented | |
| 17 | `<em>` and `<strong>` correctly converted | |
| 18 | HTML validates (no broken tags) | |
| 19 | All affiliate URLs respond 200 | |
| 20 | All internal links respond 200 | |

**Pass criteria:** 20/20 Y.

### Hard-fail triggers

- Hotel URL not matching WAP_12 verbatim → BLOCKER (Finding #77)
- HTML class invented → REGENERATE
- JSON-LD malformed → REGENERATE
- Affiliate URL non-200 → BLOCKER
- Inline CSS invented → REGENERATE

---

## Workflow integration

**Input:** `08_Draft_Voice.md` + WAP_06c + WAP_12
**Output:** `09_Final.html`
**Next phase:** Phase 10 — Audit Mechanical

---

## Changelog

- v1.0 — May 10, 2026 — Initial creation. 7-step Markdown-to-HTML using WAP_06c snippets + WAP_12 verbatim URLs + JSON-LD. 20-item checklist with HARD-FAIL on URL mismatch (Finding #77).
