import time
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.align import Align


def generate_table(processos) -> Panel:
    """Make a new table."""
    table = Table()
    table.add_column("process id")
    table.add_column("value", overflow='fold', max_width=70)
    align_table = Align.center(table)
    for index, processo in enumerate(processos):
        table.add_row("proc "+str(index), processo)
    panel = Panel(
        title='Processando: ■ Em espera: □ Sobrecarga: ◪',
        renderable=align_table,
        expand=False,)
    return panel


def generate_layout(layout, processos, tempo_total) -> None:
    with Live(Align.center(generate_table(layout)), refresh_per_second=4, screen=True, vertical_overflow="visible", transient=True) as live:
        panel = Panel('Processando: ■ \nEm espera: □\nSobrecarga: ◪', title="Live", border_style='bright_blue')
        iterator = 2
        for _ in range(tempo_total):
            layout = []
            for processo in processos:
                layout.append(processo[:iterator])
            time.sleep(0.1)
            live.update(Align.center(generate_table(layout)))
            iterator += 1
        time.sleep(5)
        live.update(Align.center(generate_table([])))
