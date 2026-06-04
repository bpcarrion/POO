# ------------------------------
# ABSTRACCIÓN: Definimos solo lo básico que tiene todo vehículo
# ------------------------------
class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        # ENCAPSULAMIENTO: Atributos privados (con guion bajo)
        self._marca = marca
        self._modelo = modelo
        self._velocidad = velocidad

    # Métodos GET y SET (para acceder y modificar los datos de forma segura)
    def get_marca(self):
        return self._marca

    def set_marca(self, nueva_marca):
        if nueva_marca != "":
            self._marca = nueva_marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    def get_velocidad(self):
        return self._velocidad

    def set_velocidad(self, nueva_velocidad):
        if nueva_velocidad >= 0:
            self._velocidad = nueva_velocidad

    # Método base
    def moverse(self):
        # Método vacío, lo definiremos en las clases hijas
        pass


# ------------------------------
# HERENCIA: Coche hereda todo de Vehiculo
# ------------------------------
class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad, puertas):
        super().__init__(marca, modelo, velocidad) # Llamamos al constructor padre
        self._puertas = puertas # Atributo propio

    # GET y SET propio
    def get_puertas(self):
        return self._puertas

    def set_puertas(self, nuevas_puertas):
        self._puertas = nuevas_puertas

    # ------------------------------
    # POLIMORFISMO: Cambiamos lo que hace el método
    # ------------------------------
    def moverse(self):
        return f"El coche {self._marca} {self._modelo} va a {self._velocidad} km/h"


# HERENCIA: Moto hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad, tipo):
        super().__init__(marca, modelo, velocidad)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    # POLIMORFISMO: Mismo método, diferente resultado
    def moverse(self):
        return f"La moto {self._marca} es de tipo {self._tipo} y corre a {self._velocidad} km/h"


# --- Prueba ---
mi_coche = Coche("hyunday", "accent", 180, 4)
mi_moto = Moto("Factory", "ninja", 280, "Deportiva")

print(mi_coche.moverse())
print(mi_moto.moverse())

# Usamos SET para cambiar datos
mi_coche.set_marca("kia")
print("Nueva marca del coche:", mi_coche.get_marca())