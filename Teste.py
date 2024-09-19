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




import pandas as pd
import numpy as np
#gerando um dataframe aleatório
df = pd.DataFrame(
    np.random.randn(15,10),
    columns=('col_%d' % i for i in range(10))
 )
#tabelas interativas
st.dataframe(df)
#tabelas fixas
st.table(df)


#Botão
if st.button('Gerar número aleatório'):
   st.write(randint(0, 1000000))
else:
   st.write('Clique no botão acima')
#Radio
chute = st.radio(
    "por que essa função se chama radio?",
    ('Opção 1: porque o rádio é um osso muito bonito',
     'Opção 2: é uma homenagem à Marie Curie',
     'Opção 3: as opções lembram botões de rádio')
)
if chute == 'as opções lembram botões de rádio':
    st.write('Correto!')
else:
    st.write("Incorreto, tente novamente.")
