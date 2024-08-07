from rich.table import Table
from rich.console import Console
from rich.align import Align


def show_all_process(processos):
    tables = []
    grid = Table(show_header=False, show_edge=False, show_lines=False)

    if len(processos) > 3:
        grid.add_column("C1", justify="center")
        grid.add_column("C2", justify="center")
        grid.add_column("C3", justify="center")

    else:
        for processo in processos:
            grid.add_row()

    for index, processo in enumerate(processos):
        tables.append(Table(expand=False))
        tables[index].add_column("ID")
        tables[index].add_column("chegada")
        tables[index].add_column("exec")
        tables[index].add_column("deadline")
        tables[index].add_row(str(index), str(processo["tempo_de_chegada"]), str(processo["tempo_de_execucao"]), str(processo["deadline"]))
        tables[index] = Align.center(tables[index], vertical="middle")

    console = Console()
    i = 0
    while i < len(tables):
        if len(tables) - i > 2:

            grid.add_row(tables[i], tables[i+1], tables[i+2])
            i += 3
        else:
            if len(tables) - i > 1:
                grid.add_row(tables[i], tables[i + 1])
                i += 2
            else:
                grid.add_row(tables[i])
                i += 1

    return Align.center(grid)

