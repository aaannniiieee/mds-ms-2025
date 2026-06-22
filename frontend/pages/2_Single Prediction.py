import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Single Customer Prediction")

st.write(
    "Enter customer information to estimate churn probability."
)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 120, 39)
    gender = st.selectbox("Gender", ["Male", "Female"], index=0)
    tenure = st.number_input("Tenure", 1, 100, 32)
    usage_frequency = st.number_input("Usage Frequency", 0, 100, 16)
    support_calls = st.number_input("Support Calls", 0, 50, 3)
    payment_delay = st.number_input("Payment Delay", 0, 100, 12)

with col2:
    subscription_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"], index=1)
    contract_length = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"], index=2)
    total_spend = st.number_input("Total Spend", 0.0, 10000.0, 661.0)
    last_interaction = st.number_input("Last Interaction", 0, 100, 14)
    monthly_spend = st.number_input("Monthly Spend", 0.0, 10000.0, 20.05)
    support_freq = st.number_input("Support Freq", 0.0, 100.0, 0.0)

if st.button("Predict"):

    payload = {
        "Age": age,
        "Gender": gender,
        "Tenure": tenure,
        "Usage Frequency": usage_frequency,
        "Support Calls": support_calls,
        "Payment Delay": payment_delay,
        "Subscription Type": subscription_type,
        "Contract Length": contract_length,
        "Total Spend": total_spend,
        "Last Interaction": last_interaction,
        "Monthly Spend": monthly_spend,
        "Support Freq": support_freq
    }

    r = requests.post(API_URL, json=payload)

    if r.status_code == 200:
        res = r.json()

        color = "#F44336" if res["prediction"] == 1 else "#66BB6A"
        label = "HIGH churn risk" if res["prediction"] == 1 else "LOW churn risk"

        st.markdown(
            f"<div style='padding:15px; border-radius:10px; background-color:{color}; color:white'>"
            f"<h3>{label}</h3>"
            f"<p>Probability: {res['churn_probability']:.2%}</p>"
            f"<p>Prediction: {res['prediction']}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.error(r.text)

st.caption(
"Note: missing values can be left as prefilled (default values based on typical dataset statistics will be used)."
)