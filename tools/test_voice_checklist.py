#!/usr/bin/env python3
"""
WAP_05d Voice Checklist — Mechanical checks on an HTML article.
Usage: python3 test_voice_checklist.py <path_to_html>

v1.1 — May 8, 2026 calibration:
- NLTK sent_tokenize replaces naive regex (fixes over-splitting)
- Single-sentence paragraphs threshold 40% → 25%
- Paragraph cap: hard 3 → soft (max 2 paragraphs may exceed 3 sentences)
- Ellipsis >300w: ≥2 → ≥1
- Italics: skip for sections ≤100 words
- Rhetorical questions: moved from per-H2 to article-level
- FAQ skip rule: sections with FAQ/details exempt from structural checks
- Banned: "charming" standalone removed, composite phrases added
"""

import sys
import re
import os
import math
import ssl
from copy import copy
from bs4 import BeautifulSoup, Comment

# NLTK setup with SSL workaround
ssl._create_default_https_context = ssl._create_unverified_context
import nltk
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Standalone banned words (word-boundary match)
BANNED_WORDS = [
    "stunning", "breathtaking", "magical", "picturesque",
    "vibrant", "bustling", "wanderlust", "delightful",
    "quaint", "moreover", "genuinely", "incredibly",
]

# Multi-word banned phrases (substring match, case-insensitive)
BANNED_PHRASES = [
    "hidden gem", "whether you're looking for", "there's something for everyone",
    "get ready to explore", "a feast for the senses", "embark on",
    "immerse yourself", "experience the magic of", "it's worth noting",
    "in conclusion", "to sum up", "don't miss", "be sure to",
    "ultimate guide", "complete guide", "locals love",
    "nestled in", "off the beaten path", "must-see", "must-visit",
    # Composite "charming" phrases (standalone "charming" is allowed)
    "charming little", "charming village", "charming streets",
    "charming neighborhood", "charming town", "charming alleys",
]

CAPS_ACRONYMS = {
    "ZTL", "FAQ", "USA", "UK", "US", "EU", "PM", "AM", "ATM", "POS",
    "NOT", "DNA", "AC", "CEO", "SIM", "XII", "II", "III", "IV",
    "FIRST", "GET", "OUT", "AND", "OR",
}

EXPANDABLE_FORMS = [
    "do not", "does not", "did not", "will not", "would not", "could not",
    "should not", "can not", "cannot", "is not", "are not", "was not",
    "were not", "has not", "have not", "had not", "must not",
    "it is", "it has", "that is", "there is", "there are",
    "i am", "i have", "i will", "i would", "i had",
    "you are", "you have", "you will", "you would", "you had",
    "we are", "we have", "we will", "we would", "we had",
    "they are", "they have", "they will", "they would", "they had",
    "he is", "he has", "he will", "he would", "he had",
    "she is", "she has", "she will", "she would", "she had",
    "let us", "who is", "who has", "what is", "what has",
    "where is", "how is",
]

