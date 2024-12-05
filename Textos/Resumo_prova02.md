<h2 align="center"> Resumo prova Modulo 2 

#### `* Data da prova: 05/12/2024*`

<h2 align="center"> Função (Def): <h2>

```python
def nome_da_funcao():
    soma=5+5
    return soma
resultado_da_funcao = nome_da_funcao()
print(resultado_da_funcao)
```
<h2 align="center"> Lista de exercício estruturas condicionais ou de decisão:<h2>

```python
medicos= ana (numero 1), marcos(numero 2), joão(numero 3)
escolha_medico= input("Escolha um medico: ")
if escolha_medico==1:
    print("seu medico escolhido é Ana")
else if escolha_medico==2:
    print("seu medico escolhido é Marcos")
else if escolha_medico==3:
    print("seu medico escolhido é João")
else:
    print("não foi possivel escolher um medico!") 
```
<h2 align= "center"> importação de bibliotecas:<h2>

```python
import time
from datetime import datetime 
```
<h2 align= "center"> Estrutura de repetição While:<h2>

```python
while True: #laço infinito até um break ou error
    print("Hello world!")
    break

i=0
while i <= 10: #laço de 1 até 10
    print(i)
    i+=1
```
<h2 align= "center"> Validação STDIN "input() "  :<h2>

```python
verificar_numero=input("Informe um número:  ")
if not verificar_numero.isnumeric():
    print("Informe um numero")
else:
    verificar_numero=int(verificar_numero)
```
<h2 align= "center"> Manipulação de Strings em Python"  :<h2>

```python
frase_para_se_tornar_minuscula = "HELLO WORLD! MODULO 2 TDS"
print(frase_para_se_tornar_minuscula.lower())
```
<h2 align= "center"> Laços For :<h2>

```python
for i in range (1,51): #ele não conta ultimo numero e vai de 1 em 1
    print(i)

for i in range (0,11,2): # 0= começo  || 11= final  || 2= vai de 2 em 2 numeros  
    print(i) #pode ser contornado com "print(i+2)"
```
