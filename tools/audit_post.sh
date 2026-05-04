#!/usr/bin/env bash
# audit_post.sh — WAP article mechanical auditor v0.6
# v0.6 (May 4 evening): B7 exclusions finalized — hotel-card divs (box-shadow)
#                       and bold data lists (>70% strong). Author intro NOT exempt.
# v0.5 (May 4 evening): B11 bold threshold 5→12 words (voice phrases valid bold),
#                       B14 FAQ answer range 30-120→15-150 words.
# v0.4 (May 4 evening): Category B (15 structural checks via BeautifulSoup Python module).
#                       Italic lead, TL;DR, affiliate disclosure, callout per H2,
#                       prose/callout char limits, bold ≤12 words, FAQ counts, Continue
#                       Planning, Bottom Line. Calls tools/audit_category_b.py.
# v0.3 (May 4): article-container extraction. v0.2 stripped head+comments+styles+scripts
#               but kept sidebar widgets and user comments section, causing A3 false
#               positive on em-dash in user comment. v0.3 isolates content to <article>
#               or <div class="entry-content"> only.
# v0.2 (May 4): body extraction strips head/comments/non-JSONLD scripts;
#               &amp; URL decoding for A10/A11/A12; curl timeout 15s;
#               WordPress system URL filter for A11; A12 accepts 202,
#               filters protocol-relative URLs.
# Implements Section 1 Category A of tools/audit_checklist_v0.1.md
# Usage: ./audit_post.sh path/to/article.html
# Exit codes: 0 = all PASS, 1 = any FAIL, 2 = usage/dependency error

set -uo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 path/to/article.html"
  exit 2
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
  echo "ERROR: File not found: $FILE"
  exit 2
fi

for cmd in curl grep awk python3; do
  if ! command -v "$cmd" &> /dev/null; then
    echo "ERROR: Missing dependency: $cmd"
    exit 2
  fi
done

# ============================================================
# Body extraction — strip <head> and HTML comments before greps
# ============================================================
# Many WordPress exports include <head> with theme/plugin metadata
# (Yoast SEO comments, etc.) that pollute em-dash and banned-word checks.
# Extract just the article body content for content-based checks.

BODY_FILE=$(mktemp -t wap_audit_body.XXXXXX.html)
trap "rm -f '$BODY_FILE'" EXIT

