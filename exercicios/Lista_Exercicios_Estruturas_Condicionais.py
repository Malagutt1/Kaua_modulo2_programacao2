"""
Obs: Toda entrada de dados via Stdin, deverá ser validada. Caso
não seja uma entrada válida, uma mensagem informativa deverá
ser exibida na tela e o programa finalizado.


1) Crie 2 variáveis com dois valores numéricos inteiros informados pelo
usuário, caso o valor do primeiro número for maior do que o segundo,
exiba em tela uma mensagem de acordo, caso contrário, exiba em tela
uma mensagem dizendo que o primeiro valor digitado é menor que o
segundo. Os números informados pelo usuário devem aparecer em
ambas as mensagens."""
print("1º exercicio")
valor1=int(input("Informe o primeiro número:\t"))
valor2=int(input("Informe o segundo número:\t"))
if valor1>valor2:
    print(f"O nuemero {valor1} é maior que o numero {valor2}")
elif valor1<valor2:
    print(f"O nuemero {valor2} é maior que o numero {valor1}")
else:
    print("Os numeros são iguais")
    



"""2) Crie um programa que possa marcar uma consulta médica. Como opções,
teremos disponíveis apenas 03 médicos, que devem ter seus nomes
exibidos na tela, p/ que possam ser escolhidos. Após a escolha do
profissional médico, exibir mensagem na tela informando que a consulta
foi marcada com o médico escolhido (nome do médico)."""
print("1º exercicio")
print("Olá, para marcar a consulta você deve primeiramente escolher um medico")
print("As opções de medico são: \nDr. Rafael Almeida (digite 1)\nDra. Clara Souza (digite 2)\nDr. Lucas Pereira (digite 3)")
escolha=int(input("Sua escolha é: \t"))
if escolha==1:
    print("Seu medico escolhido foi: Dr. Rafael Almeida")
elif escolha==2:
    print("Sua medica escolhida foi: Dra. Clara Souza")
elif escolha==3:
    print("Seu medico escolhido foi: Dr. Lucas Pereira")
else: print("Nenhum medico escolhido!")

"""3) Escreva um programa que verifica se uma determinada palavra consta
em um texto de origem. O texto não será conhecido pelo usuário que
usará de palavras aleatórias na tentativa de adivinhar que palavras
compõem a frase oculta. Frase: "Python é uma excelente linguagem de
programação!!! Se acertar, a mensagem: "A palavra (palavra digitada
pelo usuário) está na frase". Se errar, a mensagem: "A palavra (palavra
digitada pelo usuário) não está na frase". Use a função "find", referenciada
na documentação:
https://docs.python.org/3/library/stdtypes.html"""
 texto= "Python é uma excelente linguagem de programação!!!"


"""4) Crie um programa que leia um número e verifique se ele é par ou ímpar."""



"""5) Escreva um programa que receba dois números e verifique se ambos são
positivos."""


"""6) Crie um programa que leia dois números e exiba o maior entre eles. Caso
sejam iguais, exiba uma mensagem informando isso."""




"""7) Crie um programa que receba o peso e a altura de uma pessoa e calcule
seu Índice de Massa Corporal (IMC). imc = peso / (altura * altura) . O
programa deve exibir uma mensagem na tela de acordo com a seguinte
tabela:
 Abaixo de 18.5: Abaixo do peso
 Entre 18.5 e 24.9: Peso normal
 Entre 25 e 29.9: Sobrepeso
 Acima de 30: Obesidade sdg"""