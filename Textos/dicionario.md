# DICIONARIO EM PYTHON

Os dicionários em Python são estruturas de dados que armazenam pares de chave e valor. Eles são muito versáteis e permitem combinações poderosas, como armazenar listas e outros dicionários dentro deles.

---

### **1. Criando um Dicionário**  
Você pode criar dicionários vazios ou inicializá-los com valores.  

```python
# Dicionário vazio
meu_dicionario = {}

# Dicionário com valores
dicionario = {
    "nome": "Kauã",
    "Idade": 16,
    <chave>: <Valor>  # Não aceita chave duplicada
}
```  

---

### **2. Adicionar Elementos**  
Adicione novos elementos usando a atribuição direta ou o método `update()`.  

```python
# Adicionando uma nova chave e valor
meu_dicionario["cidade"] = "Chapecó"

# Adicionando múltiplos elementos com update()
meu_dicionario.update({"pais": "Brasil", "lingua": "Português"})
```

---

### **3. Atualizar Valores**  
Atualize valores existentes diretamente ou usando o método `update()`.  

```python
# Atualizar o valor de uma chave existente
meu_dicionario["idade"] = 26

# Atualizar múltiplos valores
meu_dicionario.update({"profissao": "Gerente", "cidade": "Coronel Freitas"})
```

---

### **4. Remover Elementos**  
Remova elementos com `pop()`, `popitem()`, ou `del`. Para apagar todos os itens, use `clear()`.  

```python
# Remover um item específico com pop()
profissao = meu_dicionario.pop("profissao")

# Remover o último item inserido (Python 3.7+)
ultimo_item = meu_dicionario.popitem()

# Remover usando del
del meu_dicionario["idade"]

# Limpar todo o dicionário
meu_dicionario.clear()
```

---

### **5. Acessar Elementos**  
Acesse valores usando as chaves diretamente ou o método `get()`.  

```python
# Acessar o valor de uma chave
nome = meu_dicionario["nome"]

# Usar get() para evitar erros se a chave não existir
idade = meu_dicionario.get("idade", "Chave não encontrada")
```

---

### **6. Iterar pelo Dicionário**  
É possível iterar pelas chaves, valores ou ambos.  

```python
# Iterar pelas chaves
for chave in meu_dicionario:
    print(chave)

# Iterar pelos valores
for valor in meu_dicionario.values():
    print(valor)

# Iterar pelas chaves e valores
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
```

---

### **7. Outras Operações Úteis**  
Dicionários possuem métodos úteis para diversas operações.  

```python
# Verificar se uma chave existe
if "nome" in meu_dicionario:
    print("A chave 'nome' está presente.")

# Tamanho do dicionário
tamanho = len(meu_dicionario)

# Copiar um dicionário
novo_dicionario = meu_dicionario.copy()

# Mesclar dicionários (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = d1 | d2  # {'a': 1, 'b': 3, 'c': 4}
```

---

### **8. Dicionários Aninhados**  
Dicionários podem conter outros dicionários como valores.  

```python
# Exemplo de dicionário aninhado
empresa = {
    "departamento1": {
        "nome": "Financeiro",
        "funcionarios": 10
    },
    "departamento2": {
        "nome": "TI",
        "funcionarios": 25
    }
}

# Acessando elementos
print(empresa["departamento1"]["nome"])  # Saída: Financeiro
print(empresa["departamento2"]["funcionarios"])  # Saída: 25
```

---

### **9. Lista Dentro de um Dicionário**  
Listas podem ser armazenadas como valores em dicionários.  

```python
# Exemplo de lista dentro de um dicionário
estudante = {
    "nome": "João",
    "notas": [8.5, 9.0, 7.5],
    "disciplinas": ["Matemática", "Física", "Química"]
}

# Acessando elementos
print(estudante["notas"])  # Saída: [8.5, 9.0, 7.5]
print(estudante["disciplinas"][0])  # Saída: Matemática   ( [0] = posição 1)
```

---

### **10. Lista com Dicionários Dentro**  
Listas podem conter dicionários como elementos.  

```python
# Exemplo de lista com dicionários
turma = [
    {"nome": "Eduardo ", "idade": 20},
    {"nome": "Emily", "idade": 22},
    {"nome": "Raissa", "idade": 19}
]

# Acessando elementos
print(turma[0]["nome"])  # Saída: Ana
print(turma[1]["idade"])  # Saída: 22
```

---

### **11. Estrutura Mista: Dicionários e Listas**  
É possível criar estruturas ainda mais complexas misturando dicionários e listas.  

```python
# Exemplo misto
empresa = {
    "departamentos": [
        {"nome": "Financeiro", "funcionarios": ["Alice", "Bob"]},
        {"nome": "TI", "funcionarios": ["Carlos", "Diana", "Eduardo"]}
    ],
    "localizacao": "São Paulo"
}

# Acessando elementos
print(empresa["departamentos"][0]["nome"])  # Saída: Financeiro
print(empresa["departamentos"][1]["funcionarios"][2])  # Saída: Eduardo
```

---
