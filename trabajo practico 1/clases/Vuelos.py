class vuelo(object):
    avion=None
    listadepasajeros=[]
    listadetripulantes=[]
    fecha=None
    hora=None
    origen=None
    destino=None

    def setavion(self,a):
        self.avion=a

    def agregarpasajero(self,p):
        self.listadepasajeros.append(p)

    def agregartripulante(self,t):
        self.listadetripulantes.append(t)

    def setfechayhora(self,f,h):
        self.fecha=f
        self.hora=h

    def setorigen(self,o):
        self.origen=o

    def setdestino(self,d):
        self.destino=d

