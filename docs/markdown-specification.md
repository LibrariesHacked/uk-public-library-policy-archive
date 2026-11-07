# Diplomatic Markdown Specification (`report.md`)

## Purpose and Editorial Philosophy

Every report in the **UK Public Library Policy Archive** is accompanied by a full-text Markdown transcription (`archive/reports/<report-slug>/report.md`).

Unlike commercial document-conversion pipelines designed for retrieval-augmented generation (RAG) or text summarization, our Markdown editions are **diplomatic archival transcriptions**. Their purpose is to provide an accessible, durable, plain-text representation of the source PDF that preserves exact wording, structural hierarchy, semantic formatting, and page-level citability.

> **Core Rule:** The source document remains authoritative. Never paraphrase, rewrite, modernise, improve wording, or normalise language. Preservation takes precedence over subjective interpretation. Preserve uncertainty rather than invent certainty.

While the Text Encoding Initiative (**TEI P5**) provides conceptual inspiration for page milestones (`<pb/>`), division hierarchy, and transcriptional uncertainty (`<unclear/>`), this archive intentionally **does not store documents as TEI XML**. Standard, clean, semantic Markdown ensures low maintenance overhead for a single maintainer, immediate readability in any text editor, and high-fidelity rendering across GitHub, static site generators, and web archives.

---

## 1. YAML Front Matter

Every `report.md` file must begin with a YAML front matter block delimited by `---` lines on line 1.

At minimum, the front matter must include `id`, `title`, and `year`, matching the values in the accompanying `metadata.yaml`:

```yaml
---
id: sample-report-001
title: "Demonstration Public Library Review"
subtitle: "Statutory Provision, Community Access, and Digital Infrastructure in Fictional Shire"
publisher: "Department for Public Culture and Local Services"
year: 2026
source_url: "https://example.org/publications/demonstration-public-library-review-2026"
review_level: reviewed
---
```

This duplication between `metadata.yaml` and the Markdown front matter is intentional so that `report.md` remains self-contained and identifiable if used outside this repository.

---

## 2. Title Page and Imprint Layout

On the title page (usually Page 1), structure the metadata clearly using Markdown typographic hierarchy:

```markdown
<!-- PAGE: 1 -->

# Framework for the Future

## Libraries, Learning and Information in the Next Decade

**Department for Culture, Media and Sport**  
*February 2003*
```

- Document Title: `# Title` (Level 1 heading)
- Subtitle: `## Subtitle` (Level 2 heading)
- Issuing Department / Author: bold (`**Department...**`)
- Publication metadata (date, command paper number, ISBN): italic (`*...*`) or separate paragraphs.

---

## 3. Table of Contents

A Table of Contents must never be flattened into a continuous run-on paragraph. 

Always format the Table of Contents as a standard Markdown list with references to target pages:

```markdown
<!-- PAGE: 3 -->

## Contents

- [Foreword by Minister of State for the Arts](#page-4) (p. 4)
- [Executive Summary](#page-6) (p. 6)
- [1 Introduction](#page-12) (p. 12)
- [2 The Position of Libraries](#page-14) (p. 14)
- [3 Libraries' Modern Mission](#page-21) (p. 21)
- [4 Books, Reading and Learning](#page-24) (p. 24)
- [5 Digital Citizenship](#page-34) (p. 34)
- [6 Community and Civic Values](#page-38) (p. 38)
- [7 Delivering Change](#page-43) (p. 43)
- [Appendix A -- Glossary](#page-52) (p. 52)
- [Appendix B -- Acknowledgments](#page-55) (p. 55)
```

---

## 4. Page Boundary Markers

Every page in the source document must be explicitly marked in `report.md` using an HTML comment of the exact form:

```markdown
<!-- PAGE: 34 -->
```

### Rules for Page Markers

