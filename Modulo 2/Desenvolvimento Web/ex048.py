import streamlit as st


num1 = st.text_input('Digite o primeiro número')
num2 = st.text_input('Digite o segundo número')

colunas = st.columns(4)


with colunas[0]:
    st.write('Adição')
    if st.button('Somar'):
        st.write(int(num1)+int(num2))


with colunas[1]:
    st.write('Subtração')
    if st.button('Subtrair'):
        st.write(int(num1)-int(num2))


with colunas[2]:
    st.write('Multiplicação')
    if st.button('Multiplicar'):
        st.write(int(num1)*int(num2))


with colunas[3]:
    st.write('Divisão')
    if st.button('Divisão'):
        st.write(int(num1)/int(num2))