# Backend

Use Python 3.12 or newer. From this directory, install the locked dependencies
and the local `backend` package with:

```powershell
uv sync --locked
uv run scripts/extract_pdf.py --help
```

## VS Code imports

Select `Backend/.venv/Scripts/python.exe` with **Python: Select Interpreter**.
Both `backend` and `pymupdf` must resolve from that environment.

Workspace settings apply to the folder opened in VS Code. The settings in this
directory use `./src`; the repository-root settings use `./Backend/src`. If you
open the parent `rag` folder, its settings must point to
`./Bilingual-PDPA-RAG-Engine/Backend/src` and the matching Backend interpreter.
Nested `.vscode/settings.json` files do not configure the outer workspace.

After changing the interpreter or workspace settings, run **Developer: Reload
Window** if the import diagnostics remain.
