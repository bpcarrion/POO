# ABSTRACCIÓN: Definimos estructura básica de una cuenta
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    # GET y SET
    def get_titular(self):
        return self._titular

    def set_titular(self, nombre):
        self._titular = nombre

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo

    def mostrar_info(self):
        pass


# HERENCIA: Cuenta de Ahorro
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self._interes = interes

    def get_interes(self):
        return self._interes

    def set_interes(self, valor):
        self._interes = valor

    # POLIMORFISMO
    def mostrar_info(self):
        return f"Cuenta Ahorro: Titular {self._titular}, Saldo: ${self._saldo}, Interés: {self._interes}%"


# HERENCIA: Cuenta Corriente
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self._limite = limite

    def get_limite(self):
        return self._limite

    def set_limite(self, valor):
        self._limite = valor

    # POLIMORFISMO
    def mostrar_info(self):
        return f"Cuenta Corriente: Titular {self._titular}, Saldo: ${self._saldo}, Límite: ${self._limite}"


# --- Prueba ---
cuenta1 = CuentaAhorro("Bryan", 500, 5)
cuenta2 = CuentaCorriente("Luis", 500, 200)

print(cuenta1.mostrar_info())
print(cuenta2.mostrar_info())

cuenta1.set_saldo(1200)
print("Saldo actualizado:", cuenta1.get_saldo())