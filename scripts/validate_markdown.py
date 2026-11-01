"""Validate the diplomatic Markdown editions (report.md).

Fails when:
  - YAML front matter is missing, or lacks id, title or year
  - no <!-- PAGE: N --> markers are present
  - a page number is repeated or goes backwards
  - text other than headings appears before the first page marker
  - a paragraph identifier [pN-MMM] is repeated
  - a paragraph identifier's page does not match the page it sits on
  - a footnote reference has no definition

Warns (without failing) when page numbers skip or paragraph numbering on a
page does not run 001, 002, 003 ...
"""
import re

from common import Problems, rel, report_dirs, split_front_matter

PAGE_RE = re.compile(r"^<!-- PAGE: (\d+) -->$")
PAGE_LOOSE_RE = re.compile(r"<!--\s*PAGE\s*:?.*?-->", re.IGNORECASE)
PARA_RE = re.compile(r"^\[p(\d+)-(\d{3})\]$")
PARA_LOOSE_RE = re.compile(r"^\[p\d+-\d+\]")
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)


def check_report(problems: Problems, path) -> None:
    where = rel(path)
    text = path.read_text(encoding="utf-8")

    fm, body = split_front_matter(text)
    if fm is None:
        problems.error(where, "missing YAML front matter (file must start with '---')")
        return
    if not isinstance(fm, dict):
        problems.error(where, "front matter is not a YAML mapping")
        return
    for key in ("id", "title", "year"):
        if fm.get(key) in (None, ""):
            problems.error(where, f"front matter is missing '{key}'")

    pages: list[int] = []
    seen_ids: set[str] = set()
    current_page = None
    expected_seq = 1
    in_fence = False

    for lineno, raw in enumerate(body.splitlines(), start=1):
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        m = PAGE_RE.match(line)
        if m:
            n = int(m.group(1))
            if n in pages:
                problems.error(where, f"page marker {n} appears more than once")
            elif pages and n < pages[-1]:
                problems.error(where, f"page marker {n} follows page {pages[-1]} (pages must not go backwards)")
            elif pages and n != pages[-1] + 1:
                problems.warn(where, f"page marker jumps from {pages[-1]} to {n}; confirm no pages are missing")
            pages.append(n)
            current_page = n
            expected_seq = 1
            continue
        if PAGE_LOOSE_RE.search(line):
            problems.error(where, f"malformed page marker {line!r}; expected '<!-- PAGE: N -->' on its own line")
            continue

        m = PARA_RE.match(line)
        if m:
            pid = line
            page, seq = int(m.group(1)), int(m.group(2))
            if pid in seen_ids:
                problems.error(where, f"duplicate paragraph identifier {pid}")
            seen_ids.add(pid)
            if current_page is None:
                problems.error(where, f"paragraph identifier {pid} appears before the first page marker")
            elif page != current_page:
                problems.error(where, f"paragraph identifier {pid} is on page {current_page}")
            elif seq != expected_seq:
                # A warning, not a failure: after a QA correction a late-found
                # paragraph keeps the next free number rather than forcing
                # existing identifiers (and citations to them) to change.
                problems.warn(where, f"paragraph identifier {pid} out of sequence; expected "
                                     f"[p{current_page}-{expected_seq:03d}]")
            expected_seq = max(expected_seq, seq + 1)
            continue
        if PARA_LOOSE_RE.match(line):
            problems.error(where, f"malformed paragraph identifier {line!r}; expected [pN-MMM] on its own line")
            continue

        if current_page is None and line and not line.startswith("#"):
            problems.error(where, f"content before the first page marker (body line {lineno})")

    if not pages:
        problems.error(where, "no page markers found (expected '<!-- PAGE: N -->')")
    if not seen_ids:
        problems.error(where, "no paragraph identifiers found (expected '[pN-MMM]')")

    defined = set(FOOTNOTE_DEF_RE.findall(body))
    for ref in sorted(set(FOOTNOTE_REF_RE.findall(body)) - defined):
        problems.error(where, f"footnote [^{ref}] is referenced but never defined")


def main() -> None:
    problems = Problems("validate-markdown")
    reports = [d / "report.md" for d in report_dirs() if (d / "report.md").is_file()]
    for path in reports:
        check_report(problems, path)
    problems.finish(len(reports))


if __name__ == "__main__":
    main()
