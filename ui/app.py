import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src import preprocess, train_model, recommend_rules, feedback

st.title("Smart Firewall Rule Recommender")

uploaded_file = st.file_uploader("Upload Log File", type="csv")
if uploaded_file:
    df = preprocess.load_and_clean_data(uploaded_file)
    st.write("Log Data", df.head())
    
    if st.button("Train Model"):
        train_model.train_model(df)
        st.success("Model Trained Successfully!")

    port = st.number_input("Enter Port Number to Check")
    if st.button("Get Recommendation"):
        result = recommend_rules.recommend_rule(port)
        st.info(f"Recommended Action: {result}")
