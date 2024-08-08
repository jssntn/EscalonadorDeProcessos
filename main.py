from menu import main_menu
from func_layouts import remove
from pyfiglet import Figlet
from rich.console import Console
from rich import print
from rich.align import Align


def main():
    try:
        console = Console()
        f = Figlet(font='chunky', width=150)
        console.print(Align.center(f.renderText('El Escalonador')), style="bold magenta", end=' ')
        console.print(Align.center("(Júlia & Tauane)™"), style="bold magenta")
        print('\n')
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

