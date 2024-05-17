#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


#Trecho do código para carregar uma tabela no formato html para converter em um Dataframe em Python 

with open('C:/Users/fabio/Documents/UNIVESP/PI3 2024/CSV do MySQL/BDpi3_tab_cresc_popul.html', 'r',  encoding='utf-8') as arquivo:
    html = arquivo.read()

soup = BeautifulSoup(html, 'html.parser')

tabela = soup.find('table')

dados = pd.read_html(str(tabela))


print(dados[0])

#Trecho do código para apagar a 1ª linha definida automaticamente como nome das colunas e substituí-la pela 2ª linha

dados_limpos = dados[0].rename(columns=dados[0].iloc[0]).drop(0)

#Trecho do código para apagar uma coluna

dados_limpos = dados_limpos.drop(columns=['Recorte Geográfico'])

# Trecho do código para renomear as colunas

dados_limpos.rename(columns={'Ano da pesquisa': 'Ano'}, inplace=True)
dados_limpos.rename(columns={'População(pessoas)': 'População'}, inplace=True)


# In[22]:


print(dados_limpos)


# In[23]:


#Trecho do código para transformar dado de uma coluna em inteiros
dados_limpos['População'] = dados_limpos['População'].astype(int)


# In[24]:


#Trecho do código para mudar a escala dos dados para milhões
dados_limpos['População'] = dados_limpos['População']/1000000
dados_limpos['População'] = dados_limpos['População'].round(1)

print(dados_limpos)


# In[26]:


#Trecho do código para gerar o gráfico de barras

# Configura o tamanho da figura e a fonte
plt.figure(figsize=(10, 6))
sns.set(font_scale=1.5)

# Cria o gráfico de barras
sns.barplot(x=dados_limpos['Ano'], y=dados_limpos['População'], data=dados_limpos)

# Personaliza o gráfico
plt.title('Crescimento da população brasileira (Fonte: IBGE)', fontsize=25)
plt.xlabel('Ano do Censo', fontsize=20)
plt.ylabel('População (milhões)', fontsize=20)

# Ajusta o tamanho da fonte dos dados nos eixos
plt.tick_params(axis='both', which='major', labelsize=10)

# Ajusta a largura das colunas
plt.bar(dados_limpos['Ano'], dados_limpos['População'], width=0.5)

# Mostra o gráfico
plt.show()


# In[ ]:




