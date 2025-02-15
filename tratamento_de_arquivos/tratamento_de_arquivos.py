#Kauã
import os
from time import sleep              #importação da função sleep da biblioteca time

#arquivo evento.txt     - armazenar informções sobre os eventos
#arquivo aluno.txt      - armazenar informções sobre os alunos
#arquivo inscrições.txt - armazenar informções sobre os alunos matriculados
arquivo_eventos     = "Kaua_modulo2_programacao2/tratamento_de_arquivos/evento.txt"
arquivo_aluno       = "Kaua_modulo2_programacao2/tratamento_de_arquivos/aluno.txt"
arquivo_matriculados = "Kaua_modulo2_programacao2/tratamento_de_arquivos/inscrições.txt"

somar    = "SOMAR"
subtrair = "SUBTRAIR"

menu = '''\nMenu de Opções:
            1- Cadastrar evento
            2- Excluir evento
            3- Cadastrar aluno
            4- excluir aluno
            5- Matricular aluno
            6- Desmatricular aluno
            7- Ver eventos cadastrados
            8- Ver alunos cadastrados
            9- Ver alunos matriculados
            10- Resumo SNCT
            
            Sair - digite SAIR\n'''

evento    = {} #keys: titulo, capacidade, vagas_restantes
aluno     = {} #keys: nome, curso, instituição
matricula = {} #keys: evento_nome, evento_aluno

eventos_cadastrados = [] #manipula evento
alunos_cadastrados  = [] #manipula aluno
alunos_matriculados = [] #manipula inscrição de alunos em eventos já pré cadastrados

def arquivoExiste(nomeArquivo):
    try:
        #O parâmetro "nomeArquivo" deverá conter o caminho "absoluto ou relativo"
        #do arquivo, seu nome e sua extensão
        if(os.path.exists(nomeArquivo)):
            return True
        else:
            return False
    except Exception as erroArquivo:
        print(f"Erro: {erroArquivo}")
        return False

def cadastrar_evento_arquivo():
    titulo      = input("\nDIGITE O NOME DO EVENTO: ").strip()
    capacidade  = input("DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ").strip()
    
    try:
        #Pega o diretório atual e concatena o nome do arquivo a ser criado\aberto
        #se houver espaços em branco no caminho absoluto, este deve ser passado 
        #como string (entre aspas)
        diretorioAtualPasta = "" + os.getcwd() + "/" + arquivo_eventos + ""
        
        if arquivoExiste(diretorioAtualPasta):
            #se o arquivo EXISTE, abre no modo APPEND, ou seja, um arquivo em branco, sem conteúdo
            #ao final do arquivo.
            fEvento = open(arquivo_eventos, 'a')
        else:
            #O arquivp NÃO EXISTE, e será aberto no modo WRITE, ou seja, um arquivo
            #em branco, sem conteúdo.
            fEvento = open(arquivo_eventos, 'w')
            #escreve na primeira linha o nome das colunas que identifica as informações
            nomeColunas = 'Nome do Evento | Capacidade | Vagas restantes\n'
            fEvento.write(nomeColunas)
        
            
        #o conteúdo do arquivo será gravado como uma string
        linha = [titulo
        , "|"
        , capacidade
        , "|"
        , capacidade #parametro que representa as vagas restantes
        ,"|\n"]
        #grava as informações do evento no arquivo.txt
        informacoes = "".join(linha)    
        #Evento.write(repr(informacoes))
        fEvento.write((f'{informacoes}'))
        
        #OBRIGATORIAMENTE, depois de finalizados as operações de gravação, o
        #arquivo deve ser FECHADO
        fEvento.close()
              
    except Exception as erroArquivo:
        print(f"Erro: {erroArquivo}")
    
def exibir_evento_arquivo():
    
    try:
        fEvento = open(arquivo_eventos, "r")
        
        for eventoArquivo in fEvento:
            registroEvento = eventoArquivo.split(",")
            print(registroEvento)
        fEvento.close()
    except Exception as erro:
        print(f"Erro: {erro}")

