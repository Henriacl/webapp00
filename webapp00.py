import streamlit as st


conversao = st.selectbox("Qual unidade quer converter: ",["Inicio", "Gramas", "Xicaras"])
  
if(conversao == "Inicio"):
  st.header("Site de conversao de PrePear")
  
if(conversao == "Gramas"):
  gramas = 0
  gramas = st.number_input("Valor em Gramas")
  xicaras = int(gramas)/250
  st.text("O Valor em Gramas representa {}.".format(xicaras))
  
if(conversao == "Xicaras"):
  xicaras = 0 
  numerador = 0
  denominador = 1
  xicaras = st.number_input("quantidade de xicaras: ")
  xicaras = int(xicaras)*250
  numerador = st.number_input("parte de cima da fração se houver:")
  denominador = st.number_input("Parte de baixo da fração:")

  if int(denominador) > 0 :
    fracao = int(numerador)/int(denominador)
    valor = fracao*250
    valortotal = valor + xicaras 
    print("a qtd de xicaras representa", valortotal, "gramas")

  elif int(denominador) <= 0 :
    valor = int(xicaras)
    print("a qtd de xicaras representa", int(valor), "gramas")

