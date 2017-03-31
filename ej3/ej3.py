from datetime import date
from clases.jugadores import jugadores
from .clases.equipo import equipo
#from clases.partido import partido
#from .lases.torneo import torneo

jugador1=jugadores()
jugador2=jugadores()
jugador3=jugadores()
jugador4=jugadores()

jugador1.setnombre("messi")
jugador2.setnombre("juan")
jugador3.setnombre("pedro")
jugador4.setnombre("pepito")

jugador1.setfechadenacimiento(date(2005,8,10))
jugador2.setfechadenacimiento(date(2010,9,3))
jugador3.setfechadenacimiento(date(1986,4,3))
jugador4.setfechadenacimiento(date(1956,12,1))

jugador1.setnumerodecamiseta(1)
jugador2.setnumerodecamiseta(2)
jugador3.setnumerodecamiseta(3)
jugador4.setnumerodecamiseta(4)

equipo1=equipo()

equipo1.setnombeequipo("Blue")
equipo1.setbarrio("savedra")
equipo1.setcapitan(jugador1)
equipo1.agregarjugador(jugador1)
equipo1.agregarjugador(jugador2)
