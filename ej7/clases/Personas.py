class Personas(object):
    dni=None
    nombre=""
    apellido=""


    def setnombreapellido(self,nombre,apellido):
        self.nombre=str(nombre)
        self.apellido=str(apellido)

    def setdni(self,dni):
        self.dni=dni

    def getdesc(self):
        return 0
