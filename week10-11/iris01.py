import streamlit as st
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import datasets

# Define a function to create the scatter plot
def create_scatter_plot():
    st.title("Iris Dataset Scatter Plot")
    st.write("This app displays a scatter plot of the Iris dataset.")
    # Load the Iris dataset
    iris = datasets.load_iris()

    # Create the scatter plot
    _, ax = plt.subplots()
    scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
    ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
    _ = ax.legend(
        scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
    )

    return plt.gcf()

def upload_hr_data():
    st.title("Upload Data")
    st.write("Please upload a CSV file containing HR data.")

    # File upload section
    uploaded_file = st.file_uploader("Upload CSV", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.write("Uploaded HR Data:")
        st.dataframe(df)

# Streamlit UI code
def main():
    # Create the scatter plot using the user-defined function
    scatter_plot = create_scatter_plot()
    # Display the plot in Streamlit
    st.pyplot(scatter_plot)
    # Upload external file
    upload_hr_data()

if __name__ == "__main__":
    main()
