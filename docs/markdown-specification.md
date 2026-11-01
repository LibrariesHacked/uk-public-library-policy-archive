# Diplomatic Markdown Specification (`report.md`)

## Purpose and Editorial Philosophy

Every report in the **UK Public Library Policy Archive** is accompanied by a full-text Markdown transcription (`archive/reports/<report-slug>/report.md`).

Unlike commercial document-conversion pipelines designed for retrieval-augmented generation (RAG) or text summarization, our Markdown editions are **diplomatic archival transcriptions**. Their purpose is to provide an accessible, durable, plain-text representation of the source PDF that preserves exact wording, structural hierarchy, and page-level citability.

> **Core Rule:** The source document remains authoritative. Never paraphrase, rewrite, modernise, improve wording, or normalise language. Preservation takes precedence over readability. Preserve uncertainty rather than invent certainty.

While the Text Encoding Initiative (**TEI P5**) provides the conceptual inspiration for page milestones (`<pb/>`), paragraph identification (`<p xml:id="..."/>`), and transcriptional uncertainty (`<unclear/>`), this archive intentionally **does not store documents as TEI XML**. Standard Markdown with minimal, explicit conventions ensures low maintenance overhead for a single maintainer and immediate readability in any text editor.

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

## 2. Page Boundary Markers

Every page in the source document must be explicitly marked in `report.md` using an HTML comment of the exact form:

```markdown
<!-- PAGE: 34 -->
```

### Rules for Page Markers

1. **Mandatory**: Every `report.md` must contain page markers for every transcribed page.
2. **Never removed**: Page markers must never be stripped during editing or formatting.
3. **Never renumbered**: Page markers must reflect the sequential page numbering of the source document. Automated validation requires `<!-- PAGE: N -->` markers to be present and sequential.
4. **Placement**: Place the `<!-- PAGE: N -->` marker at the exact boundary where the new page begins in the source PDF, preceded and followed by a blank line.
5. **Running headers and footers**: Repetitive running page headers, decorative borders, and standalone printed page numbers should be omitted from the body text so they do not interrupt paragraphs, as pagination is carried by `<!-- PAGE: N -->`.

---

## 3. Paragraph Identifiers

Every body paragraph in `report.md` receives a stable, page-scoped identifier placed on its own line immediately above the paragraph text:

```markdown
<!-- PAGE: 34 -->

[p34-001]
Libraries provide universal access to reading, information, and civic space across urban and rural communities.

[p34-002]
Public libraries support lifelong learning from early childhood literacy programmes to adult digital skills training.
```

### Rules for Paragraph Identifiers

1. **Format**: `[p<PAGE>-<SEQ>]`, where `<PAGE>` matches the current `<!-- PAGE: N -->` number and `<SEQ>` is a zero-padded three-digit integer starting at `001` (`001`, `002`, `003`, ...).
2. **Page-scoped reset**: Paragraph numbering **restarts at `001` on each new page**. The first paragraph on page 34 is `[p34-001]`, the second is `[p34-002]`, and the first paragraph on page 35 is `[p35-001]`.
3. **Uniqueness**: Every `[pN-MMM]` identifier within a `report.md` file must be strictly unique.
4. **Paragraphs split across page breaks**: When a single sentence or paragraph is split across two pages in the source PDF, place the `<!-- PAGE: N+1 -->` marker at the exact point of the page break and assign the continuation on the new page its own page-scoped identifier (`[p35-001]`), preserving exact page-level provenance for every word.
5. **What receives a paragraph identifier**:
   - Standard prose paragraphs, executive summary paragraphs, and appendix paragraphs receive `[pN-MMM]` identifiers.
   - Blockquotes and standalone numbered/bulleted policy recommendations that function as paragraphs should be preceded by a `[pN-MMM]` identifier.
   - Structural headings (`#`, `##`, `###`), Markdown tables, figure blocks, and footnote definitions at the bottom of a section or document do not require their own `[pN-MMM]` line, though introductory prose preceding a list or table does.

---

## 4. Headings

Preserve the heading hierarchy, numbering, and wording of the source document **exactly**:

- Use ATX-style Markdown headings (`#`, `##`, `###`, `####`).
- **Do not improve**, rewrite, rephrase, or modernise heading text.
- Retain original section numbers if present in the source (e.g., `## 3.2 Statutory Duties under the 1964 Act`).
- Retain original capitalisation or casing where meaningful, or standard title/sentence case as printed without altering words.

---

## 5. Tables

Convert tables from the source PDF into standard **GitHub Flavored Markdown (GFM) pipe tables** wherever practical:

```markdown
| Authority Type | Total Branches (2024) | Net Change Since 2019 | Statutory Inquiries |
| :--- | ---: | ---: | ---: |
| County Councils | 142 | -4 | 0 |
| Unitary Authorities | 88 | -2 | 1 |
| Metropolitan Districts | 114 | -3 | 0 |
| **Total** | **344** | **-9** | **1** |
```

### Complex Tables

- Use HTML `<table>` markup **only when genuinely necessary**—for example, when a source table relies on complex multi-row (`rowspan`) or multi-column (`colspan`) merged cells whose meaning would be lost or distorted in a flat Markdown pipe table.
- Transcribe all table titles, column headers, cell values, source notes, and table footnotes verbatim. Never round numbers or recalculate totals.

---

## 6. Figures and Illustrations

When a source report contains charts, maps, photographs, or structural diagrams:

1. Extract the visual asset into `archive/reports/<report-slug>/assets/` using a sequential, zero-padded filename such as `assets/figure-001.jpg` or `assets/figure-004.jpg` (or `.png` / `.svg` as appropriate).
2. In `report.md`, reference the relative asset path and place the verbatim caption in italics on the line below:

```markdown
![Figure 4. Library Usage Trends](assets/figure-004.jpg)

*Figure 4. Library Usage Trends*
```

The image line carries the relative asset path `assets/figure-NNN.<ext>` (the alt text repeats the verbatim caption so the edition stays meaningful where images cannot be displayed). The italic line beneath is the verbatim printed caption. Figure numbers in filenames follow the figure numbering printed in the source, not the order of extraction.

3. If a figure contains embedded text, data labels, or source notes printed beneath the caption, transcribe the caption and source note verbatim. Do not invent interpretive alt-text or AI image descriptions that are not grounded in the document.

---

## 7. Footnotes and Citations

Represent footnotes and endnotes using **native Pandoc / GitHub Flavored Markdown footnote syntax**:

```markdown
[p12-003]
Under Section 7 of the Public Libraries and Museums Act 1964, every library authority in England and Wales is under a statutory duty to provide a comprehensive and efficient library service for all persons desiring to make use thereof.[^1]

[^1]: Public Libraries and Museums Act 1964, c. 75, s. 7(1).
```

- Retain original footnote numbers (`[^1]`, `[^2]`) matching the source document.
- Place footnote definitions either at the bottom of the page section where they appear (above the next `<!-- PAGE: N -->` marker) or consolidated at the end of the document, ensuring every `[^N]` reference resolves to its exact transcribed note text.

---

## 8. Handling OCR Uncertainty and Illegible Text

Older UK library policy reports (particularly scanned publications from 1995–2005) may contain degraded print, low-resolution faxed appendices, or ambiguous characters.

- **Never silently correct OCR errors by guessing missing words.**
- **Never infer missing text.**
- Whenever a character, word, number, or passage cannot be read with certainty from the source PDF, mark it explicitly using `[UNCERTAIN]`:
  - Adjacent to an uncertain reading: `1,480 [UNCERTAIN] active terminals`
  - In place of an illegible word or span: `[UNCERTAIN]`
- Record any persistent source scan defects in the QA review notes and `provenance.yaml`.

---

## 9. Page-Level Citation

Page markers and paragraph identifiers exist so that any passage can be cited precisely and permanently:

- **Page citation** (always): cite the page number from the `<!-- PAGE: N -->` marker, which matches the source PDF.
- **Paragraph citation** (when precision helps): add the identifier, for example `p. 3, para. [p3-003]`.
- **Edition citation** (when quoting the transcription): name the file path and the Git commit hash you read.

Identifiers are never reassigned. If QA finds a paragraph that was missed, give it the next free number on that page and record the correction in the commit message. Do not renumber the paragraphs that follow it. Validation reports the out-of-order number as a warning, not a failure. Stable citations matter more than tidy numbering.

---

## 10. Automated Checks

[`scripts/validate_markdown.py`](../scripts/validate_markdown.py) (run by `.github/workflows/validate-markdown.yml`) fails a `report.md` when:

- the YAML front matter is missing, or lacks `id`, `title` or `year`
- there are no `<!-- PAGE: N -->` markers, or a page number repeats or goes backwards
- a page marker or paragraph identifier is malformed
- a paragraph identifier repeats or sits on the wrong page
- a footnote reference has no definition

It warns, without failing, when page numbers skip (so that a maintainer can confirm no pages are missing) or when paragraph numbering on a page breaks the `001, 002, 003 …` sequence.