1. **Mandatory**: Every `report.md` must contain page markers for every transcribed page.
2. **Never removed**: Page markers must never be stripped during editing or formatting.
3. **Never renumbered**: Page markers must reflect the sequential page numbering of the source document. Automated validation requires `<!-- PAGE: N -->` markers to be present and sequential.
4. **Placement**:
   - **Between paragraphs / sections**: Place `<!-- PAGE: N -->` on its own line, preceded and followed by a blank line.
   - **Inside paragraphs / sentences**: When a page break occurs in the middle of a paragraph or sentence, place `<!-- PAGE: N -->` **inline** at the exact point of the page break:
     ```markdown
     **15.** This matters because reading is ever more critical in a knowledge-driven society. Most <!-- PAGE: 8 --> web pages are text based. People cannot be active or informed citizens unless they can read.
     ```
     *Reason*: In CommonMark and GitHub Flavored Markdown (GFM), placing `<!-- ... -->` on its own line initiates a Type 2 HTML block that immediately closes the active paragraph `<p>` tag and creates a new one below it, which fractures the sentence across two HTML paragraphs with vertical margins. Placing the marker **inline** ensures CommonMark treats it as inline raw HTML, preserving a single continuous, beautifully flowing paragraph in rendered HTML and markdown previews while preserving exact word-level page boundary citation.
5. **Running headers and footers**: Repetitive running page headers, decorative borders, and standalone printed page numbers should be omitted from the body text so they do not interrupt paragraphs, as pagination is carried by `<!-- PAGE: N -->`.
6. **Cross-Page Sentence Continuity**: Ensure no words at the bottom of a column or top of the next page are dropped or truncated during transcription.

---

## 5. Numbered Paragraphs vs. Lists

In UK government policy documents, white papers, and reviews, numbered points (such as `1.`, `2.`, ... `28.`, or `1.1`, `1.2`) are typically **numbered policy paragraphs**, not HTML list items. However, genuine short enumerated lists (such as a list of three core recommendations or sequential steps) also occur and must be formatted appropriately.

### The Rule for Numbered Policy Paragraphs
- **Never** format numbered policy paragraphs with bare `1. ` or `2. ` at the beginning of a line when they span across sections or are separated by headings. In standard Markdown, this creates an `<ol><li>` list that gets broken whenever a heading, blockquote, or page break appears, resulting in invalid markup or reset counters.
- **Always** format numbered paragraphs with bold numbers:
  `**1.** Text of the paragraph...` or `**1.1** Text of the paragraph...`
- **Mandatory Blank Lines**: Always separate consecutive bold numbered paragraphs with a blank line. In CommonMark and GFM, adjacent lines starting with `**1.** ...\n**2.** ...` without a blank line collapse into a single run-on paragraph in rendered HTML!
- This ensures that:
  - Paragraphs render cleanly as standard `<p>` elements.
  - Headings can appear between numbered paragraphs without breaking list syntax.
  - Bulleted sub-points (`- `) nested inside a numbered paragraph format cleanly.

### When Genuine Ordered Lists (`1. `, `2. `) Are Required
When a passage introduces a self-contained, contiguous enumerated list within a single section or paragraph (for example, a list of three major recommendations following a colon, sequential procedural steps, or statutory references):
- **Use standard Markdown ordered list syntax**:
  ```markdown
  Our conclusions are clear, concise and practical. We make three major recommendations:

  1. The provision of a national digital resource for libraries, to be delivered in partnership with local authorities
  2. The setting up of a task and finish force, led by local government...
  3. The task force, to work with local authorities...
  ```
- **Ordered List Criteria**: Genuine ordered lists must start at `1.`, increment sequentially (`1.`, `2.`, `3.`), belong to the same block, and have no intervening Markdown headings (`#`).

```markdown
### Introduction

**1.** Libraries are a much valued public institution built around a shared ideal: to make available resources that can be used by all members of the community...

**2.** More people go to the library than to cinemas or football grounds...

### The Position of Libraries

**5.** Libraries have four key strengths. They offer:

- Neutral, welcoming community space
- Enormous stocks of material
- ICT infrastructure offering public internet access
- Committed staff.
```

---

## 6. Headings and Hierarchy

Preserve the heading hierarchy, numbering, and wording of the source document **exactly**:

- Level 1 (`#`): Full report title (cover page).
- Level 2 (`##`): Major parts, prelims, executive summaries, and numbered chapters (`## 1 Introduction`, `## 2 The Position of Libraries`, `## 3 Libraries' Modern Mission`).
- Level 3 (`###`): Section subheadings within chapters (e.g. `### Historic strengths, future potential`, `### Supporting early learning`, `### Supporting older students`, `### For the taskforce`).
- Level 4 (`####`): Minor sub-topics or titled sub-clauses.

