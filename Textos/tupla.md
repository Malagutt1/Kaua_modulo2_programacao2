# Tupla e lista
### Uma tupla é imutável e é separada por vírgulas (,)
#### exemplos
```Python
tupla=("a", "b",) # Exemplo 1: Tupla com dois elementos
tupla="a", "b",  # Exemplo 2: Tupla criada sem parênteses (usa apenas vírgula)
tupla=("a",) # Exemplo 3: Tupla com apenas um elemento (necessário incluir a vírgula)
tupla = ("a") # Exemplo 4: Isso é uma string, não uma tupla
tupla_vazia=()

variavel_do_tipo_tupla = ("a", "b","c", "d", "e", "f",) 
variavel_do_tipo_tupla[0]= "a"  # resultara error
```

# Lista:
### Uma lista é mutável, feita com colchetes ([ ]) e separada por vírgulas (,)
### Pode conter diferentes tipos de dados, ser aninhada e permite alterações nos elementos
```Python
# Exemplo 1: Lista simples
lista01 = ["ifsc", "Hello_World"]
print(lista01)  # Saída: ['ifsc', 'Hello_World']

# Exemplo 2: Lista com diferentes tipos de dados
lista02 = ["sapam", 2.0, 5, [10, 50]]
print(lista02)  # Saída: ['sapam', 2.0, 5, [10, 50]]

# Exemplo 3: Alterando elementos de uma lista
lista01[0] = "programação"  # Alterando o primeiro elemento da lista
print(lista01)  # Saída: ['programação', 'Hello_World']

# Exemplo 4: funciona com "IN":
if "ifsc" in "lista01":
    print("esse item esta dentro da lista") # procurar dentro da lista

for i in range(len(lista01)):
    lista01[i]= lista01[i]*2  # ordenar por indice


```


