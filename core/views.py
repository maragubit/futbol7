from django.shortcuts import render
from django.shortcuts import HttpResponse 
from jugadores.models import Jugador

# Create your views here.

def home (request):
   return render (request, "index.html")

def clasificacion (request):
   jugadores=Jugador.objects.all()
   jugadores = sorted(Jugador.objects.all(), key=lambda j: (j.puntos(), j.golaverage()), reverse=True)
   return render (request, "clasificacion.html",{"jugadores":jugadores})
