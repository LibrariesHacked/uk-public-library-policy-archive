# UK Public Library Policy Archive

## Purpose

The **UK Public Library Policy Archive** (`uk-public-library-policy-archive`) is a documentary preservation archive for United Kingdom public library policy, strategy, statutory standards, consultation, and review documents published from approximately 1995 onwards across England, Scotland, Wales, and Northern Ireland.

Over the past three decades, responsibility for UK public library policy and sector oversight has transferred across numerous government departments, devolved administrations, non-departmental public bodies, and sector organisations—including the Department of National Heritage, the Department for Culture, Media and Sport (DCMS), the Museums, Libraries and Archives Council (MLA), Arts Council England (ACE), the Scottish Library and Information Council (SLIC), the Welsh Government (Llywodraeth Cymru), the Department for Communities in Northern Ireland, the Society of Chief Librarians (SCL), and Libraries Connected. As institutional websites have been reorganized or decommissioned, foundational policy documents have frequently suffered from link rot, inconsistent cataloguing, or loss of context.

This repository exists as a **source archive, not a search product**. Its objective is to preserve authoritative source documents alongside diplomatic, page-citable Markdown editions, bibliographic records, and verifiable provenance metadata in plain, durable formats suitable for long-term maintenance by a single archivist or researcher.

---

## Core Principles

### 1. Fidelity to the Source

The original published document remains the sole authoritative text. Transcribed Markdown editions are diplomatic representations of the source:

- Wording, spelling, punctuation, and capitalisation are preserved exactly as printed.
- Historical terminology and formatting conventions are never modernised, rewritten, paraphrased, or "improved".
- Document structure—including front matter, tables of contents, headings, footnotes, tables, figures, appendices, and bibliography—is retained in full.
- Where optical character recognition (OCR) or physical degradation renders a passage illegible or ambiguous, uncertainty is explicitly marked using `[UNCERTAIN]` rather than silently inferred.

### 2. Transparency and Provenance

Every archived item records a complete chain of custody from acquisition to transcription:

- The canonical publication landing page URL (`source_url`) and direct source document URL (`source_pdf_url`).
- Exact dates of acquisition (`acquired_date`), access (`accessed_date`), and transcription (`conversion_date`).
- Cryptographic fixity checksums (`pdf_sha256`, `source_checksum`) to verify that preserved PDFs remain unaltered bit-for-bit.
- Explicit documentation of the acquisition and conversion methods (`download_method`, `conversion_method`) and editorial review status (`review_status`).

### 3. Citability

Digital transcriptions often strip away the pagination required for scholarly and policy citation. Every Markdown edition in this archive enforces strict structural anchoring:

- Mandatory page boundary markers (`<!-- PAGE: N -->`) corresponding to the printed or PDF pagination of the source, providing stable page-level citation.
- Clean, semantic Markdown formatting (headings, lists, blockquotes, tables) that preserves continuous sentence flow and renders cleanly in standard Markdown and HTML environments.

### 4. Reproducibility and Maintainability

The archive is designed for a single maintainer using standard command-line utilities, plain-text files (Markdown, YAML, JSON Schema), and Git. A future maintainer or independent scholar can reconstruct, audit, or validate any record in the corpus using the documentation, schemas, and model-agnostic prompts contained within this repository alone, without reliance on proprietary software or external databases.

---

## Non-Goals

To protect the integrity and longevity of the primary sources, this repository **strictly excludes**:

- AI-generated summaries, abstracts, or executive digests not present in the source text
- Semantic enrichment, entity extraction, or automated subject tagging
- Vector embeddings, chunking pipelines, or vector database configurations
- Knowledge graphs or ontology mappings
- Search indexes, web application front-ends, or recommendation systems
- Editorial commentary, policy critique, or AI interpretations of policy documents

The repository exists solely to preserve, transcribe, and document source materials.

---

## Repository Structure

