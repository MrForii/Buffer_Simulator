from app.buffer import Buffer
from app.stream import Stream
from app.monitor import mostrar_estado_buffer
import threading
import time
from rich.live import Live
from rich.console import Console

console = Console()

def ejecutar_monitor(buffer, live):
    """Monitorea el estado del buffer en vivo."""
    try:
        with live:  # Inicia el monitor en vivo
            while True:
                live.update(mostrar_estado_buffer(buffer))
                time.sleep(1)
    except KeyboardInterrupt:
        pass  # Permite salir limpiamente con Ctrl+C

def main():
    buffer = Buffer(size=15)  # Tamaño del buffer
    stream = Stream(buffer, paquete_lifetime=5)  # Paquete dura 5 segundos

    # Inicia el monitor en vivo
    live = Live(mostrar_estado_buffer(buffer), refresh_per_second=2, console=console)

    # Ejecuta el monitor en un hilo separado
    monitor_thread = threading.Thread(target=ejecutar_monitor, args=(buffer, live))
    monitor_thread.daemon = True  # El hilo se cerrará al finalizar el programa
    monitor_thread.start()

    # Imprimir mensajes en consola
    console.print("[bold blue]Iniciando transmisión...[/bold blue]")
    stream.start(duration=30)  # Inicia la transmisión (30 segundos)

    # Cierra el monitor en vivo y muestra los mensajes finales
    live.stop()
    console.print(" \n")
    console.print("[bold red]Cerrando transmisión...[/bold red]")
    console.print("[bold green]Transmisión finalizada.[/bold green]")

if __name__ == "__main__":
    main()
