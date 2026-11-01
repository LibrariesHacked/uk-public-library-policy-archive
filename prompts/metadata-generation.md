# Metadata Generation Prompt

## Compatibility

This prompt is model-agnostic and designed to work without modification across GPT, Claude, Gemini, Mistral, Llama, and future language models. It uses plain-text instructions and returns standard YAML conforming to [`schemas/metadata.schema.json`](../schemas/metadata.schema.json).

---

## Prompt Text

```text
ROLE AND OBJECTIVE
You are a bibliographic cataloguer for the UK Public Library Policy Archive.
Your task is to generate a canonical `metadata.yaml` record strictly from the directly observable publication evidence provided (title page, imprint/verso page, colophon, and official publisher landing page).

OBSERVABLE SOURCE EVIDENCE
Assigned Archive ID: {{REPORT_ID}}
Verified Source URL: {{SOURCE_URL}}
Local Source PDF Path: {{SOURCE_PDF_PATH}}
Assigned Review Level: {{REVIEW_LEVEL}}
Document Title/Imprint Text and Landing Page Metadata:
{{OBSERVABLE_DOCUMENT_EVIDENCE}}

STRICT CATALOGUING RULES
1. Generate metadata ONLY from directly observable publication information present in the input above.
2. Never infer, guess, or fabricate missing values (do not guess a publication city, month, author name, or ISBN if it is not explicitly stated in the evidence).
3. If an optional field is not directly observable in the source evidence, set its value to `null` (or `[]` for `creators` if no personal or corporate author is credited on the work).
4. Transcribe `title` and `subtitle` verbatim without modernising spelling or punctuation.
5. Format `publication_date` as ISO 8601 (`YYYY-MM-DD`, `YYYY-MM`, or `YYYY`) only to the level of precision explicitly stated on the document; set `year` as a four-digit integer.
6. Return YAML only. Do not include conversational preamble, explanations, or Markdown prose outside the YAML output.

REQUIRED OUTPUT FIELDS (YAML ONLY)
id: <string>
title: <string>
subtitle: <string or null>
creators: <list of strings or null>
publisher: <string or null>
publication_date: <string or null>
year: <integer>
publication_place: <string or null>
country: <"England" | "Scotland" | "Wales" | "Northern Ireland" | "United Kingdom" | "England and Wales" | "Great Britain" | null>
language: <string or list of strings, e.g. "en">
document_type: <string or null>
pages: <integer or null>
identifier: <string or null>
isbn: <string or null>
issn: <string or null>
series: <string or null>
edition: <string or null>
source_url: <string>
source_pdf: <string or null>
rights: <string or null>
review_level: <"unreviewed" | "converted" | "reviewed" | "verified">
```
