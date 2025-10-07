import streamlit as st
import pandas as pd
import plotly.express as px
import io


# Header
st.header('US Vehicles Data Dashboard')
st.write("Here we will show how exploratory data analysis on the `vehicles_us.csv` dataset using pandas and plotly-express. We will visualize and summarize key features to gain insights into the data.")


# Load the dataset
st.header('Dataset')
st.write('Load the vehicles dataset from the CSV file.')

# Clean up the DataFrame before displaying
df_clean = df.convert_dtypes()  # Converts columns to best possible types
df_clean = df_clean.fillna('')  # Optional: fill NaNs with empty strings

st.dataframe(df_clean)


file_path = 'vehicles_us.csv'
df = pd.read_csv(file_path)
# Clean up column types to avoid Arrow serialization errors
df = df.convert_dtypes()

#Display the dataframe
st.dataframe(df.head())

# Dataset diagnostics
st.subheader("Dataset Diagnostics")
st.write("Let's inspect the dataset to ensure it's ready for visualization.")

# Show shape
st.write("**Shape of the dataset:**", df.shape)

# Show missing values
st.write("**Missing values per column:**")
st.write(df.isna().sum())

# Show data types
st.write("**Data types of each column:**")
st.write(df.dtypes)


# Show first 5 rows
st.header('Display Basic Dataset Information')
st.write("Let's look at the first few rows, column names, and data types to understand the structure.")

# Display first 5 rows
st.dataframe(df.head())

# Show column names and data types
buffer = io.StringIO()
df.info(buf=buffer)
info_text = buffer.getvalue()
st.text(info_text)


# Summary statistics for numerical columns
st.header('Summary Statistics')
st.write("Let's look at summary statistics for the numerical columns.")
st.dataframe(df.describe().T)


# Histograms
st.header('Histograms')
st.write("Distribution of selected numerical features.")
st.subheader('Price')
fig_price = px.histogram(df, x='price', nbins=50, title='Distribution of Price')
st.plotly_chart(fig_price)

st.subheader('Odometer')
fig_odometer = px.histogram(df, x='odometer', nbins=50, title='Distribution of Odometer Reading')
st.plotly_chart(fig_odometer)

# Scatterplots
st.header('Scatterplots')
st.write("Explore relationships between variables using scatterplots.")
st.subheader('Price vs Odometer')
fig_scatter1 = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_scatter1)

st.subheader('Price vs Year')
fig_scatter2 = px.scatter(df, x='model_year', y='price', title='Price vs Year')
st.plotly_chart(fig_scatter2)

# Box plot
st.header('Box Plots')
st.write("Visualize price distribution across different conditions.")
fig_box = px.box(df, x='condition', y='price', title='Price Distribution by Condition')
st.plotly_chart(fig_box)

# Bar chart
st.header('Bar Charts')
st.write("Average price by vehicle model.")
avg_price_by_model = df.groupby('model')['price'].mean().reset_index()
fig_bar = px.bar(avg_price_by_model, x='model', y='price', title='Average Price by Model')
st.plotly_chart(fig_bar)

# Correlation heatmap
st.header('Correlation Heatmap')
st.write("Correlation heatmap for numerical features.")
import plotly.figure_factory as ff
corr = df.corr(numeric_only=True).round(2)
fig_heatmap = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    colorscale='Viridis'
)
fig_heatmap.update_layout(title='Correlation Heatmap')
st.plotly_chart(fig_heatmap)


# Checkbox to filter by condition
show_condition = st.checkbox('Show only excellent condition vehicles')
if show_condition:
    filtered_df = df[df['condition'] == 'excellent']
    st.subheader('Price Distribution (Excellent Condition)')
    fig_hist_exc = px.histogram(filtered_df, x='price', nbins=50, title='Price Distribution (Excellent Condition)')
    st.plotly_chart(fig_hist_exc)

