import menu
import copy
from live_layout import generate_layout


def fifo(processos, quantum, sobrecarga):
    if processos == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos, quantum, sobrecarga)
    else:
        chegadas = []

        for processo in processos:
            chegadas.append(processo['tempo_de_chegada'])

        index_min = min(range(len(chegadas)), key=chegadas.__getitem__)
        time_counter = processos[index_min]['tempo_de_chegada']

        layout = [""]*len(processos)

        for processo in processos:
            index_min = min(range(len(chegadas)), key=chegadas.__getitem__)
            layout[index_min] = ''
            layout[index_min] += "◌" * processos[index_min]['tempo_de_chegada']
            layout[index_min] += "□" * (time_counter - processos[index_min]['tempo_de_chegada'])
            layout[index_min] += "■" * processos[index_min]['tempo_de_execucao']
            time_counter += processos[index_min]['tempo_de_execucao']

            chegadas[index_min] = max(chegadas) + 1

        generate_layout([], layout, time_counter)
        return menu.main_menu(processos, quantum, sobrecarga)
