#!/usr/bin/env python3
"""
rhythm_detector.py — v1.2
Detects paragraphs in a Markdown file that violate Nico's rhythm rules.

Rules (from PHASE_08_Voice_Pass.md v2.4.0):
- Rule C: paragraphs must have max 3 sentences. 4+ = violation,
  UNLESS the paragraph is a rhythmic list (all sentences short).
- Rule E: sentences must have max 30 words AND max 3 conjoined clauses
  (and / but / because / so / while). Beyond = violation.

Rhythmic list exemption (v1.2):
A paragraph is exempt from Rule C if EITHER:
  - All sentences in the paragraph are <= 12 words, OR
  - Median sentence length across the paragraph is <= 6 words.
Rationale: canon 2 and canon 3 contain intentional staccato sequences
mixing one setup sentence with a sequence of short verdicts. Median is
more robust than mean to a single long opener.

Output: numbered list of violating paragraphs with reason.

Usage:
  python3 tools/rhythm_detector.py <path-to-md-file>
"""

import sys
import re
from pathlib import Path

CONJOINED_MARKERS = [
    r'\band\b',
    r'\bbut\b',
    r'\bbecause\b',
    r'\bso\b',
    r'\bwhile\b',
]


def split_sentences(text: str) -> list[str]:
    """Split a paragraph into sentences on . ! ? boundaries, preserving content."""
    # Naive splitter; good enough for prose. Avoids splitting on decimals or abbreviations
    # by requiring a following space or end-of-string.
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


def count_conjoined_clauses(sentence: str) -> int:
    """Count occurrences of conjoined clause markers (and / but / because / so / while)."""
    lower = sentence.lower()
    count = 0
    for marker in CONJOINED_MARKERS:
        count += len(re.findall(marker, lower))
    return count


def is_skippable_paragraph(text: str) -> bool:
    """Skip headers, tables, list items, blockquotes, code, placeholders, separators."""
    stripped = text.strip()
    if not stripped:
        return True
    if stripped.startswith(('#', '|', '-', '*', '>', '[', '```', '---', '!')):
        return True
    if stripped.startswith('*') and stripped.endswith('*') and '\n' not in stripped:
        # Italic lead lines like *The honest answer...*
        return True
    return False


def is_rhythmic_list(sentences: list[str]) -> bool:
    """A paragraph is a rhythmic list if all sentences are short
    OR the median sentence length is low. Such paragraphs are
    canon-grade staccato sequences and must be exempted from rule C.
    """
    word_counts = [len(s.split()) for s in sentences]
    if not word_counts:
        return False
    if all(wc <= 12 for wc in word_counts):
        return True
    sorted_counts = sorted(word_counts)
    n = len(sorted_counts)
    if n % 2 == 1:
        median = sorted_counts[n // 2]
    else:
        median = (sorted_counts[n // 2 - 1] + sorted_counts[n // 2]) / 2
    if median <= 6:
        return True
    return False


def detect_violations(md_text: str) -> list[dict]:
    """Walk the document paragraph by paragraph and report rhythm violations."""
    paragraphs = md_text.split('\n\n')
    violations = []
    para_index = 0

    for raw in paragraphs:
        para_text = raw.strip()
        if is_skippable_paragraph(para_text):
            continue
        para_index += 1
        sentences = split_sentences(para_text)
        n_sentences = len(sentences)

        reasons = []
        if n_sentences >= 4 and not is_rhythmic_list(sentences):
            reasons.append(f'paragraph has {n_sentences} sentences (rule C: max 3)')

        for s in sentences:
            wc = len(s.split())
            cc = count_conjoined_clauses(s)
            if wc > 30 and cc >= 3:
                reasons.append(
                    f'sentence has {wc} words AND {cc} conjoined clauses '
                    f'(rule E: max 30 words AND max 3 clauses)'
                )

        if reasons:
            violations.append({
                'index': para_index,
                'text': para_text,
                'sentences': n_sentences,
                'reasons': reasons,
            })

    return violations


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 tools/rhythm_detector.py <path-to-md-file>')
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f'File not found: {path}')
        sys.exit(1)

    md_text = path.read_text(encoding='utf-8')
    violations = detect_violations(md_text)

    print('=' * 70)
    print(f'RHYTHM DETECTOR REPORT — {path.name}')
    print('=' * 70)
    print()

    if not violations:
        print('PASS: no rhythm violations detected.')
        return

    print(f'FOUND {len(violations)} violating paragraph(s):\n')

    for v in violations:
        print('-' * 70)
        print(f"Paragraph #{v['index']} — {v['sentences']} sentences")
        print('Reasons:')
        for r in v['reasons']:
            print(f'  - {r}')
        print('Text:')
        preview = v['text'][:400] + ('...' if len(v['text']) > 400 else '')
        print(f'  {preview}')
        print()

    print('=' * 70)
    print(f'TOTAL VIOLATIONS: {len(violations)}')
    print('=' * 70)


if __name__ == '__main__':
    main()
