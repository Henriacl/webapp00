

import streamlit as st
import pandas as pd 
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("PrePear")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Site de Receitas do Mackenzie Campinas ")

st.sidebar.title("Receitas")
paginaselecionada = st.sidebar.selectbox("Receitas", ["Carnes", "Peixes", "Aves", "Vegetariano", "Vegano"])

if paginaselecionada == "Carnes": 
  st.title("Receitas com Carne")
  st.selectbox("Receitas", ["Carnes", "Peixes", "Aves", "Vegetariano", "Vegano"])
elif paginaselecionada == "Peixes": 
  st.title("Receitas com Peixe")
  
