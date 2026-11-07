import re
from pathlib import Path

def md_to_html(md_path: Path) -> str:
    text = md_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    
    html_out = ["<!DOCTYPE html><html><head><meta charset='utf-8'><title>Preview</title>",
                "<style>body{font-family:sans-serif;max-width:800px;margin:2rem auto;line-height:1.6;padding:1rem;} blockquote{border-left:4px solid #ccc;margin:1rem 0;padding-left:1rem;color:#555;} img{max-width:100%;height:auto;} .page-marker{display:inline-block;background:#eee;color:#888;font-size:0.8em;padding:2px 6px;margin:0 4px;border-radius:3px;border:1px solid #ddd;}</style>",
                "</head><body>"]
    
    # Strip YAML front matter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            lines = parts[2].splitlines()
            
    in_blockquote = False
    in_list = False
    in_table = False
    curr_para = []
    
    def flush_para():
        nonlocal curr_para
        if curr_para:
            p_text = " ".join(curr_para)
            # Replace inline comments with visual badges for testing
            p_text = re.sub(r'<!-- PAGE: (\d+) -->', r'<span class="page-marker">PAGE \1</span>', p_text)
            p_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p_text)
            p_text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', p_text)
            p_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2"><br>', p_text)
            html_out.append(f"<p>{p_text}</p>")
            curr_para = []

    for lineno, raw in enumerate(lines, 1):
        line = raw.strip()
        
        if not line:
            flush_para()
            if in_list:
                html_out.append("</ul>")
                in_list = False
            if in_blockquote:
                # keep or flush depending
                pass
            continue
            
        # Standalone page comment
        if re.match(r'^<!-- PAGE: \d+ -->$', line):
            flush_para()
            m = re.search(r'\d+', line)
            p_num = m.group(0) if m else '?'
            html_out.append(f'<div class="page-marker" style="display:block;margin:1rem 0;font-weight:bold;">--- PAGE {p_num} ---</div>')
            continue
            
        # Heading
        if line.startswith("#"):
            flush_para()
            level = len(line.split()[0])
            htext = line.lstrip("#").strip()
            html_out.append(f"<h{level}>{htext}</h{level}>")
            continue
            
        # Blockquote
        if line.startswith(">"):
            flush_para()
            bq_text = line.lstrip(">").strip()
            # If bq heading
            if bq_text.startswith("#"):
                lvl = len(bq_text.split()[0])
                html_out.append(f"<blockquote><h{lvl}>{bq_text.lstrip('#').strip()}</h{lvl}></blockquote>")
            else:
                html_out.append(f"<blockquote><p>{bq_text}</p></blockquote>")
            continue
            
        # List item
        if line.startswith("- "):
            flush_para()
            if not in_list:
                html_out.append("<ul>")
                in_list = True
            l_text = line[2:].strip()
            l_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', l_text)
            html_out.append(f"<li>{l_text}</li>")
            continue
            
        # Pipe table
        if line.startswith("|"):
            flush_para()
            continue
            
        # Regular text line belonging to paragraph
        curr_para.append(line)
        
    flush_para()
    if in_list:
        html_out.append("</ul>")
    html_out.append("</body></html>")
    return "\n".join(html_out)

html_content = md_to_html(Path("archive/reports/dcms-framework-for-the-future-2003/report.md"))
Path("scratch/preview.html").write_text(html_content, encoding="utf-8")
print(f"Rendered preview written to scratch/preview.html ({len(html_content)} bytes)")