def excluir_evento_arquivo(nomeDoEvento):
    registroArquivo = []
    
    try:
        diretorioAtualPasta = "" + os.getcwd() + "/" + arquivo_eventos + ""
        
        if arquivoExiste(diretorioAtualPasta):
            #O Arquivo obrigatoriamente deverá ser aberto no modo LEITURA
            with open(diretorioAtualPasta, "r") as arquivoDeEvento:
                registroArquivo = arquivoDeEvento.readlines()
                   
            if (len(registroArquivo) > 0):
                for indiceLinha in range(len(registroArquivo)):
                    linha = registroArquivo[indiceLinha]
                    
                    if linha.find(nomeDoEvento) >= 0:
                        #Encontrou o evento e excluiu da lista
                        registroArquivo.pop(indiceLinha)
                        
            #trunca o arquivo e copia a lista pra dentro dele      
            if (len(registroArquivo) > 0):
                with open(diretorioAtualPasta, "w") as arquivoDeEventosAlterado:
                    arquivoDeEventosAlterado.writelines(registroArquivo)
            
            return "Evento exclu[ido com sucesso"    
        else:
            print("Erro! Não há arquivos.")
        
    except Exception as erroArquivo:
        print(f'Erro na manipulação do Arquivo {erroArquivo}')
    
def exibir_aluno_arquivo():
    try:
        fALuno = open(arquivo_aluno, "r")
        
        for eventoArquivo in fALuno:
            registroEvento = eventoArquivo.split(",")
            print(registroEvento)
        fALuno.close()
    except Exception as erro:
        print(f"Erro: {erro}")     

def cadastrar_aluno_arquivo():
    aluno  = input("\nDIGITE O NOME DO ALUNO: ").strip()
    modulo = input("\nDIGITE SEU MÓDULO: ").strip()
    curso  = input('\nDIGITE SEU CURSO: ').strip()
    
    try:
        #Pega o diretório atual e concatena o nome do arquivo a ser criado\aberto
        #se houver espaços em branco no caminho absoluto, este deve ser passado 
        #como string (entre aspas)
        diretorioAtualPasta = "" + os.getcwd() + "/" + arquivo_aluno + ""
        
        if arquivoExiste(diretorioAtualPasta):
            #se o arquivo EXISTE, abre no modo APPEND, ou seja, um arquivo em branco, sem conteúdo
            #ao final do arquivo.
            fAluno = open(arquivo_aluno, 'a')
        else:
            #O arquivo NÃO EXISTE, e será aberto no modo WRITE, ou seja, um arquivo
            #em branco, sem conteúdo.
            fAluno = open(arquivo_aluno, 'w')
            #escreve na primeira linha o nome das colunas que identifica as informações
            nomeColunas = 'Nome do Aluno | Modulo | Curso\n'
            fAluno.write(nomeColunas)
            
        #o conteúdo do arquivo será gravado como uma string
        linha = [aluno
        , "|"
        , modulo
        , "|"
        , curso
        ,"\n"]
        #grava as informações do evento no arquivo.txt
        informacoes = "".join(linha)
        #Evento.write(repr(informacoes))
        fAluno.write((f'{informacoes}'))
        
        #OBRIGATORIAMENTE, depois de finalizados as operações de gravação, o
        #arquivo deve ser FECHADO
        fAluno.close()
              
    except Exception as erroArquivo:
        print(f"Erro: {erroArquivo}")

def excluir_aluno_arquivo(nomeAluno):
    registroArquivo = []
    
    try:
        diretorioAtualPasta = "" + os.getcwd() + "/" + arquivo_aluno + ""
        
        if arquivoExiste(diretorioAtualPasta):
            #O Arquivo obrigatoriamente deverá ser aberto no modo LEITURA
            with open(diretorioAtualPasta, "r") as arquivoDeAluno:
                registroArquivo = arquivoDeAluno.readlines()
                   
            if (len(registroArquivo) > 0):
                for indiceLinha in range(len(registroArquivo)):
                    linha = registroArquivo[indiceLinha]
                    
                    if linha.find(nomeAluno) >= 0:
                        #Encontrou o aluno e excluiu da lista
                        registroArquivo.pop(indiceLinha)
                        
            #trunca o arquivo e copia a lista pra dentro dele      
            if (len(registroArquivo) > 0):
                with open(diretorioAtualPasta, "w") as arquivoDeAlunosAlterado:
                    arquivoDeAlunosAlterado.writelines(registroArquivo)
            
            return "Aluno excluido com sucesso"    
        else:
            print("Erro! Não há arquivos.")
        
    except Exception as erroArquivo:
        print(f'Erro na manipulação do Arquivo {erroArquivo}')
        
