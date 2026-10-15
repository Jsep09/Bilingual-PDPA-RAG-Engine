# Experiments and evaluation

Every completed experiment should record:

1. Question or hypothesis.
2. Baseline configuration and changed variable.
3. Input documents and test questions.
4. Commands or steps actually run.
5. Observed results, including failures.
6. The owner's interpretation and next decision.

Agents are responsible for writing the record in `experiments/` after the owner conducts the experiment or provides its actual outputs. Attribute decisions to the owner only when the owner has made them. Mark unknown or untested items explicitly.

Start with a small test set covering Thai questions, English questions, cross-language retrieval, article-specific facts, and questions without supporting evidence. Inspect retrieved passages separately from generated answers so failures can be located.

The `week5_learning/evaluation/` example demonstrates retrieval metrics and answer assessment. Select metrics appropriate to this project's labeled source passages; do not treat a model's judging score as proof of legal correctness.

`experiments/001-typhoon-thai-ocr.md` records the owner's imported Thai OCR outputs and the agent's structural checks on 2026-10-15. OCR accuracy and retrieval quality remain unverified.

`experiments/002-typhoon-english-ocr.md` records the English import and validation failure: page 36 has material OCR errors confirmed against the rendered PDF. No commit/push was performed; English text needs correction or reprocessing and revalidation.

`experiments/003-ocr-evaluation-summary-th.md` summarizes the methods and observed results in Thai, explains CER/WER versus illustrative accuracy percentages, and records that no human-verified full-page references or actual notebook-04 accuracy reports were present at inspection. Its three-word metric example is illustrative, not a page/document score. Replacement-model evaluation remains planned.
