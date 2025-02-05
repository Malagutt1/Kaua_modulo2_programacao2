import os                               # pacote Pandas
arquivo_eventos     = "eventos.txt"     # armazena informações sobre os eventos
arquivos_alunos     = "alunos.txt"      # armazena informações sobre os alunos
arquivo_inscricoes  = "inscricoes.txt"  # armazena informações sobre os alunos

SOMAR               = "SOMAR"
SUBTRAIR            = "SUBTRAIR"

menu = """\nMenu de Opções:
            1- Cadastrar evento
            2- Cadastrar aluno
            3- Inscrever aluno
            4- Listar eventos cadastrados
            5- Listar alunos cadastrados
            6- Resumo participação
            7 - Sair\n"""""

#Dicionários
evento    = {} #keys: titulo, capacidade, vagas_restantes
aluno     = {} #keys: nome, curso, instituição
inscricao = {} #keys: evento_nome, aluno_nome

#Listas de dicionários
eventos_cadastrados    = [] #manipula evento
alunos_cadastrados     = [] #manipula aluno
inscricoes_cadastradas = [] #manipula inscrição de alunos em eventos já cadastrados

def arquivo_existente(nome_arquivo):
    # o parametro "nome_arquivo" deve conter o caminho absoluto ou relativo do arquivo, seu nome e extensão
    try:
        if (os.path.exists(nome_arquivo)):
            return True
        else: 
            return False
    except Exception as error_arquivos:
        print(f"ERROR: {error_arquivos}")
        return False

def cadastrar_evento_arquivo():
    titulo          = input('\nDIGITE O NOME DO EVENTO: ').title().strip()
    capacidade      = input('DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip()
    try:
        diretorio_atual_pasta = "" + os.getcwd() + "/" + arquivo_eventos + ""
        if arquivo_existente(diretorio_atual_pasta):
            # se o arquivo existem abre no modo append, adicionar conteudo ao final do arquivo
            fEvento= open(arquivo_eventos, "a")
        else: 
            # o arquivo não exite e sera aberto no m odo WRITE, um arquivo em branco é criado
            fEvento= open(arquivo_eventos, "w")
            nome_colunas= "nome do evento, capacidadem vagas restantes\n"
            linha = [titulo, "," ,
                     capacidade, ",",
                     capacidade, "\n"]
            informacoes = "".join(linha)  # grava no arquivo .txt
            fEvento.write(f"{informacoes}")
            fEvento.close() # obrigatorio!!!  fecha o arquivo apos as operações finalizadas
            
    except Exception as error_arquivos:
        print(f"Error: {error_arquivos}")
        
def exibir_eventos_arquivos():
    try:
        fEvento = open(arquivo_eventos, "r")
        for arquivo_eventos in fEvento:
            registro_eventos = arquivo_eventos.split(",")
            fEvento.close()
        
    except Exception as error_arquivos:
        print ("")
        



def exibir_menu():
    print(menu)

def exibir_eventos_cadastrados():
    for evento in eventos_cadastrados:
        print(evento)
        
def exibir_alunos_cadastrados():
    for aluno in alunos_cadastrados:
        print(aluno)
        
def exibir_inscricoes_efetuadas():
    for inscricao in inscricoes_cadastradas:
        print(inscricao)        

#Fazer validação dos dados e tratamento de erro
def cadastrar_evento():
    titulo          = input('\nDIGITE O NOME DO EVENTO: ').title().strip()
    if not titulo in eventos_cadastrados:
        capacidade      = input('DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip()
        if capacidade.isnumeric():
            capacidade = int(capacidade)
            evento = {'titulo_evento': titulo,#Cria um evento novo que é armazenado em uma variável do tipo "dicionário"
                    'capacidade': capacidade,
                    'vagas_restantes': capacidade}  
        eventos_cadastrados.append(evento) #Armazena, na lista de dicionários, o evento novo criado
        
    elif titulo in eventos_cadastrados:
        print("Esse titulo já foi cadastrado anteriormente")   

    
#Fazer validação dos dados e tratamento de erro
def cadastrar_aluno():
    nome        = input('\nDIGITE O NOME DO ALUNO: ').strip()
    curso       = input('DIGITE O CURSO DO ALUNO: ').strip()
    instituicao = input('DIGITE A INSTITUIÇÃO EM QUE O ALUNO ESTUDA: ').strip()

    #Cria um aluno novo que é armazenado em uma variável do tipo "dicionário"
    aluno = {'nome_aluno': nome,
                 'curso' : curso,
            'instituicao': instituicao
            }      

    #Armazena, na lista de dicionários, o aluno novo criado
    alunos_cadastrados.append(aluno)    
    
#Fazer validação dos dados e tratamento de erro
def inscrever_aluno_curso():
    nomeEvento  = input('\nDIGITE O NOME DO EVENTO EM QUE O ALUNO QUER SE INSCREVER: ').strip()
    nomeAluno   = input('DIGITE O NOME DO ALUNO: ').strip()

    #Cria uma inscrição nova que é armazenada em uma variável do tipo "dicionário"
    inscricao = {'evento_nome': nomeEvento,
                 'aluno_nome' : nomeAluno
                }
    
    #Armazena, na lista de dicionários, a inscrição nova criada
    #PRECISA validar se o aluno informado já não está inscrito nesse curso
    #PRECISA validar se o curso existe e se o aluno existe
    inscricoes_cadastradas.append(inscricao)
    
    #Atualizar o número de vagas restantes no curso em que o aluno foi inscrito
    atualizar_vagas(nomeEvento, SUBTRAIR)


#Fazer validação dos dados e tratamento de erro
def atualizar_vagas(nomeEvento, tipoAtualizacao):
    msg = ''

    if len(eventos_cadastrados) > 0:
        for indice in range(len(eventos_cadastrados)):
            if eventos_cadastrados[indice].get('titulo_evento').upper() == nomeEvento.upper():
                if tipoAtualizacao == SOMAR:
                    atualizar = int(eventos_cadastrados[indice].get('vagas_restantes')) + 1
                else:
                    atualizar = int(eventos_cadastrados[indice].get('vagas_restantes')) - 1
                
                #validar o numero máximo de vagas definida na criação do evento novo
                if atualizar >= 0:
                    eventos_cadastrados[indice].update({'vagas_restantes': atualizar})
                    msg = 'O evento ' + eventos_cadastrados[indice].get('titulo_evento') + ' foi atualizado com sucesso!'
                else:
                    msg = 'Não há mais vagas disponíveis neste curso'
    else:
        msg = 'Não existem eventos cadastrados.'

    return msg

def executar_menu():
    while True:
        exibir_menu()
        
        #Fazer validação dos dados e tratamento de erro
        opcaoDigitada = input("DIGITE UMA OPÇÃO VÁLIDA DO MENU: ")
    
        if opcaoDigitada == "1":
            #cadastrar_evento()
            cadastrar_evento_arquivo()
        
        elif opcaoDigitada == "2":
            cadastrar_aluno()
        
        elif opcaoDigitada == "3":
            inscrever_aluno_curso()
        
        elif opcaoDigitada == "4":
            exibir_eventos_cadastrados()
        
        elif opcaoDigitada == "5":
            exibir_alunos_cadastrados()
        
        elif opcaoDigitada == "6":
            exibir_inscricoes_efetuadas()
        
        elif opcaoDigitada == "7":
            break
                
        else:
            print(f"{opcaoDigitada} - OPÇÃO INVÁLIDA DE MENU.")


executar_menu()
