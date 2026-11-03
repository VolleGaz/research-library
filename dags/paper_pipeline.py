
from datetime import datetime, timezone
from pathlib import Path

from airflow.sdk import dag, task


PROJECT_DIR = Path(__file__).resolve().parents[1]
PAPERS_DIR = PROJECT_DIR / "papers"
MARKDOWN_DIR = PROJECT_DIR / "data" / "markdown"


@dag(
    dag_id="paper_pipeline",
    schedule="0 * * * *",
    start_date=datetime(2026, 11, 1, tzinfo=timezone.utc),
    catchup=False,
    tags=["research-library"],
)
def paper_pipeline():

    @task
    def detect_pdfs():
        pdf_files = sorted(PAPERS_DIR.glob("*.pdf"))

        print(f"Found {len(pdf_files)} PDF files")

        return [str(pdf) for pdf in pdf_files]

    @task
    def convert_to_markdown(pdf_files):
        import pymupdf4llm

        MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

        for pdf_file in pdf_files:
            pdf_path = Path(pdf_file)

            markdown = pymupdf4llm.to_markdown(str(pdf_path))

            output_path = MARKDOWN_DIR / f"{pdf_path.stem}.md"
            output_path.write_text(markdown, encoding="utf-8")

            print(f"Converted: {pdf_path.name}")

    convert_to_markdown(detect_pdfs())


paper_pipeline()
