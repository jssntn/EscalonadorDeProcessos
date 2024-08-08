import sys
import menu
from func_layouts import remove

def add_processo(processos, quantum, sobrecarga):
    try:
        tempo_de_chegada = input("Insira o tempo de chegada desse processo: ")
        remove()
        if type(int(tempo_de_chegada)) is not int:
            raise Exception("Tempo de chegada inválido")

        tempo_de_execucao = input("Agora, por favor insira o tempo de execução: ")
        remove()
        if type(int(tempo_de_execucao)) is not int:
            raise Exception("Tempo de execucao inválido")

        deadline = input("Por fim, informe a deadline do processo: ")
        remove()
        if type(int(deadline)) is not int:
            raise Exception("Deadline inválido")

        processo = {
            "tempo_de_chegada": int(tempo_de_chegada),
            "tempo_de_execucao": int(tempo_de_execucao),
            "deadline": int(deadline),
            "inicio": [],
            "final": []
        }

        processos.append(processo)

        return menu.main_menu(processos, int(quantum), int(sobrecarga))

    except Exception as e:
        print(e)
        return add_processo(processos, quantum, sobrecarga)

