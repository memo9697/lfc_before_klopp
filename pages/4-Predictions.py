import streamlit as st
import requests
import json

st.set_page_config(page_title="Predictions")
st.header("#")
st.markdown("#")
st.sidebar.header("Make Prediction")

price_pred = st.sidebar.text_input("price")
temps_livraison_pred = st.sidebar.text_input("temps_livraison")

make_pred_API = st.sidebar.button("Predict")

if make_pred_API:
    url = f"http://localhost:8000/{float(price_pred)}/{int(temps_livraison_pred)}"

    response = requests.get(url)

    if response.status_code == 200:
        score_pred = response.json()["prediction"]
        st.success(f"Prediction result: {score_pred} ")
    else:
        st.error("Error in prediction request.")