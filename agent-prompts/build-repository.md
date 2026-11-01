BUILD REPOSITORY: UK PUBLIC LIBRARY POLICY ARCHIVE

Create a complete GitHub repository named:

uk-public-library-policy-archive

PURPOSE

This repository is a preservation archive for UK public library policy, strategy, standards, consultation and review documents published from approximately 1995 onwards.

The repository is a source archive, not a search product.

Prioritise:

- preservation
- provenance
- citability
- transparency
- reproducibility
- long-term maintainability

Assume a single maintainer.

Keep solutions simple.

CRITICAL REQUIREMENT

Preserve source materials.

DO NOT add:

- AI summaries
- semantic enrichment
- topic tags
- embeddings
- vector databases
- knowledge graphs
- recommendation systems
- AI interpretations
- search indexes

The repository exists solely to preserve and document source materials.

CORE PRINCIPLES

FIDELITY

The source document remains authoritative.

Never:

- paraphrase
- rewrite
- modernise
- improve wording
- normalise language

Converted documents must preserve source content exactly.

TRANSPARENCY

Every archived document must record:

- source URL
- source PDF URL
- acquisition date
- conversion method
- review status

CITABILITY

All Markdown editions must support page-level citation.

REPRODUCIBILITY

A future maintainer should be able to recreate an archived record from repository documentation alone.

STANDARDS

Document how the following standards influence repository design:

- Dublin Core (bibliographic metadata concepts)
- PREMIS (preservation and provenance concepts)
- TEI (structural inspiration only, do not use TEI XML)
- Open Government Licence
- Pandoc Metadata Conventions

TEI should influence structure only.

Do not store documents as TEI XML.

REPOSITORY STRUCTURE

/
│
├── README.md
├── CITATION.cff
├── .gitignore
│
├── docs/
│   ├── metadata-schema.md
│   ├── markdown-specification.md
│   ├── preservation.md
│   └── workflow.md
│
├── schemas/
│   ├── metadata.schema.json
│   └── provenance.schema.json
│
├── templates/
│   ├── report.md
│   ├── metadata.yaml
│   ├── provenance.yaml
│   └── acquisition.yaml
│
├── prompts/
│   ├── source-acquisition.md
│   ├── source-verification.md
│   ├── pdf-conversion.md
│   ├── metadata-generation.md
│   └── qa-review.md
│
├── catalogue/
│   ├── reports.yaml
│   └── planned-reports.yaml
│
├── archive/
│   └── reports/
│
└── .github/
    └── workflows/
        ├── validate-corpus.yml
        ├── validate-metadata.yml
        ├── validate-markdown.yml
        ├── verify-checksums.yml
        └── check-links.yml

README REQUIREMENTS

Create a concise but complete README.

Include:

- purpose
- principles
- repository structure
- metadata model
- markdown preservation model
- workflow summary
- standards used
- future scope
- non-goals

The README should feel like a digital humanities archive rather than a software project.

METADATA DESIGN

Canonical metadata must be stored in:

metadata.yaml

A duplicate subset must also appear in Markdown front matter.

This duplication is intentional.

Markdown files should remain independently useful outside this repository.

METADATA FIELDS

Support:

id:
title:
subtitle:
creators:
publisher:
publication_date:
year:
publication_place:
country:
language:
document_type:
pages:
identifier:
isbn:
issn:
series:
edition:
source_url:
source_pdf:
rights:
review_level:

Provide a JSON Schema.

PROVENANCE METADATA

Store separately:

source_url:
source_pdf_url:
acquired_date:
accessed_date:
source_checksum:
pdf_sha256:
download_method:
conversion_method:
conversion_date:
review_status:

Provide a JSON Schema.

MARKDOWN PRESERVATION FORMAT

All archived reports must use:

Front Matter

---
id:
title:
year:
---

Page Markers

<!-- PAGE: 34 -->

Mandatory.

Must never be removed.

Must never be renumbered.

Paragraph Identifiers

Every paragraph receives a stable identifier.

Example:

[p34-001]

Libraries provide...

[p34-002]

Public libraries support...

Paragraph numbering restarts on each page.

HEADINGS

Preserve hierarchy exactly.

Do not improve.

Do not rewrite.

Do not modernise.

TABLES

Convert to Markdown where practical.

Use HTML only when genuinely necessary.

FIGURES

Represent as:

