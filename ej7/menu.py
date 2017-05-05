from .clases.Personas import Personas
from .clases.Alumnos import Alumnos
from .clases.Profesor import Profesor
from .clases.Pedido import Pedidos
from .clases.Platos import Platos

platos=[]
pedidos=[]
personas=[]

def agregaralumno(nombre,apellido):
    alumno=Alumnos(nombre,apellido)
    personas.append(alumno)
