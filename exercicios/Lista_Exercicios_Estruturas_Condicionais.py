"""Obs: Toda entrada de dados via Stdin, deverá ser validada. Caso
não seja uma entrada válida, uma mensagem informativa deverá
ser exibida na tela e o programa finalizado.


1) Crie 2 variáveis com dois valores numéricos inteiros informados pelo
usuário, caso o valor do primeiro número for maior do que o segundo,
exiba em tela uma mensagem de acordo, caso contrário, exiba em tela
uma mensagem dizendo que o primeiro valor digitado é menor que o
segundo. Os números informados pelo usuário devem aparecer em
ambas as mensagens."""
print("1º exercicio (maior-menor)")
while True:
    valor1=input("Informe o primeiro número:\t")
    try:
        valor1=int(valor1)
        break
    except ValueError: print("Informe um numero valido!")
while True:
    valor2=input("Informe o segundo número:\t")
    try:
        valor2=int(valor2)
        break 
    except ValueError: print("Informe um numero valido!")
if valor1>valor2:
    print(f"O nuemero {valor1} é maior que o numero {valor2}")
elif valor1<valor2:
    print(f"O nuemero {valor2} é maior que o numero {valor1}")
else:
    print("Os numeros são iguais")
    

"""2) Crie um programa que possa marcar uma consulta médica. Como opções,
teremos disponíveis apenas 03 médicos, que devem ter seus nomes
exibidos na tela, p/ que possam ser escolhidos. Após a escolha do
profissional médico, exibir mensagem na tela informando que a consulta
foi marcada com o médico escolhido (nome do médico)."""
print("\n2º exercicio (escolha medico)")
print("Olá, para marcar a consulta você deve primeiramente escolher um medico")
print("As opções de medico são: \nDr. Rafael Almeida (digite 1)\nDra. Clara Souza (digite 2)\nDr. Lucas Pereira (digite 3)")
while True:
    escolha=input("Sua escolha é: \t")
    try: 
        escolha=int(escolha) 
        break
    except ValueError: print("Informe um numero valido")
if escolha==1:
    print("Seu medico escolhido foi: Dr. Rafael Almeida")
elif escolha==2:
    print("Sua medica escolhida foi: Dra. Clara Souza")
elif escolha==3:
    print("Seu medico escolhido foi: Dr. Lucas Pereira")
else: print("Nenhum medico escolhido!")


"""3) Escreva um programa que verifica se uma determinada palavra consta
em um texto de origem. O texto não será conhecido pelo usuário que
usará de palavras aleatórias na tentativa de adivinhar que palavras
compõem a frase oculta. Frase: "Python é uma excelente linguagem de
programação!!! Se acertar, a mensagem: "A palavra (palavra digitada
pelo usuário) está na frase". Se errar, a mensagem: "A palavra (palavra
digitada pelo usuário) não está na frase". Use a função "find", referenciada
na documentação:
https://docs.python.org/3/library/stdtypes.html"""
print("\n3º exercicio")
texto= "python é uma excelente linguagem de programação!!!"
while True:
    palavra=input("Insira uma palavra para procurar no texto").lower()
    if palavra.isalpha():
        break
    else:   print("Informe uma palavra sem usar simbolos ou numeros") 
if texto.find(palavra)!= -1:
    print(f"A palavra {palavra} esta no texto!") 
else: print(f"A palavra {palavra} não esta no texto!")


"""4) Crie um programa que leia um número e verifique se ele é par ou ímpar."""
print("\n4º exercicio (par ou impar)")
while True:
    num=input("Insira um numero: ")
    try: 
        num= int(num)
        break
    except ValueError:
        print("Informe um numero valido!")
if num%2 != 0:
    print(f"O numero {num} é impar")
else:
    print(f"O numero {num} é par")


"""5) Escreva um programa que receba dois números e verifique se ambos são
positivos."""
print("\n5º exercicio (verificar numeros positivos)")
while True:
    numero1=input("Insira um numero :\t")
    try:
        numero1=int(numero1)
        break
    except ValueError:  print("Informe um numero correto")
while True:
    numero2=input("Insira um segundo numero:\t")
    try:
        numero2=int(numero2)
        break
    except ValueError: print("Informe um numero correto")
    
if numero1>0 and numero2>0:
    print(f"Os numeros {numero1} e {numero2} são positivos")
elif numero1>0 or numero2>0:
    print(f"Os numeros {numero1} e {numero2} apenas um deles é positivo ")
    
else: print(f"Os numeros {numero1} e {numero2} não são positivos")


"""6) Crie um programa que leia dois números e exiba o maior entre eles. Caso
sejam iguais, exiba uma mensagem informando isso."""
print("\n6º exercicio (verificar maior ou menor)")
while True:
    num1=input("Informe o primeiro numero:\t")
    try:
        num1= int(num1)
        break
    except ValueError: 
        print("Informe um numero corretamente")
        
while True:
    num2=input("Informe o segundo numero:\t")
    try:
        num2= int(num2)
        break
    except ValueError: 
        print("Informe um numero corretamente")
    
if num1>num2:
    print(f"O numero {num1} é maior que {num2}")
elif num2>num1:
    print(f"O numero {num2} é maior que {num1}")
else: print(f"Os numeros {num1} e {num2} são iguais")


"""7) Crie um programa que receba o peso e a altura de uma pessoa e calcule
seu Índice de Massa Corporal (IMC). imc = peso / (altura * altura) . O
programa deve exibir uma mensagem na tela de acordo com a seguinte
tabela:
 Abaixo de 18.5: Abaixo do peso
 Entre 18.5 e 24.9: Peso normal
 Entre 25 e 29.9: Sobrepeso
 Acima de 30: Obesidade sdg"""
print("\n7º exercicio (IMC)")
peso=float(input("Informe seu peso (em Kg) ")).isnumeric()
altura=float(input("Informe sua altura (em metros!)  ")).isnumeric()
imc= peso/(altura*altura)
print(f"imc: {imc:.2f}")
if imc<=18.5:
    print("Você está abaixo do peso")
elif imc>=18.5 and imc<=24.9:
    print("Você está no peso normal")
elif imc>=25 and imc<=29.9:
    print("Você está em sobrepeso")
else: print("Obesidade, é importante consultar um profissional de saúde")
#fazer a 7 para verificação!!!