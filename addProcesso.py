import menu


def add_processo(processos, quantum, sobrecarga):
    tempo_de_chegada = input("Insira o tempo de chegada desse processo\n")
    tempo_de_execucao = input("Agora, por favor insira o tempo de execução\n")
    deadline = input("Por fim, informe a deadline do processo\n")

    processo = {
        "tempo_de_chegada": int(tempo_de_chegada),
        "tempo_de_execucao": int(tempo_de_execucao),
        "deadline": int(deadline)
    }

    processos.append(processo)

    return menu.main_menu(processos, int(quantum), int(sobrecarga))
