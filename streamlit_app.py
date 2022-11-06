import streamlit as st
import pandas as pd

# Open csv file and read it into a dataframe
df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

st.title('Roller Coaster Data from Around the World')
st.markdown("Github Copilot test")

st.header("Test 1")
st.dataframe(df)


# create a list with all the locations in df dataframe
locations = df['Location'].unique()
suppliers = df['Supplier'].unique()

location = st.selectbox('Select', locations)
supplier = st.selectbox('Select', suppliers)

filtered_df = df[(df['Location'] == location) & (df['Supplier'] == supplier)]

st.dataframe(filtered_df)
