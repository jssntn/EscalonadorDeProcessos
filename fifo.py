import menu
from operator import itemgetter
from live_layout import generate_layout


def fifo(processos, quantum, sobrecarga):
    if processos == 0:
        print("É necessário adicionar ao menos um processo para iniciar a simulação")
        return menu.main_menu(processos, quantum, sobrecarga)
    else:
        processos = sorted(processos, key=itemgetter('tempo_de_chegada'))
        output_size = len(str(len(processos)))
        time_counter = processos[0]['tempo_de_chegada']
        layout = []
        tempo_de_espera = 0
        for index, processo in enumerate(processos):
            layout.append("")
            if index == 0:
                layout[index] += "◌" * processo['tempo_de_chegada']
                layout[index] += "■" * int(processo["tempo_de_execucao"])
                time_counter += processo['tempo_de_execucao']
            else:
                layout[index] += "◌" * processo['tempo_de_chegada']
                layout[index] += "□" * (time_counter - processo['tempo_de_chegada'])
                layout[index] += "■" * processo['tempo_de_execucao']
                time_counter += processo['tempo_de_execucao']

        generate_layout([], layout, time_counter)
        return menu.main_menu(processos, quantum, sobrecarga)
