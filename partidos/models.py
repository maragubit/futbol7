from django.db import models
from equipos.models import Equipo
from jugadores.models import Jugador
from datetime import date

# Create your models here.

class Partido(models.Model):
    equipo_local=models.ForeignKey('equipos.Equipo',related_name='partidos_local',on_delete=models.CASCADE)
    equipo_visitante=models.ForeignKey('equipos.Equipo',related_name='partidos_visitante',on_delete=models.CASCADE)
    goles_local=models.PositiveIntegerField()
    goles_visitante=models.PositiveIntegerField()
    mvp=models.ForeignKey(Jugador, on_delete=models.SET_NULL, related_name='mvp',null=True)
    fecha=models.DateField(default=date.today)

    def __str__(self):
        return ("Partido del: {}".format(self.fecha))

    