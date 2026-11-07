import re
from pathlib import Path

text = Path("archive/reports/dcms-framework-for-the-future-2003/report.md").read_text(encoding="utf-8")

# CommonMark paragraph splitting:
# Blocks are separated by blank lines (or blockquotes, headings, html blocks, lists, code fences).
lines = text.splitlines()

# Let's inspect all blocks
blocks = []
curr_block = []
in_fence = False

for lineno, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith("```"):
        in_fence = not in_fence
        curr_block.append((lineno, line))
        continue
    if in_fence:
        curr_block.append((lineno, line))
        continue
    if not stripped:
        if curr_block:
            blocks.append(curr_block)
            curr_block = []
    else:
        # Check if line is a standalone block element that interrupts
        if stripped.startswith("#") or stripped.startswith("<!-- PAGE:") or stripped.startswith("|") or stripped.startswith(">"):
            if curr_block:
                blocks.append(curr_block)
                curr_block = []
            blocks.append([(lineno, line)])
        else:
            curr_block.append((lineno, line))

if curr_block:
    blocks.append(curr_block)

print(f"Total blocks identified: {len(blocks)}")

# Now find all blocks that look like regular paragraphs
paras = []
for b in blocks:
    first_line = b[0][1].strip()
    if first_line.startswith("#") or first_line.startswith("<!--") or first_line.startswith("|") or first_line.startswith("```") or first_line.startswith("---") or first_line.startswith(">") or first_line.startswith("- "):
        continue
    # This is a paragraph block!
    full_text = " ".join(line.strip() for _, line in b)
    paras.append((b[0][0], b[-1][0], full_text))

print(f"Total paragraph blocks: {len(paras)}")

# Look for paragraphs that end without punctuation or start with lowercase
issues = []
for i, (start_l, end_l, p_text) in enumerate(paras):
    # Check starts with lowercase
    first_char = p_text.lstrip("*_ #`>-[0123456789.]")[:1]
    ends_punc = bool(re.search(r'[.!?:\'"]$', p_text.strip()))
    
    if first_char.islower():
        issues.append((start_l, "STARTS_LOWER", p_text[:80]))
    if not ends_punc:
        issues.append((end_l, "ENDS_NO_PUNC", p_text[-80:]))

for l, kind, snippet in issues:
    print(f"Line {l:4d} [{kind}]: {snippet}")
