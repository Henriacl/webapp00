

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
  
  testeteste = st.selectbox("Tipos de Peixe", ("Salmao", "Atum", "Tilapia"))
  if testeteste == "Salmao":
    st.write("Receitas com Salmao \
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-salmao/)")
  elif testeteste == "Atum":
    st.write("Receitas com Atum \
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-atum-em-lata/)")
  elif testeteste == "Tilapia":
    st.write("Receitas com Tilapia \
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-tilapia/)")

elif paginaselecionada == 'Aves':
  st.title('Receitas com Aves')
  st.write("receitas com aves diferentes\
  [Leia mais](https://www.tudogostoso.com.br/categorias/1009-aves)")
  
  testeteste = st.selectbox("Tipos de Aves", ("Frango", "Pato", "Pinguin"))
  if testeteste == "Frango":
    st.write("Receitas com Frango \
    [Mais Receitas](https://www.sabornamesa.com.br/receita-de-carnes/peito-de-frango-simples-e-facil)")
  elif testeteste == "Pato":
    st.write("Receitas com Pato \
    [Mais Receitas](https://www.receiteria.com.br/receitas-de-pato/)")
  elif testeteste == "Pinguin":
    st.write("Receitas com penguin \
    [Mais Receitas](https://www.tudoreceitas.com/receitas-de-peru-1101/)")
  
elif paginaselecionada == 'Vegetarianas':
  st.title('Receitas Vegetarianas')
  st.write("Receitas diversas vegetarianas \
  [Leia mais](https://www.receiteria.com.br/receitas-vegetarianas/)")
  
     
elif paginaselecionada == 'Veganas':
  st.title('Receitas Veganas')
  st.write("receitas diversas veganas\
  [Leia mais](https://www.receiteria.com.br/receitas-veganas/)")
  
  
  from PIL import Image
image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')
