# Instalando o Pandas
Para instalar a biblioteca Pandas, utilize o seguinte comando:
```ipynb
!pip install pandas
```

# Criando um Arquivo `teste.ipynb`
Dentro do arquivo `teste.ipynb`, podemos importar a biblioteca Pandas da seguinte forma:
```ipynb
import pandas as pd
```

## O que é o Pandas?
* `pandas` é uma biblioteca do Python utilizada para trabalhar com conjuntos de dados.
* Possui funções para analisar, limpar, explorar e manipular dados.
* O nome "pandas" é uma referência a "Painel de Dados" (Panel Data) e "Python Data Analysis".
* Criado por Wes McKinney em 2008.
* Permite analisar grandes volumes de dados (`Big Data`) e obter insights baseados em estatísticas.
* Facilita a limpeza de dados desorganizados, tornando-os mais legíveis e relevantes.

## O que o Pandas pode fazer?
O Pandas permite:
* Carregar e visualizar dados de diversas fontes (CSV, Excel, SQL, JSON, etc.).
* Manipular e transformar dados de forma eficiente.
* Lidar com dados ausentes.
* Filtrar, agrupar e agregar dados.
* Gerar estatísticas descritivas sobre os dados.
* Criar gráficos e visualizações integradas com bibliotecas como Matplotlib e Seaborn.

# Principais Estruturas de Dados

## Series
Uma `Series` é um array unidimensional que pode conter qualquer tipo de dado (inteiros, strings, floats, etc.) e possui um índice associado.

### Criando uma `Series`
```ipynb
import pandas as pd

dados = [10, 20, 30, 40, 50]
series = pd.Series(dados)
series
```

Cada valor possui um índice (por padrão, numérico e sequencial). Também podemos definir um índice personalizado:
```ipynb
dados = [10, 20, 30, 40, 50]
indices = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(dados, index=indices)
series
```

## DataFrame
O `DataFrame` é uma estrutura de dados bidimensional (tabela) que consiste em linhas e colunas, semelhante a uma planilha do Excel.

### Criando um `DataFrame`
Podemos criar um `DataFrame` a partir de um dicionário:
```ipynb
dados = {
    'Nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(dados)
df
```

### Acessando Colunas
Para acessar uma coluna específica:
```ipynb
df['Nome']
```

### Acessando Linhas
Para acessar uma linha pelo índice:
```ipynb
df.loc[1]
```

Podemos acessar várias linhas ao mesmo tempo:
```ipynb
df.loc[0:1]
```

### Filtrando Dados
Podemos filtrar os dados baseando-se em uma condição:
```ipynb
df[df['Idade'] > 25]
```

### Adicionando uma Nova Coluna
Podemos adicionar uma nova coluna ao `DataFrame`:
```ipynb
df['Profissão'] = ['Engenheira', 'Médico', 'Advogado']
df
```

### Removendo uma Coluna
Para remover uma coluna:
```ipynb
df.drop(columns=['Profissão'], inplace=True)
df
```

### Estatísticas Básicas
Podemos obter estatísticas descritivas dos dados:
```ipynb
df.describe()
```
Isso exibe estatísticas como média, desvio padrão, valores mínimos e máximos das colunas numéricas.

# Conclusão
O `pandas` é uma biblioteca essencial para análise de dados, permitindo manipular e explorar conjuntos de dados de forma eficiente. Ele facilita tarefas como limpeza de dados, análise estatística e visualização, tornando-se uma ferramenta poderosa para cientistas de dados e analistas.

