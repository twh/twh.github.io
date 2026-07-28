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
    m = re.search(
        r'<meta\s+name=["\']%s["\']\s+content=["\'](.*?)["\']\s*/?>' % name,
        source,
        re.S | re.I,
    )
    return html.unescape(m.group(1)).strip() if m else ""


def main() -> int:
    html_path, pdf_in, pdf_out = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(html_path, encoding="utf-8") as fh:
        source = fh.read()

    title = meta(source, "title") or "Wayne Hendricks — Resume"
    keywords = meta(source, "keywords")
    subject = meta(source, "description")

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
