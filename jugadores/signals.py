from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.dispatch import receiver
from partidos.models import Partido
from partidos.models import Temporada




# 'receiver' escucha el evento post_save, post_delete del modelo Partido
@receiver([post_save, post_delete], sender=Partido)
def actualizar_jugadores(sender, instance, created, **kwargs):
    print(instance.fecha)
    temporada=Temporada.objects.filter(inicio__lte=instance.fecha, fin__gte=instance.fecha).first()
    print(temporada)
    jugadores= instance.equipo_local.jugadores.all() | instance.equipo_visitante.jugadores.all()
    metricas = [
        "goles_a_favor", "goles_en_contra", "golaverage", "puntos",
        "partidos_jugados", "ratio", "partidos_ganados", "partidos_perdidos",
        "sancionados", "tarjetas_amarillas", "tarjetas_rojas"
    ]
    for jugador in jugadores:
        keys = [f"jugador:{jugador.pk}:{metrica}:{temporada.id}" for metrica in metricas]
        cache.delete_many(keys)
        