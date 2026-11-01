"""Check that every archived report package is complete.

Every directory under archive/reports/ must contain report.md,
metadata.yaml, provenance.yaml and acquisition.yaml. Every entry in
catalogue/reports.yaml must point to an existing package, and every package
should be catalogued.
"""
from common import REQUIRED_FILES, ROOT, Problems, load_yaml, rel, report_dirs


def main() -> None:
    problems = Problems("validate-corpus")
    dirs = report_dirs()

    if not dirs:
        problems.error("archive/reports", "no report packages found")

    for d in dirs:
        for name in REQUIRED_FILES:
            f = d / name
            if not f.is_file():
                problems.error(rel(f), f"missing required file '{name}'")
            elif f.stat().st_size == 0:
                problems.error(rel(f), "required file is empty")
        if not (d / "source").is_dir():
            problems.warn(rel(d), "no source/ directory; the preserved PDF should live in source/")

    catalogue_path = ROOT / "catalogue" / "reports.yaml"
    catalogue = load_yaml(catalogue_path) or {}
    entries = catalogue.get("reports") or []
    catalogued_paths = set()
    for entry in entries:
        path = entry.get("path")
        if not path:
            problems.error(rel(catalogue_path), f"entry '{entry.get('id')}' has no path")
            continue
        catalogued_paths.add(path.rstrip("/"))
        if not (ROOT / path).is_dir():
            problems.error(rel(catalogue_path), f"entry '{entry.get('id')}' points to missing package '{path}'")

    for d in dirs:
        if rel(d) not in catalogued_paths:
            problems.error(rel(d), "package is not registered in catalogue/reports.yaml")

    problems.finish(len(dirs))


if __name__ == "__main__":
    main()