python3 <<PYEOF > "$BODY_FILE"
import re
with open('$FILE', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Step 1: Strip <head>...</head>
content = re.sub(r'<head\b[^>]*>.*?</head>', '', content, flags=re.IGNORECASE | re.DOTALL)

# Step 2: Strip HTML comments
content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

# Step 3: Strip <style> blocks
content = re.sub(r'<style\b[^>]*>.*?</style>', '', content, flags=re.IGNORECASE | re.DOTALL)

# Step 4: Strip <script> blocks (preserve JSON-LD for schema checks)
def strip_non_jsonld_scripts(match):
    block = match.group(0)
    if 'application/ld+json' in block.lower():
        return block
    return ''
content = re.sub(r'<script\b[^>]*>.*?</script>', strip_non_jsonld_scripts, content, flags=re.IGNORECASE | re.DOTALL)

# Step 5: Extract article container ONLY
# Try selectors in order of specificity:
# 1. <div class="entry-content"> ... up to comments/article-close (most precise)
# 2. <article id="post-..."> (main post article, not comment-body articles)
# 3. Original full content if no match (last resort)

ec_match = re.search(r'<div\b[^>]*class=["\'][^"\']*entry-content[^"\']*["\'][^>]*>', content, re.IGNORECASE)
if ec_match:
    ec_start = ec_match.end()
    # Find where entry-content ends: before comments section, author box closing,
    # or the main </article> tag. Use known boundary markers.
    boundaries = []
    for pattern in [r'<div\b[^>]*id=["\']comments["\']', r'<div\b[^>]*class=["\'][^"\']*comments-area',
                    r'<footer\b[^>]*class=["\'][^"\']*entry-meta']:
        bm = re.search(pattern, content[ec_start:], re.IGNORECASE)
        if bm:
            boundaries.append(bm.start())
    if boundaries:
        content = content[ec_start:ec_start + min(boundaries)]
    else:
        content = content[ec_start:]
else:
    # Fallback: try <article id="post-..."> (skip comment-body articles)
    art_match = re.search(r'<article\b[^>]*id=["\']post-\d+["\'][^>]*>(.*?)</article>', content, re.IGNORECASE | re.DOTALL)
    if art_match:
        content = art_match.group(1)
    # else: keep stripped content as-is

# Step 6: Within article, strip any nested comments, aside, nav, footer
content = re.sub(r'<div\b[^>]*id=["\']comments["\'][^>]*>.*', '', content, flags=re.IGNORECASE | re.DOTALL)
content = re.sub(r'<section\b[^>]*class=["\'][^"\']*comments?[^"\']*["\'][^>]*>.*?</section>', '', content, flags=re.IGNORECASE | re.DOTALL)
content = re.sub(r'<aside\b[^>]*>.*?</aside>', '', content, flags=re.IGNORECASE | re.DOTALL)
content = re.sub(r'<nav\b[^>]*>.*?</nav>', '', content, flags=re.IGNORECASE | re.DOTALL)
content = re.sub(r'<footer\b[^>]*>.*?</footer>', '', content, flags=re.IGNORECASE | re.DOTALL)

print(content)
PYEOF

FAIL_COUNT=0
PASS_COUNT=0
WARN_COUNT=0

if [ -t 1 ]; then
  GREEN='\033[0;32m'; RED='\033[0;31m'; YELLOW='\033[0;33m'; NC='\033[0m'
else
  GREEN=''; RED=''; YELLOW=''; NC=''
fi

print_pass() { printf "${GREEN}[PASS]${NC} %s\n" "$1"; PASS_COUNT=$((PASS_COUNT + 1)); }
print_fail() { printf "${RED}[FAIL]${NC} %s\n" "$1"; [ -n "${2:-}" ] && printf "       Reason: %s\n" "$2"; FAIL_COUNT=$((FAIL_COUNT + 1)); }
print_warn() { printf "${YELLOW}[WARN]${NC} %s\n" "$1"; WARN_COUNT=$((WARN_COUNT + 1)); }

echo "============================================"
echo "WAP Article Auditor v0.6 — Category A + B"
echo "File: $FILE ($(wc -c < "$FILE") bytes)"
echo "============================================"
echo ""

# A1 — File integrity
FILESIZE=$(wc -c < "$FILE")
if [ "$FILESIZE" -gt 1024 ]; then
  print_pass "A1 File integrity ($FILESIZE bytes)"
else
  print_fail "A1 File integrity" "File is only $FILESIZE bytes — likely truncated"
fi

# A2 — HTML valid
if command -v tidy &> /dev/null; then
  TIDY_ERRORS=$(tidy -e -q "$FILE" 2>&1 | grep -c "Error:" || true)
  if [ "$TIDY_ERRORS" -eq 0 ]; then
    print_pass "A2 HTML valid (no tidy errors)"
  else
    print_fail "A2 HTML valid" "$TIDY_ERRORS tidy errors found"
  fi
else
  print_warn "A2 HTML valid (tidy not installed — skipping)"
fi

# A3 — 0 em-dashes
EMDASH_COUNT=$(grep -c "—" "$BODY_FILE" || true)
if [ "$EMDASH_COUNT" -eq 0 ]; then
  print_pass "A3 0 em-dashes"
else
  print_fail "A3 0 em-dashes" "$EMDASH_COUNT em-dashes found"
fi

# A4 — 0 banned words
BANNED=$(grep -ciE "( SEO |AI Overview|ranking|keywords|schema markup)" "$BODY_FILE" || true)
if [ "$BANNED" -eq 0 ]; then
  print_pass "A4 0 banned words"
else
  print_fail "A4 0 banned words" "$BANNED matches found"
  grep -niE "( SEO |AI Overview|ranking|keywords|schema markup)" "$BODY_FILE" | head -3 | sed 's/^/       /'
fi

# A5 — 0 Italian-name violations
ITALIAN_V=$(grep -ciE "(Castellamare[^a]|Albergaria|Villa Igea[^,]|Piazza Matrice|Familia[^r])" "$BODY_FILE" || true)
if [ "$ITALIAN_V" -eq 0 ]; then
  print_pass "A5 0 Italian-name violations"
else
  print_fail "A5 0 Italian-name violations" "$ITALIAN_V violations found"
  grep -niE "(Castellamare[^a]|Albergaria|Villa Igea[^,]|Piazza Matrice|Familia[^r])" "$BODY_FILE" | head -3 | sed 's/^/       /'
fi

# A6 — 0 placeholders left
PLACEHOLDERS=$(grep -cE "\[NICO:|\[VERIFY:|TODO|TBD" "$BODY_FILE" || true)
if [ "$PLACEHOLDERS" -eq 0 ]; then
  print_pass "A6 0 placeholders left"
else
  print_fail "A6 0 placeholders left" "$PLACEHOLDERS found"
fi

# A7 — Title tag 50-60 chars
TITLE=$(python3 -c "
import re
with open('$FILE') as f: c = f.read()
m = re.search(r'<title[^>]*>(.*?)</title>', c, re.I|re.S)
print(m.group(1).strip() if m else '')
" 2>/dev/null)
if [ -z "$TITLE" ]; then
  print_warn "A7 Title tag not present in body HTML"
else
  TITLE_LEN=${#TITLE}
  if [ "$TITLE_LEN" -ge 50 ] && [ "$TITLE_LEN" -le 60 ]; then
    print_pass "A7 Title tag ($TITLE_LEN chars)"
  else
    print_fail "A7 Title tag length" "$TITLE_LEN chars (need 50-60): '$TITLE'"
  fi
fi

# A8: Meta description 140-160 chars per Google official guidelines (Nico choice May 4 — option A strict)
META=$(python3 -c "
import re
with open('$FILE') as f: c = f.read()
m = re.search(r'<meta[^>]*name=[\"\\x27]description[\"\\x27][^>]*content=[\"\\x27](.*?)[\"\\x27]', c, re.I|re.S)
print(m.group(1).strip() if m else '')
" 2>/dev/null)
if [ -z "$META" ]; then
  print_warn "A8 Meta description not present"
else
  META_LEN=${#META}
  if [ "$META_LEN" -ge 140 ] && [ "$META_LEN" -le 160 ]; then
    print_pass "A8 Meta description ($META_LEN chars)"
  else
    print_fail "A8 Meta description length" "$META_LEN chars (need 140-160)"
  fi
fi

# A9 — URL slug (skip in body-only mode)
print_warn "A9 URL slug check (validated at publish time)"

# A10 — All images return 200
echo ""
echo "Checking images (A10)..."
IMG_URLS=$(grep -oE 'src="[^"]+\.(jpg|jpeg|png|gif|webp|svg)[^"]*"' "$BODY_FILE" | sed 's/^src="//;s/"$//' | sed 's/&amp;/\&/g' | grep "^http" | sort -u)
IMG_FAILED=0
IMG_TOTAL=0
while IFS= read -r url; do
  [ -z "$url" ] && continue
  IMG_TOTAL=$((IMG_TOTAL + 1))
  STATUS=$(curl -sI -o /dev/null -w "%{http_code}" --max-time 15 "$url" 2>/dev/null || echo "000")
  if [ "$STATUS" != "200" ]; then
    IMG_FAILED=$((IMG_FAILED + 1))
    [ $IMG_FAILED -le 5 ] && printf "       [%s] %s\n" "$STATUS" "${url:0:80}"
  fi
done <<< "$IMG_URLS"
if [ "$IMG_TOTAL" -eq 0 ]; then
  print_warn "A10 No images with absolute URLs found"
elif [ "$IMG_FAILED" -eq 0 ]; then
  print_pass "A10 All $IMG_TOTAL images return 200"
else
  print_fail "A10 Images" "$IMG_FAILED of $IMG_TOTAL failed"
fi

# A11 — Internal links return 200
echo ""
echo "Checking internal links (A11)..."
INT_URLS=$(grep -oE 'href="https?://(www\.)?wearepalermo\.com[^"]*"' "$BODY_FILE" \
  | sed 's/^href="//;s/"$//' \
  | sed 's/&amp;/\&/g' \
  | grep -vE '(xmlrpc\.php|wp-admin|wp-login|wp-json|/feed/?|\?feed=|wp-content/uploads)' \
  | sort -u | grep -v "^$")
INT_FAILED=0
INT_TOTAL=0
while IFS= read -r url; do
  [ -z "$url" ] && continue
  INT_TOTAL=$((INT_TOTAL + 1))
  STATUS=$(curl -sI -L -o /dev/null -w "%{http_code}" --max-time 15 "$url" 2>/dev/null || echo "000")
  if [ "$STATUS" != "200" ]; then
    INT_FAILED=$((INT_FAILED + 1))
    [ $INT_FAILED -le 5 ] && printf "       [%s] %s\n" "$STATUS" "${url:0:80}"
  fi
done <<< "$INT_URLS"
if [ "$INT_TOTAL" -eq 0 ]; then
  print_warn "A11 No internal links found"
elif [ "$INT_FAILED" -eq 0 ]; then
  print_pass "A11 All $INT_TOTAL internal links return 200"
else
  print_fail "A11 Internal links" "$INT_FAILED of $INT_TOTAL failed"
fi

# A12 — Affiliate links return 200 (note: Booking/GYG often 403 on HEAD)
echo ""
echo "Checking affiliate links (A12)..."
AFF_URLS=$(grep -oE 'href="[^"]*booking\.com[^"]*"' "$BODY_FILE" | sed 's/^href="//;s/"$//' | sed 's/&amp;/\&/g' | grep '^https\?://' | sort -u)
AFF_TOTAL=$(echo "$AFF_URLS" | grep -c "booking\.com" || true)
AFF_FAILED=0
while IFS= read -r url; do
  [ -z "$url" ] && continue
  STATUS=$(curl -sI -L -o /dev/null -w "%{http_code}" --max-time 15 "$url" 2>/dev/null || echo "000")
  # Accept 200, 202, 301, 302, 403 (anti-bot) as "reachable"
  if [[ ! "$STATUS" =~ ^(200|202|301|302|403)$ ]]; then
    AFF_FAILED=$((AFF_FAILED + 1))
    [ $AFF_FAILED -le 3 ] && printf "       [%s] %s\n" "$STATUS" "${url:0:80}"
  fi
done <<< "$AFF_URLS"
if [ "$AFF_TOTAL" -eq 0 ]; then
  print_warn "A12 No affiliate links found"
elif [ "$AFF_FAILED" -eq 0 ]; then
  print_pass "A12 All $AFF_TOTAL affiliate links reachable"
else
  print_fail "A12 Affiliate links" "$AFF_FAILED of $AFF_TOTAL unreachable"
fi

# A13 — aid=918822 in every Booking link
BOOKING_TOTAL=$(grep -oE 'href="[^"]*booking\.com[^"]*"' "$BODY_FILE" | grep -c "booking\.com" || true)
BOOKING_AID=$(grep -oE 'href="[^"]*booking\.com[^"]*"' "$BODY_FILE" | grep -c "aid=918822" || true)
if [ "$BOOKING_TOTAL" -eq 0 ]; then
  print_warn "A13 No Booking links"
elif [ "$BOOKING_TOTAL" -eq "$BOOKING_AID" ]; then
  print_pass "A13 All $BOOKING_TOTAL Booking links have aid=918822"
else
  MISSING=$((BOOKING_TOTAL - BOOKING_AID))
  print_fail "A13 Booking aid" "$MISSING of $BOOKING_TOTAL missing aid=918822"
fi

# A14 — Article schema JSON-LD
SCHEMA_RESULT=$(python3 -c "
import re, json
with open('$FILE') as f: c = f.read()
scripts = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', c, re.S)
for s in scripts:
    try:
        d = json.loads(s.strip())
        if isinstance(d, dict) and d.get('@type') in ('Article','BlogPosting'):
            missing = [f for f in ('headline','author','datePublished') if f not in d]
            print('VALID' if not missing else f'INVALID: missing {missing}')
            exit()
    except: pass
print('NOT_FOUND')
" 2>/dev/null)
if [ "$SCHEMA_RESULT" = "VALID" ]; then
  print_pass "A14 Article schema valid"
elif [ "$SCHEMA_RESULT" = "NOT_FOUND" ]; then
  print_warn "A14 Article schema not in HTML (WordPress/Yoast adds at publish)"
else
  print_fail "A14 Article schema" "$SCHEMA_RESULT"
fi

# A15 — FAQPage schema
HAS_FAQ=$(grep -c "faq-brutto-ma-funziona" "$FILE" || true)
if [ "$HAS_FAQ" -eq 0 ]; then
  print_warn "A15 No FAQ section (skipping FAQPage schema check)"
else
  FAQ_RESULT=$(python3 -c "
import re, json
with open('$FILE') as f: c = f.read()
scripts = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', c, re.S)
for s in scripts:
    try:
        d = json.loads(s.strip())
        if isinstance(d, dict) and d.get('@type') == 'FAQPage':
            if 'mainEntity' in d and len(d['mainEntity']) > 0:
                print(f'VALID ({len(d[\"mainEntity\"])} questions)')
            else:
                print('INVALID: empty mainEntity')
            exit()
    except: pass
print('NOT_FOUND')
" 2>/dev/null)
  if [[ "$FAQ_RESULT" == VALID* ]]; then
    print_pass "A15 FAQPage schema $FAQ_RESULT"
  elif [ "$FAQ_RESULT" = "NOT_FOUND" ]; then
    print_fail "A15 FAQPage schema" "FAQ section present but no FAQPage JSON-LD found"
  else
    print_fail "A15 FAQPage schema" "$FAQ_RESULT"
  fi
fi

# ============================================================
# Category B — structural checks (Python module)
# ============================================================
echo ""
echo "============================================"
echo "Category B — Structural checks"
echo "============================================"

# Resolve path to audit_category_b.py relative to this script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CAT_B_OUTPUT=$(cat "$BODY_FILE" | python3 "$SCRIPT_DIR/audit_category_b.py" 2>&1)
CAT_B_EXIT=$?
echo "$CAT_B_OUTPUT"

# Parse PASS/FAIL/WARN counts from category B output
CAT_B_PASS=$(echo "$CAT_B_OUTPUT" | grep -c "^\[PASS\]\|^.*\[PASS\]" || true)
CAT_B_FAIL=$(echo "$CAT_B_OUTPUT" | grep -c "^\[FAIL\]\|^.*\[FAIL\]" || true)
CAT_B_WARN=$(echo "$CAT_B_OUTPUT" | grep -c "^\[WARN\]\|^.*\[WARN\]" || true)

PASS_COUNT=$((PASS_COUNT + CAT_B_PASS))
FAIL_COUNT=$((FAIL_COUNT + CAT_B_FAIL))
WARN_COUNT=$((WARN_COUNT + CAT_B_WARN))

# Summary
echo ""
echo "============================================"
printf "Summary: ${GREEN}$PASS_COUNT PASS${NC}, ${RED}$FAIL_COUNT FAIL${NC}, ${YELLOW}$WARN_COUNT WARN${NC}\n"
echo "============================================"

if [ "$FAIL_COUNT" -eq 0 ]; then
  echo "Result: ALL CHECKS PASSED"
  exit 0
else
  echo "Result: $FAIL_COUNT CHECK(S) FAILED"
  exit 1
fi
