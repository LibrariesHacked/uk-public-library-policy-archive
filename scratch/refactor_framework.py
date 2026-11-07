"""Refactor Framework for the Future into clean, beautiful, semantic diplomatic Markdown.

Removes [pN-MMM] tags.
Reconstructs broken sentences and paragraphs.
Formats genuine Markdown bullet lists and blockquotes.
Preserves page boundary markers <!-- PAGE: N -->.
"""
import re
from pathlib import Path

SOURCE_FILE = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")
OUTPUT_FILE = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")

def clean_report():
    text = SOURCE_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Find front matter
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

    # Process page by page
    pages = []
    curr_page_num = None
    curr_page_lines = []

    for l in body_lines:
        m = re.match(r"^<!-- PAGE: (\d+) -->$", l.strip())
        if m:
            if curr_page_num is not None:
                pages.append((curr_page_num, curr_page_lines))
            curr_page_num = int(m.group(1))
            curr_page_lines = []
            continue
        if curr_page_num is not None:
            curr_page_lines.append(l)

    if curr_page_num is not None:
        pages.append((curr_page_num, curr_page_lines))

    # Refactor each page
    refactored_pages = []

    for p_num, p_lines in pages:
        out = [f"<!-- PAGE: {p_num} -->", ""]

        # Filter out [pN-MMM] lines and clean up
        cleaned_raw = []
        for l in p_lines:
            s = l.strip()
            if re.match(r"^\[p\d+-\d{3}\]$", s):
                continue
            cleaned_raw.append(l)

        # Reconstruct paragraphs and blocks
        # First group by blank lines or headings
        blocks = []
        curr_b = []
        for l in cleaned_raw:
            s = l.strip()
            if not s:
                if curr_b:
                    blocks.append(curr_b)
                    curr_b = []
            elif s.startswith("#") or s.startswith(">") or s.startswith("![") or s.startswith("|"):
                if curr_b:
                    blocks.append(curr_b)
                    curr_b = []
                blocks.append([s])
            else:
                curr_b.append(s)
        if curr_b:
            blocks.append(curr_b)

        # Now merge blocks that are broken sentences or part of bullet lists
        processed_blocks = []
        i = 0
        while i < len(blocks):
            b = blocks[i]
            b_text = " ".join(b)

            # Heading, blockquote, image, table
            if b[0].startswith("#") or b[0].startswith(">") or b[0].startswith("![") or b[0].startswith("|") or b[0].startswith("*"):
                processed_blocks.append(b[0])
                i += 1
                continue

            # Check if this block is an isolated bullet marker: "-", "•"
            if b_text in ("-", "•", "• "):
                # Next block is the bullet text
                if i + 1 < len(blocks):
                    next_b = " ".join(blocks[i+1])
                    processed_blocks.append(f"- {next_b}")
                    i += 2
                    continue
                else:
                    i += 1
                    continue

            # Check if block is a bullet item starting with "-" or "•"
            if b_text.startswith("- ") or b_text.startswith("• "):
                bullet_content = re.sub(r"^[-•]\s*", "", b_text)
                processed_blocks.append(f"- {bullet_content}")
                i += 1
                continue

            # Check if block is a number prefix: e.g. "1.", "12."
            if re.match(r"^\d+\.\s*$", b_text):
                if i + 1 < len(blocks):
                    next_b = " ".join(blocks[i+1])
                    processed_blocks.append(f"{b_text} {next_b}")
                    i += 2
                    continue

            # Check if block is a broken sentence that continues into next block:
            # e.g. ends with "They need", "Building", "in", "The", "Report,"
            # and next block doesn't start with a heading or number
            if i + 1 < len(blocks):
                next_first = blocks[i+1][0]
                # If current ends with lowercase / comma / hyphen / conjunction / preposition
                if (not b_text.endswith((".", ":", ";", "?", "!")) or b_text.endswith((",", "and", "in", "the", "to", "of", "Report,", "Building"))) and not next_first.startswith("#") and not re.match(r"^\d+\.", next_first) and next_first not in ("-", "•"):
                    # Merge with next block
                    merged = b_text + " " + " ".join(blocks[i+1])
                    blocks[i+1] = [merged]
                    i += 1
                    continue

            processed_blocks.append(b_text)
            i += 1

        # Append processed blocks to out with clean spacing
        in_list = False
        for pb in processed_blocks:
            if pb.startswith("- "):
                out.append(pb)
                in_list = True
            else:
                if in_list:
                    out.append("")
                    in_list = False
                out.append(pb)
                out.append("")

        refactored_pages.append("\n".join(out).rstrip())

    full_text = "\n".join(fm_lines) + "\n\n" + "\n\n".join(refactored_pages) + "\n"
    
    # Specific targeted typographic improvements:
    full_text = full_text.replace("The Audit Commission Report, Building Better Library Services", "The Audit Commission Report, *Building Better Library Services*")
    full_text = full_text.replace("Audit Commission Report Building Better Library Services", "Audit Commission Report *Building Better Library Services*")
    
    OUTPUT_FILE.write_text(full_text, encoding="utf-8")
    print(f"Refactored {OUTPUT_FILE} ({len(full_text):,} characters, {len(pages)} pages)")

if __name__ == "__main__":
    clean_report()

