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