```text
/
├── README.md                          # Repository overview and archival guide
├── LICENSE.md                         # Open Government Licence v3.0 text
├── CITATION.cff                       # Citation File Format metadata for scholarly citation
├── .gitignore                         # Standard ignore rules for temporary and local files
├── .gitattributes                     # Fixity protection: binary flag for PDFs/images, LF for text
│
├── docs/                              # Archival documentation and editorial specifications
│   ├── metadata-schema.md             # Bibliographic metadata field definitions and Dublin Core mappings
│   ├── markdown-specification.md      # Diplomatic Markdown transcription rules and citation format
│   ├── preservation.md                # PREMIS-aligned provenance, fixity, and rights documentation
│   └── workflow.md                    # Nine-stage archival ingestion and quality assurance workflow
│
├── schemas/                           # JSON Schemas for automated validation
│   ├── metadata.schema.json           # Validation schema for metadata.yaml
│   └── provenance.schema.json         # Validation schema for provenance.yaml
│
├── templates/                         # Canonical starter templates for new archival records
│   ├── report.md                      # Diplomatic Markdown edition template
│   ├── metadata.yaml                  # Bibliographic metadata template
│   ├── provenance.yaml                # Provenance and fixity record template
│   └── acquisition.yaml               # Initial source acquisition log template
│
├── prompts/                           # Model-agnostic LLM prompts for assisted archival tasks
│   ├── source-acquisition.md          # Locating and recording authoritative publication sources
│   ├── source-verification.md         # Auditing publisher identity, URLs, and licensing
│   ├── pdf-conversion.md              # Strict diplomatic transcription from PDF to Markdown
│   ├── metadata-generation.md         # Extracting observable bibliographic metadata
│   └── qa-review.md                   # Comparing transcribed Markdown against source PDFs
│
├── catalogue/                         # Master corpus registries
│   ├── reports.yaml                   # Registry of archived and verified reports in the corpus
│   └── planned-reports.yaml           # Desiderata list of ~40 foundational UK library policy reports
│
├── archive/                           # Preserved document corpus
│   └── reports/
│       └── <report-slug>/             # Individual report package (e.g., sample-report)
│           ├── report.md              # Full diplomatic Markdown edition
│           ├── metadata.yaml          # Canonical bibliographic metadata
│           ├── provenance.yaml        # Fixity, conversion, and review provenance
│           ├── acquisition.yaml       # Point-of-capture acquisition record
│           ├── assets/                # Extracted figures and diagrams (e.g., figure-001.jpg)
│           ├── scans/                 # Optional page scans for OCR verification
│           └── source/                # Unmodified original PDF publication
│
├── scripts/                           # Maintenance and validation utilities
│   ├── new_report.py                  # Scaffolds new report packages from templates
│   ├── compute_fixity.py              # Computes SHA-256 fixity of preserved PDFs
│   ├── validate_all.py                # Runs the complete local validation suite
│   ├── validate_corpus.py             # Package completeness checker
│   ├── validate_metadata.py           # JSON Schema validator
│   ├── validate_markdown.py           # Diplomatic transcription syntax validator
│   ├── verify_checksums.py            # SHA-256 fixity verification
│   ├── check_links.py                 # Source URL resolution check
│   └── requirements.txt               # Validation dependencies (PyYAML, jsonschema)
│
└── .github/
    └── workflows/                     # Automated repository integrity checks
        ├── validate-corpus.yml        # Verifies required files exist for every archived report
        ├── validate-metadata.yml      # Validates metadata.yaml and provenance.yaml against JSON Schemas
        ├── validate-markdown.yml      # Verifies front matter, page markers, and unique paragraph IDs
        ├── verify-checksums.yml       # Checks SHA-256 fixity digests of preserved source files
        └── check-links.yml            # Scheduled and manual checks of recorded source URLs
```

---

## Metadata Model

Archival description is separated into three distinct YAML records per report, ensuring a clean separation between bibliographic description, preservation provenance, and initial capture notes:

