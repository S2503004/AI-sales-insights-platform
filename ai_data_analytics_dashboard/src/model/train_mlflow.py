import mlflow
import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from src.etl.etl_demo import run_etl

def train_with_mlflow(out_path='models/sales_model_mlflow.joblib', experiment_name='sales_insights'):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    data_path = run_etl()
    df = pd.read_csv(data_path)
    X = df[['units_sold','price','marketing_spend']]
    y = df['units_sold'] * df['price']
    mlflow.set_experiment(experiment_name)
    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=50, random_state=42)
        model.fit(X, y)
        joblib.dump(model, out_path)
        mlflow.log_param('n_estimators', 50)
        mlflow.log_metric('train_samples', len(df))
        mlflow.log_artifact(out_path)
    return out_path

if __name__ == '__main__':
    print("Model saved to:", train_with_mlflow())
