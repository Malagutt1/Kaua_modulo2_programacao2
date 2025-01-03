#####################################################ESTRUTURAS_DE_DADOS#####################################################
"""1. Crie 03 variáveis do tipo tupla que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das tuplas."""

def itens_tupla_questao_01(tupla):
    print(tupla)
    for i in tupla:
        print(i)
  

"""2. Crie 03 variáveis do tipo lista que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das listas."""
lista_dia_da_semana= ["Domingo","Segunda", "terça", "Quarta", "Quinta", "Sexta", "Sabado\n"]
lista_meses= ["Janeiro", "Fevereiro", "Março", "Abril", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro\n"]
lista_estacoes= ["verão", "outono", "inverno", "primavera\n"]
def itens_lista_questao_02(lista):
    for i in lista:
        print(i)
    

"""3. Exiba o tamanho e os elementos: primeiro, terceiro e último das estruturas de
dados criadas e inicializadas nas questões 1 e 2."""


def primeiro_terceiro_ultimo_item_da_lista(lista):
    print(lista[0])
    print(lista[2])
    print(lista[-1])

"""4. Crie uma lista de compras de supermercado com 15 itens. Através de um
laço de repetição, exiba na tela, cada um dos itens dessa lista de compras.
Você deve decidir que tipo de estrutura de dados utilizar e imprimir, logo
abaixo da lista de compras, os motivos da sua decisão, ou seja, explique
porque utilizou tal estrutura de dados."""
Lista_do_supermercado=["arroz", "feijão", "macarrão", "açúcar", "sal", "óleo", "leite", "ovos", "frutas", "legumes", "carne", "pão", "queijo", "café", "biscoitos"]
def lista_supermercado(itens_da_lista_de_compras):
    for i in itens_da_lista_de_compras:
        print(i)
    


#print("Questão 05: Adicionar, remover ou atualizar lista de Compras Questão 04")
def incluir_item_a_lista(lista_do_supermercado):
    novo_item= input("Informe um item a ser adicionado a lista de compras: ").lower()
    Lista_do_supermercado.append(novo_item)
    return f" O item {novo_item} foi adicionado com exito"
def remover_item_da_lista(item):
    print("\nItens da lista\n")
    for i in item:
        print(i)
    item_removido= input("\nInforme o nome de um item a ser renovido desta lista:").lower()
    Lista_do_supermercado.remove(item_removido)
    return f" O item {item_removido} foi removido com exito"
def atulizar_item_da_lista(item):
    nome_antigo_do_item=input("Informe o nome antido do item: ").lower()
    atualizar_lista=input("Digite o novo nome do item a ser atualizado: ").lower()
    if nome_antigo_do_item in item:
        novo_nome= item.index(nome_antigo_do_item)
        item[novo_nome]=atualizar_lista
        return(f" Item '{nome_antigo_do_item}' foi atualizado para '{atualizar_lista}'")
    else: return(f" o item {nome_antigo_do_item} não foi encontrado!")


"""6. Crie uma estrutura de dados que armazene o nome das linguagens de
programação: C, C++, JavaScript, Java, Lua e Python. Implemente um
programa que solicite ao usuário que tente adivinhar quais linguagens de
programação constam em uma lista oculta de nomes, informando, para tanto,
nomes de linguagens de programação. Exiba mensagem na tela para o
usuário informando se a linguagem consta ou não na lista oculta. A
funcionalidade de procurar em uma lista oculta de nomes deverá ser
implementada através de função."""
#print("Questão 6: Adivinha de linguagens de programação!")

def adivinha(linguagens_de_programacao):
    while True:
        adivinha_usuario=input("Digite o nome de uma linguagem de programação para tentar adivinhar\n    ").lower()
        if adivinha_usuario in linguagens_de_programacao:
            return(f" A linguagem {adivinha_usuario} estava no texto!")
        else: 
            return(f" A linguagem {adivinha_usuario} NÃo estava no texto!")
            
"""7. Crie um programa que possa marcar uma consulta médica. Utilize uma
estrutura de dados para armazenar o nome dos médicos que atendem na
clínica. Solicite ao usuário que informe com qual profissional deseja marcar
uma consulta médica. Implemente funções que possam: imprimir na tela o
nome dos profissionais, procurar na lista de profissionais o nome informado,
exibir na tela mensagem de que a consulta foi marcada com sucesso. Em
caso de falha, exibir mensagem na tela informando o usuário do ocorrido.""" 
#print("Questão 07: Marcar consulta com medico(a)\n")
medicos=("dr. gabriel costa", "dra. mariana souza", "dr. rafael oliveira", "dra. beatriz almeida", "dr. felipe martins")
def nome_medicos():
    print("Doutores e Doutorar que possam lhe atender neste momento:")
    for i in medicos:
        print(i)
    deseja_realizar_consulta=input("Deseja realizar consulta? (resonda com 'sim' e 'não')").lower()
    if deseja_realizar_consulta =="sim":
        consulta_medico=marcar_consulta()
        return consulta_medico
    elif deseja_realizar_consulta=="não" or "nao":
        return("Não foi realizado nenhuma consulta!")

def marcar_consulta():
    marcar_consulta_com_dr=input("Qual Dr(a) você gostaria de se consultar? ").lower()
    if marcar_consulta_com_dr in medicos:
        return(f"A consulta foi marcada com exito com {marcar_consulta_com_dr}!")
    else: return(f"Não foi possivel marcar consulta com {marcar_consulta_com_dr}. O nome pode ter sido digitado incorretamente ou não está na lista.")

"""9. Baseado no dicionário criado na questão 8, crie um programa que solicite ao usuário que 
informe o nome de um produto. Se o produto informado pelo usuário estiver na lista de compras do tipo 
dicionário, exiba a mensagem na tela: "O item {nome do produto} faz parte da lista de compras do supermercado".
 Senão, exiba a mensagem: "O item {nome do produto} NÃO faz parte da lista de compras do supermercado"."""
def item_esta_no_dicionario(lista_de_compras, Prod_digitado_pelo_usuario):
    lista_de_compras.get("Prod_Prod_digitado_pelo_usuario")
    if Prod_digitado_pelo_usuario is None:
        return (f"O item {Prod_digitado_pelo_usuario} NÃO faz parte da lista de compras do supermercado")
    else: return (f"O item {Prod_digitado_pelo_usuario} faz parte da lista de compras do supermercado")
    #if Prod_digitado_pelo_usuario in lista_de_compras:
    
    
#####################################################FUNCOES_STRING#####################################################
OPCAO_SINTAXE                  = 1
OPCAO_SEMANTICA                = 2
OPCAO_LACO_INFINITO            = 3
OPCAO_VARIAVEL                 = 4
CONCEITO_TEORICO_SINTAXE       = "Sintaxe é o conjunto de regras e estruturas que definem como o código deve ser escrito."
CONCEITO_TEORICO_SEMANTICA     = "Semântica diz respeito ao significado das instruções/estruturas de uma linguagem de programação. Aquilo que faz sentido dentro da linguagem."
CONCEITO_TEORICO_LACO_INFINITO = "Um laço infinito é uma condição de erro que pode ocorrer nas estruturas de repetição das linguagens de programação. Acontece quando o controle do laço nunca se torna falso, fazendo com que o laço de repetição execute infinitamente. Isso causa um consumo elevado dos recursos de máquina e o travamento do programa. A correta atualização do controle do laço, sua verificação a cada iteração e a garantia de que uma condição de parada será alcançada, são medidas para evitar que a condição de laço infinito aconteça."
CONCEITO_TEORICO_VARIAVEL      = "Variável, em linguagem de programação, é um espaço de memória do computador usado para armazenar um valor, de forma temporária, que pode ser alterado durante a execução do programa."



#QUESTÃO 01 || CALCULAR TAMANHO DA MUSICA DO CHAVES
def calcular_tamanho_da_string(letra_da_musica):  #função principal
    if (type(letra_da_musica)==str):
        return len(letra_da_musica)
    else:
        return -1
    
# QUESTÃO 02 || DESCOBRIR LETRA PELO NUMERO 
def obter_caracter(string, indice):
    # Verificador de indice
    if indice < 0 or indice >= len(string):
        return -1
    return string[indice-1]
def principal():
    string_analise = input("Digite a string: ")
    
    try:
        posicao_caracter = int(input("Digite o índice da letra que você quer saber: "))
    except ValueError:
        print("Erro: o índice deve ser um número inteiro.")
        return
    
    resultado = obter_caracter(string_analise, posicao_caracter)
    
    if resultado == -1:
        print(f"Índice fora do intervalo. A String não possui o índice {posicao_caracter}.")
    else:
        print(f"O caractere na posição {posicao_caracter} é '{resultado}'.")


# QUESTÃO 03 || ENUMERAÇÃO DAS LETRAS DE UMA STRING
def exibirCaracteresString(stringCaracteres):
    for contador in range(len(stringCaracteres)):
        print(f"{stringCaracteres[contador]} - {contador + 1}º caracter da String \"{stringCaracteres}\"")
        
# QUESTÃO 04 || FINAL FRASE TERMINA COM ____ 
def finalFrase(frase, terminoFrase):
    return frase.endswith(terminoFrase)

# QUESTÃO 05 || CONCEITO LINGUAGENS DE PROGRAMAÇÃO
def conceitosTeoricosLinguagensProgramacao(opcaoDigitadaPeloUsuario):
    
    if int(opcaoDigitadaPeloUsuario) ==  OPCAO_SINTAXE :
        return CONCEITO_TEORICO_SINTAXE
            
    elif int(opcaoDigitadaPeloUsuario) == OPCAO_SEMANTICA :
        return CONCEITO_TEORICO_SEMANTICA
        
    elif int(opcaoDigitadaPeloUsuario) == OPCAO_LACO_INFINITO :
        return CONCEITO_TEORICO_LACO_INFINITO
        
    elif int(opcaoDigitadaPeloUsuario) == OPCAO_VARIAVEL :
        return CONCEITO_TEORICO_VARIAVEL
    
    else:
        return ""        

def menuDeOpcoes():
    print("\n" + """ 1 - Sintaxe \n 2 - Semântica \n 3 - Laço Infinito \n 4 - Variável \n Sair \n""")

def validarCodigoConceitoInformado(codigoConceitoTeorico, opcaoDigitadaPeloUsuario):
    opcaoValida = True
    
    if not opcaoDigitadaPeloUsuario.strip().isnumeric():
        opcaoValida = False
    else:
        if (int(codigoConceitoTeorico) != OPCAO_SINTAXE and int(codigoConceitoTeorico) != OPCAO_SEMANTICA
            and int(codigoConceitoTeorico) != OPCAO_LACO_INFINITO and int(codigoConceitoTeorico) != OPCAO_VARIAVEL):    
            opcaoValida = False
        
    return opcaoValida

# QUESTÃO 06 || VALIDAR SENHA  
import re
def validarTamanhoSenha(senhaInformada):
    senhaComTamanhoCorreto = True
    
    tamanhoDaSenha = len(senhaInformada)
    
    if tamanhoDaSenha < 6:
        senhaComTamanhoCorreto = False
    elif tamanhoDaSenha > 20:
        senhaComTamanhoCorreto = False
        
    return senhaComTamanhoCorreto

def validarCaracteresMinusculos(senhaInformada):
    #"[a-z]" expressão regular que valida se a senha tem PELO MENOS UMA LETRA MINUSCULA
    return re.search("[a-z]", senhaInformada) != None

def validarCaracteresMaiusculos(senhaInformada):
    #"[A-Z]" expressão regular que valida se a senha tem PELO MENOS UMA LETRA MAIUSCULA 
    return re.search("[A-Z]", senhaInformada) != None

def validarCaracteresNumericos(senhaInformada):
    #"[0-9]" expressão regular que valida se a senha tem PELO MENOS UM NÚMERO
    return re.search("[0-9]", senhaInformada) != None

def validarCaracteresEspeciais(senhaInformada, listaDeCaracteresEspeciais):
    #"[$#@!&]" expressão regular que valida se a senha tem PELO MENOS UM CARACTER ESPECIAL que consta na lista 
    return re.search(listaDeCaracteresEspeciais, senhaInformada) != None

def validarCaracteresWhiteSpace(senhaInformada):
    #\s verifica se existem caracteres “whitespace” na senha, o que não é permitido
    return re.search(r"\s", senhaInformada) != None

# QUESTÃO 07 || TRANSFORMAR PRIMEIRA LETRA EM MAIUSCULA
def primeiraLetraMaiuscula(nomeMinusculo):
    nomeMinusculo = nomeMinusculo.lower()
    return nomeMinusculo.title()

# QUESTÃO 08 || INSERIR CARACTER A PALAVRA DO USUARIO
def inserir_caracter(string, caracter):
    return caracter.join(string)



#####################################################PRATICA_REVISÃO_02#####################################################
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
    def maior_menor():
        """1) Crie 2 variáveis com dois valores numéricos inteiros informados pelo
        usuário, caso o valor do primeiro número for maior do que o segundo,
        exiba em tela uma mensagem de acordo, caso contrário, exiba em tela
        uma mensagem dizendo que o primeiro valor digitado é menor que o
        segundo. Os números informados pelo usuário devem aparecer em
        ambas as mensagens."""
        print("\nVerificar numero maior e numero menor:")
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
            except ValueError: 
                return("Informe um numero valido!")
        if valor1>valor2:
            return(f"O nuemero {valor1} é maior que o numero {valor2}")
        elif valor1<valor2:
            return(f"O nuemero {valor2} é maior que o numero {valor1}")
        else:
            #print("Os numeros são iguais")
            return ("Os numeros são iguais")
    Verificar_maior_menor=maior_menor()
    print(Verificar_maior_menor)
            
    def escolha_medico():
        print("\nEscolher medico:")
        """2) Crie um programa que possa marcar uma consulta médica. Como opções,
        teremos disponíveis apenas 03 médicos, que devem ter seus nomes
        exibidos na tela, p/ que possam ser escolhidos. Após a escolha do
        profissional médico, exibir mensagem na tela informando que a consulta
        foi marcada com o médico escolhido (nome do médico)."""
        #print("\n2º exercicio (escolha medico)")
        print("Olá, para marcar a consulta você deve primeiramente escolher um medico")
        print("As opções de medico são: \nDr. Rafael Almeida (digite 1)\nDra. Clara Souza (digite 2)\nDr. Lucas Pereira (digite 3)")
        while True:
            escolha=input("Sua escolha é: \t")
            try: 
                escolha=int(escolha) 
                break
            except ValueError: return("Informe um numero valido")
        if escolha==1:
            return("Seu medico escolhido foi: Dr. Rafael Almeida")
        elif escolha==2:
            return("Sua medica escolhida foi: Dra. Clara Souza")
        elif escolha==3:
            return("Seu medico escolhido foi: Dr. Lucas Pereira")
        else: 
            return("Nenhum medico escolhido!")
    medico_escolhido_pelo_usuario=escolha_medico()
    print(medico_escolhido_pelo_usuario)

    def procurar_palavra_no_texto():
        """3) Escreva um programa que verifica se uma determinada palavra consta
        em um texto de origem. O texto não será conhecido pelo usuário que
        usará de palavras aleatórias na tentativa de adivinhar que palavras
        compõem a frase oculta. Frase: "Python é uma excelente linguagem de
        programação!!! Se acertar, a mensagem: "A palavra (palavra digitada
        pelo usuário) está na frase". Se errar, a mensagem: "A palavra (palavra
        digitada pelo usuário) não está na frase". Use a função "find", referenciada
        na documentação:
        https://docs.python.org/3/library/stdtypes.html"""
        print("\nProcurar palavra no texto")
        texto= "python é uma excelente linguagem de programação!!!"
        while True:
            palavra=input("Insira uma palavra para procurar no texto").lower()
            if palavra.isalpha():
                break
            else:   return("Informe uma palavra sem usar simbolos ou numeros") 
        if texto.find(palavra)!= -1:
            return(f"A palavra {palavra} esta no texto!") 
        else: return(f"A palavra {palavra} não esta no texto!")
    palavra_procurada_no_texto=procurar_palavra_no_texto()
    print(palavra_procurada_no_texto)

    def par_impar():
        """4) Crie um programa que leia um número e verifique se ele é par ou ímpar."""
        print("\nVerificar numero (par ou impar)")
        while True:
            num=input("Insira um numero: ")
            try: 
                num= int(num)
                break
            except ValueError:
                return("Informe um numero valido!")
        if num%2 != 0:
            return(f"O numero {num} é impar")
        else:
            return(f"O numero {num} é par")
    este_numero_par_impar=par_impar()
    print(este_numero_par_impar)

    def numero_positivo():
        """5) Escreva um programa que receba dois números e verifique se ambos são
        positivos."""
        print("\nverificar numeros positivos")
        while True:
            numero1=input("Insira um numero :\t")
            try:
                numero1=int(numero1)
                break
            except ValueError:  return("Informe um numero correto")
        while True:
            numero2=input("Insira um segundo numero:\t")
            try:
                numero2=int(numero2)
                break
            except ValueError: return("Informe um numero correto")
            
        if numero1>0 and numero2>0:
            return(f"Os numeros {numero1} e {numero2} são positivos")
        elif numero1>0 or numero2>0:
            return(f"Os numeros {numero1} e {numero2} apenas um deles é positivo ")
        else: return(f"Os numeros {numero1} e {numero2} não são positivos")
    verificador_de_numero_positivos=numero_positivo()
    print(verificador_de_numero_positivos)

    def maior_menor_de_2_numeros():
        """6) Crie um programa que leia dois números e exiba o maior entre eles. Caso
        sejam iguais, exiba uma mensagem informando isso."""
        print("\nMaior e menor numero")
        while True:
            num1=input("Informe o primeiro numero:\t")
            try:
                num1= int(num1)
                break
            except ValueError: 
                return("Informe um numero corretamente")
                
        while True:
            num2=input("Informe o segundo numero:\t")
            try:
                num2= int(num2)
                break
            except ValueError: 
                return("Informe um numero corretamente")
            
        if num1>num2:
            return(f"O numero {num1} é maior que {num2}")
        elif num2>num1:
            return(f"O numero {num2} é maior que {num1}")
        else: return(f"Os numeros {num1} e {num2} são iguais")
    maior_menor_two_numeros=maior_menor_de_2_numeros()
    print(maior_menor_two_numeros)
    

    def IMC_com_categoria_de_imc():  # problema que eu não sei o que deu (Print do Imc não estava querendo funcionar dentro do return!)
        """7) Crie um programa que receba o peso e a altura de uma pessoa e calcule
        seu Índice de Massa Corporal (IMC). imc = peso / (altura * altura) . O
        programa deve exibir uma mensagem na tela de acordo com a seguinte
        tabela:
         Abaixo de 18.5: Abaixo do peso
         Entre 18.5 e 24.9: Peso normal
         Entre 25 e 29.9: Sobrepeso
         Acima de 30: Obesidade sdg"""
        print("\nIMC e sua categoria")
        peso=float(input("Informe seu peso (em Kg) "))
        altura=float(input("Informe sua altura (em metros!)  "))
        imc= peso/(altura*altura)
        print(f"imc: {imc:.2f}") #no return (dentro de um if) não estava querendo funcionar (exemplo do que eu fiz abaixo!)
        if imc<=18.5:
            return("Você está abaixo do peso") #return f"imc:"+str(imc) + "\nVocê está abaixo do peso"
        elif imc>=18.5 and imc<=24.9:
            return("Você está no peso normal") #return f"imc:" +str(imc) + "\nVocê está no peso normal"
        elif imc>=25 and imc<=29.9:
            return("Você está em sobrepeso")   #return f"imc:"+str(imc) +"\nVocê está em sobrepeso"
        else: return("Obesidade, é importante consultar um profissional de saúde") #return f"imc:"+str(imc) +"\nObesidade, é importante consultar um profissional de saúde"
    IMC_categorizado=IMC_com_categoria_de_imc()
    print(IMC_categorizado)

    return

def exercicio_01_estruturas_repeticao():  # return em todos
    def contagem_até_10():
        """1) Crie e inicialize uma variável do tipo inteiro. Enquanto o valor dessa variável for
        menor ou igual a um valor definido por você, exiba uma mensagem na tela e o
        valor dessa variável. Explique em um comentário como o controle do laço vai
        funcionar."""
        print("1 questão:")
        numero=1
        while (numero<=10):
            print(f" {numero}º numero")
            numero+=1
        return
    contagem_até_10()

    def num_aleatorio():
        """2) Escreva um programa que gera um número aleatório entre 0 a 10, salvando
        esse número em uma variável. Solicite ao usuário que tente adivinhar o
        número que foi gerado aleatoriamente através da digitação via stdin. Caso o
        usuário acerte o número, exiba uma mensagem parabenizando-o e mostrando
        na mensagem o número adivinhado. Utilize a instrução “import” para que a
        biblioteca Random possa ser utilizada. O número aleatório deverá ser
        gerado através da função randint. Restrinja ao máximo de 5 tentativas por
        parte do usuário, caso não acerte, exiba mensagem e termine o programa."""
        print("\n2 questão:")
        import random
        numero_gerado=random.randint(0,10)
        tentativa=0
        max=5
        while tentativa<max:
            teste=input("Insira um numero de 1 a 10:\t")
            if teste.isnumeric():
                teste=int(teste)

                if teste==numero_gerado:
                    print(" Seu numero foi o correto!\a")
                    break
                else:
                    print("Numero incorreto!")
                    tentativa+=1
                    return
        num_aleatorio()
    def verificar_site():
        """3) Escreva um programa que verifica se um endereço URL de um site foi digitado
        levando-se em conta o prefixo “www.” e o sufixo “.com.br”. Se o endereço foi
        digitado nesse formato corretamente, exiba mensagem, inclusive mostrando o
        endereço digitado, e finalize o programa. Se não digitou corretamente, exiba
        uma mensagem informando que a URL é inválida, mostre o endereço no
        formato errado e solicite ao usuário que digite novamente a URL do site. Uma
        forma de resolver esse problema é utilizar métodos da classe String do Python,
        como por exemplo: startswith() e endswith(). A documentação desses métodos
        pode ser encontrada em: https://docs.python.org/ptbr/3/library/stdtypes.html.dgs
        Enquanto a URL informada não estiver correta, o programa não deve ser
        finalizado."""
        print("\n3 questão:")
        while True:
            url_informado=input("Informe uma URL: \t")
            if url_informado. startswith("www.") and (url_informado.endswith(".com.br") or url_informado.endswith(".com")) :
                print(f"É uma URL val valida: {url_informado}")
                break
            else: print(f"Nâo é uma URL val valida: {url_informado}")
    verificar_site()
    
    return

def codigo_exemplo_validacao_stdin():
    def codigo_exemplo_validacao_entrada():
        primeiroValorInformadoPeloUsuario = input("Digite o primeiro número: ")
        segundoValorInformadoPeloUsuario  = input("Digite o segundo número: ")

        #Validação do tipo de entrada informada pelo Stdin (teclado)
        if not (primeiroValorInformadoPeloUsuario.strip().isnumeric()):
            return(f"O primeiro valor informado: \"{primeiroValorInformadoPeloUsuario}\" não é um valor numérico válido.")
        elif (not (segundoValorInformadoPeloUsuario.strip().isnumeric())):
            return(f"O segundo valor informado: \"{segundoValorInformadoPeloUsuario}\" não é um valor numérico válido.")
        else:
            opcaoDigitadaPeloUsuario = input("Informe um valor numérico de 1 a 10: ")
            
            #Validação do tipo de entrada informada pelo Stdin (teclado)
            if not (opcaoDigitadaPeloUsuario.strip().isnumeric()):
                return(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")
                
            elif (int(opcaoDigitadaPeloUsuario) <= 0 or int(opcaoDigitadaPeloUsuario) > 10):
                return(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")
            else:
                return("Todos os valores numéricos informados via stdin foram válidos.")    
    validacao_entrada=codigo_exemplo_validacao_entrada()
    print(validacao_entrada)
    return

def lista_for_exercicios(): # return em todos
    def IFSC_horizontal_vertical():
        """1) Crie uma estrutura de repetição que percorra a String “Instituto Federal
        de Santa Catarina” exibindo na tela letra por letra dessa String, tanto na
        orientação horizontal quanto na vertical."""
        print("\nIFSC sigla na horizontal e vertical:")
        for item_da_lista in "Instituto Federal de Santa Catarina":
            print(item_da_lista)
            mostrar_na_horizontal= ""
        for item_da_lista in "Instituto Federal de Santa Catarina":
            mostrar_na_horizontal+=item_da_lista
        print(mostrar_na_horizontal)
    IFSC_horizontal_vertical()

    def contagem_ate_20():
        """2) Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os
        números pares."""
        print("exercicio 2")
        for par in range(0,21,2): 
            print (par)
    contagem_ate_20()
    
        
    def tabuada():
        """3) Crie um programa que exiba na tela a tabuada de um determinado número
        fornecido pelo usuário."""
        print("exercicio 3")
        tabuada_do_usuario=int(input("Insira um numero para fazer a tabuada:\t"))
        for i in range(1,11):
            tabuada= tabuada_do_usuario*i
            print(f"Tabuada= {tabuada_do_usuario}x{i}={tabuada} ")
    tabuada()

    def contagem_regressiva_até_20():
        """4) Crie um programa que realiza a contagem regressiva de 20 segundos."""
        print("exercicio 4") 
        import time
        for cont_regressiva in range(20,0,-1):
            print("Contagem regressiva:")
            print(cont_regressiva)
            time.sleep(1)  #tirar aspas pois estava com o contador de 20 segundos
        print("Seu tempo acabou!")   
        return
    contagem_regressiva_até_20()

    def quant_par_impar_ate_100():
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
    quant_par_impar_ate_100()

    def num_primo():
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
            return
    num_primo()

    def polindromo():
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
            return
    polindromo()

    def numeros_em_sequencia():
        """8) Crie uma função de número de parâmetros indefinido, que realize a soma
        dos números passados como parâmetro, independentemente da
        quantidade de parâmetros."""
        print("exercicio 8")
        numeros = input("Digite os números separados por espaço: ").split()
        soma = 0
        for numero in numeros:
            soma += int(numero)
        print(f"A soma dos números é: {soma}")
        return
    numeros_em_sequencia()

    def palavras_na_frase_minuscula_maiuscula():
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
    palavras_na_frase_minuscula_maiuscula()
    

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
            codigo_exemplo_validacao_stdin()
            
            i+=1
        elif escolher_funcao_para_ser_executada =="5":
            lista_for_exercicios()
            i+=1
        elif escolher_funcao_para_ser_executada=="sair":
            exit()
