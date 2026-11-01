"""Verify the SHA-256 fixity of preserved source files.

For each report, any checksum recorded in provenance.yaml (pdf_sha256,
source_checksum) or acquisition.yaml (pdf_sha256) is compared with the actual
digest of the preserved PDF. Reports with no recorded checksum are reported
as warnings, not failures: checksums are verified "when present".

The preserved file is located, in order of preference, from
acquisition.yaml local_file, metadata.yaml source_pdf, or the single PDF in
source/.
"""
import hashlib

from common import Problems, load_yaml, rel, report_dirs


def sha256(path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load(path) -> dict:
    return (load_yaml(path) or {}) if path.is_file() else {}


def locate_source(d, acquisition: dict, metadata: dict):
    for candidate in (acquisition.get("local_file"), metadata.get("source_pdf")):
        if candidate and not str(candidate).startswith(("http://", "https://")):
            return d / candidate
    pdfs = sorted((d / "source").glob("*.pdf")) if (d / "source").is_dir() else []
    return pdfs[0] if len(pdfs) == 1 else None


def main() -> None:
    problems = Problems("verify-checksums")
    verified = 0

    for d in report_dirs():
        prov = load(d / "provenance.yaml")
        acq = load(d / "acquisition.yaml")
        meta = load(d / "metadata.yaml")

        recorded = {}
        if prov.get("pdf_sha256"):
            recorded["provenance.yaml pdf_sha256"] = str(prov["pdf_sha256"]).lower()
        if prov.get("source_checksum"):
            value = str(prov["source_checksum"]).lower()
            if ":" in value:
                algo, value = value.split(":", 1)
                if algo != "sha256":
                    problems.warn(rel(d / "provenance.yaml"), f"source_checksum uses unsupported algorithm '{algo}'")
                    value = None
            if value:
                recorded["provenance.yaml source_checksum"] = value
        if acq.get("pdf_sha256"):
            recorded["acquisition.yaml pdf_sha256"] = str(acq["pdf_sha256"]).lower()

        if not recorded:
            problems.warn(rel(d), "no checksum recorded; fixity cannot be verified")
            continue

        source = locate_source(d, acq, meta)
        if source is None or not source.is_file():
            problems.error(rel(d), f"checksum recorded but preserved file not found ({source and rel(source)})")
            continue

        actual = sha256(source)
        for label, expected in recorded.items():
            if expected != actual:
                problems.error(rel(source), f"{label} is {expected} but file digest is {actual}")
        if all(v == actual for v in recorded.values()):
            print(f"OK  {rel(source)}  sha256:{actual}")
            verified += 1

    problems.finish(verified)


if __name__ == "__main__":
    main()

