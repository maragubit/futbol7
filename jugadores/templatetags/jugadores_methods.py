from django import template

register = template.Library()

@register.filter
def puntos(jugador, temporada_id):
    """
    Devuelve los puntos del jugador en la temporada indicada.
    Uso en template: {{ jugador|puntos:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.puntos(temporada_id)
    return ""
@register.filter
def partidos_jugados(jugador, temporada_id):
    """
    Devuelve los partidos jugados del jugador en la temporada indicada.
    Uso en template: {{ jugador|partidos_jugados:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.partidos_jugados(temporada_id)
    return ""
@register.filter
def partidos_ganados(jugador, temporada_id):
    """
    Devuelve los partidos ganados del jugador en la temporada indicada.
    Uso en template: {{ jugador|partidos_ganados:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.partidos_ganados(temporada_id)
    return ""
@register.filter
def partidos_perdidos(jugador, temporada_id):
    """
    Devuelve los partidos perdidos del jugador en la temporada indicada.
    Uso en template: {{ jugador|partidos_perdidos:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.partidos_perdidos(temporada_id)
    return ""
@register.filter
def ratio(jugador, temporada_id):
    """
    Devuelve el ratio de puntos por partido jugado del jugador en la temporada indicada.
    Uso en template: {{ jugador|ratio:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.ratio(temporada_id)
    return ""
@register.filter
def goles_a_favor(jugador, temporada_id):
    """
    Devuelve los goles a favor del jugador en la temporada indicada.
    Uso en template: {{ jugador|goles_a_favor:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.goles_a_favor(temporada_id)
    return ""
@register.filter
def goles_en_contra(jugador, temporada_id):
    """
    Devuelve los goles en contra del jugador en la temporada indicada.
    Uso en template: {{ jugador|goles_en_contra:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.goles_en_contra(temporada_id)
    return ""
@register.filter
def golaverage(jugador, temporada_id):
    """
    Devuelve el golaverage del jugador en la temporada indicada.
    Uso en template: {{ jugador|golaverage:temporada_id }}
    """
    if jugador and temporada_id:
        return jugador.golaverage(temporada_id)
    return ""
@register.filter
def mvp_count(jugador,temporada_id):
    """
    Devuelve el número de veces que el jugador ha sido MVP.
    Uso en template: {{ jugador|mvp_count }}
    """
    from partidos.models import Temporada
    temporada=Temporada.objects.get(id=temporada_id)
    jugador=jugador.mvp.filter(fecha__range=(temporada.inicio,temporada.fin))
    if jugador:
        return jugador.count()
    return 0

@register.filter
def tarjetas_amarillas(jugador, temporada_id):
    """
    Devuelve el número de tarjetas amarillas del jugador.
    Uso en template: {{ jugador|tarjetas_amarillas }}
    """
    if jugador:
        return jugador.tarjetas_amarillas(temporada_id)
    return 0

@register.filter
def tarjetas_rojas(jugador, temporada_id):
    """
    Devuelve el número de tarjetas rojas del jugador.
    Uso en template: {{ jugador|tarjetas_rojas }}
    """
    if jugador:
        return jugador.tarjetas_rojas(temporada_id)
    return 0