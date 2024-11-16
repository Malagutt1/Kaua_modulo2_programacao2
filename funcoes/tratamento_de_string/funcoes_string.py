'''Obs.: Um programa deve ser criado p/ que todas as funções desenvolvidas possam ser usadas.'''

'''1. Crie uma função que calcule o tamanho de uma String. Tal função deverá ter um
parâmetro de entrada, do tipo String. O retorno da função deverá ser do tipo Inteiro.
No primeiro teste da função o valor do parâmetro de entrada deverá ser a letra de
uma música de sua preferência. O programa que usará a função deverá exibir a
mensagem “A letra da música (nome da música) tem (número de caracteres)
caracteres. O desenvolvedor deverá validar o tipo do parâmetro de entrada, caso
não seja válido, retornar o valor -1. Nesse caso o programa que usará a função
deverá exibir mensagem de erro informando que a entrada de dados é inválida.”'''
print("questão 1")
nome_da_musica=('Que Bonita a Sua Roupa (Chaves)')
letra_da_musica=('Que bonita a sua roupa, que roupinha muito louca, nela é tudo remendado, não vale nenhum centavo, mas agrada a quem olhar! Eu sou o famoso Chaves, todos dizem que minha roupa é remendada, que faço tremer as bases com minhas peraltices preparadas; dizem a todo instante que ele é mais espaçoso que um trem, que ela é azul... crinante, e que tão chata como ela não há ninguém; o Professor visita a vila procurando casamento, e o Seu Madruga não evita levar um tabefe a todo momento; a Popis é muito boba, pra Dona Clotilde só falta uma escova, o Nhonho não se manca, do Seu Barriga leva sempre uma bronca!')
def calcular_tamanho_da_string(letra_da_musica):  #função principal
    if (type(letra_da_musica)==str):
        return len(letra_da_musica)
    else:
        return -1
#chamar a função
tamanho_da_string=calcular_tamanho_da_string(letra_da_musica)
if tamanho_da_string<0:
    print("Entrada de dados invalida!")
else:
    print(f"A letra da música '{nome_da_musica}' tem {tamanho_da_string} caracteres.")


'''2. Crie uma função que retorne um caracter de uma String em uma posição específica.
Para tanto, dois argumentos de entrada deverão ser fornecidos: a string e a posição
que se deseja ter um carácter retornado. O controle sobre a posição (índice)
passada por parâmetro é de responsabilidade do desenvolvedor. Caso uma posição
inválida (IndexError: string index out of range) seja fornecida pelo usuário, a função
deverá retornar “-1”. Nesse caso, o programa que usa a função deverá exibir a
mensagem “Índice fora do intervalo". A String não possui o índice {índice passado
como parâmetro}”. Execute os testes na função tal que o primeiro caracter possa ser
retornado, o último, um do meio da String, etc…'''
print("questão 2") 

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

# Chama a função principal
principal()

'''3. Crie uma função que itere sobre uma String, através de um laço de repetição,
passada como parâmetro e exiba o caracter e a posição que esse caracter aparece
na String. Por exemplo: Z - 8º caracter da String “string passada como parâmetro”'''
print("questão 3")
def exibirCaracteresString(stringCaracteres):
    for contador in range(len(stringCaracteres)):
        print(f"{stringCaracteres[contador]} - {contador + 1}º caracter da String \"{stringCaracteres}\"")

entradaUsuario= input("Digite a string: ")
exibirCaracteresString(entradaUsuario)


'''4. Crie uma função que retorne verdadeiro ou falso quando avalia se uma frase termina
com determinada palavra ou letra. A frase deverá ser passada através de uma
variável, criada e inicializada previamente, enquanto que a palavra ou letra deve ser
passada entre aspas duplas. O programa que usar essa função deverá exibir a
mensagem [A frase passada por parâmetro] termina com [palavra ou letra passada
por parâmetro] quando a função retornar VERDADEIRO. Caso contrário, exibir a
mensagem: [A frase passada por parâmetro] NÃO termina com [palavra ou letra
passada por parâmetro]. Para efeito de testes, inicialize a variável criada com uma
das estrofes do hino nacional brasileiro.'''
print("questão 4")
def finalFrase(frase, terminoFrase):
    return frase.endswith(terminoFrase)
frase_usuario = input("Digite a frase: ")
terminoFraseInseridoUsuario = input("Digite o termo de termino: ")
if finalFrase(frase_usuario, terminoFraseInseridoUsuario):
    print(f"A frase {frase_usuario} termina com o termo {terminoFraseInseridoUsuario}")
else:
    print(f"A frase {frase_usuario} não termina com o termo {terminoFraseInseridoUsuario}")

'''5. Crie uma função que implemente a questão 1 da avaliação01 teórico-prática.'''
print("questão 5")

'''6. Crie uma função que implemente a questão 4 da avaliação01 teórico-prática.'''
print("questão 6")

'''7. Crie uma função que receba uma String, toda em letras minúsculas, e retorne essa
mesma String passada como parâmetro com a primeira letra de cada palavra em
maiuscula. O desenvolvedor deve garantir que a String esteja em letras minúsculas.
Como forma de testes, o seu nome completo pode ser passado como parâmetro
dessa função.'''
print("questão 7")
def primeiraLetraMaiuscula(nomeMinusculo):
    nomeMinusculo = nomeMinusculo.lower()
    return nomeMinusculo.title()
nomeInicializado = input("Digite seu nome com letras minusculas: ")
nomeFormatado = primeiraLetraMaiuscula(nomeInicializado)
print(nomeFormatado)

'''8. Crie uma função que receba uma String e um caracter imprimível. Essa função
deverá retornar a String passada por parâmetro com o caracter dentro da string, por
exemplo “Python” -> “P*y*t*h*o*n”.'''
print("questão 8")
def inserir_caracter(string, caracter):
    return caracter.join(string)
# Teste da função
print("questão 8")
palavra=input("Insira uma palavra: ")
print(inserir_caracter(palavra, "*"))