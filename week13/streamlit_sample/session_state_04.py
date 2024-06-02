import streamlit as st
import pandas as pd
import plotly.express as px

# This code is done by chat-GPT

# Function to retrieve CO2 data
@st.cache_data
def get_co2_data(): 
    url = 'https://raw.githubusercontent.com/alanjones2/CO2/master/data/countries_df.csv'
    df = pd.read_csv(url)
    df = df[['Entity', 'Year', 'Code', 'Annual CO₂ emissions']]
    return df

# Title of the Streamlit app
st.title("CO2 Emissions")

# Retrieve CO2 data
df = get_co2_data()

# List of unique countries
countries = df['Entity'].unique()

# List to store selected countries
selected_countries = st.session_state.selected_countries if 'selected_countries' in st.session_state else []

# Text input for adding a country
country_input = st.text_input("Add a country")

# Check if the entered country is valid and add it to the list of selected countries
if country_input in countries:
    if country_input not in selected_countries:
        selected_countries.append(country_input)
else:
    st.warning(f"{country_input} is not in the country list")

# Store selected countries in session state
st.session_state.selected_countries = selected_countries

# Filter data for selected countries
df_selected = df[df['Entity'].isin(selected_countries)]

# Draw a chart of CO2 emissions for selected countries
if not df_selected.empty:
    fig = px.line(df_selected, "Year", "Annual CO₂ emissions", color="Entity")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("No data available for the selected countries.")
