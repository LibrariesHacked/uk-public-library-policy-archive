"""Scaffold a new report package under archive/reports/<slug>/.

Usage:
  python scripts/new_report.py <report-slug>

Sets up directory structure (assets/, scans/, source/) and initialises
acquisition.yaml, metadata.yaml, provenance.yaml, and report.md from templates.
If <report-slug> exists in catalogue/planned-reports.yaml, working title and
metadata will be pre-populated.
"""
import argparse
import datetime
import shutil
import sys
from pathlib import Path

from common import REPORTS_DIR, ROOT, load_yaml

TEMPLATES_DIR = ROOT / "templates"
PLANNED_PATH = ROOT / "catalogue" / "planned-reports.yaml"


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new report package in the archive.")
    parser.add_argument("slug", help="Unique hyphenated report slug (e.g. dcms-framework-for-the-future-2003)")
    args = parser.parse_args()

    slug = args.slug.strip().lower()
    target_dir = REPORTS_DIR / slug

    if target_dir.exists():
        print(f"Error: directory already exists: {target_dir}", file=sys.stderr)
        sys.exit(1)

    # Check planned-reports.yaml for matching working record
    planned_entry = None
    if PLANNED_PATH.is_file():
        planned_data = load_yaml(PLANNED_PATH) or {}
        for item in planned_data.get("planned_reports") or []:
            if item.get("id") == slug:
                planned_entry = item
                break

    today = datetime.date.today().isoformat()

    # Create directories
    target_dir.mkdir(parents=True)
    (target_dir / "assets").mkdir()
    (target_dir / "scans").mkdir()
    (target_dir / "source").mkdir()

    # 1. acquisition.yaml
    acq_tmpl = (TEMPLATES_DIR / "acquisition.yaml").read_text(encoding="utf-8")
    acq_content = acq_tmpl.replace("2026-01-01", today)
    if planned_entry:
        if planned_entry.get("publisher"):
            acq_content = acq_content.replace('"Official Publishing Body"', f'"{planned_entry["publisher"]}"')
    (target_dir / "acquisition.yaml").write_text(acq_content, encoding="utf-8")

    # 2. metadata.yaml
    meta_tmpl = (TEMPLATES_DIR / "metadata.yaml").read_text(encoding="utf-8")
    meta_content = meta_tmpl.replace("publisher-short-title-yyyy", slug)
    meta_content = meta_content.replace("2026-01-01", today)
    if planned_entry:
        if planned_entry.get("title"):
            meta_content = meta_content.replace('"Exact Title from Source Document"', f'"{planned_entry["title"]}"')
        if planned_entry.get("year"):
            meta_content = meta_content.replace("year: 2026", f"year: {planned_entry['year']}")
        if planned_entry.get("publisher"):
            meta_content = meta_content.replace('"Official Publishing Body"', f'"{planned_entry["publisher"]}"')
        if planned_entry.get("country"):
            meta_content = meta_content.replace('country: "England"', f'country: "{planned_entry["country"]}"')
        if planned_entry.get("document_type"):
            meta_content = meta_content.replace('document_type: "policy-paper"', f'document_type: "{planned_entry["document_type"]}"')
    (target_dir / "metadata.yaml").write_text(meta_content, encoding="utf-8")

    # 3. provenance.yaml
    prov_tmpl = (TEMPLATES_DIR / "provenance.yaml").read_text(encoding="utf-8")
    prov_content = prov_tmpl.replace("2026-01-01", today)
    (target_dir / "provenance.yaml").write_text(prov_content, encoding="utf-8")

    # 4. report.md
    rpt_tmpl = (TEMPLATES_DIR / "report.md").read_text(encoding="utf-8")
    rpt_content = rpt_tmpl.replace("publisher-short-title-yyyy", slug)
    if planned_entry:
        if planned_entry.get("title"):
            rpt_content = rpt_content.replace('"Exact Title from Source Document"', f'"{planned_entry["title"]}"')
            rpt_content = rpt_content.replace("# Exact Title from Source Document", f"# {planned_entry['title']}")
        if planned_entry.get("year"):
            rpt_content = rpt_content.replace("year: 2026", f"year: {planned_entry['year']}")
        if planned_entry.get("publisher"):
            rpt_content = rpt_content.replace('"Official Publishing Body"', f'"{planned_entry["publisher"]}"')
    (target_dir / "report.md").write_text(rpt_content, encoding="utf-8")

    print(f"Created new report package: archive/reports/{slug}/")
    if planned_entry:
        print(f"  Pre-populated working info from planned_reports: '{planned_entry.get('title')}'")
    print("\nNext steps according to docs/workflow.md:")
    print("  1. Verify official source URL and licensing (Stage 2)")
    print(f"  2. Download unchanged PDF into: archive/reports/{slug}/source/<filename>.pdf (Stage 3)")
    print(f"  3. Compute and write fixity:    python scripts/compute_fixity.py {slug} --write (Stage 4)")
    print(f"  4. Transcribe into:             archive/reports/{slug}/report.md (Stage 5)")
    print("  5. Verify observable metadata:  metadata.yaml and provenance.yaml (Stages 6 & 7)")
    print("  6. Run validation:              python scripts/validate_all.py (Stage 8)")
    print("  7. Register in catalogue:       catalogue/reports.yaml (Stage 9)")


if __name__ == "__main__":
    main()

