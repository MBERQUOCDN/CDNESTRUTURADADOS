import streamlit as st

#Diferentes tamanhos de texto
st.title('Isso é um título')
st.header('Isso é um cabeçalho')
st.subheader('Isso é um subcabeçalho')
st.text('Isso é um texto normal')
#formatação
st.markdown('Texto em **negrito** ou _itálico_')
#Utilização para guardar html
st.markdown('[Isso é um texto com html](https://docs.streamlit.io/en/stable/api.html#display-text)',False)
