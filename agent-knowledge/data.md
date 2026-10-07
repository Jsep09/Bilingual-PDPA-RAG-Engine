# Data workflow

## Directories

- `Data/raw/`: immutable source PDFs, one Thai and one English.
- `Data/extracted/`: readable text extracted from each PDF. Current files are placeholders and empty.
- `Data/jsonl/`: future structured records with text and provenance metadata.

## First hands-on experiment

The owner should choose an extraction method, run it on both PDFs, and compare sample pages with the PDF originals. Inspect Thai characters, headings, article numbers, page order, missing text, and line breaks. Record the method and problems before selecting the baseline.

For future JSONL records, aim to retain `language`, `source_file`, `page`, `section_or_article`, and `text` when reliably available. Do not invent page or article values if extraction cannot establish them.