### Key Rules for Headings
1. **Unite Chapter Numbers and Titles**: In decorative PDF designs, chapter numerals (`1`, `2`, `3`) often appear on separate lines or coordinates above the title. They must ALWAYS be united into a single heading: `## 3 Libraries' Modern Mission`. Never allow an orphaned chapter number to attach to an adjacent case study box (e.g. `3 > ### Case Study...` is invalid).
2. **Never Drop Subheadings**: All topical section subheadings within chapters must be mapped to `### Subheading`. Never omit them, merge them into the body text, or leave them as unstyled plain text.

---

## 7. Callout Boxes, Case Studies, and Action Panels

Sidebars, case studies, spotlight panels, action callouts, and extended quotes set apart from the main text in tinted boxes or borders should be formatted as **Markdown blockquotes (`>`)**:

```markdown
> ### Case Study: Bournemouth Central Library
>
> Bournemouth's new Central Library is based in a bold, light, open modern building. It is already starting to change the town.
>
> There are fifty personal computers dotted around the building. In the foyer is a new café...
>
> > ![Bournemouth Central Library](assets/figure-014.jpg)
>
> *Bournemouth Central Library courtesy of Bournemouth Libraries, Leisure and Tourism Directorate.*
```

### Action Panels with Categorized Actors
When reports feature shaded "ACTION" or "ACTIONS" callout boxes with categorized actors (e.g., `Central government`, `Taskforce`, `Local government`), format them as blockquotes with underlined subheadings:

```markdown
> ### ACTIONS
>
> <u>Central government</u>
>
> - To make available funding to enable local authorities to extend WiFi access, computer facilities and workforce training for all public libraries in England
>
> <u>Taskforce</u>
>
> - To support the creation of a national digital library network
```

### Dedicated Case Study Chapters
When a report includes a dedicated case studies section (`## Case studies`), format each case study with a Level 3 heading: `### Case Study: [Title]` (e.g., `### Case Study: City of York`). This guarantees explicit document hierarchy and clean navigation across table of contents parsers.

### Rules for Callout Boxes
1. **Heading Formatting**: Always give the box a heading inside the blockquote: `> ### Case Study: [Title]`, `> ### ACTION`, or `> ### [Box Title]`. Never merge the box title into the first sentence of the text, and never leave `ACTION` as an unstyled bare line.
2. **Complete Enclosure**: Prefix every line of the callout (paragraphs, bullet lists, image embeds) with `> `.
3. **Contained Visuals**: If an illustration or photo belongs to the case study, embed it inside or immediately under the blockquote.

---

## 8. Tables and Member Directories

Convert tabular information from the source PDF into standard **GitHub Flavored Markdown (GFM) pipe tables** wherever practical:

```markdown
| Authority Type | Total Branches (2024) | Net Change Since 2019 | Statutory Inquiries |
| :--- | ---: | ---: | ---: |
| County Councils | 142 | -4 | 0 |
| Unitary Authorities | 88 | -2 | 1 |
| Metropolitan Districts | 114 | -3 | 0 |
| **Total** | **344** | **-9** | **1** |
```

### Table Integrity Rules
1. **Blank Lines**: Always ensure a blank line precedes and follows a Markdown table.
2. **No Empty Cells**: Never leave a cell completely empty between pipes (`| |`), which can break table parsing in standard markdown parsers. Use an em-dash (`| — |`) or descriptive placeholder.
3. **Cross-Page Table Continuation**: If a table spans across a page boundary (`<!-- PAGE: N -->`), close the table row before the page marker and restart the table with its header row after the marker.

---

## 9. Figures, Illustrations, and Signatures

When a source report contains charts, maps, photographs, structural diagrams, or author signatures:

1. **Image Audit Requirement**: Whenever a caption, figure credit (`Courtesy of...`, `Photographer: ...`), or author signature appears in the PDF, the corresponding visual asset **must** be extracted from the PDF at high resolution and saved into `archive/reports/<report-slug>/assets/` using a sequential filename (`assets/figure-NNN.jpg` or `assets/figure-NNN-desc.jpg`).
2. **Embedding and Verbatim Captions**: In `report.md`, reference the relative asset path and place the verbatim caption in italics on the line below:

