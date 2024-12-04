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
            int(num)
            break
    while True: 
        num2=input("Informe o segundo numero:  ")
        if not num2.isnumeric():
            print("Valor inválido, você deve inserir um número")
        else:
            int(num2)
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
        if escolha==1:
            soma=num+num2
            #print("o resultado é de ", soma)
            return "o resultado é de" + str(soma)
        elif escolha==2:
            subtracao=num-num2

            print("o resultado é de ", subtracao)
        elif escolha==3:
            multi=num*num2
            print("o resultado é de ", multi)
        elif escolha==4:
            divisao=num/num2
            print("o resultado é de ", divisao)

    
    
    
    
    
lista_de_exercicios_03_questão01()

