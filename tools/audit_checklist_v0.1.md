# Audit Checklist v0.1 — WAP Article Quality Gate

**Last updated:** May 3, 2026 (evening session)
**Status:** Conceptual checklist — to be implemented as bash script `tools/audit_post.sh` in next session.

---

## Two Lists, Not One

The original idea of "one big checklist" failed because we mixed two different things:

**1. Mechanical checks (BINARY).** Bash can verify these in 1-2 lines. Yes/no. No interpretation needed. These are what the mechanical auditor runs. If any FAIL, article cannot publish.

**2. Writing rules (NON-BINARY).** Require interpretation, context, judgment. These belong in WAP_05 (voice), WAP_06 (format), WAP_06b (post-type). The writing agent applies them during writing. Nico verifies them during final read (Fase 9). NOT what the mechanical auditor runs.

This document captures both. The mechanical script will only implement Section 1.

---

## Section 1 — MECHANICAL CHECKS (Binary, scriptable)

### A — File integrity & technical (15 checks)

| # | Check | How to verify (bash) |
|---|---|---|
| A1 | File ≥ source byte count (no truncation) | `wc -c` source vs disk file, diff = 0 |
| A2 | HTML valid (all tags closed) | `tidy -e` exit code 0 |
| A3 | 0 em-dashes in body | `grep -c "—"` = 0 |
| A4 | 0 banned words (SEO, AI Overview, ranking, keywords, schema markup) | `grep -ciE "(SEO\|AI Overview\|ranking\|keywords\|schema markup)"` = 0 |
| A5 | 0 Italian-name violations | `grep -ciE "(Castellamare\|Albergaria\|Villa Igea\|Piazza Matrice\|Familia\|Daita'\|Ruggero VII)"` = 0 |
| A6 | 0 placeholders left | `grep -cE "\[NICO:\|\[VERIFY:\|TODO\|TBD"` = 0 |
| A7 | Title tag 50-60 chars | extract `<title>`, count chars, in range |
| A8 | Meta description 140-160 chars | extract `<meta name="description">`, count, in range |
| A9 | URL slug ASCII simple | regex check |
| A10 | All `<img src>` return 200 | `curl -sI` each |
| A11 | All internal links (wearepalermo.com) return 200 | `curl -sI` each |
| A12 | All affiliate links (Booking/GetYourGuide/DiscoverCars) return 200 | `curl -sI` each |
| A13 | aid=918822 in every Booking link | grep all `booking.com` URLs, verify query param |
| A14 | Article schema JSON-LD valid | extract script type=application/ld+json with @type=Article, parse JSON, check required fields |
| A15 | FAQPage schema JSON-LD valid (if FAQ section present) | extract, parse, validate |

### B — Structure (counts, scriptable, 19 checks)

| # | Check | How to verify (bash) |
|---|---|---|
| B1 | Italic lead exists as first body element | first `<em>` or `<p><em>` immediately after H1, yes/no |
| B2 | Italic lead ≤25 words | `wc -w` on that em content |
| B3 | Featured image present right after lead | next sibling element after lead is `<img>` |
| B4 | Total word count in post-type range | `wc -w` body, compare to WAP_06 table per post type |
| B5 | Each H2 has image immediately after | iterate H2s, verify next non-text element is `<img>` |
| B6 | Each H2 (except FAQ + Conclusion) has closing callout | iterate H2 sections, check last styled div before next H2 is callout pattern |
| B7 | H2 sections 300-400 words | wc per H2 section, flag outside range |
| B8 | H3 sub-sections ≥80 words OR flagged for merge | wc per H3, flag <50 |
| B9 | 0 paragraphs >180 chars | awk on each `<p>` content |
| B10 | 0 callout `<p>` >180 chars | awk on `<p>` inside callout div |
| B11 | 0 callout total text >250 chars | sum chars across all `<p>` inside callout div |
| B12 | 0 callout with >4 `<p>` | count `<p>` per callout div |
| B13 | TL;DR table present with 5 rows | grep tldr-box pattern, count `<tr>` |
| B14 | Affiliate disclosure present right after TL;DR | grep grey-box pattern, position check |
| B15 | FAQ section present with 4-6 questions | count `<details>` inside `faq-brutto-ma-funziona` |
| B16 | Each FAQ answer 40-75 words | wc on each `<details>` content |
| B17 | Continue Planning grey-box present before signature | grep pattern |
| B18 | Conclusion section 100-180 words | wc on last section before signature |
| B19 | 0 `<strong>` with >5 words (revised from 4 to 5, May 4 2026) | extract strong content, wc each, flag >5 |

