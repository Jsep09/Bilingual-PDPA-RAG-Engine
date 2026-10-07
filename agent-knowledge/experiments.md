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

No experiments have been recorded yet.
