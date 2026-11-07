from pathlib import Path
import re

text = Path('archive/reports/independent-library-report-for-england-2014/report.md').read_text(encoding='utf-8')
lines = text.splitlines()

for i, l in enumerate(lines, 1):
    if re.match(r'^<!-- PAGE: \d+ -->$', l.strip()):
        # find prev non empty line
        p = i - 2
        while p >= 0 and not lines[p].strip():
            p -= 1
        prev_l = lines[p].strip() if p >= 0 else ''
        if not re.search(r"[.!?:\'\"\*\`\>\]\)]$", prev_l) and not prev_l.startswith(("#", "-", "*")):
            print(f"Marker line {i} (PAGE {l.strip()}):")
            print(f"   Prev line {p+1}: {repr(prev_l)}")
