import streamlit as st
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Define a function to create the scatter plot
def create_scatter_plot():
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

# Define a function to apply StandardScaler to the dataset
def apply_standard_scaler():
    # Load the Iris dataset
    iris = datasets.load_iris()

    # Apply StandardScaler to the dataset
    scaler = StandardScaler()
    iris_scaled = scaler.fit_transform(iris.data)

    # Create a DataFrame with the scaled data
    iris_scaled_df = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)

    return iris_scaled_df

# Streamlit UI code
def main():
    st.title("Iris Dataset Analysis")
    st.write("This app displays a scatter plot of the Iris dataset and the scaled data using StandardScaler.")

    # Create the scatter plot using the user-defined function
    scatter_plot = create_scatter_plot()

    # Display the scatter plot in Streamlit
    st.pyplot(scatter_plot)

    # Apply StandardScaler and display the scaled data as a DataFrame
    st.subheader("Scaled Iris Dataset")
    iris_scaled_df = apply_standard_scaler()
    st.write("Scaled Iris Data:")
    st.dataframe(iris_scaled_df)

if __name__ == "__main__":
    main()