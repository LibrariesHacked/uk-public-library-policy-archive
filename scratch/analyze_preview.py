import re
from pathlib import Path
# simple analysis

html = Path("scratch/preview.html").read_text(encoding="utf-8")
lines = html.splitlines()

for i, l in enumerate(lines):
    if '--- PAGE ' in l:
        p_num = re.search(r'PAGE (\d+)', l).group(1)
        prev_el = lines[i-1] if i > 0 else ""
        next_el = lines[i+1] if i + 1 < len(lines) else ""
        
        # Strip html tags to inspect pure text
        p_text = re.sub(r'<[^>]+>', '', prev_el).strip()
        n_text = re.sub(r'<[^>]+>', '', next_el).strip()
        
        # Check if p_text ends with punctuation
        ends_punc = bool(re.search(r'[.!?:\'"]$', p_text))
        starts_upper = bool(re.match(r'^[A-Z0-9#\-\*\"\(]', n_text))
        
        # Flag any suspicious transitions
        flag = not ends_punc or not starts_upper
        print(f"Page {int(p_num):2d}: {'[CHECK]' if flag else '  [OK] '} | Prev: {p_text[-50:] if p_text else '(empty)'} || Next: {n_text[:50] if n_text else '(empty)'}")
