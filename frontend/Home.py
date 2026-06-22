import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Churn Prediction")

st.markdown("""
This service estimates the probability of customer churn using a machine learning model.

The prediction is based on customer characteristics and their interaction history with the company.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("""
**Tech Stack**

• Streamlit (Frontend)

• FastAPI (Backend)

• Machine Learning (Logistic Regression)

• SQLite Database
""")

with col2:
    st.success("""
**Features**

• Prediction for a single customer
               
• Prediction history
               
• Batch prediction via CSV file *(under development)*

• Data visualization *(under development)*
""")

st.divider()

st.subheader("About the Project")

st.write("""
The goal of this project is to automate customer churn risk estimation based on information about user activity, subscription type, and service interactions.

The application allows generating predictions both for individual customers and for groups of customers uploaded via a CSV file.
""")

st.divider()

st.markdown("""
### Navigation

Use the sidebar menu to navigate through the application pages:

- **Single Prediction** — prediction for one customer
- **Batch Prediction** — bulk prediction for a set of customers
- **History** — prediction history
""")