def codigo_principal(): #ok
    escolhaDoMenu = ''
    while escolhaDoMenu != 'sair':
        print(exibir_menu(menu))
        escolhaDoMenu = str(input('Digite sua escolha: ')).strip().lower()
        if escolhaDoMenu == 'sair':
            break
        else:
            print(escolha_do_menu(escolhaDoMenu))
    print('Saiu. Obrigado!')
    resumo()    

def exibir_matriculado_arquivo():
    try:
        fMatriculado = open(arquivo_aluno, "r")
        
        for eventoArquivo in fMatriculado:
            registroEvento = eventoArquivo.split(",")
            print(registroEvento)
        fMatriculado.close()
    except Exception as erro:
        print(f"Erro: {erro}") 

def matricular_aluno_arquivo():
    exibir_aluno_arquivo()
    aluno  = input("\ESCOLHA O NOME DO ALUNO: ").strip()
    exibir_evento_arquivo()
    evento = input("\nESCOLHA O EVENTO: ")
    
    
    try:
        #Pega o diretório atual e concatena o nome do arquivo a ser criado\aberto
        #se houver espaços em branco no caminho absoluto, este deve ser passado 
        #como string (entre aspas)
        diretorioAtualPasta = "" + os.getcwd() + "/" + arquivo_matriculados + ""
        
        if arquivoExiste(diretorioAtualPasta):
            #se o arquivo EXISTE, abre no modo APPEND, ou seja, um arquivo em branco, sem conteúdo
            #ao final do arquivo.
            fMatriculado = open(arquivo_matriculados, 'a')
        else:
            #O arquivo NÃO EXISTE, e será aberto no modo WRITE, ou seja, um arquivo
            #em branco, sem conteúdo.
            fMatriculado = open(arquivo_matriculados, 'w')
            #escreve na primeira linha o nome das colunas que identifica as informações
            nomeColunas = 'Nome do Aluno | Evento\n'
            fMatriculado.write(nomeColunas)
            
        #o conteúdo do arquivo será gravado como uma string
        linha = [aluno
        , "|"
        , evento
        , "|"
        ,"\n"]
        #grava as informações do evento no arquivo.txt
        informacoes = "".join(linha)
        #Evento.write(repr(informacoes))
        fMatriculado.write((f'{informacoes}'))
        manipular_vaga_arquivo(evento, -1)
        #OBRIGATORIAMENTE, depois de finalizados as operações de gravação, o
        #arquivo deve ser FECHADO
        fMatriculado.close()
              
    except Exception as erroArquivo:
        print(f"Erro: {erroArquivo}")

def desmatricular_aluno_arquivo(nomeInscrito):
    registroArquivo = []
    
    try:
        diretorioAtualPasta = "" + os.getcwd() + "/" + arquivo_matriculados + ""
        
        if arquivoExiste(diretorioAtualPasta):
            #O Arquivo obrigatoriamente deverá ser aberto no modo LEITURA
            with open(diretorioAtualPasta, "r") as registroDeMatriculado:
                registroArquivo = registroDeMatriculado.readlines()
                   
            if (len(registroArquivo) > 0):
                for indiceLinha in range(len(registroArquivo)):
                    linha = registroArquivo[indiceLinha]
                    infoMatricula = linha.split("|")
                    evento = infoMatricula[1]
                    
                    if linha.find(nomeInscrito) >= 0:
                        #Encontrou o aluno e excluiu da lista
                        registroArquivo.pop(indiceLinha)
                        
            #trunca o arquivo e copia a lista pra dentro dele      
            if (len(registroArquivo) > 0):
                with open(diretorioAtualPasta, "w") as arquivoDeMatriculadoAlterado:
                    arquivoDeMatriculadoAlterado.writelines(registroArquivo)
            
            manipular_vaga_arquivo(evento, 1)
            return "Aluno desmatriculado com sucesso"    
        else:
            print("Erro! Não há arquivos.")
        
    except Exception as erroArquivo:
        print(f'Erro na manipulação do Arquivo {erroArquivo}')
        
