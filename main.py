from menu import main_menu


def main():
    processos = []
    print('■')
    print('□')
    quantum = input("Por favor, informe o quantum que será utilizado para a simulação\n")
    sobrecarga = input("e qual seria a sobrecarga do sistema?\n")

    main_menu(processos, quantum, sobrecarga)


if __name__ == "__main__":
    main()