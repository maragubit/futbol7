from django.shortcuts import render
from django.shortcuts import HttpResponse 
from jugadores.models import Jugador
from partidos.models import Temporada

# Create your views here.

def home (request):
   return render (request, "index.html")

def clasificacion (request):
   jugadores=Jugador.objects.all()
   temporadas=Temporada.objects.all()
   if request.GET.get("temporada"):
      temporada=Temporada.objects.get(id=request.GET.get("temporada"))
   else:
       temporada=Temporada.objects.last()
   jugadores = sorted(Jugador.objects.all(), key=lambda j: (j.puntos(temporada.id), j.golaverage(temporada.id)), reverse=True)
   return render (request, "clasificacion.html",{"jugadores":jugadores,"temporada_id":temporada.id,"temporadas":temporadas})

