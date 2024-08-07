import subprocess
import menu


def remove():
    tput = subprocess.Popen(['tput', 'cols'], stdout=subprocess.PIPE)
    cols = int(tput.communicate()[0].strip())
    print("\033[A{}\033[A".format(' '*cols))


def add_processo(processos, quantum, sobrecarga):
    tempo_de_chegada = input("Insira o tempo de chegada desse processo: ")
    remove()
    tempo_de_execucao = input("Agora, por favor insira o tempo de execução: ")
    remove()
    deadline = input("Por fim, informe a deadline do processo: ")
    remove()

    processo = {
        "tempo_de_chegada": int(tempo_de_chegada),
        "tempo_de_execucao": int(tempo_de_execucao),
        "deadline": int(deadline),
        "inicio": [],
        "final": []
    }

    processos.append(processo)

    return menu.main_menu(processos, int(quantum), int(sobrecarga))
