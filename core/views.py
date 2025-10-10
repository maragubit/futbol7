from django.shortcuts import render
from django.shortcuts import HttpResponse 
from jugadores.models import Jugador
from jugadores.templatetags.jugadores_methods import partidos_jugados
from partidos.models import Temporada

# Create your views here.

def home (request):
   return render (request, "index.html")

def clasificacion (request):
   temporadas=Temporada.objects.all()
   if request.GET.get("temporada"):
      temporada=Temporada.objects.get(id=request.GET.get("temporada"))
   else:
       temporada=Temporada.objects.last()
       
   jugadores = [j for j in Jugador.objects.all() if j.partidos_jugados(temporada.id) > 0]
   jugadores = sorted(jugadores, key=lambda j: (j.puntos(temporada.id), j.golaverage(temporada.id)), reverse=True)
   return render (request, "clasificacion.html",{"jugadores":jugadores,"temporada_id":temporada.id,"temporadas":temporadas})