assets/figure-004.jpg

*Figure 4. Library Usage Trends*

FOOTNOTES

Use native Markdown footnotes.

WORKFLOW

Document and implement:

1. Identify source.
2. Verify official publication source.
3. Download PDF unchanged.
4. Record acquisition metadata.
5. Create Markdown edition.
6. Create metadata.
7. Create provenance metadata.
8. Run QA checks.
9. Add to catalogue.

PROMPT LIBRARY

Create model-agnostic prompts.

Prompts must work with:

- GPT
- Claude
- Gemini
- Mistral
- Llama
- future models

Avoid vendor-specific features.

SOURCE ACQUISITION PROMPT

Requirements:

- locate authoritative source
- prefer official publisher
- record canonical URL
- record direct PDF URL
- record licence
- record access date

Rules:

- never invent URLs
- never use mirrors when official source exists

Output YAML only.

SOURCE VERIFICATION PROMPT

Validate:

- publisher identity
- URL authenticity
- PDF availability
- licence information
- publication date

Output findings only.

Do not invent information.

PDF CONVERSION PROMPT

Most important prompt.

Must explicitly require:

- preserve wording exactly
- preserve structure exactly
- preserve page boundaries
- preserve tables
- preserve figures
- preserve appendices
- preserve footnotes
- preserve contents pages
- preserve references

Never:

- summarise
- paraphrase
- modernise
- infer missing text
- silently correct OCR

When uncertain:

[UNCERTAIN]

must be used.

Include these statements verbatim:

"Preservation takes precedence over readability."

"Preserve uncertainty rather than invent certainty."

METADATA GENERATION PROMPT

Generate metadata only from directly observable publication information.

Return YAML only.

Never infer missing values.

QUALITY ASSURANCE PROMPT

Compare:

- source PDF
- generated Markdown

Report:

- missing pages
- missing text
- missing tables
- missing figures
- heading hierarchy issues
- page numbering issues
- OCR uncertainty

Report findings only.

Do not modify content.

CATALOGUE

Create:

reports:

and

planned_reports:

Populate planned_reports with approximately 40 significant UK public library policy documents.

Include at minimum:

ENGLAND

- Public Library Standards (2001)
- Comprehensive and Efficient? (2002)
- Framework for the Future (2003)
- Envisioning the Library of the Future (2013)
- Independent Library Report for England (2014)
- Libraries Deliver (2016)
- Libraries Deliver Action Plan
- Libraries Deliver: Ambition Refresh

SCOTLAND

- Ambition & Opportunity (2015)
- Ambition & Opportunity refreshes

WALES

- Libraries Inspire
- Welsh Public Library Standards Framework

NORTHERN IRELAND

- Delivering Tomorrow's Library

LIBRARIES CONNECTED

- Universal Offer documents
- Strategic plans

DIGITAL PROGRAMMES

- Single Digital Presence reports

BUSINESS & IP CENTRES

- Impact reports

SAMPLE REPORT

Create a complete fictional report.

Do not use copyrighted material.

Demonstrate:

- front matter
- metadata.yaml
- provenance.yaml
- acquisition.yaml
- page markers
- paragraph identifiers
- tables
- figures
- footnotes
- citations
- multi-page layout

This sample report should become the canonical implementation example for the repository.

GITHUB ACTIONS

Implement maintainable workflows.

validate-corpus.yml

Verify every report contains:

- report.md
- metadata.yaml
- provenance.yaml
- acquisition.yaml

Fail on missing files.

validate-metadata.yml

Validate metadata against JSON Schema.

Fail on missing required fields.

validate-markdown.yml

Validate:

- front matter exists
- page markers exist
- paragraph identifiers are unique

Fail on violations.

verify-checksums.yml

Verify stored checksums when present.

check-links.yml

Validate source URLs.

Support:

- scheduled execution
- manual execution

CITATION.CFF

Create a valid citation file.

Repository title:

UK Public Library Policy Archive

SUCCESS CRITERIA

Generate all repository files with realistic content rather than placeholders.

The repository should feel like:

- a digital humanities archive
- a preservation project
- a scholarly source repository

It should not feel like:

- a software product
- an AI project
- a search engine
- a semantic knowledge graph

Prioritise:

- preservation
- provenance
- fidelity
- reproducibility
- maintainability

Produce a complete, usable repository ready for GitHub.