# Data workflow

## Directories

- `Data/raw/`: immutable source PDFs, one Thai and one English.
- `Data/extracted/`: intended location for readable extraction outputs in the local pipeline; absent as of 2026-10-15. The previous placeholders and sample are no longer present.
- `Data/jsonl/`: Thai Typhoon OCR output, one record per PDF page. The imported folder had a leading U+0E4B character, corrected to `jsonl` on 2026-10-15 without changing file content.
- `Data/txt/` and `Data/md/`: owner-imported Thai Colab exports, retained in their supplied locations.

## First hands-on experiment

On 2026-10-08, the owner reported that `ประการเกี่ยวกับการจำกัดสิทธิ` was extracted as `ประการเกี่ยวกับการจ ากัดสิทธิ`. The agent confirmed `จ ากัด` in the Thai sample and reproduced the same form twice on the first PDF page using both bundled pypdf and pdfplumber. Changing extractors alone did not resolve this example. The exact font/character-map cause has not been established. No automatic text corrections have been applied; retain original extraction and review any corrections separately.

The owner should choose an extraction method, run it on both PDFs, and compare sample pages with the PDF originals. Inspect Thai characters, headings, article numbers, page order, missing text, and line breaks. Record the method and problems before selecting the baseline.

For future JSONL records, aim to retain `language`, `source_file`, `page`, `section_or_article`, and `text` when reliably available. Do not invent page or article values if extraction cannot establish them.

## Extraction script

## Colab Typhoon OCR notebook

The owner chose the OCR approach and removed the previous extraction pipeline/script, retaining the exploratory notebook as experiment history. Do not recreate that pipeline as part of OCR evaluation.

After reviewing the known English errors and evaluation plan, the owner explicitly authorized committing and pushing the work as a historical record on 2026-10-15. This supersedes the earlier conditional hold on commit/push, but does not approve OCR accuracy or resolve English page 36. Preserve raw outputs and the documented limitations.

On 2026-10-15, prepared `Backend/notebooks/04_ocr_evaluation.ipynb` and its guide. Following the owner's request to keep evaluation small, it uses CER, English WER, one per-page CER comparison plot, and text alignment, with optional CSV/plot export. Human-checked full-page references go in `Data/ground_truth/{en,th}/page_NNN.txt`; none have been supplied yet, so actual OCR accuracy remains unevaluated. Multiple model JSONL files can be compared on exactly the same reference pages. Tests covered real-data loading/no-reference behavior and isolated synthetic comparisons; they are not OCR accuracy results. No annotation manifest, automatic approval threshold, table metric, or replacement OCR model was added. The research links, including the owner's LlamaIndex OCR accuracy article, are recorded in the guide.

The owner subsequently imported the English exports on 2026-10-15. All 39 pages pass structural checks and TXT/Markdown match JSONL, but English PDF page 36 has confirmed content errors: OCR replaces the Section 83 continuation and changes Section 84's `five million Baht` to `three million Baht`. Verified against a rendered PDF page. The English data is not approved for indexing; raw exports remain unchanged. Commit/push was withheld under the owner's conditional request. See `experiments/002-typhoon-english-ocr.md` for checks and next steps.

On 2026-10-15, the owner imported the Thai JSONL, TXT, and Markdown outputs. Structural validation found 44 records with consecutive `pdf_page` values 1–44, all `language=th`, `source_file=PDPA (TH).pdf`, and `model=typhoon-ai/typhoon-ocr1.5-2b`. No blank text or `possibly_truncated=true` records were found; text totals 84,305 characters. TXT and Markdown exactly match reconstruction from the JSONL using the notebook's export format after normalizing line endings. All `section_or_article` values remain null. Page 1 includes a `<figure>` description; OCR accuracy and that description have not been visually verified against the PDF. No English OCR export is present locally. See `experiments/001-typhoon-thai-ocr.md`.

On 2026-10-15, the owner reported obtaining the Thai OCR result and running the English notebook on Colab. The agent downloaded the current Colab notebook and synchronized `Backend/notebooks/03_typhoon_ocr_colab.ipynb` byte-for-byte. Compared with the previous local copy, the source changes are `LANGUAGE = 'en'` and export to JSONL, TXT, and Markdown under Drive `PDPA_RAG/Data/{jsonl,txt,md}/`. The existing Markdown instructions still describe JSONL-only export. At inspection, the visible Colab output identified the English PDF as 39 pages and the GPU as Tesla T4; the model-loading cell was executing. This snapshot does not establish that English OCR or export completed, and the Thai output files were not inspected. No Colab cells were edited or executed by the agent.

## Exploratory notebook

On 2026-10-08, the owner chose to explore extraction in Jupyter before refining the pipeline. Added `Backend/notebooks/01_pdf_to_text.ipynb` and installed `ipykernel` as a Backend development dependency. The notebook previews one selected PDF page as an image, compares sorted and unsorted extraction, lists suspicious Thai spacing, and previews an editable, exact-text correction for `จ ากัด`. Raw text is retained. Export is disabled by default and refuses existing output paths. All six code cells passed a direct Python execution smoke check for Thai page 1 in preview mode; notebook outputs remain empty for the owner to run. This does not establish extraction accuracy, verify the owner's choice of cleaning rules, or confirm the editor's live kernel selection.

On 2026-10-08, added `Backend/scripts/extract_pdf.py`, calling the reusable PyMuPDF function in `Backend/src/backend/pipelines/pdf_to_text.py`. From Backend, run `uv run scripts/extract_pdf.py --language th` (or `en`) for the first five pages, adding `--all` for the full document. Outputs are UTF-8 text with 1-based PDF page markers; samples use `_sample.txt`. Non-empty outputs are protected from overwriting.

During agent troubleshooting on 2026-10-08, `uv run` failed to query Python with `Access is denied (os error 5)` in the agent environment. Direct invocation using `.venv/Scripts/python.exe scripts/extract_pdf.py --language th` succeeded with PyMuPDF 1.28.2, generating `pdpa_th_sample.txt`. Reported stripped text lengths for PDF pages 1–5 were 1483, 2338, 2272, 2076, and 2115 characters. This was a runtime check, not an owner experiment or a verified extraction-quality result. English extraction quality and visual comparison against the source PDFs remain unverified.

The owner subsequently reported Pylance missing imports, followed by `reportAttributeAccessIssue` on `text.strip()`. On 2026-10-08, added `typing.cast(str, ...)` around `get_text("text", sort=True)` because PyMuPDF's general extraction method can also return lists or dictionaries for other formats. Verified one-page extraction from both source PDFs into temporary files using the Backend interpreter: Thai page 1 had 1483 stripped characters and English page 1 had 2518. Both outputs exactly matched the original extraction call with the expected page marker. Temporary files were removed; this was a runtime check, not an extraction-quality experiment. Live Pylance diagnostics remain to be checked in the editor.
