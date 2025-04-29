# Importing necessary libraries
import streamlit as st  # Streamlit is used for building interactive web apps
import pandas as pd  # Pandas is used for data manipulation and analysis

# Setting the title of the Streamlit app
st.title("Streamlit text input")

# Text input widget to get the user's name
name = st.text_input("Enter your name")
if name:  # If the user enters a name, display a greeting message
    st.write(f"Hello {name}!")

# Slider widget to get the user's age
age = st.slider("Enter your age", min_value=0, max_value=100, value=25)  # Default age is set to 25
st.write(f"Your age is {age}")  # Display the selected age

# Dropdown (selectbox) widget to choose a favorite programming language
programming_language_options = ["Python", "Java", "C++", "JavaScript"]  # List of programming languages
programming_language = st.selectbox("Select your favorite programming language", programming_language_options)
st.write(f"Your favorite programming language is {programming_language}")  # Display the selected language

# Creating a sample DataFrame with some data
data = {
    "Name": ["Alice", "Bob", "Charlie"],  # Names of individuals
    "Age": [25, 30, 35],  # Corresponding ages
    "City": ["New York", "Los Angeles", "Chicago"]  # Corresponding cities
}
df = pd.DataFrame(data)  # Convert the dictionary into a Pandas DataFrame

# Save the DataFrame to a CSV file named 'sampledata.csv'
df.to_csv("sampledata.csv", index=False)  # 'index=False' prevents writing row indices to the file

# Display the DataFrame in the Streamlit app
st.write(df)

# File uploader widget to allow users to upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])  # Restrict file type to CSV
if uploaded_file is not None:  # Check if a file has been uploaded
    df = pd.read_csv(uploaded_file)  # Read the uploaded CSV file into a DataFrame
    st.write(df)  # Display the contents of the uploaded file