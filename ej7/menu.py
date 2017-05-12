from .clases.Personas import Personas
from .clases.Alumnos import Alumnos
from .clases.Profesor import Profesor
from .clases.Pedido import Pedidos
from .clases.Platos import Platos
from datetime import datetime

listaplatos=[]
listapedidos=[]
listapersonas=[]



def agregaralumno(nombre,apellido,division):
    alumno=Alumnos()
    alumno.setdivision(division)
    alumno.setnombreapellido(nombre,apellido)
    listapersonas.append(alumno)

def agregarprofesor(nombre,apellido,descuento):
    profesor=Profesor()
    profesor.setnombreapellido(nombre,apellido)
    profesor.setdesc(descuento)
    listapersonas.append(profesor)

def agregarplatos (nombre,precio):
    plato=Platos()
    plato.setnombre(nombre)
    plato.setprecio(precio)
    listaplatos.append(plato)

def agregarpedido(fecha,plato,persona):
    pedido=Pedidos()
    pedido.setfecha(fecha)
    pedido.setpersona(persona)
    pedido.setplato(plato)
    listaplatos.append(pedido)

def modificaralumno(dni,nombre,apellido,div):
    for alumno in listapersonas:
        if type(alumno) is Alumnos:
            if alumno.dni==dni:
                alumno.setnombreapellido(nombre,apellido)
                alumno.setdivision(div)

def modificarprofesor(dni,nombre,apellido,des):
    for profesor in listapersonas:
        if type(profesor) is Profesor:
            if profesor.dni==dni:
                profesor.setnombreapellido(nombre,apellido)
                profesor.setdesc(des)

def modificarplato(nombre,precio):
    for plato in listaplatos:
        if plato.nombre==nombre:
            plato.setprecio(precio)

def eliminarpersona(dni):
    for persona in listapersonas:
        if persona.dni==dni:
            listapersonas.remove(persona)

def eliminarplato(nombre):
    for plato in listaplatos:
        if plato.nombre==nombre:
            listaplatos.remove(plato)


def listadepedidos(fecha,):
    listaplatosacocinar=[]
    for pedido in listapedidos:
        if pedido.fechadecreacion==fecha:

def guardarenarchivopersonas():
    p=open("personas.txt","w+")
    for persona in listapersonas:
        p.write(persona.dni)
        p.write("|")
        p.write(persona.nombre)
        p.write("|")
        p.write(persona.apellido)
        p.write("|")
        if type(persona) is Alumnos:
            p.write(persona.division)
        if type(persona) is Profesor:
            p.write(persona.descuento)
        p.write("\n")

def guardarenarchivoplatos():
    p=open("platos.txt","w+")
    for plato in listaplatos:
        p.write(plato.nombre)
        p.write("|")
        p.write(plato.precio)
        p.write("\n")

def guardarenarchivopedidos():
    p=open("pedidos.txt","w+")
    for pedido in listapedidos:
        fecha=pedido.fechadecreacion.datetime.strptime("%d-%m-%Y").date()
        p.write(fecha)
        p.write("|")
        p.write(pedido.plato.nombre)
        p.write("|")
        p.write(pedido.plato.precio)
        p.write("|")
        p.write(pedido.persona.dni)
        p.write("|")
        p.write(pedido.persona.nombre)
        p.write("|")
        p.write(pedido.persona.apellido)
        p.write("|")
        if type(pedido.persona) is Alumnos:
            p.write(pedido.persona.division)
        if type(pedido.persona) is Profesor:
            p.write(pedido.persona.descuento)
        p.write("|")
        p.write(pedido.entregado)
        p.write("\n")

def abrirarchivopersonas():
    p=open("personas.txt","r+")
    for line in p:

