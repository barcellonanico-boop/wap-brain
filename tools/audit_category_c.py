#!/usr/bin/env python3
"""
audit_category_c.py — Category C affiliate + facts checks.
stdin: article body HTML (extracted by audit_post.sh)
argv[1]: article path (for project-folder manual gate checks)

Checks:
  C1 — Every hotel URL = WAP_12 verbatim
  C2 — Affiliate Opportunity Check completed (manual gate)
  C3 — Old article images recovered (manual gate, rewrites)
  C4 — 0 named restaurants (WAP_09 blacklist)
  C5 — Scout corrections applied (manual gate)
"""

import sys
import re
from pathlib import Path

content = sys.stdin.read()
article_path = sys.argv[1] if len(sys.argv) > 1 else None

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

def decode_amp(url):
    return url.replace('&amp;', '&')

# C1 — Hotel URLs match WAP_12 verbatim
booking_urls = set()
for m in re.finditer(r'href=["\']([^"\']*booking\.com[^"\']+)["\']', content):
    booking_urls.add(decode_amp(m.group(1)))

script_dir = Path(__file__).parent
wap_12_path = script_dir.parent / 'brain' / 'WAP_12_AFFILIATE_LINKS.md'

if not wap_12_path.exists():
    print_fail("C1 Hotel URL = WAP_12 verbatim", f"WAP_12 not found at {wap_12_path}")
else:
    wap_12_content = wap_12_path.read_text()
    wap_12_urls = set()
    for m in re.finditer(r'(https?://[^\s\)\]]*booking\.com[^\s\)\]]+)', wap_12_content):
        wap_12_urls.add(decode_amp(m.group(1).rstrip('.,;')))

    # Only check hotel-specific URLs (skip site-wide /index URLs etc.)
    article_hotel_urls = {u for u in booking_urls if '/hotel/' in u}
    extras = article_hotel_urls - wap_12_urls

    if not extras:
        print_pass(f"C1 All {len(article_hotel_urls)} hotel URLs match WAP_12 verbatim")
    else:
        print_fail(f"C1 Hotel URL = WAP_12 verbatim", f"{len(extras)} URLs not in WAP_12: {list(extras)[:3]}")

# C2 — Affiliate Opportunity Check (manual gate)
if article_path and 'projects/POST_' in article_path:
    project_dir = Path(article_path).parent
    prep_file = project_dir / '02_Prep.md'
    if prep_file.exists():
        prep_content = prep_file.read_text()
        if any(s in prep_content for s in ['Affiliate Opportunity Check', 'Affiliate Audit', 'affiliate opportunity']):
            print_pass("C2 Affiliate Opportunity Check section in 02_Prep.md")
        else:
            print_fail("C2 Affiliate Opportunity Check", "02_Prep.md exists but no Affiliate section")
    else:
        print_fail("C2 Affiliate Opportunity Check", f"02_Prep.md not found")
else:
    print_warn("C2 Affiliate Opportunity Check", "Skipped (test fixture, not a project)")

# C3 — Old article images recovered (manual gate)
if article_path and 'projects/POST_' in article_path:
    project_dir = Path(article_path).parent
    if (project_dir / '00_Live_HTML.md').exists():
        print_pass("C3 00_Live_HTML.md exists (images recovered)")
    else:
        print_warn("C3 Old article images", "00_Live_HTML.md not found (only required for rewrites)")
else:
    print_warn("C3 Old article images recovered", "Skipped (test fixture)")

# C4 — 0 named restaurants from WAP_09 blacklist
wap_09_path = script_dir.parent / 'brain' / 'WAP_09_PLACES_RESTAURANTS_BARS.md'

if not wap_09_path.exists():
    print_warn("C4 Named restaurants", "WAP_09 not found")
else:
    wap_09_content = wap_09_path.read_text()
    restaurant_names = []
    for m in re.finditer(r'\|\s*R\d{3}\s*\|\s*([^\|]+?)\s*\|', wap_09_content):
        name = m.group(1).strip()
        if 'Markets' in name or len(name) < 4:
            continue
        restaurant_names.append(name)

    body_text = re.sub(r'<[^>]+>', ' ', content)
    body_text = re.sub(r'\s+', ' ', body_text)

    found = []
    for name in restaurant_names:
        pattern = r'\b' + re.escape(name) + r'\b'
        if re.search(pattern, body_text):
            found.append(name)

    if not found:
        print_pass(f"C4 0 named restaurants ({len(restaurant_names)} blacklist entries checked)")
    else:
        print_fail(f"C4 0 named restaurants", f"Found: {found[:5]}")

# C5 — Scout corrections (manual gate)
if article_path and 'projects/POST_' in article_path:
    project_dir = Path(article_path).parent
    scout_files = list(project_dir.glob('*Scout_Verification*.md')) + list(project_dir.glob('*scout*.md'))
    if scout_files:
        print_pass(f"C5 Scout file present ({scout_files[0].name})")
    else:
        print_warn("C5 Scout corrections", "No Scout_Verification file found")
else:
    print_warn("C5 Scout corrections applied", "Skipped (test fixture)")

print()
print(f"Category C summary: {PASS} PASS / {FAIL} FAIL / {WARN} WARN")
sys.exit(1 if FAIL > 0 else 0)
