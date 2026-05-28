class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    def estudiar(self):
        print("Mi nombre es : ", self.nombre, "estoy estudiando")

class Trabajador:
    def __init__(self, tiempo):
        self.tiempo= tiempo
    def trabajar(self):
        print("Estoy trabajando: ", self.tiempo)

class EstudianteTrabajador(Estudiante, Trabajador):
    def __init__(self, nombre, edad, tiempo):

        # Inicializar clase Estudiante
        Estudiante.__init__(self, nombre, edad)

        # Inicializar clase Trabajador
        Trabajador.__init__(self, tiempo)
    def rutinas(self):
        self.estudiar()
        self.trabajar()

persona = EstudianteTrabajador("bryan", "20", "medio tiempo")
persona.estudiar()
persona.trabajar()
print("------------")
persona.rutinas()