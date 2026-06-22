import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "predictions.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

        age INTEGER,
        gender TEXT,
        tenure INTEGER,
        usage_frequency INTEGER,
        support_calls INTEGER,
        payment_delay INTEGER,
        subscription_type TEXT,
        contract_length TEXT,
        total_spend REAL,
        last_interaction INTEGER,
        monthly_spend REAL,
        support_freq REAL,

        churn_probability REAL,
        prediction INTEGER
    )
    """)

    conn.commit()
    conn.close()