def manipular_vaga_arquivo(evento, quantidade):
    registroArquivo = []
    
    try:
        diretorioAtualPasta = "" + os.getcwd() + "/" + arquivo_eventos + ""
        
        if arquivoExiste(diretorioAtualPasta):
            #O Arquivo obrigatoriamente deverá ser aberto no modo LEITURA
            with open(diretorioAtualPasta, "r") as arquivoDeEvento:
                registroArquivo = arquivoDeEvento.readlines()
                   
            if (len(registroArquivo) > 0):
                for indiceLinha in range(len(registroArquivo)):
                    linha = registroArquivo[indiceLinha]
                    
                    if linha.find(evento) >= 0:
                        #Encontrou o evento e excluiu da lista
                        infoEvento = linha.split("|")
                        
                        titulo = infoEvento[0]
                        capacidade = int(infoEvento[1])
                        limite = int(infoEvento[2])
                        
                        if quantidade > 0:
                            if limite == capacidade:
                                print("Não há vagas há remover")
                            else:
                                limite += quantidade
                        elif quantidade < 0:
                            if limite <= 0:
                                print("Não há mais vagas disponiveis")
                            else:
                                limite += quantidade
                            
                        linhaEvento = [titulo
                        , "|"
                        , str(capacidade)
                        , "|"
                        , str(limite) #parametro que representa as vagas restantes
                        ,"|\n"]
                        #grava as informações do evento no arquivo.txt
                        informacoes = "".join(linhaEvento)    
                        
                        registroArquivo[indiceLinha] = informacoes
                        break
                        
            #trunca o arquivo e copia a lista pra dentro dele      
            if (len(registroArquivo) > 0):
                with open(diretorioAtualPasta, "w") as arquivoDeEventosAlterado:
                    arquivoDeEventosAlterado.writelines(registroArquivo)
            
            return "Evento exclu[ido com sucesso"    
        else:
            print("Erro! Não há arquivos.")
        
    except Exception as erroArquivo:
        print(f'Erro na manipulação do Arquivo {erroArquivo}')
        
    
def exibir_menu(menuDeOpcoes): #ok
    return menuDeOpcoes

def escolha_do_menu(escolha): #ok
    if escolha == '1':
        return cadastrar_evento_arquivo()
    
    elif escolha == '2':
        exibir_evento_arquivo()
        nomeEvento = input("\nDIGITE O NOME DO EVENTO QUE VOCÊ DESEJA EXCLUIR: ")
        return excluir_evento_arquivo(nomeEvento)
    
    elif escolha == '3':
        return cadastrar_aluno_arquivo()
    
    elif escolha == '4':
        exibir_aluno_arquivo()
        nomeDoAluno = input("\nDIGITE O NOME DO ALUNO QUE VOCÊ DESEJA EXCLUIR: ")
        return excluir_aluno_arquivo(nomeDoAluno)
    
    elif escolha == '5':
        return matricular_aluno_arquivo()
    
    elif escolha == '6':
        exibir_matriculado_arquivo
        nomeMatriculado = input('\nDIGITE O NOME DO ALUNO QUE DESEJA DESMATRICULAR: ')
        return desmatricular_aluno_arquivo(nomeMatriculado)     
    
    elif escolha == '7':
        return exibir_evento_arquivo()
    
    elif escolha == '8':
        return exibir_aluno_arquivo()
    
    elif escolha == '9':
        return exibir_matriculado_arquivo(alunos_matriculados)
    
    elif escolha == '10':
        return resumo(alunos_cadastrados, eventos_cadastrados, alunos_matriculados)
    
    else:
        return 'ENTRADA INVÁLIDA.'

def resumo(): #ok
    print('\n\nLISTA DE ALUNOS CADASTRADOS:\n')
    exibir_aluno_arquivo()
    print('\nLISTA DE EVENTOS CADASTRADOS:\n')
    exibir_evento_arquivo()
    print('\nLISTA DE MATRICULADOS:\n')
    exibir_matriculado_arquivo()    

codigo_principal()