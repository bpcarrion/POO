class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
    def obtener(self):
        print("Salario: ", self.salario)

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono
        
    def obtener_salario(self): # Sobrescribe el método padre
        print("Nombre: ", self.nombre, "salario total: ",self.salario+self.bono)

# Uso:
jefe = Gerente("Ana", 5000, 1500)
jefe.obtener()
jefe.obtener_salario()