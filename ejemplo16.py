# ABSTRACCIÓN
class Transporte:
    def __init__(self, matricula, velocidad):
        self._matricula = matricula
        self._velocidad = velocidad

    # GET y SET
    def get_matricula(self):
        return self._matricula

    def set_matricula(self, nueva):
        self._matricula = nueva

    def get_velocidad(self):
        return self._velocidad

    def set_velocidad(self, valor):
        if valor > 0:
            self._velocidad = valor

    def tiempo_viaje(self, distancia):
        pass


# HERENCIA
class Camion(Transporte):
    def __init__(self, matricula, velocidad, carga):
        super().__init__(matricula, velocidad)
        self._carga = carga

    def get_carga(self):
        return self._carga

    def set_carga(self, peso):
        self._carga = peso

    # POLIMORFISMO
    def tiempo_viaje(self, distancia):
        # Camión va más lento
        return distancia / (self._velocidad * 0.8)


# HERENCIA
class Bicicleta(Transporte):
    def __init__(self, matricula, velocidad, tipo):
        super().__init__(matricula, velocidad)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, nuevo):
        self._tipo = nuevo

    # POLIMORFISMO
    def tiempo_viaje(self, distancia):
        return distancia / self._velocidad


# --- Prueba ---
camion1 = Camion("TR123", 60, "5 toneladas")
bici1 = Bicicleta("BICI45", 20, "Montaña")

distancia = 100
print(f"Tiempo camión: {camion1.tiempo_viaje(distancia):.2f} horas")
print(f"Tiempo bicicleta: {bici1.tiempo_viaje(distancia):.2f} horas")