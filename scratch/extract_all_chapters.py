"""Extracts full text and structure for all 60 pages of dcms-framework-for-the-future-2003.
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

def get_page_boxes():
    all_pages = []
    for pdf_path, start_p in PARTS:
        pages = list(extract_pages(pdf_path))
        for idx, page in enumerate(pages):
            p_num = start_p + idx
            boxes = []
            for el in page:
                if isinstance(el, LTTextContainer):
                    t = clean(el.get_text()).strip()
                    if not t: continue
                    # Top running header
                    if el.y1 > 795: continue
                    # Bottom page number
                    if re.match(r"^\d{1,2}$", t) and (el.y0 < 36 or el.y1 > 790): continue
                    boxes.append({
                        "x0": el.x0, "y0": el.y0, "x1": el.x1, "y1": el.y1,
                        "text": t
                    })
            all_pages.append((p_num, boxes))
    return all_pages

if __name__ == "__main__":
    pages = get_page_boxes()
    print(f"Loaded {len(pages)} pages.")
