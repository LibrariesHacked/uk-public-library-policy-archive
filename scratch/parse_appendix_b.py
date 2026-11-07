"""Extract 3-column structured tables for Appendix B (Acknowledgments).
"""
import re
from pathlib import Path
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

part3 = "archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future3.pdf"
pages = list(extract_pages(part3))

def parse_ack_page(p_num):
    # p_num is 55..59 -> index is p_num - 41
    page = pages[p_num - 41]
    elements = []
    for el in page:
        if isinstance(el, LTTextContainer) and el.y1 < 750 and el.y0 > 35:
            elements.append((el.x0, el.y0, el.x1, el.y1, el.get_text().strip()))
    
    # Sort by y0 descending
    # Find intro texts (usually span width or start at x0 < 50)
    intros = []
    row_elements = []
    for x0, y0, x1, y1, t in elements:
        if "In July 2002" in t or "Advisory Council on Libraries" in t and "advice and guidance" in t or "would also like to thank" in t:
            intros.append((y1, t))
        else:
            row_elements.append((x0, y0, x1, y1, t))
            
    # Classify row elements by column:
    # col 1 (Name): x0 < 130
    # col 2 (Role): 130 <= x0 < 350
    # col 3 (Org): x0 >= 350
    return intros, row_elements

print("Loaded parse_ack_page.")
