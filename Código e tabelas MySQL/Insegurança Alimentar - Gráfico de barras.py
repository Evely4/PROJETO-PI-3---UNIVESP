#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

#Trecho do código para carregar uma tabela no formato html para converter em um Dataframe em Python 

fonte = 'C:/Users/fabio/Documents/UNIVESP/PI3 2024/CSV do MySQL/BDpi3_tab_inseg_alimentar.html'

with open(fonte, 'r',  encoding='utf-8') as arquivo:
    html = arquivo.read()

soup = BeautifulSoup(html, 'html.parser')

tabela = soup.find('table')

dados = pd.read_html(str(tabela))

#Trecho do código para apagar a 1ª linha definida automaticamente como nome das colunas e substituí-la pela 2ª linha

dados_limpos = dados[0].rename(columns=dados[0].iloc[0]).drop(0)

#Trecho do código para converter dados em inteiros, depois mudar a escala dos dados para milhões com até 1 casa decimal 

dados_limpos['Números'] = dados_limpos['Números'].astype(int)

dados_limpos['Números'] = (dados_limpos['Números']/1000000).round(1)

#Trecho do código para renomear coluna

dados_limpos.rename(columns={'Números': 'Números(Milhões)'}, inplace=True)
                     
print(dados_limpos)


# In[102]:


# Trecho do código para gerar um gráfico de barras horizontais

# Criando uma lista de cores para cada barra
cores = ['green' if barra == 'População (BR)' or barra == 'Total de domicílios (BR)' or barra == 'Insegurança alimentar (BR)' or barra == 'Domicílios com insegurança alimentar (BR)' else 'red' for barra in dados_limpos['Comparativo']]

# Criando uma legenda personalizada com índice de dois campos
legenda_personalizada = [
    ('Brasil', 'green'),
    ('São Paulo', 'red')
]

#Cria o gráfico de barras
ax = dados_limpos.plot(kind='barh', x='Comparativo', y='Números(Milhões)', color=cores)
plt.xlabel('Números (em Milhões)', fontsize=15, fontweight='bold')
plt.ylabel('Comparativo', fontsize=15, fontweight='bold')
plt.title('Insegurança Alimentar - Brasil x São Paulo (Fonte: IBGE-2023)', color='brown', fontweight='bold')

# Adiciona anotações aos valores das barras
for i, v in enumerate(dados_limpos['Números(Milhões)']):
    ax.text(v, i, str(v), ha='left', va='center')
    
# Cria uma legenda para a legenda personalizada
patches = [plt.Rectangle((0,0),1,1, color=color) for _, color in legenda_personalizada]
plt.legend(patches, [name for name, _ in legenda_personalizada])

# Exibindo o gráfico
plt.show()



# In[ ]:




