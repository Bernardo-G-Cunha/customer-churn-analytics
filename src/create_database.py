import sqlite3
import pandas as pd

from src.config import DATA_DIR


df = pd.read_csv(
    DATA_DIR / "processed" / "customer_churn_clean.csv"
)

conn = sqlite3.connect(
    DATA_DIR / "customer_churn.db"
)

df.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database successfully created.")