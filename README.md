# Research Library — INFO-H420 Assignment 3

A local Apache Airflow pipeline that turns research PDFs into a searchable HTML library. It converts PDFs to Markdown, uses a **local LLM** to generate metadata, stores the metadata in **SQLite**, and sends **Discord** notifications.

## Prerequisites

- Git and [uv](https://docs.astral.sh/uv/)
- Python 3.12 (uv can install/manage it)
- [Ollama](https://ollama.com/) for the local LLM (or an equivalent OpenAI-compatible local server)
- A locally synced Google Drive folder containing `ResearchLibrary/papers/` and `ResearchLibrary/output/`
- A Discord webhook URL (for notifications)

> **Windows:** Run Airflow in WSL2. The commands below assume a Linux/macOS shell.

## First-time setup (each teammate)

**1. Clone the shared repository:**

```bash
git clone <REPOSITORY_URL>
cd research-library
```

**2. Install the same Python dependencies as the rest of the team:**

```bash
uv sync --locked
```

This reads the committed `pyproject.toml` and `uv.lock`. **Do not run `uv init` again.**

**3. Create local directories and configuration:**

```bash
mkdir -p dags pipeline data .airflow
cp .env.example .env
```

Edit `.env` and set `PAPERS_DIR` and `OUTPUT_DIR` to the **absolute paths** of your own synced Google Drive folders. Set `DB_PATH` to a **local, non-synced** path. Add your Discord webhook URL when available. **Never commit `.env`.**

**4. Start the local LLM (Ollama example):**

```bash
ollama pull llama3.2
ollama serve
```

If Ollama is already running in the background, you do not need to run `ollama serve` again. Keep the LLM available while the pipeline runs.

**5. Start Airflow (in a separate terminal, from the repository root):**

```bash
set -a
source .env
set +a

export AIRFLOW_HOME="$PWD/.airflow"
export AIRFLOW__CORE__DAGS_FOLDER="$PWD/dags"
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

uv run airflow standalone
```

Open **http://localhost:8080**. Airflow will initialize its local services on the first run. The DAG will appear after `dags/paper_pipeline.py` has been implemented.

## Expected project structure

```text
research-library/
├── dags/
│   └── paper_pipeline.py
├── pipeline/             # PDF, LLM, database, HTML, Discord helpers
├── data/
│   └── papers.db         # local only; do not commit
├── .airflow/              # local Airflow state; do not commit
├── .env                   # local config/secrets; do not commit
├── .env.example           # safe config template; commit
├── pyproject.toml
├── uv.lock
└── README.md
```

Google Drive keeps PDFs in `ResearchLibrary/papers/` and generated HTML in `ResearchLibrary/output/index.html`. **Do not put `papers.db` in the synced Google Drive folder.**

## Working together

Create a branch for each feature, open pull requests, and pull the latest code before continuing work:

```bash
git pull
uv sync --locked
```

If a dependency needs to be added, one person can run `uv add <package>` and commit **both** `pyproject.toml` and `uv.lock`.

## Important

The environment variable names in `.env.example` are the team's proposed convention: the pipeline code must read those same names. Keep `.venv/`, `.airflow/`, `.env`, and local `.db` files out of Git. If `.gitignore` contains `.env.*`, add `!.env.example` so the template can be committed.
