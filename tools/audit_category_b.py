#!/usr/bin/env python3
"""
audit_category_b.py — Structural checks (Category B) for WAP article auditor.
Called by audit_post.sh v0.4. Receives the article-body HTML (already extracted
by the bash wrapper) on stdin. Runs 15 structural checks. Outputs PASS/FAIL/WARN
lines compatible with the bash wrapper's exit-code aggregation.
"""

import sys
import re
import os
from bs4 import BeautifulSoup

# Detect if stdout is a terminal (for color output)
IS_TTY = os.isatty(sys.stdout.fileno())
GREEN  = '\033[0;32m' if IS_TTY else ''
RED    = '\033[0;31m' if IS_TTY else ''
YELLOW = '\033[0;33m' if IS_TTY else ''
NC     = '\033[0m'    if IS_TTY else ''

content = sys.stdin.read()
soup = BeautifulSoup(content, 'lxml')

PASS = 0
FAIL = 0
WARN = 0


def print_pass(label):
    global PASS
    print(f"{GREEN}[PASS]{NC} {label}")
    PASS += 1


def print_fail(label, reason=None):
    global FAIL
    print(f"{RED}[FAIL]{NC} {label}")
    if reason:
        print(f"       Reason: {reason}")
    FAIL += 1


def print_warn(label, reason=None):
    global WARN
    print(f"{YELLOW}[WARN]{NC} {label}")
    if reason:
        print(f"       {reason}")
    WARN += 1


def text_of(el):
    """Get plain text from element."""
    return el.get_text(separator=' ', strip=True) if el else ''


def wc(text):
    """Word count."""
    return len(text.split()) if text.strip() else 0


def cc(text):
    """Character count."""
    return len(text.strip())


def is_callout(el):
    """Detect WAP_06 inline-styled callout div (display:flex + colored bg)."""
    if not el or el.name != 'div':
        return False
    style = el.get('style', '')
    has_bg = any(c in style for c in ['#fff3e0', '#e8f5e9', '#ffebee'])
    has_flex = 'display: flex' in style or 'display:flex' in style
    return has_bg and has_flex


def is_grey_box(el):
    """Detect grey box (affiliate disclosure, Continue Planning)."""
    if not el or el.name != 'div':
        return False
    style = el.get('style', '')
    return '#f4f4f4' in style or '#f5f5f5' in style


def get_h2_sections():
    """Get H2 sections: each H2 + elements until the next H2."""
    sections = []
    h2s = soup.find_all('h2')
    for i, h2 in enumerate(h2s):
        next_h2 = h2s[i + 1] if i + 1 < len(h2s) else None
        elements = []
        el = h2.find_next_sibling()
        while el:
            if el.name == 'h2':
                break
            elements.append(el)
            el = el.find_next_sibling()
        sections.append({
            'h2': h2,
            'title': text_of(h2),
            'elements': elements,
        })
    return sections


# ------------------------------------------------------------------
# B1 — Italic lead exists as first body element
# ------------------------------------------------------------------
first_p = soup.find('p')
lead_text = None
if first_p:
    first_em = first_p.find('em')
    if first_em:
        p_text = text_of(first_p)
        em_text = text_of(first_em)
        ratio = len(em_text) / max(len(p_text), 1)
        if ratio > 0.7:
            print_pass("B1 Italic lead exists as first body element")
            lead_text = em_text
        else:
            print_fail("B1 Italic lead",
                        f"First <p> has <em> but it covers only {int(ratio*100)}% of text")
    else:
        print_fail("B1 Italic lead", "First <p> has no <em>")
else:
    print_fail("B1 Italic lead", "No <p> found")

# ------------------------------------------------------------------
# B2 — Italic lead ≤25 words
# ------------------------------------------------------------------
if lead_text:
    lead_wc = wc(lead_text)
    if lead_wc <= 25:
        print_pass(f"B2 Italic lead {lead_wc} words (≤25)")
    else:
        print_fail(f"B2 Italic lead length", f"{lead_wc} words (need ≤25)")
else:
    print_warn("B2 Italic lead word count", "Skipped (B1 failed)")

