import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset
file_path = 'vehicles_us.csv'
df = pd.read_csv(file_path)

# Header
st.header('US Vehicles Data Dashboard')
st.write("Here we will show how exploratory data analysis on the `vehicles_us.csv` dataset using pandas and plotly-express. We will visualize and summarize key features to gain insights into the data.")


# Load the dataset
st.header('Dataset')
st.write('Load the vehicles dataset from the CSV file.')

file_path = '../vehicles_us.csv'
df = pd.read_csv(file_path)
df.head()

# Show first 5 rows
st.header(' Display Basic Dataset Information')
st.write("Let's look at the first few rows, column names, and data types to understand the structure.")
df.head()
# Show column names and data types
df.info()

# Summary statistics for numerical columns
st.header('Summary Statistics')
st.write("Let's look at summary statistics for the numerical columns.")
df.describe().T

# HistogramDistribution
st.header('Histograms')
st.write("Distribution of selected numerical features.")
st.subheader('Price ')
# Histogram of price
px.histogram(df, x='price', nbins=50, title='Distribution of Price')
# Histogram of odometer
px.histogram(df, x='odometer', nbins=50, title='Distribution of Odometer Reading')

# Scatterplot
st.header( 'Scatterplots')
st.write("Explore relationships between variables using scatterplots.")
st.subheader('Price vs Odometer')
# Scatterplot: price vs odometer
px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
# Scatterplot: price vs year
px.scatter(df, x='model_year', y='price', title='Price vs Year')

# Box plot: price by condition
st.header('Box Plots')
st.write("Visualize price distribution acros different conditions.")
px.box(df, x='condition', y='price', title='Price Distribution by Condition')

# Bar chart: average price by model
st.header('Bar Charts')
st.write("Average price by vehicle model.")
avg_price_by_model = df.groupby('model')['price'].mean().reset_index()
px.bar(avg_price_by_model, x='model', y='price', title='Average Price by Model')

# Correlation heatmap for numerical features
st.header('Correlation Heatmap')
st.write("Correlation heatmap for numerical features.")
import plotly.figure_factory as ff
corr = df.corr(numeric_only=True).round(2)
fig = ff.create_annotated_heatmap(z=corr.values, x=list(corr.columns), y=list(corr.index), colorscale='Viridis')
fig.update_layout(title='Correlation Heatmap')
fig.show()

# Checkbox to filter by condition
show_condition = st.checkbox('Show only excellent condition vehicles')
if show_condition:
    filtered_df = df[df['condition'] == 'excellent']
    st.subheader('Price Distribution (Excellent Condition)')
    fig_hist_exc = px.histogram(filtered_df, x='price', nbins=50, title='Price Distribution (Excellent Condition)')
    st.plotly_chart(fig_hist_exc)

