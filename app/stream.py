import time
import random
from threading import Thread

class Stream:
    def __init__(self, buffer, paquete_lifetime=5):
        self.buffer = buffer
        self.paquete_lifetime = paquete_lifetime  # Tiempo de vida de cada paquete en segundos

    def _consumir_paquete(self):
        """Elimina un paquete del buffer después de un tiempo de vida específico."""
        time.sleep(self.paquete_lifetime)  # Espera hasta que expire el paquete
        removed_packet = self.buffer.remove()
        if removed_packet:
            print(f"Paquete {removed_packet} eliminado automáticamente por tiempo.")

    def start(self, duration=30):
        """Inicia la transmisión y consumo en paralelo."""
        for _ in range(duration):
            packet = random.randint(1, 100)

            if self.buffer.add(packet):
                print(f"Paquete {packet} agregado al buffer.")
                # Inicia un hilo que elimina el paquete tras `paquete_lifetime` segundos
                Thread(target=self._consumir_paquete).start()
            else:
                print("[red]Buffer lleno. No se pudo agregar paquete.[/red]")

            time.sleep(0.5)  # Espera entre transmisiones
