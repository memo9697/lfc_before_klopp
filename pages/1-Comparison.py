import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("training_dataset.csv")

st.set_page_config(page_title="Olist Dataset")
st.header("Comparison - Olist Dataset")
st.markdown("Explore the variables to understand the relationship between them and how they relate to the rating. "
            "As paterns emerge, we can intuit how the XGboost makes decisions in classifying data.")
st.sidebar.header("Variable comparison")

options = st.sidebar.radio("Select comparison",
                           options=["temps_livraison Vs retard_livraison",
                                    "temps_livraison Vs price"])

if options == "temps_livraison Vs retard_livraison":
    plot = px.scatter(
        df,
        x="temps_livraison",
        y="retard_livraison",
        color="review_score",
        title=options)
elif options == "temps_livraison Vs price":
    plot = px.scatter(
        df,
        x="temps_livraison",
        y="price",
        color="review_score",
        title=options)
    
st.plotly_chart(plot)