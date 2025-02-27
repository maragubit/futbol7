from django.db import models
from jugadores.models import Jugador
from datetime import date, timedelta

# Create your models here.
class Amonestacion(models.Model):
    TARJETAS_CHOICE=(
        ('amarilla','amarilla'),
        ('roja','roja'),
    )
    jugador=models.ForeignKey("jugadores.Jugador",on_delete=models.CASCADE,related_name="amonestaciones")
    tarjeta=models.CharField(max_length=10,choices=TARJETAS_CHOICE, null=True, blank=True)
    fecha=models.DateField(default=date.today)
    fecha_sancion=models.DateField(default=date.today)
    observaciones=models.TextField(null=True,max_length=200,blank=True)

    def __str__(self):
        return ("{} | {} | {} : Sancionado hasta {} ").format(self.fecha,self.jugador,self.tarjeta,self.fecha_sancion)
    
    def save (self,*args,**kwargs):
        if self.tarjeta=="roja":
            self.fecha_sancion=self.fecha+timedelta(days=8)
        return super(Amonestacion,self).save(*args,**kwargs)