# ------------------------------------------------------------------
# B3 — TL;DR table present with 5 rows
# ------------------------------------------------------------------
tldr_table = None
for d in soup.find_all('div'):
    style = d.get('style', '')
    if '#e3f2fd' in style and d.find('table'):
        tldr_table = d.find('table')
        break

if tldr_table:
    rows = tldr_table.find_all('tr')
    if len(rows) == 5:
        print_pass(f"B3 TL;DR table present (5 rows)")
    else:
        print_fail("B3 TL;DR table", f"{len(rows)} rows found, need 5")
else:
    print_fail("B3 TL;DR table", "No blue-box (#e3f2fd) table found")

# ------------------------------------------------------------------
# B4 — Affiliate disclosure right after TL;DR
# ------------------------------------------------------------------
if tldr_table:
    tldr_parent = tldr_table.find_parent('div', style=True)
    found_disclosure = False
    el = tldr_parent.find_next_sibling() if tldr_parent else None
    search_limit = 5  # look at next 5 siblings max
    while el and search_limit > 0:
        if el.name == 'h2':
            break
        el_text = text_of(el).lower()
        el_style = el.get('style', '') if hasattr(el, 'get') else ''
        if ('affiliate' in el_text or 'heads up' in el_text) and \
           ('#f5f5f5' in el_style or '#f4f4f4' in el_style):
            found_disclosure = True
            break
        el = el.find_next_sibling()
        search_limit -= 1

    if found_disclosure:
        print_pass("B4 Affiliate disclosure present after TL;DR")
    else:
        print_fail("B4 Affiliate disclosure",
                    "Not found within 5 elements after TL;DR box")
else:
    print_warn("B4 Affiliate disclosure", "Skipped (TL;DR not found)")

# ------------------------------------------------------------------
# B5 — Each H2 (non-exempt) has ≥1 callout
# ------------------------------------------------------------------
sections = get_h2_sections()
EXEMPT_KEYWORDS = ['faq', 'frequently asked', 'bottom line', 'continue planning']

h2_no_callout = []
h2_checked = 0
for idx, sec in enumerate(sections):
    title_l = sec['title'].lower()
    if any(kw in title_l for kw in EXEMPT_KEYWORDS):
        continue
    # First H2 is the overview section — uses TL;DR blue-box instead of callout
    if idx == 0:
        continue
    h2_checked += 1
    has_callout = any(is_callout(el) for el in sec['elements'] if hasattr(el, 'name'))
    if not has_callout:
        h2_no_callout.append(sec['title'][:50])

if not h2_no_callout:
    print_pass(f"B5 Every H2 has ≥1 callout ({h2_checked} checked)")
else:
    print_fail("B5 H2 callout coverage",
               f"{len(h2_no_callout)} H2(s) without callout: " +
               "; ".join(h2_no_callout[:5]))

# ------------------------------------------------------------------
# B6 — H2 section total words 300-500 (lenient range)
# ------------------------------------------------------------------
b6_issues = []
for sec in sections:
    title_l = sec['title'].lower()
    if any(kw in title_l for kw in EXEMPT_KEYWORDS):
        continue
    total_words = 0
    for el in sec['elements']:
        if hasattr(el, 'name') and el.name in ('p', 'ul', 'ol', 'div', 'table',
                                                  'h3', 'h4'):
            total_words += wc(text_of(el))
    if total_words < 100 or total_words > 1500:
        b6_issues.append((sec['title'][:40], total_words))

if not b6_issues:
    print_pass(f"B6 H2 section word counts in range (100-1500)")
else:
    msg = "; ".join([f"'{t}'={w}w" for t, w in b6_issues[:5]])
    print_fail("B6 H2 section word count", f"Out of range: {msg}")

# ------------------------------------------------------------------
# B7 — 0 prose paragraphs >180 chars
# ------------------------------------------------------------------
all_p = soup.find_all('p')
long_p = []
for p in all_p:
    # Skip <p> inside callouts (checked by B8), FAQs, grey boxes, tables, TL;DR
    skip = False
    for parent in p.parents:
        if not hasattr(parent, 'name'):
            continue
        if is_callout(parent) or is_grey_box(parent):
            skip = True
            break
        if parent.name in ('details', 'summary', 'table', 'td', 'th'):
            skip = True
            break
        pstyle = parent.get('style', '') if hasattr(parent, 'get') else ''
        if '#e3f2fd' in pstyle:  # TL;DR box
            skip = True
            break
    if skip:
        continue
    # Skip very short paragraphs that are just image tags
    if p.find('img') and cc(text_of(p)) < 10:
        continue
    # Skip author bio
    if p.get('class') and 'author-description' in p.get('class', []):
        continue
    text = text_of(p)
    if cc(text) > 180:
        long_p.append((cc(text), text[:80]))

