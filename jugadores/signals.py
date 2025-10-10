from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.dispatch import receiver
from partidos.models import Partido




# 'receiver' escucha el evento post_save, post_delete del modelo Partido
@receiver([post_save, post_delete], sender=Partido)
def actualizar_jugadores(sender, instance, created, **kwargs):
    jugadores= instance.equipo_local.jugadores.all() | instance.equipo_visitante.jugadores.all()
    for jugador in jugadores:
        cache_key_goles_a_favor = f"jugador:{jugador.pk}:goles_a_favor:{instance.equipo_local.temporada_set.first().id}"
        cache_key_goles_en_contra = f"jugador:{jugador.pk}:goles_en_contra:{instance.equipo_local.temporada_set.first().id}"
        cache_key_golaverage = f"jugador:{jugador.pk}:golaverage:{instance.equipo_local.temporada_set.first().id}"
        cache_key_puntos = f"jugador:{jugador.pk}:puntos:{instance.equipo_local.temporada_set.first().id}"
        cache_key_partidos_jugados = f"jugador:{jugador.pk}:partidos_jugados:{instance.equipo_local.temporada_set.first().id}"
        cache_key_ratio = f"jugador:{jugador.pk}:ratio:{instance.equipo_local.temporada_set.first().id}"
        cache_key_partidos_ganados = f"jugador:{jugador.pk}:partidos_ganados:{instance.equipo_local.temporada_set.first().id}"
        cache_key_partidos_perdidos = f"jugador:{jugador.pk}:partidos_perdidos:{instance.equipo_local.temporada_set.first().id}"
        cache_key_sancionados = f"jugador:{jugador.pk}:sancionados:{instance.equipo_local.temporada_set.first().id}"
        cache_key_tarjetas_amarillas = f"jugador:{jugador.pk}:tarjetas_amarillas:{instance.equipo_local.temporada_set.first().id}"
        cache_key_tarjetas_rojas = f"jugador:{jugador.pk}:tarjetas_rojas:{instance.equipo_local.temporada_set.first().id}"
        cache.delete_many([
           cache_key_goles_a_favor,
            cache_key_goles_en_contra,
            cache_key_golaverage,
            cache_key_puntos,
            cache_key_partidos_jugados,
            cache_key_ratio,
            cache_key_partidos_ganados,
            cache_key_partidos_perdidos,
            cache_key_sancionados,
            cache_key_tarjetas_amarillas,
            cache_key_tarjetas_rojas,
           ])