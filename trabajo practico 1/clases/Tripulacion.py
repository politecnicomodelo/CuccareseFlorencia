from .Personas import Personas
class Tripulante (object,Personas):
    avionespermitidos=[]

    def agregarmodelodeavion(self,a):
        self.avionespermitidos.append(a)
