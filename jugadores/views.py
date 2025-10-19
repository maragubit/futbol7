from django.shortcuts import render
from django.views.generic.detail import DetailView

from partidos.models import Temporada
from .models import Jugador

# Create your views here.


def jugador_detail(request, pk, *args, **kwargs):
    jugador = Jugador.objects.get(pk=pk)
    temporada_id = request.GET.get("temporada")
    if not temporada_id:
        temporada_id = Temporada.objects.last().id
    print(temporada_id)
    temporadas = Temporada.objects.all()
    temporada = Temporada.objects.get(id=temporada_id)
    return render(request, 'jugador.html', {'jugador': jugador, 'temporadas': temporadas, 'temporada': temporada})