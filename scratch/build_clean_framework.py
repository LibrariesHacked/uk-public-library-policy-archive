"""Comprehensive high-fidelity builder for dcms-framework-for-the-future-2003.

Follows the updated diplomatic specification:
- Title page: # Framework for the Future, ## Subtitle, **Department...**
- Contents: Markdown list with internal anchors
- Foreword: Tessa Blackstone + pull quote blockquote
- Executive summary: ### subheadings, **1.** to **32.** numbered paragraphs, bullet lists
- Chapters 1-7: ## N Chapter, ### subheadings, **N.M** numbered paragraphs, blockquote case studies
- Page 39: figure-039.jpg
- Appendices A & B
- Sequential <!-- PAGE: N --> markers with clean cross-page sentence flow
"""
import re
from pathlib import Path
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

PARTS = [
    ("archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future1.pdf", 1),
    ("archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future2.pdf", 21),
    ("archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future3.pdf", 41),
]

def clean(s: str) -> str:
    s = s.replace("\xad", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "--").replace("\u2014", "---")
    s = s.replace("\u00a3", "£")
    s = s.replace("\u00a0", " ")
    return s

def extract_raw_pages():
    raw_pages = []
    for pdf_path, start_p in PARTS:
        pages = list(extract_pages(pdf_path))
        for idx, page in enumerate(pages):
            p_num = start_p + idx
            elements = []
            for el in page:
                if isinstance(el, LTTextContainer):
                    t = clean(el.get_text()).strip()
                    # Exclude top running header and bottom standalone page numbers
                    if not t:
                        continue
                    if el.y1 > 795:
                        continue
                    if re.match(r"^\d{1,2}$", t) and (el.y0 < 36 or el.y1 > 790):
                        continue
                    elements.append({
                        "x0": el.x0, "y0": el.y0, "x1": el.x1, "y1": el.y1,
                        "text": t
                    })
            raw_pages.append((p_num, elements))
    return raw_pages

print("Loaded extract_raw_pages definition.")
