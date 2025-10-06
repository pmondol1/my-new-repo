import streamlit as st
import pandas as pd

st.title("Vehicle Data Explorer")

df = pd.read_csv("vehicles_us.csv")
st.write("Here's a preview of the dataset:")
st.dataframe(df)
