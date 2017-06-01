from .Personas import Personas
class Tripulante (Personas):
    avionespermitidos=[]

    def agregarmodelodeavion(self,a):
        self.avionespermitidos.append(a)
