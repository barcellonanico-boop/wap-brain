#!/usr/bin/env python3
"""
WAP_05d Voice Checklist — Mechanical checks on an HTML article.
Usage: python3 test_voice_checklist.py <path_to_html>
"""

import sys
import re
import math
from bs4 import BeautifulSoup, Comment

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BANNED_PHRASES = [
    "stunning", "breathtaking", "magical", "charming", "picturesque",
    "vibrant", "bustling", "hidden gem", "wanderlust", "delightful",
    "quaint", "whether you're looking for", "there's something for everyone",
    "get ready to explore", "a feast for the senses", "embark on",
    "immerse yourself", "experience the magic of", "it's worth noting",
    "moreover", "in conclusion", "to sum up", "don't miss", "be sure to",
    "ultimate guide", "complete guide", "locals love", "genuinely",
    "incredibly", "nestled in", "off the beaten path", "must-see",
    "must-visit",
]

CAPS_ACRONYMS = {
    "ZTL", "FAQ", "USA", "UK", "US", "EU", "PM", "AM", "ATM", "POS",
    "NOT", "DNA",
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
    """Return a copy of the entry-content div with excluded blocks removed."""
    ec = soup.find("div", class_="entry-content")
    if not ec:
        sys.exit("ERROR: No entry-content div found.")
    from copy import copy
    ec = BeautifulSoup(str(ec), "lxml").find("div", class_="entry-content")

    # Remove scripts, styles, comments
    for tag in ec.find_all(["script", "style"]):
        tag.decompose()
    for comment in ec.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()

    # Remove sidebar, footer, nav (unlikely inside entry-content but safe)
    for tag in ec.find_all(["aside", "footer", "nav"]):
        tag.decompose()

    # Remove hotel card divs (box-shadow in style)
    for div in ec.find_all("div", style=True):
        if "box-shadow" in div.get("style", ""):
            div.decompose()

    # Remove FAQ section (details/summary blocks)
    for tag in ec.find_all("details"):
        tag.decompose()

    # Remove TL;DR blue box (background-color: #e3f2fd)
    for div in ec.find_all("div", style=True):
        if "e3f2fd" in div.get("style", ""):
            div.decompose()

    # Remove callout divs (background-color: #fff3e0, #e8f5e9, #ffebee with display:flex)
    for div in ec.find_all("div", style=True):
        style = div.get("style", "")
        if any(c in style for c in ["fff3e0", "e8f5e9", "ffebee"]):
            div.decompose()

    # Remove affiliate disclosure div
    for div in ec.find_all("div"):
        text = div.get_text(strip=True)[:200].lower()
        if "affiliate" in text and ("disclosure" in text or "commission" in text or "earn" in text):
            # Only remove if it's a small standalone disclosure box
            if len(div.get_text(strip=True)) < 500:
                div.decompose()

    # Remove Pros/Cons/Advice divTable blocks
    for div in ec.find_all("div", class_=lambda c: c and "divTable" in c):
        div.decompose()

    # Remove Continue Planning grey box (background with grey tones)
    for div in ec.find_all("div", style=True):
        style = div.get("style", "")
        text_snippet = div.get_text(strip=True)[:100].lower()
        if "continue planning" in text_snippet and "background" in style:
            div.decompose()

    return ec


def split_by_h2(ec):
    """Split entry-content at h2 boundaries. Returns list of (title, soup_fragment)."""
    sections = []
    h2s = ec.find_all("h2")
    if not h2s:
        return sections

    for i, h2 in enumerate(h2s):
        title = h2.get_text(strip=True)
        # Collect all siblings between this h2 and the next h2
        fragment = BeautifulSoup("<div></div>", "lxml").find("div")
        sibling = h2.next_sibling
        while sibling:
            if getattr(sibling, "name", None) == "h2":
                break
            from copy import copy
            fragment.append(copy(sibling))
            sibling = sibling.next_sibling
        sections.append((title, fragment))
    return sections


def get_plain_text(element):
    return element.get_text(separator=" ", strip=True)


def count_words(text):
    return len(text.split())


def split_sentences(text):
    """Split text into sentences on .!? followed by space or end."""
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return []
    # Split on sentence-ending punctuation followed by space or end
    parts = re.split(r'(?<=[.!?])(?:\s+|$)', text)
    return [s.strip() for s in parts if s.strip()]


def get_paragraphs(fragment):
    """Return list of <p> tag elements."""
    return fragment.find_all("p")


def get_italics(fragment):
    """Return list of <em> and <i> tags."""
    return fragment.find_all(["em", "i"])


def count_ellipsis(text):
    """Count ... and \u2026 occurrences."""
    return text.count("\u2026") + text.count("...")


def count_rhetorical_questions(sentences):
    """Count sentences ending with ?"""
    return sum(1 for s in sentences if s.rstrip().endswith("?"))


def find_banned_phrases(text):
    """Return list of found banned phrases."""
    text_lower = text.lower()
    found = []
    for phrase in BANNED_PHRASES:
        # Use word boundary for single words, substring for multi-word
        if " " in phrase:
            if phrase.lower() in text_lower:
                found.append(phrase)
        else:
            if re.search(r'\b' + re.escape(phrase.lower()) + r'\b', text_lower):
                found.append(phrase)
    return found


def count_all_caps(text):
    """Count ALL CAPS words (>=2 chars) excluding known acronyms."""
    words = re.findall(r'\b[A-Z]{2,}\b', text)
    return [w for w in words if w not in CAPS_ACRONYMS]


def count_em_dashes(text):
    return text.count("\u2014")


def sentence_word_count(sentence):
    return len(sentence.split())


def count_compound_sentences(sentences):
    """Sentences >=15 words containing and/because/however/although."""
    count = 0
    for s in sentences:
        if sentence_word_count(s) >= 15 and COMPOUND_MARKERS.search(s):
            count += 1
    return count


def contraction_pattern():
    return re.compile(r"\b\w+['\\u2019]\w+\b")


def count_contractions(text):
    """Count words with apostrophe (contractions)."""
    # Match words like don't, won't, it's, you're etc.
    return len(re.findall(r"\b\w+['\u2019]\w+\b", text))


def count_expandable_forms(text):
    """Count expandable forms like 'do not', 'it is', etc."""
    text_lower = text.lower()
    count = 0
    for form in EXPANDABLE_FORMS:
        count += len(re.findall(r'\b' + re.escape(form) + r'\b', text_lower))
    return count


def paragraph_sentence_count(p_element):
    text = p_element.get_text(separator=" ", strip=True)
    return len(split_sentences(text))


# ---------------------------------------------------------------------------
# Main checks
# ---------------------------------------------------------------------------

def check_section(title, fragment, section_num):
    """Run all per-H2-section checks. Returns (results_lines, pass_count, fail_count)."""
    text = get_plain_text(fragment)
    words = count_words(text)
    paragraphs = get_paragraphs(fragment)
    sentences = split_sentences(text)
    italics = get_italics(fragment)
    results = []
    fails = 0
    passes = 0

    results.append(f"\n--- H2 #{section_num}: {title} ({words} words) ---")

    # 1A-1: Sentences <=3 words
    short_sentences = sum(1 for s in sentences if sentence_word_count(s) <= 3)
    threshold_short = math.ceil(words / 200) if words > 0 else 1
    status = "PASS" if short_sentences >= threshold_short else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Sentences <=3 words: {short_sentences} (threshold >= {threshold_short}) -- {status}")

    # 1A-2: Single-sentence paragraphs
    single_sent_paras = sum(1 for p in paragraphs if paragraph_sentence_count(p) == 1)
    total_paras = len(paragraphs)
    ratio = single_sent_paras / total_paras if total_paras > 0 else 0
    status = "PASS" if ratio >= 0.40 else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Single-sentence paragraphs: {single_sent_paras}/{total_paras} ({ratio:.0%}) (threshold >= 40%) -- {status}")

    # 1A-3: Italics instances
    italic_count = len(italics)
    if words > 300:
        ital_thresh = 3
    else:
        ital_thresh = 1
    status = "PASS" if italic_count >= ital_thresh else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Italics: {italic_count} (threshold >= {ital_thresh}) -- {status}")

    # 1A-4: Ellipsis
    ellipsis_count = count_ellipsis(text)
    if words > 300:
        ell_thresh = 2
        status = "PASS" if ellipsis_count >= ell_thresh else "FAIL"
    else:
        ell_thresh = 0
        status = "PASS"  # not required for <=300 words
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    thresh_label = f">= {ell_thresh}" if words > 300 else "N/A (<=300w)"
    results.append(f"  Ellipsis: {ellipsis_count} (threshold {thresh_label}) -- {status}")

    # 1A-5: Rhetorical questions
    rhet_q = count_rhetorical_questions(sentences)
    status = "PASS" if rhet_q >= 1 else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Rhetorical questions: {rhet_q} (threshold >= 1) -- {status}")

    # 1A-6: Banned phrases
    banned_found = find_banned_phrases(text)
    status = "PASS" if len(banned_found) == 0 else "HARD-FAIL"
    if status != "PASS":
        fails += 1
    else:
        passes += 1
    if banned_found:
        results.append(f"  Banned phrases: {len(banned_found)} found -- {status}: {', '.join(banned_found)}")
    else:
        results.append(f"  Banned phrases: 0 found (threshold 0) -- {status}")

    # 1C-1: Max sentences per paragraph
    max_sent = max((paragraph_sentence_count(p) for p in paragraphs), default=0)
    over_paras = sum(1 for p in paragraphs if paragraph_sentence_count(p) >= 4)
    status = "PASS" if over_paras == 0 else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Max sentences/paragraph: {max_sent} (max 3 allowed, {over_paras} paras over) -- {status}")

    # 1C-2: Bullet usage
    ul_ol = len(fragment.find_all(["ul", "ol"]))
    p_count = len(paragraphs)
    total_blocks = ul_ol + p_count
    bullet_ratio = ul_ol / total_blocks if total_blocks > 0 else 0
    status = "PASS" if bullet_ratio <= 0.30 else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Bullet ratio: {ul_ol}/{total_blocks} ({bullet_ratio:.0%}) (threshold <= 30%) -- {status}")

    # 1D-1: Average sentence length
    if sentences:
        avg_len = sum(sentence_word_count(s) for s in sentences) / len(sentences)
    else:
        avg_len = 0
    if 9 <= avg_len <= 12:
        status = "PASS"
    elif 13 <= avg_len <= 15:
        status = "WARN"
    else:
        status = "FAIL"
    if status == "FAIL":
        fails += 1
    elif status == "WARN":
        passes += 1  # warn counts as pass for section result
    else:
        passes += 1
    results.append(f"  Avg sentence length: {avg_len:.1f} words (target 9-12, 13-15 warn, >15 fail) -- {status}")

    # 1D-2: Compound sentences
    compound_count = count_compound_sentences(sentences)
    status = "PASS" if compound_count <= 2 else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Compound sentences (>=15w + connector): {compound_count} (max 2) -- {status}")

    # 1D-3: Contractions density
    contraction_count = count_contractions(text)
    expandable_count = count_expandable_forms(text)
    total_forms = contraction_count + expandable_count
    contr_ratio = contraction_count / total_forms if total_forms > 0 else 1.0
    status = "PASS" if contr_ratio >= 0.80 else "FAIL"
    if status == "FAIL":
        fails += 1
    else:
        passes += 1
    results.append(f"  Contractions density: {contraction_count}/{total_forms} ({contr_ratio:.0%}) (threshold >= 80%) -- {status}")

    # Section result
    section_status = "PASS" if fails == 0 else f"FAIL ({fails} checks failed)"
    results.append(f"  Section result: {section_status}")

    return results, passes, fails


def check_article_level(ec):
    """Run article-level checks."""
    text = get_plain_text(ec)
    results = []
    fails = 0

    # 1B-1: All-caps words
    caps_words = count_all_caps(text)
    status = "PASS" if len(caps_words) >= 1 else "FAIL"
    if status == "FAIL":
        fails += 1
    results.append(f"  All-caps: {len(caps_words)} found (threshold >= 1) -- {status}")
    if caps_words:
        # Show first 10
        sample = caps_words[:10]
        results.append(f"    Sample: {', '.join(sample)}")

    # 1B-2: Em-dashes
    em_count = count_em_dashes(text)
    status = "PASS" if em_count == 0 else "HARD-FAIL"
    if status != "PASS":
        fails += 1
    results.append(f"  Em-dashes: {em_count} found (threshold 0) -- {status}")

    return results, fails


def fail_pattern_analysis(section_check_names, section_results_map):
    """Analyze which checks fail most often across sections."""
    check_names = [
        "Sentences <=3 words",
        "Single-sentence paragraphs",
        "Italics",
        "Ellipsis",
        "Rhetorical questions",
        "Banned phrases",
        "Max sentences/paragraph",
        "Bullet ratio",
        "Avg sentence length",
        "Compound sentences",
        "Contractions density",
    ]
    fail_counts = {}
    total_sections = len(section_results_map)
    for name in check_names:
        fail_counts[name] = 0

    for sec_idx, checks in section_results_map.items():
        for name, passed in checks.items():
            if not passed:
                fail_counts[name] = fail_counts.get(name, 0) + 1

    # Sort by most failing first
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
    import os
    filename = os.path.basename(path)

    soup = load_html(path)
    ec = extract_entry_content(soup)
    sections = split_by_h2(ec)

    print(f"=== WAP_05d Voice Checklist — Test Results ===")
    print(f"Article: {filename}")
    print(f"Total H2 sections: {len(sections)}")

    total_pass_sections = 0
    total_fail_sections = 0
    section_results_map = {}  # sec_idx -> {check_name: bool}

    check_names = [
        "Sentences <=3 words",
        "Single-sentence paragraphs",
        "Italics",
        "Ellipsis",
        "Rhetorical questions",
        "Banned phrases",
        "Max sentences/paragraph",
        "Bullet ratio",
        "Avg sentence length",
        "Compound sentences",
        "Contractions density",
    ]

    for i, (title, fragment) in enumerate(sections):
        sec_num = i + 1
        lines, passes, fails = check_section(title, fragment, sec_num)
        for line in lines:
            print(line)

        # Track per-check pass/fail for pattern analysis
        section_results_map[sec_num] = {}
        # Parse pass/fail from output lines (simpler: re-run checks inline)
        text = get_plain_text(fragment)
        words = count_words(text)
        paragraphs = get_paragraphs(fragment)
        sentences = split_sentences(text)
        italics = get_italics(fragment)

        # Re-evaluate each check for pattern tracking
        short_sentences = sum(1 for s in sentences if sentence_word_count(s) <= 3)
        threshold_short = math.ceil(words / 200) if words > 0 else 1
        section_results_map[sec_num]["Sentences <=3 words"] = short_sentences >= threshold_short

        single_sent_paras = sum(1 for p in paragraphs if paragraph_sentence_count(p) == 1)
        total_paras = len(paragraphs)
        ratio = single_sent_paras / total_paras if total_paras > 0 else 0
        section_results_map[sec_num]["Single-sentence paragraphs"] = ratio >= 0.40

        italic_count = len(italics)
        ital_thresh = 3 if words > 300 else 1
        section_results_map[sec_num]["Italics"] = italic_count >= ital_thresh

        ellipsis_count = count_ellipsis(text)
        if words > 300:
            section_results_map[sec_num]["Ellipsis"] = ellipsis_count >= 2
        else:
            section_results_map[sec_num]["Ellipsis"] = True

        rhet_q = count_rhetorical_questions(sentences)
        section_results_map[sec_num]["Rhetorical questions"] = rhet_q >= 1

        banned_found = find_banned_phrases(text)
        section_results_map[sec_num]["Banned phrases"] = len(banned_found) == 0

        max_sent_over = sum(1 for p in paragraphs if paragraph_sentence_count(p) >= 4)
        section_results_map[sec_num]["Max sentences/paragraph"] = max_sent_over == 0

        ul_ol = len(fragment.find_all(["ul", "ol"]))
        p_count = len(paragraphs)
        total_blocks = ul_ol + p_count
        bullet_ratio = ul_ol / total_blocks if total_blocks > 0 else 0
        section_results_map[sec_num]["Bullet ratio"] = bullet_ratio <= 0.30

        if sentences:
            avg_len = sum(sentence_word_count(s) for s in sentences) / len(sentences)
        else:
            avg_len = 0
        # For pattern analysis: fail if outside 9-15 range (but not if section is empty)
        if not sentences:
            section_results_map[sec_num]["Avg sentence length"] = True  # skip empty
        else:
            section_results_map[sec_num]["Avg sentence length"] = 9 <= avg_len <= 15

        compound_count = count_compound_sentences(sentences)
        section_results_map[sec_num]["Compound sentences"] = compound_count <= 2

        contraction_count = count_contractions(text)
        expandable_count = count_expandable_forms(text)
        total_forms = contraction_count + expandable_count
        contr_ratio = contraction_count / total_forms if total_forms > 0 else 1.0
        section_results_map[sec_num]["Contractions density"] = contr_ratio >= 0.80

        if fails == 0:
            total_pass_sections += 1
        else:
            total_fail_sections += 1

    # Article-level checks
    print(f"\n=== ARTICLE-LEVEL CHECKS ===")
    art_lines, art_fails = check_article_level(ec)
    for line in art_lines:
        print(line)

    art_status = "PASS" if art_fails == 0 else "FAIL"

    # Summary
    total = len(sections)
    print(f"\n=== SUMMARY ===")
    print(f"Sections: {total_pass_sections} PASS / {total_fail_sections} FAIL out of {total} total")
    print(f"Article-level: {art_status}")

    # Fail pattern analysis
    print(f"\n=== FAIL PATTERN ANALYSIS ===")
    pattern_lines = fail_pattern_analysis(check_names, section_results_map)
    for line in pattern_lines:
        print(line)


if __name__ == "__main__":
    main()
