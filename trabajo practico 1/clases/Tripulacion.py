from .Personas import Personas
class tripulante (object,Personas):
    avionespermitidos=[]

    def agregarmodelodeavion(self,a):
        self.avionespermitidos.append(a)
