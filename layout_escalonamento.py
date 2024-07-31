from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich import print
from rich.table import Table


def escalonador_layout(title, processos):
    console = Console()
    layout = Layout()

    layout.split(
        Layout(name=title, size=3, visible= False),
        Layout(name='main')
    )
    table = Table(show_header=False, expand=True, border_style="deep_pink4")
    table.add_column("process_id", justify="center", style="magenta")
    table.add_column("escalonamento", justify="left")

    for index, processo in enumerate(processos):
        table.add_row("proc " + str(index), processo)

    layout['main'].update(
        Panel(
            title=title,
            renderable=table,
            border_style="bright_magenta")
    )
    console.print(layout)


