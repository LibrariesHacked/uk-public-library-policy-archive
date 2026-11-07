"""Test high-fidelity reconstruction of Framework for the Future pages 6-11.
"""
import re
from pathlib import Path
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

BOXES_DIR = Path(r"C:\Users\dave_\.gemini\antigravity\brain\0baef501-1552-4547-a502-ae79e523241a\scratch\fff_boxes")

def clean_text(s: str) -> str:
    s = s.replace("\xad", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "--").replace("\u2014", "---")
    s = s.replace("\u00a3", "£")
    s = s.replace("\u00a0", " ")
    return s

def read_boxes(page_num: int):
    f = BOXES_DIR / f"page_{page_num:02d}.txt"
    if not f.is_file():
        return []
    content = f.read_text(encoding="utf-8")
    raw_blocks = content.split("--- BOX ")
    boxes = []
    for b in raw_blocks:
        if not b.strip():
            continue
        lines = b.splitlines()
        header = lines[0]
        m = re.search(r"x0=([\d\.]+)\s+y0=([\d\.]+)\s+x1=([\d\.]+)\s+y1=([\d\.]+)", header)
        if not m:
            continue
        x0, y0, x1, y1 = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))
        text = "\n".join(lines[1:]).strip()
        if text:
            boxes.append({"x0": x0, "y0": y0, "x1": x1, "y1": y1, "text": text})
    return boxes

def reconstruct_page(p: int):
    boxes = read_boxes(p)
    # Separate into columns
    col1 = [b for b in boxes if b["x0"] < 300]
    col2 = [b for b in boxes if b["x0"] >= 300]
    col1.sort(key=lambda b: -b["y1"])
    col2.sort(key=lambda b: -b["y1"])

    def process_col(col_boxes):
        items = []
        i = 0
        while i < len(col_boxes):
            b = col_boxes[i]
            txt = b["text"].strip()

            # Check if this is a heading
            if re.match(r"^(Executive Summary|Introduction|The Position of Libraries|Libraries' Modern Mission|Books, Reading and Learning|Digital Citizenship|Community and Civic Values|Delivering Change|Appendix [AB] -- [A-Za-z]+|\d\s+[A-Z][A-Za-z\s]+)$", txt):
                items.append(("heading", 2, txt))
                i += 1
                continue

            # Check if this is a numbered paragraph prefix: e.g. "1.", "12.", "12.  Libraries..."
            num_match = re.match(r"^(\d+)\.\s*$", txt)
            if num_match:
                num = num_match.group(1)
                # Find matching text block with similar y
                matched_idx = None
                for j in range(i + 1, min(i + 4, len(col_boxes))):
                    candidate = col_boxes[j]
                    # if candidate top is close to number top
                    if abs(candidate["y1"] - b["y1"]) < 20 and candidate["x0"] > b["x0"]:
                        matched_idx = j
                        break
                if matched_idx is not None:
                    # Merge number with candidate text
                    cand_text = col_boxes[matched_idx]["text"].strip()
                    # Remove candidate from col_boxes
                    del col_boxes[matched_idx]
                    full_text = f"{num}. {cand_text}"
                    items.append(("para", full_text))
                else:
                    items.append(("para", txt))
                i += 1
                continue

            # Check bullet character "(cid:2)"
            if txt == "(cid:2)":
                # Find matching text block
                matched_idx = None
                for j in range(i + 1, min(i + 4, len(col_boxes))):
                    candidate = col_boxes[j]
                    if abs(candidate["y1"] - b["y1"]) < 15 and candidate["x0"] > b["x0"]:
                        matched_idx = j
                        break
                if matched_idx is not None:
                    cand_text = col_boxes[matched_idx]["text"].strip()
                    del col_boxes[matched_idx]
                    items.append(("bullet", cand_text))
                i += 1
                continue

            # Regular text block
            items.append(("para", txt))
            i += 1

        return items

    c1_items = process_col(col1)
    c2_items = process_col(col2)

    lines = [f"<!-- PAGE: {p} -->", ""]
    for kind, *args in c1_items + c2_items:
        if kind == "heading":
            lvl, text = args
            lines.append(f"{'#' * lvl} {text}")
            lines.append("")
        elif kind == "bullet":
            text = " ".join(l.strip() for l in args[0].splitlines() if l.strip())
            lines.append(f"- {text}")
        elif kind == "para":
            text = " ".join(l.strip() for l in args[0].splitlines() if l.strip())
            lines.append(text)
            lines.append("")

    return "\n".join(lines)

if __name__ == "__main__":
    for p in range(6, 8):
        print(f"=== PAGE {p} ===")
        print(reconstruct_page(p))

