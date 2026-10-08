# Data workflow

## Directories

- `Data/raw/`: immutable source PDFs, one Thai and one English.
- `Data/extracted/`: readable text extracted from each PDF. Full-document files remain empty placeholders; a Thai five-page sample was generated during agent troubleshooting on 2026-10-08.
- `Data/jsonl/`: future structured records with text and provenance metadata.

## First hands-on experiment

On 2026-10-08, the owner reported that `ประการเกี่ยวกับการจำกัดสิทธิ` was extracted as `ประการเกี่ยวกับการจ ากัดสิทธิ`. The agent confirmed `จ ากัด` in the Thai sample and reproduced the same form twice on the first PDF page using both bundled pypdf and pdfplumber. Changing extractors alone did not resolve this example. The exact font/character-map cause has not been established. No automatic text corrections have been applied; retain original extraction and review any corrections separately.

The owner should choose an extraction method, run it on both PDFs, and compare sample pages with the PDF originals. Inspect Thai characters, headings, article numbers, page order, missing text, and line breaks. Record the method and problems before selecting the baseline.

For future JSONL records, aim to retain `language`, `source_file`, `page`, `section_or_article`, and `text` when reliably available. Do not invent page or article values if extraction cannot establish them.

## Extraction script

## Exploratory notebook

On 2026-10-08, the owner chose to explore extraction in Jupyter before refining the pipeline. Added `Backend/notebooks/01_pdf_to_text.ipynb` and installed `ipykernel` as a Backend development dependency. The notebook previews one selected PDF page as an image, compares sorted and unsorted extraction, lists suspicious Thai spacing, and previews an editable, exact-text correction for `จ ากัด`. Raw text is retained. Export is disabled by default and refuses existing output paths. All six code cells passed a direct Python execution smoke check for Thai page 1 in preview mode; notebook outputs remain empty for the owner to run. This does not establish extraction accuracy, verify the owner's choice of cleaning rules, or confirm the editor's live kernel selection.

On 2026-10-08, added `Backend/scripts/extract_pdf.py`, calling the reusable PyMuPDF function in `Backend/src/backend/pipelines/pdf_to_text.py`. From Backend, run `uv run scripts/extract_pdf.py --language th` (or `en`) for the first five pages, adding `--all` for the full document. Outputs are UTF-8 text with 1-based PDF page markers; samples use `_sample.txt`. Non-empty outputs are protected from overwriting.

During agent troubleshooting on 2026-10-08, `uv run` failed to query Python with `Access is denied (os error 5)` in the agent environment. Direct invocation using `.venv/Scripts/python.exe scripts/extract_pdf.py --language th` succeeded with PyMuPDF 1.28.2, generating `pdpa_th_sample.txt`. Reported stripped text lengths for PDF pages 1–5 were 1483, 2338, 2272, 2076, and 2115 characters. This was a runtime check, not an owner experiment or a verified extraction-quality result. English extraction quality and visual comparison against the source PDFs remain unverified.

The owner subsequently reported Pylance missing imports, followed by `reportAttributeAccessIssue` on `text.strip()`. On 2026-10-08, added `typing.cast(str, ...)` around `get_text("text", sort=True)` because PyMuPDF's general extraction method can also return lists or dictionaries for other formats. Verified one-page extraction from both source PDFs into temporary files using the Backend interpreter: Thai page 1 had 1483 stripped characters and English page 1 had 2518. Both outputs exactly matched the original extraction call with the expected page marker. Temporary files were removed; this was a runtime check, not an extraction-quality experiment. Live Pylance diagnostics remain to be checked in the editor.
