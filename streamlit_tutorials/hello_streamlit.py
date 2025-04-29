import streamlit as st
import pandas as pd
import numpy as np

## title of the application
st.title("Data Analysis App")

## display simple dataframe
df = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50],
    "C": [100, 200, 300, 400, 500]
})
st.write("This is a simple dataframe:")
st.dataframe(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)