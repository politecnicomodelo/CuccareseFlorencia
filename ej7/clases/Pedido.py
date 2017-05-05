class Pedidos(object):
    fechadecreacion=None
    plato=None
    persona=None
    entregado=False

    def setfecha(self,f):
        self.fechadecreacion=f

    def setplato(self,pl):
        self.plato=pl

    def setpersona(self,per):
        self.persona=per

    def pedidoentregado(self):
        self.entregado=True