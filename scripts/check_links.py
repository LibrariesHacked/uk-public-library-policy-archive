"""Check that recorded source URLs still resolve.

Collects source_url and source_pdf_url values from every metadata.yaml,
provenance.yaml and acquisition.yaml and requests each one. Uses only the
standard library so it runs anywhere.

URLs on reserved documentation domains (example.org, example.com,
example.net; RFC 2606) are skipped: they belong to the fictional sample.

A broken link does not mean the archive is wrong. The preserved PDF in
source/ remains authoritative. Record a UK Government Web Archive capture as
an additional source rather than overwriting the original URL.
"""
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse

from common import Problems, load_yaml, rel, report_dirs

URL_FIELDS = ("source_url", "source_pdf_url")
FILES = ("metadata.yaml", "provenance.yaml", "acquisition.yaml")
SKIP_HOSTS = {"example.org", "example.com", "example.net"}
USER_AGENT = "uk-public-library-policy-archive link check (+https://github.com/LibrariesHacked/uk-public-library-policy-archive)"
TIMEOUT = 30


def request(url: str, method: str) -> int:
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.status


def check(url: str) -> tuple[bool, str]:
    last = ""
    for attempt in range(3):
        try:
            try:
                status = request(url, "HEAD")
            except urllib.error.HTTPError as e:
                if e.code in (403, 405, 501):  # some servers refuse HEAD
                    status = request(url, "GET")
                else:
                    raise
            return True, str(status)
        except urllib.error.HTTPError as e:
            if e.code < 500:
                return False, f"HTTP {e.code}"
            last = f"HTTP {e.code}"
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = str(getattr(e, "reason", e))
        time.sleep(2 * (attempt + 1))
    return False, last


def main() -> None:
    problems = Problems("check-links")
    urls: dict[str, list[str]] = {}
    for d in report_dirs():
        for name in FILES:
            f = d / name
            data = load_yaml(f) if f.is_file() else None
            if not isinstance(data, dict):
                continue
            for field in URL_FIELDS:
                value = data.get(field)
                val_list = [value] if isinstance(value, str) else (value if isinstance(value, list) else [])
                for u in val_list:
                    if isinstance(u, str) and u.startswith(("http://", "https://")):
                        urls.setdefault(u, []).append(f"{rel(f)}#{field}")

    checked = 0
    for url, where in sorted(urls.items()):
        host = (urlparse(url).hostname or "").lower()
        if host in SKIP_HOSTS or any(host.endswith("." + h) for h in SKIP_HOSTS):
            print(f"SKIP {url} (reserved documentation domain)")
            continue
        ok, detail = check(url)
        checked += 1
        if ok:
            print(f"OK   {url} ({detail})")
        else:
            problems.error(where[0], f"{url} failed: {detail} (recorded in {', '.join(where)})")

    problems.finish(checked)


if __name__ == "__main__":
    main()

