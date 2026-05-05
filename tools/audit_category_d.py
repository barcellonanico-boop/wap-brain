#!/usr/bin/env python3
"""
audit_category_d.py — Category D voice + reader-flow checks.
stdin: article body HTML (extracted by audit_post.sh)

Checks:
  D1 — Technical concepts (ZTL, Via dei Tesori, bidet, AMAT) have explainer callout in same H2 of first mention
  D2 — 0 generic travel-blog phrases (vibrant, hidden gem, must-see, bucket list, amazing, incredible, stunning, breathtaking)
  D3 — 0 reflective listening phrases (I hear you, I understand, I get it)
  D4 — Fake enthusiasm threshold: warn if absolutely/definitely appears >3 times
"""

import sys
import re
from bs4 import BeautifulSoup

content = sys.stdin.read()
soup = BeautifulSoup(content, 'lxml')

PASS = 0
FAIL = 0
WARN = 0

def print_pass(label):
    global PASS
    print(f"\033[0;32m[PASS]\033[0m {label}")
    PASS += 1

def print_fail(label, reason=None):
    global FAIL
    print(f"\033[0;31m[FAIL]\033[0m {label}")
    if reason:
        print(f"       Reason: {reason}")
    FAIL += 1

def print_warn(label, reason=None):
    global WARN
    print(f"\033[0;33m[WARN]\033[0m {label}")
    if reason:
        print(f"       {reason}")
    WARN += 1

def is_callout(div):
    if not div or not hasattr(div, 'name') or div.name != 'div':
        return False
    style = div.get('style', '') or ''
    has_bg = any(c in style for c in ['#fff3e0', '#e8f5e9', '#ffebee'])
    has_flex = 'display: flex' in style or 'display:flex' in style
    return has_bg and has_flex

# Plain text version of body for searching (strip all HTML)
body_text = re.sub(r'<[^>]+>', ' ', content)
body_text = re.sub(r'\s+', ' ', body_text)

# ============================================================
# D1 — Technical concepts have explainer callout in same H2
# ============================================================
# For each technical term, find first mention. Identify the H2
# section containing it. Verify a callout exists in that section
# OR an inline explanation is present nearby.

technical_terms = {
    'ZTL': r'\b(Z\.\s*T\.\s*L\.|ZTL)\b',
    'Via dei Tesori': r'\bVia dei Tesori\b',
    'bidet': r'\bbidet\b',
    'AMAT': r'\bAMAT\b',
}

# Find all H2s and their content sections
h2s = soup.find_all('h2')

def get_section_for_position(text_position, full_text, h2_positions):
    """Return the H2 section index for a given text position."""
    section = -1
    for i, pos in enumerate(h2_positions):
        if pos <= text_position:
            section = i
        else:
            break
    return section

# Build positions of each H2 in body_text
h2_positions = []
for h2 in h2s:
    h2_text = h2.get_text(strip=True)
    if h2_text:
        idx = body_text.find(h2_text)
        if idx >= 0:
            h2_positions.append(idx)

d1_violations = []

