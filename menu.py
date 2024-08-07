import sys
from simple_term_menu import TerminalMenu
from addProcesso import add_processo
from fifo import fifo
from sjf import sjf
from edf import edf
from roundRobin import round_robin
from delete_process import delete_process
from edit_process import edt_process


def main_menu(processos, quantum, sobrecarga):
    terminal_menu = TerminalMenu(["Adicionar processo", "Editar Processo", "Remover Processo", "Iniciar simulação", "Sair"], title="Selecione uma das opções abaixo")
    menu0_entry_index = terminal_menu.show()

    if menu0_entry_index == 0:
        add_processo(processos, quantum, sobrecarga)
    elif menu0_entry_index == 1:
        edt_process(processos, quantum, sobrecarga)
    elif menu0_entry_index == 2:
        delete_process(processos, quantum, sobrecarga)
    elif menu0_entry_index == 3:
        esc_menu = TerminalMenu(["FIFO", "SJF", "Round Robin", "EDF", "Voltar"])
        esc_entry_index = esc_menu.show()
        if esc_entry_index == 0:
            fifo(processos, quantum, sobrecarga)
        elif esc_entry_index == 1:
            sjf(processos, quantum, sobrecarga)
        elif esc_entry_index == 2:
            round_robin(processos, quantum, sobrecarga)
        elif esc_entry_index == 3:
            edf(processos, quantum, sobrecarga)
        else:
            return main_menu(processos, quantum, sobrecarga)
    else:
        sys.exit()
    return

