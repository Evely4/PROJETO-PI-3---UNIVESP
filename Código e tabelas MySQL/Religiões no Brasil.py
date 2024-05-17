#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

#Trecho do código para carregar uma tabela no formato html para converter em um Dataframe em Python 

fonte = 'C:/Users/fabio/Documents/UNIVESP/PI3 2024/CSV do MySQL/BDpi3_tab_religiao_br.html'

with open(fonte, 'r',  encoding='utf-8') as arquivo:
    html = arquivo.read()

soup = BeautifulSoup(html, 'html.parser')

tabela = soup.find('table')

dados = pd.read_html(str(tabela))


#Trecho do código para apagar a 1ª linha definida automaticamente como nome das colunas e substituí-la pela 2ª linha

dados_limpos = dados[0].rename(columns=dados[0].iloc[0]).drop(0)

# Trecho do código para renomear as colunas

dados_limpos.rename(columns={'religiao': 'Religião'}, inplace=True)
dados_limpos.rename(columns={'proporcao': 'Proporção'}, inplace=True)

#Trecho do código para converter dados da coluna em float(frações)
dados_limpos['Proporção'] = dados_limpos['Proporção'].astype(float)

print(dados_limpos)


# In[4]:


# Trecho do código para criar gráfico de pizza personalizado

fig, ax = plt.subplots(figsize=(8, 8))

# Gráfico de pizza
_, _, autotexts = ax.pie(dados_limpos['Proporção'], autopct='%1.1f%%', startangle=0)

# Adiciona um índice de cores ao lado direito do gráfico
ax.legend(loc='center left', labels=dados_limpos['Religião'], bbox_to_anchor=(1, 0.5))

# Personaliza os textos dentro das fatias
for autotext in autotexts:
    autotext.set_color('yellow')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Mostra o gráfico
plt.title('TAMANHO DAS RELIGIÕES NO BRASIL (Fonte: DataFolha-2020)')
plt.axis('equal')  # Faz com que o gráfico seja uma circunferência
plt.show()


# In[ ]:




