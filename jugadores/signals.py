from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.dispatch import receiver
from partidos.models import Partido
from django_redis import get_redis_connection



# 'receiver' escucha el evento post_save, post_delete del modelo Partido
@receiver([post_save, post_delete], sender=Partido)
def actualizar_jugadores(sender, instance, created, **kwargs):
    jugadores= instance.equipo_local.jugadores.all() | instance.equipo_visitante.jugadores.all()
    redis_conn = get_redis_connection("default")
    for jugador in jugadores:
        pattern = f"jugador:{jugador.pk}:*"
        redis_conn.delete_pattern(pattern)
        