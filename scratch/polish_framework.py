"""Polish Framework for the Future Markdown edition.

- Formats all bullet lists cleanly with newlines and standard Markdown list syntax.
- Formats sidebar / case study callout boxes with blockquotes (>).
- Fixes heading and paragraph transitions.
"""
import re
from pathlib import Path

FILE_PATH = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")

def polish():
    text = FILE_PATH.read_text(encoding="utf-8")

    # Fix bullet lists embedded in lines like: "include: - Item 1 - Item 2"
    def split_inline_bullets(match):
        pre = match.group(1).rstrip()
        items = match.group(2)
        # Split on " - " or " -   "
        parts = re.split(r"\s+-\s+", items.strip())
        res = [pre, ""]
        for p in parts:
            p_clean = p.strip()
            if p_clean:
                # remove leading dash if present
                p_clean = re.sub(r"^[-•]\s*", "", p_clean)
                res.append(f"- {p_clean}")
        res.append("")
        return "\n".join(res)

    # Replace inline bullet sequences
    # Pattern: something ending in : or ; followed by - ...
    pattern = r"([^\n]+:\s*)- +(.*)"
    
    # We will process line by line
    new_lines = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if line contains inline bullets: e.g. "include: - Item 1 - Item 2"
        if re.search(r":\s*-\s+", line):
            m = re.match(r"^(.*?:\s*)-\s+(.*)$", line)
            if m:
                intro = m.group(1).strip()
                bullet_str = m.group(2).strip()
                # split bullets by " -   " or " - "
                bullets = re.split(r"\s+-\s+", bullet_str)
                new_lines.append(intro)
                new_lines.append("")
                for b in bullets:
                    b = b.strip()
                    if b:
                        new_lines.append(f"- {b}")
                new_lines.append("")
                i += 1
                continue

        # Fix "4. ## The Position of Libraries" -> "## The Position of Libraries"
        if "4. ## The Position of Libraries" in line:
            new_lines.append("## The Position of Libraries")
            i += 1
            continue

        # Fix "4. ## Introduction" or similar
        line = re.sub(r"^\d+\.\s+##", "##", line)

        # Fix Audit Commission sidebar callout box:
        if line.startswith("Building Better Library Services -- Audit Commission, May 2002"):
            new_lines.append("> ### Building Better Library Services (Audit Commission, May 2002)")
            new_lines.append(">")
            new_lines.append("> Library services need to direct their resources at delivering the services that local people want, in particular:")
            new_lines.append(">")
            new_lines.append("> - Providing the books and information services that people want and need")
            new_lines.append("> - Maximising accessibility by opening at times that suit local people, making better use of joint-use facilities, and using the internet to provide access to their services to people at home")
            new_lines.append("> - Making services easy and pleasant to use -- in particular looking at what attracts people to bookshops")
            new_lines.append("> - Building awareness among non-users of the services they have on offer.")
            new_lines.append("")
            i += 1
            continue

        new_lines.append(line)
        i += 1

    result = "\n".join(new_lines)
    # Deduplicate multiple blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)

    FILE_PATH.write_text(result, encoding="utf-8")
    print(f"Polished {FILE_PATH} ({len(result):,} chars)")

if __name__ == "__main__":
    polish()

