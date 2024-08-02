from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table


def escalonador_layout(title, processos):
    console = Console()
    layout = Layout()

    layout.split(
        # Layout(name=title, size=3, visible= False),
        Layout(name='body', ratio=1),
    )
    layout['body'].split(
        Layout(name='main', ratio=1),
        Layout(name='legenda', ratio=1),
    )
    table = Table(show_header=False, expand=True)
    table.add_column("process_id", justify="center")
    table.add_column("escalonamento", justify="left", overflow='fold')

    for index, processo in enumerate(processos):
        table.add_row("proc " + str(index), processo)

    layout['body']['main'].update(
        Panel(
            title=title,
            renderable=table
           )
    )
    layout['body']['legenda'].update(
        Panel(
            title='Legenda',
            renderable='Processando: ■ \nEm espera: □\nSobrecarga: ◪',
            border_style="red"
        )
    )
    console.print(layout)





