import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="NBA Active Players Data",
    page_icon="⬇",
    layout="wide"
)

# Page title
st.title("NBA Active Players Data")

# Caching data for improved performance
@st.cache_data(ttl=3600)
def get_data():
    #data = pd.read_csv("./players.csv")
    data = pd.read_csv("./players.csv", encoding="latin1")

    return data

# Loading and preprocessing data
data = get_data()
print(data.sample(20))
data['birthday'] = pd.to_datetime(data['birthday'], format=None)

# Sidebar filters
player_position = st.sidebar.multiselect(
    "Player position",
    data['position'].unique().tolist(),
    default=["Center"]
)

if player_position:
    data = data[data['position'].isin(player_position)]

player_countries = st.sidebar.multiselect(
    "Player country",
    data['country'].unique().tolist()
)

if player_countries:
    data = data[data['country'].isin(player_countries)]

player_school = st.sidebar.multiselect(
    "Player school",
    data['school'].unique().tolist()
)

if player_school:
    data = data[data['school'].isin(player_school)]

# Resetting index for visualization
data = data.reset_index(inplace=False)

# Displaying player information
col1, col2 = st.columns(2)
for _, row in data.iterrows():
    with col1:
        st.write(row.playerid)
        st.image("./img/" + str(row.playerid) + ".png")
    with col2:
        st.table(row)