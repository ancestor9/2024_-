import streamlit as st
import streamlit as st 
import pandas as pd 
import plotly.express as px 

import streamlit as st
import sqlite3

def create_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items
                 (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')
    conn.commit()
    conn.close()

create_db()

# Step 2: CRUD Function Implementation

def add_item(name, description):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    items = c.fetchall()
    conn.close()
    return items

def update_item(id, name, description):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('UPDATE items SET name = ?, description = ? WHERE id = ?', (name, description, id))
    conn.commit()
    conn.close()

def delete_item(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Step 3: User Interface Design

st.title('Simple CRUD App')

# Add Item
with st.form("add_item_form"):
    st.write("Add a new item")
    new_name = st.text_input('Name', key="add_name")
    new_description = st.text_area('Description', key="add_description")
    submit_add = st.form_submit_button("Add Item")
    if submit_add:
        add_item(new_name, new_description)
        st.success('Item added successfully!')

# Update and Delete Operations need a selection of item ID
items = get_items()
item_id_list = [str(item[0]) for item in items]
selected_id = st.selectbox('Select an item ID to update or delete', options=item_id_list)

if selected_id:
    # Display selected item details
    selected_item = next((item for item in items if str(item[0]) == selected_id), None)
    if selected_item:
        st.write(f"ID: {selected_item[0]}, Name: {selected_item[1]}, Description: {selected_item[2]}")

        # Update Form
        with st.form("update_item_form"):
            st.write("Update the selected item")
            updated_name = st.text_input('New Name', value=selected_item[1], key="update_name")
            updated_description = st.text_area('New Description', value=selected_item[2], key="update_description")
            submit_update = st.form_submit_button("Update Item")
            if submit_update:
                update_item(selected_item[0], updated_name, updated_description)
                st.success('Item updated successfully!')

        # Delete Button
        if st.button('Delete Item'):
            delete_item(selected_item[0])
            st.success('Item deleted successfully!')
            st.experimental_rerun() # Rerun the app to refresh the items list and input forms


# Display the current count
st.write(f"Total clicks: {st.session_state.click_count}")


# # Initialization
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'

# # Session State also supports attribute based syntax
# if 'key' not in st.session_state:
#     st.session_state.key = 'value'
  
# # Read
# st.write(st.session_state.key)
# st.session_state.key = 'value2'     # Attribute API
# st.session_state['key'] = 'value2'  # Dictionary like API
# st.write(st.session_state)
# # With magic:
# st.session_state
# # Delete a single key-value pair
# del st.session_state['key']
# # Delete all the items in Session state
# for key in st.session_state.keys():
#     del st.session_state[key]