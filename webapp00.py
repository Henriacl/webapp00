

import streamlit as st
from PIL import Image
from fractions import Fraction


conversao = st.selectbox("Qual unidade quer converter: ",
                        ["Inicio", "Gramas", "Xicaras"])

  
if(conversao == "Inicio"):
    st.header("Site de conversao de PrePear")

elif(conversao == "Gramas"):
  gramas = 0
  gramas = st.number_input("Valor em Gramas")
  xicaras = int(gramas)/250
  resto = int(gramas) % 250
  fracao = Fraction(resto , 250)
  st.text("O Valor em Gramas representa {}.".format(xicaras))
  st.text("Xicaras e {}.".format(fracao.limit_denominator(5))
          elif(conversao == "Xicaras"):
  st.text("aohdoahdoah")
