'''Interface.py - Interface com o usuário.

Este arquivo é o "painel de controle" do sistema: Mostra o logotipo e os menus, recebe o que o usuário digita e exibi as funções dos outros dois arquivos:
  - Tarefas.py -> Lógica (cadastrar, listar, atualizar, remover)
  - Persistencia.py -> Registrar e fazer a leitura das tarefas no arquivo tarefas_cadastradas.json
'''

import os
import Tarefas
import Persistencia

tarefas = Persistencia.carregar_tarefas()
 
def exibir_nome_do_sistema():
    '''Exibe o nome do sistema () em letras grandes, como um logotipo.'''
    print("""
 
░██████╗░███████╗██████╗░███████╗███╗░░██╗░█████╗░██╗░█████╗░██████╗░░█████╗░██████╗░	██████╗░███████╗
██╔════╝░██╔════╝██╔══██╗██╔════╝████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗	██╔══██╗██╔════╝
██║░░██╗░█████╗░░██████╔╝█████╗░░██╔██╗██║██║░░╚═╝██║███████║██║░░██║██║░░██║██████╔╝	██║░░██║█████╗░░
██║░░╚██╗██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██║██╔══██║██║░░██║██║░░██║██╔══██╗	██║░░██║██╔══╝░░
╚██████╔╝███████╗██║░░██║███████╗██║░╚███║╚█████╔╝██║██║░░██║██████╔╝╚█████╔╝██║░░██║	██████╔╝███████╗
░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝	╚═════╝░╚══════╝
 
████████╗░█████╗░██████╗░███████╗███████╗░█████╗░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
░░░██║░░░███████║██████╔╝█████╗░░█████╗░░███████║╚█████╗░
░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██╔══╝░░██╔══██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║███████╗██║░░░░░██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░
 
""")
 
 
def exibir_menu():
    '''Exibe na tela as opções do menu principal.'''
    print('1. Cadastrar Tarefas')
    print('2. Listar Tarefas')
    print('3. Atualizar Tarefas')
    print('4. Remover Tarefas')
    print('0. Sair\n')
 
def finalizar():
     '''Exibe a mensagem de encerramento do sistema.'''
     exibir_subtitulo('Finalizando Tarefas.')
 
def retornar_menu():
      '''O programa aguarda até o usuário pressionar ENTER.
      
      Serve para o usuário conseguir ler a mensagem na tela antes de o menu aparecer novamente.
      '''
      input('\nPressione ENTER para voltar ao menu principal.')
 
def opcao_invalida():
    '''Exibe a mensagem que o usuário digitou uma opção inexistente no menu.'''
    print('Opção Inválida! Tente Novamente.')
    retornar_menu()
 