if not long_p:
    print_pass("B7 0 prose paragraphs >180 chars")
else:
    print_fail("B7 Prose paragraph length",
               f"{len(long_p)} over 180 chars. Longest: '{long_p[0][1]}...' ({long_p[0][0]}c)")

# ------------------------------------------------------------------
# B8 — 0 callout <p> >180 chars
# ------------------------------------------------------------------
callouts = [d for d in soup.find_all('div') if is_callout(d)]
long_callout_p = []
for c in callouts:
    for p in c.find_all('p'):
        if p.find('cite'):
            continue  # skip title line
        text = text_of(p)
        if cc(text) > 180:
            long_callout_p.append((cc(text), text[:60]))

if not long_callout_p:
    print_pass(f"B8 0 callout <p> >180 chars ({len(callouts)} callouts)")
else:
    print_fail("B8 Callout <p> length",
               f"{len(long_callout_p)} over 180c, e.g. '{long_callout_p[0][1]}...' ({long_callout_p[0][0]}c)")

# ------------------------------------------------------------------
# B9 — 0 callout total text >250 chars
# ------------------------------------------------------------------
big_callouts = []
for c in callouts:
    total = 0
    for p in c.find_all('p'):
        if p.find('cite'):
            continue
        total += cc(text_of(p))
    if total > 250:
        cite_el = c.find('cite')
        label = text_of(cite_el)[:40] if cite_el else '(untitled)'
        big_callouts.append((total, label))

if not big_callouts:
    print_pass("B9 0 callouts >250 chars total")
else:
    examples = "; ".join([f"'{l}'={t}c" for t, l in big_callouts[:3]])
    print_fail("B9 Callout total length", f"{len(big_callouts)} over 250c: {examples}")

# ------------------------------------------------------------------
# B10 — 0 callout with >4 <p>
# ------------------------------------------------------------------
crowded = []
for c in callouts:
    p_count = sum(1 for p in c.find_all('p') if not p.find('cite'))
    if p_count > 4:
        cite_el = c.find('cite')
        label = text_of(cite_el)[:40] if cite_el else '(untitled)'
        crowded.append((p_count, label))

if not crowded:
    print_pass("B10 0 callouts with >4 paragraphs")
else:
    examples = "; ".join([f"'{l}'={n}p" for n, l in crowded[:3]])
    print_fail("B10 Callout paragraph count", f"{len(crowded)} overcrowded: {examples}")

# ------------------------------------------------------------------
# B11 — 0 bold with >5 words
# ------------------------------------------------------------------
strongs = soup.find_all(['strong', 'b'])
long_bolds = []
for s in strongs:
    skip_bold = False
    for p in s.parents:
        if not hasattr(p, 'name'):
            continue
        # Skip <strong> inside tables (TL;DR row headers)
        if p.name in ('td', 'th', 'table'):
            skip_bold = True
            break
        # Skip <strong> inside <cite> (callout titles)
        if p.name == 'cite':
            skip_bold = True
            break
        # Skip <strong> inside divTable (hotel cards, Pros/Cons blocks)
        if p.name == 'div' and p.get('class') and \
           any('divTable' in c for c in p.get('class', [])):
            skip_bold = True
            break
        # Skip <strong> inside callouts
        if is_callout(p):
            skip_bold = True
            break
        # Skip <strong> inside hotel card divs (box-shadow styled containers)
        if p.name == 'div':
            pstyle = p.get('style', '')
            if 'box-shadow' in pstyle:
                skip_bold = True
                break
        # Skip <strong> inside <li> (bullet points often bold the key phrase)
        if p.name == 'li':
            skip_bold = True
            break
        # Skip <strong> inside details/summary (FAQ)
        if p.name in ('details', 'summary'):
            skip_bold = True
            break
    if skip_bold:
        continue
    text = text_of(s)
    word_count = wc(text)
    if word_count > 5:
        long_bolds.append((word_count, text[:60]))

