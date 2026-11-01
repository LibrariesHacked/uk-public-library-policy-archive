# Bibliographic Metadata Specification (`metadata.yaml`)

## Overview

Every archived document in the **UK Public Library Policy Archive** includes a canonical bibliographic metadata file named `metadata.yaml` stored in its report directory (`archive/reports/<report-slug>/metadata.yaml`).

In addition, a minimal subset of core citation fields (`id`, `title`, `year`, and optionally `publisher`, `publication_date`, and `source_url`) is intentionally duplicated inside the YAML front matter of `report.md`. This duplication ensures that every Markdown transcription remains self-describing and independently citable if distributed or read outside the repository structure. Where any discrepancy arises during maintenance, `metadata.yaml` is the canonical bibliographic source of truth, and automated validation checks verify consistency between `metadata.yaml` and the `report.md` front matter.

---

## Standards Alignment

### Dublin Core (ISO 15836 / DCMI Metadata Terms)

The field inventory in `metadata.yaml` draws directly on the **Dublin Core Metadata Element Set** and **DCMI Metadata Terms**, adapted into clear, domain-specific YAML keys suited to UK public sector policy publications:

| Archive Field | Dublin Core Mapping | Obligation |
| :--- | :--- | :--- |
| `id` | `dcterms:identifier` (local repository slug) | **Required** |
| `title` | `dc:title` | **Required** |
| `subtitle` | `dcterms:alternative` / title refinement | Optional (nullable) |
| `creators` | `dc:creator` | Optional (list) |
| `publisher` | `dc:publisher` | Optional |
| `publication_date` | `dcterms:issued` | Optional (nullable) |
| `year` | `dcterms:issued` (4-digit year) | **Required** |
| `publication_place` | `dcterms:spatial` (place of publication) | Optional (nullable) |
| `country` | `dcterms:spatial` (jurisdiction / nation) | Optional (nullable) |
| `language` | `dc:language` (ISO 639-1 / BCP 47) | Optional |
| `document_type` | `dc:type` | Optional |
| `pages` | `dcterms:extent` | Optional (nullable) |
| `identifier` | `dc:identifier` (command paper / departmental ref) | Optional (nullable) |
| `isbn` | `dcterms:bibliographicCitation` / `urn:isbn` | Optional (nullable) |
| `issn` | `dcterms:bibliographicCitation` / `urn:issn` | Optional (nullable) |
| `series` | `dcterms:isPartOf` | Optional (nullable) |
| `edition` | `dcterms:hasVersion` | Optional (nullable) |
| `source_url` | `dc:source` / `dcterms:isFormatOf` | **Required** |
| `source_pdf` | `dcterms:hasFormat` (local relative path or filename) | Optional (nullable) |
| `rights` | `dc:rights` / `dcterms:license` | Optional (nullable) |
| `review_level` | Administrative quality status | **Required** |

### Pandoc Metadata Conventions

Field names use lowercase `snake_case` keys compatible with **Pandoc YAML metadata blocks**. Dates follow ISO 8601 (`YYYY-MM-DD`, `YYYY-MM`, or `YYYY`), and multi-author credits use YAML sequence lists under `creators`.

---

## Core Editorial Rule: Observable Evidence Only

