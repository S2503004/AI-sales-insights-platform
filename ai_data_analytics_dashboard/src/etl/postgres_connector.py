import os
import pandas as pd
from sqlalchemy import create_engine

def fetch_sales_from_postgres(conn_str=None, query=None):
    """
    Fetch sales data from Postgres. For demo, if no conn_str provided, returns None.
    Replace conn_str with 'postgresql://user:pass@host:port/dbname'
    """
    if conn_str is None:
        raise ValueError("No Postgres connection string provided.")
    engine = create_engine(conn_str)
    q = query or "SELECT date, units_sold, price, marketing_spend FROM sales LIMIT 10000;"
    df = pd.read_sql(q, engine)
    return df
