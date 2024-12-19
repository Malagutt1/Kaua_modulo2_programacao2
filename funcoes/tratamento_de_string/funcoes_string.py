import sys
sys.path.append(".")
sys.path.append("../custom_utils/utils")

from custom_utils import utils
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
#chamar a função
tamanho_da_string= utils.calcular_tamanho_da_string(letra_da_musica)
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

# Chama a função principal
utils.principal()

'''3. Crie uma função que itere sobre uma String, através de um laço de repetição,
passada como parâmetro e exiba o caracter e a posição que esse caracter aparece
na String. Por exemplo: Z - 8º caracter da String “string passada como parâmetro”'''
print("questão 3")


entradaUsuario= input("Digite a string: ")
utils.exibirCaracteresString(entradaUsuario)


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

frase_usuario = input("Digite a frase: ")
terminoFraseInseridoUsuario = input("Digite o termo de termino: ")
if utils.finalFrase(frase_usuario, terminoFraseInseridoUsuario):
    print(f"A frase {frase_usuario} termina com o termo {terminoFraseInseridoUsuario}")
else:
    print(f"A frase {frase_usuario} não termina com o termo {terminoFraseInseridoUsuario}")

'''5. Crie uma função que implemente a questão 1 da avaliação01 teórico-prática.'''
print("questão 5")
OPCAO_SINTAXE                  = 1
OPCAO_SEMANTICA                = 2
OPCAO_LACO_INFINITO            = 3
OPCAO_VARIAVEL                 = 4

CONCEITO_TEORICO_SINTAXE       = """\"Sintaxe é o conjunto de regras e estruturas que definem como o código deve ser escrito.\""""
CONCEITO_TEORICO_SEMANTICA     = """\"Semântica diz respeito ao significado das instruções\estruturas de uma linguagem de programação. Aquilo que faz sentido dentro da linguagem.\""""
CONCEITO_TEORICO_LACO_INFINITO = """\"Um laço infinito é uma condição de erro que pode ocorrer nas estruturas de repetição das linguagens de programação. 
Acontece quando o controle do laço nunca se torna falso, fazendo com que o laço de repetição execute infinitamente. Isso 
causa um consumo elevado dos recursos de máquina e o travamento do programa. A correta atualização do controle do laço, 
sua verificação a cada iteração e a garantia de que uma condição de parada será alcançada, são medidas para evitar que  
a condição de laço infinito aconteça.\""""
CONCEITO_TEORICO_VARIAVEL      = """\"Variável, em linguagem de programação, é um espaço de memória do computador usado para armazenar um valor, de
forma temporária, que pode ser alterado durante a execução do programa.\""""
opcaoDigitadaPeloUsuario       = ""
usuarioDigitouSair             = False

while not usuarioDigitouSair:
    opcaoDigitadaPeloUsuario = input("Informe a opção de menu desejada: ")    
    
    if utils.validarCodigoConceitoInformado(opcaoDigitadaPeloUsuario, opcaoDigitadaPeloUsuario):        
        print("\n" + utils.conceitosTeoricosLinguagensProgramacao(opcaoDigitadaPeloUsuario) + "\n") 
    else:
        
        if opcaoDigitadaPeloUsuario.upper() == "SAIR" :
            #Atualiza o controle do laço para finalizar o programa
            usuarioDigitouSair = True
                
        else:
            print(f"Opção inválida. A opção \"{opcaoDigitadaPeloUsuario}\" não existe no menu de opções.\n")
            
            #Exibe o menu de opções novamente
            utils.menuDeOpcoes()

'''6. Crie uma função que implemente a questão 4 da avaliação01 teórico-prática.'''
print("questão 6")
import re
    
 
senhaInformadaPeloUsuario = input('Digite uma senha para ser validada: ')
SEIS_CARACTERES=6
VINTE_CARACTERES=20
if not utils.validarTamanhoSenha(senhaInformadaPeloUsuario, SEIS_CARACTERES, VINTE_CARACTERES):
    print(f"A senha deve ter no mínimo {SEIS_CARACTERES} caracteres e no mximo {VINTE_CARACTERES}")

elif not utils.validarCaracteresMinusculos(senhaInformadaPeloUsuario):
    print('A senha deve ter ao menos uma letra minuscula') 

elif not utils.validarCaracteresNumericos(senhaInformadaPeloUsuario):
    print('A senha deve ter ao menos um numero') 

elif not utils.validarCaracteresMaiusculos(senhaInformadaPeloUsuario):
    print('A senha deve ter ao menos uma letra maiuscula') 

elif not utils.validarCaracteresEspeciais(senhaInformadaPeloUsuario, "[$#@!&]"):
    print('A senha deve ter ao menos um caractere especial do conjunto: $#@!&') 

elif utils.validarCaracteresWhiteSpace(senhaInformadaPeloUsuario):
    print("Caracteres do tipo \"whitespace\" não são permitidos: espaço em branco, "
            + "tabulações (\\t), quebra de linha (\\n), retorno do carro (\\r), etc…")
else:
    print('Senha validada com sucesso!')    

'''7. Crie uma função que receba uma String, toda em letras minúsculas, e retorne essa
mesma String passada como parâmetro com a primeira letra de cada palavra em
maiuscula. O desenvolvedor deve garantir que a String esteja em letras minúsculas.
Como forma de testes, o seu nome completo pode ser passado como parâmetro
dessa função.'''
print("questão 7")

nomeInicializado = input("Digite seu nome com letras minusculas: ")
nomeFormatado = utils.primeiraLetraMaiuscula(nomeInicializado)
print(nomeFormatado)

'''8. Crie uma função que receba uma String e um caracter imprimível. Essa função
deverá retornar a String passada por parâmetro com o caracter dentro da string, por
exemplo “Python” -> “P*y*t*h*o*n”.'''


# Teste da função
print("questão 8")
palavra=input("Insira uma palavra: ")
print(utils.inserir_caracter(palavra, "*"))
