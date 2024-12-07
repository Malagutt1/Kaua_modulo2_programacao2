"""Arquivos no SIGAA - Campo Descrição
➢ Lista de exercícios 03; ##
➢ Lista de exercício estruturas condicionais ou de decisão; ##
➢ Exercício 01 - estruturas de repetição; ##
➢ Código exemplo validação da entrada via stdin;
➢ Lista For de exercícios. """##
def lista_de_exrcicios_03():
    def lista_de_exercicios_03_questão01():
        print("\nCalculadora de 2 números")

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
        print("\nCalculadora de IMC (Índice de Massa Corporal)")
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
        print("\nMensagem de boas-vindas invertida:")
        """3) Escreva um programa que exiba no terminal a mensagem: “Bem vindo
        turma da Programação II ao mundo da programação Python!!!” de trás p/
        a frente. Ou seja, o resultado esperado, deverá ser: !!!nohtyP
        oãçamargorp ad odnum oa II oãçamargorP ad amrut odniv meB. NÃO
        UTILIZAR FUNÇÃO P/ RESOLVER ESSA QUESTÃO. A função
        responsável por imprimir no stdout é uma das formas de resolver a
        questão."""
        frase = ("Bem vindo turma da Programação II ao mundo da programação Python!!!")
        ######### string=input
        string = frase[::-1]
        #print('A frase que você digitou invertida fica: {}'.format(string))
        return "A frase que você digitou invertida fica: {}" .format(string)
    retorno_procurar_na_frase=procurar_na_frase()
    print(retorno_procurar_na_frase)

    def gerar_senha_aleatoria():
        """4) Crie um programa que gere uma senha aleatória, com um tamanho
        definido pelo usuário. O tamanho da senha deverá ser representado por
        um número inteiro, positivo, maior do que ZERO. A SENHA GERADA
        NÃO PODERÁ TER MAIS DO QUE 128 CARACTERES. Ou seja, se o
        usuário digitar o valor 8, uma senha de 8 caracteres de verá ser gerada.
        Funções da Biblioteca Padrão do Python: https://docs.python.org/ptbr/3/library/ poderão ser utilizadas.
        Utilize como base da senha, um valorUUID (universally unique identifier) identificador universalmente exclusivo.
        Procurar na Internet por gerador online UUID p/ obter valores UUID."""
        print("\nGerador de senhas:")
        import random
        tamanho=int(input("Informe a quantidade de caracteres: "))
        uuid_gerador_senha= "bfb773b4093a47549d103888e0dcea5d7e5dd88bb7d240518e5362693319b41cf0d1002d5f8f44f8865a4cb50964c37ab9499b01c04441ef80f8628a931aa3f217000ab30e9d4b3eaa5a22186559a1a4"
        senha_gerada= " ". join(random.sample(uuid_gerador_senha, tamanho))
        #print(f"senha gerada com {senha_gerada}")
        return f"senha gerada com {senha_gerada}"
    senha_criada=gerar_senha_aleatoria()
    print(senha_criada)

    def data_hora():
        """5) Crie um programa que mostra a data atual, no formato: dia/mês/ano
        hora:minuto:segundo. Funções da Biblioteca Padrão do Python:
        https://docs.python.org/pt-br/3/library/ poderão ser utilizadas."""
        print("\n Mostrar data e hora")
        import datetime 
        agora= datetime.datetime.now()
        return agora.strftime("%d/%m/%y  %H:%M:%S")
    data_hora_formatada=data_hora()
    print(f"{data_hora_formatada}\n")
    return #lista_de_exrcicios_03

def lista_exercicio_estruturas_condicionais():
    
    return

def exercicio_01_estruturas_repeticao():
    return

def codigo_exemplo_validacao_entrada():
    return

def lista_for_exercicios():
    return

def area_teste():
    def data_hora():
        """5) Crie um programa que mostra a data atual, no formato: dia/mês/ano
        hora:minuto:segundo. Funções da Biblioteca Padrão do Python:
        https://docs.python.org/pt-br/3/library/ poderão ser utilizadas."""
        print("\n\nQUESTÃO 05")
        import datetime 
        agora= datetime.datetime.now()
        return agora.strftime("%D/%m/%y  %h:%M:%S")
    data_hora_formatada=data_hora()
    print(data_hora_formatada)
    
    return



def funcao_principal():
    i=1
    while i <=10:
        escolher_funcao_para_ser_executada=input("1 = Lista de exercícios 03\n2 = Lista de exercício estruturas condicionais ou de decisão\n3 = Exercício 01 - estruturas de repetição\n4 = Código exemplo validação da entrada via stdin\n5 = Lista For de exercícios\nDigite 'sair' para parar o código.\n    Digite a opção selecionada: ").lower()
        if escolher_funcao_para_ser_executada =="1":
            lista_de_exrcicios_03()
            i+=1
        elif escolher_funcao_para_ser_executada =="2":
            lista_exercicio_estruturas_condicionais()
            i+=1
        elif escolher_funcao_para_ser_executada =="3":
            exercicio_01_estruturas_repeticao()
            i+=1
        elif escolher_funcao_para_ser_executada =="4":
            codigo_exemplo_validacao_entrada()
            i+=1
        elif escolher_funcao_para_ser_executada =="5":
            lista_for_exercicios()
            i+=1
        elif escolher_funcao_para_ser_executada=="area_teste": #area teste aleatoria
            area_teste()
            i+=1
        elif escolher_funcao_para_ser_executada=="sair":
            exit()
    return
funcao_principal()

