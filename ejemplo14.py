# ABSTRACCIÓN
class Figura:
    def __init__(self, color):
        self._color = color

    # GET y SET
    def get_color(self):
        return self._color

    def set_color(self, nuevo_color):
        self._color = nuevo_color

    def calcular_area(self):
        pass


# HERENCIA
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self._lado = lado

    def get_lado(self):
        return self._lado

    def set_lado(self, valor):
        if valor > 0:
            self._lado = valor

    # POLIMORFISMO
    def calcular_area(self):
        return self._lado * self._lado


# HERENCIA
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self._radio = radio

    def get_radio(self):
        return self._radio

    def set_radio(self, valor):
        self._radio = valor

    # POLIMORFISMO
    def calcular_area(self):
        return 3.14 * self._radio * self._radio


# --- Prueba ---
cuadrado1 = Cuadrado("Azul", 5)
circulo1 = Circulo("Rojo", 3)

print(f"Área del cuadrado: {cuadrado1.calcular_area()}")
print(f"Área del círculo: {circulo1.calcular_area()}")

cuadrado1.set_color("Verde")
print("Nuevo color:", cuadrado1.get_color())