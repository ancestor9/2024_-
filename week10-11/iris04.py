import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

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

# Define a function to perform KNN classification
def knn_classification(X, y):
    # Load the Iris dataset
    iris = datasets.load_iris()
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a KNN classifier
    knn_classifier = KNeighborsClassifier(n_neighbors=3)  # You can adjust the number of neighbors as needed

    # Train the classifier
    knn_classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn_classifier.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Generate classification report
    report = classification_report(y_test, y_pred, target_names=iris.target_names)

    return knn_classifier, accuracy, report

# Define a function to make predictions
def make_predictions(classifier, input_values):
    # Load the Iris dataset
    iris = datasets.load_iris()
    # Perform predictions using the trained KNN classifier
    predicted_class = classifier.predict([input_values])[0]
    predicted_class_name = iris.target_names[predicted_class]

    return predicted_class, predicted_class_name

# Streamlit UI code
def main():
    st.title("Iris Dataset Analysis and KNN Classification")
    st.write("This app displays a scatter plot of the Iris dataset, the scaled data using StandardScaler, and performs KNN classification.")

    # Create the scatter plot using the user-defined function
    scatter_plot = create_scatter_plot()

    # Display the scatter plot in Streamlit
    st.pyplot(scatter_plot)

    # Apply StandardScaler and display the scaled data as a DataFrame
    st.subheader("Scaled Iris Dataset")
    iris_scaled_df = apply_standard_scaler()
    st.write("Scaled Iris Data:")
    st.dataframe(iris_scaled_df)

    # Perform KNN classification
    st.subheader("KNN Classification Results")
    X = iris_scaled_df.values  # Features
    y = datasets.load_iris().target  # Target variable

    knn_classifier, accuracy, report = knn_classification(X, y)

    # Display the results
    st.write(f"Accuracy: {accuracy}")
    st.write("Classification Report:")
    st.text(report)
    # Load the Iris dataset
    iris = datasets.load_iris()
    # User input for making predictions
    st.subheader("Make Predictions")
    st.write("Enter values for four features to make predictions:")
    input_values = []


    for i in range(4):
        input_value = st.number_input(f"Enter {iris.feature_names[i]}", min_value=0.0, step=0.01)
        input_values.append(input_value)

    if st.button("Make Predictions"):
        predicted_class, predicted_class_name = make_predictions(knn_classifier, input_values)
        st.write(f"Predicted Class: {predicted_class_name}")

if __name__ == "__main__":
    main()