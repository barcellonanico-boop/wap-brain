#!/usr/bin/env python3
"""
rhythm_merger.py — v1.0

Merges split paragraphs (from rhythm-fix pass) back into a source Markdown file.

Workflow:
1. Reads the source MD file (e.g. 08_Draft_Voice.md).
2. Reads the rhythm violations JSON (containing original paragraph indices and texts).
3. Reads the split output MD file (containing "### Paragraph N" blocks with the split versions).
4. For each violation, replaces the original paragraph text in the source with the split version.
5. Writes the merged output to a new MD file.

The matching is done by exact text match of the original paragraph in the source file.
If a match is not found, the script reports it and skips (does NOT silently fail).

Usage:
  python3 tools/rhythm_merger.py <source.md> <violations.json> <split_output.md> <output.md>
"""

import sys
import json
import re
from pathlib import Path


def parse_split_output(text: str) -> dict[int, str]:
    """Parse the split output file into a dict {paragraph_index: split_text}."""
    blocks = re.split(r'\n### Paragraph (\d+)\n', '\n' + text)
    result = {}
    for i in range(1, len(blocks), 2):
        if i + 1 < len(blocks):
            idx = int(blocks[i])
            content = blocks[i + 1].split('\n---\n')[0].strip()
            content = content.replace('All 23 paragraphs split. Done.', '').strip()
            result[idx] = content
    return result


def main():
    if len(sys.argv) != 5:
        print('Usage: python3 tools/rhythm_merger.py <source.md> <violations.json> <split_output.md> <output.md>')
        sys.exit(1)

    source_path = Path(sys.argv[1])
    violations_path = Path(sys.argv[2])
    split_path = Path(sys.argv[3])
    output_path = Path(sys.argv[4])

    for p in [source_path, violations_path, split_path]:
        if not p.exists():
            print(f'File not found: {p}')
            sys.exit(1)

    source_text = source_path.read_text(encoding='utf-8')
    violations_data = json.loads(violations_path.read_text(encoding='utf-8'))
    split_text = split_path.read_text(encoding='utf-8')

    splits = parse_split_output(split_text)

    print('=' * 70)
    print('RHYTHM MERGER')
    print('=' * 70)
    print(f'Source: {source_path.name}')
    print(f'Violations: {violations_data["total_violations"]}')
    print(f'Splits parsed: {len(splits)}')
    print()

    merged_text = source_text
    replaced = []
    missing = []

    for violation in violations_data['violations']:
        idx = violation['index']
        original = violation['text']

        if idx not in splits:
            missing.append((idx, 'no split version provided'))
            continue

        split_version = splits[idx]

        if original in merged_text:
            merged_text = merged_text.replace(original, split_version, 1)
            replaced.append(idx)
        else:
            missing.append((idx, 'original text not found in source'))

    print(f'Replaced: {len(replaced)} paragraphs')
    print(f'  Indices: {replaced}')

    if missing:
        print(f'\nFAIL: {len(missing)} paragraphs not replaced:')
        for idx, reason in missing:
            print(f'  Paragraph {idx}: {reason}')
        sys.exit(1)

    output_path.write_text(merged_text, encoding='utf-8')

    source_words = len(source_text.split())
    output_words = len(merged_text.split())

    print(f'\nOutput written: {output_path}')
    print(f'Source words: {source_words}')
    print(f'Output words: {output_words}')
    print(f'Diff: {output_words - source_words:+d} words')
    print('\nDONE.')


if __name__ == '__main__':
    main()
