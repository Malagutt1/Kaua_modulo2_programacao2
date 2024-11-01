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
"""import time
for cont_regressiva in range(20,0,-1):
    print("Contagem regressiva:")
    print(cont_regressiva)
    time.sleep(1) 
print("Seu tempo acabou!") """   #tirar aspas pois estava com o contador de 20 segundos

"""5) Crie um programa que realiza a contagem de 1 até 100, considerando
apenas os números ímpares. Exiba na tela quantos números ímpares
foram encontrados nesse intervalo e qual a soma desses números
ímpares."""
print("exercicio 5")
num_impar=0
soma=0
for num in range(1,101):
    
    soma+=num
    num_impar+=1
print(num_impar)
print(num)
"""6) Crie um programa que pede ao usuário que digite um número qualquer,
em seguida retorne se esse número é primo ou não, caso não, retorne
também quantas vezes esse número é divisível."""
print("exercicio 6")

"""7) Crie um programa que pede que o usuário digite um nome ou uma frase,
verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em
tela esse resultado."""
print("exercicio 7")

"""8) Crie uma função de número de parâmetros indefinido, que realize a soma
dos números passados como parâmetro, independentemente da
quantidade de parâmetros."""
print("exercicio 8")

"""9) Escreva um programa que lê uma palavra ou frase digitada pelo usuário,
retornando o número de letras maiúsculas e minúsculas da mesma. Usar
apenas de logica e de funções embutidas ao sistema."""
print("exercicio 9")