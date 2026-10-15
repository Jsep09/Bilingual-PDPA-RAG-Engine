# Thai Typhoon OCR output check — 2026-10-15

## Question and method

The owner ran Thai OCR on Colab and imported `pdpa_th_typhoon_ocr.{jsonl,txt,md}` into `Data/{jsonl,txt,md}/`. The agent parsed every JSONL line as UTF-8 JSON, checked page order and metadata, and reconstructed TXT/Markdown using the notebook's export format to compare with the supplied files. The agent did not rerun OCR.

## Observed results

- 44 records, numbered consecutively from 1 to 44; no blank text records.
- All records identify language `th`, source `PDPA (TH).pdf`, and model `typhoon-ai/typhoon-ocr1.5-2b`.
- Total OCR text: 84,305 characters. No record has `possibly_truncated=true`; this flag does not prove that every source passage was recognized.
- TXT and Markdown match the JSONL text and expected page separators after line-ending normalization.
- All 44 `section_or_article` values are null. Page 1 contains a `<figure>` description. No U+FFFD replacement characters were found in the JSONL text.
- Corrected the imported directory name from a leading U+0E4B plus `jsonl` to `jsonl`; the file hash was unchanged. TXT/MD were retained in their supplied directories.

## Interpretation and open work

The three exports are structurally consistent. OCR accuracy, article completeness, and the figure description have not been compared visually against the source PDF. No baseline quality comparison or retrieval experiment was run. The owner has not yet selected cleaning or chunking rules. English OCR was reported in progress; no English export was present locally at inspection.
