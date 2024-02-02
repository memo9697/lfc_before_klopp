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
                           options=["temps_livraison",
                                    "price"])

show_df = df.filter(items=[options, "review_score"])

plot1 = px.histogram(
        show_df,
        x=show_df[options],
        title=f"{options} Histogram",
        nbins=30,
        color="review_score")

st.plotly_chart(plot1)