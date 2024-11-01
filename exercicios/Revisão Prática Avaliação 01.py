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
descobrir_par_impar= par_impar%2
if par_impar%2 == 0:
    print("Este numero é par!")
else: print("Este numero é impar!")

"""6. Crie um programa que peça a idade do usuário e exiba se ele é maior de idade ou
não."""
print("\nCódigo 6: Pede a idade do usuário e verifica se é maior de idade.")
idade_mais_18=int(input("Informe sua idade:\t"))
if idade_mais_18>=18:
    print("você é maior de idade")
else: print("Você é menor de idade")

"""7. Escreva um programa que calcule a média aritmética de três números fornecidos
pelo usuário."""
print("\nCódigo 7: Calcula a média aritmética de três números.")
numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))
media = (numero1 + numero2 + numero3) / 3
print(f"A média aritmética dos números é: {media}")

"""8. Faça um programa que leia um valor e informe se ele está entre 10 e 20."""
print("\nCódigo 8: Verifica se um valor está entre 10 e 20.")
valor8=int(input("Insira um valor aleatorio:\t"))
if valor8>=10 and valor8<=20:
    print("Este numero esta nos parametros entre 10 e 20")
else:    print("Este número não está entre 10 e 20.")

"""9. Escreva um programa que verifique se um ano é bissexto."""
print("\nCódigo 9: Verifica se um ano é bissexto.")
ano = int(input("Insira um ano: "))
# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

"""10. Crie um programa que leia um número e informe se ele é divisível por 3 ou por 5."""
print("\nCódigo 10: Verifica se um número é divisível por 3 ou 5.")
numero_div_3e5_ = int(input("Insira um número: "))
if numero_div_3e5_ %3 == 0:
    print(f"O número {numero_div_3e5_} é divisível por 3.")
elif numero_div_3e5_ %5 == 0:
    print(f"O número {numero_div_3e5_} é divisível por 5.")
else:
    print(f"O número {numero_div_3e5_} não é divisível nem por 3 nem por 5.")

"""11. Faça um programa que peça um número inteiro e exiba todos os números de 1 até o
número fornecido."""
print("\nCódigo 11: Exibe todos os números de 1 até um número fornecido.")
i=1
numero11=int(input("Insira um numero:\t"))
while i<=numero11:
    print (i)
    i+=1

"""12. Crie um programa que leia a temperatura em graus Celsius e converta para
Fahrenheit. Expressão de conversão: (celsius * 9/5) + 32."""
print("\nCódigo 12: Converte temperatura de Celsius para Fahrenheit.")
graus_celcius=float(input("Insira a temperatura em graus Celsius:\t"))
Fahrenheit=(graus_celcius* 9/5)+32
print(f"A temperatura em Fahrenheit é de {Fahrenheit}")

"""13. Escreva um programa que peça o nome e a idade de uma pessoa e exiba uma
mensagem de boas-vindas personalizada."""
print("\nCódigo 13: Exibe uma mensagem de boas-vindas personalizada.")
nome_do_usuario=input("Olá, qual seu nome?   ")
idade_do_usuario=int(input("Insira sua idade por gentileza"))
if idade_do_usuario < 0:
    print("Idade inválida! Por favor, insira uma idade positiva.")
elif idade_do_usuario <= 15:
    print(f"Olá {nome_do_usuario}, tudo bem? Seja bem-vindo à sua juventude!")
elif idade_do_usuario < 18:
    print(f"Olá {nome_do_usuario}, tudo certo? Você está quase lá, em breve maior de idade!")
elif idade_do_usuario < 60:
    print(f"Olá {nome_do_usuario}, tudo certo campeão(campeã)? Aproveite esta fase incrível da vida!")
else:
    print(f"Olá {nome_do_usuario}, que bom te ver! A maturidade traz sabedoria, não é mesmo? Seja muito bem-vindo!")   

"""14. Crie um programa que leia dois números e exiba o resultado da multiplicação entre
eles."""
print("\nCódigo 14: Multiplica dois números fornecidos pelo usuário.")
multipliacacao_numero1= int(input("Insira o primeiro numero para multiplicação:   "))
multiplicacao_numero2= int(input("Insira o segundo numero para multiplicação:   "))
multiplicacao=multipliacacao_numero1*multiplicacao_numero2
print (multiplicacao)

"""15. Faça um programa que leia três números e exiba o menor deles."""
print("\nCódigo 15: Exibe o menor de três números.")
numero15_num1= int(input("Insira o primeiro numero:\t"))
numero15_num2=int(input("Insira o segundo numero:\t"))
numero15_num3=int(input("Insira o terceiro numero:\t"))
if numero15_num1<numero15_num2 and numero15_num1<numero15_num3:
    print(f" numero {numero15_num1} é menor que {numero15_num2} e {numero15_num3}")
