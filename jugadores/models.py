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
    
    def goles_a_favor(self,temporada_id):
        from partidos.models import Temporada
        goles=0
        temporada=Temporada.objects.get(id=temporada_id)
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_local:
                goles+=partido.goles_local
            partidos_visitante=equipo.partidos_visitante.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_visitante:
                    goles+=partido.goles_visitante
        return goles
    def goles_en_contra(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        goles=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_local:
                goles+=partido.goles_visitante
            partidos_visitante=equipo.partidos_visitante.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_visitante:
                    goles+=partido.goles_local
        return goles
    
    def golaverage(self,temporada_id):
         return self.goles_a_favor(temporada_id)-self.goles_en_contra(temporada_id)

    def puntos(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        puntos=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_local:
                if partido.goles_local>partido.goles_visitante:
                     puntos+=3
                elif partido.goles_local==partido.goles_visitante:
                     puntos+=1
            partidos_visitante=equipo.partidos_visitante.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_visitante:
                if partido.goles_visitante>partido.goles_local:
                     puntos+=3
                elif partido.goles_visitante==partido.goles_local:
                     puntos+=1
        return puntos
    
    def partidos_jugados(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        partidos_jugados=self.equipos.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin).count()
        return partidos_jugados
    
    def ratio(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        """Calcula el ratio de puntos por partido jugado."""
        ratio=0
        if self.partidos_jugados(temporada.id) == 0:
            return ratio  # Para evitar división por cero
        return round(self.puntos(temporada.id)/self.partidos_jugados(temporada.id),2)

    def partidos_ganados(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        partidos_ganados=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_local:
                if partido.goles_local>partido.goles_visitante:
                     partidos_ganados+=1
            partidos_visitante=equipo.partidos_visitante.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_visitante:
                if partido.goles_visitante>partido.goles_local:
                     partidos_ganados+=1
        return partidos_ganados
    
    def partidos_perdidos(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        partidos_perdidos=0
        for equipo in self.equipos.all():
            partidos_local=equipo.partidos_local.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
            for partido in partidos_local:
                if partido.goles_local<partido.goles_visitante:
                     partidos_perdidos+=1
            partidos_visitante=equipo.partidos_visitante.filter(fecha__gte=temporada.inicio, fecha__lt=temporada.fin)
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

    def tarjetas_amarillas(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        return self.amonestaciones.filter(tarjeta='amarilla', fecha__range=(temporada.inicio,temporada.fin)).count()
    
    def tarjetas_rojas(self,temporada_id):
        from partidos.models import Temporada
        temporada=Temporada.objects.get(id=temporada_id)
        return self.amonestaciones.filter(tarjeta='roja', fecha__range=(temporada.inicio,temporada.fin)).count()


        