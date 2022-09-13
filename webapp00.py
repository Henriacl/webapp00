

import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("PrePear")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Site de Receitas do Mackenzie Campinas ")

st.sidebar.title("Receitas")
paginaselecionada = st.sidebar.selectbox('Receitas', ["Carnes", "Peixes", "Aves", "Vegetariano", "Vegano"])

if paginaselecionada == 'Carnes': 
  st.title('Receitas com Carne')

elif paginaselecionada == 'Peixes': 
  st.title('com Peixe')
  
elif paginaselecionada == 'Aves':
  st.title('Receitas com Carne')
  
elif paginaselecionada == 'Vegetariano':
  st.title('Receitas com Carne')
    
elif paginaselecionada == 'Vegano':
  st.title('Receitas com Carne')
