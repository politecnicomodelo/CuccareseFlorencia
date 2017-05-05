from .Personas import Personas
class Profesor (object,Personas):
    descuento=None

    def setdesc(self,des):
        self.descuento=des

    def getdesc(self):
        return self.descuento