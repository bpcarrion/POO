class celular:
    def __init__(self, color,marca):
        self.color = color
        self.marca = marca
        
    #Metodos o acciones 
    def encender(self):
        print("el color del celular es", self.color, "La marca es", self.marca)
        
    #Fuera de la clase
    #Instanciar la clase   
    
celu=celular("dorado", "tecno")
celu.encender()

class estuche(celular):
    def __init__(self, color, marca, modelo):
        #llamar al constructor padre
        super().__init__(color, marca)
        self.modelo= modelo
    def mostrar(self):
        print(f"el celular es color:{self.color} la marca es: {self.marca} el modelo es: {self.modelo}")

cel=estuche("gris", "xiaomi", "antigolpes")

cel.encender()
cel.mostrar()