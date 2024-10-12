"""LISTA DE EXERCÍCIOS – ESTRUTURAS DE REPETIÇÃO – WHILE
1) Crie e inicialize uma variável do tipo inteiro. Enquanto o valor dessa variável for
menor ou igual a um valor definido por você, exiba uma mensagem na tela e o
valor dessa variável. Explique em um comentário como o controle do laço vai
funcionar."""
print("1 questão:")
numero=1
while (numero<=10):
    print(f" {numero}º numero")
    numero+=1
    



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
    