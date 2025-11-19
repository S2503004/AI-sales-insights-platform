from src.model.train_mlflow import train_with_mlflow
def test_mlflow_train_creates_model(tmp_path):
    out = str(tmp_path / 'model_mlflow.joblib')
    p = train_with_mlflow(out)
    assert p == out
