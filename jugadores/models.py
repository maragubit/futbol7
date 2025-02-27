from django.db import models
from django.utils import timezone

# Create your models here.
class Jugador(models.Model):
    
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='jugadores',blank=True,null=True, default='jugador.jpg')
   
    def __str__(self):
            hoy=timezone.now()
            amonestaciones = self.amonestaciones.all()
            amonestado=amonestaciones.filter(fecha_sancion__gt=hoy).order_by("fecha_sancion").last()
            if amonestado:
                 return ('{} SANCIONADO').format(self.nombre)
            return ('{}').format(self.nombre)
    
    def goles_a_favor(self):
        goles=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.all()
            for partido in partidos_local:
                goles+=partido.goles_local
            partidos_visitante=equipo.partidos_visitante.all()
            for partido in partidos_visitante:
                    goles+=partido.goles_visitante
        return goles
    def goles_en_contra(self):
        goles=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.all()
            for partido in partidos_local:
                goles+=partido.goles_visitante
            partidos_visitante=equipo.partidos_visitante.all()
            for partido in partidos_visitante:
                    goles+=partido.goles_local
        return goles
    
    def golaverage(self):
         return self.goles_a_favor()-self.goles_en_contra()

    def puntos(self):
        puntos=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.all()
            for partido in partidos_local:
                if partido.goles_local>partido.goles_visitante:
                     puntos+=3
                elif partido.goles_local==partido.goles_visitante:
                     puntos+=1
            partidos_visitante=equipo.partidos_visitante.all()
            for partido in partidos_visitante:
                if partido.goles_visitante>partido.goles_local:
                     puntos+=3
                elif partido.goles_visitante==partido.goles_local:
                     puntos+=1
        return puntos
    
    def partidos_jugados(self):
        partidos_jugados=self.equipos.count()
        return partidos_jugados
    
    def ratio(self):
        """Calcula el ratio de puntos por partido jugado."""
        ratio=0
        if self.partidos_jugados() == 0:
            return ratio  # Para evitar división por cero
        return self.puntos()/self.partidos_jugados()
    
    def partidos_ganados(self):
        partidos_ganados=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.all()
            for partido in partidos_local:
                if partido.goles_local>partido.goles_visitante:
                     partidos_ganados+=1
            partidos_visitante=equipo.partidos_visitante.all()
            for partido in partidos_visitante:
                if partido.goles_visitante>partido.goles_local:
                     partidos_ganados+=1
        return partidos_ganados
    
    def partidos_perdidos(self):
        partidos_perdidos=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.all()
            for partido in partidos_local:
                if partido.goles_local<partido.goles_visitante:
                     partidos_perdidos+=1
            partidos_visitante=equipo.partidos_visitante.all()
            for partido in partidos_visitante:
                if partido.goles_visitante<partido.goles_local:
                     partidos_perdidos+=1
        return partidos_perdidos
    def sancionado(self):
        hoy=timezone.now()
        amonestaciones = self.amonestaciones.all()
        amonestado=amonestaciones.filter(fecha_sancion__gt=hoy).order_by("fecha_sancion").last()
        if amonestado:
                return ('hasta {} ').format(amonestado.fecha_sancion)
        else:
             return "NO"
    
    def tarjetas_amarillas(self):
        return self.amonestaciones.filter(tarjeta='amarilla').count()
    def tarjetas_rojas(self):
        return self.amonestaciones.filter(tarjeta='roja').count()
            
                   
        