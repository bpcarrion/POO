# ABSTRACCIÓN
class Empleado:
    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    # GET y SET
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, valor):
        if valor > 0:
            self._sueldo = valor

    def calcular_pago(self):
        pass


# HERENCIA
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, sueldo, bono):
        super().__init__(nombre, sueldo)
        self._bono = bono

    def get_bono(self):
        return self._bono

    def set_bono(self, valor):
        self._bono = valor

    # POLIMORFISMO
    def calcular_pago(self):
        return self._sueldo + self._bono


# HERENCIA
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo, horas):
        super().__init__(nombre, sueldo)
        self._horas = horas

    def get_horas(self):
        return self._horas

    def set_horas(self, cantidad):
        self._horas = cantidad

    # POLIMORFISMO
    def calcular_pago(self):
        return self._sueldo * self._horas


# --- Prueba ---
emp1 = EmpleadoTiempoCompleto("Carlos", 1200, 300)
emp2 = EmpleadoPorHoras("Sofía", 10, 40)

print(f"Pago de {emp1.get_nombre()}: ${emp1.calcular_pago()}")
print(f"Pago de {emp2.get_nombre()}: ${emp2.calcular_pago()}")