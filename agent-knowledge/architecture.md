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

This records the intended stack only. Framework initialization and implementation will happen later.
