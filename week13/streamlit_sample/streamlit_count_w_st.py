import streamlit as st

# Set title of the web app
st.title("Interactive Counter")

# Check if "click_count" exists in session state, if not, initialize it to 0
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# Display the button
button_clicked = st.button("Click to Increase Counter")

# If the button is clicked, increment the counter
if button_clicked:
    st.session_state.click_count += 1

# Display the current count
st.write(f"Total clicks: {st.session_state.click_count}")
