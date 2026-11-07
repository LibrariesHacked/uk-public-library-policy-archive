import re
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

parts = [
    ("archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future1.pdf", 1),
    ("archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future2.pdf", 21),
    ("archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future3.pdf", 41),
]

all_paras = []
for pdf_path, start_p in parts:
    pages = list(extract_pages(pdf_path))
    for idx, page in enumerate(pages):
        p_num = start_p + idx
        for el in page:
            if isinstance(el, LTTextContainer) and el.y1 < 795:
                t = el.get_text().strip()
                for m in re.finditer(r"(?:^|\n)(\d+\.\d+)\s+", t):
                    all_paras.append((p_num, m.group(1)))

for ch in range(1, 8):
    found = sorted(set(p for page, p in all_paras if p.startswith(f"{ch}.")), key=lambda x: [int(n) for n in x.split(".")])
    print(f"Chapter {ch}: found {len(found)} paras: {found}")
