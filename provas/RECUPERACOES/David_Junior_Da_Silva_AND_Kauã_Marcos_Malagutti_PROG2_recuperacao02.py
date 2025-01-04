from colorama import init, Fore  # Importa a biblioteca Colorama para estilizar texto no terminal.
init()  # Inicializa a biblioteca Colorama para uso.

# Declaração de listas e dicionários que armazenarão informações dos eventos e alunos.
lista_dos_eventos = []  # Lista para armazenar os nomes dos eventos.
quantidade_de_pessoas = []  # Lista para armazenar o número máximo de vagas de cada evento.
alunos_por_evento = {}  # Dicionário que relaciona eventos aos alunos inscritos.
alunos_por_evento["aluno"]=[] # Inicia a lista de alunos como vazia

# Função para cadastrar um evento com título e número máximo de participantes.
def cadastrar_eventos(titulo_do_evento, quantidade_maxima_de_pessoas):
    lista_dos_eventos.append(titulo_do_evento)  # Adiciona o nome do evento à lista de eventos.
    quantidade_de_pessoas.append(quantidade_maxima_de_pessoas)  # Adiciona o número de vagas à lista de vagas.
    alunos_por_evento[titulo_do_evento] = []  # Inicializa a lista de alunos do evento como vazia.
    print(Fore.GREEN + f"O evento '{titulo_do_evento}' foi adicionado!" + Fore.RESET)  # Mensagem de confirmação.
    print(Fore.GREEN + f"Seu evento tem a quantidade máxima de {quantidade_maxima_de_pessoas} pessoas." + Fore.RESET)  # Confirma o número máximo de vagas.

def remover_eventos(titulo_do_evento):
    lista_dos_eventos.remove(titulo_do_evento) # remove o evento da lista de eventos
    alunos_por_evento.pop(titulo_do_evento, None)  # Remove os alunos relacionados ao evento
    print(Fore.GREEN + f" O evento {titulo_do_evento} foi removido com sucesso"+ Fore.RESET)
 
# Função para cadastrar um aluno pelo nome.
def cadastrar_alunos(nome_aluno):
    alunos_por_evento["aluno"].append(nome_aluno)# Adiciona o nome do aluno à lista de alunos.
    print(Fore.GREEN + f"O(a) aluno(a) {nome_aluno} foi registrado no sistema!" + Fore.RESET)  # Mensagem de confirmação.
    return nome_aluno  # Retorna o nome do aluno.

def excluir_alunos(nome_aluno): 
    aluno_removido = False
    for evento, alunos in alunos_por_evento.items():
        if evento != "aluno" and nome_aluno in alunos:  # Ignora a chave 'aluno' e verifica se o aluno está inscrito no evento.
            alunos_por_evento[evento].remove(nome_aluno)  # Remove o aluno da lista de inscritos no evento.
            indice_evento = lista_dos_eventos.index(evento)  # Obtém o índice do evento na lista.
            quantidade_de_pessoas[indice_evento] += 1  # Incrementa o número de vagas disponíveis.
            aluno_removido = True  # Marca que o aluno foi removido.

    # Verifica se o aluno está na lista geral de alunos (fora dos eventos)
    if nome_aluno in alunos_por_evento["aluno"]:
        alunos_por_evento["aluno"].remove(nome_aluno)  # Remove o aluno da lista geral.
        aluno_removido = True  # Marca que o aluno foi removido da lista geral.
    
    if aluno_removido:
        print(Fore.GREEN + f"O(a) aluno(a) {nome_aluno} foi removido(a) de todos os eventos e da lista geral!" + Fore.RESET)
    else:
        print(Fore.RED + f"O(a) aluno(a) {nome_aluno} não foi encontrado(a) nos eventos nem na lista geral de alunos." + Fore.RESET)

    return aluno_removido  # Retorna se o aluno foi removido ou não.

