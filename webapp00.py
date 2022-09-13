

import streamlit as st
import pandas as pd 
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("PrePear")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Site de Receitas do Mackenzie Campinas ")


st.sidebar.selectbox("Receitas", ["Carnes", "Peixes", "Aves", "Vegetariano", "Vegano"])
st.sidebar.selectbox("Trends", ["Tiktok", "Instagram", "FaceBook"])

if selectedoption == "Carnes":
  st.title("Receitas com Carne")
  st.selectbox("opçao", ["opr1", "opt2"])
  
if selectedoption == "Peixes":
  st.title("Receitas com Peixes")
  st.selectbox("opçao", ["opr1", "opt2"])
  
elif return0 
