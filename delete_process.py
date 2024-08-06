import menu
import time


def delete_process(processos, quantum, sobrecarga):
    if len(processos) != 0:
        for index, processo in enumerate(processos):
            print('ID ' + str(index) + ':\n')
            print('Chegada: ' + str(processo['tempo_de_chegada']))
            print('Execução: ' + str(processo['tempo_de_execucao']))
            print('Prioridade: ' + str(processo['deadline']))

        del_index = input('Insira o código do processo que deseja deletar: ')
        del processos[int(del_index)]
        return menu.main_menu(processos, quantum, sobrecarga)

    else:
        print("Não existem processos a serem excluídos")
        time.sleep(10)
        return menu.main_menu(processos, quantum, sobrecarga)
