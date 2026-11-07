"""Extract content photos and signature from Framework for the Future PDFs.
"""
import pypdf
from pathlib import Path

ASSETS_DIR = Path("archive/reports/dcms-framework-for-the-future-2003/assets")
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

TARGETS = [
    # (part_file, page_index_in_part, img_index, filename)
    ("Framework_for_the_Future1.pdf", 3, 0, "figure-004.jpg"),              # Page 4: Tessa Blackstone portrait
    ("Framework_for_the_Future1.pdf", 4, 0, "figure-005-signature.jpg"),    # Page 5: Tessa Blackstone signature
    ("Framework_for_the_Future1.pdf", 12, 0, "figure-013.jpg"),             # Page 13: Supporting early learning
    ("Framework_for_the_Future1.pdf", 13, 0, "figure-014.jpg"),             # Page 14: Bournemouth Central Library
    ("Framework_for_the_Future1.pdf", 14, 0, "figure-015.jpg"),             # Page 15: Promoting reading
    ("Framework_for_the_Future1.pdf", 17, 0, "figure-018.jpg"),             # Page 18: Norfolk & Norwich Millennium Library
    ("Framework_for_the_Future2.pdf", 0, 0, "figure-021.jpg"),              # Page 21: Idea Store at Bow
    ("Framework_for_the_Future2.pdf", 18, 0, "figure-039.jpg"),             # Page 39: Peckham Library
    ("Framework_for_the_Future3.pdf", 0, 0, "figure-041.jpg"),              # Page 41: Fazakerley Community Library
    ("Framework_for_the_Future3.pdf", 1, 0, "figure-042.jpg"),              # Page 42: Cookham Library
]

for part, p_idx, img_idx, fname in TARGETS:
    pdf_path = Path("archive/reports/dcms-framework-for-the-future-2003/source") / part
    reader = pypdf.PdfReader(str(pdf_path))
    page = reader.pages[p_idx]
    if len(page.images) > img_idx:
        img = page.images[img_idx]
        out_path = ASSETS_DIR / fname
        out_path.write_bytes(img.data)
        print(f"Saved {fname} ({len(img.data)} bytes)")
    else:
        print(f"Warning: Page index {p_idx} in {part} has {len(page.images)} images, needed index {img_idx}")

print("Image extraction finished.")
