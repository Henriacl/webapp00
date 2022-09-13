

import streamlit as st

st.sidebar.title("Receitas")
paginaselecionada = st.sidebar.selectbox('Receitas', ["Inicio", "Carnes", "Peixes", "Aves", "Vegetarianas", "Veganas"])

if paginaselecionada == "Inicio":
  st.title("PrePear")
  st.header("Site de Receitas do Mackenzie Campinas")
  st.write("Quem somos \nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \
  Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

elif paginaselecionada == 'Carnes':
  testeteste = st.selectbox("qual receita", ("carne1", "carne2", "carne3"))
  if testeteste == "carne1":
    st.write("receita1")
  elif testeteste == "carne2":
    st.write("receita2")
  elif testeteste == "carne3:
    st.write("receita3")
    
  st.title('Receitas com Carne')
  st.write("aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
  Excepteur sint\
  [Receitas Com Carne](https://paladar.estadao.com.br/noticias/receita,bife-wellington-como-fazer-o-classico-em-casa-a-prova-de-erro,70003582982)")
 
elif paginaselecionada == 'Peixes': 
  st.title('Receitas com Peixe')
  st.write("aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
  Excepteur sint\
  [Leia mais](https://www.sabornamesa.com.br/receitas-de-peixes/file-de-peixe-simples-e-facil)")

elif paginaselecionada == 'Aves':
  st.title('Receitas com Aves')
  
elif paginaselecionada == 'Vegetarianas':
  st.title('Receitas Vegetarianas')
    
elif paginaselecionada == 'Veganas':
  st.title('Receitas Veganas')