Metadata must be recorded **solely from directly observable publication evidence** (the title page, verso/imprint page, colophon, running headers/footers, or the official publisher's landing page).

- **Never guess or infer** missing bibliographic values.
- If a field is not stated in the source publication or official publisher record, either omit the optional key or set its value to `null`.
- Do not fabricate ISBNs, publication months, or personal author names when a report is issued anonymously by a department or taskforce.

---

## Field Reference

### `id` *(Required, string)*
A unique, immutable lowercase alphanumeric slug with hyphens identifying the report across the archive. It should match the directory name under `archive/reports/` or include a stable numeric/year suffix.
- **Pattern**: `^[a-z0-9]+(-[a-z0-9]+)*$`
- **Example**: `"dcms-framework-for-the-future-2003"` or `"sample-report-001"`

### `title` *(Required, string)*
The main title of the publication, transcribed verbatim from the title page without subtitle (unless the subtitle is grammatically inseparable). Preserve original spelling and punctuation.
- **Example**: `"Framework for the Future"`

### `subtitle` *(Optional, string or null)*
The secondary or explanatory title as printed on the cover or title page.
- **Example**: `"Libraries, Learning and Information in the Next Decade"`

### `creators` *(Optional, array of strings)*
Personal authors, principal investigators, chairpersons, or corporate bodies credited with authoring the text. List in the order printed on the title page.
- **Example**:
  ```yaml
  creators:
    - "William Sieghart"
    - "Independent Library Report Advisory Panel"
  ```

### `publisher` *(Optional, string or null)*
The government department, devolved administration, public body, or sector organisation responsible for issuing the document.
- **Example**: `"Department for Culture, Media and Sport"`

### `publication_date` *(Optional, string or null)*
The most specific observable date of publication in ISO 8601 format (`YYYY-MM-DD`, `YYYY-MM`, or `YYYY`).
- **Pattern**: `^[0-9]{4}(-(0[1-9]|1[0-2])(-(0[1-9]|[12][0-9]|3[01]))?)?$`
- **Example**: `"2014-12-18"` or `"2003-02"`

### `year` *(Required, integer)*
The four-digit calendar year of publication (`1900`–`2100`).
- **Example**: `2014`

### `publication_place` *(Optional, string or null)*
The city or town of publication as stated in the imprint (e.g., `"London"`, `"Edinburgh"`, `"Cardiff"`, `"Belfast"`). Set to `null` if unstated.

### `country` *(Optional, string or null)*
The primary UK nation or jurisdiction to which the policy document applies or in which it was issued.
- **Recommended values**: `"England"`, `"Scotland"`, `"Wales"`, `"Northern Ireland"`, `"United Kingdom"`

### `language` *(Optional, string or array of strings)*
BCP 47 / ISO 639-1 language code(s) of the document text. Defaults to `"en"` (English) or `["en", "cy"]` for bilingual Welsh/English publications.

### `document_type` *(Optional, string or null)*
The functional genre of the policy publication.
- **Recommended values**:
  - `"policy-paper"`
  - `"strategy"`
  - `"standards"`
  - `"independent-review"`
  - `"consultation"`
  - `"action-plan"`
  - `"impact-report"`
  - `"guidance"`
  - `"research-report"`
  - `"select-committee-report"`

### `pages` *(Optional, integer or null)*
The total number of pages in the source PDF file (or printed pagination count where explicitly consistent).
- **Example**: `64`

### `identifier` *(Optional, string or null)*
Any official departmental reference number, Command Paper number, Parliamentary paper number, or publisher reference code printed on the document.
- **Example**: `"PP 124/2003"` or `"Cm 8940"`

### `isbn` *(Optional, string or null)*
The 10-digit or 13-digit International Standard Book Number if printed on the document. Retain hyphens or normalise to digits; set to `null` if absent.
- **Example**: `"978-0-10-189402-9"`

### `issn` *(Optional, string or null)*
The 8-character International Standard Serial Number (`NNNN-NNNX`) if the publication belongs to a numbered serial.

### `series` *(Optional, string or null)*
The title of the series or programme to which the report belongs, if printed on the document.
- **Example**: `"Welsh Public Library Standards"`

### `edition` *(Optional, string or null)*
The edition statement or version designation printed on the source (e.g., `"First edition"`, `"Sixth Framework"`, `"Revised edition"`).

### `source_url` *(Required, string — URI)*
The canonical web page URL (landing page or official UK Government Web Archive capture page) from which the publication record originates.
- **Example**: `"https://www.gov.uk/government/publications/independent-library-report-for-england"`

### `source_pdf` *(Optional, string or null)*
The relative path within the report folder to the preserved source PDF (e.g., `"source/report.pdf"`) or the direct PDF filename.

### `rights` *(Optional, string or null)*
The copyright and licensing statement governing the source document (see [`docs/preservation.md`](../docs/preservation.md)).
- **Example**: `"Crown Copyright. Licensed under the Open Government Licence v3.0 (OGL-UK-3.0)."`

### `review_level` *(Required, string)*
Indicates the editorial quality assurance stage of the record and its accompanying Markdown transcription:
- `"unreviewed"` — Initial automated or raw capture; not yet checked against the PDF.
- `"converted"` — Converted to diplomatic Markdown with page and paragraph markers, awaiting full editorial review.
- `"reviewed"` — Checked against the source PDF for completeness of pages, headings, tables, figures, and footnotes.
- `"verified"` — Line-by-line proofread and independently verified against the authoritative source PDF with zero unresolved discrepancies.
