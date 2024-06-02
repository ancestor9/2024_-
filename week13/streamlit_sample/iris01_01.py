import streamlit as st
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import random

st.title("Iris Dataset")
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target


def create_seaborn():      
    # 1. iris 데이터셋을 불러옵니다.
    st.write(df)
    
    # 2. Streamlit을 사용하여 두 개의 변수를 입력받습니다.
    st.title("Iris Dataset Scatter Plot")
    st.write("Select two features to plot:")

    feature_x = st.selectbox("Select the first feature:", df.columns)
    feature_y = st.selectbox("Select the second feature:", df.columns)

    # 3. 선택한 두 변수로 산점도를 그립니다.
    if feature_x and feature_y:
        st.write("This app displays a scatter plot of the Iris dataset.")
        fig, ax = plt.subplots()
        sns.scatterplot(x=feature_x, y=feature_y, 
                        hue='target', palette='viridis', 
                        data= df, ax=ax)
        ax.set_xlabel(feature_x)
        ax.set_ylabel(feature_y)
        ax.set_title(f'Scatter plot of {feature_x} vs {feature_y}')
        
        return st.pyplot(fig)

# Define a function to create the scatter plot
def create_scatter_plot():
    st.title("Iris Random Dataset Scatter Plot")
    st.write("This app displays a scatter plot of the Iris dataset by Random.")
    # Load the Iris dataset

    # 1. 임의의 두 개 변수를 선택합니다.
    features = random.sample(df.columns.tolist(), 2)
    st.write(f'임의선택 2개 {features}')
    # Create the scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x=features[0], y=features[1], 
                    hue='target', palette='viridis',
                    data=df, ax=ax)
    ax.set_xlabel(features[0])
    ax.set_ylabel(features[1])
    ax.set_title('Scatter plot of two random features from the iris dataset')
    
    # Display the plot in the Streamlit app
    return st.pyplot(fig)

def upload_hr_data():
    st.title("Upload Data")
    st.write("Please upload a CSV file.")

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
    # 2개 변수를 입력받아 그리기
    create_seaborn()
    
    # Create the scatter plot by random
    create_scatter_plot()
    
    # Upload external file
    upload_hr_data()

if __name__ == "__main__":
    main()