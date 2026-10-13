'''Tarefas.py - Lógica do sistema (as "regras" do gerenciador de tarefas).

Este arquivo NÃO conversa com o usuário (não usa input nem menus). Ele somente realiza as operações com as tarefas:
  - Validar dados (Data e Status)
  - Cadastrar, Buscar, Listar, Atualizar e Remover tarefas

Como cada tarefa é registrada (um dicionário):
    {'id': 1, 'descricao': 'Estudar', 'vencimento': '10/10/2026', 'status': 'Pendente'}

Todas as tarefas ficam juntas em uma lista de dicionários:
    [ {tarefa 1}, {tarefa 2}, {tarefa 3} ]
'''

from datetime import datetime
 
STATUS_VALIDOS = ['Pendente', 'Em Andamento', 'Concluída\n']
FORMATO_DATA = '%d/%m/%Y'


def validar_data(texto):
    '''Confere se o texto é uma data real no formato DD/MM/AAAA.
    
    Input:
    - texto: str -> A data digitada

    Output:
    - True se a data for válida, False se não for
    '''
    try:
        datetime.strptime(texto, FORMATO_DATA)
        return True
    except ValueError:
        return False


def validar_status(status):
    '''Confere se o status é um dos aceitos pelo sistema.
    
    Input:
    - status: str -> O status a conferir

    Output:
    - True se o status está na lista STATUS_VALIDOS, False se não estiver
    '''
    return status in STATUS_VALIDOS


def buscar_tarefa(tarefas, id_tarefa):  
    '''Realiza a procura de uma tarefa pelo ID

    Input:
    - tarefas: list -> A lista com todas as tarefas
    - id_tarefa: int -> O número (ID) da tarefa procurada

    Output:
    - O dicionário da tarefa, se for encontrada
    - None se não existir tarefa com esse ID
    '''
    for tarefa in tarefas:      
        if tarefa['id'] == id_tarefa:
         return tarefa    
    return None

 
def gerar_id(tarefas):
    '''Cria o próximo ID para uma nova tarefa.
    
    Input:
    - tarefas: list -> A lista com todas as tarefas

    Output:
    - int -> O maior ID existente + 1 (ou 1, se a lista estiver vazia)
    '''
    if not tarefas:
        return 1
    return max(t['id'] for t in tarefas) + 1
 
def cadastrar_tarefa(lista, nome, descricao, vencimento, status):
    '''Realiza a criação de uma nova tarefa e a adiciona na lista.
    
    Input:
    - lista: list -> A lista onde a tarefa será adicionada
    - nome: str -> Título curto da tarefa (ex.: 'Sistema em Python')
    - descricao: str -> O que precisa ser feito
    - vencimento: str -> Data limite no formato DD/MM/AAAA
    - status: str -> 'Pendente', 'Em Andamento' ou 'Concluída'

    Output: 
    - O dicionário da tarefa criada, ou None se algum dado for inválido
    '''
    if not nome:
        print('Nome não pode ser vazio.')
        return None
    if not descricao:
        print('A Descrição não pode ser vazia.')
        return None
    if not validar_data(vencimento):
        print('Data Inválida! Use o formato DD/MM/AAAA.')
        return None
    if not validar_status(status):
        print('Status Inválido! Use um dos seguintes: Pendente, Em Andamento, Concluída.')
        return None
 
    tarefa = {
        'id': gerar_id(lista),
        'nome': nome,
        'descricao': descricao,
        'vencimento': vencimento,
        'status': status
    }
 
    lista.append(tarefa)
    return tarefa
 
 
def listar_tarefas(lista, status=None, vencimento=None):
    '''Devolve as tarefas, com filtros.
    
    Input:
    - lista: list -> Todas as tarefas
    - status: str -> Se informado, devolve só as tarefas com esse status
    - vencimento: str -> Se informado, devolve só as tarefas com essa data

    Output:
    - list -> As tarefas que passaram pelos filtros (sem filtro = todas)
    '''
    resultado = lista
 
    if status is not None:
        resultado = [t for t in resultado if t["status"] == status]
    if vencimento is not None:
        resultado = [t for t in resultado if t["vencimento"] == vencimento]
 
    return list(resultado)
 
 
def atualizar_tarefa(lista, id_tarefa, nome=None, descricao=None, vencimento=None, status=None):
    '''Atualiza só os campos informados.
    
    Input:
    - lista: list -> Todas as tarefas
    - id_tarefa: int -> O ID da tarefa que será alterada
    - nome, descricao, vencimento, status: Novos valores (None = não alterar)

    Output:
    - True se atualizou, False se a tarefa não existe ou algum dado é inválido
    '''
    tarefa = buscar_tarefa(lista, id_tarefa)
 
    if tarefa is None:
        return False
    if vencimento is not None and not validar_data(vencimento):
        print('Data Inválida! Use o formato DD/MM/AAAA.')
        return False
    if status is not None and not validar_status(status):
        print('Status Inválido! Use um dos seguintes: Pendente, Em Andamento, Concluída.')
        return False

    if nome:
        tarefa['nome'] = nome
    if descricao:
        tarefa['descricao'] = descricao
    if vencimento:
        tarefa['vencimento'] = vencimento
    if status:
        tarefa['status'] = status
    return True
 
 
def remover_tarefa(lista, id_tarefa):
    '''Realiza a remoção de uma tarefa presente na lista.
    
    Input:
    - lista: list -> Todas as tarefas
    - id_tarefa: int -> O ID da tarefa que será removida

    Output:
    - True se removeu, False se não existe tarefa com esse ID
    '''
    tarefa = buscar_tarefa(lista, id_tarefa)
    if tarefa is None:
        return False
    lista.remove(tarefa)
    return True