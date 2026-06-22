import sqlite3
import pandas as pd
import streamlit as st
from pathlib import Path

st.title("Prediction History")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "backend" / "predictions.db"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        "SELECT * FROM predictions ORDER BY id DESC",
        conn
    )
    conn.close()
    return df

if st.button("Refresh"):
    st.rerun()

try:
    df = load_data()
    st.dataframe(df, use_container_width=True, hide_index=True)
except Exception as e:
    st.error(str(e))