import menu
from operator import itemgetter


def fifo(processos, quantum, sobrecarga):
    if processos == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos, quantum, sobrecarga)
    else:
        processos = sorted(processos, key=itemgetter('tempo_de_chegada'))
        output_size = len(str(len(processos)))
        tempo_de_espera = 0
        for index, processo in enumerate(processos):
            if index == 0:
                print(f"proc {index} " + (' '*(output_size - len(str(index)))) + (int(processo["tempo_de_execucao"]) * "■"))
            else:
                tempo_de_espera += int(processos[index-1]["tempo_de_execucao"])
                print(f"proc {index} " + (' '*(output_size - len(str(index)))) + ("□"*tempo_de_espera) + (int(processo["tempo_de_execucao"]) * "■"))
        print("-----------------------------------------------\n")
        return menu.main_menu(processos, quantum, sobrecarga)
