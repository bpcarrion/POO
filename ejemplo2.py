class Perro:

  def __init__(self, name, age):
      self.name = name
      self.age = age      
  #Acciones saludar y despedirse
  def saludar(self):
      print ("Te esta saludando: ", self.name)
    #accion despedirse
  def despedirse(self):
      print ("Con este mensaje me despido", self.name)


class Animal(Perro):

    def __init__(self, name, age, clase):
        #llamar al constructor padre
        super().__init__(name, age)
        self.clase=clase

    def mostrar(self):
    ##  print(f"{self.name}, estudia la carrera de: {self.carrera}")
        print(self.name, "de edad: ",self.age, "pertenece a la clasificacion: ", self.clase)

#fuera de la clase 
#instanciar estudiante
perro=Animal("Boby","6","Mamiferos")
perro.saludar()
perro.mostrar()