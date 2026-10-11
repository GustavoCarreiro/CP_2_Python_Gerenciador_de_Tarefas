'''Persistencia.py - Guarda e recupera as tarefas em um arquivo

"Persistência" significa fazer os dados continuarem existindo depois que o sistema é fechado. Sem isso, as tarefas ficariam somente na mémória da máquina e sumiriam ao encerrar o sistema.

As tarefas são registradas no arquivo 'tarefas_cadastradas.json'.
'''

import os
import json
 
ARQUIVO = 'tarefas_cadastradas.json'


def salvar_tarefas(tarefas, arquivo=ARQUIVO):
    '''Salva a lista de tarefas no arquivo, substituindo o conteúdo anterior.
    
    Input:
    - tarefas: list -> A lista de tarefas a ser salva
    - arquivo: str -> Nome do arquivo (se não for informado, usa tarefas.json)
    '''
    with open(arquivo, 'w', encoding='utf-8') as file:
        json.dump(tarefas, file, ensure_ascii=False, indent=4)
 
 
def carregar_tarefas(arquivo=ARQUIVO):
    '''Realiza a leitura das tarefas salvas no arquivo.
    
    Input:
    - arquivo: str -> Nome do arquivo (se não for informado, usa tarefas.json)

    Output:
    - list -> As tarefas salvas, ou uma lista vazia [] se o arquivo ainda não existe ou se não puder ser lido
    '''
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print('Aviso: Não foi possível ler o arquivo de tarefas. Iniciando com lista vazia.')
        return []