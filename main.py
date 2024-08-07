from menu import main_menu
from func_layouts import remove


def main():
    processos = []
    quantum = input("Quantum: ")
    remove()
    sobrecarga = input("Sobrecarga: ")
    remove()

    main_menu(processos, quantum, sobrecarga)


if __name__ == "__main__":
    main()

