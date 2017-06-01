from .Tripulacion import Tripulante
class Servicioabordo(Tripulante):
    idiomas=[]

    def agregaridioma(self,i):
        self.idiomas.append(i)
