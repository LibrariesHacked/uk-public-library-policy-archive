from pathlib import Path
import re
from pdfminer.high_level import extract_text

pdf_path = 'archive/reports/independent-library-report-for-england-2014/source/Independent_Library_Report-_18_December.pdf'
md_path = 'archive/reports/independent-library-report-for-england-2014/report.md'

md_lines = Path(md_path).read_text(encoding='utf-8').splitlines()

line_numbers = [156, 234, 272, 309, 325, 343, 370, 436]

for ln in line_numbers:
    print(f"=== Line {ln} in report.md ===")
    start = max(0, ln - 3)
    end = min(len(md_lines), ln + 4)
    for k in range(start, end):
        print(f"  {k+1}: {md_lines[k]}")
    print()
