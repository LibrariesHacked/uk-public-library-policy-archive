from pathlib import Path
import re
from pdfminer.high_level import extract_text

pdf_files = [
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future1.pdf',
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future2.pdf',
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future3.pdf',
]

all_pages = []
for f in pdf_files:
    # 20 pages per file
    for p in range(20):
        t = extract_text(f, page_numbers=[p])
        all_pages.append(t)

print(f"Total pages extracted: {len(all_pages)}")

for p_idx in range(len(all_pages) - 1):
    p_curr = all_pages[p_idx].strip()
    p_next = all_pages[p_idx + 1].strip()
    
    # Get lines of p_curr from the end
    lines_curr = [l.strip() for l in p_curr.splitlines() if l.strip()]
    lines_next = [l.strip() for l in p_next.splitlines() if l.strip()]
    
    # Filter out running header "Framework for the Future: Libraries, Learning and Information in the Next Decade"
    # and standalone page numbers
    clean_curr = [l for l in lines_curr if not re.match(r'^(Framework for the Future|\d+$)', l)]
    clean_next = [l for l in lines_next if not re.match(r'^(Framework for the Future|\d+$)', l)]
    
    last_l = clean_curr[-1] if clean_curr else ""
    first_l = clean_next[0] if clean_next else ""
    
    # Check if last_l ends with hyphen, or lowercase/comma, or no period
    ends_incomplete = bool(re.search(r'([a-z0-9,\-—]|the|and|or|of|in|to|for|with|a|an)$', last_l, re.IGNORECASE)) and not bool(re.search(r'[.!?]\s*$', last_l))
    starts_continuation = bool(re.match(r'^[a-z]', first_l))
    
    if ends_incomplete or starts_continuation:
        print(f"=== CROSS-PAGE SPLIT: Page {p_idx + 1} -> Page {p_idx + 2} ===")
        print(f"  Bottom P.{p_idx + 1}: {' '.join(clean_curr[-3:])}")
        print(f"  Top    P.{p_idx + 2}: {' '.join(clean_next[:3])}")
