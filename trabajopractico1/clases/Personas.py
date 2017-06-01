class Personas (object):
    dni=None
    nombre=None
    apellido=None
    fechadenacimiento=None

    def setdni(self,dni):
        self.dni=dni

    def setnombre(self,n):
        self.nombre=str(n)

    def setapellido(self,a):
        self.apellido=str(a)

    def setfechadenacimiento(self,f):
        self.fechadenacimiento=f
