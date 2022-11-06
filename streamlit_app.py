import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

st.title('Solar Employment by Sector, 2010')
st.dataframe(df)
