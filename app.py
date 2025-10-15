import streamlit as st
import pandas as pd
import plotly.express as px
import io


# Header
st.header('US Vehicles Data Dashboard')
st.write("Welcome! This dashboard helps you explore trends in used vehicle listings across the U.S. It allows users to interactively visualize trends in price, mileage, condition, and more using a clean and intuitive interface.")


# Load the dataset
st.header('Dataset')
file_path = 'vehicles_us.csv'
df = pd.read_csv(file_path)
df = df.convert_dtypes()


# Display the cleaned DataFrame
st.dataframe(df.head())
st.markdown("---")


# Histograms
st.header('Histograms')
st.subheader('Price')
fig_price = px.histogram(df, x='price', nbins=50, title='Distribution of Price')
st.plotly_chart(fig_price)


# Scatterplots
st.header('Scatterplots')
fig_scatter1 = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_scatter)

# Checkbox to filter by condition
if st.checkbox("Show only vehicles in excellent condition"):
    filtered_df = df[df["condition"] == "excellent"]
    fig_filtered = px.histogram(filtered_df, x="price", title="Price Distribution (Excellent Condition)")
    st.plotly_chart(fig_filtered)


st.markdown("---")
st.write("Thank you for exploring the dashboard!")

