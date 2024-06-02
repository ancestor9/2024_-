import streamlit as st
import pandas as pd

# Large data file path
url = 'https://raw.githubusercontent.com/alanjones2/CO2/master/data/countries_df.csv'

# Function to load data without caching
def load_data_without_caching():
    st.write("Loading data without caching...")
    df = pd.read_csv(url)
    data = df[['Entity', 'Year', 'Code', 'Annual CO₂ emissions']]
    return data



# Function to load data with caching
@st.cache_data
def load_data_with_caching():
    st.write("Loading data with caching...")  # Move this line outside of the cached function
    df = pd.read_csv(url)
    data = df[['Entity', 'Year', 'Code', 'Annual CO₂ emissions']]
    return data

# Main code
st.title("Caching Example")

# Checkbox to toggle caching
use_caching = st.checkbox("Use caching")

# If caching is enabled, load data with caching, otherwise load data without caching
if use_caching:
    data = load_data_with_caching()
else:
    data = load_data_without_caching()


# Display some information about the loaded data
st.write("Data loaded successfully!")
st.write(f"Number of rows: {len(data)}")
st.write("Sample data:")
st.write(data.head())