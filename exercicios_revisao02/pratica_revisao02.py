"""Arquivos no SIGAA - Campo Descrição
➢ Lista de exercícios 03; ##
➢ Lista de exercício estruturas condicionais ou de decisão; ##
➢ Exercício 01 - estruturas de repetição; ##
➢ Código exemplo validação da entrada via stdin;
➢ Lista For de exercícios. """##
def lista_de_exercicios_03_questão01():
    """1) Escreva um programa que peça ao usuário que informe dois valores
    numéricos de entrada, em seguida, exiba em tela o resultado da soma,
    subtração, multiplicação e divisão desses números. NÃO UTILIZAR
    FUNÇÃO P/ RESOLVER ESSA QUESTÃO. Se desejarem poderão
    utilizar o conceito de FString, concatenação de String, qualquer uma das
    sobrecargas de função responsável por imprimir no stdout."""
    while True:
        num=input("Informe o primeiro numero:  ")
        if not num.isnumeric():
            print("Valor inválido, você deve inserir um número")
        else:
            num= int(num)
            break
    while True: 
        num2=input("Informe o segundo numero:  ")
        if not num2.isnumeric():
            print("Valor inválido, você deve inserir um número")
        else:
            num2=int(num2)
            break

    print(f"     ➢os numeros escolhidos foram {num} e {num2}")
    print("     ➢Escolha sua operação matematica em que você queira fazer:")
    print("     ➢Escolha 1 para SOMA")
    print("     ➢Escolha 2 para SUBTRAÇÃO")
    print("     ➢Escolha 3 para MULTIPLICAÇÃO")
    print("     ➢Escolha 4 para DIVISÃO")

    escolha=input("confirme sua escolha:  ")
    if not escolha.isnumeric():
        print ("Valor invalido, tentar novamente")
        
    else:
        escolha=int(escolha)
        if escolha==1:
            soma=num+num2
            #print("o resultado é de ", soma)
            return "o resultado é de    " + str(soma)
                   
        elif escolha==2:
            subtracao=num-num2
            return "o resultado é de    "+ str(subtracao)
            #print("o resultado é de ", +subtracao)
        elif escolha==3:
            multi=num*num2
            #print("o resultado é de ", multi)
            return "o resultado é de    " + str(multi)
        elif escolha==4:
            divisao=num/num2
            #print("o resultado é de ", divisao)
            return "o resultado é de    " + str(divisao)
        

retorno_da_funcao=lista_de_exercicios_03_questão01()
print(retorno_da_funcao)


def IMC_funcao():
    """2) Escreva um programa que calcule o “índice de massa corporal” (IMC).
IMC = peso em quilos / altura 2. Exiba o resultado na tela. Utilizar valores
em ponto flutuante, precisão simples."""
    print("Calculadora de IMC")
    peso=float(input("Informe seu peso (em Kg) "))
    altura=float(input("Informe sua altura (em metros!)  "))
    imc= peso/(altura*altura)
    return "Seu IMC é de:   " +str(imc)
retorno_IMC=IMC_funcao()
print(retorno_IMC)

def procurar_na_frase():
    """3) Escreva um programa que exiba no terminal a mensagem: “Bem vindo
    turma da Programação II ao mundo da programação Python!!!” de trás p/
    a frente. Ou seja, o resultado esperado, deverá ser: !!!nohtyP
    oãçamargorp ad odnum oa II oãçamargorP ad amrut odniv meB. NÃO
    UTILIZAR FUNÇÃO P/ RESOLVER ESSA QUESTÃO. A função
    responsável por imprimir no stdout é uma das formas de resolver a
    questão."""

    print("\n\nprocurar na frase")
    frase = ("Bem vindo turma da Programação II ao mundo da programação Python!!!")
    ######### string=input
    string = frase[::-1]
    print('A frase que você digitou invertida fica: {}'.format(string))
    
    return