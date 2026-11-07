from pathlib import Path
import re

text = Path('archive/reports/independent-library-report-for-england-2014/report.md').read_text(encoding='utf-8')
lines = text.splitlines()

for i, l in enumerate(lines):
    if l.strip() in ['ACTION', 'ACTIONS']:
        start = max(0, i-2)
        end = min(len(lines), i+15)
        print(f"=== Action block at line {i+1} ===")
        for k in range(start, end):
            print(f"  {k+1}: {lines[k]}")
        print()
