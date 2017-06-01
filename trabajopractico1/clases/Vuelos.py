from datetime import date
class Vuelo(object):
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

    def nominadepersonas(self):
        listadepersonas=[]
        for item in self.listadepasajeros:
            listadepersonas.append(item)
        for item in self.listadetripulantes:
            listadepersonas.append(item)

        return listadepersonas

    def pasajeromasjoven(self):
        fecha=self.listadepasajeros[0].fechadenacimiento
        pasajeroaux=None
        for pasajero in self.listadepasajeros:
            if fecha < pasajero.fechadenacimiento:
                fecha=pasajero.fechadenacimiento
                pasajeroaux=pasajero
        return pasajeroaux

    def tripulacionminima(self):
        sepuedevolar=True
        if len(self.listadetripulantes)< self.avion.cantdetripulantes:
            sepuedevolar=False
        return sepuedevolar

    def tripulacionautorizada(self):
        tripulancionautorizada=False
        for tripulante in self.listadetripulantes:
            for avion in tripulante.avionespermitidos:
                if self.avion==avion:
                   tripulancionautorizada=True
            if tripulancionautorizada!=True:
                return tripulancionautorizada

        return tripulancionautorizada

    def personasvipoespeciales(self):
        lista=[]
        for pasajero in self.listadepasajeros:
            if pasajero.vip == True or pasajero.necesidadesespeciales!=None:
                lista.append(pasajero)

        return lista