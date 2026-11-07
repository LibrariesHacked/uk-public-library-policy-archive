from pathlib import Path
p = Path('docs/workflow.md')
lines = p.read_text(encoding='utf-8').splitlines()

new_bullets = [
    '   - Include YAML front matter (`id`, `title`, `year`, etc.).',
    '   - Insert `<!-- PAGE: N -->` at the start of every single page without exception. When a page break falls in the middle of a sentence or paragraph, place `<!-- PAGE: N -->` INLINE (`word <!-- PAGE: N --> word`) so CommonMark HTML previews do not fracture the sentence into two separate `<p>` tags with vertical margins.',
    '   - Format numbered policy paragraphs with bold numbers (`**1.**`, `**1.1**`), never bare `1. `, preventing list resets across headings and callouts.',
    '   - Format all callout boxes and case studies as blockquotes with explicit headings (`> ### Case Study: [Title]`).',
    '   - Maintain natural paragraph continuity, native Markdown lists, and definition lists for glossaries (`- **Term** — Definition`).',
    '   - Preserve exact wording, spelling, punctuation, heading hierarchy, tables, footnotes (`[^1]`), appendices, tables of contents, and references.',
    '   - Complete Image Audit: Extract all content photos, figures, and author signatures into `archive/reports/<report-slug>/assets/figure-NNN.jpg` and embed them with verbatim italicised captions (`*Verbatim caption*`).',
    '   - Mark any illegible or ambiguous OCR passages with `[UNCERTAIN]` rather than guessing.',
]

# find line starting with '   - Include YAML'
idx = next(i for i, l in enumerate(lines) if l.strip().startswith('- Include YAML'))
# find line starting with '   - Mark any illegible'
idx2 = next(i for i, l in enumerate(lines) if l.strip().startswith('- Mark any illegible'))

lines[idx:idx2+1] = new_bullets
p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('Updated docs/workflow.md successfully!')
