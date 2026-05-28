class Perro:
    def __init__(self, nombre, sonido):
        self.nombre= nombre
        self.sonido= sonido
    def realiza(self):
        print("Mi nombre es : ", self.nombre, "sonido que realiza", self.sonido)

class Animal:
    def __init__(self, raza):
        self.raza= raza
    def pertenecer(self):
        print("pertenezco a la raza: ", self.raza)

class Mascota(Perro, Animal):
    def __init__(self, nombre, sonido, raza):

        # Inicializar clase Estudiante
        Perro.__init__(self, nombre, sonido)

        # Inicializar clase Trabajador
        Animal.__init__(self, raza)
    def rutinas(self):
        self.realiza()
        self.pertenecer()

persona = Mascota("boby", "guauu guauuu", "pitbull")
persona.realiza()
persona.pertenecer()
print("------------")
persona.rutinas()