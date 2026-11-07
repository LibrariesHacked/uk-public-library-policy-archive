from pathlib import Path
import re

text = Path('archive/reports/independent-library-report-for-england-2014/report.md').read_text(encoding='utf-8')
lines = text.splitlines()

print("Searching for footnote occurrences:")
for i, l in enumerate(lines):
    if re.search(r'^\s*\d+\s+https?://', l):
        print(f"Def at line {i+1}: {l[:80]}")
    if re.search(r'(Library 211|Strategy2|report3|Libraries4|authorities5|authorities6|futures7|thereof\'8|Programme9|initiative10)', l):
        print(f"Ref at line {i+1}: {l[:80]}")