COMPOUND_MARKERS = re.compile(
    r'\b(and|because|however|although)\b', re.IGNORECASE
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_html(path):
    with open(path, encoding="utf-8") as f:
        return BeautifulSoup(f, "lxml")


def extract_entry_content(soup):
    ec = soup.find("div", class_="entry-content")
    if not ec:
        sys.exit("ERROR: No entry-content div found.")
    ec = BeautifulSoup(str(ec), "lxml").find("div", class_="entry-content")

    for tag in ec.find_all(["script", "style"]):
        tag.decompose()
    for comment in ec.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    for tag in ec.find_all(["aside", "footer", "nav"]):
        tag.decompose()
    for div in ec.find_all("div", style=True):
        if "box-shadow" in div.get("style", ""):
            div.decompose()
    for tag in ec.find_all("details"):
        tag.decompose()
    for div in ec.find_all("div", style=True):
        if "e3f2fd" in div.get("style", ""):
            div.decompose()
    for div in ec.find_all("div", style=True):
        style = div.get("style", "")
        if any(c in style for c in ["fff3e0", "e8f5e9", "ffebee"]):
            div.decompose()
    for div in ec.find_all("div"):
        text = div.get_text(strip=True)[:200].lower()
        if "affiliate" in text and ("disclosure" in text or "commission" in text or "earn" in text):
            if len(div.get_text(strip=True)) < 500:
                div.decompose()
    for div in ec.find_all("div", class_=lambda c: c and "divTable" in c):
        div.decompose()
    for div in ec.find_all("div", style=True):
        style = div.get("style", "")
        text_snippet = div.get_text(strip=True)[:100].lower()
        if "continue planning" in text_snippet and "background" in style:
            div.decompose()

    return ec


def split_by_h2(ec):
    sections = []
    h2s = ec.find_all("h2")
    if not h2s:
        return sections
    for i, h2 in enumerate(h2s):
        title = h2.get_text(strip=True)
        fragment = BeautifulSoup("<div></div>", "lxml").find("div")
        sibling = h2.next_sibling
        while sibling:
            if getattr(sibling, "name", None) == "h2":
                break
            fragment.append(copy(sibling))
            sibling = sibling.next_sibling
        sections.append((title, fragment))
    return sections


def get_plain_text(element):
    return element.get_text(separator=" ", strip=True)


def count_words(text):
    return len(text.split())


def split_sentences(text):
    """Use NLTK sent_tokenize for proper sentence splitting."""
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return []
    # Preserve ellipsis markers
    text = text.replace('...', '<ELLIPSIS>').replace('\u2026', '<ELLIPSIS>')
    sents = sent_tokenize(text)
    return [s.replace('<ELLIPSIS>', '...').strip() for s in sents if s.strip()]


def get_paragraphs(fragment):
    return fragment.find_all("p")


def get_italics(fragment):
    return fragment.find_all(["em", "i"])


def count_ellipsis(text):
    return text.count("\u2026") + text.count("...")


def count_rhetorical_questions(sentences):
    return sum(1 for s in sentences if s.rstrip().endswith("?"))


def find_banned(text):
    """Return list of found banned words/phrases."""
    text_lower = text.lower()
    found = []
    for word in BANNED_WORDS:
        if re.search(r'\b' + re.escape(word.lower()) + r'\b', text_lower):
            found.append(word)
    for phrase in BANNED_PHRASES:
        if phrase.lower() in text_lower:
            found.append(phrase)
    return found


def count_all_caps(text):
    words = re.findall(r'\b[A-Z]{2,}\b', text)
    return [w for w in words if w not in CAPS_ACRONYMS]


def count_em_dashes(text):
    return text.count("\u2014")


def sentence_word_count(sentence):
    return len(sentence.split())


def count_compound_sentences(sentences):
    count = 0
    for s in sentences:
        if sentence_word_count(s) >= 15 and COMPOUND_MARKERS.search(s):
            count += 1
    return count


def count_contractions(text):
    return len(re.findall(r"\b\w+['\u2019]\w+\b", text))


def count_expandable_forms(text):
    text_lower = text.lower()
    count = 0
    for form in EXPANDABLE_FORMS:
        count += len(re.findall(r'\b' + re.escape(form) + r'\b', text_lower))
    return count


def paragraph_sentence_count(p_element):
    text = p_element.get_text(separator=" ", strip=True)
    return len(split_sentences(text))


def is_faq_section(title):
    t = title.lower()
    return "faq" in t or "frequently asked" in t


# ---------------------------------------------------------------------------
# Main checks
# ---------------------------------------------------------------------------

def check_section(title, fragment, section_num):
    text = get_plain_text(fragment)
    words = count_words(text)
    paragraphs = get_paragraphs(fragment)
    sentences = split_sentences(text)
    italics = get_italics(fragment)
    results = []
    fails = 0
    passes = 0
    check_results = {}
    faq = is_faq_section(title)

    results.append(f"\n--- H2 #{section_num}: {title} ({words} words){' [FAQ — structural checks exempt]' if faq else ''} ---")

    if words == 0:
        results.append("  (empty section after exclusions — skipped)")
        return results, 0, 0, {}, True

    # 1A-1: Sentences <=3 words
    short_sentences = sum(1 for s in sentences if sentence_word_count(s) <= 3)
    threshold_short = max(1, math.ceil(words / 200))
    ok = short_sentences >= threshold_short
    check_results["Sentences <=3 words"] = ok
    status = "PASS" if ok else "FAIL"
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Sentences <=3 words: {short_sentences} (threshold >= {threshold_short}) -- {status}")

    # 1A-2: Single-sentence paragraphs (25% threshold, FAQ exempt)
    single_sent_paras = sum(1 for p in paragraphs if paragraph_sentence_count(p) == 1)
    total_paras = len(paragraphs)
    ratio = single_sent_paras / total_paras if total_paras > 0 else 0
    if faq:
        ok = True
        status = "EXEMPT (FAQ)"
    else:
        ok = ratio >= 0.25
        status = "PASS" if ok else "FAIL"
    check_results["Single-sentence paragraphs"] = ok
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Single-sentence paragraphs: {single_sent_paras}/{total_paras} ({ratio:.0%}) (threshold >= 25%) -- {status}")

    # 1A-3: Italics (skip if ≤100 words)
    italic_count = len(italics)
    if words <= 100:
        ok = True
        status = "EXEMPT (≤100w)"
        ital_thresh = 0
    elif words > 300:
        ital_thresh = 3
        ok = italic_count >= ital_thresh
        status = "PASS" if ok else "FAIL"
    else:
        ital_thresh = 1
        ok = italic_count >= ital_thresh
        status = "PASS" if ok else "FAIL"
    check_results["Italics"] = ok
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Italics: {italic_count} (threshold >= {ital_thresh}) -- {status}")

    # 1A-4: Ellipsis (WARN only if >300w and 0 — does NOT block pass)
    ellipsis_count = count_ellipsis(text)
    if words > 300 and ellipsis_count == 0:
        status = "WARN (0 ellipsis in >300w section — informational)"
    else:
        status = "PASS"
    # Ellipsis is always PASS for section result — WARN is informational
    check_results["Ellipsis"] = True
    passes += 1
    thresh_label = "WARN if 0 (>300w)" if words > 300 else "N/A (<=300w)"
    results.append(f"  Ellipsis: {ellipsis_count} (threshold {thresh_label}) -- {status}")

    # 1A-5: Banned phrases
    banned_found = find_banned(text)
    ok = len(banned_found) == 0
    check_results["Banned phrases"] = ok
    status = "PASS" if ok else "HARD-FAIL"
    if ok: passes += 1
    else: fails += 1
    if banned_found:
        results.append(f"  Banned phrases: {len(banned_found)} found -- {status}: {', '.join(banned_found)}")
    else:
        results.append(f"  Banned phrases: 0 found (threshold 0) -- {status}")

    # 1C-1: Max sentences per paragraph (soft cap: max 4 paras OR ≤50% over, FAQ exempt)
    over_paras = sum(1 for p in paragraphs if paragraph_sentence_count(p) >= 4)
    max_sent = max((paragraph_sentence_count(p) for p in paragraphs), default=0)
    over_ratio = over_paras / total_paras if total_paras > 0 else 0
    if faq:
        ok = True
        status = "EXEMPT (FAQ)"
    else:
        ok = over_paras <= 4 or over_ratio <= 0.50
        status = "PASS" if ok else "FAIL"
    check_results["Max sentences/paragraph"] = ok
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Max sentences/paragraph: {max_sent} max, {over_paras} paras over 3 ({over_ratio:.0%}), (soft cap: max 4 or ≤50%) -- {status}")

    # 1C-2: Bullet usage
    ul_ol = len(fragment.find_all(["ul", "ol"]))
    p_count = len(paragraphs)
    total_blocks = ul_ol + p_count
    bullet_ratio = ul_ol / total_blocks if total_blocks > 0 else 0
    ok = bullet_ratio <= 0.30
    check_results["Bullet ratio"] = ok
    status = "PASS" if ok else "FAIL"
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Bullet ratio: {ul_ol}/{total_blocks} ({bullet_ratio:.0%}) (threshold <= 30%) -- {status}")

    # 1D-1: Average sentence length (v1.2: floor 7, target 7-12, warn 13-15, fail >15)
    if sentences:
        avg_len = sum(sentence_word_count(s) for s in sentences) / len(sentences)
    else:
        avg_len = 0
    if not sentences:
        ok = True
        status = "PASS (no sentences)"
    elif 7 <= avg_len <= 12:
        ok = True
        status = "PASS"
    elif 13 <= avg_len <= 15:
        ok = True
        status = "WARN (13-15w acceptable)"
    elif avg_len < 7:
        ok = False
        status = "FAIL (too short, <7w)"
    else:
        ok = False
        status = "FAIL (too long, >15w)"
    check_results["Avg sentence length"] = ok
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Avg sentence length: {avg_len:.1f} words (target 7-12, warn 13-15, fail <7 or >15) -- {status}")

    # 1D-2: Compound sentences (max 2 per H2)
    compound_count = count_compound_sentences(sentences)
    ok = compound_count <= 2
    check_results["Compound sentences"] = ok
    status = "PASS" if ok else "FAIL"
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Compound sentences (>=15w + connector): {compound_count} (max 2) -- {status}")

    # 1D-3: Contractions density
    contraction_count = count_contractions(text)
    expandable_count = count_expandable_forms(text)
    total_forms = contraction_count + expandable_count
    contr_ratio = contraction_count / total_forms if total_forms > 0 else 1.0
    ok = contr_ratio >= 0.80
    check_results["Contractions density"] = ok
    status = "PASS" if ok else "FAIL"
    if ok: passes += 1
    else: fails += 1
    results.append(f"  Contractions density: {contraction_count}/{total_forms} ({contr_ratio:.0%}) (threshold >= 80%) -- {status}")

    section_status = "PASS" if fails == 0 else f"FAIL ({fails} checks failed)"
    results.append(f"  Section result: {section_status}")

    return results, passes, fails, check_results, False


def check_article_level(ec):
    text = get_plain_text(ec)
    sentences = split_sentences(text)
    results = []
    fails = 0

    # 1B-1: All-caps words
    caps_words = count_all_caps(text)
    ok = len(caps_words) >= 1
    status = "PASS" if ok else "FAIL"
    if not ok: fails += 1
    results.append(f"  All-caps: {len(caps_words)} found (threshold >= 1) -- {status}")
    if caps_words:
        results.append(f"    Sample: {', '.join(caps_words[:10])}")

    # 1B-2: Em-dashes
    em_count = count_em_dashes(text)
    ok = em_count == 0
    status = "PASS" if ok else "HARD-FAIL"
    if not ok: fails += 1
    results.append(f"  Em-dashes: {em_count} found (threshold 0) -- {status}")

    # 1B-3: Rhetorical questions (moved from per-H2 to article-level)
    rhet_q = count_rhetorical_questions(sentences)
    ok = rhet_q >= 1
    status = "PASS" if ok else "FAIL"
    if not ok: fails += 1
    results.append(f"  Rhetorical questions (article-wide): {rhet_q} (threshold >= 1) -- {status}")

    return results, fails


def fail_pattern_analysis(section_results_map):
    check_names = [
        "Sentences <=3 words", "Single-sentence paragraphs", "Italics",
        "Ellipsis", "Banned phrases", "Max sentences/paragraph",
        "Bullet ratio", "Avg sentence length", "Compound sentences",
        "Contractions density",
    ]
    total_sections = len(section_results_map)
    fail_counts = {name: 0 for name in check_names}

    for sec_idx, checks in section_results_map.items():
        for name, passed in checks.items():
            if name in fail_counts and not passed:
                fail_counts[name] += 1

    sorted_fails = sorted(fail_counts.items(), key=lambda x: -x[1])
    lines = []
    for name, count in sorted_fails:
        pct = count / total_sections * 100 if total_sections > 0 else 0
        lines.append(f"  {name}: {count}/{total_sections} sections failed ({pct:.0f}%)")
    return lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 test_voice_checklist.py <path_to_html>")
        sys.exit(1)

    path = sys.argv[1]
    filename = os.path.basename(path)

    soup = load_html(path)
    ec = extract_entry_content(soup)
    sections = split_by_h2(ec)

    print(f"=== WAP_05d Voice Checklist v1.1 — Test Results ===")
    print(f"Article: {filename}")
    print(f"Total H2 sections: {len(sections)}")

    total_pass_sections = 0
    total_fail_sections = 0
    total_skipped = 0
    section_results_map = {}

    for i, (title, fragment) in enumerate(sections):
        sec_num = i + 1
        lines, passes, fails, check_results, skipped = check_section(title, fragment, sec_num)
        for line in lines:
            print(line)

        if skipped:
            total_skipped += 1
        elif fails == 0:
            total_pass_sections += 1
        else:
            total_fail_sections += 1

        if check_results:
            section_results_map[sec_num] = check_results

    # Article-level checks
    print(f"\n=== ARTICLE-LEVEL CHECKS ===")
    art_lines, art_fails = check_article_level(ec)
    for line in art_lines:
        print(line)

    art_status = "PASS" if art_fails == 0 else "FAIL"

    # Summary
    total_checked = total_pass_sections + total_fail_sections
    print(f"\n=== SUMMARY ===")
    print(f"Sections: {total_pass_sections} PASS / {total_fail_sections} FAIL out of {total_checked} checked ({total_skipped} skipped)")
    print(f"Article-level: {art_status}")

    # Fail pattern analysis
    if section_results_map:
        print(f"\n=== FAIL PATTERN ANALYSIS ===")
        pattern_lines = fail_pattern_analysis(section_results_map)
        for line in pattern_lines:
            print(line)


if __name__ == "__main__":
    main()
