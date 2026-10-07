# Agent instructions

This file is the single source of truth for agent instructions in this repository. Read the relevant files in `agent-knowledge/` for project context; those files are background information, not additional instruction files.

## Learning ownership

- This is the owner's learning project. The owner must perform more than 50% of the design, coding, experiments, and interpretation. Agents may write the experiment summaries on the owner's behalf.
- Work in small, reviewable steps. Explain the reason for a choice, invite the owner to implement learning-critical parts, and review their attempts before supplying a full implementation.
- Do not claim an experiment happened unless it was run and its inputs and results were recorded.
- Write and maintain experiment summaries in `experiments/` from observed outputs and the owner's notes. Distinguish verified observations, the owner's interpretation, and open questions; never invent results or decisions.
- Preserve the owner's existing work. Ask only when a decision truly depends on missing information.

## Project conventions

- Keep source PDFs in `Data/raw/`, extracted text in `Data/extracted/`, and structured records in `Data/jsonl/`.
- Put application and pipeline code in `Backend/` and user interface code in `Frontend/`.
- Keep generated vector indexes and local secrets out of Git. Track source material and reproducible experiment records when appropriate.
- Keep Thai and English sources distinguishable. Preserve source file, page, and section or article metadata when extraction makes it possible.
- Ground answers in retrieved passages, show citations, and state when evidence is insufficient. Do not present the system as legal advice.
- Use `../week5_learning/` as a learning reference for ingestion, retrieval, evaluation, and experiments; adapt its ideas to this project's documents.

## Project context

- `../ROOT_AGENTS.md`: overview of this project and its sibling learning reference
- `agent-knowledge/project.md`: scope, learning goals, current state
- `agent-knowledge/data.md`: data layout and extraction checks
- `agent-knowledge/experiments.md`: experiment and evaluation record format
- `experiments/README.md`: format and status of actual experiment records
- `agent-knowledge/architecture.md`: intended Frontend/Backend boundaries

Update the relevant context file when a decision or verified result changes. Keep these files factual and concise.
