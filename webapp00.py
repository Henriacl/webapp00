

import streamlit as st
from PIL import Image

st.sidebar.title("Receitas")
paginaselecionada = st.sidebar.selectbox('Receitas', ["Inicio", "Carnes", "Peixes", "Aves", "Vegetarianas", "Veganas"])

if paginaselecionada == "Inicio":
  st.title("PrePear")
  st.header("Site de Receitas do Mackenzie Campinas")
  st.write("Quem somos: site de receitas do mackenzie campinas feito por henrique, miguel e thalita")

elif paginaselecionada == 'Carnes':
  st.title('Receitas com Carne')
  st.write("ALgumas ideia de receitas com Carne que talvez voce possa gostar\
  [Receitas Com Carne](https://www.tudogostoso.com.br/categorias/1004-carnes)")
  
  testeteste = st.selectbox("Tipos de Carne", ("Carne Moida", "Carne Seca", "Carne de Porco"))
  if testeteste == "Carne Moida":
    image = Image.open("imagensnovo/carne moida.jfif")
    st.write("Receitas com Carne Moida, podem ter diferentes usos sendo muito versatil no seu preparo \
    [Mais Receitas](https://www.sabornamesa.com.br/receita-de-carnes/receitas-com-carne-moida)")
    st.image(image)
  elif testeteste == "Carne Seca":
    image = Image.open("imagensnovo/carne seca.jfif")
    st.write("Receita com Carne Seca \ 
    caldo de mandioca com carne seca n\
    n\
    300g de carne seca \ ")
    st.image(image)
  elif testeteste == "Carne de Porco":
    image = Image.open("imagensnovo/carne de porco.jpg")
    st.write("Receitas com Carne de Porco \
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-carne-de-porco/)")
    st.image(image)
    
  
 
elif paginaselecionada == 'Peixes':
  st.title('Receitas com Peixe')
  st.write("aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
  Excepteur sint\
  [Leia mais](https://www.sabornamesa.com.br/receitas-de-peixes/file-de-peixe-simples-e-facil)")
  testeteste = st.selectbox("Tipos de Peixe", ("Salmao", "Atum", "Tilapia"))
    
                     
  if testeteste == "Salmao":
    image = Image.open("imagensnovo/salmao.jpg")
    st.write("Receitas com Salmao \
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-salmao/)")
    st.image(image)
  elif testeteste == "Atum":
    image = Image.open("imagensnovo/atum.jfif")
    st.write("Receitas com Atum \
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-atum-em-lata/)")
    st.image(image)
  elif testeteste == "Tilapia":
    image = Image.open("imagensnovo/tilapia.jpg")
    st.write("Receitas com Tilapia \
    [Mais Receitas](https://www.receiteria.com.br/receitas-com-tilapia/)")
    st.image(image)

elif paginaselecionada == 'Aves':                  
  st.title('Receitas com Aves')
  st.write("receitas com aves diferentes\
  [Leia mais](https://www.tudogostoso.com.br/categorias/1009-aves)")
  
  testeteste = st.selectbox("Tipos de Aves", ("Frango", "Pato", "Peru"))
  if testeteste == "Frango":
    image = Image.open("imagensnovo/frango.webp")
    st.write("Receitas com Frango \
    [Mais Receitas](https://www.sabornamesa.com.br/receita-de-carnes/peito-de-frango-simples-e-facil)")
    st.image(image)
  elif testeteste == "Pato":
    image = Image.open("imagensnovo/pato.webp")
    st.write("Receitas com Pato \
    [Mais Receitas](https://www.receiteria.com.br/receitas-de-pato/)")
    st.image(image)
  elif testeteste == "Peru":
    image = Image.open("imagensnovo/peru.jfif")
    st.write("Receitas com penguin \
    [Mais Receitas](https://www.tudoreceitas.com/receitas-de-peru-1101/)")
    st.image(image)
  
elif paginaselecionada == 'Vegetarianas':
  image = Image.open("imagensnovo/vegetariano.jpg")                 
  st.title('Receitas Vegetarianas')
  st.write("Receitas diversas vegetarianas \
  [Leia mais](https://www.receiteria.com.br/receitas-vegetarianas/)")
  st.image(image)
  
     
elif paginaselecionada == 'Veganas':
  image = Image.open("imagensnovo/vegano.webp")               
  st.title('Receitas Veganas')
  st.write("receitas diversas veganas\
  [Leia mais](https://www.receiteria.com.br/receitas-veganas/)")
  st.image(image)
  


