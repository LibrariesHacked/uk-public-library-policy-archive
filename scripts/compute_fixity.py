"""Compute and record SHA-256 fixity digests for a report package.

Usage:
  python scripts/compute_fixity.py <report-slug> [--write]

Finds the source PDF in archive/reports/<report-slug>/source/, calculates
its SHA-256 checksum, and either prints the values or updates provenance.yaml
and acquisition.yaml in place.
"""
import argparse
import hashlib
import sys
from pathlib import Path

from common import REPORTS_DIR, load_yaml


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest().lower()


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute source PDF fixity for an archival package.")
    parser.add_argument("slug", help="Report package directory slug under archive/reports/")
    parser.add_argument("--write", action="store_true", help="Update provenance.yaml and acquisition.yaml directly")
    args = parser.parse_args()

    report_dir = REPORTS_DIR / args.slug
    if not report_dir.is_dir():
        print(f"Error: report directory not found: {report_dir}", file=sys.stderr)
        sys.exit(1)

    source_dir = report_dir / "source"
    pdfs = list(source_dir.glob("*.pdf")) if source_dir.is_dir() else []
    if not pdfs:
        print(f"Error: no PDF found in {source_dir}", file=sys.stderr)
        sys.exit(1)
    if len(pdfs) > 1:
        print(f"Warning: multiple PDFs found in {source_dir}: {[p.name for p in pdfs]}. Using {pdfs[0].name}")

    pdf_path = pdfs[0]
    digest = sha256_file(pdf_path)
    print(f"File:        {pdf_path.relative_to(report_dir.parent.parent)}")
    print(f"Size:        {pdf_path.stat().st_size:,} bytes")
    print(f"SHA-256:     {digest}")
    print(f"Checksum:    sha256:{digest}")

    if args.write:
        # Update provenance.yaml
        prov_path = report_dir / "provenance.yaml"
        if prov_path.is_file():
            content = prov_path.read_text(encoding="utf-8")
            import re
            content = re.sub(r'pdf_sha256:\s*.*', f'pdf_sha256: "{digest}"', content)
            content = re.sub(r'source_checksum:\s*.*', f'source_checksum: "sha256:{digest}"', content)
            prov_path.write_text(content, encoding="utf-8")
            print(f"Updated {prov_path.name}")

        # Update acquisition.yaml
        acq_path = report_dir / "acquisition.yaml"
        if acq_path.is_file():
            content = acq_path.read_text(encoding="utf-8")
            import re
            content = re.sub(r'pdf_sha256:\s*.*', f'pdf_sha256: "{digest}"', content)
            content = re.sub(r'local_file:\s*.*', f'local_file: "source/{pdf_path.name}"', content)
            acq_path.write_text(content, encoding="utf-8")
            print(f"Updated {acq_path.name}")

        # Update metadata.yaml source_pdf if default
        meta_path = report_dir / "metadata.yaml"
        if meta_path.is_file():
            content = meta_path.read_text(encoding="utf-8")
            import re
            content = re.sub(r'source_pdf:\s*"source/report\.pdf"', f'source_pdf: "source/{pdf_path.name}"', content)
            meta_path.write_text(content, encoding="utf-8")
            print(f"Updated {meta_path.name}")


if __name__ == "__main__":
    main()

