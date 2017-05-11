from .clases.Personas import Personas
from .clases.Alumnos import Alumnos
from .clases.Profesor import Profesor
from .clases.Pedido import Pedidos
from .clases.Platos import Platos

platos=[]
pedidos=[]
personas=[]

def agregaralumno(nombre,apellido,division):
    alumno=Alumnos()
    alumno.setdivision(division)
    alumno.setnombreapellido(nombre,apellido)
    personas.append(alumno)

def agregarprofesor(nombre,apellido,descuento):
    profesor=Profesor()
    profesor.setnombreapellido(nombre,apellido)
    profesor.setdesc(descuento)
    personas.append(profesor)


