"""Assemble the standalone site from its HTML template and Wonder Bite files."""

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "src"
OUTPUT = ROOT / "index.html"
INCLUDE = re.compile(rb"<!-- include: (wonder-bites/[a-z0-9-]+\.html) -->")


def build_html():
    template = (SOURCE / "index.template.html").read_bytes()
    if b"<!-- include:" in INCLUDE.sub(b"", template):
        raise ValueError("Invalid include marker in src/index.template.html")
    return INCLUDE.sub(
        lambda match: (SOURCE / match[1].decode("ascii")).read_bytes(),
        template,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Check that index.html is up to date."
    )
    args = parser.parse_args()
    try:
        html = build_html()
        if args.check:
            if not OUTPUT.is_file() or OUTPUT.read_bytes() != html:
                raise ValueError("index.html is out of date. Run python3 build.py.")
        else:
            OUTPUT.write_bytes(html)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