elif numero15_num2<numero15_num1 and numero15_num2<numero15_num3:
    print(f" numero {numero15_num2} é menor que {numero15_num1} e {numero15_num3}")
elif numero15_num3<numero15_num1 and numero15_num3<numero15_num2:
    print(f" numero {numero15_num3} é menor que {numero15_num1} e {numero15_num2}")
else: print("Todos os numeros são iguais")


"""16. Escreva um programa que leia a nota de um aluno e verifique se ele foi aprovado
(nota >= 6)."""
print("\nCódigo 16: Verifica se um aluno foi aprovado com nota >= 6.")
nota_aluno=float(input("Insira a nota de um aluno: "))
if nota_aluno>=0 and nota_aluno <= 6: 
    print("O aluno não passou! REPROVADO")
elif nota_aluno>=6 and nota_aluno<=10:
    print("O aluno  passou! AREPROVADO")
else: print("Informe um numero correto!")

"""17. Crie um programa que leia o peso e a altura de uma pessoa e calcule seu IMC."""
print("\nCódigo 17: Calcula o IMC com base no peso e altura fornecidos.")
peso = float(input("Informe seu peso (em Kg): "))
altura = float(input("Informe sua altura (em metros): "))
imc = peso / (altura * altura)
print(f"IMC: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está no peso normal.")
elif 25 <= imc < 30:
    print("Você está em sobrepeso.")
else:
    print("Obesidade, é importante consultar um profissional de saúde.")


"""18. Faça um programa que leia um número e exiba sua tabuada (de 1 a 10)."""
print("\nCódigo 18: Exibe a tabuada de um número fornecido.")
tabuada_laço=1
tabuada_num=int(input("Insira um numero para tabela: "))
while tabuada_laço<=10:
    tabuada= tabuada_num *tabuada_laço
    print (f"{tabuada_num}x{tabuada_laço}= {tabuada}")
    tabuada_laço+=1

"""19. Crie um programa que conte de 1 até 100 e exiba apenas os números pares."""
print("Código 19: Exibe apenas os números pares de 1 a 100.")
for numero_par_ate_100 in range(0,101,2):
    print(numero_par_ate_100)

"""20. Faça um programa que simule uma calculadora simples (soma, subtração,
multiplicação e divisão) com duas entradas do usuário."""
print("Código 20: Simula uma calculadora simples com duas entradas.")
numero_calculadora_1=float(input("insira um numero para a calculadora="))
numero_calculadora_2=float(input("insira um segundo numero para a calculadora="))
escolha_calculadora=int(input("Insira um numero de 1 a 4, sendo as opções\n1=Soma\n2=subtração\n3=multiplicação\n4=divisão\nEscolha="))
if escolha_calculadora== 1:
    soma_calculadora= numero_calculadora_1+numero_calculadora_2
    print(f"A soma de {numero_calculadora_1}+{numero_calculadora_2}={soma_calculadora}")
elif escolha_calculadora==2:
    subtracao_calculadora= numero_calculadora_1-numero_calculadora_2
    print(f"A subtração de {numero_calculadora_1}-{numero_calculadora_2}={subtracao_calculadora}")
elif escolha_calculadora== 3:
    soma_calculadora= numero_calculadora_1*numero_calculadora_2
    print(f"A multiplicação de {numero_calculadora_1}x{numero_calculadora_2}={soma_calculadora}")
elif escolha_calculadora==4:
    subtracao_calculadora= numero_calculadora_1/numero_calculadora_2
    print(f"A divisão de {numero_calculadora_1}/{numero_calculadora_2}={subtracao_calculadora}")
else: print("Nenhuma opção escolhida")

"""21. Crie um programa que peça um número ao usuário e imprima se ele é primo ou não."""
print("Código 21: Verifica se um número é primo.") #como se verifica se ele é primo ou não? 

"""22. Escreva um programa que some todos os números de 1 até 100."""
print("Código 22: Soma todos os números de 1 a 100.")
num_1_a_100_loop=1
soma_dos_numero_de_1_a_100=0
while num_1_a_100_loop <=100:
    soma_dos_numero_de_1_a_100+=num_1_a_100_loop
    num_1_a_100_loop+=1
print(f"A soma de todos os números de 1 a 100 é {soma_dos_numero_de_1_a_100}")

"""23. Crie um programa que peça um número e calcule seu fatorial."""
print("Código 23: Calcula o fatorial de um número fornecido.")
numero_fatorial = int(input("Insira um número: "))
if numero_fatorial < 0:
    print("Fatorial não definido para números negativos.")
else:
    fatorial = 1
    for i in range(1, numero_fatorial + 1):
        fatorial *= i
    print(f"O fatorial de {numero_fatorial} é {fatorial}.")
