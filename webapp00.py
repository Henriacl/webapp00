import streamlit as st


conversao = st.selectbox("Qual unidade quer converter: ",["Inicio", "Gramas", "Xicaras"])
  
if(conversao == "Inicio"):
  st.header("Site de conversao de PrePear")
  
if(conversao == "Gramas"):
  gramas = 0
  gramas = st.number_input("Valor em Gramas")
  xicaras = int(gramas)/250
  st.text("O Valor em Gramas representa {} xicaras".format(xicaras))
  
if(conversao == "Xicaras"):
  xicaras = 0 
  xicaras = st.number_input("quantidade de xicaras: ")
  valor = int(xicaras)*250
  st.text("A qtd de xicaras representa {} Gramas".format(valor))
