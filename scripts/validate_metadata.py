"""Validate metadata.yaml and provenance.yaml against the JSON Schemas.

Also checks that the front matter subset duplicated in report.md agrees with
the canonical metadata.yaml, and that the catalogue entry agrees on id.
"""
import json

from jsonschema import Draft202012Validator, FormatChecker

from common import ROOT, SCHEMAS_DIR, Problems, load_yaml, rel, report_dirs, split_front_matter

# Fields that, when present in report.md front matter, must equal metadata.yaml.
SHARED_FIELDS = ("id", "title", "subtitle", "publisher", "year", "source_url", "review_level")


def validator(name: str) -> Draft202012Validator:
    schema = json.loads((SCHEMAS_DIR / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_file(problems: Problems, v: Draft202012Validator, path) -> dict | None:
    if not path.is_file():
        problems.error(rel(path), "file not found")
        return None
    data = load_yaml(path)
    if not isinstance(data, dict):
        problems.error(rel(path), "file does not contain a YAML mapping")
        return None
    for err in sorted(v.iter_errors(data), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "(root)"
        problems.error(rel(path), f"{loc}: {err.message}")
    return data


def main() -> None:
    problems = Problems("validate-metadata")
    meta_v = validator("metadata.schema.json")
    prov_v = validator("provenance.schema.json")
    dirs = report_dirs()
    catalogue = load_yaml(ROOT / "catalogue" / "reports.yaml") or {}
    catalogue_by_path = {e.get("path", "").rstrip("/"): e for e in catalogue.get("reports") or []}
    seen_ids: dict[str, str] = {}

    for d in dirs:
        meta = validate_file(problems, meta_v, d / "metadata.yaml")
        prov = validate_file(problems, prov_v, d / "provenance.yaml")
        if not meta:
            continue

        rid = meta.get("id")
        if rid in seen_ids:
            problems.error(rel(d / "metadata.yaml"), f"id '{rid}' is also used by {seen_ids[rid]}")
        seen_ids[rid] = rel(d)

        if prov and meta.get("source_url") != prov.get("source_url"):
            problems.error(rel(d / "provenance.yaml"), "source_url differs from metadata.yaml")
        if prov and meta.get("review_level") != prov.get("review_status"):
            problems.warn(rel(d / "provenance.yaml"),
                          f"review_status '{prov.get('review_status')}' differs from "
                          f"metadata review_level '{meta.get('review_level')}'")

        report = d / "report.md"
        if report.is_file():
            fm, _ = split_front_matter(report.read_text(encoding="utf-8"))
            if isinstance(fm, dict):
                for key in SHARED_FIELDS:
                    if key in fm and fm[key] != meta.get(key):
                        problems.error(rel(report), f"front matter '{key}' ({fm[key]!r}) differs from "
                                                    f"metadata.yaml ({meta.get(key)!r})")

        entry = catalogue_by_path.get(rel(d))
        if entry and entry.get("id") != rid:
            problems.error("catalogue/reports.yaml", f"entry for {rel(d)} has id '{entry.get('id')}', "
                                                     f"metadata.yaml has '{rid}'")

    problems.finish(len(dirs))


if __name__ == "__main__":
    main()

