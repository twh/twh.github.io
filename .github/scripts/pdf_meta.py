#!/usr/bin/env python3
"""Stamp PDF document properties onto the generated resume.

Reads the standard <meta> tags out of the built resume HTML and writes them
into the PDF's document-information dictionary (Title, Author, Subject,
Keywords). Applicant tracking systems and document indexers read these fields,
but they are not part of the visible page, so the printed resume stays clean.

This uses the PDF's own metadata fields. It deliberately does NOT inject hidden
or white-on-white text into the page body: ATS vendors flag that as keyword
stuffing and it can disqualify a candidate.

Usage: pdf_meta.py <resume.html> <in.pdf> <out.pdf>
"""
import html
import re
import sys
from pypdf import PdfReader, PdfWriter


def meta(source: str, name: str) -> str:
    """Read a <meta name=... content=...> value.

    Attribute values may be double-quoted, single-quoted, or bare: `hugo
    --minify` strips the quotes from `name="keywords"` but keeps them on the
    content, and matching only the quoted form silently yields "".
    """
    m = re.search(
        r'<meta\s+name=["\']?%s["\']?\s+content=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))\s*/?>'
        % name,
        source,
        re.S | re.I,
    )
    if not m:
        return ""
    value = next(g for g in m.groups() if g is not None)
    return html.unescape(value).strip()


def main() -> int:
    html_path, pdf_in, pdf_out = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(html_path, encoding="utf-8") as fh:
        source = fh.read()

    keywords = meta(source, "keywords")
    subject = meta(source, "description")

    # These fields are the whole point of the step: an ATS reads them. Writing
    # them empty produces a PDF that looks fine and carries nothing, so treat a
    # parse miss as a build failure rather than shipping a hollow file.
    missing = [n for n, v in (("keywords", keywords), ("description", subject)) if not v]
    if missing:
        print(f"ERROR: no <meta> content found for: {', '.join(missing)}", file=sys.stderr)
        return 1

    reader = PdfReader(pdf_in)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.add_metadata(
        {
            "/Title": "Wayne Hendricks — Resume",
            "/Author": "Wayne Hendricks",
            "/Subject": subject,
            "/Keywords": keywords,
            "/Creator": "waynehendricks.com",
        }
    )
    with open(pdf_out, "wb") as fh:
        writer.write(fh)

    print(f"pages={len(reader.pages)} keywords={len(keywords.split(','))} -> {pdf_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
