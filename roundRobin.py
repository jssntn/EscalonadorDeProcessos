import menu
from operator import itemgetter


def round_robin (processos, quantum, sobrecarga):
    if processos == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos, quantum, sobrecarga)
    else:
        processos = sorted(processos, key=itemgetter('tempo_de_chegada'))
        processos_ativos = len(processos)
        output_size = len(str(len(processos)))

        print("---------------------- INICIO ROUND ROBIN ----------------------")
        for index, processo in enumerate(processos):
            print(f"proc {index} " + (' ' * (output_size - len(str(index)))), end='')
            # if index == 0:
            #     while processo["tempo_de_execucao"] > 0:
            #         if processo["tempo_de_execucao"] >= quantum:
            #             print("■" * quantum, end='')
            #         else:
            #             print("■" * processo["tempo_de_execucao"], end='')
            #
            #         print("◪" * sobrecarga, end='')
            #         processo["tempo_de_execucao"] -= quantum
            #         if processo["tempo_de_execucao"] > 0:
            #             print("□" * ((len(processos) - 1) * (quantum + sobrecarga)), end='')

            # else:
            tempo_inativo = processo["tempo_de_execucao"] % quantum
            while processo["tempo_de_execucao"] > 0:
                print("□" * (index * (quantum + sobrecarga)), end='')
                if processo["tempo_de_execucao"] >= quantum:
                    print("■" * quantum, end='')
                else:
                    print("■" * processo["tempo_de_execucao"], end='')
                print("◪" * sobrecarga, end='')
                processo["tempo_de_execucao"] -= quantum
                if processo["tempo_de_execucao"] > 0:
                    if index != 0:
                        if tempo_inativo != 0:
                            print("□" * (tempo_inativo+sobrecarga), end='')
                        else:
                            print("□" * (quantum + sobrecarga), end='')
                    else:
                        print("□" * ((processos_ativos - 1) * (quantum + sobrecarga)), end='')
                else:
                    processos_ativos -= 1

            print("\n")
