from src.model.train import train_demo_model
def test_train_creates_model(tmp_path):
    out = str(tmp_path / 'model.joblib')
    p = train_demo_model(out)
    assert p == out
