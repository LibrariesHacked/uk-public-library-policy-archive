# Preservation, Provenance, and Fixity Guide (`provenance.yaml` & `acquisition.yaml`)

## Purpose

A trustworthy documentary archive requires more than transcribed text: a future scholar or maintainer must be able to verify **where** a document came from, **when** it was captured, **whether** the preserved source file has remained unaltered bit-for-bit, and **how** the diplomatic Markdown transcription was produced and reviewed.

In the **UK Public Library Policy Archive**, preservation and provenance metadata are stored separately from bibliographic description in two files within each report directory (`archive/reports/<report-slug>/`):

1. `acquisition.yaml` — Point-of-capture log recorded immediately when the source document is located and downloaded.
2. `provenance.yaml` — Complete preservation, fixity, conversion, and editorial review record validated against [`schemas/provenance.schema.json`](../schemas/provenance.schema.json).

---

## Standards Alignment

### PREMIS Data Dictionary for Preservation Metadata (v3.0)

Our preservation model adapts core concepts from the **PREMIS (Preservation Metadata: Implementation Strategies)** standard into lightweight, human-readable YAML:

- **PREMIS Object Entity**: Represented by the preserved PDF file in `source/` and its cryptographic fixity digests (`pdf_sha256` and `source_checksum`).
- **PREMIS Event Entities**:
  - *Ingestion / Acquisition Event*: Recorded via `acquired_date`, `accessed_date`, `source_url`, `source_pdf_url`, and `download_method`.
  - *Migration / Transcription Event*: Recorded via `conversion_method` and `conversion_date`.
  - *Quality Assurance / Validation Event*: Recorded via `review_status`.
- **PREMIS Rights Entity**: Documented alongside Dublin Core `rights` in `metadata.yaml` and verified during acquisition in `acquisition.yaml`, with particular attention to the **UK Open Government Licence (OGL v3.0)** and Crown Copyright provisions.

### UK Government Web Archive (UKGWA) and Official Sources

Because many UK public library policy reports published between 1995 and 2015 were originally hosted on legacy domains (`culture.gov.uk`, `mla.gov.uk`, `resource.gov.uk`, `artscouncil.org.uk`, `scotland.gov.uk`, `wales.gov.uk`, `dcalni.gov.uk`), official URLs frequently redirect to or reside within **The National Archives' UK Government Web Archive** (`webarchive.nationalarchives.gov.uk`).

- Always prefer the original publishing body's live domain (`gov.uk`, `gov.scot`, `gov.wales`, `communities-ni.gov.uk`, `artscouncil.org.uk`, `librariesconnected.org.uk`, `scottishlibraries.org`) when the authoritative PDF remains live.
- When the original domain is defunct or the publication has been removed from live government websites, the **UK Government Web Archive** (`webarchive.nationalarchives.gov.uk`) or **British Library / Legal Deposit** capture is treated as an official archival source, and both the snapshot URL and original URL should be noted.
- Never use unofficial third-party mirrors or commercial document-sharing websites when an official publisher or national web archive source exists.

---

## Provenance Schema Reference (`provenance.yaml`)

All `provenance.yaml` files are validated against [`schemas/provenance.schema.json`](../schemas/provenance.schema.json) and support the following fields:

| Field | Type | Obligation | Description |
| :--- | :--- | :--- | :--- |
| `source_url` | string (URI) | **Required** | Canonical URL of the publication landing page or official web archive record. |
| `source_pdf_url` | string (URI / null) | Optional | Direct URL from which the source PDF binary was downloaded. |
| `acquired_date` | string (`YYYY-MM-DD`) | **Required** | ISO 8601 date on which the source file was downloaded into the archive. |
| `accessed_date` | string (`YYYY-MM-DD` / null) | Optional | ISO 8601 date on which the online source landing page was last verified. |
| `source_checksum` | string / null | Optional | Algorithm-prefixed cryptographic digest of the source file (e.g., `sha256:<64-hex-chars>`). |
| `pdf_sha256` | string (64 hex chars / null) | Optional | Raw 64-character lowercase hexadecimal SHA-256 digest of the preserved PDF in `source/`. |
| `download_method` | string / null | Optional | Tool or method used to retrieve the source PDF (e.g., `curl`, `wget`, `browser-direct`, `ukgwa-capture`). |
| `conversion_method` | string | **Required** | Method or pipeline used to produce `report.md` (e.g., `manual`, `ocr-assisted-manual-review`, `pdf-text-extraction-with-manual-verification`). |
| `conversion_date` | string (`YYYY-MM-DD` / null) | Optional | ISO 8601 date on which the diplomatic Markdown transcription was generated. |
| `review_status` | string (enum) | **Required** | Quality assurance status of the transcription: `unreviewed`, `converted`, `reviewed`, or `verified`. |

---

## Fixity and Checksum Verification

### Computing Checksums

Whenever a source PDF is placed in `archive/reports/<report-slug>/source/`, its SHA-256 checksum must be computed immediately and stored unaltered in `provenance.yaml` (and `acquisition.yaml`).

- **Linux / macOS**:
  ```bash
  shasum -a 256 archive/reports/<report-slug>/source/*.pdf
  ```
- **Windows PowerShell**:
  ```powershell
  (Get-FileHash archive/reports/<report-slug>/source/*.pdf -Algorithm SHA256).Hash.ToLower()
  ```

### Fixity Rules

1. **Never modify a source PDF**: Do not re-compress, OCR-overwrite, linearise, crop, or edit PDF metadata inside the `source/` file. The file in `source/` must remain an exact byte-for-byte copy of the published file.
2. **Populate both `pdf_sha256` and `source_checksum`**:
   - `pdf_sha256` stores the 64-character lowercase hex string:
     `"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"`
   - `source_checksum` stores the prefixed form:
     `"sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"`
3. **Automated verification**: The GitHub Actions workflow [`.github/workflows/verify-checksums.yml`](../.github/workflows/verify-checksums.yml) recalculates the SHA-256 digest of every preserved PDF in `archive/reports/*/source/` on every push and pull request and fails if any digest diverges from `provenance.yaml`.

---

## Licensing and Rights Preservation

UK public library policy documents typically fall into one of three licensing categories, which must be recorded accurately in `metadata.yaml` (`rights`) and `acquisition.yaml` (`licence`):

1. **Crown Copyright — Open Government Licence (OGL v3.0)**: Applies to publications issued by central UK Government departments (DCMS, DNH), the Scottish Government, the Welsh Government, Northern Ireland Executive departments, and Crown bodies.
2. **Non-Departmental Public Body / Sector Body Open Licences**: Publications by bodies such as Arts Council England, MLA, SLIC, or Libraries Connected that carry explicit Open Government Licence, Creative Commons (e.g., `CC BY 4.0`), or open reproduction permissions for research and policy preservation.
3. **All Rights Reserved / Specific Permission Required**: If a historical third-party report or charity publication does not carry an open licence permitting full-text redistribution, record the bibliographic metadata and provenance in the catalogue and confirm rights clearance before committing redistributable binaries.
