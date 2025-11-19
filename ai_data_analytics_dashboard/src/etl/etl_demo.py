import pandas as pd
import os
from datetime import datetime
def run_etl(out_folder='data'):
    os.makedirs(out_folder, exist_ok=True)
    # Synthetic demo data
    df = pd.DataFrame({
        'date': pd.date_range(end=datetime.today(), periods=90).tolist(),
        'units_sold': (abs(pd.Series(range(90)).apply(lambda x: 50 + x*0.5 + (x%7)*5)) ).tolist(),
        'price': (pd.Series([20 + (x%5) for x in range(90)]) ).tolist(),
        'marketing_spend': (pd.Series([100 + (x%10)*10 for x in range(90)]) ).tolist()
    })
    out_path = os.path.join(out_folder, 'sales_demo.csv')
    df.to_csv(out_path, index=False)
    return out_path

if __name__ == '__main__':
    print("ETL output:", run_etl())
