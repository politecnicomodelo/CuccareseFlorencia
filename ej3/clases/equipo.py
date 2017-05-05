class equipo (object):
    listadejugadores=[]
    disponibilidadhoraria=[]
    nombreequipo=""
    capitan=None
    barrrio=""

    def __init__(self):
        self.listadejugadores=[]

    def __init__(self):
        self.disponibilidadhoraria=[]
        self.disponibilidadhoraria=[[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]


    def agregarjugador(self,jugador):
        self.listadejugadores.append(jugador)

    def agregardisponibildad (self,dia,turno):
        self.disponibilidadhoraria[dia][turno]=True


    def setnombeequipo (self,nombreequipo):
        self.nombreequipo=str(nombreequipo)

    def setbarrio (self,barrio):
        self.barrio=str(barrio)

    def setcapitan (self,capitan):
        self.capitan=capitan
