from pathlib import Path
import re
import pypdf

# Load PDFs
pdf_files = [
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future1.pdf',
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future2.pdf',
    'archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future3.pdf',
]

pdf_pages = []
for f in pdf_files:
    r = pypdf.PdfReader(f)
    for p in r.pages:
        pdf_pages.append(p.extract_text() or "")

print(f"Total PDF pages loaded: {len(pdf_pages)}")

# Load report.md
md_text = Path('archive/reports/dcms-framework-for-the-future-2003/report.md').read_text(encoding='utf-8')
md_pages = re.split(r'<!-- PAGE: \d+ -->', md_text)
print(f"Total markdown sections separated by PAGE comments: {len(md_pages)}")

# Check boundaries
for p_num in range(1, len(pdf_pages)):
    # PDF page p_num ends, page p_num+1 starts
    p_curr = pdf_pages[p_num - 1].strip()
    p_next = pdf_pages[p_num].strip()
    
    # Check markdown section p_num
    if p_num < len(md_pages):
        sec_curr = md_pages[p_num].strip()
        sec_next = md_pages[p_num + 1].strip() if (p_num + 1) < len(md_pages) else ""
        
        # Check last words of sec_curr and first words of sec_next
        sec_curr_lines = [l for l in sec_curr.splitlines() if l.strip()]
        sec_next_lines = [l for l in sec_next.splitlines() if l.strip()]
        last_l = sec_curr_lines[-1] if sec_curr_lines else ""
        first_l = sec_next_lines[0] if sec_next_lines else ""
        
        # Check if last_l ends with punctuation
        ends_punc = bool(re.search(r'[.!?:\'"]$', last_l.strip()))
        starts_cap = bool(re.match(r'^(#|\*\*|\>|\-|\*|\[|[A-Z0-9])', first_l.strip()))
        
        if not ends_punc or not starts_cap:
            print(f"=== Boundary Page {p_num} -> {p_num+1} ===")
            print(f"  MD End P.{p_num}: {last_l[-60:]}")
            print(f"  MD Start P.{p_num+1}: {first_l[:60]}")
