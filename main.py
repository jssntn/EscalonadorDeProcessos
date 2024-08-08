from menu import main_menu
from func_layouts import remove


def main():
    try:
        processos = []
        quantum = input("Quantum: ")
        remove()
        if type(int(quantum)) is not int:
            raise Exception("Invalid quantum value")

        sobrecarga = input("Sobrecarga: ")
        remove()
        if type(int(sobrecarga)) is not int:
            raise Exception("Invalid sobrecarga value")

        return main_menu(processos, quantum, sobrecarga)
    except Exception as e:
        print(e)
        return main()


if __name__ == "__main__":
    main()

