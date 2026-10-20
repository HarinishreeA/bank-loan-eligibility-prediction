import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Bank Loan Prediction System")

loan_amount = st.number_input("Loan Amount")
co_income = st.number_input("Coapplicant Income")
app_income = st.number_input("Applicant Income")
monthly_exp = st.number_input("Monthly Expenses")
savings = st.number_input("Savings Amount")
age = st.number_input("Age")
loan_term = st.number_input("Loan Term")
dependents = st.number_input("Dependents")
existing_loans = st.number_input("Existing Loans")

employment = st.selectbox("Employment Type Private?", [0, 1])

if st.button("Predict"):
    input_data = np.array([[loan_amount, co_income, app_income,
                            monthly_exp, savings, age,
                            loan_term, dependents,
                            existing_loans, employment]])

    result = model.predict(input_data)

    if result[0] == 0:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
