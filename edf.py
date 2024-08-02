import menu
import copy
from operator import itemgetter


def edf(processos, quantum, sobrecarga):
    if processos == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos, quantum, sobrecarga)
    else:
        processos = sorted(processos, key=itemgetter('deadline'))
        processos_local = copy.deepcopy(processos)
        output_size = len(str(len(processos)))

        is_processing = True
        time_counter = 0
        while is_processing:
            is_processing = False
            for index, processo in enumerate(processos):
                if processos_local[index]["tempo_de_execucao"] > 0:
                    if processos_local[index]['tempo_de_execucao'] < quantum:
                        processos_local[index]['inicio'].append(time_counter)
                        time_counter += (processos_local[index]['tempo_de_execucao'] + sobrecarga)
                        processos_local[index]['final'].append(time_counter)
                        processos_local[index]['tempo_de_execucao'] -= processos_local[index]['tempo_de_execucao']

                    else:
                        is_processing = True
                        processos_local[index]['inicio'].append(time_counter)
                        time_counter += (quantum+sobrecarga)
                        processos_local[index]['final'].append(time_counter)
                        processos_local[index]['tempo_de_execucao'] -= quantum
                else:
                    pass

        print("---------------------- INICIO EDF ----------------------")
        for index, processo in enumerate(processos_local):
            print(f"proc {index} " + (' ' * (output_size - len(str(index)))), end='')
            for i, inicio in enumerate(processo['inicio']):
                if i == 0:
                    print("□" * inicio, end='')
                    print("■" * (processo['final'][i] - inicio - sobrecarga), end='')
                    print("◪" * sobrecarga, end="")
                else:
                    print("□" * (inicio - processo['final'][i-1]), end='')
                    print("■" * (processo['final'][i] - inicio - sobrecarga), end='')
                    print("◪" * sobrecarga, end="")
            print("\n")
        print("-----------------------------------------------\n")
        return menu.main_menu(processos, quantum, sobrecarga)
