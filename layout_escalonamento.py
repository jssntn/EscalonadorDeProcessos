from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
import menu


def escalonador_layout(title, processos, process, quantum, sobrecarga):
    console = Console()
    layout = Layout()

    layout.split(
        # Layout(name=title, size=3, visible= False),
        Layout(name='body', ratio=1),
    )
    layout['body'].split(
        Layout(name='main', ratio=1),
        Layout(name='legenda')
    )

    table = Table(show_header=False, expand=True)
    legenda = Table(show_header=False)
    legenda.add_column(justify='center')
    table.add_column("process_id", justify="center")
    table.add_column("escalonamento", justify="left", overflow='fold')

    legenda.add_row(
            'Processando: ■ \nEm espera: □\nSobrecarga: ◪')
    for index, processo in enumerate(processos):
        table.add_row("proc " + str(index), processo)

    layout['body']['main'].update(
        Panel(
            title=title,
            renderable=table
           )
    )

    console.print(layout['body']['main'])
    console.print(legenda, justify='center')






