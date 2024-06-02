import streamlit as st
st.title("Without session state")

count = 0

increment = st.button("click button but still 1")

if increment:
    count += 1
    
st.write("Count =", count)
