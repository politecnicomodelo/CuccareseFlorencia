class equipo (object):
    listadejugadores=[]
    disponibilidadhoraria=[]
    nombreequipo=""
    capitan=None
    barrrio=""

    def agregarjugador(self,jugador):
        self.listadejugadores.append(jugador)

    #def agregardisponibildad (self):

    def setnombeequipo (self,nombreequipo):
        self.nombreequipo=str(nombreequipo)

    def setbarrio (self,barrio):
        self.barrio=str(barrio)

    def setcapitan (self,capitan):
        self.capitan=capitan
