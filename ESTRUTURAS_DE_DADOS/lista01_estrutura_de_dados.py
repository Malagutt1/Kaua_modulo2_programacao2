import sys
sys.path.append(".")
sys.path.append("../custom_utils/utils")

from custom_utils import utils

tupla_dia_da_semana= ("Domingo","Segunda", "terça", "Quarta", "Quinta", "Sexta", "Sabado\n")
tupla_meses= ("Janeiro", "Fevereiro", "Março", "Abril", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro\n") 
tupla_estacoes= ("verão", "outono", "inverno", "primavera\n")

print("Questão 01: 3 variaveis do tipo tupla")
print("Dia da semana:")
utils.itens_tupla_questao_01(tupla_dia_da_semana)
print("Meses do ano:")
utils.itens_tupla_questao_01(tupla_meses)
print("Estações do ano:")
utils.itens_tupla_questao_01(tupla_estacoes)
print("\n\n")

"""2. Crie 03 variáveis do tipo lista que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das listas."""
lista_dia_da_semana= ["Domingo","Segunda", "terça", "Quarta", "Quinta", "Sexta", "Sabado\n"]
lista_meses= ["Janeiro", "Fevereiro", "Março", "Abril", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro\n"]
lista_estacoes= ["verão", "outono", "inverno", "primavera\n"]
def itens_lista_questao_02(lista):
    for i in lista:
        print(i)
    return
print("Questão 02: 3 variaveis do tipo lista")
print("Dia da semana:")
utils.itens_tupla_questao_01(lista_dia_da_semana)
print("Meses do ano:")
utils.itens_tupla_questao_01(lista_meses)
print("Estações do ano:")
utils.itens_tupla_questao_01(lista_estacoes)




"""3. Exiba o tamanho e os elementos: primeiro, terceiro e último das estruturas de
dados criadas e inicializadas nas questões 1 e 2."""
print("Questão 03: Tamanho e elementos das questões 01 e 02")
# O que é para eu fazer? Não entendi (primeiro, terceiro e ultimo).
print("Primeiro, terceiro e ultimo (Tupla dia da semana)")
utils.primeiro_terceiro_ultimo_item_da_lista(tupla_dia_da_semana)
print("\nPrimeiro, terceiro e ultimo (Tupla meses)")
utils.primeiro_terceiro_ultimo_item_da_lista(tupla_meses)
print("\nPrimeiro, terceiro e ultimo (Tupla estações do ano)")
utils.primeiro_terceiro_ultimo_item_da_lista(tupla_estacoes)
print("\nPrimeiro, terceiro e ultimo (Lista dia da semana)")
utils.primeiro_terceiro_ultimo_item_da_lista(lista_dia_da_semana)
print("\nPrimeiro, terceiro e ultimo (Lista meses)")
utils.primeiro_terceiro_ultimo_item_da_lista(lista_meses)
print("\nPrimeiro, terceiro e ultimo (Lista estações do ano)")
utils.primeiro_terceiro_ultimo_item_da_lista(lista_estacoes)

"""4. Crie uma lista de compras de supermercado com 15 itens. Através de um
laço de repetição, exiba na tela, cada um dos itens dessa lista de compras.
Você deve decidir que tipo de estrutura de dados utilizar e imprimir, logo
abaixo da lista de compras, os motivos da sua decisão, ou seja, explique
porque utilizou tal estrutura de dados."""

print("Questão 04: Lista de supermercado e esclarecimento")
Lista_do_supermercado=["arroz", "feijão", "macarrão", "açúcar", "sal", "óleo", "leite", "ovos", "frutas", "legumes", "carne", "pão", "queijo", "café", "biscoitos"]
utils.lista_supermercado(Lista_do_supermercado)
print("Esclarecimento da escolha: Optei por usar uma LISTA porque, ao contrário de uma TUPLA, que é imutável, uma lista de supermercado pode ser removido ou adicionado itens a ela")

"""5. Crie um programa que atualize a lista de compras da questão 4. O programa
deve solicitar ao usuário, através de um menu de opções, que tipo de
operação deseja efetuar sobre a lista de compras: incluir um novo item,
remover um item ou atualizar um item existente. Crie uma função para cada
tipo de operação permitida. Após o usuário informar uma das opções válida
do menu, o programa deve solicitar que o usuário digite o nome do
produto\item para que a função correta seja chamada e a alteração da lista
de compras possa ser feita. Implemente uma forma de encerrar o programa
através da interação do usuário."""
print("Questão 05: Adicionar, remover ou atualizar lista de Compras Questão 04")
while True:
    escolha_usuario=input("1= Incluir Item\n2= Excluir Item\n3= Atualizar Nome do Item\n4= Mostrar itens da lista\ndigite 'SAIR' para enserar o programa!\n").lower()
    if escolha_usuario=="1":
        new_item=utils.incluir_item_a_lista(Lista_do_supermercado)
        print(new_item)
    elif escolha_usuario=="2":
        item_da_lista_removido= utils.remover_item_da_lista(Lista_do_supermercado)
        print(item_da_lista_removido)
    elif escolha_usuario=="3":
        utils.atulizar_item_da_lista(Lista_do_supermercado)
    elif escolha_usuario=="4":
        print("\n")
        for i in Lista_do_supermercado:
            print(i)
        print("\n")
    elif escolha_usuario== "sair":
        break

          


while True:
    continuar_jogando= input("Continuar jogando?").lower()
    if continuar_jogando=="sim":
        return_adivinha= utils.adivinha()
        print(return_adivinha)
    elif continuar_jogando=="não":
        break


print("Questão 07: Marcar consulta com medico(a)\n")
medicos_escolhidos=utils.nome_medicos()
print(medicos_escolhidos)

