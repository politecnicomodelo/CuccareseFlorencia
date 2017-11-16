from .lugar import lugar

class ciudad(object,lugar):
    listadebarrios= []

    def set_barrio_en_ciudad(self,b):
        self.listadebarrios=b

    def get_poblacion(self,):