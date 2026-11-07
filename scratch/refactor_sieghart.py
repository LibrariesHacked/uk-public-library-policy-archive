"""Refactor Independent Library Report for England (Sieghart 2014).

Removes [pX-YYY] tags.
Formats clean lists, recommendations, and case studies.
Preserves page markers <!-- PAGE: N -->.
"""
import re
from pathlib import Path

FILE_PATH = Path("archive/reports/independent-library-report-for-england-2014/report.md")

def refactor():
    text = FILE_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()

    fm_lines = []
    body_lines = []
    in_fm = False
    fm_done = False

    for l in lines:
        if not fm_done:
            if l.strip() == "---":
                fm_lines.append(l)
                if in_fm:
                    fm_done = True
                else:
                    in_fm = True
                continue
            if in_fm:
                fm_lines.append(l)
                continue
        body_lines.append(l)

    cleaned_body = []
    for l in body_lines:
        s = l.strip()
        # strip [pX-YYY] lines
        if re.match(r"^\[p\d+-\d{3}\]$", s):
            continue
        cleaned_body.append(l)

    # Join cleaned body text
    body_text = "\n".join(cleaned_body)

    # Clean up cases where bullet lists have empty lines between each item
    # In Markdown, list items can be directly adjacent:
    # - item 1
    # - item 2
    body_lines = [l.strip() for l in body_text.splitlines()]
    
    formatted = []
    in_list = False
    for l in body_lines:
        if not l:
            if not in_list:
                formatted.append("")
            continue
        
        # Check if line is a bullet
        if l.startswith("•") or l.startswith("- ") or l.startswith("* "):
            content = re.sub(r"^[-•\*]\s*", "", l)
            formatted.append(f"- {content}")
            in_list = True
            continue
        
        # Check if numbered recommendation: e.g. "1.  The provision..."
        if re.match(r"^\d+\.\s+", l):
            formatted.append(l)
            in_list = True
            continue

        if in_list:
            formatted.append("")
            in_list = False

        formatted.append(l)
        formatted.append("")

    result = "\n".join(fm_lines) + "\n\n" + "\n".join(formatted) + "\n"
    result = re.sub(r"\n{3,}", "\n\n", result)

    FILE_PATH.write_text(result, encoding="utf-8")
    print(f"Refactored {FILE_PATH} ({len(result):,} chars)")

if __name__ == "__main__":
    refactor()

