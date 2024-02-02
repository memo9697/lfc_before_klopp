import streamlit as st
import requests

st.set_page_config(page_title="Training")
st.header("Training - Olist Dataset")
st.markdown("Train model to make predictions on customer satisfaction regarding price and delivery_time.")
st.sidebar.header("Train model")

launch_training = st.sidebar.button("Training")

if launch_training:
    url = f"http://localhost:8000/train_model"

    response = requests.get(url)

    if response.status_code == 200:
        response = response.json()["Response"]
        st.success(f"Model training message: {response}")
    else:
        print("Pause")
else:
    url = f"http://localhost:8000/infos"

    response = requests.get(url)

    if response.status_code == 200:
        message = response.json()[0]
        st.success(f"API welcome message: {message}")
    else:
        st.error("Error in welcome request.")