```markdown
![Peckham Library](assets/figure-039.jpg)

*Peckham Library. Photographer: Len Cross 2000. Courtesy of London Borough of Southwark Libraries and Museums Service.*
```

3. **No Orphaned Captions**: Never leave a caption or credit stranded as plain text without its corresponding embedded image.
4. **No Merged Captions**: Never merge an image caption into a surrounding body text paragraph.
5. **Signatures**: Key ministerial or author signatures in forewords, prefaces, or transmittal letters must be extracted and embedded with an appropriate alt-text (`![Author Signature](assets/figure-NNN-signature.jpg)`).

---

## 10. Glossaries and Definition Lists

Glossaries, terminology reference lists, and acronym definitions must be formatted as **structured definition lists**:

```markdown
- **Advisory Council on Libraries (ACL)** — The statutory body set up under the Public Libraries and Museums Act 1964 to advise the Secretary of State for Culture, Media and Sport on public libraries.
- **Annual Library Plans (ALPs)** — Introduced by DCMS in 1998. English library authorities, through their ALPs, provide DCMS with an overview of their service...
- **The People's Network** — A £120 million lottery funded initiative, through the New Opportunities Fund (NOF)...
```

*Reason*: Formatting glossaries as `- **Term** — Definition` ensures proper hanging indentation, clear visual hierarchy, and readable rendering across all Markdown viewers, avoiding an undifferentiated wall of plain text paragraphs.

---

## 11. Footnotes and Citations

Represent footnotes and endnotes using **native Pandoc / GitHub Flavored Markdown footnote syntax**:

In the body text:
```markdown
Under Section 7 of the Public Libraries and Museums Act 1964, every library authority in England and Wales is under a statutory duty to provide a comprehensive and efficient library service for all persons desiring to make use thereof.[^1]
```

At the end of the document, consolidated under a `## Footnotes` section:
```markdown
## Footnotes

[^1]: Public Libraries and Museums Act 1964, c. 75, s. 7(1).
[^2]: <https://www.gov.uk/government/publications/example-policy-report>
```

### Footnote Rules
1. **Consolidate at End**: All footnote definitions (`[^N]:`) must be gathered at the **very end of the document** under a `## Footnotes` section, rather than scattered across individual pages. This keeps page markers and paragraphs clean, ensures seamless reading flow, and allows Markdown engines to render bidirectional jump links cleanly.
2. **Never Leave Raw Unlinked Footnotes**: Footnote citations in the text must never be glued as raw digits to words (e.g. `Library 211` or `report3`); always separate and format as `Library 21[^1]` and `report[^3]`.
3. **Never Leave Unformatted URLs at Page Bottoms**: Never leave raw numbers and URLs (e.g. `1 http://...` or `4 http:... 5 http:...`) at the bottom of pages before `<!-- PAGE: N -->` markers.
4. **Auto-linking URLs**: In footnote definitions containing URLs, wrap the URL in angle brackets `<http://...>` or Markdown link syntax `[Title](http://...)` to ensure the link is clickable in previews.
5. **Retain Original Numbering**: Retain original footnote numbers (`[^1]`, `[^2]`) matching the source document.


---

## 12. Handling OCR Uncertainty and Illegible Text

Older UK library policy reports (particularly scanned publications from 1995–2005) may contain degraded print, low-resolution faxed appendices, or ambiguous characters.

- **Never silently correct OCR errors by guessing missing words.**
- **Never infer missing text.**
- Whenever a character, word, number, or passage cannot be read with certainty from the source PDF, mark it explicitly using `[UNCERTAIN]`:
  - Adjacent to an uncertain reading: `1,480 [UNCERTAIN] active terminals`
  - In place of an illegible word or span: `[UNCERTAIN]`
- Record any persistent source scan defects in the QA review notes and `provenance.yaml`.

---

## 13. Automated Checks

[`scripts/validate_markdown.py`](../scripts/validate_markdown.py) (run by `.github/workflows/validate-markdown.yml`) fails a `report.md` when:

- the YAML front matter is missing, or lacks `id`, `title` or `year`
- there are no `<!-- PAGE: N -->` markers, or a page number repeats or goes backwards
- a page marker is malformed
- a footnote reference has no definition

It warns, without failing, when page numbers skip (so that a maintainer can confirm no pages are missing).