# Função para exibir todos os eventos e suas vagas disponíveis.
def exibir_eventos():
    print(Fore.LIGHTYELLOW_EX + "Eventos disponíveis:" + Fore.RESET)  # Cabeçalho da lista de eventos.
    for evento, vagas in zip(lista_dos_eventos, quantidade_de_pessoas):  # Itera pelos eventos e suas respectivas vagas.
        print(f"- {evento}: {vagas} vaga(s) disponível(is)")  # Exibe o nome do evento e o número de vagas.

# Função para inscrever um aluno em um evento.
def fazer_inscricao(aluno, evento):
    if evento not in lista_dos_eventos:  # Verifica se o evento existe.
        print(Fore.RED + "Evento não encontrado." + Fore.RESET)  # Mensagem de erro se o evento não for encontrado.
        return

    indice_evento = lista_dos_eventos.index(evento)  # Obtém o índice do evento na lista.

    if quantidade_de_pessoas[indice_evento] <= 0:  # Verifica se ainda há vagas no evento.
        print(Fore.RED + "O número de participantes nesse evento foi excedido." + Fore.RESET)  # Erro se não houver vagas.
        return

    alunos_por_evento[evento].append(aluno)  # Adiciona o aluno à lista de alunos do evento.
    quantidade_de_pessoas[indice_evento] -= 1  # Reduz o número de vagas disponíveis.
    print(Fore.GREEN + f"O(a) aluno(a) {aluno} foi inscrito(a) no evento '{evento}'." + Fore.RESET)  # Confirmação da inscrição.

# Função para exibir os alunos inscritos em cada evento.
def exibir_alunos_no_evento():
    print(Fore.LIGHTYELLOW_EX + "Alunos por evento:" + Fore.RESET) 
    # Exibe os alunos inscritos por evento
    for evento in lista_dos_eventos:
        alunos = alunos_por_evento.get(evento, [])
        print(f"- {evento}: {', '.join(alunos) if alunos else 'Nenhum aluno inscrito.'}")
        
def exibir_alunos_cadastrados():
    print(Fore.LIGHTYELLOW_EX + "Lista de Alunos Cadastrados:" + Fore.RESET)  # Cabeçalho da lista.
    if alunos_por_evento["aluno"]:  # Verifica se há alunos cadastrados.
        for nome in alunos_por_evento["aluno"]:
            print(f"- {nome}")  # Exibe o nome de cada aluno.
    else:
        print(Fore.RED + "Nenhum aluno cadastrado no sistema." + Fore.RESET)

