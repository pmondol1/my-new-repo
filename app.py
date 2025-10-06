import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
file_path = 'vehicles_us.csv'
df = pd.read_csv(file_path)

# Header
st.header('US Vehicles Data Dashboard')

# Histogram
st.subheader('Price Distribution')
fig_hist = px.histogram(df, x='price', nbins=50, title='Distribution of Price')
st.plotly_chart(fig_hist)

# Scatterplot
st.subheader('Price vs Odometer')
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_scatter)

# Checkbox to filter by condition
show_condition = st.checkbox('Show only excellent condition vehicles')
if show_condition:
    filtered_df = df[df['condition'] == 'excellent']
    st.subheader('Price Distribution (Excellent Condition)')
    fig_hist_exc = px.histogram(filtered_df, x='price', nbins=50, title='Price Distribution (Excellent Condition)')
    st.plotly_chart(fig_hist_exc)

