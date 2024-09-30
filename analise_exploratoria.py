#Usamos o Google Collab para realizar a Análise Explorátoria dos Dados 
rom google.colab import files
uploaded = files.upload()  


import pandas as pd
df = pd.read_csv('world_population_data.csv')

# Exibindo as primeiras linhas do dataset
print(df.head())

# Importando as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração para exibir gráficos 
%matplotlib inline

# Verificar o número de linhas e colunas
print(f"O dataset contém {df.shape[0]} linhas e {df.shape[1]} colunas")

# Exibir a estrutura dos dados
df.info()

# Resumo estatístico das variáveis numéricas
df.describe()

# Verificar valores ausentes
df.isnull().sum()

# Caso precise vizualizar as colunas da Tabela
print(df.columns)

# Histograma da Taxa de Crescimento Populacional
sns.histplot(df['growth rate'], bins=20, kde=True)
plt.title('Distribuição da Taxa de Crescimento Populacional')
plt.xlabel('Taxa de Crescimento')
plt.ylabel('Frequência')
plt.show()
# Histograma da Densidade Populacional
sns.histplot(df['density (km²)'], bins=20, kde=True)
plt.title('Distribuição da Densidade Populacional')
plt.xlabel('Densidade Populacional (por km²)')
plt.ylabel('Frequência')
plt.show()
# Selecionar algumas colunas para comparar as populações de diferentes anos
df[['country', '2023 population', '2022 population', '2020 population', '2015 population']].head()
# Criar uma nova coluna para o crescimento populacional de 2020 a 2023
df['growth 2020-2023'] = ((df['2023 population'] - df['2020 population']) / df['2020 population']) * 100

# Visualizar o crescimento populacional de 2020 a 2023
sns.histplot(df['growth 2020-2023'], bins=20, kde=True)
plt.title('Crescimento Populacional de 2020 a 2023 (%)')
plt.xlabel('Crescimento (%)')
plt.ylabel('Frequência')
plt.show()
# Remover o símbolo de porcentagem e converter para float
df['growth rate'] = df['growth rate'].str.replace('%', '').astype(float)

# Verifique as outras colunas também se forem strings que precisam ser convertidas
df['density (km²)'] = pd.to_numeric(df['density (km²)'], errors='coerce')
df['2023 population'] = pd.to_numeric(df['2023 population'], errors='coerce')
df['2020 population'] = pd.to_numeric(df['2020 population'], errors='coerce')

# Agora calcular a matriz de correlação
correlacao = df[['growth rate', 'density (km²)', '2023 population', '2020 population']].corr()

# Visualizar a matriz de correlação
plt.figure(figsize=(8,6))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação entre Variáveis Populacionais')
plt.show()
