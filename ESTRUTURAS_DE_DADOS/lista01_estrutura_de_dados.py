import sys
sys.path.append(".")
sys.path.append("../custom_utils/utils")

from custom_utils import utils
tupla_dia_da_semana= ("Domingo","Segunda", "terça", "Quarta", "Quinta", "Sexta", "Sabado\n")
tupla_meses= ("Janeiro", "Fevereiro", "Março", "Abril", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro\n") 
tupla_estacoes= ("verão", "outono", "inverno", "primavera\n")
lista_dia_da_semana= ["Domingo","Segunda", "terça", "Quarta", "Quinta", "Sexta", "Sabado\n"]
lista_meses= ["Janeiro", "Fevereiro", "Março", "Abril", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro\n"]
lista_estacoes= ["verão", "outono", "inverno", "primavera\n"]
Lista_do_supermercado=["arroz", "feijão", "macarrão", "açúcar", "sal", "óleo", "leite", "ovos", "frutas", "legumes", "carne", "pão", "queijo", "café", "biscoitos"]
linguagens_de_programacao= ("c", "c++", "javascript", "java", "lua", "python")

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
utils.lista_supermercado(Lista_do_supermercado)
print("Esclarecimento da escolha: Optei por usar uma LISTA porque, ao contrário de uma TUPLA, que é imutável, uma lista de supermercado pode ser removido ou adicionado itens a ela")

"""5. Crie um programa que atualize a lista de compras da questão 4. O programa 
deve solicitar ao usuário, através de um menu de opções, que tipo de
operação deseja efetuar sobre a lista de compras: incluir um novo item,
remover um item ou atualizar um item existente. Crie uma função para cada
tipo de operação permitida. Após o usuário informar uma das opções válida
do menu, o programa deve solicitar que o usuário digite o nome do
produto/item para que a função correta seja chamada e a alteração da lista
de compras possa ser feita. Implemente uma forma de encerrar o programa
através da interação do usuário."""  
# ERROR line 64: SyntaxWarning: sequência de escape '\i' inválida  || (o Python achou que \i era algo como \n) SITUAÇÃO: RESOLVIDO
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

          

print("Questão 6: Adivinha de linguagens de programação!")
while True:
    continuar_jogando= input("Continuar jogando?").lower()
    if continuar_jogando=="sim":
        return_adivinha= utils.adivinha(linguagens_de_programacao)
        print(return_adivinha)
    elif continuar_jogando=="não":
        break


print("Questão 07: Marcar consulta com medico(a)\n")
medicos_escolhidos=utils.nome_medicos()
print(medicos_escolhidos)

############################## CONTINUAÇÃO LISTA01, SÓ QUE COM DICIONARIO ##############################

"""8. Crie um dicionário, baseado nas informações usadas para criar a lista de compras da questão 4, 
de forma que seja possível definir o preço de cada produto. """
lista_de_compras={
    "arroz": 8.0,
    "feijão": 8.5,
    "macarrão": 5.0,
    "açúcar": 5.0,
    "sal": 7.0,
    "óleo": 12.0,
    "leite": 8.0,
    "ovos": 25.0,
    "frutas": 5.0,
    "legumes": 6.0,
    "carne": 50.0,
    "pão": 12.0,
    "queijo":9.0,
    "café": 8.9,
    "biscoitos":8.0}

"""9. Baseado no dicionário criado na questão 8, crie um programa que solicite ao usuário que 
informe o nome de um produto. Se o produto informado pelo usuário estiver na lista de compras do tipo 
dicionário, exiba a mensagem na tela: "O item {nome do produto} faz parte da lista de compras do supermercado".
 Senão, exiba a mensagem: "O item {nome do produto} NÃO faz parte da lista de compras do supermercado"."""
print("Questão 9: Encontrar produto na lista de compra")
Prod_digitado_pelo_usuario= input("Informe o nome do produto dentro de sua lista de compras:  ")
ITEM_DICIONARIO_COMPRAS= utils.item_esta_no_dicionario(lista_de_compras, Prod_digitado_pelo_usuario)
print(ITEM_DICIONARIO_COMPRAS)

"""10. Crie um dicionário que armazene um cadastro para uma loja. Esse cadastro deve conter informações como: 
nome, idade, sexo, estado civil, nacionalidade, faixa de renda, etc... Exiba na tela tais informações."""
print("Questão 10: Cadastro da loja")
cadastro_loja={
    "NOME":  "Kauã",
    "IDADE": 16,
    "SEXO": "Masculino",
    "ESTADO_CIVIL": "Abandonado",
    "NACIONALIDADE": "Brasileiro",
    "FAIXA_DE_RENDA": "1 milhão"  #As vezes temos que ser verdadeiros kk
}
for cadastro, dados_cadastrado in cadastro_loja.items():
    print(f"\n{cadastro}= {dados_cadastrado} ")

"""11. Crie um programa que receba dados de um aluno como: nome e notas. Cadastre 03 trimestres de informações. 
Retorne uma nova estrutura de dados que armazene o nome e a média do aluno. 
Imprima, na tela, as informações dessa nova estrutura de dados."""
estudante={
    "nome": "Fulano",
    "Notas": [8, 7.5, 9] # media final de 3 trimestres
}
media_notas= sum(estudante["Notas"]) / len(estudante["Notas"])
print(f" O aluno {estudante['nome']} tem a media final de:{media_notas:.2f}")