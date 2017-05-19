from .clases.Personas import Personas
from .clases.Pasajeros import Pasajero
from .clases.Tripulacion import Tripulante
from .clases.Aviones import Avion
from .clases.Piloto import Piloto
from .clases.Servicioabordo import Servicioabordo

listadepersonas=[]
listadeaviones=[]
listadevuelos=[]

def listavuelamasdeunavez():
    listavuelamasdeunavez=[]
    fecha=None
    cont=0
    for persona in listadepersonas:
        if type(persona) is Tripulante:
            for vuelo in listadevuelos:
                for tripulante in vuelo.listadetripulantes:
                    if tripulante==persona:
                        fecha=vuelo.fecha

                        for vuelo2 in listadevuelos:
                            for tripulante2 in vuelo2.listadetripulantes:
                                if tripulante2 == persona and vuelo2.fecha == fecha:
                                    cont=cont+1
                        if cont>1 :
                            listavuelamasdeunavez.append(persona)

        cont=0












def cargaraviones():
    a=open("aviones.dat","r")
    for line in a:
        avion = Avion()
        l=line.split("|")
        avion.codunico=l
        l = line.split("|")
        avion.cantdepasajeros=int(l)
        l = line.split("|")
        avion.cantdetripulantes=int(l)
        listadeaviones.append(avion)
    a.close()

def cargarpersonas():
    p=open("personas.dat","r")
    for line in p:
        l=line.split("|")
        if l== "Pasajero":
            pasajero=Pasajero()
            l = line.split("|")
            pasajero.setnombre(l)
            l = line.split("|")
            pasajero.setapellido(l)
            l = line.split("|")
            pasajero.setfechadenacimiento(l)
            l = line.split("|")
            pasajero.setdni(l)
            l = line.split("|")
            pasajero.setvip(l)
            l = line.split("|")
            pasajero.setnecesidades(l)
        if l=="Piloto":
            piloto=Piloto()
            l = line.split("|")
            piloto.setnombre(l)
            l = line.split("|")
            piloto.setapellido(l)
            l = line.split("|")
            piloto.setfechadenacimiento(l)
            l = line.split("|")
            piloto.setdni(l)
            l = line.split("|")
            l=l.split(",")
            for avion in listadeaviones:
                if avion.codunico == l
                    pl


