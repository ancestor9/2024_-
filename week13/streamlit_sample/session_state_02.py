# A new version of the code that doesn't work properly!
# The country list is constantly initialised and so will only 
# contain one name

import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def get_co2_data(): 
    url = 'https://raw.githubusercontent.com/alanjones2/CO2/master/data/countries_df.csv'
    df = pd.read_csv(url)
    df = df[['Entity', 'Year', 'Code', 'Annual CO₂ emissions']]
    return df

st.title("CO2 Emissions")

df = get_co2_data()

countries = df['Entity'].unique()
selected_countries = []

country_input = st.text_input("Add a country")
if country_input in countries:
    selected_countries.append(country_input)
else:
    st.warning(f"{country_input} is not in the country list")

df1 = df.query('Entity in @selected_countries' )

# Draw a chart of CO2 emissions for selected countries
fig = px.line(df1,"Year","Annual CO₂ emissions",color="Entity")
st.plotly_chart(fig, use_container_width=True)