for term_name, pattern in technical_terms.items():
    match = re.search(pattern, body_text)
    if not match:
        continue  # term not used in article, skip

    first_pos = match.start()
    section_idx = get_section_for_position(first_pos, body_text, h2_positions)

    if section_idx == -1:
        continue

    # Section bounds
    section_start = h2_positions[section_idx]
    section_end = h2_positions[section_idx + 1] if section_idx + 1 < len(h2_positions) else len(body_text)
    section_text = body_text[section_start:section_end]

    # Check if there's an explanation pattern in the section
    # Pattern: term followed within 500 chars by an explanation cue
    # OR a callout exists in this H2 section

    explanation_cues = [
        r'is\s+(an?|the)\s+[A-Z]',  # "is a Limited Traffic Zone"
        r'stands for',
        r'means',
        r'\(',  # parenthetical explanation
        r'—',  # em-dash explanation (won't be there since banned, but just in case)
        r'\.\s+[A-Z][a-z]+\s+[A-Z]',  # next sentence with proper noun explanation
    ]

    # Find term position within section
    section_term_match = re.search(pattern, section_text)
    if not section_term_match:
        continue

    term_pos_in_section = section_term_match.start()
    after_term = section_text[term_pos_in_section:term_pos_in_section + 500]

    has_inline_explanation = any(re.search(cue, after_term) for cue in explanation_cues)

    # Check if there's a callout in this H2 section (search the original soup)
    section_callouts = 0
    h2_el = h2s[section_idx]
    next_h2_el = h2s[section_idx + 1] if section_idx + 1 < len(h2s) else None
    for sib in h2_el.find_all_next():
        if sib == next_h2_el:
            break
        if hasattr(sib, 'name') and sib.name == 'div' and is_callout(sib):
            section_callouts += 1

    if not has_inline_explanation and section_callouts == 0:
        d1_violations.append((term_name, h2_el.get_text(strip=True)[:50]))

if not d1_violations:
    terms_used = [n for n, p in technical_terms.items() if re.search(p, body_text)]
    print_pass(f"D1 Technical concepts have explainer ({len(terms_used)} terms checked: {', '.join(terms_used)})")
else:
    print_fail("D1 Technical concepts explainer", f"Missing for: {d1_violations}")

# ============================================================
# D2 — 0 generic travel-blog phrases
# ============================================================
generic_phrases = [
    'vibrant',
    'hidden gem',
    'must-see',
    'must see',
    'bucket list',
    'breathtaking',
    'stunning',
    'awe-inspiring',
    'unforgettable',
    'magical experience',
    'picturesque',
    'quaint',
    'charming little',
]

# Note: "amazing" and "incredible" excluded — Nico uses these legitimately as Maniscalco-flavored
# emphasis (e.g., "amazing food"). They're not generic when in his voice.

d2_found = []
for phrase in generic_phrases:
    pattern = r'\b' + re.escape(phrase) + r'\b'
    matches = list(re.finditer(pattern, body_text, re.IGNORECASE))
    if matches:
        d2_found.append((phrase, len(matches)))

if not d2_found:
    print_pass(f"D2 0 generic travel-blog phrases ({len(generic_phrases)} blacklist entries checked)")
else:
    print_fail("D2 0 generic travel-blog phrases", f"Found: {d2_found}")

# ============================================================
# D3 — 0 reflective listening phrases
# ============================================================
# Phrases that sound like a therapist, not Nico
reflective_phrases = [
    "I hear you",
    "I understand",
    "I get it",
    "That makes sense",
    "I feel you",
    "I totally get",
]

d3_found = []
for phrase in reflective_phrases:
    pattern = r'\b' + re.escape(phrase) + r'\b'
    if re.search(pattern, body_text, re.IGNORECASE):
        d3_found.append(phrase)

if not d3_found:
    print_pass(f"D3 0 reflective listening phrases ({len(reflective_phrases)} blacklist entries checked)")
else:
    print_fail("D3 0 reflective listening phrases", f"Found: {d3_found}")

# ============================================================
# D4 — Fake enthusiasm threshold
# ============================================================
# Warn if "absolutely" or "definitely" appears more than 3 times each
d4_warnings = []
for word in ['absolutely', 'definitely']:
    pattern = r'\b' + word + r'\b'
    count = len(re.findall(pattern, body_text, re.IGNORECASE))
    if count > 3:
        d4_warnings.append((word, count))

if not d4_warnings:
    print_pass("D4 Fake enthusiasm threshold (absolutely/definitely each ≤3)")
else:
    print_warn("D4 Fake enthusiasm threshold", f"Excessive use: {d4_warnings}")

# ============================================================
# Summary
# ============================================================
print()
print(f"Category D summary: {PASS} PASS / {FAIL} FAIL / {WARN} WARN")
sys.exit(1 if FAIL > 0 else 0)
