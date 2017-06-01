from clases.Pasajeros import Pasajero
from clases.Tripulacion import Tripulante
from clases.Aviones import Avion
from clases.Piloto import Piloto
from clases.Servicioabordo import Servicioabordo
from clases.Vuelos import Vuelo
from datetime import datetime

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
    a=open("/home/alumno/Descargas/aviones.dat","r")
    for line in a:
        avion = Avion()
        l=line.split("|")
        avion.setcodigo(l[0])
        avion.setcantidaddepasajeros(int(l[1]))
        avion.setcantidaddetripulantes(int(l[2]))
        listadeaviones.append(avion)
    a.close()

def cargarpersonas():
    p=open("/home/alumno/Descargas/personas.dat","r")
    for line in p:
        l=line.split("|")

        if l[0]== "Pasajero":
            pasajero=Pasajero()
            pasajero.setnombre(l[1])
            pasajero.setapellido(l[2])
            pasajero.setfechadenacimiento(l[3])
            pasajero.setdni(l[4])
            pasajero.setvip(l[5])
            if len(l) == 6:
                pasajero.setnecesidades(l[6])
            else:
                pasajero.setnecesidades(None)
            listadepersonas.append(pasajero)

        if l[0]=="Piloto":
            piloto=Piloto()
            piloto.setnombre(l[1])
            piloto.setapellido(l[2])
            piloto.setfechadenacimiento(l[3])
            piloto.setdni(l[4])
            aux=l[5].split(",")
            for item in aux:
                for avion in listadeaviones:
                    if avion.codunico==item:
                        piloto.agregarmodelodeavion(avion)
            listadepersonas.append(piloto)
        if l[0]=="Servicio":
            servicio=Servicioabordo()
            servicio.setnombre(l[1])
            servicio.setapellido(l[2])
            servicio.setfechadenacimiento(l[3])
            servicio.setdni(l[4])
            aux = l[5].split(",")
            for item in aux:
                for avion in listadeaviones:
                    if avion.codunico == item:
                        servicio.agregarmodelodeavion(avion)

            aux = l[6].split(",")
            servicio.agregaridioma(aux)
            listadepersonas.append(servicio)
    p.close()



def cargarvuelos():
    v= open("/home/alumno/Descargas/vuelos.dat", "r")
    for line in v:
        l = line.split("|")
        vuelo=Vuelo()
        for avion in listadeaviones:
            if avion.codunico==l[0]:
                vuelo.setavion(avion)

        date=datetime.strptime(l[1],"%d-&m-%y").date()
        time=datetime.strptime(l[2],"%i:&M").time()
        vuelo.setfechayhora(date,time)
        vuelo.setorigen(l[3])
        vuelo.setdestino(l[4])
        aux=l[5].split(",")
        for item in aux:
            for persona in listadepersonas:
                if persona.dni == item:
                    vuelo.agregartripulante(persona)
        aux = l[6].split(",")
        for item in aux:
            for persona in listadepersonas:
                if persona.dni == item:
                    vuelo.agregarpasajero(persona)
        listadevuelos.append(vuelo)

    v.close()
def listamasjovenesporvuelo():
    listamasjoven=[]
    for vuelo in listadevuelos:
        aux=vuelo.pasajeromasjoven()
        listamasjoven.append(aux)
    return listamasjoven

def tripulacionmin():
    lista=[]
    for vuelo in listadevuelos:
        aux=vuelo.tripulacionminima()
        if aux==False:
            lista.append(vuelo)
    return lista
def vuelosnoauto():
    lista=[]
    for vuelo in listadevuelos:
        aux=vuelo.tripulacionautorizada()
        if aux==False:
            lista.append(vuelo)
    return lista

def imprimirpersona(listap):
    for persona in listap:
        print(persona.dni)
        print(persona.dni)
def menu():
    cargaraviones()
    cargarpersonas()
    for per in listadepersonas:
        if type(per) is Piloto:
            print(per.nombre)
            print(per.avionespermitidos[0].codunico)

menu()