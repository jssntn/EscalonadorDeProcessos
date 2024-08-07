import menu
import time
from func_layouts import show_all_process
from rich.console import Console

console = Console()


def delete_process(processos, quantum, sobrecarga):
    try:
        if len(processos) == 0:
            raise Exception("Nenhum processo foi adicionado")

        console.print(show_all_process(processos))
        process_id = input("Digite o id do processo que deseja deletar: ")
        print("\033[A                             \033[A")
        del processos[int(process_id)]
        menu.main_menu(processos, quantum, sobrecarga)

    except Exception as e:
        print(e)
