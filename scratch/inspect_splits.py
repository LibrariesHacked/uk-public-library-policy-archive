from pathlib import Path
from pdfminer.high_level import extract_text

pdf_files = [
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future1.pdf',
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future2.pdf',
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future3.pdf',
]

def get_page(p_num):
    # p_num is 1-based (1..60)
    file_idx = (p_num - 1) // 20
    page_in_file = (p_num - 1) % 20
    return extract_text(pdf_files[file_idx], page_numbers=[page_in_file])

targets = [
    (6, 7),
    (7, 8),
    (9, 10),
    (10, 11),
    (15, 16),
    (26, 27),
    (31, 32),
    (35, 36),
    (36, 37),
    (49, 50),
]

for p1, p2 in targets:
    t1 = get_page(p1)
    t2 = get_page(p2)
    print(f"==================================================")
    print(f"=== TRANSITION: PAGE {p1} -> PAGE {p2} ===")
    print(f"==================================================")
    print(f"--- Bottom of Page {p1} ---")
    lines1 = [l.strip() for l in t1.splitlines() if l.strip()]
    print("\n".join(lines1[-12:]))
    print(f"\n--- Top of Page {p2} ---")
    lines2 = [l.strip() for l in t2.splitlines() if l.strip()]
    print("\n".join(lines2[:12]))
    print()
