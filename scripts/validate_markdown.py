"""Validate the diplomatic Markdown editions (report.md).

Fails when:
  - YAML front matter is missing, or lacks id, title or year
  - no <!-- PAGE: N --> markers are present
  - a page number is repeated or goes backwards
  - a page marker is malformed
  - text other than headings appears before the first page marker
  - a footnote reference has no definition

Warns (without failing) when page numbers skip.
"""
import re
import sys
from pathlib import Path

from common import Problems, rel, report_dirs, split_front_matter

PAGE_RE = re.compile(r"<!-- PAGE: (\d+) -->")
PAGE_LOOSE_RE = re.compile(r"<!--\s*PAGE\s*:?.*?-->", re.IGNORECASE)
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)


def check_report(problems: Problems, path: Path) -> None:
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
    current_page = None
    in_fence = False

    for lineno, raw in enumerate(body.splitlines(), start=1):
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        found_markers = list(PAGE_RE.finditer(line))
        if found_markers:
            for m in found_markers:
                n = int(m.group(1))
                if n in pages:
                    problems.error(where, f"page marker {n} appears more than once")
                elif pages and n < pages[-1]:
                    problems.error(where, f"page marker {n} follows page {pages[-1]} (pages must not go backwards)")
                elif pages and n != pages[-1] + 1:
                    problems.warn(where, f"page marker jumps from {pages[-1]} to {n}; confirm no pages are missing")
                pages.append(n)
                current_page = n
            continue

        if PAGE_LOOSE_RE.search(line):
            problems.error(where, f"malformed page marker in {line!r}; expected '<!-- PAGE: N -->'")
            continue

        if current_page is None and line and not line.startswith("#"):
            problems.error(where, f"content before the first page marker (body line {lineno})")

    if not pages:
        problems.error(where, "no page markers found (expected '<!-- PAGE: N -->')")

    # Footnote integrity: every [^n] in body must have a matching [^n]: definition
    defs = set(FOOTNOTE_DEF_RE.findall(body))
    refs = set(FOOTNOTE_REF_RE.findall(body))
    for ref in refs:
        if ref not in defs:
            problems.error(where, f"footnote reference '[^{ref}]' has no matching '[^{ref}]:' definition")

    # Asset verification and structural checks
    report_dir = path.parent
    IMAGE_RE = re.compile(r"!\[[^\]]*\]\((assets/[^)]+)\)")
    for img_ref in IMAGE_RE.findall(body):
        asset_file = report_dir / img_ref
        if not asset_file.is_file():
            problems.error(where, f"referenced image asset '{img_ref}' does not exist on disk")

    # Lint: check for bare numbered list items, standalone page markers, and unformatted/misplaced footnotes
    body_lines = body.splitlines()

    # Find the line of the last page marker to verify footnotes are at the end
    last_page_lineno = 0
    for idx, raw in enumerate(body_lines, start=1):
        if PAGE_RE.search(raw):
            last_page_lineno = idx

    for lineno, raw in enumerate(body_lines, start=1):
        s_line = raw.strip()

        # Unformatted footnote checks: e.g. "1 http://..." or "10 https://..."
        if re.match(r"^\d+\s+https?://", s_line):
            problems.error(where, f"line {lineno}: unformatted footnote definition '{s_line[:40]}...'; format as '[^N]: <URL>' and consolidate under '## Footnotes' at the end of the document")
        elif re.search(r"\b\d+\s+https?://.*?\b\d+\s+https?://", s_line):
            problems.error(where, f"line {lineno}: multiple unformatted footnotes merged on single line; separate and format as '[^N]: <URL>' under '## Footnotes'")

        # Consolidated footnotes check: all [^n]: definitions should appear after the last page content
        fn_match = re.match(r"^\[\^([^\]]+)\]:", s_line)
        if fn_match and lineno < last_page_lineno:
            problems.warn(where, f"line {lineno}: footnote definition '[^{fn_match.group(1)}]:' placed mid-document (before last page marker line {last_page_lineno}); consolidate all footnote definitions at the end of the report under '## Footnotes'")

        # Bare ACTION / ACTIONS panel title check: e.g. "ACTION" or "ACTIONS" as standalone unstyled line
        if s_line in ("ACTION", "ACTIONS"):
            problems.warn(where, f"line {lineno}: standalone unstyled '{s_line}'; format action callout boxes as blockquotes (e.g. '> ### {s_line}') with underlined subheadings ('> <u>Central government</u>')")

        # Isolated long bullet check: prose paragraphs mistakenly formatted with a list marker
        if re.match(r"^[-*]\s+", s_line) and not s_line.startswith(">") and len(s_line) > 120:
            prev_bullet = False
            p = lineno - 2
            while p >= 0:
                p_line = body_lines[p].strip()
                if not p_line or p_line.startswith("<!-- PAGE:"):
                    p -= 1
                    continue
                if re.match(r"^[-*]\s+", p_line):
                    prev_bullet = True
                break

            next_bullet = False
            n = lineno
            while n < len(body_lines):
                n_line = body_lines[n].strip()
                if not n_line or n_line.startswith("<!-- PAGE:"):
                    n += 1
                    continue
                if re.match(r"^[-*]\s+", n_line):
                    next_bullet = True
                break

            if not prev_bullet and not next_bullet:
                problems.warn(where, f"line {lineno}: isolated long bullet point '{s_line[:40]}...'; appears to be a prose paragraph erroneously prefixed with a list marker")

        # Standalone page marker check
        if re.match(r"^<!-- PAGE: \d+ -->$", s_line):
            # Check preceding non-empty line
            prev_idx = lineno - 2
            while prev_idx >= 0 and not body_lines[prev_idx].strip():
                prev_idx -= 1
            if prev_idx >= 0:
                prev_line = body_lines[prev_idx].strip()
                # If prev_line doesn't end in punctuation or markup, it may be a mid-sentence break
                if not re.search(r"[.!?:\'\"\*\`\>\]\)”’]$", prev_line) and not prev_line.startswith(("#", "-", "*")):
                    problems.warn(where, f"line {prev_idx + 1} appears to end mid-sentence before standalone page marker on line {lineno}; place marker inline ('word <!-- PAGE: N --> word') to prevent paragraph fracturing in CommonMark previews")

    # Check for run-on bold numbered clauses on adjacent lines: e.g. "**1.** ...\n**2.** ..."
    # In CommonMark, adjacent bold lines without blank lines collapse into a single run-on paragraph.
    for idx in range(len(body_lines) - 1):
        l1 = body_lines[idx].strip()
        l2 = body_lines[idx + 1].strip()
        if re.match(r"^\*\*\d+\.\*\*", l1) and re.match(r"^\*\*\d+\.\*\*", l2):
            problems.error(where, f"lines {idx+1}-{idx+2}: adjacent bold numbered clauses without separating blank lines; CommonMark collapses these into a single run-on paragraph. Use standard ordered list syntax ('1. ', '2. ') or add blank lines between bold clauses.")

    # Check for broken or pseudo-ordered lists:
    # A genuine ordered list starts with 1. and increments sequentially (1., 2., 3., ...) without intervening headings.
    in_code_block = False
    items = []
    for idx, raw in enumerate(body_lines, 1):
        s = raw.strip()
        if s.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if s.startswith("#"):
            items.append((idx, "HEADING", 0, s))
            continue
        m = re.match(r"^(\d+)\.\s+(.*)", s)
        if m:
            items.append((idx, "NUM", int(m.group(1)), s))

    valid_ordered_lines = set()
    i = 0
    while i < len(items):
        idx, kind, num, s = items[i]
        if kind == "NUM" and num == 1:
            seq = [items[i]]
            j = i + 1
            expected = 2
            while j < len(items):
                j_idx, j_kind, j_num, j_s = items[j]
                if j_kind == "HEADING":
                    break
                if j_num == expected:
                    seq.append(items[j])
                    expected += 1
                    j += 1
                elif j_num == 1:
                    break
                else:
                    j += 1
            if len(seq) >= 2:
                for valid_item in seq:
                    valid_ordered_lines.add(valid_item[0])
        i += 1

    for idx, kind, num, s in items:
        if kind == "NUM" and idx not in valid_ordered_lines:
            problems.warn(where, f"line {idx}: bare numbered list item '{s[:25]}...'; genuine ordered lists must start at 1 and increment sequentially without intervening headings. Use bold numbering ('**N.**') for policy clauses.")


def main() -> None:
    problems = Problems("validate-markdown")
    if len(sys.argv) > 1:
        reports = [Path(p) for p in sys.argv[1:]]
    else:
        reports = [d / "report.md" for d in report_dirs() if (d / "report.md").is_file()]
    for path in reports:
        check_report(problems, path)
    problems.finish(len(reports))


if __name__ == "__main__":
    main()
