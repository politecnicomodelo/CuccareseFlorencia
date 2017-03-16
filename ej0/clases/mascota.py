class mascota (object):
    nombre=""
    tipo=""

    def setnombre(self,n):
        self.nombre=str(n)

    def settipo (self,t):
        self.tipo=str(t)

    def quiensoy (self):
        return "soy "+self.nombre+" un "+self.tipo
