# ABSTRACCIÓN
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    # GET y SET
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, valor):
        if valor > 0:
            self._precio = valor

    def precio_final(self):
        pass


# HERENCIA
class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def get_talla(self):
        return self._talla

    def set_talla(self, nueva_talla):
        self._talla = nueva_talla

    # POLIMORFISMO
    def precio_final(self):
        # Ropa tiene 10% de descuento
        return self._precio * 0.90


# HERENCIA
class Electronico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self._garantia = garantia

    def get_garantia(self):
        return self._garantia

    def set_garantia(self, tiempo):
        self._garantia = tiempo

    # POLIMORFISMO
    def precio_final(self):
        # Electrónica tiene 15% de impuesto
        return self._precio * 1.15


# --- Prueba ---
camisa = Ropa("Camisa", 20, "M")
telefono = Electronico("Celular", 500, "1 año")

print(f"Precio final {camisa.get_nombre()}: ${camisa.precio_final():.2f}")
print(f"Precio final {telefono.get_nombre()}: ${telefono.precio_final():.2f}")