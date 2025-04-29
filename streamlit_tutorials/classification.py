import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cache the function to improve performance by avoiding reloading the data multiple times
@st.cache
def load_data():
    """Load the Iris dataset."""
    iris = load_iris()  # Load the Iris dataset from sklearn
    # Create a DataFrame with feature data and add a column for species (target)
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target  # Add the target column (species)
    return df, iris.target_names  # Return the DataFrame and target names

# Load the dataset and target names
df, target_names = load_data()

# Initialize and train a Random Forest Classifier using the dataset
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])  # Train the model on feature columns and target column

# Streamlit app title
st.title("Iris Flower Classification")

# Sidebar sliders for user input of feature values
sepal_length = st.sidebar.slider(
    "Sepal Length", 
    float(df['sepal length (cm)'].min()), 
    float(df['sepal length (cm)'].max())
)
sepal_width = st.sidebar.slider(
    "Sepal Width", 
    float(df['sepal width (cm)'].min()), 
    float(df['sepal width (cm)'].max())
)
petal_length = st.sidebar.slider(
    "Petal Length", 
    float(df['petal length (cm)'].min()), 
    float(df['petal length (cm)'].max())
)
petal_width = st.sidebar.slider(
    "Petal Width", 
    float(df['petal width (cm)'].min()), 
    float(df['petal width (cm)'].max())
)

# Combine user inputs into a single list for prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Make a prediction using the trained model
prediction = model.predict(input_data)

# Display the prediction result
st.write("Prediction: ", target_names[prediction][0])