# AI-enabled Sales Insights — Product Manager Project

**Project type:** End-to-end data analytics product (ETL → Model → API → Dashboard)  
**Goal:** Provide near-real-time sales insights and anomaly detection for product managers.  
**Author:** Generated scaffold  
**Created:** 2025-11-19

## Contents
- `src/` — application code (ETL, model training, API)
- `notebooks/` — exploratory notebook & demo
- `docs/` — architecture, report, setup, usage
- `models/` — trained model placeholder
- `Dockerfile`, `docker-compose.yml`, CI workflow
- `report.docx` — Word report (high-level documentation)

## Quickstart (development)
1. Create a Python venv and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Run API:
```bash
uvicorn src.api.app:app --reload --port 8000
```
3. Run ETL demo:
```bash
python src/etl/etl_demo.py
```

## Deliverables included
- Production-style code (FastAPI, modular ETL, sklearn model)
- Dockerfile & docker-compose
- CI workflow (GitHub Actions)
- Word report, README, architecture diagrams
- Suggested commit history and resume-ready project description


## Added in update
- Postgres and S3 connector templates (src/etl).
- MLflow-integrated training (src/model/train_mlflow.py).
- Basic React dashboard scaffold in `frontend/` using Recharts.
- CI/CD workflow template to build and push Docker image (.github/workflows/deploy.yml).
- Mock UI and architecture images in docs/images.
