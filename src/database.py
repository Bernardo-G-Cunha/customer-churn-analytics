import sqlite3
import pandas as pd

from src.config import DATA_DIR, SQL_DIR

DB_PATH = DATA_DIR / "customer_churn.db"


def run_query(query):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def run_sql_file(filename):

    with open(SQL_DIR / filename, "r") as file:
        query = file.read()
    
    return run_query(query)


def load_customers():

    return run_query(
        "SELECT * FROM customers"
    )