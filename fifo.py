import menu
import copy
from operator import itemgetter
from live_layout import generate_layout


def fifo(processos_raw, quantum, sobrecarga):
    if processos_raw == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos_raw, quantum, sobrecarga)
    else:
        processos = sorted(processos_raw, key=itemgetter('tempo_de_chegada'))
        processos_local = copy.deepcopy(processos)

        numero_de_processos_processados = 0
        time_counter = processos[0]['tempo_de_chegada']

        while numero_de_processos_processados < len(processos):

            processo_escolhido = None

            if numero_de_processos_processados != 0:
                processos_disponiveis = []

                for index, processo in enumerate(processos):
                    if processo['tempo_de_chegada'] <= time_counter and processos_local[index][
                        'tempo_de_execucao'] != 0:
                        processos_disponiveis.append(processo)

                if processos_disponiveis:
                    processos_disponiveis.sort(key=itemgetter('tempo_de_chegada'))
                    processo_escolhido = processos_disponiveis[0]
            else:
                processo_escolhido = processos[0]

            if processo_escolhido != None:
                processo_escolhido_index = processos.index(processo_escolhido)

                numero_de_processos_processados += 1
                processos[processo_escolhido_index]['inicio'].append(time_counter)

                time_counter += processos_local[processo_escolhido_index]['tempo_de_execucao']
                processos_local[processo_escolhido_index]['tempo_de_execucao'] = 0

                processos[processo_escolhido_index]['final'].append(time_counter)
            else:
                time_counter = processos[numero_de_processos_processados]['tempo_de_chegada']

        layout = []
        turnAround = 0
        for index, processo in enumerate(processos_raw):
            layout.append("")
            inicio_do_processo = 0
            final_do_processo = 0
            for i, inicio in enumerate(processo['inicio']):
                # verifica se é a primeira iteração
                if i == 0:
                    layout[index] += "◌" * processo['tempo_de_chegada']
                    layout[index] += "□" * (inicio - processo['tempo_de_chegada'])
                    inicio_do_turnaround = processo['tempo_de_chegada']

                else:
                    layout[index] += "□" * (inicio - processo['final'][i - 1])

                if inicio != processo['inicio'][-1]:
                    layout[index] += "■" * (processo['final'][i] - inicio - sobrecarga)
                    layout[index] += "◪" * sobrecarga
                else:
                    layout[index] += "■" * (processo['final'][i] - inicio)
                    final_do_turnaround = processo['final'][i]

            turnAround += final_do_turnaround - inicio_do_turnaround
            processo['inicio'] = []
            processo['final'] = []

        turnAround = turnAround / numero_de_processos_processados

        generate_layout([], layout, time_counter, turnAround)
        return menu.main_menu(processos_raw, quantum, sobrecarga)

