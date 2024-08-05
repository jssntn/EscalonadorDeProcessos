import menu
import copy
from operator import itemgetter
from layout_escalonamento import escalonador_layout



def round_robin(processos_raw, quantum, sobrecarga):
    if processos_raw == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos_raw, quantum, sobrecarga)
    else:
        processos = sorted(processos_raw, key=itemgetter('tempo_de_chegada'))
        processos_local = copy.deepcopy(processos)

        output_size = len(str(len(processos)))

        is_processing = True
        time_counter = 0

        while is_processing:
            is_processing = False

            for index, processo in enumerate(processos):
                is_ready = False
                while not is_ready:
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

                    if processos[(index + 1) % len(processos)]['tempo_de_chegada'] >= time_counter:
                        if processos_local[index]['tempo_de_execucao'] != 0:
                            is_ready = False

        layout = []
        for index, processo in enumerate(processos_raw):
            layout.append("")
            for i, inicio in enumerate(processo['inicio']):
                if index == 0 and i == 0:
                    layout[index] += "◫" * processo['tempo_de_chegada']
                if i == 0:
                    layout[index] += "□" * inicio

                else:
                    layout[index] += "□" * (inicio - processo['final'][i - 1])

                if inicio != processo['inicio'][-1]:
                    layout[index] += "■" * (processo['final'][i] - inicio - sobrecarga)
                    layout[index] += "◪" * sobrecarga
                else:
                    layout[index] += "■" * (processo['final'][i] - inicio)
                    # print("■" * (processo['final'][i] - inicio), end='')
            processo['inicio'] = []
            processo['final'] = []

        escalonador_layout("Escalonador de Processos", layout, processos_raw, quantum, sobrecarga)
        return menu.main_menu(processos_raw, quantum, sobrecarga)












