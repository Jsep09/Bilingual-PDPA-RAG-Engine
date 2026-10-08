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

## Backend structure

Follow [FastAPI Bigger Applications — Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/) for API organization. Adapt its example `app/` package to this repository's existing `Backend/src/backend/` package; preserve the uv src layout and package name.

```text
Backend/
├── pyproject.toml
├── uv.lock
├── src/
│   └── backend/
│       ├── __init__.py
│       ├── main.py
│       ├── dependencies.py
│       ├── routers/
│       │   ├── __init__.py
│       │   └── questions.py
│       ├── internal/           # Optional internal API routers
│       │   └── __init__.py
│       ├── schemas/            # Project extension: request/response models
│       │   └── __init__.py
│       ├── services/           # Project extension: retrieval and answering
│       │   └── __init__.py
│       └── pipelines/          # Project extension: extraction and indexing
│           └── __init__.py
├── scripts/                    # Thin entry points for offline workflows
└── tests/                      # Tests added alongside implemented behavior
```

This is the target layout, not a claim that these modules already exist. Create modules only when needed; `questions.py` is an example feature name.

### FastAPI organization

- Keep `main.py` focused on creating the `FastAPI` app and registering routers with `app.include_router(...)`.
- Group related endpoints in `routers/` using `APIRouter`. Define shared prefixes, tags, responses, and dependencies at router level where appropriate.
- Keep reusable FastAPI dependency providers in `dependencies.py` and inject them with `Depends`.
- Include `__init__.py` in Python packages. Use package imports such as `from backend.routers import questions`, or consistent relative imports. Import router modules to avoid colliding `router` names.
- Add `internal/` only for internal API routes when needed; the folder name does not enforce access control.

### RAG-specific boundaries

The `schemas/`, `services/`, `pipelines/`, `scripts/`, and `tests/` choices are project adaptations, not requirements of the linked tutorial.

- Keep routers thin: validate requests, call services, and return responses. Put retrieval and answer-generation logic in `services/` and request/response models in `schemas/`.
- Keep PDF extraction, data preparation, and index construction in `pipelines/`, separate from per-question processing. Offline scripts call these modules without duplicating their logic.
- Services and pipelines must not import routers or `main.py`; avoid circular imports and HTTP coupling in reusable RAG logic.
- Keep source and intermediate data in the repository-level `Data/` directories. Do not move PDFs, secrets, or generated indexes into the Python package.
- Keep dependencies and uv configuration under `Backend/`. When configuring the FastAPI CLI, use `backend.main:app` as the application entry point for this src layout.
- Updating these instructions does not authorize scaffolding or migrating application code; implement the structure incrementally during Backend work.

## Project context

- `../ROOT_AGENTS.md`: overview of this project and its sibling learning reference
- `agent-knowledge/project.md`: scope, learning goals, current state
- `agent-knowledge/data.md`: data layout and extraction checks
- `agent-knowledge/experiments.md`: experiment and evaluation record format
- `experiments/README.md`: format and status of actual experiment records
- `agent-knowledge/architecture.md`: intended Frontend/Backend boundaries

Update the relevant context file when a decision or verified result changes. Keep these files factual and concise.
