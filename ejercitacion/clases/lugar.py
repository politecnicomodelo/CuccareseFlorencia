class lugar (object):
    nombre=""
    codigo=None
    listadecordenadas=[]

    def set_nombre(self,n):
        self.nombre=n

    def set_codigo(self,c):
        self.codigo=c

    def set_cordenada(self,coordenada):
        self.listadecordenadas.append(coordenada)
