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
            


#while True:
#    continuar_jogando= input("Continuar jogando?").lower()
#    if continuar_jogando=="sim":
#        return_adivinha= adivinha()
#        print(return_adivinha)
#    elif continuar_jogando=="não":
#        break

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
    

#medicos_escolhidos=nome_medicos()
#print(medicos_escolhidos)

