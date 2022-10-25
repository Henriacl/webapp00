

import streamlit as st
from PIL import Image

st.sidebar.title("Receitas")
paginaselecionada = st.sidebar.selectbox('Receitas', ["Inicio", "Carnes", "Peixes", "Aves", "Vegetarianas", "Veganas", "teste"])

if paginaselecionada == "Inicio":
  st.title("PrePear")
  st.header("Site de Receitas do Mackenzie Campinas")
  st.write("Quem somos: site de receitas do mackenzie campinas feito por henrique, miguel e thalita")

  
elif paginaselecionada == "teste":
  st.title("testando")
  input("valor em gramas")
  
  
  


