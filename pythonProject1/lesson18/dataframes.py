import pandas as pd
import streamlit as st

st.header("Display dataframes")

data = pd.DataFrame({
    'Name': ['Alice','Bob','Charlie','David','Eva'],
    'Age':[24, 27, 32, 29, 23],
    'City':['New York', 'Los Angeles', ' Chicago', 'Houston', 'Phoenix']
})
st.dataframe(data)