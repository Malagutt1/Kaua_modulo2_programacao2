"""1) Crie uma estrutura de repetição que percorra a String “Instituto Federal
de Santa Catarina” exibindo na tela letra por letra dessa String, tanto na
orientação horizontal quanto na vertical."""
print("exercicio 1")
for item_da_lista in "Instituto Federal de Santa Catarina":
    print(item_da_lista)
    mostrar_na_horizontal= ""
for item_da_lista in "Instituto Federal de Santa Catarina":
    mostrar_na_horizontal=mostrar_na_horizontal + item_da_lista
print(mostrar_na_horizontal)

"""2) Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os
números pares."""
print("exercicio 2")
for par in range(0,21,2): 
    print(par)

"""3) Crie um programa que exiba na tela a tabuada de um determinado número
fornecido pelo usuário."""
print("exercicio 3")
tabuada_do_usuario=int(input("Insira um numero para fazer a tabuada:\t"))
for i in range(1,11):
    tabuada= tabuada_do_usuario*i
    print(f"Tabuada= {tabuada_do_usuario}x{i}={tabuada} ")

"""4) Crie um programa que realiza a contagem regressiva de 20 segundos."""
print("exercicio 4") 
import time
for cont_regressiva in range(20,0,-1):
    print("Contagem regressiva:")
    print(cont_regressiva)
    time.sleep(1)  #tirar aspas pois estava com o contador de 20 segundos
print("Seu tempo acabou!")   

"""5) Crie um programa que realiza a contagem de 1 até 100, considerando
apenas os números ímpares. Exiba na tela quantos números ímpares
foram encontrados nesse intervalo e qual a soma desses números
ímpares."""
print("exercicio 5")
num_impar  =0
soma       =0
for num in range(1,101):
    if num % 2 != 0:
        num_impar+=1
        soma+=num
print(num_impar)
print(soma)
"""6) Crie um programa que pede ao usuário que digite um número qualquer,
em seguida retorne se esse número é primo ou não, caso não, retorne
também quantas vezes esse número é divisível."""
print("exercicio 6")
quantidadeDeDivisores = 0
numeroDoUsuario = int(input("Digite um número: "))
for i in range(1, numeroDoUsuario+1):
    if numeroDoUsuario%i==0:
        quantidadeDeDivisores += 1
if quantidadeDeDivisores > 2:
    print(f"O número escolhido não é primo e possui {quantidadeDeDivisores} divisores")
else:
    print(f"O número escolhido é primo, possuindo {quantidadeDeDivisores} divisores")

"""7) Crie um programa que pede que o usuário digite um nome ou uma frase,
verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em
tela esse resultado."""
print("exercicio 7")

palavraDigitadaPeloUsuario = str(input("Digite uma palavra: "))
palavraAoContrario = palavraDigitadaPeloUsuario[::-1]

if palavraAoContrario.strip() == palavraDigitadaPeloUsuario.strip():
    print(f"A palavra/frase '{palavraDigitadaPeloUsuario}' é um palíndromo. ({palavraAoContrario})")
else:
    print(f"A palavra/frase '{palavraDigitadaPeloUsuario}' não é um palíndromo. ({palavraAoContrario})")
    
"""8) Crie uma função de número de parâmetros indefinido, que realize a soma
dos números passados como parâmetro, independentemente da
quantidade de parâmetros."""
print("exercicio 8")
numeros = input("Digite os números separados por espaço: ").split()
soma = 0
for numero in numeros:
    soma += int(numero)
print(f"A soma dos números é: {soma}")

"""9) Escreva um programa que lê uma palavra ou frase digitada pelo usuário,
retornando o número de letras maiúsculas e minúsculas da mesma. Usar
apenas de logica e de funções embutidas ao sistema."""
print("exercicio 9")
texto = input("Digite uma palavra ou frase: ")
maiusculas = 0
minusculas = 0

for caractere in texto:
    if caractere.isupper():
        maiusculas += 1
    elif caractere.islower():
        minusculas += 1

print(f"Maiúsculas: {maiusculas}, Minúsculas: {minusculas}")



