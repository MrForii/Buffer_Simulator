from rich.table import Table

def mostrar_estado_buffer(buffer):
    """Genera una tabla con el estado del buffer."""
    table = Table(title="Estado del Buffer")
    table.add_column("Posición", justify="center")
    table.add_column("Estado", justify="center")

    current, total = buffer.get_status()
    for i in range(total):
        if i < current:
            table.add_row(f"{i + 1}", "[green]Cargado[/green]")
        else:
            table.add_row(f"{i + 1}", "[red]Vacío[/red]")

    return table
