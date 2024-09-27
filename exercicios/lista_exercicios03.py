"""Utilizar padrão de escrita de código em Python: Camel_Case e\ou snake_case

Se desejar executar um trecho específico de código, selecione-o e
pressione Shift + Enter ou clique com o botão direito e escolha "Run
Selection/Line in Python Terminal"."""


"""1) Escreva um programa que peça ao usuário que informe dois valores
numéricos de entrada, em seguida, exiba em tela o resultado da soma,
subtração, multiplicação e divisão desses números. NÃO UTILIZAR
FUNÇÃO P/ RESOLVER ESSA QUESTÃO. Se desejarem poderão
utilizar o conceito de FString, concatenação de String, qualquer uma das
sobrecargas de função responsável por imprimir no stdout."""

num=int(input("Informe o primeiro numero"))
num2=int(input("Informe o segundo numero"))
print(f"os numeros escolhidos foram {num} e {num2}")
print("Escolha sua operação matematica em que você queira fazer:")
print("Escolha 1 para SOMA")
print("Escolha 2 para SUBTRAÇÃO")
print("Escolha 3 para MULTIPLICAÇÃO")
print("Escolha 4 para DIVISÃO")

escolha=int(input("confirme sua escolha:  "))
if escolha==1:
    soma=num+num2
    print("o resultado é de ", soma)
elif escolha==2:
    subtracao=num-num2
    print("o resultado é de ", subtracao)
elif escolha==3:
    multi=num*num2
    print("o resultado é de ", multi)
elif escolha==4:
    divisao=num/num2
    print("o resultado é de ", divisao)
else:
    print("operação invalida")
    
    




"""2) Escreva um programa que calcule o “índice de massa corporal” (IMC).
IMC = peso em quilos / altura 2. Exiba o resultado na tela. Utilizar valores
em ponto flutuante, precisão simples."""
print("\n\nQUESTÃO 02")
peso=float(input("Informe seu peso (em Kg) "))
altura=float(input("Informe sua altura (em metros!)  "))
imc= peso/(altura*altura)
print(imc)



"""3) Escreva um programa que exiba no terminal a mensagem: “Bem vindo
turma da Programação II ao mundo da programação Python!!!” de trás p/
a frente. Ou seja, o resultado esperado, deverá ser: !!!nohtyP
oãçamargorp ad odnum oa II oãçamargorP ad amrut odniv meB. NÃO
UTILIZAR FUNÇÃO P/ RESOLVER ESSA QUESTÃO. A função
responsável por imprimir no stdout é uma das formas de resolver a
questão."""

print("\n\nQUESTÃO 03")
frase = ("Bem vindo turma da Programação II ao mundo da programação Python!!!")
string = frase[::-1]
print('A frase que você digitou invertida fica: {}'.format(string))

#Link referencia:https://pt.stackoverflow.com/questions/401489/inverter-as-palavras-de-uma-frase-mantendo-a-ordem-delas-na-frase



"""4) Crie um programa que gere uma senha aleatória, com um tamanho
definido pelo usuário. O tamanho da senha deverá ser representado por
um número inteiro, positivo, maior do que ZERO. A SENHA GERADA
NÃO PODERÁ TER MAIS DO QUE 128 CARACTERES. Ou seja, se o
usuário digitar o valor 8, uma senha de 8 caracteres de verá ser gerada.
Funções da Biblioteca Padrão do Python: https://docs.python.org/ptbr/3/library/ poderão ser utilizadas.
Utilize como base da senha, um valorUUID (universally unique identifier) identificador universalmente exclusivo.
Procurar na Internet por gerador online UUID p/ obter valores UUID."""
print("\n\nQUESTÃO 04")
import random
tamanho=int(input("Informe a quantidade de caracteres: "))
uuid_gerador_senha= "bfb773b4093a47549d103888e0dcea5d7e5dd88bb7d240518e5362693319b41cf0d1002d5f8f44f8865a4cb50964c37ab9499b01c04441ef80f8628a931aa3f217000ab30e9d4b3eaa5a22186559a1a4"
senha_gerada= " ". join(random.sample(uuid_gerador_senha, tamanho))
print(f"senha gerada com {senha_gerada}")

"""5) Crie um programa que mostra a data atual, no formato: dia/mês/ano
hora:minuto:segundo. Funções da Biblioteca Padrão do Python:
https://docs.python.org/pt-br/3/library/ poderão ser utilizadas."""
print("\n\nQUESTÃO 05")


