# Intended component boundaries

## Data and Backend

The future Backend owns PDF extraction, data preparation, indexing, retrieval, answer generation, and any API. Keep extraction and ingest separate from per-question answering so each can be tested independently. Store source provenance through every stage.

## Frontend

The future Frontend accepts Thai or English questions and shows the answer beside retrieved passages and their source locations. It should expose insufficient evidence clearly.

## Storage

PDFs and extracted/structured text are the reviewable source data. A future vector index is generated from structured data and can be rebuilt. No database technology has been selected yet.

## Chosen application stack

- Frontend: React with TypeScript and Vite, under `Frontend/`.
- Backend API: Python with FastAPI, under `Backend/`.
- Backend Python environment and dependencies: uv, with `pyproject.toml` and `uv.lock` under `Backend/`. Keep the local virtual environment out of Git.

On 2026-10-08, verified that `backend.pipelines.pdf_to_text` and PyMuPDF 1.28.2 import successfully using `Backend/.venv/Scripts/python.exe`. Corrected the outer `rag/.vscode/settings.json` to use this interpreter and `Bilingual-PDPA-RAG-Engine/Backend/src` for import resolution, replacing its system-environment project setting. This outer configuration is local to the parent workspace. See `Backend/README.md` for VS Code setup; live Pylance diagnostics still require checking in the editor.

As verified on 2026-10-08, Backend has a uv project, a lockfile, and a starter FastAPI app in `Backend/src/backend/main.py`. The RAG pipeline and the target module separation are not implemented yet.

## Backend organization decision

On 2026-10-08, the owner selected the FastAPI Bigger Applications approach for Backend structure. Retain `Backend/src/backend/`, separate API routers and reusable dependencies, and register routers in `main.py`. Add schemas, services, and offline pipelines incrementally for the RAG workload. The authoritative target tree and rules are in `AGENTS.md`; this note records the decision only.
