from .lugar import lugar

class barrio (object,lugar):
    poblacion=None

    def set_poblacion(self,p):
        self.poblacion=p

    def get_poblacion(self):
        return self.poblacion
