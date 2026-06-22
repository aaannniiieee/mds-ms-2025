from fastapi import FastAPI
import joblib
import pandas as pd
from pathlib import Path
from backend.init_db import init_db, get_connection

app = FastAPI()
init_db()


BASE_DIR = Path(__file__).resolve().parent
PIPELINE_PATH = BASE_DIR / "ml" / "models" / "churn_pipeline.pkl"
THRESHOLD_PATH = BASE_DIR / "ml" / "models" / "threshold.pkl"

pipeline = joblib.load(PIPELINE_PATH)
threshold = joblib.load(THRESHOLD_PATH)


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    proba = pipeline.predict_proba(df)[:, 1][0]
    pred = int(proba >= threshold)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO predictions (
        age,
        gender,
        tenure,
        usage_frequency,
        support_calls,
        payment_delay,
        subscription_type,
        contract_length,
        total_spend,
        last_interaction,
        monthly_spend,
        support_freq,
        churn_probability,
        prediction
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        int(df["Age"].iloc[0]),
        str(df["Gender"].iloc[0]),
        int(df["Tenure"].iloc[0]),
        int(df["Usage Frequency"].iloc[0]),
        int(df["Support Calls"].iloc[0]),
        int(df["Payment Delay"].iloc[0]),
        str(df["Subscription Type"].iloc[0]),
        str(df["Contract Length"].iloc[0]),
        float(df["Total Spend"].iloc[0]),
        int(df["Last Interaction"].iloc[0]),
        float(df["Monthly Spend"].iloc[0]),
        float(df["Support Freq"].iloc[0]),
        float(proba),
        int(pred)
    ))

    conn.commit()
    conn.close()

    verdict = "High churn risk" if pred == 1 else "Low churn risk"
    return {
        "churn_probability": float(proba),
        "prediction": pred,
        "verdict": verdict
    }
