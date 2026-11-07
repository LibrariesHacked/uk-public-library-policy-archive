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


def locate_sources(d, acquisition: dict, metadata: dict) -> list:
    for candidate in (acquisition.get("local_file"), metadata.get("source_pdf")):
        if isinstance(candidate, list):
            paths = [d / c for c in candidate if not str(c).startswith(("http://", "https://"))]
            if paths and all(p.is_file() for p in paths):
                return paths
        elif candidate and not str(candidate).startswith(("http://", "https://")):
            p = d / candidate
            if p.is_file():
                return [p]
    if (d / "source").is_dir():
        return sorted((d / "source").glob("*.pdf"))
    return []


def normalize_checksum(val):
    if isinstance(val, list):
        return [normalize_checksum(v) for v in val]
    if not isinstance(val, str):
        return None
    val = val.lower().strip()
    if val.startswith("sha256:"):
        val = val[7:]
    return val


def main() -> None:
    problems = Problems("verify-checksums")
    verified = 0

    for d in report_dirs():
        prov = load(d / "provenance.yaml")
        acq = load(d / "acquisition.yaml")
        meta = load(d / "metadata.yaml")

        prov_hash = normalize_checksum(prov.get("pdf_sha256") or prov.get("source_checksum"))
        acq_hash = normalize_checksum(acq.get("pdf_sha256"))

        expected_hashes = prov_hash if prov_hash is not None else acq_hash
        if not expected_hashes:
            problems.warn(rel(d), "no checksum recorded; fixity cannot be verified")
            continue

        sources = locate_sources(d, acq, meta)
        if not sources:
            problems.error(rel(d), "checksum recorded but preserved file(s) not found in source/")
            continue

        if isinstance(expected_hashes, list):
            if len(expected_hashes) != len(sources):
                problems.error(rel(d), f"recorded {len(expected_hashes)} checksum(s) but found {len(sources)} file(s)")
                continue
            all_ok = True
            for src, exp in zip(sources, expected_hashes):
                act = sha256(src)
                if exp != act:
                    problems.error(rel(src), f"expected {exp} but file digest is {act}")
                    all_ok = False
                else:
                    print(f"OK  {rel(src)}  sha256:{act}")
            if all_ok:
                verified += 1
        else:
            if len(sources) != 1:
                problems.error(rel(d), f"recorded 1 checksum but found {len(sources)} files in source/")
                continue
            src = sources[0]
            act = sha256(src)
            if expected_hashes != act:
                problems.error(rel(src), f"expected {expected_hashes} but file digest is {act}")
            else:
                print(f"OK  {rel(src)}  sha256:{act}")
                verified += 1

    problems.finish(verified)


if __name__ == "__main__":
    main()

