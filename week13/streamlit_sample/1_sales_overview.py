import streamlit as st
import pandas as pd
import plotly.express as px

# Example data creation
def create_data():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [10, 20, 10, 30, 50, 40, 30, 50, 60, 70, 60, 50]
    profit = [x * 0.1 for x in sales]
    df = pd.DataFrame({'Month': months, 'Sales': sales, 'Profit': profit})
    return df

df = create_data()

# Creating a simple sidebar with filter options
year = st.sidebar.selectbox('Select Year', options=[2018, 2019, 2020])
month = st.sidebar.selectbox('Select Month', options=['All'] + df['Month'].tolist())

# Filtering data based on selections
if month != 'All':
    df = df[df['Month'] == month]

# Displaying key metrics
st.header(f"Sales Dashboard for {year}")
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Sales", f"${df['Sales'].sum():,.0f}M")
col2.metric("Profit", f"${df['Profit'].sum():,.0f}M")
col3.metric("Return on Sales", f"{(df['Profit'].sum() / df['Sales'].sum() * 100):.2f}%")

# Sales & Profit by Month Line Chart
fig = px.line(df, x='Month', y='Sales', title='Sales by Month')
fig.add_scatter(x=df['Month'], y=df['Profit'], mode='lines', name='Profit')
st.plotly_chart(fig, use_container_width=True)

# Placeholder for additional charts and metrics
st.subheader("Sales by Top 10 Customers")
st.write("Placeholder for customer sales data.")

st.subheader("Sales by Top 10 Products")
st.write("Placeholder for product sales data.")