1. **Bibliographic Metadata (`metadata.yaml`)**: The canonical descriptive record for the publication, capturing `id`, `title`, `subtitle`, `creators`, `publisher`, `publication_date`, `year`, `publication_place`, `country`, `language`, `document_type`, `pages`, `identifier`, `isbn`, `issn`, `series`, `edition`, `source_url`, `source_pdf`, `rights`, and `review_level`. Validated by [`schemas/metadata.schema.json`](schemas/metadata.schema.json) and documented in [`docs/metadata-schema.md`](docs/metadata-schema.md).
2. **Markdown Front Matter (`report.md`)**: A deliberate subset of core bibliographic fields (`id`, `title`, `year`, plus optional core citation fields) is duplicated in the YAML front matter of every `report.md` file. This duplication is intentional so that each Markdown edition remains self-contained and independently identifiable if copied or cited outside this repository.
3. **Provenance and Fixity (`provenance.yaml` & `acquisition.yaml`)**: Records the technical chain of custody—including `source_url`, `source_pdf_url`, `acquired_date`, `accessed_date`, `source_checksum`, `pdf_sha256`, `download_method`, `conversion_method`, `conversion_date`, and `review_status`. Validated by [`schemas/provenance.schema.json`](schemas/provenance.schema.json) and documented in [`docs/preservation.md`](docs/preservation.md).

---

## Markdown Preservation Model

Every `report.md` file adheres to the specification in [`docs/markdown-specification.md`](docs/markdown-specification.md):

- **YAML Front Matter**: Begins with `---` delimited metadata containing at minimum `id`, `title`, and `year`.
- **Page Markers**: Every page begins with an explicit HTML comment marker—for example, `<!-- PAGE: 34 -->`. Page markers are mandatory, must never be removed, and must never be renumbered.
- **Paragraph Identifiers**: Every paragraph is preceded by a unique bracketed identifier scoped to the current page—for example, `[p34-001]`, `[p34-002]`. Numbering restarts at `001` on each new page.
- **Headings**: Preserve the exact wording, numbering, and hierarchy of the source document without editorial normalisation.
- **Tables**: Represented in standard GitHub Flavored Markdown pipe tables wherever practical, falling back to clean HTML `<table>` markup only when complex row/column spans cannot be represented in Markdown without loss of meaning.
- **Figures**: Referenced relative to the report folder (`![Figure 4. Library Usage Trends](assets/figure-004.jpg)`) followed immediately by the verbatim figure caption in italics (`*Figure 4. Library Usage Trends*`).
- **Footnotes**: Represented using native Markdown footnote syntax (`[^1]`).

The fictional [sample report](archive/reports/sample-report/) is the canonical worked example of every convention above. Copy its patterns rather than the prose of this README.

### Citing an Archived Edition

Cite the original publication first, and its page. Add the paragraph identifier and the archive edition where precision helps:

> Department for Public Culture and Local Services, *Demonstration Public Library Review* (London, 2026), p. 3, para. [p3-003]. Diplomatic edition: UK Public Library Policy Archive, `archive/reports/sample-report/report.md`, commit `<hash>`.

Because page markers are never renumbered and paragraph identifiers are never reassigned, a citation to `[p3-003]` stays valid as transcriptions are corrected. Citing a commit hash pins the exact text you read.

---

## Workflow Summary

Adding a document to the archive follows a strict nine-stage workflow detailed in [`docs/workflow.md`](docs/workflow.md):

1. **Identify source**: Select a candidate policy document from [`catalogue/planned-reports.yaml`](catalogue/planned-reports.yaml) and locate its authoritative publication page.
2. **Verify official publication source**: Confirm publisher authenticity, original release date, and licensing status (e.g., Open Government Licence or UK Government Web Archive provenance).
3. **Download PDF unchanged**: Retrieve the original PDF bit-for-bit into `archive/reports/<slug>/source/` without re-saving, compressing, or modifying the file.
4. **Record acquisition metadata**: Compute the SHA-256 digest and populate `acquisition.yaml` immediately upon capture.
5. **Create Markdown edition**: Transcribe the PDF into `report.md` with exact wording, page markers (`<!-- PAGE: N -->`), and semantic Markdown structure (lists, blockquotes, tables).
6. **Create metadata**: Populate `metadata.yaml` exclusively from directly observable bibliographic evidence on the document and official landing page.
7. **Create provenance metadata**: Record the full acquisition, fixity, and conversion trail in `provenance.yaml`.
8. **Run QA checks**: Audit the Markdown transcription against the source PDF for missing pages, text, tables, figures, or OCR ambiguities, and run the repository validation suite.
9. **Add to catalogue**: Register the completed report in [`catalogue/reports.yaml`](catalogue/reports.yaml) and update its status in [`catalogue/planned-reports.yaml`](catalogue/planned-reports.yaml).

