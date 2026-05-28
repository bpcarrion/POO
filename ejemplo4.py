#Clase padre
class figura ():

    def __init__(self, base, altura):
        self.base= base
        self.altura= altura

#metodo
    def mostrar(self):
        print("la figura tiene de base: ", self. base, "y de altura: ", self.altura)

class clasifica (figura):
    def __init__(self, base, altura, Nlados):
        #llamamos al constructor padre
        super().__init__(base, altura)
        self.Nlados=Nlados


    #metodo 2
    def clasi(self):
        print("su base es: ", self.base, "y altura: ", self.altura, "su numero de lados es:" , self.Nlados)


fi=clasifica("5", "9", "4")
fi.mostrar()
fi.clasi()