def exibir_subtitulo(texto):
    '''Exibe o subtítulo de cada opção escolhida contida no menu principal.
    
    Input:
    - texto: str -> O título que será exibido
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
 
 
def exibir_data(mensagem, obrigatoria=True):
    '''Exibe uma data ao usuário e repete até ela ser válida.

    Input:
    - mensagem: str -> Texto que aparece para o usuário
    - obrigatoria: bool -> Se False, o usuário pode pressionar ENTER para pular

    Output:
    - Retorna a data (texto no formato DD/MM/AAAA) ou None se foi pulada
    '''
    while True:
        texto = input(mensagem).strip()
        if not texto and not obrigatoria:
            return None
        if Tarefas.validar_data(texto):
            return texto
        print('Data Inválida! Use o formato DD/MM/AAAA.')
 
 
def exibir_status(mensagem, obrigatoria=True):
    '''Exibe os status numerados e devolve o que o usuário escolher.

    Input:
    - mensagem: str -> Texto que aparece para o usuário
    - obrigatoria: bool -> Se False, o usuário pode pressionar ENTER para pular

    Output:
    - O nome do Status (ex: 'Pendente') ou None se foi pulado
    '''
    for i, status in enumerate(Tarefas.STATUS_VALIDOS, start=1):
        print(f'{i}. {status}')
       
    while True:
        texto = input(mensagem).strip()
        if not texto and not obrigatoria:
            return None
        if texto.isdigit() and 1 <= int(texto) <= len(Tarefas.STATUS_VALIDOS):
            return Tarefas.STATUS_VALIDOS[int(texto) - 1]
        print('Opção de Status Inválida.')
 
 
def exibir_id(mensagem):
    '''Pede o número (ID) de uma tarefa. 
    
    Input:
    - mensagem: str -> Texto que aparece para o usuário
    
    Output:
    - O ID como número inteiro, ou None se o usuário não digitou um número
    '''
    texto = input(mensagem).strip()
    if texto.isdigit():
        return int(texto)
    return None
 
 
def mostrar_tarefas(lista):
    '''Exibe uma lista de tarefas em forma de tabela.
    
    Input:
    - lista: list -> As tarefas que serão exibidas
    '''
    if not lista:
        print('Nenhuma tarefa encontrada.')
        return
 
    print(f'{"ID":<5} | {"Nome":<20} | {"Descrição":<50} | {"Vencimento":<12} | Status')
    print('-' * 90)
 
    for t in lista:
        print(f'{t["id"]:<5} | {t.get("nome", ""):<20} | {t["descricao"]:<50} | {t["vencimento"]:<12} | {t["status"]}')


def cadastrar_nova_tarefa():
    '''Opção 1: Exibe os dados, cria uma tarefa e salva no arquivo.
    
    Input:
    - Nome, Descrição, Data de Vencimento e Status (digitados pelo usuário)
    
    Output:
    - A tarefa é adicionada à lista e registrada no arquivo tarefas_cadastradas.json
    '''
    exibir_subtitulo('Cadastro de Novas Tarefas')

    nome_tarefa = input('Digite o Nome da Nova Tarefa: ').strip()
    
    if not nome_tarefa:
        print('O Nome não pode ficar vazio.')
        retornar_menu()
        return

    descricao = input('Digite a Descrição da nova tarefa: ').strip()

    if not descricao:
            print('A Descrição não pode ficar vazia.')
            retornar_menu()
            return
 
    vencimento = exibir_data('Data de Vencimento (DD/MM/AAAA): ')
    print('\nStatus da Tarefa: ')
    status = exibir_status('Escolha o Status: ')

    Tarefas.cadastrar_tarefa(tarefas, nome_tarefa, descricao, vencimento, status)
    Persistencia.salvar_tarefas(tarefas)

    print('\nTarefa cadastrada com sucesso!')
    retornar_menu()
 
 
def listar_tarefas():
    '''Opção 2: Exibe as tarefas, com filtro por status ou data.
    
    Input:
    - O tipo de filtro e o valor do filtro (digitados pelo usuário)

    Output:
    - A tabela de tarefas exibida na tela
    '''
    exibir_subtitulo('Lista de Tarefas')
    print('Filtrar por: ')
    print('1. Todas')
    print('2. Status')
    print('3. Data de Vencimento')

    opcao = input('\nEscolha uma opção: ').strip()

    status = None
    vencimento = None
 
    if opcao == '2':
        print()
        status = exibir_status('Escolha o Status: ')
    elif opcao == '3':
        vencimento = exibir_data('Data de Vencimento (DD/MM/AAAA): ')
    elif opcao != '1':
        opcao_invalida()
        return
    
    print()
    mostrar_tarefas(Tarefas.listar_tarefas(tarefas, status, vencimento))
    retornar_menu()
 
 
def atualizar_tarefa():
    '''Opção 3: Altera Descrição, Data e/ou Status de uma tarefa existente.
    
    Input:
    - O ID da tarefa e os novos valores (ENTER mantém o valor anterior)

    Output:
    - A tarefa é alterada na lista e o arquivo é atualizado
    '''
    exibir_subtitulo('Atualizar Tarefa')
    mostrar_tarefas(Tarefas.listar_tarefas(tarefas))
   
    if not tarefas:
        retornar_menu()
        return
 
    id_tarefa = exibir_id('\nDigite o ID da tarefa que deseja atualizar: ')
 
    if id_tarefa is None or Tarefas.buscar_tarefa(tarefas, id_tarefa) is None:
        print('Tarefa Não Encontrada.')
        retornar_menu()
        return

    nome_tarefa = input('Novo Nome da Tarefa: ').strip() or None
    descricao = input('Nova Descrição: ').strip() or None
    vencimento = exibir_data('Nova Data de Vencimento (DD/MM/AAAA): ', obrigatoria=False)
    print('\nNovo Status: ')
    status = exibir_status('Escolha o Novo Status: ', obrigatoria=False)
 
    Tarefas.atualizar_tarefa(tarefas, id_tarefa, nome_tarefa, descricao, vencimento, status)
    Persistencia.salvar_tarefas(tarefas)
 
    print('\nTarefa Atualizada com Sucesso!')
    retornar_menu()


def remover_tarefa():
    '''Opção 4: Exclui uma tarefa, solicitando antes a confirmação de remoção.
    
    Input:
    - O ID da tarefa e a confirmação (s/n)

    Output:
    - A tarefa é removida da lista e o arquivo é atualizado
    '''
    exibir_subtitulo('Remover Tarefa')
    mostrar_tarefas(Tarefas.listar_tarefas(tarefas))
 
    if not tarefas:
        retornar_menu()
        return
 
    id_tarefa = exibir_id('\nDigite o ID da tarefa que deseja remover: ')
 
    if id_tarefa is None or Tarefas.buscar_tarefa(tarefas, id_tarefa) is None:
        print('Tarefa Não Encontrada.')
    elif input('Tem certeza que deseja remover essa tarefa? (s/n): ').strip().lower() == 's':
        Tarefas.remover_tarefa(tarefas, id_tarefa)
        Persistencia.salvar_tarefas(tarefas)
        print('Tarefa Removida com Sucesso!')
    else:
        print('Remoção Cancelada.')
    retornar_menu()


def escolher_opcao():
    '''Realizada a opção digitada no menu e exibi a opção escolhida.
    
    Input:
    - A opção digitada pelo usuário
    
    Output:
    - True para o sistema Continuar executando ou False para Encerrar
    '''
    try:
        opcao_escolhida = input('Escolha uma opção contida no Menu Principal: ').strip()
 
        if opcao_escolhida == '1':
            cadastrar_nova_tarefa()
        elif opcao_escolhida == '2':
            listar_tarefas()
        elif opcao_escolhida == '3':
            atualizar_tarefa()
        elif opcao_escolhida == '4':
            remover_tarefa()
        elif opcao_escolhida == '0':
            finalizar()
            return False
        else:
            opcao_invalida()
 
    except KeyboardInterrupt:
        finalizar()
        return False
 
    return True


def main():
    '''Função Principal: Repete o Menu Principal até o usuário escolher Sair.'''
    continuar = True
 
    while continuar:
        os.system('cls')
        exibir_nome_do_sistema()
        exibir_menu()
        continuar = escolher_opcao()
 
if __name__ == '__main__':
    main()