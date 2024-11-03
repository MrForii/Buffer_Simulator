from threading import Lock

class Buffer:
    def __init__(self, size=15):
        self.size = size
        self.data = []
        self.lock = Lock()

    def add(self, packet):
        """Añade un paquete si hay espacio."""
        with self.lock:
            if len(self.data) < self.size:
                self.data.append(packet)
                return True  # Indica que se agregó correctamente
            return False  # Buffer lleno

    def remove(self):
        """Elimina un paquete del buffer si está disponible."""
        with self.lock:
            if self.data:
                return self.data.pop(0)

    def get_status(self):
        """Devuelve el estado del buffer: paquetes actuales y capacidad total."""
        with self.lock:
            return len(self.data), self.size