### C — Affiliate + facts (scriptable subset, 5 checks)

| # | Check | How to verify (bash) |
|---|---|---|
| C1 | Every hotel URL = WAP_12 verbatim | extract booking.com URLs, diff against WAP_12 |
| C2 | Affiliate opportunity check completed (Phase 1 question answered) | manual gate, not bash. Auditor checks deliverable file exists |
| C3 | Old article images recovered (if rewrite) | check 00_Live_HTML.md exists for project |
| C4 | 0 named restaurants in content | grep blacklist of WAP-tracked restaurant names from WAP_06 |
| C5 | Scout corrections applied | manual gate, auditor checks 04_Scout_Verification.md UPDATE items present in final |

### D — Reader-flow + voice (scriptable subset, 4 checks)

| # | Check | How to verify (bash) |
|---|---|---|
| D1 | Technical concepts have explainer callout within same H2 of first mention | grep technical terms (ZTL, Via dei Tesori, bidet, AMAT, etc. from a known list), verify callout exists in same H2 block |
| D2 | 0 generic travel-blog phrases | `grep -ciE "(vibrant\|hidden gem\|must-see\|bucket list\|amazing\|incredible\|stunning\|breathtaking)"` = 0 |
| D3 | 0 reflective listening phrases | `grep -ciE "(I hear you\|I understand\|I get it)"` = 0 |
| D4 | 0 fake enthusiasm | `grep -ciE "(absolutely\|definitely)"` = warn if >3 (allow some, flag overuse) |

**Total mechanical checks: 43.**

If ANY mechanical check FAILS → article CANNOT publish. Returns to relevant phase ONCE. If FAIL again → escalate to Nico.

---

## Section 2 — WRITING RULES (Non-binary, applied during writing)

These rules require interpretation. They cannot be fully verified by bash. The writing agent applies them. Nico verifies during final read.

### Voice (WAP_05)
- Author Intro follows 8-step architecture
- Tone alternation rhythm (long sentence, short, long, very short pattern)
- Mode A vs Mode B selection appropriate to context
- 21 signature moves used appropriately
- Italic vocal stress vs bold topics applied correctly
- 0 em-dashes (THIS IS BINARY — also in mechanical A3)
- 0 boring paragraphs (subjective)
- 0 lazy swearing (subjective)

### Format (WAP_06)
- 540-Word Rule: complete answer to main question in first 540 words
- Section Architecture: H2 → image → prose → callout
- Bold helps skimmers (subjective: bold makes sense if read alone)
- Walls of text avoided (mostly mechanical via B7-B12)
- Featured image alt text descriptive with keyword (subjective)

### Reader-flow (WAP_15 — TBD)
- H2 order matches persona's question order
- Cold Reader Check 11 points addressed for each area (where-to-stay specific)
- Section ordering: Areas before Pricing before Apartment/Hotel/Villa (where-to-stay specific)
- Persona match: implicit reader matches WAP_15 scheda

### Affiliate (WAP_06 + WAP_03)
- Affiliate links inserted naturally, not forced
- Old article affiliates preserved + new ones added
- 0 specific restaurants by name (BINARY — also in mechanical C4)
- Star ratings only on Giata-classified hotels

### Post-type specific (WAP_06b)
- Where-to-stay: Pros/Cons/Advice block per area
- Where-to-stay: Hotel cards canonical pattern
- Where-to-stay: Centro Storico = 1 area, not 4 sub-neighborhoods
- Other post types: rules TBD as we encounter them

---

## Implementation Plan

Phase 1 (next session):
- Implement Section 1 (43 mechanical checks) as `tools/audit_post.sh`
- Test against `/where-to-stay-palermo/` published article
- Iterate until script gives correct PASS for that article

Phase 2 (later):
- Find ways to make Section 2 rules more mechanical where possible
- Some will move to Section 1
- Others stay subjective and rely on Nico's final read

Phase 3 (production):
- Run audit_post.sh in v2.3 workflow Fase 8
- If PASS → Fase 9 Nico review + publish
- If FAIL → return to relevant fase ONCE, then escalate
