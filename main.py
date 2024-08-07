from menu import main_menu
import subprocess

def remove():
    tput = subprocess.Popen(['tput', 'cols'], stdout=subprocess.PIPE)
    cols = int(tput.communicate()[0].strip())
    print("\033[A{}\033[A".format(' '*cols))


def main():
    processos = []
    quantum = input("Quantum: ")
    remove()
    sobrecarga = input("Sobrecarga: ")
    remove()

    main_menu(processos, quantum, sobrecarga)


if __name__ == "__main__":
    main()

