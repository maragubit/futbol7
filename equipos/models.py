from django.db import models
from jugadores.models import Jugador
from datetime import date

# Create your models here.

class Equipo(models.Model):
    
    COLOR_CHOICES = (
        ('Blanco','blanco'),
        ('Color','color'),
    )
    jugadores=models.ManyToManyField('jugadores.Jugador',related_name='equipos')
    color=models.CharField(max_length=30,choices=COLOR_CHOICES)
    fecha=models.DateField(default=date.today)

    def __str__(self):
        return ("{} ({})").format(self.color,self.fecha)
    
    class Meta():
        ordering=['-id']
    