class Electrodomestico:
    def __init__(self, consumo, precio):
        self.consumo = consumo
        self.precio = precio
# metodo 1
    def costo(self):
        print("El Precios es: ", self.precio)

class Lavadora(Electrodomestico):
    def __init__(self, consumo, precio, carga_maxima):
        super().__init__(consumo, precio)
        self.carga_maxima = carga_maxima
    #metodo 2    
    def lavar(self):
        print("Su consumo es: ",self.consumo, "con una capacidad en kilos de: ", self.carga_maxima, "Su precio final es: ", self.precio)

# llamamos a los metodos
electr = Lavadora("A", 400, 8)
electr.costo()
electr.lavar()