# Project scope and state

The project is a bilingual Thai PDPA RAG learning exercise. The intended user asks in Thai or English and sees an answer with supporting source passages.

The owner must do more than 50% of the hands-on design, implementation, experimentation, and result interpretation. Agent help should support that work, especially through explanations, review, and debugging.

As of 2026-10-07, the two source PDFs exist in `Data/raw/`. The prepared text files in `Data/extracted/` are empty. No extraction, ingest, vector index, Backend API, or Frontend has been implemented in this repository.

The reference learning material is `../week5_learning/`, especially `RAG-flow.md`, `implementation/`, `evaluation/`, and the day 1–5 notebooks.

On 2026-10-07 at 22:20 ICT, the owner decided to focus on a local, evaluable bilingual RAG baseline before Docker, AWS deployment, or MLOps. Revisit Docker when the Backend API runs consistently and others need to run it or deployment begins. Revisit MLOps after the local baseline answers with source citations, has a bilingual and cross-language test set including insufficient-evidence questions, and can rerun preparation and evaluation reproducibly.
