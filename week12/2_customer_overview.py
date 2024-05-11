import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Example data creation
def create_data():
    # Monthly sales and profit data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [10, 20, 10, 30, 50, 40, 30, 50, 60, 70, 60, 50]  # example sales data in millions
    profit = [x * 0.1 for x in sales]  # example profit data in millions
    
    # Customer sales data
    customers = ['Jordan Turner', 'Willie Xu', 'Nichole Nara', 'Kaitlyn Henderson']
    customer_sales = {
        'Jordan Turner': [2433, 540, 2849, 2462, 4820, 2355, 540],
        'Willie Xu': [2295, 2393, 777, 3578, 2071, 2375],
        'Nichole Nara': [2419, 2482, 2494, 5901],
        'Kaitlyn Henderson': [2398, 2515, 6086, 2295, 2340, 3578]
    }
    
    # Create dataframes
    df_sales = pd.DataFrame({'Month': months, 'Sales': sales, 'Profit': profit})
    df_customers = pd.DataFrame.from_dict(customer_sales, orient='index').T
    df_customers.columns = customers
    df_customers['Month'] = months[:len(df_customers)]
    
    return df_sales, df_customers

df_sales, df_customers = create_data()

# Streamlit layout
st.title('AdventureWorks - Sales Dashboard')
year = st.sidebar.selectbox('Select Year', options=[2018, 2019, 2020])
month = st.sidebar.selectbox('Select Month', options=['All'] + df_sales['Month'].tolist())

# Filtering data
if month != 'All':
    df_sales = df_sales[df_sales['Month'] == month]

# Display key metrics
col1, col2 = st.columns(2)
col1.metric("Sales", f"${df_sales['Sales'].sum():,.0f}M")
col2.metric("Customers", "18K")  # Example static value

# Sales by customer city and category
st.subheader("Sales by Top 10 Customer City and Product Category")
# This is a placeholder for a real chart which would need actual data
st.write("Placeholder chart for city and category sales.")

# Customer monthly sales data table
st.subheader("Customer Sales Details")
st.dataframe(df_customers.set_index('Month'))

# Placeholder for additional components
st.subheader("Sales by Accessories, Bikes, and Clothing")
st.write("Placeholder data for sales by category.")