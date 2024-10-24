"""Revisão Prática Avaliação 01 - 23/10/24 Python
1. Crie um programa que leia dois números inteiros do usuário e exiba a soma entre
eles."""
print("Código 1: Lê dois números inteiros e exibe a soma.")
num1=int(input("Insira um numero"))
num2=int(input("Insira um numero"))
soma1=num1+num2
print(soma1)
"""2. Faça um programa que leia um número e informe se ele é positivo, negativo ou zero."""
print("\nCódigo 2: Lê um número e informa se é positivo, negativo ou zero.")
numero3=int(input("Insira um numero"))
if numero3==0:
    print("Este numero é 0")
elif numero3<0:
    print("Este numero é negativo")
elif numero3>0:
    print("Este numero é positivo")

"""3. Escreva um programa que leia dois números e exiba o maior deles."""
print("\nCódigo 3: Lê dois números e exibe o maior deles.")
num_maior1=int(input("Insira o primeiro numero para verificar qual é o meior:  "))
num_maior2=int(input("Insira o segundo numero para verificar qual é o meior:  "))
if num_maior1>num_maior2:
    print(f"{num_maior1} é maior que {num_maior2}")
elif num_maior2>num_maior1:
    print(f"{num_maior2} é maior que {num_maior1}")
elif num_maior1==num_maior2:
    print(f"{num_maior2} são iguais {num_maior1}")

"""4. Crie um programa que calcule o quadrado de um número fornecido pelo usuário.."""
print("\nCódigo 4: Calcula o quadrado de um número fornecido pelo usuário.")
numero_quadrado=int(input("Insira um numero:  "))
quadrado=numero_quadrado ** 2
print(quadrado)

"""5. Escreva um programa que verifique se um número é par ou ímpar."""
print("\nCódigo 5: Verifica se um número é par ou ímpar.")
par_impar=int(input("Insira um numero par ou impar: "))
if par_impar!= 0:
    print("Este numero é impar!")
else: print("Este numero é par")

"""6. Crie um programa que peça a idade do usuário e exiba se ele é maior de idade ou
não."""
print("Código 6: Pede a idade do usuário e verifica se é maior de idade.")
idade_mais_18=int(input("Informe sua idade:\t"))
if idade_mais_18>=18:
    print("você é maior de idade")
else: print("Você é menor de idade")

"""7. Escreva um programa que calcule a média aritmética de três números fornecidos
pelo usuário."""
print("Código 7: Calcula a média aritmética de três números.")

"""8. Faça um programa que leia um valor e informe se ele está entre 10 e 20."""
print("Código 8: Verifica se um valor está entre 10 e 20.")
valor8=int(input("Insira um valor aleatorio:\t"))
if valor8>=10 and valor8<=20:
    print("Este numero esta nos parametros entre 10 e 20")
else:    print("Este número não está entre 10 e 20.")

"""9. Escreva um programa que verifique se um ano é bissexto."""
print("Código 9: Verifica se um ano é bissexto.")

"""10. Crie um programa que leia um número e informe se ele é divisível por 3 ou por 5."""
print("Código 10: Verifica se um número é divisível por 3 ou 5.")

"""11. Faça um programa que peça um número inteiro e exiba todos os números de 1 até o
número fornecido."""
print("Código 11: Exibe todos os números de 1 até um número fornecido.")
i=1
numero11=int(input("Insira um numero:\t"))
while i<=numero11:
    print (i)
    i+=1

"""12. Crie um programa que leia a temperatura em graus Celsius e converta para
Fahrenheit. Expressão de conversão: (celsius * 9/5) + 32."""
print("Código 12: Converte temperatura de Celsius para Fahrenheit.")

"""13. Escreva um programa que peça o nome e a idade de uma pessoa e exiba uma
mensagem de boas-vindas personalizada."""
print("Código 13: Exibe uma mensagem de boas-vindas personalizada.")

"""14. Crie um programa que leia dois números e exiba o resultado da multiplicação entre
eles."""
print("Código 14: Multiplica dois números fornecidos pelo usuário.")

"""15. Faça um programa que leia três números e exiba o menor deles."""
print("Código 15: Exibe o menor de três números.")

"""16. Escreva um programa que leia a nota de um aluno e verifique se ele foi aprovado
(nota >= 6)."""
print("Código 16: Verifica se um aluno foi aprovado com nota >= 6.")

"""17. Crie um programa que leia o peso e a altura de uma pessoa e calcule seu IMC."""
print("Código 17: Calcula o IMC com base no peso e altura fornecidos.")

"""18. Faça um programa que leia um número e exiba sua tabuada (de 1 a 10)."""
print("Código 18: Exibe a tabuada de um número fornecido.")

"""19. Crie um programa que conte de 1 até 100 e exiba apenas os números pares."""
print("Código 19: Exibe apenas os números pares de 1 a 100.")

"""20. Faça um programa que simule uma calculadora simples (soma, subtração,
multiplicação e divisão) com duas entradas do usuário."""
print("Código 20: Simula uma calculadora simples com duas entradas.")

"""21. Crie um programa que peça um número ao usuário e imprima se ele é primo ou não."""
print("Código 21: Verifica se um número é primo.")

"""22. Escreva um programa que some todos os números de 1 até 100."""
print("Código 22: Soma todos os números de 1 a 100.")

"""23. Crie um programa que peça um número e calcule seu fatorial."""
print("Código 23: Calcula o fatorial de um número fornecido.")