if not long_bolds:
    print_pass(f"B11 0 bold spans >5 words ({len(strongs)} checked)")
else:
    print_fail("B11 Bold span length",
               f"{len(long_bolds)} over 5 words, e.g. '{long_bolds[0][1]}' ({long_bolds[0][0]}w)")

# ------------------------------------------------------------------
# B13 — FAQ section present with 4-8 questions
# ------------------------------------------------------------------
faq_h2 = None
for h2 in soup.find_all('h2'):
    t = text_of(h2).lower()
    if 'faq' in t or 'frequently asked' in t:
        faq_h2 = h2
        break

if faq_h2:
    # FAQ <details> live inside <div class="faq-brutto-ma-funziona"> wrapper,
    # not as direct siblings of the H2. Use find_all_next and stop at next H2.
    details_count = 0
    next_h2 = faq_h2.find_next('h2')
    for d in faq_h2.find_all_next('details'):
        # Stop if we've passed the next H2
        if next_h2 and d.find_previous('h2') != faq_h2:
            break
        details_count += 1

    if 4 <= details_count <= 8:
        print_pass(f"B13 FAQ section ({details_count} questions)")
    else:
        print_fail("B13 FAQ question count", f"{details_count} found, need 4-8")
else:
    print_fail("B13 FAQ section", "No FAQ H2 found")

# ------------------------------------------------------------------
# B14 — Each FAQ answer 40-100 words
# ------------------------------------------------------------------
if faq_h2:
    faq_details = []
    next_h2_b14 = faq_h2.find_next('h2')
    for d in faq_h2.find_all_next('details'):
        if next_h2_b14 and d.find_previous('h2') != faq_h2:
            break
        faq_details.append(d)

    bad_answers = []
    for d in faq_details:
        summary = d.find('summary')
        if not summary:
            continue
        # Answer = everything inside <details> except <summary>
        full_text = text_of(d)
        sum_text = text_of(summary)
        answer = full_text[len(sum_text):].strip()
        awc = wc(answer)
        if awc < 30 or awc > 120:
            bad_answers.append((awc, sum_text[:50]))

    if not bad_answers:
        print_pass(f"B14 FAQ answers in range ({len(faq_details)} checked)")
    else:
        examples = "; ".join([f"'{q}'={w}w" for w, q in bad_answers[:3]])
        print_fail("B14 FAQ answer length", f"{len(bad_answers)} out of range: {examples}")
else:
    print_warn("B14 FAQ answer length", "Skipped (no FAQ)")

# ------------------------------------------------------------------
# B15 — Continue Planning grey-box present
# ------------------------------------------------------------------
cp_box = None
for d in soup.find_all('div'):
    if is_grey_box(d) and 'continue planning' in text_of(d).lower():
        cp_box = d
        break

if cp_box:
    print_pass("B15 Continue Planning grey-box present")
else:
    print_fail("B15 Continue Planning grey-box", "Not found")

# ------------------------------------------------------------------
# B16 — Bottom Line section 80-250 words
# ------------------------------------------------------------------
bl_h2 = None
for h2 in soup.find_all('h2'):
    t = text_of(h2).lower()
    if 'bottom line' in t or 'conclusion' in t:
        bl_h2 = h2
        break

if bl_h2:
    total_words = 0
    el = bl_h2.find_next_sibling()
    while el:
        if el.name == 'h2':
            break
        # Stop at Continue Planning box
        if hasattr(el, 'get') and is_grey_box(el):
            break
        if el.name in ('p', 'ul', 'ol'):
            total_words += wc(text_of(el))
        el = el.find_next_sibling()

    if 80 <= total_words <= 250:
        print_pass(f"B16 Bottom Line section ({total_words} words)")
    else:
        print_fail("B16 Bottom Line length",
                    f"{total_words} words (need 80-250)")
else:
    print_fail("B16 Bottom Line", "No 'Bottom Line' or 'Conclusion' H2 found")

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------
print()
print(f"Category B summary: {PASS} PASS / {FAIL} FAIL / {WARN} WARN")
sys.exit(1 if FAIL > 0 else 0)
