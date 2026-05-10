# PHASE 10 — Audit Mechanical

**Last updated:** May 10, 2026
**Position in workflow:** Tenth phase of SOP_01 v2.3
**Agent:** Bash script (`tools/audit_post.sh v0.8`)
**Status:** Operational since May 5, 2026.
**Pairs with:** tools/audit_post.sh, tools/audit_category_b.py, tools/audit_category_c.py, tools/audit_category_d.py

---

## Purpose

Mechanical verification of Phase 9 HTML output before final review. 39 checks across 4 categories. Last automated gate before Nico sign-off in Phase 11.

---

## Procedure

### Step 1 — Input: `09_Final.html`

### Step 2 — Run audit script

```bash
bash tools/audit_post.sh projects/POST_[article-slug]/09_Final.html
```

39 checks across 4 categories:
- **Category A (15):** Markup, schema, structure
- **Category B (15):** Prose geometry
- **Category C (5):** Affiliate verification (WAP_12 match)
- **Category D (4):** Voice safety net

### Step 3 — Process output (PASS / FAIL / WARN per check)

### Step 4 — Save log to `10_Audit_Log.txt`

### Step 5 — Decide next action
- **All PASS:** advance to Phase 11
- **Any FAIL:** loop back (Cat A/C → Phase 9, Cat B/D → Phase 8)
- **WARN only:** advance with warnings logged

---

## Checklist

The 39 checks in audit_post.sh ARE the checklist. **Pass criteria:** 0 FAIL.

---

## Workflow integration

**Input:** `09_Final.html`
**Output:** `10_Audit_Log.txt`
**Next phase:** Phase 11 — Review + Publish (only if 0 FAIL)

---

## Validation history

audit_post.sh v0.8 operational since May 5, 2026. Validated on Where-to-stay-palermo (32 PASS / 2 FAIL / 5 WARN).

---

## Changelog

- v1.0 — May 10, 2026 — Wrapper. Implementation in tools/audit_post.sh v0.8 (May 5).
