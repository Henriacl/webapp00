import streamlit as st


conversao = st.selectbox("Qual unidade quer converter: ",["Inicio", "Gramas", "Xicaras", "Colheres de Sopa"])
  
if(conversao == "Inicio"):
  st.header("Site de conversao de PrePear")
  
if(conversao == "Gramas"):
  gramas = 0 
  Colheres de Sopa = 0
  gramas = st.number_input("Valor em Gramas")
  xicaras = int(gramas)/250
  Colheres de Sopa = int(gramas)/20
  st.text("O Valor em Gramas representa {} xicaras".format(xicaras))
  st.text("Ou")
  st.text("Representa {} Colheres de Sopa".format(Colheres de Sopa))
  
if(conversao == "Xicaras"):
  xicaras = 0 
  xicaras = st.number_input("Quantidade de xicaras: ")
  valor = xicaras*250
  st.text("A qtd de xicaras representa {} Gramas".format(valor))
  
  
if(conversao == "Colheres de Sopa"):
  Colheres de Sopa = 0 
  xicaras = st.number_input("Qantidade de Colheres: ")
  valor = Colheres de Sopa*20
  st.text("A qtd de Colheres de Sopa representa {} Gramas".format(valor))
