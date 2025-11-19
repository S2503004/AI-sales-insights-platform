import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
from src.etl.etl_demo import run_etl

def train_demo_model(out_path='models/sales_model.joblib'):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    data_path = run_etl()
    df = pd.read_csv(data_path)
    # simple feature engineering
    X = df[['units_sold','price','marketing_spend']]
    # target: revenue = units_sold * price (synthetic)
    y = df['units_sold'] * df['price']
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    joblib.dump(model, out_path)
    return out_path

if __name__ == '__main__':
    print("Model saved to:", train_demo_model())
