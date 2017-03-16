class alumno (object):
    nombre=""
    apellido=""
    fechan=None
    listanotas=[]

    def setnombre(self,n):
        self.nombre=str(n)
    def setapellido(self,a):
        self.apellido=str(a)
    def setfechan(self,f):
        self.fechan=str(f)
    def agregarnota(self,nota):
        self.listanotas.append(nota)

