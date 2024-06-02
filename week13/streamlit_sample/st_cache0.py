import streamlit as st
import time

# Function to simulate an expensive computation
@st.cache_data
def expensive_computation(n):
    # Simulate computation time
    time.sleep(2)
    return n * 2

# Function to simulate a non-expensive computation
def non_expensive_computation(n):
    return n * 2

# Main code
st.title("Cache vs No-cache")

# Option to choose computation type
computation_type = st.radio("Select computation type:", ("Expensive", "Non-expensive"))

# Input field to enter a number
number = st.number_input("Enter a number:", value=5)

# Perform computation based on selected type
if computation_type == "Expensive":
    result = expensive_computation(number)
else:
    result = non_expensive_computation(number)

# Display result
st.write(f"Result: {result}")
