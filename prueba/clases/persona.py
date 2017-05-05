from .registro import registro
from datetime import date
class persona (object,registro):
    nombre=""
    apellido=""
    fechan=None
    registroalturapeso=[]

    def __init__(self):
        self.registroalturapeso=[]

    def setnombre (self,n):
        self.nombre=n

    def setapellido(self,ap):
        self.apellido=ap

    def setfechan (self,fecha):
        self.fechan=fecha

    def setregistro(self,r):
        self.registroalturapeso.append(r)

    def buscarpesoaltura(self,fecha):
        for item in self.registroalturapeso:
            if item.fecharegistro == fecha:
                return item
        return False

    def promediopesoaltura (self,op,año):
        if op ==1:
            aux1=0
            aux2=None
            promedio=0
            for item in self.registroalturapeso:
                if item.year() == año:
                   aux1=aux1+1
                   aux2=item.peso+aux2

             promedio=aux2/aux1
             return promedio

        if op==2:
            aux1 = 0
            aux2 = None
            promedio = 0

            for item in self.registroalturapeso:
                if item.fecharegistro.year() == año:
                    aux1 = aux1 + 1
                    aux2 = item.altura + aux2
            promedio = aux2 / aux1
            return promedio

    def porcentajedecrecimiento(self,an1,an2):
        new_date1.date(an1,12,30)
        new_date2.date(an2,12,30)



        