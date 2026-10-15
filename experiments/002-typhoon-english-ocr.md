# English Typhoon OCR validation — 2026-10-15

## Question and inputs

The owner imported the English OCR exports and requested validation before committing and pushing. Checked `Data/jsonl/pdpa_en_typhoon_ocr.jsonl`, its TXT/Markdown counterparts, and `Data/raw/PDPA (Eng).pdf`. Raw OCR files were retained unchanged.

## Checks performed

- Parsed every JSONL record with strict UTF-8 decoding; checked required fields, page order, language, source filename, and nonblank text.
- Reconstructed TXT and Markdown from JSONL using the notebook's export format and compared after line-ending normalization.
- Rechecked Thai exports using the same structural checks.
- Used the existing Backend Python interpreter with PyMuPDF to count the English PDF pages and compare extracted text against OCR on all 39 pages. A diagnostic comparison lowercased text and removed non-ASCII-alphanumeric characters before using `difflib.SequenceMatcher(autojunk=False)`; this is a screening aid, not an accuracy score.
- Inspected the complete rendered image of English PDF page 36 to verify the discrepancy found by text comparison.

## Observed results

- English structural checks passed: 39 consecutive pages, all language `en` and source `PDPA (Eng).pdf`; 104,900 text characters. TXT/Markdown match the JSONL content. No blank text, U+FFFD replacement characters, or `possibly_truncated=true` records were found. Article metadata remains null on all pages.
- Thai structural checks still passed: 44 pages; TXT/Markdown match JSONL.
- English page 36 had the lowest normalized similarity (0.9443); other pages were at least 0.9970. These numbers do not prove semantic correctness.
- A heading-pattern comparison also flagged line-wrap differences on several pages; these alone do not prove missing sections.
- **Confirmed material OCR error on PDF page 36:** the source begins with a continuation of Section 83 ending in `three million Baht`. OCR replaces that continuation with an added `Section 83` paragraph resembling Section 84 and ending in `five million Baht`.
- **Confirmed material OCR error on the same page:** source Section 84 ends in `five million Baht`; OCR says `three million Baht`. This was confirmed against the rendered PDF page, not only its text layer.
- The local notebook has no stored cell outputs, `displayName`/`userId` metadata, or matches for the checked API-token patterns. This is not a comprehensive privacy audit.

## Decision and next step

English OCR fails content validation despite passing structural checks. No commit or push was performed because the owner's authorization was conditional on passing validation. Reprocess or correct page 36 with recorded provenance, regenerate all three English exports consistently, and validate again. Full visual proofreading of all pages and retrieval evaluation remain undone. The agent did not modify OCR text or remove unrelated Backend files.
