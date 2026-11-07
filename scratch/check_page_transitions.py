from pathlib import Path
import re

text = Path('archive/reports/dcms-framework-for-the-future-2003/report.md').read_text(encoding='utf-8')
lines = text.splitlines()

for i, l in enumerate(lines):
    m = re.search(r'<!-- PAGE: (\d+) -->', l)
    if m:
        page_num = int(m.group(1))
        prev_lines = [lines[k] for k in range(max(0, i-5), i) if lines[k].strip()]
        next_lines = [lines[k] for k in range(i+1, min(len(lines), i+6)) if lines[k].strip()]
        prev_l = prev_lines[-1] if prev_lines else ''
        next_l = next_lines[0] if next_lines else ''
        
        ends_punc = bool(re.search(r'[.!?:\'"]\s*$', prev_l))
        starts_new = bool(re.match(r'^(#|\*\*|\>|\-|\*|\[)', next_l))
        
        warn = []
        if not ends_punc:
            warn.append('PREV_NO_PUNC')
        if not starts_new:
            warn.append('NEXT_NOT_NEW_BLOCK')
            
        print(f"Page {page_num:2d} (line {i+1}): {' '.join(warn) if warn else 'OK'}")
        if warn:
            print(f"   Prev: {prev_l}")
            print(f"   Next: {next_l}")
