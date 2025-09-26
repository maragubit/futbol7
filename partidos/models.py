from django.db import models
from equipos.models import Equipo
from jugadores.models import Jugador
import dateutil
import datetime as dt
from dateutil.relativedelta import relativedelta # type: ignore

# Create your models here.
hoy=dt.date.today()
ayer=hoy-relativedelta(days=+1)

class Partido(models.Model):
    equipo_local=models.ForeignKey('equipos.Equipo',related_name='partidos_local',on_delete=models.CASCADE)
    equipo_visitante=models.ForeignKey('equipos.Equipo',related_name='partidos_visitante',on_delete=models.CASCADE)
    goles_local=models.PositiveIntegerField()
    goles_visitante=models.PositiveIntegerField()
    mvp=models.ForeignKey(Jugador, on_delete=models.SET_NULL, related_name='mvp',null=True)
    fecha=models.DateField(default=ayer)

    def __str__(self):
        return ("Partido del: {}".format(self.fecha))
    
class Temporada(models.Model):
    nombre=models.CharField(max_length=100)
    inicio=models.DateField()
    fin=models.DateField()

    def __str__(self):
        return ("Temporada: {}".format(self.nombre))

    