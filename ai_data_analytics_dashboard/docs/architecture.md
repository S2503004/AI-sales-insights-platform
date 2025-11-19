# Architecture Overview

Components:
1. ETL (src/etl/etl_demo.py) — ingest synthetic CSV, basic feature engineering.
2. Model (src/model/train.py) — trains a RandomForestRegressor, saves to `models/`.
3. API (src/api/app.py) — FastAPI endpoints for health, ETL trigger, training, and prediction.
4. Deployment — Dockerfile + docker-compose; CI via GitHub Actions.

Data flow:
ETL -> data CSV -> train -> model.joblib -> API predict endpoint

Extensibility ideas:
- Replace synthetic ETL with connectors (S3, BigQuery, Postgres).
- Add incremental training and model registry (MLflow).
- Add authentication and role-based access for PMs.