### Running the Checks Locally

The GitHub Actions workflows call the same scripts a maintainer can run before committing:

```bash
python -m venv .venv
. .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r scripts/requirements.txt

# Run the complete validation suite:
python scripts/validate_all.py

# Or run individual checks:
python scripts/validate_corpus.py
python scripts/validate_metadata.py
python scripts/validate_markdown.py
python scripts/verify_checksums.py
python scripts/check_links.py   # needs network access
```

### Ingestion Helper Utilities

For day-to-day maintainer operations:

- **Scaffold a new report package**:
  ```bash
  python scripts/new_report.py <report-slug>
  ```
  Creates `archive/reports/<report-slug>/` with `assets/`, `scans/`, and `source/` subdirectories and initialises `acquisition.yaml`, `metadata.yaml`, `provenance.yaml`, and `report.md` from templates, pre-populating working details if the slug exists in [`catalogue/planned-reports.yaml`](catalogue/planned-reports.yaml).

- **Compute and record PDF fixity**:
  ```bash
  python scripts/compute_fixity.py <report-slug> --write
  ```
  Calculates the SHA-256 digest of the source PDF placed in `source/` and updates `provenance.yaml` and `acquisition.yaml`.

A [`.gitattributes`](.gitattributes) file marks PDFs and images as binary, so Git never alters preserved files on checkout.

---

## Standards Used

The design of this archive is informed by five established bibliographic, archival, and publishing standards:

- **Dublin Core Metadata Element Set (ISO 15836 / DCMI Metadata Terms)**: Provides the conceptual foundation for bibliographic fields in `metadata.yaml` (`title`, `creators`, `publisher`, `publication_date`, `identifier`, `language`, `rights`, `source_url`), ensuring interoperability with research catalogues and institutional repositories.
- **PREMIS Data Dictionary for Preservation Metadata (v3.0)**: Shapes the separation of descriptive metadata from preservation provenance in `provenance.yaml`, specifically modeling Object fixity (`pdf_sha256`, `source_checksum`), Events (`acquired_date`, `conversion_date`, `download_method`, `conversion_method`), and quality review status (`review_status`).
- **Text Encoding Initiative (TEI P5 Guidelines)**: Inspires our diplomatic transcription principles—structural division fidelity, page break milestones (`<pb/>` realized as `<!-- PAGE: N -->`), semantic division anchoring, and explicit uncertainty markers (`<unclear/>` realized as `[UNCERTAIN]`). **Note:** TEI is used for structural inspiration only; documents are stored in plain Markdown, never TEI XML.
- **Open Government Licence (OGL v3.0) & Crown Copyright Framework**: Governs the reuse and attribution framework for UK central government, devolved administration, and Arm's Length Body publications preserved in the corpus.
- **Pandoc Markdown & YAML Metadata Conventions**: Standardises the YAML front matter block, pipe table syntax, and native footnote notation (`[^1]`) so that every `report.md` file remains human-readable in plain text and cleanly parsable by standard scholarly publishing tools.

---

## Future Scope

As the archive grows, priority is given to:

- Completing the ingestion of the core ~40 policy, strategy, and standards reports listed in [`catalogue/planned-reports.yaml`](catalogue/planned-reports.yaml) across England, Scotland, Wales, and Northern Ireland.
- Expanding coverage of historical statutory inquiries and select committee reports on public libraries from 1995 to the present.
- Upgrading transcriptions from initial `converted` status to double-checked `verified` status through line-by-line proofreading against original print or PDF copies.
