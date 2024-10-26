import streamlit as st
import pandas as pd
st.title('🎈 Machine Learning app ')

st.info('this is app build a machine learning model')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
