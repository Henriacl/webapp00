# myFirstStreamlitApp.py
  
#import the library
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("PrePear")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Site de Receitas do Mackenzie Campinas ")

st.title("Receitas")
st.sidebar.selectbox("Trends", ["Tiktok", "Instagram", "FaceBook"])
