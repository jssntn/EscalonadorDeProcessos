from func_layouts import show_all_process
from func_layouts import remove
import menu
from rich.console import Console

console = Console()


def edt_process(processos, quantum, sobrecarga):

    console.print(show_all_process(processos))

    process_id = input("Digite o id do processo que deseja editar: ")
    processos[int(process_id)]["tempo_de_chegada"] = int(input("Chegada: "))
    remove()
    processos[int(process_id)]["tempo_de_execucao"] = int(input("Tempo de execução: "))
    remove()
    processos[int(process_id)]["deadline"] = int(input("Deadline: "))
    remove()

    return menu.main_menu(processos, quantum, sobrecarga)
