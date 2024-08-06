from simple_term_menu import TerminalMenu
from addProcesso import add_processo
from fifo import fifo
from sjf import sjf
from edf import edf
from roundRobin import round_robin
from delete_process import delete_process


def main_menu(processos, quantum, sobrecarga):
    terminal_menu = TerminalMenu(["Adicionar processo", "Remover Processo", "Iniciar simulação"], title="Selecione uma das opções abaixo")
    menu0_entry_index = terminal_menu.show()

    if menu0_entry_index == 0:
        add_processo(processos, quantum, sobrecarga)
    elif menu0_entry_index == 1:
        delete_process(processos, quantum, sobrecarga)
    else:
        esc_menu = TerminalMenu(["FIFO", "SJF", "Round Robin", "EDF"])
        esc_entry_index = esc_menu.show()
        if esc_entry_index == 0:
            fifo(processos, quantum, sobrecarga)
        elif esc_entry_index == 1:
            sjf(processos, quantum, sobrecarga)
        elif esc_entry_index == 2:
            round_robin(processos, quantum, sobrecarga)
        elif esc_entry_index == 3:
            edf(processos, quantum, sobrecarga)
