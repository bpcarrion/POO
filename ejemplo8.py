class Computadora:
    def __init__(self, procesador, ram):
        self.procesador = procesador
        self.ram = ram
        
    def encender(self):
        print("Sistema iniciado. ",self.procesador,"  RAM: ", self.ram)

class Servidor(Computadora):
    def __init__(self, procesador, ram, ip_estatica):
        super().__init__(procesador, ram)
        self.ip_estatica = ip_estatica
        
    def reiniciar_servidor(self):
        print("Servidor reiniciado mediante IP: ",self.ip_estatica, "procesador: ", self.procesador, "RAM: ", self.ram)

# Uso:
server = Servidor("Intel Xeon", 128, "192.168.1.10")
server.encender()
server.reiniciar_servidor()