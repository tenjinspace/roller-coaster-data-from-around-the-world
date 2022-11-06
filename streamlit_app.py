import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('/Golden_Ticket_Award_Winners_Wood.csv')

st.title('Roller Coaster Data from Around the World')
st.markdown("Github Copilot test")

st.header("Test 1")
st.dataframe(df)

