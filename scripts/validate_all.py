"""Run all repository validation checks in sequence.

Convenience runner for maintainers before committing changes:
  python scripts/validate_all.py
"""
import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    ("Validate corpus completeness", "validate_corpus.py"),
    ("Validate metadata & schemas", "validate_metadata.py"),
    ("Validate markdown editions", "validate_markdown.py"),
    ("Verify source fixity digests", "verify_checksums.py"),
]

def main() -> None:
    root = Path(__file__).resolve().parent
    python = sys.executable
    failed = []

    print("=" * 60)
    print("UK Public Library Policy Archive — Validation Suite")
    print("=" * 60)

    for title, script in SCRIPTS:
        script_path = root / script
        print(f"\n--> {title} ({script})...")
        res = subprocess.run([python, str(script_path)])
        if res.returncode != 0:
            failed.append(script)

    print("\n" + "=" * 60)
    if failed:
        print(f"FAILED: {len(failed)} check(s) failed ({', '.join(failed)}).")
        sys.exit(1)
    else:
        print("ALL CHECKS PASSED: Corpus is clean and compliant.")
        sys.exit(0)

if __name__ == "__main__":
    main()

