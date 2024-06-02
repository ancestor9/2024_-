import streamlit as st
import pandas as pd

# Sample dataframe
df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35]
})

if 'final_dataframe' not in st.session_state:
    # If there is no value called final_dataframe in the session state,
    st.session_state.final_dataframe = df
    # Initial value setting: Insert initial dataframe data into the final_dataframe key in session_state.

# Display the dataframe using st.table
st.table(df)

# The code below changes the final_dataframe value in the session_state object every time the dataframe is manipulated.
# The display continues to change as it is modified.
st.table(st.session_state.final_dataframe)