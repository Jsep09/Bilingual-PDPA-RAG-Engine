"""Extract readable text with PDF page markers; no OCR or cleaning."""

from pathlib import Path
from typing import cast

import pymupdf


def extract_pdf_to_text(
    pdf_path: Path,
    output_path: Path,
    page_limit: int | None = 5,
) -> int:
    """Save UTF-8 text and return the number of extracted pages."""
    if page_limit is not None and page_limit < 1:
        raise ValueError("page_limit must be positive or None for all pages.")
    if output_path.exists() and output_path.stat().st_size > 0:
        raise FileExistsError(
            f"Output already contains text: {output_path}. "
            "Move it aside before rerunning."
        )

    pages_text = []
    with pymupdf.open(pdf_path) as document:
        page_count = len(document)
        if page_limit is not None:
            page_count = min(page_limit, page_count)

        for page_index in range(page_count):
            # The "text" format returns str; other formats can return lists or dicts.
            text = cast(str, document[page_index].get_text("text", sort=True))
            pages_text.append(f"=== PDF PAGE {page_index + 1} ===\n{text}")
            print(f"PDF page {page_index + 1}: {len(text.strip())} characters")
            if not text.strip():
                print("WARNING: No text found; inspect this page for OCR needs.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(pages_text), encoding="utf-8")
    return page_count