# Função principal para exibir o menu de opções e executar ações escolhidas pelo usuário.
def menu_opcoes():
    while True:  # Loop principal para manter o menu ativo.
        Menu_opcoes_escolher = input("\nDigite um número para as seguintes funções:\n"
                                    "1 = Cadastrar novo evento\n"
                                    "2 = Remover evento\n"
                                    "3 = Cadastrar aluno\n"
                                    "4 = Remover aluno\n"
                                    "5 = Exibir eventos na tela\n"
                                    "6 = Fazer inscrição do aluno em um evento\n"
                                    "7 = Exibir alunos no evento\n"
                                    "8 = Exibir todos os alunos cadastrados\n"
                                    "Digite 'sair' para sair do menu\n"
                                    "Escolha a opção desejada: ").strip().lower()  # Solicita a escolha do usuário.

        if Menu_opcoes_escolher == "1":  # Opção para cadastrar um novo evento.
            titulo_do_evento = input("Insira o nome para o novo evento: ").strip()  # Solicita o nome do evento.
            if titulo_do_evento in lista_dos_eventos:  # Verifica se o evento já existe.
                print(Fore.RED + f"Erro: O evento '{titulo_do_evento}' já foi cadastrado!" + Fore.RESET)  # Mensagem de erro.
            else:
                while True:  # Valida o número máximo de pessoas.
                    quantidade_maxima_de_pessoas = input("Insira a quantidade máxima de pessoas para seu novo evento: ").strip()
                    if not quantidade_maxima_de_pessoas.isnumeric():  # Verifica se o valor é numérico.
                        print(Fore.RED + "Favor inserir um número válido!" + Fore.RESET)  # Mensagem de erro para entrada inválida.
                    else:
                        quantidade_maxima_de_pessoas = int(quantidade_maxima_de_pessoas)  # Converte para inteiro.
                        cadastrar_eventos(titulo_do_evento, quantidade_maxima_de_pessoas)  # Chama a função para cadastrar o evento.
                        break
        elif Menu_opcoes_escolher == "2":
            titulo_do_evento = input("Insira o nome do evento para ser removido: ").strip()  # Solicita o nome do evento.
            if titulo_do_evento in lista_dos_eventos :
                remover_eventos(titulo_do_evento)
            else: print(Fore.RED + "Evento não encontrado no sistema!" + Fore.RESET)

        elif Menu_opcoes_escolher == "3":  # Opção para cadastrar um aluno.
            nome_aluno = input("Insira o nome do estudante: ").strip()  # Solicita o nome do aluno.
            if nome_aluno in alunos_por_evento["aluno"]:
                print(Fore.RED + f"O aluno '{nome_aluno}' já está cadastrado!" + Fore.RESET)
            else: cadastrar_alunos(nome_aluno)  # Chama a função para registrar o aluno.
            
        elif Menu_opcoes_escolher == "4":
            nome_aluno = input("Insira o nome do estudante a ser removido: ").strip()  # Solicita o nome do aluno.
            if nome_aluno in alunos_por_evento["aluno"]:
                excluir_alunos(nome_aluno)  # Chama a função para excluir o aluno.
            else:
                print(Fore.RED + "Aluno não encontrado no sistema!" + Fore.RESET)

        elif Menu_opcoes_escolher == "5":  # Opção para exibir os eventos disponíveis.
            exibir_eventos()  # Chama a função para exibir os eventos.

        elif Menu_opcoes_escolher == "6":  # Opção para inscrever um aluno em um evento.
            nome_aluno = input("Insira o nome do aluno para inscrição: ").strip()  # Solicita o nome do aluno.
            if nome_aluno in alunos_por_evento["aluno"]:  # Verifica se o aluno foi registrado previamente.
                evento = input("Insira o nome do evento: ").strip()  # Solicita o nome do evento.
                fazer_inscricao(nome_aluno, evento)  # Chama a função para fazer a inscrição.
            else:
                print(Fore.RED + "O aluno deve ser cadastrado antes de se inscrever em um evento." + Fore.RESET)  # Mensagem de erro para aluno não registrado.
            
        elif Menu_opcoes_escolher == "7":  # Opção para exibir os alunos inscritos em eventos.
            if not lista_dos_eventos:  # Verifica se há eventos cadastrados antes de tentar mostrar os alunos.
                print(Fore.RED + "Nenhum evento cadastrado. Retornando ao menu..." + Fore.RESET)  # Mensagem caso não haja eventos.
                continue
            else:  exibir_alunos_no_evento()  # Chama a função para exibir alunos por evento.

        elif Menu_opcoes_escolher == "8":  # Nova opção para exibir alunos cadastrados.
            exibir_alunos_cadastrados()  # Chama a função para exibir os alunos.

        elif Menu_opcoes_escolher == "sair":  # Opção para sair do menu.
            deseja_sair = input("Tem certeza que deseja sair? Digite 'sair' novamente para confirmar: ").strip().lower()  # Confirmação adicional para sair.
            if deseja_sair == 'sair':
                break  # Encerra o loop principal.

        else:  # Caso o usuário insira uma opção inválida.
            print(Fore.RED + "Por favor, selecione uma opção válida!" + Fore.RESET)  # Mensagem de erro.

menu_opcoes()  # Chama a função principal para iniciar o menu interativo.