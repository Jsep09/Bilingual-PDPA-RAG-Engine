"""Run from Backend: uv run scripts/extract_pdf.py --language th."""

import argparse
from pathlib import Path

from backend.pipelines.pdf_to_text import extract_pdf_to_text


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract PDPA PDF text.")
    parser.add_argument("--language", choices=("th", "en"), default="th")
    parser.add_argument(
        "--all", action="store_true", help="Extract all pages instead of the first 5."
    )
    args = parser.parse_args()

    project_dir = Path(__file__).resolve().parents[2]
    source_file = "PDPA (TH).pdf" if args.language == "th" else "PDPA (Eng).pdf"
    suffix = "" if args.all else "_sample"
    pdf_path = project_dir / "Data" / "raw" / source_file
    output_path = (
        project_dir / "Data" / "extracted" / f"pdpa_{args.language}{suffix}.txt"
    )

    try:
        page_count = extract_pdf_to_text(
            pdf_path, output_path, page_limit=None if args.all else 5
        )
    except (OSError, ValueError, RuntimeError) as error:
        parser.exit(1, f"Extraction failed: {error}\n")
    print(f"Saved {page_count} pages to: {output_path}")


if __name__ == "__main__":
    main()
