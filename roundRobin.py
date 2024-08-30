import menu
import copy
from operator import itemgetter
from live_layout import generate_layout


def round_robin(processos_raw, quantum, sobrecarga):
    if processos_raw == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos_raw, quantum, sobrecarga)
    else:
        processos = sorted(processos_raw, key=itemgetter('tempo_de_chegada'))
        processos_local = copy.deepcopy(processos)


        is_processing = True
        time_counter = processos[0]['tempo_de_chegada']-1

        while is_processing:
            is_processing = False
            is_ready = False

            for index, processo in enumerate(processos):
                if not is_ready:
                    is_ready = True
                    if processos_local[index]['tempo_de_execucao'] > 0:
                        is_processing = True
                        processo['inicio'].append(time_counter)

                        if processos_local[index]['tempo_de_execucao'] <= quantum:
                            time_counter += processos_local[index]['tempo_de_execucao']
                            processos_local[index]['tempo_de_execucao'] = 0

                        else:
                            time_counter += quantum + sobrecarga
                            processos_local[index]['tempo_de_execucao'] -= quantum

                        processo['final'].append(time_counter)

                if processos[(index + 1) % len(processos)]['tempo_de_chegada'] <= time_counter:
                    is_ready = False
                    if processos_local[(index + 1) % len(processos)]['tempo_de_execucao'] == 0:
                        is_ready = True

                if processos_local[index]['tempo_de_execucao'] > 0:
                    time_counter += 1
                    is_processing = True

        layout = []
        for index, processo in enumerate(processos_raw):
            layout.append("")
            for i, inicio in enumerate(processo['inicio']):
                if i == 0:
                    layout[index] += "◌" * processo['tempo_de_chegada']
                    layout[index] += "□" * (inicio - processo['tempo_de_chegada']+1)

                else:
                    layout[index] += "□" * (inicio - processo['final'][i - 1])

                if inicio != processo['inicio'][-1]:
                    layout[index] += "■" * (processo['final'][i] - inicio - sobrecarga)
                    layout[index] += "◪" * sobrecarga
                else:
                    layout[index] += "■" * (processo['final'][i] - inicio)

            # define a lista de inicios e finais como vazio para não rodar de novo
            processo['inicio'] = []
            processo['final'] = []

        generate_layout([], layout, time_counter)
        return menu.main_menu(processos_raw, quantum, sobrecarga)












