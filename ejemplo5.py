class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print("Nombre: ", self.nombre, "$: ", self.precio)

class Libro(Producto):

    def __init__(self, nombre, precio, categoria):
        super().__init__(nombre, precio)
        self.categoria= categoria
    def detalles(self):
        print(f"Libro: {self.nombre}, Precio: ${self.precio}, categoria: {self.categoria}")

libro = Libro("Harry Potter", 20, "fantasia")
libro.mostrar()
libro.detalles() 