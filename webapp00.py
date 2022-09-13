

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
  st.title('Receitas com Carne')
  st.write("ALgumas ideia de receitas com Carne que talvez voce possa gostar\
  [Receitas Com Carne](https://www.tudogostoso.com.br/categorias/1004-carnes)")
  
  testeteste = st.selectbox("Tipos de Carne", ("Carne Moida", "Carne Seca", "Carne de Porco"))
  if testeteste == "Carne Moida":
    st.write("Receitas com Carne Moida, podem ter diferentes usos sendo muito versatil no seu preparo \
    [Mais Receitas](https://www.sabornamesa.com.br/receita-de-carnes/receitas-com-carne-moida)")
  elif testeteste == "Carne Seca":
    st.write("Receitas com Carne Seca \ 
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-carne-seca/)")
  elif testeteste == "Carne de Porco":
    st.write("Receitas com Carne de Porco \ 
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-carne-de-porco/)")
    
  
 
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
