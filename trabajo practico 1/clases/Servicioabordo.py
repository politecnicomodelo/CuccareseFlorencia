from .Tripulacion import Tripulante
class Servicioabordo(object,Tripulante):
    idiomas=[]

    def agregaridioma(self,i):
        self.idiomas.append(i)
