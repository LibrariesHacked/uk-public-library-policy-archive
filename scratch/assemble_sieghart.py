"""Refined diplomatic Markdown edition generator for independent-library-report-for-england-2014.

Extracts text layout using pdfminer, groups lines into paragraphs by vertical gap,
preserves headings and bullet points, and generates verified diplomatic Markdown.
"""
import re
from pathlib import Path
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LTChar

PDF_PATH = Path("archive/reports/independent-library-report-for-england-2014/source/Independent_Library_Report-_18_December.pdf")
OUTPUT_FILE = Path("archive/reports/independent-library-report-for-england-2014/report.md")

FRONT_MATTER = """---
id: independent-library-report-for-england-2014
title: "Independent Library Report for England"
subtitle: null
publisher: "Department for Culture, Media & Sport"
year: 2014
source_url: "https://www.gov.uk/government/publications/independent-library-report-for-england"
review_level: converted
---
"""

SECTION_HEADINGS = {
    "Foreword", "Actions", "Digital library network", "Library taskforce",
    "Wider government initiatives", "E-lending", "Professional development",
    "Volunteers and community-led libraries", "Role of local government", "Case studies"
}

def clean_text(s: str) -> str:
    s = s.replace("\xad", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "--").replace("\u2014", "---")
    s = s.replace("\u00a3", "£")
    s = s.replace("\u2022", "•")
    s = s.replace("\u00a0", " ")
    return s

def extract_page_lines(page_layout):
    """Extract all text lines with bounding box (y1, y0, x0, font_size, text)."""
    raw_lines = []
    for element in page_layout:
        if isinstance(element, LTTextBox):
            for text_line in element:
                if isinstance(text_line, LTTextLine):
                    text = clean_text(text_line.get_text()).strip()
                    if not text:
                        continue
                    # Find maximum font size in line
                    font_sizes = [c.size for c in text_line if isinstance(c, LTChar)]
                    avg_size = sum(font_sizes) / len(font_sizes) if font_sizes else text_line.height
                    raw_lines.append({
                        "y1": text_line.y1,
                        "y0": text_line.y0,
                        "x0": text_line.x0,
                        "size": avg_size,
                        "text": text
                    })
    # Sort top-to-bottom
    raw_lines.sort(key=lambda l: -l["y1"])
    return raw_lines

def assemble():
    pages = list(extract_pages(str(PDF_PATH)))
    total_pages = len(pages)
    pages_md = []

    for page_idx, page_layout in enumerate(pages):
        p = page_idx + 1
        page_lines = [f"<!-- PAGE: {p} -->", ""]
        seq = 1

        def add_para(text):
            nonlocal seq
            pid = f"[p{p}-{seq:03d}]"
            seq += 1
            page_lines.append(pid)
            page_lines.append(text.strip())
            page_lines.append("")

        def add_heading(level, text):
            page_lines.append(f"{'#' * level} {text.strip()}")
            page_lines.append("")

        if p == 1:
            add_heading(1, "Independent Library Report for England")
            add_para("18 December 2014")
            pages_md.append("\n".join(page_lines).rstrip())
            continue

        if p == 2:
            add_para("[Blank page in original publication]")
            pages_md.append("\n".join(page_lines).rstrip())
            continue

        if p == 34:
            add_para("4th Floor, 100 Parliament Street\nLondon SW1A 2BQ\nwww.gov.uk/dcms")
            pages_md.append("\n".join(page_lines).rstrip())
            continue

        raw_lines = extract_page_lines(page_layout)

        # Filter out running header and running footer / page number
        content_lines = []
        for l in raw_lines:
            t = l["text"]
            # Top header: y0 >= 780
            if l["y0"] >= 780 and (t in ("Department for Culture, Media & Sport", "Independent Library Report") or re.match(r"^\d{1,2}$", t)):
                continue
            # Standalone page number near top or bottom
            if re.match(r"^\d{1,2}$", t) and (l["y0"] >= 750 or l["y0"] <= 60):
                continue
            content_lines.append(l)

        if p == 3:
            add_heading(2, "Contents")
            for l in content_lines:
                t = l["text"]
                if t.startswith("Contents"):
                    continue
                # Normalize dots in table of contents: "Foreword .... 4" -> "Foreword -- 4"
                clean_toc = re.sub(r"\.{2,}\s*", "-- ", t)
                add_para(clean_toc)
            pages_md.append("\n".join(page_lines).rstrip())
            continue

        # Group content_lines into blocks based on vertical gap or heading status
        # A new block starts if:
        # - it's a section heading (size > 18 or text in SECTION_HEADINGS)
        # - it's a sub-heading (bold / larger font, e.g. "Case study...", "Action...", "Recommendation...")
        # - the vertical gap between prev_line["y0"] and curr_line["y1"] > 14
        # - or it starts with a bullet point "•"
        blocks = []
        curr_block = []

        for l in content_lines:
            t = l["text"]
            is_sec_head = (t in SECTION_HEADINGS) or (l["size"] > 18)
            is_sub_head = bool(re.match(r"^(Case study|Action \d|Recommendation \d|For central government|For local government|Key findings|The role of|Next steps|Conclusion)", t, re.IGNORECASE))
            is_bullet = t.startswith("•") or t.startswith("- ") or t.startswith("* ")

            if not curr_block:
                curr_block.append(l)
                continue

            prev = curr_block[-1]
            gap = prev["y0"] - l["y1"]

            # Headings always break
            if is_sec_head or is_sub_head or is_bullet:
                blocks.append(curr_block)
                curr_block = [l]
            elif gap > 15: # Significant paragraph gap
                blocks.append(curr_block)
                curr_block = [l]
            else:
                curr_block.append(l)

        if curr_block:
            blocks.append(curr_block)

        # Output blocks as headings or paragraphs
        for b in blocks:
            b_text = " ".join(line["text"] for line in b)
            # Check if block is a heading
            first = b[0]
            if first["text"] in SECTION_HEADINGS:
                add_heading(2, first["text"])
                # If there was more text in the block
                if len(b) > 1:
                    rest = " ".join(l["text"] for l in b[1:])
                    add_para(rest)
            elif re.match(r"^(Case study|Action \d|Recommendation \d|For central government|For local government)", b_text, re.IGNORECASE) and len(b_text) < 80:
                add_heading(3, b_text)
            else:
                add_para(b_text)

        pages_md.append("\n".join(page_lines).rstrip())

    full_md = FRONT_MATTER + "\n" + "\n\n".join(pages_md) + "\n"
    OUTPUT_FILE.write_text(full_md, encoding="utf-8")
    print(f"Successfully generated {OUTPUT_FILE} ({len(full_md):,} characters, {total_pages} pages)")

if __name__ == "__main__":
    assemble()
