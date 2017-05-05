class torneo (object):
    listadeequipos=[]
    listadepartidos=[]

    def agregarequipo (self,equipo):
        if equipo in self.listadeequipos:
            return false
        self.listadeequipos.append(equipo)
        return true



    #def organizarfixture(self):