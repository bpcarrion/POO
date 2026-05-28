# Clase Padre
class Vehiculo:
    # 3 ATRIBUTOS
    def __init__(self, marca, modelo, color):
        self.marca = marca      # Atributo 1
        self.modelo = modelo    # Atributo 2
        self.color = color      # Atributo 3

    # MÉTODO 1
    def mostrar_datos(self):
        print( f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")



# Clase Hija (HERENCIA)
class Moto(Vehiculo):
    # 3 ATRIBUTOS: heredados + 1 nuevo, 
    def __init__(self, marca, modelo, color, cilindrada):
        # Llamamos al constructor de la clase padre
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada  # Atributo propio 
        

    # MÉTODO 2
    def mostrar(self):
        # Usamos el método del padre y agregamos info
    #    print( super().mostrar_datos() + f", Cilindrada: {self.cilindrada} cc")
         print("la marca es: ", self.marca, "su modelo: ",self.modelo, "de color: ", self.color, "el cilindraje ", self.cilindrada, " cc")



vehiculo1 = Vehiculo("Toyota", "Corolla", "Rojo")
vehiculo1.mostrar_datos()


moto1 = Moto("Yamaha", "YZF-R3", "Azul", 300)
moto1.mostrar()
