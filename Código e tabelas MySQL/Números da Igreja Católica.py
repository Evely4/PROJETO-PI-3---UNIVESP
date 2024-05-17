#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

#Trecho do código para carregar uma tabela no formato html para converter em um Dataframe em Python 
fonte = 'C:/Users/fabio/Documents/UNIVESP/PI3 2024/CSV do MySQL/BDpi3_tab_num_catolicos.html'

with open(fonte, 'r',  encoding='utf-8') as arquivo:
    html = arquivo.read()

soup = BeautifulSoup(html, 'html.parser')

tabela = soup.find('table')

dados = pd.read_html(str(tabela))

#Trecho do código para apagar a 1ª linha definida automaticamente como nome das colunas e substituí-la pela 2ª linha

dados_limpos = dados[0].rename(columns=dados[0].iloc[0]).drop(0)

# Trecho do código para renomear as colunas

dados_limpos.rename(columns={'campo': 'Dados da Igreja(Fonte: CNBB)'}, inplace=True)
dados_limpos.rename(columns={'dados': 'Resultado'}, inplace=True)
dados_limpos.rename(columns={'data_pesq': 'Ano da Pesquisa'}, inplace=True)


print(dados_limpos)


# In[2]:


#Trecho do código para transformar a tabela em um formato visualmente mais agradável

df = pd.DataFrame(dados_limpos)

# Estilizar a tabela usando o Styler do pandas
estilizado = df.style\
    .set_properties(**{'background-color': 'darkgreen', 'color': 'blue', 'border-color': 'white', 'text-align': 'left', 'font-family': 'Times New Roman', 'color': 'white'})\
    .set_table_styles([{
        'selector': 'th',
        'props': [('background-color', 'blue'), ('color', 'yellow'), ('text-align', 'left'), ('Font-Weight', 'bold')]
    }])

# Exibir a tabela estilizada
estilizado


# In[ ]:




