import menu
from func_layouts import show_all_process
from func_layouts import remove
from rich.console import Console

console = Console()


def delete_process(processos, quantum, sobrecarga):
    try:
        if len(processos) == 0:
            raise Exception("Nenhum processo foi adicionado")

        console.print(show_all_process(processos))
        process_id = input("Digite o id do processo que deseja deletar: ")
        remove()
        del processos[int(process_id)]
        menu.main_menu(processos, quantum, sobrecarga)

    except Exception as e:
        print(e)
